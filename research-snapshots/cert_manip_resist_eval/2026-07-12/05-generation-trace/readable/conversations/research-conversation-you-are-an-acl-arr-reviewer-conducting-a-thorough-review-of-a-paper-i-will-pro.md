# Research conversation: You are an ACL ARR reviewer conducting a thorough review of a paper. I will provide you all the information you need. Yo

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a95da934c42f8700a.jsonl`
- **Structured JSON:** [`7bf7ffaa54573208f292.json`](../../sessions/7b/7bf7ffaa54573208f292.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-21T13:51:45.023Z_

You are an ACL ARR reviewer conducting a thorough review of a paper. I will provide you all the information you need. Your job is to produce a detailed review report in the exact format I specify at the end.

## Paper Information

**Title**: Cross-Lingual Correctness Probe Transfer Reveals Architecture-Dependent Depth Effects: Distributional Matching Fails but Linear Projection Succeeds

**Venue**: EACL via ACL Rolling Review (ARR)

**Paper length**: 10 pages + 2 pages references (12 total). No appendix.

## Paper Content Summary

The paper presents the first large-scale study of cross-lingual correctness probe transfer across 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), 20 languages spanning 4 resource tiers, and multiple transfer methods.

**Key findings:**
1. A depth-transferability Pareto tradeoff that is architecture-dependent — 9/20 languages show significant negative depth-transfer correlation on Qwen3 vs 5/20 on Llama4, 7/20 on Gemma4. The tradeoff is linked to CKA cliff slope: steeper CKA decline → stronger Pareto.
2. Simpson's Paradox in CKA-transfer relationship: raw Spearman ρ between CKA and transfer AUROC is negative (−0.24 to −0.30, p<0.001), but partial correlation controlling for depth is positive in 2/3 architectures (Llama4: ρ=+0.31, p=0.012; Gemma4: ρ=+0.24, p=0.038; Qwen3: ρ=+0.16, p=0.072 — NOT significant).
3. CaCLR (MMD-based consistency loss) is inert across a full β sweep (0.001-1.0). CORAL and high-dimensional MMD variants also fail. Geometric explanation: CaCLR reduces MMD distance (marginal alignment) but leaves the correctness subspace angle unchanged. This is grounded in Zhao et al. (2019) theory.
4. Linear projection with ~80 parallel pairs achieves 95% of maximum improvement (+3.0pp with 200 pairs). Procrustes effect reversal: languages with ZS AUROC > 0.65 are *harmed* by projection (−1.5pp mean); threshold ~0.57.
5. Probing controls (Hewitt & Liang 2019) reveal 22% of language-layer combinations are capacity artifacts, concentrated in LOW-resource shallow layers (80% artifact rate at 0-25% depth for LOW tier).

**Additional experiments:**
- Difficulty decomposition: Projecting out difficulty direction improves MID-resource languages (+2-3pp) but harms LOW-resource ones. Prescriptive accuracy only 56% (barely above 50% chance). Presented as descriptive, not prescriptive.
- Cross-lingual orthogonality: Correctness-confidence cosine similarity is 0.04 overall, 17/20 languages below 0.10. Architecture-independent.
- LR vs MLP: LR has +2.1pp lower EN AUROC but +3pp better ZS transfer. LR's single-hyperplane constraint forces language-agnostic features.
- Cross-benchmark generalization: Belebele (RC) and MMLU-ProX confirm all qualitative findings. Cross-benchmark language ranking ρ = 0.89.
- Quantization validation: All |ΔAUROC| < 0.015, CKA > 0.97.
- Extended language coverage: 52 languages, rank correlation with 20-lang results = 0.95. VERY-LOW resource languages have 45% artifact rate.

**Paper structure**: Abstract, Introduction, Related Work, Method (3.1-3.5), Experiments (4.1-4.12), Discussion, Conclusion. 16 tables. **Zero figures.**

## Experiment Coverage Assessment

The full experiment plan had 13 experiments (plan_001 through plan_013). ALL 13 are covered in the paper:
- plan_001 (Qwen3 Pareto): ✅ Section 4.1
- plan_002 (Llama4 Pareto): ✅ Section 4.1
- plan_003 (CaCLR negative result): ✅ Section 4.3
- plan_004 (Difficulty decomposition): ✅ Section 4.6
- plan_005 (Orthogonality): ✅ Section 4.7
- plan_006 (LR vs MLP): ✅ Section 4.8
- plan_007 (Belebele + MMLU-ProX): ✅ Section 4.9
- plan_008 (Gemma 4 Dense): ✅ Section 4.1
- plan_009 (52 languages): ✅ Section 4.12
- plan_010 (Quantization validation): ✅ Section 4.11
- plan_011 (CKA + Simpson's): ✅ Section 4.2
- plan_012 (Linear projection sensitivity): ✅ Section 4.5
- plan_013 (Probing controls): ✅ Section 4.10

Coverage: 13/13 (100%).

## ARR Scoring Scale (as of Feb 2025)

**Soundness** (1-5):
- 5 = Excellent: one of the most thorough studies
- 4 = Strong: sufficient support for all claims
- 3 = Acceptable: sufficient support for main claims
- 2 = Weak: some claims not well-supported
- 1 = Poor: major issues

**Excitement** (1-5):
- 5 = Transformative
- 4 = Exciting
- 3 = Interesting
- 2 = Uninspiring
- 1 = Not exciting

**Overall Assessment** (1-5):
- 5 = Strong Accept
- 4 = Accept
- 3 = Borderline
- 2 = Reject
- 1 = Strong Reject

## Your Task

Write a thorough, fair, and constructive review. Your review MUST be structured exactly as follows (use these exact headers):

```
## Summary
[2-3 paragraph summary of the paper's contributions]

## Strengths
[Numbered list of major strengths, each with explanation]

## Weaknesses
[Numbered list of major weaknesses, each with explanation]

## Questions for Authors
[Numbered list of clarifying questions]

## Minor Issues
[Bulleted list of minor presentation/writing issues]

## Missing References
[Any relevant work not cited, or "None identified."]

## Ethical Considerations
[Any ethical concerns, or "No concerns."]

## Scores
- **Soundness**: X/5 — [one-line justification]
- **Excitement**: X/5 — [one-line justification]
- **Overall Assessment**: X/5 — [one-line justification]
- **Confidence**: X/5 — [self-assessed confidence in this review]

## Meta-Review Assessment
[1 paragraph: overall verdict, what would move the score up/down, recommendation]
```

Be specific and cite exact numbers from the paper. Do not be generic. Focus on:
1. Whether claims are well-supported by evidence
2. Whether effect sizes are meaningful
3. Methodological soundness
4. Presentation quality (especially the lack of figures)
5. Novelty relative to existing work
6. Practical impact

Return ONLY the review text, no preamble.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "daded219-2295-49e3-ac22-87f6bbbc54c9",
  "agentId": "a95da934c42f8700a",
  "type": "user",
  "uuid": "3b7e8256-a0eb-4eff-a5c8-4995cd7bfb2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T13:51:45.029Z_

```json
{
  "parentUuid": "3b7e8256-a0eb-4eff-a5c8-4995cd7bfb2d",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
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
  "uuid": "ee4c45a9-344f-477d-8030-4d35c2bc7ec7",
  "timestamp": "2026-05-21T13:51:45.029Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T13:51:48.348Z_



I need to read the actual paper and supporting materials to write a thorough review. Let me start by finding and reading the paper and related files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee4c45a9-344f-477d-8030-4d35c2bc7ec7",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpj4fCbM15WDB43LCyR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b89fcd6-40b9-40e8-9d1f-64e7c78121aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VdK1dHQDZHyTpt3ViTCYh3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16188,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16188,
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

_source line 4 · 2026-05-21T13:51:49.238Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KZB8fRHVAzho5vYCegzdm1`</summary>

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
  "parentUuid": "6b89fcd6-40b9-40e8-9d1f-64e7c78121aa",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpj4fCbM15WDB43LCyR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e4f332c-d388-4fbc-8b6a-0462abd9990c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VdK1dHQDZHyTpt3ViTCYh3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16188,
      "cache_read_input_tokens": 0,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16188
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 136,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16188,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16188,
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

_source line 5 · 2026-05-21T13:51:49.242Z_

<details><summary>↩ Tool result · `toolu_01KZB8fRHVAzho5vYCegzdm1`</summary>

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
  "parentUuid": "3e4f332c-d388-4fbc-8b6a-0462abd9990c",
  "isSidechain": true,
  "promptId": "daded219-2295-49e3-ac22-87f6bbbc54c9",
  "agentId": "a95da934c42f8700a",
  "type": "user",
  "uuid": "09d1262f-3cf4-4561-bf0f-b16f338a1fda",
  "sourceToolAssistantUUID": "3e4f332c-d388-4fbc-8b6a-0462abd9990c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-21T13:51:51.844Z_



Let me read the paper and supporting materials to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09d1262f-3cf4-4561-bf0f-b16f338a1fda",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpjNxnfgWZMdH6k62yk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ac737db-f68a-4848-871d-824c5d846987",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Sr7PP67UthdqRwDWnJKrV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1458,
      "cache_read_input_tokens": 16188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1458,
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

_source line 7 · 2026-05-21T13:51:52.329Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_018JAfdtiZkKHwwTVQgigTTK`</summary>

```json
{
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ac737db-f68a-4848-871d-824c5d846987",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpjNxnfgWZMdH6k62yk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a17d9ab0-18b2-4d0c-9a67-b2dec480d4e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Sr7PP67UthdqRwDWnJKrV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1458,
      "cache_read_input_tokens": 16188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1458,
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

_source line 8 · 2026-05-21T13:51:52.383Z_

<details><summary>↩ Tool result · `toolu_018JAfdtiZkKHwwTVQgigTTK`</summary>

```text
{"result":"# 项目 xling_calib_direction 概况\n\n## 实验状态 (9 个)\n\n- **plan_001**: RUNNING — \n- **plan_002_v3**: DONE (killed) — \n- **plan_002_4gpu**: DONE (failed) — \n- **plan_013_probing_controls_v2**: DONE (failed) — \n- **plan_002**: DONE (failed) — \n- **plan_013**: DONE (success) — \n- **mvp_003**: DONE (success) — \n- **mvp_001**: DONE (success) — \n- **mvp_002**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| plan_001 | Cross-lingual correctness direction transfers across languages in Qwen3-235B-A22B (94-layer MoE, GPTQ-Int4): English-trained linear probes at 24 probed layers (every 4th + final layer 93) will transfer to 19 non-English languages with AUROC ≥ 0.58 for ≥15/19 languages at best layer, with depth-dependent transfer pattern. 235B MoE architecture with 22B active params provides scale contrast to 7-8B dense models (mvp_001/003). | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan_002_v3** (killed): Cross-lingual correctness direction transfers across languages in Llama 4 Scout (48-layer MoE, W4A16): English-trained linear probes at 13 probed layers (0,4,8,...,44,47) will transfer to 19 non-English languages with AUROC ≥ 0.58 for ≥15/19 languages at best layer, with depth-dependent transfer pattern (shallow→deep ΔAUROC ≥ 5pp). MoE architecture with 17B active params provides architectural contrast to dense Qwen models. Retry after killing Qwen3 dry run (PID 482839) that was occupying GPU 1-3. ← 基于 plan_002_4gpu\n- **plan_002_4gpu** (failed): Cross-lingual correctness direction transfers across languages in Llama 4 Scout (48-layer MoE, W4A16): English-trained linear probes at 13 probed layers (0,4,8,...,44,47) will transfer to 19 non-English languages with AUROC ≥ 0.58 for ≥15/19 languages at best layer, with depth-dependent transfer pattern (shallow→deep ΔAUROC ≥ 5pp). MoE architecture with 17B active params provides architectural contrast to dense Qwen models. Retry of plan_002 with 4 GPUs (single-GPU OOM confirmed by dry-run). ← 基于 plan_002\n- **plan_013_probing_controls_v2** (failed): —\n\n## 趋势\n成功 4 / 负向 0 / 失败 3 / 共 8\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-13176: 无 GPU 信息\n\n## 告警\n- plan_013_probing_controls_v2: 训练失败 — unknown\n- plan_002: 训练失败 — unknown\n- plan_002_4gpu: 训练失败 — unknown\n- plan_002_v3: 已被终止 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a17d9ab0-18b2-4d0c-9a67-b2dec480d4e4",
  "isSidechain": true,
  "promptId": "daded219-2295-49e3-ac22-87f6bbbc54c9",
  "agentId": "a95da934c42f8700a",
  "type": "user",
  "uuid": "b6f34810-9392-49a8-b757-f4faf3ab7710",
  "sourceToolAssistantUUID": "a17d9ab0-18b2-4d0c-9a67-b2dec480d4e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T13:51:53.290Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Lg7qvxhMFDXPXSUZz48Yyd`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6f34810-9392-49a8-b757-f4faf3ab7710",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpjNxnfgWZMdH6k62yk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f664588f-9244-40bb-8c79-78990cd1ba20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Sr7PP67UthdqRwDWnJKrV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1458,
      "cache_read_input_tokens": 16188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1458,
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

_source line 10 · 2026-05-21T13:51:53.310Z_

<details><summary>↩ Tool result · `toolu_01Lg7qvxhMFDXPXSUZz48Yyd`</summary>

```text
artifacts/dream_reports/dream_20260520T185641/best/paper.tex
artifacts/dream_reports/dream_20260520T185641/median/paper.tex
artifacts/dream_reports/dream_20260520T185641/worst/paper.tex
artifacts/dream_reports/dream_20260520T201854/best/paper.tex
artifacts/dream_reports/dream_20260520T201854/median/paper.tex
artifacts/dream_reports/dream_20260520T201854/worst/paper.tex
artifacts/dream_reports/dream_20260521T032808/best/paper.tex
artifacts/dream_reports/dream_20260521T032808/median/paper.tex
artifacts/dream_reports/dream_20260521T032808/worst/paper.tex
docs/paper/acl_latex.tex
artifacts/_project/paper/method.tex
artifacts/dream_reports/dream_20260521T044911/best/paper.tex
artifacts/dream_reports/dream_20260521T044911/median/paper.tex
artifacts/dream_reports/dream_20260521T044911/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/introduction_d6b9b9.tex
docs/paper/introduction.tex
docs/paper/experiments.tex
docs/paper/method.tex
docs/paper/related_work.tex
artifacts/dream_reports/dream_20260521T122458/best/paper.tex
artifacts/dream_reports/dream_20260521T122458/median/paper.tex
artifacts/dream_reports/dream_20260521T122458/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f664588f-9244-40bb-8c79-78990cd1ba20",
  "isSidechain": true,
  "promptId": "daded219-2295-49e3-ac22-87f6bbbc54c9",
  "agentId": "a95da934c42f8700a",
  "type": "user",
  "uuid": "6b655730-51fd-4d56-82f4-aa9446e1a838",
  "sourceToolAssistantUUID": "f664588f-9244-40bb-8c79-78990cd1ba20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T13:51:53.456Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01AMKhk74EYvHW3R1w1KqKGw`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b655730-51fd-4d56-82f4-aa9446e1a838",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpjNxnfgWZMdH6k62yk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "addd8f82-fa0f-48ba-b514-47af7ce83855",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Sr7PP67UthdqRwDWnJKrV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1458,
      "cache_read_input_tokens": 16188,
      "output_tokens": 253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1458
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 253,
          "cache_read_input_tokens": 16188,
          "cache_creation_input_tokens": 1458,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1458,
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

_source line 12 · 2026-05-21T13:51:53.467Z_

<details><summary>↩ Tool result · `toolu_01AMKhk74EYvHW3R1w1KqKGw`</summary>

```text
artifacts/dream_reports/dream_20260520T185641/best/paper.pdf
artifacts/dream_reports/dream_20260520T185641/median/paper.pdf
artifacts/dream_reports/dream_20260520T185641/worst/paper.pdf
artifacts/dream_reports/dream_20260520T201854/best/paper.pdf
artifacts/dream_reports/dream_20260520T201854/median/paper.pdf
artifacts/dream_reports/dream_20260520T201854/worst/paper.pdf
artifacts/dream_reports/dream_20260521T032808/best/paper.pdf
artifacts/dream_reports/dream_20260521T032808/median/paper.pdf
artifacts/dream_reports/dream_20260521T032808/worst/paper.pdf
artifacts/dream_reports/dream_20260521T044911/best/paper.pdf
artifacts/dream_reports/dream_20260521T044911/median/paper.pdf
artifacts/dream_reports/dream_20260521T044911/worst/paper.pdf
artifacts/dream_reports/dream_20260521T122458/best/paper.pdf
artifacts/dream_reports/dream_20260521T122458/median/paper.pdf
artifacts/dream_reports/dream_20260521T122458/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "addd8f82-fa0f-48ba-b514-47af7ce83855",
  "isSidechain": true,
  "promptId": "daded219-2295-49e3-ac22-87f6bbbc54c9",
  "agentId": "a95da934c42f8700a",
  "type": "user",
  "uuid": "5fc3f33f-2280-466b-bfa5-e637fa212667",
  "sourceToolAssistantUUID": "addd8f82-fa0f-48ba-b514-47af7ce83855",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-21T13:51:56.798Z_

Let me read the latest paper version (the most recent dream report's best paper).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fc3f33f-2280-466b-bfa5-e637fa212667",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpjgq5LGMsHYGGnoGbR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0f830f9-4d3d-401b-8262-cd0a31ee6ecf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YCd9TDM7p9G3889Z6SXny",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2097,
      "cache_read_input_tokens": 17646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2097,
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

_source line 14 · 2026-05-21T13:51:57.274Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YW5fTDETb85JcSagRiy6d4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0f830f9-4d3d-401b-8262-cd0a31ee6ecf",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpjgq5LGMsHYGGnoGbR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba36d988-579a-4db2-becd-01aa120bda04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YCd9TDM7p9G3889Z6SXny",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2097,
      "cache_read_input_tokens": 17646,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2097
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 17646,
          "cache_creation_input_tokens": 2097,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2097,
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

_source line 15 · 2026-05-21T13:51:57.282Z_

<details><summary>↩ Tool result · `toolu_01YW5fTDETb85JcSagRiy6d4`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{array}
12	\usepackage{tabularx}
13	\usepackage{subcaption}
14	\usepackage[numbers]{natbib}
15	\usepackage{hyperref}
16	
17	\newcommand{\pp}{\,\text{pp}}
18	\newcommand{\caclr}{CaCLR}
19	
20	\title{Cross-Lingual Correctness Probes Reveal Architecture-Dependent\\Depth--Transfer Tradeoffs: A Simpson's Paradox in Representation Geometry}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	Probe-based calibration of large language models has shown promise for English, yet whether correctness probes transfer across languages remains unexplored.
29	We conduct the first large-scale study of cross-lingual correctness probe transfer, spanning three architectures (Qwen3-235B MoE, Llama~4 Scout MoE, Gemma~4 31B Dense), 20 typologically diverse languages, and five transfer conditions.
30	We report four findings forming a causal chain.
31	\textbf{(1)}~Deeper layers generally improve both English quality and cross-lingual transfer (median per-language Spearman $\rho{=}+0.66$), but the deepest layers exhibit an architecture-dependent local Pareto tradeoff in 62\% of language--architecture pairs (mean EN--ZS gap $5.2\pp$).
32	\textbf{(2)}~Decomposing the correctness signal into difficulty-shared and capability-specific components reveals that capability drives 86\% of transfer degradation despite contributing only 38\% of variance.
33	\textbf{(3)}~Calibration-Aware Cross-Lingual Regularization (\caclr{}) shifts the Pareto frontier by $+3.3\pp$ mean AUROC across 14/20 languages, reducing non-English ECE by 38\% compared to temperature scaling, requiring zero target-language labels.
34	\textbf{(4)}~A Simpson's Paradox in the CKA--transfer relationship (raw $\rho$ negative, partial $\rho{=}+0.44$ controlling for depth, $p{<}0.01$ across all three architectures) provides a geometric explanation: within each layer, cross-lingual representation similarity predicts transfer quality, but depth acts as a confound that reverses the sign when pooled.
35	Probing control tasks reveal a 10\% cross-lingual artifact rate concentrated in low-resource languages, and linear projection saturates at approximately 40 parallel pairs.
36	\end{abstract}
37	
38	%% ============================================================
39	\section{Introduction}
40	%% ============================================================
41	
42	Non-English languages suffer substantially worse calibration in multilingual large language models.
43	Correctness and verbalized confidence occupy near-orthogonal directions in representation space~\cite{miao2026steering}, rendering output-based calibration structurally limited---an observation we confirm holds across 20 languages and three architectures (mean cosine similarity $0.048$, all values below $0.10$).
44	Existing fixes either require per-language labeled data~\cite{zhou2024lace} or multiply inference cost~\cite{wang2024mka}, leaving a practical gap for label-free cross-lingual calibration.
45	
46	Recent work has established probe-based calibration as effective for English~\cite{miao2026coral,ji2024confidence}, and Xiao et al.~\cite{xiao2025knowledge} transferred knowledge-boundary probes across 8 languages.
47	However, knowledge-boundary probes target input-level answerability (a language-agnostic property), whereas correctness probes target output-dependent accuracy---a fundamentally different signal whose cross-lingual alignment properties are unknown.
48	No prior work has systematically studied whether correctness probes transfer across languages, nor characterized when and why such transfer succeeds or fails.
49	
50	We address this gap through the first large-scale cross-lingual correctness probing study.
51	Using three architectures that span both MoE and dense designs, we probe 12--24 layers per model across 20 typologically diverse languages under five transfer conditions: zero-shot, mean-shift, Procrustes linear projection, few-shot, and a new method---Calibration-Aware Cross-Lingual Regularization (\caclr{}).
52	Our experimental design eliminates the architecture-type confound (MoE vs.\ dense), the quantization confound (Gemma~4 runs in BF16), and the scale confound (active parameters range from 17B to 22B).
53	
54	Our contributions form a causal chain: (1)~we discover that the depth--transfer relationship is overwhelmingly positive but exhibits a local architecture-dependent Pareto tradeoff at the deepest layers; (2)~we decompose this tradeoff into transferable difficulty and non-transferable capability components; (3)~we show that \caclr{}'s consistency loss directly targets the capability component, shifting the Pareto frontier by $+3.3\pp$ without target-language labels; and (4)~we provide a geometric explanation via a Simpson's Paradox in the CKA--transfer relationship, confirmed across all three architectures.
55	Additionally, we contribute probing control tasks revealing a 10\% cross-lingual artifact rate, linear projection sample-efficiency analysis showing saturation at ${\sim}40$ parallel pairs, and a Procrustes effect-reversal threshold at zero-shot AUROC ${\approx}0.52$ that provides direct practitioner guidance.
56	
57	
58	%% ============================================================
59	\section{Related Work}
60	%% ============================================================
61	
62	\paragraph{Probe-Based Calibration.}
63	Correctness probes train linear classifiers on internal representations to predict answer accuracy.
64	Miao et al.~\cite{miao2026coral} introduced cross-task correctness probes for English, while Ji et al.~\cite{ji2024confidence} identified manipulable confidence directions.
65	Miao \& Ungar~\cite{miao2026steering} demonstrated that correctness and verbalized confidence are orthogonal in 7--8B English models.
66	All three lines are English-only; we extend to 20 languages.
67	
68	\paragraph{Cross-Lingual Probing and Transfer.}
69	Xiao et al.~\cite{xiao2025knowledge} transferred knowledge-boundary probes across 8 languages, finding positive transfer for answerability (an input-level, language-agnostic property).
70	Correctness is output-dependent and language-specific, making transfer fundamentally harder.
71	Civelli et al.\ demonstrated cross-lingual difficulty probe transfer, which we use as a control in our decomposition analysis.
72	Pires et al.~\cite{pires2019multilingual} and Wu \& Dredze~\cite{wu2019beto} established that multilingual BERT representations enable cross-lingual transfer, but did not study calibration.
73	
74	\paragraph{Calibration in Multilingual Settings.}
75	Zhou et al.~\cite{zhou2024lace} proposed per-language layer ensembles requiring target-language labels.
76	Temperature scaling~\cite{guo2017calibration} is language-agnostic but operates post-hoc on logits and cannot address representation-level misalignment.
77	Conformal prediction~\cite{angelopoulos2023conformal} provides coverage guarantees but requires calibration data per language.
78	
79	\paragraph{Representation Similarity and Domain Adaptation.}
80	We use linear CKA~\cite{kornblith2019similarity} to measure cross-lingual representation alignment.
81	Ben-David et al.~\cite{bendavid2010theory} provide theoretical grounding via the $\mathcal{H}$-divergence framework; Zhao et al.~\cite{zhao2019learning} explain why marginal distribution matching fails when conditional distributions differ---directly relevant to our CaCLR analysis.
82	Cross-lingual alignment methods (MUSE~\cite{conneau2018word}, VecMap~\cite{artetxe2018robust}) motivate our Procrustes linear projection, applied here at the sentence-level correctness representation.
83	
84	
85	%% ============================================================
86	\section{Method}
87	%% ============================================================
88	
89	\subsection{Correctness Probing Framework}
90	
91	Given a multilingual LLM $f$ with $L$ layers, we extract the hidden representation $\mathbf{h}_\ell^{(x)} \in \mathbb{R}^d$ at layer $\ell$ for input $x$.
92	For each layer, we train an English logistic regression probe $g_\ell(\mathbf{h}) = \sigma(\mathbf{w}_\ell^\top \mathbf{h} + b_\ell)$ on GlobalMMLU English items, where the binary label indicates whether the model's generated answer is correct.
93	The probe is then applied zero-shot to target-language representations.
94	
95	\paragraph{Transfer Conditions.}
96	We evaluate five transfer strategies:
97	(i)~\textbf{Zero-shot}: apply the English probe directly;
98	(ii)~\textbf{Mean-shift}: subtract the target-language activation mean (provably AUROC-invariant under StandardScaler + logistic regression);
99	(iii)~\textbf{Linear projection}: learn a Procrustes rotation from parallel EN--target activations;
100	(iv)~\textbf{Few-shot}: retrain with 25 or 100 target-language labeled examples;
101	(v)~\textbf{\caclr{}}: our proposed calibration-aware regularization (Section~\ref{sec:caclr}).
102	
103	\subsection{Difficulty--Capability Decomposition}
104	\label{sec:decomposition}
105	
106	Following Civelli et al., we train IRT difficulty probes via Ridge regression on human difficulty scores, obtaining a difficulty direction $\mathbf{d}_\ell$ at each layer.
107	We project out the difficulty component: $\mathbf{h}_\ell^{\text{res}} = \mathbf{h}_\ell - (\mathbf{h}_\ell \cdot \hat{\mathbf{d}}_\ell)\hat{\mathbf{d}}_\ell$, then retrain correctness probes on the residuals.
108	The decomposition separates a \emph{difficulty-shared} component (language-agnostic, well-transferable) from a \emph{capability-specific} component (language-dependent, driving transfer degradation).
109	
110	\subsection{Calibration-Aware Cross-Lingual Regularization (\caclr{})}
111	\label{sec:caclr}
112	
113	\caclr{} extends the standard BCE probe loss with two regularization terms:
114	\begin{equation}
115	\mathcal{L}_{\text{CaCLR}} = \mathcal{L}_{\text{BCE}} + \alpha \cdot \mathcal{L}_{\text{SB-ECE}} + \beta \cdot \mathcal{L}_{\text{consistency}}
116	\end{equation}
117	where $\mathcal{L}_{\text{SB-ECE}}$ is the sample-based Expected Calibration Error and $\mathcal{L}_{\text{consistency}}$ is a Maximum Mean Discrepancy (MMD) penalty on probe logits computed from parallel English and target-language inputs:
118	\begin{equation}
119	\mathcal{L}_{\text{consistency}} = \text{MMD}^2\!\big(g_\ell(\mathbf{h}^{\text{en}}),\, g_\ell(\mathbf{h}^{\text{tgt}})\big)
120	\end{equation}
121	using a Gaussian RBF kernel with median-heuristic bandwidth.
122	The MMD operates on 1-D probe logits, ensuring gradient flow to probe parameters.
123	Parallel activations come from GlobalMMLU train-split items (70/30 stratified split for training/evaluation); no target-language correctness labels are used.
124	
125	\paragraph{Implementation.}
126	We optimize with Adam (lr=$10^{-3}$, linear warmup 10\%, cosine decay) for 50 epochs with early stopping (patience 10, monitoring validation AUROC on 15\% held-out).
127	Probes are initialized from the standard logistic regression solution.
128	Batch size is 256; MMD is computed on the same items as BCE (overlapping).
129	Parallel set sizes range from 1,900 to 4,100 items per language (mean 2,800).
130	
131	\subsection{CKA Geometric Analysis}
132	
133	We compute linear CKA between English and each target language at every probed layer, yielding a $\text{CKA}(\ell, t)$ matrix for each architecture.
134	The key analysis is the \emph{partial Spearman correlation} between CKA and zero-shot AUROC, controlling for normalized depth---testing whether cross-lingual similarity predicts transfer \emph{within} each depth stratum.
135	
136	
137	%% ============================================================
138	\section{Experimental Setup}
139	%% ============================================================
140	
141	\paragraph{Models.}
142	We study three architectures: \textbf{Qwen3-235B-A22B} (94-layer MoE, INT4, ${\sim}$22B active parameters, 24 probed layers), \textbf{Llama~4 Scout} (48-layer MoE, W4A16, 17B$\times$16 experts, 12 probed layers), and \textbf{Gemma~4 31B} (60-layer dense, BF16, 16 probed layers).
143	Gemma~4 runs without quantization, providing an unquantized reference.
144	Quantization validation (Section~\ref{sec:quant}) confirms negligible distortion (${\leq}0.5\pp$ mean, rank correlation ${>}0.995$).
145	
146	\paragraph{Languages.}
147	We evaluate 20 typologically diverse languages spanning three resource tiers: \textbf{HIGH}~(zh, es, fr, de, ja, nl, pt), \textbf{MID}~(ar, hi, ko, ru, tr, vi, id, pl, uk), and \textbf{LOW}~(sw, bn, te, yo).
148	Extended experiments cover 52 languages (Section~\ref{sec:extended}).
149	
150	\paragraph{Data.}
151	All experiments use GlobalMMLU.
152	We partition the test split into probe training (70\%) and evaluation (30\%) via stratified sampling.
153	English correctness labels are derived from model-generated answers.
154	Parallel activations for \caclr{} and linear projection use the same items across languages.
155	
156	\paragraph{Metrics.}
157	Primary: AUROC for discrimination, ECE for calibration.
158	All comparisons include bootstrap confidence intervals (1,000 resamples).
159	We report per-language Spearman $\rho$ (depth vs.\ ZS AUROC) with significance tests.
160	
161	
162	%% ============================================================
163	\section{Results}
164	%% ============================================================
165	
166	\subsection{Claim 1: Architecture-Dependent Depth--Transfer Tradeoff}
167	\label{sec:pareto}
168	
169	Table~\ref{tab:arch_summary} summarizes findings across three architectures.
170	The overall positive depth--transfer trend is strong: median per-language Spearman $\rho = +0.66$, with 54/60 language--architecture pairs showing positive correlation (44/60 significant at $p{<}0.05$).
171	However, the deepest layers exhibit a local Pareto tradeoff in 37/60 (62\%) of combinations, where the English-optimal layer differs from the zero-shot-optimal layer.
172	
173	\begin{table}[t]
174	\centering
175	\small
176	\begin{tabular}{@{}lcccccc@{}}
177	\toprule
178	\textbf{Model} & \textbf{Type} & \textbf{EN} & \textbf{ZS} & \textbf{Gap} & \textbf{$\tilde{\rho}$} & \textbf{Pareto} \\
179	 & & best & mean & (pp) & & langs \\
180	\midrule
181	Qwen3-235B & MoE & .835 & .775 & 6.0 & +.62 & 15/20 \\
182	Llama 4 Scout & MoE & .815 & .765 & 5.0 & +.72 & 10/20 \\
183	Gemma 4 31B & Dense & .805 & .760 & 4.5 & +.65 & 12/20 \\
184	\midrule
185	\textbf{Mean} & --- & \textbf{.818} & \textbf{.767} & \textbf{5.2} & \textbf{+.66} & \textbf{62\%} \\
186	\bottomrule
187	\end{tabular}
188	\caption{Three-architecture summary. EN best: English AUROC at English-optimal layer. ZS mean: 20-language mean AUROC at ZS-optimal layer. Gap: EN best minus ZS mean at EN-optimal layer. $\tilde{\rho}$: median per-language Spearman $\rho$ (depth vs.\ ZS AUROC). Pareto langs: fraction showing local tradeoff.}
189	\label{tab:arch_summary}
190	\end{table}
191	
192	The tradeoff strength is architecture-dependent.
193	Qwen3-235B exhibits the strongest effect: the EN-optimal layer (L68, 72\% depth) and ZS-optimal layer (L48, 51\% depth) are separated by 20 layers, with a $3.8\pp$ ZS drop at the EN optimum.
194	Llama~4 Scout shows a weaker tradeoff (10/20 languages, $2.5\pp$ drop), with its ZS-optimal layer at 58\% depth.
195	Gemma~4 (dense, unquantized) falls between the two MoE models (12/20, $3.0\pp$), confirming that the Pareto tradeoff is a property of transformer depth, not MoE routing.
196	
197	Table~\ref{tab:pareto_qwen} shows the Qwen3 Pareto frontier at representative layers.
198	The transition from net-positive to net-negative transfer occurs around 50\% depth across all three architectures, defining a universal ``mid-depth transfer zone.''
199	
200	\begin{table}[t]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba36d988-579a-4db2-becd-01aa120bda04",
  "isSidechain": true,
  "promptId": "daded219-2295-49e3-ac22-87f6bbbc54c9",
  "agentId": "a95da934c42f8700a",
  "type": "user",
  "uuid": "09311249-a5ae-455f-93f9-c7e043f9ff25",
  "sourceToolAssistantUUID": "ba36d988-579a-4db2-becd-01aa120bda04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T13:52:02.316Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PswgZ8G3gmiStQWbkJkK9i`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper.tex",
  "offset": 200,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09311249-a5ae-455f-93f9-c7e043f9ff25",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpjyB5Y8Hew7NeDoQHq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3d7f717-ff2e-4b38-a588-7c6a7328f26e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XqMbTB9ur4w6pFXudXzYyC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5104,
      "cache_read_input_tokens": 19743,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5104
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 19743,
          "cache_creation_input_tokens": 5104,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5104,
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

_source line 17 · 2026-05-21T13:52:02.324Z_

<details><summary>↩ Tool result · `toolu_01PswgZ8G3gmiStQWbkJkK9i`</summary>

```text
200	\begin{table}[t]
201	\centering
202	\small
203	\begin{tabular}{@{}ccccc@{}}
204	\toprule
205	\textbf{Layer} & \textbf{Depth} & \textbf{EN} & \textbf{ZS} & \textbf{Drop} \\
206	(idx) & (\%) & AUROC & mean & (pp) \\
207	\midrule
208	20 & 21 & .710 & .700 & 1.0 \\
209	36 & 38 & .785 & .770 & 1.5 \\
210	48 & 51 & .815 & .775 & 4.0 \\
211	56 & 60 & .828 & .757 & 7.1 \\
212	68 & 72 & .835 & .737 & 9.8 \\
213	80 & 85 & .822 & .695 & 12.7 \\
214	92 & 98 & .790 & .642 & 14.8 \\
215	\bottomrule
216	\end{tabular}
217	\caption{Qwen3-235B Pareto frontier (selected layers). Drop = EN AUROC $-$ ZS mean AUROC at each layer. L48 is the ZS-optimal layer; L68 is EN-optimal.}
218	\label{tab:pareto_qwen}
219	\end{table}
220	
221	Per-language analysis reveals a resource-tier gradient.
222	On Qwen3, HIGH-resource languages achieve ZS AUROC $0.817$ (mean), MID $0.788$, LOW $0.693$.
223	Per-language Spearman $\rho$ is significantly positive ($p{<}0.05$) for 14/20 languages; the three languages with negative $\rho$ (yo, te, sw) are all LOW-resource, where pretraining representation quality degrades faster with depth than probe discrimination improves.
224	
225	
226	\subsection{Claim 2: Difficulty Transfers, Capability Does Not}
227	\label{sec:decomposition_results}
228	
229	Table~\ref{tab:decomp} presents the decomposition analysis pooled across three architectures and 10 languages.
230	IRT difficulty probes achieve $R^2{=}0.67$ (range $0.54$--$0.76$), successfully capturing the universal difficulty signal.
231	The difficulty-shared component accounts for 62\% of correctness variance but only 14\% of transfer degradation; the capability-specific component accounts for 38\% of variance but 86\% of degradation.
232	
233	\begin{table}[t]
234	\centering
235	\small
236	\begin{tabular}{@{}lcccc@{}}
237	\toprule
238	\textbf{Component} & \textbf{Var} & \textbf{Transfer} & \textbf{Drop} & \textbf{Degr.} \\
239	 & (\%) & AUROC & (pp) & share \\
240	\midrule
241	Full correctness & 100 & .767 & 5.2 & 100\% \\
242	Difficulty (shared) & 62 & .755 & 0.7 & 14\% \\
243	Capability (specific) & 38 & .672 & 7.8 & 86\% \\
244	Random direction & --- & .752 & --- & --- \\
245	\bottomrule
246	\end{tabular}
247	\caption{Difficulty--capability decomposition (3 architectures, 10 languages pooled). The random-direction control confirms that difficulty projection captures genuine structure, not a dimensionality-reduction artifact ($-1.5\pp$ vs.\ $+4.5\pp$ for difficulty projection).}
248	\label{tab:decomp}
249	\end{table}
250	
251	Capability transfer degradation increases sharply with depth: from $0.5\pp$ at 20--30\% depth to $8.8\pp$ at 75--90\% depth (ratio $2.5{\times}$ to $7.3{\times}$ vs.\ difficulty degradation).
252	Projecting out the difficulty direction reduces EN AUROC by $4.2\pp$ (removing easy--hard distinction) but \emph{improves} ZS transfer by $4.5\pp$---the residual probe, forced to rely on the language-agnostic component of capability, transfers better.
253	Clean separation is observed in 8/10 languages; the two exceptions (sw, bn) reflect noisy difficulty labels from low-quality translations.
254	The decomposition achieves 76\% prescriptive accuracy: given the difficulty/capability ratio at each language--layer combination, it correctly predicts whether zero-shot or \caclr{} is the optimal strategy.
255	
256	\subsection{Claim 3: \caclr{} Shifts the Pareto Frontier}
257	\label{sec:caclr_results}
258	
259	\paragraph{Main Result.}
260	Table~\ref{tab:transfer} compares all transfer conditions at the ZS-optimal layer, averaged across three architectures and 20 languages.
261	\caclr{} (1-D MMD) achieves the highest label-free AUROC ($0.800$, $+3.3\pp$ vs.\ zero-shot) and the lowest ECE ($0.073$, a 38\% reduction compared to temperature scaling).
262	The higher-dimensional variant (PCA-50 MMD) further improves to $0.809$ ($+4.2\pp$).
263	
264	\begin{table}[t]
265	\centering
266	\small
267	\begin{tabular}{@{}lcccl@{}}
268	\toprule
269	\textbf{Method} & \textbf{AUROC} & \textbf{ECE} & \textbf{$\Delta$} & \textbf{Requires} \\
270	 & & & (pp) & \\
271	\midrule
272	Zero-shot & .767 & .118 & --- & --- \\
273	Mean-shift & .767 & .118 & 0.0 & --- \\
274	LinProj (50) & .781 & .100 & +1.4 & 50 pairs \\
275	LinProj (200) & .783 & .097 & +1.6 & 200 pairs \\
276	Few-shot (25) & .754 & .108 & $-$1.3 & 25 labels \\
277	Few-shot (100) & .785 & .090 & +1.8 & 100 labels \\
278	\caclr{} (1-D) & .800 & .073 & +3.3 & parallel act. \\
279	\caclr{} (PCA-50) & \textbf{.809} & \textbf{.068} & \textbf{+4.2} & parallel act. \\
280	\bottomrule
281	\end{tabular}
282	\caption{Transfer conditions at the ZS-optimal layer (3-architecture, 20-language average). $\Delta$: improvement over zero-shot in AUROC (pp). \caclr{} requires parallel activations but no target-language labels.}
283	\label{tab:transfer}
284	\end{table}
285	
286	\paragraph{Consistency Loss ($\beta$) Sweep.}
287	Table~\ref{tab:beta} shows the effect of $\beta$ on transfer quality.
288	The optimal $\beta{=}0.05$ balances consistency regularization against accuracy: below $0.01$, the MMD gradient is overwhelmed by noise; above $0.1$, the probe sacrifices accuracy to match distributions.
289	Multi-seed standard deviation is ${\pm}0.35\pp$, confirming robustness.
290	
291	\begin{table}[t]
292	\centering
293	\small
294	\begin{tabular}{@{}cccc@{}}
295	\toprule
296	$\beta$ & $\Delta$AUROC (pp) & $\Delta$ECE (pp) & Note \\
297	\midrule
298	0 & 0.0 & 0.0 & BCE only \\
299	0.001 & +0.5 & $-$0.3 & marginal \\
300	0.01 & +1.6 & $-$0.9 & signal emerges \\
301	\textbf{0.05} & \textbf{+3.3} & $\mathbf{-2.2}$ & \textbf{optimal} \\
302	0.1 & +3.0 & $-$1.8 & slight over-reg. \\
303	1.0 & +0.6 & $-$0.3 & MMD dominates \\
304	\bottomrule
305	\end{tabular}
306	\caption{$\beta$ sweep for consistency loss (3-architecture average, $\alpha{=}0.1$). Optimal at $\beta{=}0.05$ with inverted-U response.}
307	\label{tab:beta}
308	\end{table}
309	
310	\paragraph{Component Ablation.}
311	BCE alone yields $0.767$ mean AUROC. Adding SB-ECE ($+\alpha$) improves to $0.774$ ($+0.7\pp$ from calibration). Adding MMD ($+\beta$) without SB-ECE yields $0.792$ ($+2.5\pp$---the main contributor). The full \caclr{} loss achieves $0.800$ ($+3.3\pp$), confirming synergy between calibration and consistency.
312	
313	\paragraph{Tier-Stratified Improvement.}
314	\caclr{} improvement is inversely correlated with resource level: HIGH $+1.2\pp$ (3/7 improved), MID $+3.8\pp$ (8/9), LOW $+6.5\pp$ (3/4).
315	One language is hurt (yo, $-$), where low-quality parallel translations introduce noise into the MMD matching.
316	14/20 languages show improvement overall.
317	
318	\paragraph{Depth Profile.}
319	\caclr{}'s benefit increases with depth: $+1.2\pp$ at shallow layers (30\% depth) vs.\ $+4.5\pp$ at deep layers (72\%+ depth).
320	This directly corresponds to the capability-specific degradation profile from the decomposition analysis (Section~\ref{sec:decomposition_results}): \caclr{}'s consistency loss targets exactly the non-transferable capability component that grows with depth.
321	
322	\paragraph{Distributional Matching Comparison.}
323	CORAL (second-order matching) achieves $+2.8\pp$ in 1-D and $+3.6\pp$ in PCA-50, confirming that distributional matching generally works and is not MMD-specific.
324	MMD-PCA50 ($+4.2\pp$) outperforms MMD-1D ($+3.3\pp$) by capturing covariance structure in the 50-dimensional PCA space, but PCA-100 regresses slightly ($+3.8\pp$) due to the curse of dimensionality.
325	
326	
327	\subsection{Claim 4: Simpson's Paradox in CKA--Transfer Geometry}
328	\label{sec:cka}
329	
330	\paragraph{The Paradox.}
331	Table~\ref{tab:simpson} presents the core geometric finding.
332	Pooling across all layers and languages, the raw Spearman correlation between CKA and zero-shot AUROC is \emph{negative} ($\rho = -0.38$ to $-0.42$, $p{<}0.001$): languages with higher CKA tend to have lower AUROC.
333	However, controlling for normalized depth reverses the sign: the partial correlation is \emph{positive} ($\rho = +0.41$ to $+0.48$, all $p{<}0.01$) with bootstrap 95\% CIs excluding zero.
334	This Simpson's Paradox is confirmed across all three architectures.
335	
336	\begin{table}[t]
337	\centering
338	\small
339	\begin{tabular}{@{}llccc@{}}
340	\toprule
341	\textbf{Model} & \textbf{Analysis} & $\rho$ & $p$ & \textbf{95\% CI} \\
342	\midrule
343	\multirow{2}{*}{Qwen3} & Raw pooled & $-$.38 & ${<}.001$ & [$-$.46,$-$.29] \\
344	 & Partial & +.48 & .002 & [+.30,+.63] \\
345	\midrule
346	\multirow{2}{*}{Llama 4} & Raw pooled & $-$.42 & ${<}.001$ & [$-$.51,$-$.32] \\
347	 & Partial & +.41 & .007 & [+.21,+.58] \\
348	\midrule
349	\multirow{2}{*}{Gemma 4} & Raw pooled & $-$.40 & ${<}.001$ & [$-$.49,$-$.30] \\
350	 & Partial & +.44 & .004 & [+.26,+.60] \\
351	\bottomrule
352	\end{tabular}
353	\caption{Simpson's Paradox: raw vs.\ partial Spearman correlation between CKA and ZS AUROC. Partial correlation controls for normalized depth. Sign reversal confirmed across all architectures.}
354	\label{tab:simpson}
355	\end{table}
356	
357	The causal mechanism is as follows: depth simultaneously drives CKA down (representations diverge) and AUROC up-then-down (probe quality improves to mid-depth, then capability-specific features dominate).
358	This creates a depth confound in the raw correlation.
359	Within each layer, higher CKA genuinely predicts better transfer---the positive partial correlation captures this layer-local relationship.
360	
361	\paragraph{Subspace Angle Analysis.}
362	Table~\ref{tab:subspace} provides mechanistic grounding.
363	The correctness direction is near-universal within each layer: cross-language angles average $12.8^{\circ}$ ($\pm 5.4^{\circ}$), far from the $87.1^{\circ}$ random baseline.
364	However, the direction rotates substantially across layers ($37.5^{\circ}$ $\pm 10.8^{\circ}$), explaining why within-layer CKA predicts transfer but pooled CKA does not.
365	
366	\begin{table}[t]
367	\centering
368	\small
369	\begin{tabular}{@{}lcc@{}}
370	\toprule
371	\textbf{Comparison} & \textbf{Angle ($^{\circ}$)} & \textbf{Std ($^{\circ}$)} \\
372	\midrule
373	Within-layer cross-language & 12.8 & 5.4 \\
374	Cross-layer same-language & 37.5 & 10.8 \\
375	Random baseline (shuffled) & 87.1 & 2.0 \\
376	\bottomrule
377	\end{tabular}
378	\caption{Subspace angle analysis (pooled across architectures). The correctness direction is near-universal within layers but rotates significantly across layers.}
379	\label{tab:subspace}
380	\end{table}
381	
382	\paragraph{CKA Cliff Threshold.}
383	We identify a CKA collapse threshold at ${\approx}0.35$: below this value, mean ZS AUROC drops to $0.60$ (vs.\ $0.74$ above).
384	This threshold connects the Pareto tradeoff (Claim~1) with the geometric analysis: Qwen3's steeper CKA cliff causes more languages to cross the threshold at deeper layers, producing a stronger tradeoff (15/20) than Llama~4 (10/20).
385	
386	
387	%% ============================================================
388	\section{Additional Analyses}
389	%% ============================================================
390	
391	\subsection{Probing Control Tasks}
392	\label{sec:control}
393	
394	Following Hewitt \& Liang~\cite{hewitt2019designing}, we train probes on randomly permuted labels and compute selectivity (real AUROC $-$ control AUROC).
395	Table~\ref{tab:control} shows cross-lingual artifact rates by resource tier.
396	The overall rate is 10\% (260/2,736 language--layer--architecture combinations with selectivity below 0.05), but this is heavily concentrated in LOW-resource languages at deep layers (28\% artifact rate vs.\ 3\% for HIGH).
397	
398	\begin{table}[t]
399	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3d7f717-ff2e-4b38-a588-7c6a7328f26e",
  "isSidechain": true,
  "promptId": "daded219-2295-49e3-ac22-87f6bbbc54c9",
  "agentId": "a95da934c42f8700a",
  "type": "user",
  "uuid": "39654355-5b75-47d2-bc5e-a92dadc18b67",
  "sourceToolAssistantUUID": "a3d7f717-ff2e-4b38-a588-7c6a7328f26e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T13:52:07.515Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VSRz4ea8REvJtxfHY5aGN2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper.tex",
  "offset": 400,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39654355-5b75-47d2-bc5e-a92dadc18b67",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpkLdAtyrxLFrvpZ5Nh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92dacc3f-7950-4319-adc9-2e2b6607ede1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CnkrjFAtUqdcTv1cRxCzPp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4567,
      "cache_read_input_tokens": 24847,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4567
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 24847,
          "cache_creation_input_tokens": 4567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4567,
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

_source line 19 · 2026-05-21T13:52:07.522Z_

<details><summary>↩ Tool result · `toolu_01VSRz4ea8REvJtxfHY5aGN2`</summary>

```text
400	\small
401	\begin{tabular}{@{}lccc@{}}
402	\toprule
403	\textbf{Tier} & \textbf{Combinations} & \textbf{Artifacts} & \textbf{Rate (\%)} \\
404	\midrule
405	HIGH & 1,008 & 30 & 3 \\
406	MID & 1,152 & 69 & 6 \\
407	LOW & 576 & 161 & 28 \\
408	\midrule
409	Total & 2,736 & 260 & 10 \\
410	\bottomrule
411	\end{tabular}
412	\caption{Cross-lingual artifact rates (selectivity threshold $= 0.05$). Artifacts concentrate in LOW-resource languages at $>$60\% depth.}
413	\label{tab:control}
414	\end{table}
415	
416	This finding has field-level implications: cross-lingual probing studies that omit selectivity checks risk overestimating low-resource transfer quality.
417	Our core Pareto and CKA analyses (Sections~\ref{sec:pareto}, \ref{sec:cka}) are primarily driven by HIGH and MID patterns and are not affected.
418	
419	\subsection{Linear Projection Sample Efficiency and Procrustes Reversal}
420	\label{sec:linproj}
421	
422	Procrustes alignment saturates rapidly: ${\sim}40$ parallel pairs achieve 95\% of 200-pair performance, with resource-tier stratification (HIGH: 22 pairs, MID: 36, LOW: 48 to 95\%).
423	The saturation curve reflects the low effective dimensionality of the correctness subspace.
424	
425	A striking reversal emerges when stratifying by baseline quality: Procrustes helps substantially when ZS AUROC $< 0.52$ ($+4.2\pp$) but \emph{hurts} when ZS AUROC $> 0.68$ ($-1.0\pp$).
426	The reversal threshold (${\approx}0.52$) corresponds to a CKA of ${\approx}0.35$ (the cliff threshold from Section~\ref{sec:cka}), providing geometric consistency across analyses.
427	Practitioners should condition alignment strategy on baseline transfer quality: apply linear projection only when zero-shot performance is poor.
428	
429	\subsection{Cross-Lingual Correctness--Confidence Orthogonality}
430	
431	Extending Miao \& Ungar's English finding~\cite{miao2026steering}, we measure cosine similarity between correctness and verbalized confidence directions across 20 languages and three architectures.
432	All 59/60 model--language pairs have cosine $< 0.10$ (mean $0.048$), confirming that output-based calibration is structurally limited regardless of language.
433	A small resource-tier gradient exists (HIGH: $0.036$, MID: $0.050$, LOW: $0.070$; Spearman $\rho = -0.62$ with resource level), but the absolute range is narrow ($0.034$).
434	
435	\subsection{Probe Complexity Comparison}
436	
437	Two-layer MLPs (hidden $= 128$) gain $+2.0\pp$ EN AUROC over logistic regression but suffer $-5.6\pp$ worse cross-lingual transfer (ZS drop: $10.8\pp$ vs.\ $5.2\pp$).
438	The gap widens at deep layers ($+8.5\pp$ logistic regression advantage at $>$70\% depth), where MLPs overfit to English-specific nonlinear feature interactions.
439	This validates the linear probe choice: the correctness subspace is a near-universal linear structure (subspace angle $12.8^{\circ}$), and linear probes naturally preserve cross-lingual generalization.
440	
441	\subsection{Cross-Benchmark Generalization}
442	
443	Table~\ref{tab:crossbench} shows that all findings replicate across benchmarks.
444	\caclr{} improvement is consistent (CV $= 0.04$ across benchmarks), and the Pareto frontier structure holds on both Belebele (reading comprehension) and MMLU-ProX (harder factual).
445	
446	\begin{table}[t]
447	\centering
448	\small
449	\begin{tabular}{@{}lccc@{}}
450	\toprule
451	\textbf{Benchmark} & \textbf{ZS} & \textbf{\caclr{}} & $\Delta$ (pp) \\
452	\midrule
453	GlobalMMLU & .767 & .800 & +3.3 \\
454	Belebele & .748 & .780 & +3.2 \\
455	MMLU-ProX & .735 & .770 & +3.5 \\
456	\bottomrule
457	\end{tabular}
458	\caption{Cross-benchmark generalization (3 architectures, 20 languages).}
459	\label{tab:crossbench}
460	\end{table}
461	
462	\subsection{Quantization Validation}
463	\label{sec:quant}
464	
465	W4A16 (Llama~4) introduces $0.3\pp$ mean AUROC difference (max $0.7\pp$) vs.\ FP16; GPTQ-INT4 (Qwen3) introduces $0.5\pp$ mean (max $1.2\pp$).
466	Rank correlations exceed $0.995$ for both, confirming that Pareto frontier ordering is fully preserved.
467	CKA distortion is bounded by $0.02$.
468	Gemma~4 (BF16) provides the unquantized cross-validation anchor.
469	
470	\subsection{Extended Language Coverage}
471	\label{sec:extended}
472	
473	Expanding to 52 languages across five new language families (Austronesian, Dravidian, Uralic, Kartvelian, Niger-Congo~B), all findings hold.
474	ZS AUROC above $0.60$ for 43/52 languages; \caclr{} improves 48/52.
475	The Pareto frontier and Simpson's Paradox structure replicate at full scale.
476	The resource-tier gradient extends smoothly: HIGH (10 langs) $+2.5\pp$, MID (24) $+3.2\pp$, LOW (14) $+4.8\pp$, VERY\_LOW (4) $+5.8\pp$.
477	
478	
479	%% ============================================================
480	\section{Discussion}
481	%% ============================================================
482	
483	\paragraph{Why Mean-Shift Fails.}
484	Under StandardScaler preprocessing followed by logistic regression, mean-shift adds a constant offset to all logits.
485	Since AUROC is rank-invariant, $\Delta\text{AUROC} \equiv 0$ mathematically.
486	Our data confirm this: mean-shift produces exactly zero AUROC change across all languages and layers.
487	This proof distinguishes our setting from Xiao et al., where mean-shift improves accuracy under different metrics and pipeline configurations, and motivates the need for stronger alignment methods.
488	
489	\paragraph{Practitioner Recommendations.}
490	Our results yield concrete guidance:
491	(i)~Probe at 50--60\% depth for best cross-lingual transfer.
492	(ii)~Use \caclr{} with $\beta{=}0.05$ when parallel activations are available; fall back to linear projection with ${\sim}40$ parallel pairs when they are not.
493	(iii)~Apply Procrustes only when zero-shot AUROC $< 0.52$; above $0.68$, it hurts.
494	(iv)~Always run selectivity controls for low-resource languages.
495	
496	\paragraph{Limitations.}
497	Our study is limited to MCQA, which enables clean correctness labeling but may not generalize to open-ended generation.
498	The three architectures, while spanning MoE and dense designs, cannot support causal attribution to specific architectural features (e.g., MoE routing) without controlled experiments holding all else equal.
499	Low-resource results (yo, te, sw) should be interpreted with caution given the 28\% artifact rate and potentially noisy translations.
500	
501	
502	%% ============================================================
503	\section{Conclusion}
504	%% ============================================================
505	
506	We presented the first large-scale study of cross-lingual correctness probe transfer across three architectures and 20 languages.
507	Our four linked findings---Pareto discovery, difficulty--capability decomposition, \caclr{} method, and Simpson's Paradox geometric explanation---provide both theoretical understanding and practical tools for multilingual calibration.
508	\caclr{}-trained correctness probes reduce non-English ECE by 38\% compared to temperature scaling, requiring zero target-language labels.
509	The 10\% artifact rate in probing controls serves as a methodological warning for the field, and the ${\sim}40$-pair saturation point for linear projection offers an immediately actionable finding.
510	Future work should extend correctness probing beyond MCQA, explore adapter-based alignment for very low-resource languages, and test whether the Simpson's Paradox structure holds for other cross-lingual probing tasks.
511	
512	
513	\bibliographystyle{plainnat}
514	\bibliography{references}
515	
516	\appendix
517	
518	\section{Per-Language Spearman Correlations (Qwen3-235B)}
519	\label{app:spearman}
520	
521	\begin{table}[h]
522	\centering
523	\small
524	\begin{tabular}{@{}llccc@{}}
525	\toprule
526	\textbf{Lang} & \textbf{Tier} & $\rho$ & $p$ & \textbf{Sig.} \\
527	\midrule
528	zh & HIGH & +.75 & .0001 & \checkmark \\
529	de & HIGH & +.73 & .0002 & \checkmark \\
530	es & HIGH & +.72 & .0002 & \checkmark \\
531	nl & HIGH & +.71 & .0003 & \checkmark \\
532	fr & HIGH & +.70 & .0003 & \checkmark \\
533	pt & HIGH & +.69 & .0004 & \checkmark \\
534	ja & HIGH & +.68 & .0005 & \checkmark \\
535	ru & MID & +.68 & .0005 & \checkmark \\
536	ar & MID & +.67 & .0006 & \checkmark \\
537	ko & MID & +.65 & .001 & \checkmark \\
538	id & MID & +.63 & .002 & \checkmark \\
539	hi & MID & +.62 & .002 & \checkmark \\
540	pl & MID & +.62 & .002 & \checkmark \\
541	tr & MID & +.60 & .003 & \checkmark \\
542	uk & MID & +.58 & .005 & \checkmark \\
543	vi & MID & +.55 & .007 & \checkmark \\
544	bn & LOW & +.35 & .100 & \\
545	sw & LOW & $-$.12 & .580 & \\
546	te & LOW & $-$.08 & .720 & \\
547	yo & LOW & $-$.18 & .420 & \\
548	\bottomrule
549	\end{tabular}
550	\caption{Per-language Spearman $\rho$ (depth vs.\ ZS AUROC) for Qwen3-235B. Checkmark indicates $p < 0.05$.}
551	\label{app:tab_spearman}
552	\end{table}
553	
554	\section{CaCLR Depth Profile (Qwen3)}
555	\label{app:depth_profile}
556	
557	\begin{table}[h]
558	\centering
559	\small
560	\begin{tabular}{@{}cccc@{}}
561	\toprule
562	\textbf{Depth (\%)} & \textbf{ZS} & \textbf{\caclr{}} & $\Delta$ (pp) \\
563	\midrule
564	30 & .740 & .752 & +1.2 \\
565	43 & .779 & .798 & +1.9 \\
566	51 & .775 & .805 & +3.0 \\
567	60 & .757 & .798 & +4.1 \\
568	72 & .737 & .785 & +4.8 \\
569	85 & .695 & .740 & +4.5 \\
570	\bottomrule
571	\end{tabular}
572	\caption{\caclr{} improvement by depth on Qwen3-235B (20-language mean). Benefit increases with depth, targeting the capability-specific component.}
573	\label{app:tab_depth}
574	\end{table}
575	
576	
577	\end{document}
578	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92dacc3f-7950-4319-adc9-2e2b6607ede1",
  "isSidechain": true,
  "promptId": "daded219-2295-49e3-ac22-87f6bbbc54c9",
  "agentId": "a95da934c42f8700a",
  "type": "user",
  "uuid": "520f433a-aab3-4ad2-b1ff-be656af34982",
  "sourceToolAssistantUUID": "92dacc3f-7950-4319-adc9-2e2b6607ede1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-21T13:52:11.617Z_

Now let me read the paper's actual experiment results and the project's ideas/roadmap/memory for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "520f433a-aab3-4ad2-b1ff-be656af34982",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpkixLuAgNhqppPRXHf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3bf2112f-c1a5-44be-a58f-b2ce9d71c284",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKe1w1ammTCzRgch9FYqig",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3574,
      "cache_read_input_tokens": 29414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3574,
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

_source line 21 · 2026-05-21T13:52:12.690Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01D8CE43yYTrfSWjLJPq21WK`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "ideas.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bf2112f-c1a5-44be-a58f-b2ce9d71c284",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpkixLuAgNhqppPRXHf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b226a6fe-5c52-453b-b2dd-7cfc49c9c85b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKe1w1ammTCzRgch9FYqig",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3574,
      "cache_read_input_tokens": 29414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3574,
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

_source line 22 · 2026-05-21T13:52:12.711Z_

<details><summary>↩ Tool result · `toolu_01D8CE43yYTrfSWjLJPq21WK`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'xling_calib_direction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b226a6fe-5c52-453b-b2dd-7cfc49c9c85b",
  "isSidechain": true,
  "promptId": "daded219-2295-49e3-ac22-87f6bbbc54c9",
  "agentId": "a95da934c42f8700a",
  "type": "user",
  "uuid": "d2664572-cac6-487c-8741-97b4b33cd0b8",
  "sourceToolAssistantUUID": "b226a6fe-5c52-453b-b2dd-7cfc49c9c85b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T13:52:13.090Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KR3RfBEAt2yoRSs323S8zG`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "memory.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2664572-cac6-487c-8741-97b4b33cd0b8",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpkixLuAgNhqppPRXHf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73902e25-ec00-4f2e-9865-8de33cdc5deb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKe1w1ammTCzRgch9FYqig",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3574,
      "cache_read_input_tokens": 29414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3574,
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

_source line 24 · 2026-05-21T13:52:13.105Z_

<details><summary>↩ Tool result · `toolu_01KR3RfBEAt2yoRSs323S8zG`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/memory.md\", \"content\": \"# Memory\\n\\n## 2026-05-21: compressed_tensors OOM 根因纠正\\n\\n- **原始诊断（错误）**: compressed_tensors W4A16 解压 OOM\\n- **真实根因**: Qwen3 dry run (PID 482839) 占着 GPU 1-3（88 GiB），plan_002_4gpu 与之冲突导致 OOM\\n- **证据**: 4卡 dry run 在 clean GPU 上成功；failure_reason 显示 \\\"Process 482839 has 88.03 GiB memory in use\\\"\\n- **教训**: OOM 诊断时先检查 nvidia-smi 是否有其他进程占用，再分析框架层面的原因。compressed_tensors 格式本身在 4 卡上是可行的\\n\\n## 2026-05-21: CKA 数据不一致根因（3 套数据差异）\\n\\n- **现象**: sw L0 CKA 值在 3 套数据间差异巨大（0.44 vs 0.91）\\n- **根因**: `code/compute_cka.py` pilot 版的 `load_eval_activations()` 对 `.pt` 格式做位置 70/30 分割（取后 30%），但 MMLU 按 subject 排序，位置分割 = subject 分割 → 有偏子集\\n- **正确值**: 全量 14042 样本 → sw L0 = 0.44（A/B 版本）；后 30% 位置分割 → sw L0 = 0.91（pilot 版，有偏）\\n- **验证**: 随机抽样同样 4213 样本给出 CKA = 0.42，接近全量值，证明是位置偏差非样本量问题\\n- **修复**: compute_cka.py 应使用全量数据或随机分割，不做位置切分\\n- **影响**: Simpson's Paradox 发现需用全量 CKA 数据重新验证（pilot 基于有偏数据）\\n\\n## 2026-05-21: 实验提交环境变量模板（3次失败教训）\\n\\nplan_002 连续失败 3 次，根因：`bash -c` 不读 `.bashrc`，导致 HF_HOME 未设置 + 网络访问失败。\\n\\n**所有实验提交必须用以下 env var block**：\\n```bash\\nbash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \\\\\\nexport PYTHONUNBUFFERED=1 && \\\\\\nexport HF_HOME=/root/autodl-tmp/.hf_cache && \\\\\\nexport HF_HUB_OFFLINE=1 && \\\\\\nexport HF_DATASETS_OFFLINE=1 && \\\\\\nexport TRANSFORMERS_OFFLINE=1 && \\\\\\ncd /root/xling_calib_direction && \\\\\\npython -u code/xxx.py ...\\\"\\n```\\n\\n其他教训：\\n- `--gpu_id` 不是 extract_activations.py 的合法参数，用 CUDA_VISIBLE_DEVICES 控制 GPU\\n- `--languages` 用空格分隔（nargs=\\\"+\\\"），不是逗号\\n- `--model_name` 是必选参数\\n- 模型已在本地时必须设 OFFLINE=1，否则 transformers 尝试联网会因 HTTP client closed 崩溃\\n\\n## 2026-05-21: Simpson's Paradox in CKA-transfer relationship (D012 关键发现)\\n\\n- **发现**: CKA vs transfer AUROC 存在 Simpson's Paradox——pool 所有 layer 时弱负相关 (rho≈−0.16)，控制 depth 后符号反转为正 (Llama rho=+0.41 p=0.006, Qwen rho=+0.18 ns)\\n- **机制**: CKA 随 depth 下降，AUROC 随 depth 上升，两趋势相消产生虚假负相关。同一 depth 下，CKA 越高 → transfer 越好\\n- **⚠️ 注意**: 此发现基于 pilot CKA 数据（可能含位置分割偏差），需用全量 CKA 数据重新验证\\n- **意义**: 直接回应 Reviewer depth confound 质疑；符号反转本身是 publishable finding\\n- **局限**: Qwen partial rho underpowered (n=40)，per-layer n=5 只能看方向。Full-scale 20 langs 会大幅增加统计功效\\n\\n## 2026-05-21: run_plan_001.sh 关键设计决策\\n\\n- **GPTQ 加载**: `--quantization none` 让 HF 自动检测 GPTQ（不用 bitsandbytes NF4）\\n- **Train/eval split**: `--split_ratio 0.7` 产出 `_train.pt`/`_eval.pt`，symlink 桥接下游脚本\\n- **Procrustes 平行配对**: for_eval/ 中 EN 必须指向 eval split（与 target 平行），已修复初始 bug\\n\\n## 2026-05-21: 模型下载路径\\n\\n- Llama4 正确路径: `/root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/`\\n- Qwen3 路径: `/root/autodl-tmp/models/Qwen3-235B-GPTQ-Int4/`（注意：目录名是 `Qwen3-235B-GPTQ-Int4`，不含 `A22B`）\\n- Qwen3 config: num_hidden_layers=94, hidden_size=4096, num_local_experts=128\\n- 必须用 `HF_HUB_DISABLE_XET=1`（在 os.environ 中设置）+ `hf-mirror.com`\\n- `python3` 不在 PATH，用 `/root/miniconda3/bin/python3`\\n\\n## 2026-05-21: EN AUROC 数据分裂（必须统一）\\n\\n- **问题**: registry mvp_001 EN AUROC=0.7541@L27（60/20/20 split）vs pareto_results.json EN AUROC=0.7459@L27（70/30 split, D010 后）\\n- **差异**: 0.82pp，因评估分割不同\\n- **决定**: 论文 figure 和表格统一使用 70/30 split 数据（D010 决策）。不同表格/图之间数字必须一致\\n- **注意**: 引用 registry metrics 时检查是否为 70/30 split；旧 MVP 数据用 60/20/20，需标注或替换\\n\", \"total_chars\": 3113, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73902e25-ec00-4f2e-9865-8de33cdc5deb",
  "isSidechain": true,
  "promptId": "daded219-2295-49e3-ac22-87f6bbbc54c9",
  "agentId": "a95da934c42f8700a",
  "type": "user",
  "uuid": "1c0910db-603d-4d8a-b6f2-deaf50b840d6",
  "sourceToolAssistantUUID": "73902e25-ec00-4f2e-9865-8de33cdc5deb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T13:52:13.627Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01N47VhZuj8uzsEvfCjQ8YSH`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "ROADMAP.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c0910db-603d-4d8a-b6f2-deaf50b840d6",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpkixLuAgNhqppPRXHf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b10bcb2-2381-4f13-8669-6500768ec9d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKe1w1ammTCzRgch9FYqig",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3574,
      "cache_read_input_tokens": 29414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3574,
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

_source line 26 · 2026-05-21T13:52:13.636Z_

<details><summary>↩ Tool result · `toolu_01N47VhZuj8uzsEvfCjQ8YSH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/ROADMAP.md\", \"content\": \"# xling_calib_direction — Research Dashboard\\n\\n> 最后更新: 2026-05-21 13:49 UTC | 更新原因: plan_001 (Qwen3-235B) RUNNING on 4 GPU. PID 299313. Verification pending.\\n\\n## 核心方向\\nCross-lingual correctness probe transfer: LLM 内部 correctness direction 的跨语言可迁移性。**Novelty 锚点**：CKA Simpson's Paradox（partial ρ=-0.29, p=0.078, 符号反转确认）+ control task（selectivity depth-dependent）。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research + 审稿进行中 + 论文写作并行\\n- **MVP**: 3/3 完成 ✓\\n- **Research**: plan_013 ✓; CKA pilot ✓; CKA 数据修正 ✓\\n- **plan_001 (Qwen3-235B)**: **🟢 RUNNING** — PID 299313, 4 GPU, 24 层 × 20 语言, ~20-40h\\n- **plan_002 (Llama4)**: 6 次失败 → killed, 推后至 plan_001 完成后（D019）\\n- **plan_013_v2**: RUNNING（CPU-bound, PID 47972, 4/8 层）\\n- **Dream 趋势**: #3 best=4/6 WA; #4 best=3.5/5 Findings → **目标: 4/5 正会**\\n- **论文写作**: Intro ✅ | Method ✅ | Related Work ✅ | Experiments Setup ✅ | Figures pilot ✅ | 剩余: Abstract, Results, Conclusion\\n\\n## 模型状态\\n| 模型 | 量化 | 状态 |\\n|------|------|------|\\n| Qwen3-235B-A22B | GPTQ-Int4 | **🟢 RUNNING** plan_001 (PID 299313, 4 GPU) |\\n| Llama 4 Scout 17B-16E | W4A16 | ⏸️ 推后（脚本需 CPU 调试） |\\n| Gemma 4 32.7B Dense | BF16 | ⏳ 等新服务器 SSH |\\n\\n## GPU 执行计划 (westd-13176, 4× RTX PRO 6000 96GB)\\n\\n**Phase 1 (NOW)**: plan_001 Qwen3 on 4 GPU (~20-40h) ✅ RUNNING\\n**Phase 2 (plan_001 完成后)**: plan_002 Llama4 on 4 GPU (~6-10h)\\n**Phase 3**: plan_008 Gemma4（新服务器）\\n**CPU 并行**: plan_013_v2; Llama4 脚本调试; CKA 分析准备\\n\\n## 近期任务\\n- [x] plan_001 启动 ✅ (PID 299313)\\n- [ ] plan_001 验证（Reviewer 独立核实 GPU 占用 + log 正常）\\n- [ ] plan_001 运行期间：CPU 调试 Llama4 extract_activations.py\\n- [ ] 新服务器 SSH → plan_008 (Gemma 4)\\n- [ ] plan_001 完成 → 立即启动 plan_002 (Llama4)\\n- [ ] plan_011 CKA full-scale — 依赖 plan_001/002 activations\\n- [ ] plan_003 CaCLR + high-dim MMD — 依赖 plan_001/002 activations\\n\\n## 阻塞项\\n- **Agent 反复卡死** (本 session 7 次) — 系统级 bug，Issue open\\n- **新服务器 SSH 未提供** — 阻塞 plan_008 (Gemma 4)\\n\\n## 关键发现\\n- **CKA Simpson's Paradox** (confirmed + strengthened): pooled ρ=+0.08 vs partial ρ=-0.29 (p=0.078), 符号反转。根因: compute_cka.py positional split bias → 已修正用 full data\\n- **plan_013 controls**: selectivity 在深层集中，correctness direction 非伪信号\\n\\n## GPU 预算\\n- **westd-13176**: 4× RTX PRO 6000 96GB — 当前全部用于 plan_001\\n- **新服务器(待开)**: 4× RTX 6000 96G\\n- P0 总计: 190 GPU-h; 实际墙钟 ~38h + plan_008 新服务器并行\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D019 | 2026-05-21 | Swap execution order: plan_001 (Qwen3) first, plan | plan_001, plan_002 |\\n| D018 | 2026-05-21 | Llama4 and Qwen3 extraction must serialize on 4-GP | plan_002, plan_001 |\\n| D017 | 2026-05-21 | Float16 activation storage + parallel extraction o | plan_001, plan_002 |\\n| D016 | 2026-05-21 | Dream #4 processed (3.5/3/2 on ACL 1-5 scale). Add | plan_003, plan_008 |\\n| D015 | 2026-05-21 | Re-dream processed (4/FAIL/3). P0 structurally app | plan_003, plan_013, plan_001, plan_002 |\\n| D014 | 2026-05-21 | Dream median Action Matrix: 3.5/5 Borderline Accep | plan_010, plan_002, plan_008 |\\n| D013 | 2026-05-21 | Depth-transfer narrative correction: overall posit | plan_013, mvp_001 |\\n| D012 | 2026-05-21 | Novelty strategy: CKA partial correlation (plan_01 | plan_011, plan_013, plan_012 |\\n| D011 | 2026-05-21 | Revert to parallel download: Llama4 (66GB) + Qwen3 | plan_001, plan_002 |\\n| D010 | 2026-05-20 | GlobalMMLU data decisions: test 70/30 split for Ca | — |\\n\\n\\n\\n\", \"total_chars\": 3285, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b10bcb2-2381-4f13-8669-6500768ec9d1",
  "isSidechain": true,
  "promptId": "daded219-2295-49e3-ac22-87f6bbbc54c9",
  "agentId": "a95da934c42f8700a",
  "type": "user",
  "uuid": "9d61f3d2-00df-43f4-b923-6fae590ff1b3",
  "sourceToolAssistantUUID": "6b10bcb2-2381-4f13-8669-6500768ec9d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-21T13:52:17.169Z_

Now let me read the actual experiment data/results to understand what was really run versus what the paper claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d61f3d2-00df-43f4-b923-6fae590ff1b3",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpmBmdya1kdxtXNCL9z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4b65e8f-7462-42ad-9146-9669df279feb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdVP5ZDch5ssphpkzGboFX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4478,
      "cache_read_input_tokens": 32988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4478,
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

_source line 28 · 2026-05-21T13:52:17.643Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01C9XL6RDBbc3B4nxjPELGhY`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "paper_framing.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4b65e8f-7462-42ad-9146-9669df279feb",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpmBmdya1kdxtXNCL9z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a624ed1-c44f-4b11-80b8-569a2373352d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdVP5ZDch5ssphpkzGboFX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4478,
      "cache_read_input_tokens": 32988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4478,
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

_source line 29 · 2026-05-21T13:52:17.653Z_

<details><summary>↩ Tool result · `toolu_01C9XL6RDBbc3B4nxjPELGhY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/paper_framing.md\", \"content\": \"# Paper Framing — xling_calib_direction\\n\\n## Target Venue\\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\\n- Core submission: 3 models (Qwen3-235B MoE + Llama 4 Scout MoE + Gemma 4 31B Dense) × 20 languages × all contributions\\n- Camera-ready extension: 30+ languages\\n\\n## Core Insight\\nThe model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. Deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages in pilot), but the Pareto frontier reveals a local tradeoff at the deepest layers: final 1–3 layers gain marginal English AUROC (+0.8pp) at the cost of transfer degradation (1.5–4pp in 3/5 languages). This local tradeoff shape is architecture-dependent (strong on Qwen, weak on Llama), and combines with the geometric CKA insight to provide a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\\n\\n## Core Claims (4, causal chain)\\n\\n### Claim 1 — Pareto Frontier (Discovery)\\nCross-lingual correctness probes show that deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages), but the deepest layers exhibit a local Pareto tradeoff where marginal English gains trade against transfer quality. This local tradeoff varies across architectures: on Qwen, the final layers consistently degrade transfer (3/5 languages, 1.5–4pp); on Llama, the tradeoff is language-specific. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\\n- Full evidence: 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense) × 20 languages × all layers × 5 transfer conditions. Dense vs MoE contrast addresses architecture confound (D016). Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\\n\\n### Claim 2 — Decomposition (Analysis)\\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\\n\\n### Claim 3 — CaCLR (Method / Diagnostic)\\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space. **Defense**: 1-D is the principled choice — MMD should match probe OUTPUT distributions (calibration target), not activation-space distributions (3584-D where MMD is statistically unreliable due to curse of dimensionality). High-dimensional activation-space MMD would be an alignment objective, not a calibration objective. Frame as \\\"principled scope\\\" not \\\"design limitation.\\\"\\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\\n\\n### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)\\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty (\\\"method replication to more languages\\\"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).\\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\\n\\n### Key Empirical Contributions (elevated from appendix to main body, D012)\\n- **Control task methodological warning**: English probing controls (Hewitt & Liang selectivity) show selectivity concentrated in deeper layers (L20+, selectivity >0.20), with shallow layers near chance — raising concerns that shallow-layer positive transfer in low-resource languages may reflect capacity artifacts. Cross-lingual control experiments planned to quantify the fraction. First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.\\n- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.\\n- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.\\n\\n## Story Spine\\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\\n- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) English probing controls reveal layer-dependent selectivity, suggesting shallow-layer low-resource results may be capacity artifacts (control task warning for the field; cross-lingual quantification pending); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the local Pareto tradeoff at the deepest layers (overall depth-transfer trend is positive), decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.\\n- **Headline template (method success)**: \\\"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\\\"\\n- **Headline template (negative result)**: \\\"Cross-lingual correctness probe transfer reveals architecture-dependent depth effects; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs is the most effective label-free transfer method.\\\" Note: linear projection is \\\"the only label-free method that consistently improves over zero-shot across resource tiers\\\" — NOT \\\"only viable path.\\\" Zero-shot is viable for high-resource (AUROC>0.60); few-shot (100 labels) may outperform linear projection in absolute terms. CaCLR outcome pending. The value proposition is zero correctness labels + cross-tier consistency, not absolute best performance.\\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\\n\\n## Field-Level Significance\\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\\n\\n## Anticipated Reviewer Concerns & Responses\\n1. **\\\"Xiao et al. already did this\\\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier.\\n\\n... [截断: 省略 7335 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 19335, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a624ed1-c44f-4b11-80b8-569a2373352d",
  "isSidechain": true,
  "promptId": "daded219-2295-49e3-ac22-87f6bbbc54c9",
  "agentId": "a95da934c42f8700a",
  "type": "user",
  "uuid": "d9f1a202-54a2-40a7-b1f5-0e578daa6ea9",
  "sourceToolAssistantUUID": "9a624ed1-c44f-4b11-80b8-569a2373352d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T13:52:18.810Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01JqFXtKfwrLnHDyn7xG65D2`</summary>

```json
{
  "pattern": "artifacts/dream_reports/dream_20260521T122458/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9f1a202-54a2-40a7-b1f5-0e578daa6ea9",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpmBmdya1kdxtXNCL9z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9ab0da3-8cdc-451a-8492-acf6048b194d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdVP5ZDch5ssphpkzGboFX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4478,
      "cache_read_input_tokens": 32988,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4478
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 32988,
          "cache_creation_input_tokens": 4478,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4478,
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

_source line 31 · 2026-05-21T13:52:18.823Z_

<details><summary>↩ Tool result · `toolu_01JqFXtKfwrLnHDyn7xG65D2`</summary>

```text
artifacts/dream_reports/dream_20260521T122458/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260521T122458/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260521T122458/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260521T122458/logs/orchestrator.log
artifacts/dream_reports/dream_20260521T122458/logs/phase2_median_attempt1.log
artifacts/dream_reports/dream_20260521T122458/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260521T122458/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260521T122458/best/experiment_data.json
artifacts/dream_reports/dream_20260521T122458/best/paper_framing.md
artifacts/dream_reports/dream_20260521T122458/best/references.bib
artifacts/dream_reports/dream_20260521T122458/best/paper.tex
artifacts/dream_reports/dream_20260521T122458/best/paper.bbl
artifacts/dream_reports/dream_20260521T122458/best/paper.blg
artifacts/dream_reports/dream_20260521T122458/best/paper.aux
artifacts/dream_reports/dream_20260521T122458/best/paper.out
artifacts/dream_reports/dream_20260521T122458/best/paper.pdf
artifacts/dream_reports/dream_20260521T122458/best/paper.log
artifacts/dream_reports/dream_20260521T122458/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260521T122458/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260521T122458/median/experiment_data.json
artifacts/dream_reports/dream_20260521T122458/median/paper_framing.md
artifacts/dream_reports/dream_20260521T122458/median/paper.tex
artifacts/dream_reports/dream_20260521T122458/median/paper.aux
artifacts/dream_reports/dream_20260521T122458/median/paper.out
artifacts/dream_reports/dream_20260521T122458/median/paper.pdf
artifacts/dream_reports/dream_20260521T122458/median/paper.log
artifacts/dream_reports/dream_20260521T122458/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260521T122458/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260521T122458/worst/experiment_data.json
artifacts/dream_reports/dream_20260521T122458/worst/paper_framing.md
artifacts/dream_reports/dream_20260521T122458/worst/paper.tex
artifacts/dream_reports/dream_20260521T122458/worst/paper.aux
artifacts/dream_reports/dream_20260521T122458/worst/paper.out
artifacts/dream_reports/dream_20260521T122458/worst/paper.pdf
artifacts/dream_reports/dream_20260521T122458/worst/paper.log
artifacts/dream_reports/dream_20260521T122458/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260521T122458/best/review_context.yaml
artifacts/dream_reports/dream_20260521T122458/best/review_report.md
artifacts/dream_reports/dream_20260521T122458/logs/review_best.log
artifacts/dream_reports/dream_20260521T122458/median/review_context.yaml
artifacts/dream_reports/dream_20260521T122458/logs/review_median.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9ab0da3-8cdc-451a-8492-acf6048b194d",
  "isSidechain": true,
  "promptId": "daded219-2295-49e3-ac22-87f6bbbc54c9",
  "agentId": "a95da934c42f8700a",
  "type": "user",
  "uuid": "f955270f-fb6a-4543-9e5e-6e9bfeb38210",
  "sourceToolAssistantUUID": "f9ab0da3-8cdc-451a-8492-acf6048b194d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-21T13:52:23.624Z_

Let me check the experiment data, imagined experiments, and the review context to understand what data is real vs. projected.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f955270f-fb6a-4543-9e5e-6e9bfeb38210",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpmZHT5gjzS8rAqmGGi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1835a3f7-2120-4f11-a374-261926d2b8cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLanRC7XnUuxEVXZUg616X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4336,
      "cache_read_input_tokens": 37466,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4336,
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

_source line 33 · 2026-05-21T13:52:24.566Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EbhMS6cVApTP74Mv4yR4YN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1835a3f7-2120-4f11-a374-261926d2b8cf",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpmZHT5gjzS8rAqmGGi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da1ffee7-7fed-4281-9ae5-4ca621b5452e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLanRC7XnUuxEVXZUg616X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4336,
      "cache_read_input_tokens": 37466,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4336,
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

_source line 34 · 2026-05-21T13:52:24.859Z_

<details><summary>↩ Tool result · `toolu_01EbhMS6cVApTP74Mv4yR4YN`</summary>

```text
1	tier: best
2	narrative_guidance: 'Method contribution paper — 因果链完整：Pareto discovery（architecture-dependent
3	  depth-transferability tradeoff with overall positive depth-transfer trend）→ Decomposition
4	  explains it（difficulty transfers, capability does not）→ CaCLR solves it（consistency
5	  loss shifts Pareto frontier, +3.3pp mean, 14/20 languages improved）→ CKA geometric
6	  explanation reveals why（Simpson''s Paradox confirmed across 3 architectures, partial
7	  rho +0.44 mean, p<0.01）。四条 claim 全力度支撑。Headline: "CaCLR-trained correctness probes
8	  reduce non-English ECE by 38% requiring zero target-language labels." Control task
9	  warning（10% cross-lingual artifact rate） 和 linear projection sample efficiency（~40
10	  pairs to 95%）作为 elevated empirical contributions 进入 main body。Procrustes effect
11	  reversal（threshold ~0.52）为 practitioner 提供直接指导。 三个架构（Qwen3 MoE + Llama4 MoE + Gemma4
12	  Dense）消除架构混淆因子——phenomenon 是 transformer depth 的 universal property。Mean EN AUROC
13	  0.818（range 0.805–0.835），ZS 20-lang mean 0.767， gap 5.2pp。所有 key metrics 落在 best
14	  区间内。
15	
16	  '
17	imagined_experiments:
18	- name: Full Pareto Frontier — Qwen3-235B-A22B (MoE)
19	  plan_id: plan_001
20	  description: '94-layer MoE (INT4, ~22B active), 24 probed layers (every 4th: L0,L4,...,L92),
21	    20 typologically diverse languages, English logistic regression probes, 5 transfer
22	    conditions: zero-shot, mean-shift, linear projection (200 pairs), few-shot 25/100,
23	    CaCLR (optimal α=0.1, β=0.05 from plan_003)。验证 MVP 发现的 positive depth-transfer
24	    trend 和 local deep-layer Pareto tradeoff 在大 MoE 模型上放大。
25	
26	    '
27	  expected_results:
28	    en_best_auroc: 0.835
29	    en_best_layer_idx: 68
30	    en_best_depth_pct: 72
31	    en_auroc_range:
32	    - 0.59
33	    - 0.835
34	    en_ece_raw_best: 0.172
35	    zs_mean_auroc_20lang_at_zs_optimal: 0.775
36	    zs_best_transfer_layer_idx: 48
37	    zs_best_transfer_depth_pct: 51
38	    zs_pass_rate_auroc_gt_058: 19
39	    zs_fail_langs:
40	    - yo
41	    zs_auroc_by_tier:
42	      HIGH_mean: 0.817
43	      MID_mean: 0.788
44	      LOW_mean: 0.693
45	    zs_auroc_selected:
46	      zh: 0.83
47	      es: 0.82
48	      fr: 0.82
49	      de: 0.82
50	      ja: 0.81
51	      nl: 0.81
52	      pt: 0.81
53	      ar: 0.8
54	      hi: 0.79
55	      ko: 0.79
56	      ru: 0.8
57	      tr: 0.78
58	      vi: 0.77
59	      id: 0.79
60	      pl: 0.79
61	      uk: 0.78
62	      sw: 0.72
63	      bn: 0.73
64	      te: 0.67
65	      yo: 0.575
66	    overall_spearman_depth_vs_zs:
67	      global_rho: 0.68
68	      global_p: 0.0003
69	    per_lang_spearman_rho_median: 0.62
70	    per_lang_positive_rho_count: 17
71	    per_lang_significant_positive_count: 14
72	    per_lang_negative_rho_langs:
73	    - yo
74	    - te
75	    - sw
76	    pareto_tradeoff_langs_count: 15
77	    pareto_en_optimal_layer: 68
78	    pareto_zs_optimal_layer: 48
79	    pareto_depth_gap_layers: 20
80	    pareto_zs_drop_at_en_optimal_pp: 3.8
81	    mean_shift_delta_auroc: 0.0
82	    linproj_200pairs_mean_auroc: 0.793
83	    linproj_200pairs_delta_pp: 1.8
84	    fewshot_25_mean_auroc: 0.762
85	    fewshot_100_mean_auroc: 0.788
86	    caclr_mean_auroc: 0.812
87	    caclr_delta_vs_zs_pp: 3.7
88	  result_rationale: 'Qwen3-235B 的 22B active params 比 MVP Qwen2.5-7B 多 ~3×。Probing
89	    scaling 预期 EN AUROC 从 0.754 提升至 0.835：更大模型在 intermediate layers 编码更清晰的 correctness
90	    signal， 因为 pretraining loss 更低 → 内部 representations 对 factual accuracy 更 informative。
91	
92	    Overall positive depth-transfer trend（median per-lang Spearman ρ=+0.62）因为更深层 encode
93	    更多 semantic content → 更好的 correctness discrimination，且 correctness direction 的
94	    cross-lingual alignment 在 shallow-to-mid layers 持续改善（CKA 在 0-50% depth 下降缓慢）。
95	    17/20 languages 有 positive ρ，3 个 negative 的（yo/te/sw）是 LOW-resource：这些语言在 Qwen3
96	    pretraining corpus 中占比极低（<0.1%），ZS AUROC 的 depth profile 呈倒 U 形 （peak 在 ~40% depth
97	    而非 >50%），因为深层的 language-specific specialization 对这些语言 反而有害。
98	
99	    Local Pareto tradeoff：从 ZS-optimal (L48, 51% depth) 到 EN-optimal (L68, 72% depth)，
100	    EN 增加 2pp（0.815→0.835）但 ZS 平均下降 3.8pp（0.775→0.737）。这一 tradeoff 在 15/20 languages
101	    上可观测（ZS-optimal ≠ EN-optimal，gap >1.5pp）。94 层深网络比 28 层 MVP 有 更大的 specialization
102	    空间，使 EN-optimal 与 ZS-optimal 之间的 depth gap 从 MVP 的 3 层 扩大至 20 层（22pp depth）。
103	
104	    MoE routing 在深层产生 language-specific expert activation patterns，加速 CKA cliff 下降，导致
105	    Qwen3 的 Pareto tradeoff 比 Llama4/Gemma4 更 pronounced（15/20 vs 10-12/20）。
106	
107	    Mean-shift ΔAUROC ≡ 0：StandardScaler + LR 下 mean-shift 对 AUROC 无影响（rank-invariant,
108	    MVP 中已数学证明并实验验证）。
109	
110	    Linear projection (+1.8pp) 通过 Procrustes 捕获 correctness subspace 旋转。 CaCLR (+3.7pp)
111	    通过 end-to-end 优化超越 linear projection。 Few-shot-100 (+1.3pp) 在 full-scale 上弱于 ZS
112	    因为 100 个 labeled samples 对 14K train set 的 probe 参数贡献边际很小。
113	
114	    '
115	  tables:
116	  - name: 'Table 1: Qwen3-235B Pareto Frontier (selected layers)'
117	    columns:
118	    - layer_idx
119	    - depth_pct
120	    - en_auroc
121	    - zs_mean_20
122	    - zs_drop_vs_en_pp
123	    - on_pareto
124	    rows:
125	    - - 4
126	      - 4
127	      - 0.59
128	      - 0.582
129	      - 0.8
130	      - false
131	    - - 12
132	      - 13
133	      - 0.645
134	      - 0.636
135	      - 0.9
136	      - false
137	    - - 20
138	      - 21
139	      - 0.71
140	      - 0.7
141	      - 1.0
142	      - false
143	    - - 28
144	      - 30
145	      - 0.752
146	      - 0.74
147	      - 1.2
148	      - false
149	    - - 36
150	      - 38
151	      - 0.785
152	      - 0.77
153	      - 1.5
154	      - false
155	    - - 40
156	      - 43
157	      - 0.798
158	      - 0.779
159	      - 1.9
160	      - false
161	    - - 44
162	      - 47
163	      - 0.808
164	      - 0.782
165	      - 2.6
166	      - false
167	    - - 48
168	      - 51
169	      - 0.815
170	      - 0.775
171	      - 4.0
172	      - true
173	    - - 52
174	      - 55
175	      - 0.822
176	      - 0.768
177	      - 5.4
178	      - true
179	    - - 56
180	      - 60
181	      - 0.828
182	      - 0.757
183	      - 7.1
184	      - true
185	    - - 60
186	      - 64
187	      - 0.832
188	      - 0.745
189	      - 8.7
190	      - true
191	    - - 64
192	      - 68
193	      - 0.834
194	      - 0.738
195	      - 9.6
196	      - true
197	    - - 68
198	      - 72
199	      - 0.835
200	      - 0.737
201	      - 9.8
202	      - true
203	    - - 72
204	      - 77
205	      - 0.834
206	      - 0.725
207	      - 10.9
208	      - false
209	    - - 76
210	      - 81
211	      - 0.83
212	      - 0.71
213	      - 12.0
214	      - false
215	    - - 80
216	      - 85
217	      - 0.822
218	      - 0.695
219	      - 12.7
220	      - false
221	    - - 84
222	      - 89
223	      - 0.815
224	      - 0.678
225	      - 13.7
226	      - false
227	    - - 88
228	      - 94
229	      - 0.805
230	      - 0.66
231	      - 14.5
232	      - false
233	    - - 92
234	      - 98
235	      - 0.79
236	      - 0.642
237	      - 14.8
238	      - false
239	  - name: 'Table 2: Per-Language Spearman ρ (depth vs ZS AUROC), Qwen3'
240	    columns:
241	    - language
242	    - tier
243	    - spearman_rho
244	    - p_value
245	    - significant_at_005
246	    rows:
247	    - - zh
248	      - HIGH
249	      - 0.75
250	      - 0.0001
251	      - true
252	    - - es
253	      - HIGH
254	      - 0.72
255	      - 0.0002
256	      - true
257	    - - fr
258	      - HIGH
259	      - 0.7
260	      - 0.0003
261	      - true
262	    - - de
263	      - HIGH
264	      - 0.73
265	      - 0.0002
266	      - true
267	    - - ja
268	      - HIGH
269	      - 0.68
270	      - 0.0005
271	      - true
272	    - - nl
273	      - HIGH
274	      - 0.71
275	      - 0.0003
276	      - true
277	    - - pt
278	      - HIGH
279	      - 0.69
280	      - 0.0004
281	      - true
282	    - - ar
283	      - MID
284	      - 0.67
285	      - 0.0006
286	      - true
287	    - - hi
288	      - MID
289	      - 0.62
290	      - 0.002
291	      - true
292	    - - ko
293	      - MID
294	      - 0.65
295	      - 0.001
296	      - true
297	    - - ru
298	      - MID
299	      - 0.68
300	      - 0.0005
301	      - true
302	    - - tr
303	      - MID
304	      - 0.6
305	      - 0.003
306	      - true
307	    - - vi
308	      - MID
309	      - 0.55
310	      - 0.007
311	      - true
312	    - - id
313	      - MID
314	      - 0.63
315	      - 0.002
316	      - true
317	    - - pl
318	      - MID
319	      - 0.62
320	      - 0.002
321	      - true
322	    - - uk
323	      - MID
324	      - 0.58
325	      - 0.005
326	      - true
327	    - - sw
328	      - LOW
329	      - -0.12
330	      - 0.58
331	      - false
332	    - - bn
333	      - LOW
334	      - 0.35
335	      - 0.1
336	      - false
337	    - - te
338	      - LOW
339	      - -0.08
340	      - 0.72
341	      - false
342	    - - yo
343	      - LOW
344	      - -0.18
345	      - 0.42
346	      - false
347	  - name: 'Table 3: Transfer Conditions at ZS-Optimal Layer (L48), Qwen3'
348	    columns:
349	    - condition
350	    - mean_auroc_20
351	    - delta_vs_zs_pp
352	    - requires
353	    rows:
354	    - - zero-shot
355	      - 0.775
356	      - 0.0
357	      - —
358	    - - mean-shift
359	      - 0.775
360	      - 0.0
361	      - —
362	    - - linear_proj_200
363	      - 0.793
364	      - 1.8
365	      - 200 parallel pairs
366	    - - few-shot-25
367	      - 0.762
368	      - -1.3
369	      - 25 labeled per lang
370	    - - few-shot-100
371	      - 0.788
372	      - 1.3
373	      - 100 labeled per lang
374	    - - CaCLR
375	      - 0.812
376	      - 3.7
377	      - parallel activations
378	  figures_description:
379	  - 'Figure 1a: EN AUROC (blue) and ZS mean AUROC (orange) vs normalized depth (%).
380	    Both rise together until ~50% depth, then diverge: EN continues to ~72%, ZS peaks
381	    and declines. Shaded region between curves from 51-72% depth marks Pareto zone.
382	
383	    '
384	  - 'Figure 1b: Heatmap — ZS AUROC by language (y-axis, ordered HIGH→MID→LOW) × layer
385	    index (x-axis). Warm yellow band in mid-depth (30-55%), cooling gradient toward
386	    deep layers, LOW-resource rows cool earliest.
387	
388	    '
389	  analysis: 'Qwen3-235B 展现 strong, consistent positive depth-transfer trend（global
390	    ρ=+0.68, p=0.0003）和 pronounced local Pareto tradeoff（15/20 langs）。EN-optimal (L68)
391	    与 ZS-optimal (L48) 相距 20 层，远大于 MVP 的 3 层，确认 tradeoff 在大模型上放大。 14/20 languages
392	    的 per-language ρ 显著为正，表明 "deeper is generally better for transfer" 是跨语言一致的。3 个
393	    LOW-resource languages (yo/te/sw) 显示 negative/near-zero ρ， 因为这些语言的 correctness
394	    signal quality 在深层退化快于 probe discrimination 的提升。 CaCLR 在 ZS-optimal layer 提供 +3.7pp，是所有
395	    label-free methods 中最优。
396	
397	    '
398	- name: Full Pareto Frontier — Llama 4 Scout (MoE)
399	  plan_id: plan_002
400	  description: '48-layer MoE (W4A16, 17B×16E, top-2 routing), 12 probed layers (every
401	    4th: L0,L4,...,L44,L47), 20 languages, 5 transfer conditions。验证 MVP Llama-3.1-8B
402	    的 weaker/mixed tradeoff pattern 是否是 Llama 架构家族特征。
403	
404	    '
405	  expected_results:
406	    en_best_auroc: 0.815
407	    en_best_layer_idx: 36
408	    en_best_depth_pct: 75
409	    en_auroc_range:
410	    - 0.57
411	    - 0.815
412	    en_ece_raw_best: 0.178
413	    zs_mean_auroc_20lang_at_zs_optimal: 0.765
414	    zs_best_transfer_layer_idx: 28
415	    zs_best_transfer_depth_pct: 58
416	    zs_pass_rate_auroc_gt_058: 17
417	    zs_fail_langs:
418	    - yo
419	    - te
420	    - sw
421	    zs_auroc_by_tier:
422	      HIGH_mean: 0.808
423	      MID_mean: 0.778
424	      LOW_mean: 0.672
425	    per_lang_spearman_rho_median: 0.72
426	    per_lang_positive_rho_count: 19
427	    per_lang_significant_positive_count: 16
428	    per_lang_negative_rho_langs:
429	    - yo
430	    pareto_tradeoff_langs_count: 10
431	    pareto_zs_drop_at_en_optimal_pp: 2.5
432	    mean_shift_delta_auroc: 0.0
433	    linproj_200pairs_mean_auroc: 0.781
434	    fewshot_100_mean_auroc: 0.778
435	    caclr_mean_auroc: 0.798
436	    caclr_delta_vs_zs_pp: 3.3
437	  result_rationale: 'Llama 4 Scout 延续 MVP Llama-3.1-8B 的 weaker tradeoff 模式但在关键方面加强。
438	    Per-language Spearman median ρ=+0.72 高于 Qwen3 (0.62)，因为 Llama4 仅 48 层—— 更少的深层
439	    specialization 空间意味着 ZS AUROC 的下降区间更短（最后 ~20% 层）， 而上升区间（前 58% 层）主导了 overall correlation。19/20
440	    languages 有 positive ρ （仅 yo negative）。
441	
442	    Pareto tradeoff 仅 10/20 languages（vs Qwen3 15/20），且 ZS drop 仅 2.5pp （vs Qwen3
443	    3.8pp）。这与 MVP 一致（Llama-3.1-8B: 2/5 langs showed tradeoff, ar/ko 在深层反而改善）。归因于 Meta
444	    的 multilingual training recipe：Llama4 在 pretraining 中对中高资源语言的 cross-lingual alignment
445	    更均匀，深层 language-specific routing 效应弱于 Qwen3。
446	
447	    EN best AUROC 0.815 低于 Qwen3 的 0.835，部分因为 17B active params < 22B (Qwen3)，部分因为
448	    W4A16 量化引入 ~0.3pp noise（plan_010 验证）。
449	
450	    Architecture-dependent tradeoff strength 是 Claim 1 核心： Qwen3 strong (15/20, -3.8pp)
451	    vs Llama4 weak (10/20, -2.5pp)， median per-lang ρ 差异虽然在同一方向（都正），但 Qwen3 的 Pareto
452	    zone 更宽。
453	
454	    '
455	  tables:
456	  - name: 'Table 4: Llama 4 Scout Pareto Frontier'
457	    columns:
458	    - layer_idx
459	    - depth_pct
460	    - en_auroc
461	    - zs_mean_20
462	    - on_pareto
463	    rows:
464	    - - 4
465	      - 8
466	      - 0.57
467	      - 0.562
468	      - false
469	    - - 8
470	      - 17
471	      - 0.64
472	      - 0.63
473	      - false
474	    - - 12
475	      - 25
476	      - 0.7
477	      - 0.69
478	      - false
479	    - - 16
480	      - 33
481	      - 0.74
482	      - 0.728
483	      - false
484	    - - 20
485	      - 42
486	      - 0.768
487	      - 0.755
488	      - false
489	    - - 24
490	      - 50
491	      - 0.785
492	      - 0.764
493	      - false
494	    - - 28
495	      - 58
496	      - 0.798
497	      - 0.765
498	      - true
499	    - - 32
500	      - 67
501	      - 0.808
502	      - 0.755
503	      - true
504	    - - 36
505	      - 75
506	      - 0.815
507	      - 0.742
508	      - true
509	    - - 40
510	      - 83
511	      - 0.81
512	      - 0.722
513	      - false
514	    - - 44
515	      - 92
516	      - 0.795
517	      - 0.695
518	      - false
519	    - - 47
520	      - 98
521	      - 0.778
522	      - 0.668
523	      - false
524	  - name: 'Table 5: Architecture-Dependent Pareto Summary'
525	    columns:
526	    - metric
527	    - Qwen3_235B
528	    - Llama4_Scout
529	    - interpretation
530	    rows:
531	    - - en_best_auroc
532	      - 0.835
533	      - 0.815
534	      - both strong, Qwen slightly higher (22B>17B active)
535	    - - zs_mean_at_zs_opt
536	      - 0.775
537	      - 0.765
538	      - comparable transfer quality
539	    - - per_lang_rho_median
540	      - '+0.62'
541	      - '+0.72'
542	      - both positive; Llama higher (fewer deep layers)
543	    - - positive_rho_langs
544	      - 17/20
545	      - 19/20
546	      - Llama more consistent
547	    - - pareto_tradeoff_langs
548	      - 15/20
549	      - 10/20
550	      - Qwen stronger tradeoff
551	    - - pareto_zs_drop_pp
552	      - 3.8
553	      - 2.5
554	      - Qwen steeper
555	    - - best_transfer_depth_pct
556	      - 51
557	      - 58
558	      - comparable mid-depth zone
559	  figures_description:
560	  - 'Figure 2: Overlaid Pareto frontiers (normalized depth %). Qwen3 (blue) and Llama4
561	    (orange) share similar shape but Qwen3 has wider divergence zone between EN and
562	    ZS curves. Both peak in transfer at 51-58% depth.
563	
564	    '
565	  - 'Figure 3: Per-language Spearman ρ distribution — violin plots. Both architectures
566	    cluster on the positive side. Llama4 tighter (0.4-0.85), Qwen3 wider spread (−0.2
567	    to 0.8) with 3 LOW-resource outliers below zero.
568	
569	    '
570	  analysis: 'Llama4 与 Qwen3 的对比确认 architecture-dependent tradeoff strength。两者都有 positive
571	    depth-transfer trend 和 local Pareto tradeoff，但 effect sizes 不同： Qwen3 在 15/20
572	    languages 上有 measurable tradeoff（mean drop 3.8pp），Llama4 仅 10/20（mean drop 2.5pp）。差异无法从
573	    domain adaptation theory 预测—— 这是 architecture/training-recipe 的 empirical finding。Best-transfer
574	    depth converges to 51-58%，暗示 universal "mid-depth transfer zone"。
575	
576	    '
577	- name: Full Pareto Frontier — Gemma 4 31B Dense
578	  plan_id: plan_008
579	  description: '60 text layers, dense architecture, BF16 (~62.5GB, single 96GB GPU),
580	    16 probed layers (every 4th + final: L0,L4,...,L56,L59), 20 languages, 5 transfer
581	    conditions。 P0 priority — provides dense vs MoE architectural contrast, eliminates
582	    confound between architecture type and tradeoff strength。无量化 → 消除量化 confound。
583	
584	    '
585	  expected_results:
586	    en_best_auroc: 0.805
587	    en_best_layer_idx: 44
588	    en_best_depth_pct: 73
589	    en_auroc_range:
590	    - 0.57
591	    - 0.805
592	    en_ece_raw_best: 0.185
593	    zs_mean_auroc_20lang_at_zs_optimal: 0.76
594	    zs_best_transfer_layer_idx: 36
595	    zs_best_transfer_depth_pct: 60
596	    zs_pass_rate_auroc_gt_058: 18
597	    zs_fail_langs:
598	    - yo
599	    - te
600	    zs_auroc_by_tier:
601	      HIGH_mean: 0.802
602	      MID_mean: 0.772
603	      LOW_mean: 0.67
604	    per_lang_spearman_rho_median: 0.65
605	    per_lang_positive_rho_count: 18
606	    per_lang_significant_positive_count: 14
607	    pareto_tradeoff_langs_count: 12
608	    pareto_zs_drop_at_en_optimal_pp: 3.0
609	    linproj_200pairs_mean_auroc: 0.776
610	    caclr_mean_auroc: 0.79
611	    caclr_delta_vs_zs_pp: 3.0
612	    simpson_partial_rho: 0.44
613	    simpson_partial_p: 0.004
614	  result_rationale: 'Gemma4 31B Dense 是三架构中唯一的 dense model，消除了 "MoE routing 导致 Pareto
615	    tradeoff" 的替代解释。EN best AUROC 0.805 低于两个 MoE 模型（0.835/0.815）， 因为 31B dense < 22B/17B
616	    MoE active（MoE 的 expert routing 提供 effective capacity boost，使相同 active param 下
617	    probe 信号更强）。
618	
619	    Pareto tradeoff 在 12/20 languages 上可观测（介于 Qwen3 15/20 和 Llama4 10/20 之间），ZS drop
620	    3.0pp。Dense architecture 没有 routing-specific specialization， 但深层仍然发生 language-specific
621	    feature specialization（attention heads 在 deep layers 对不同语言的 subword patterns 有不同
622	    activation）。这证实 Pareto tradeoff 是 transformer depth 的 universal property，不是 MoE
623	    routing 的 artifact。
624	
625	    Simpson''s Paradox 在 dense 架构上同样成立（partial ρ=+0.44, p=0.004）， 确认 geometric insight
626	    是 architecture-universal。BF16 无量化 → 消除量化 distortion confound，使 CKA 和 subspace
627	    angle 分析更 reliable。
628	
629	    Per-lang Spearman median ρ=+0.65（介于 Qwen 0.62 和 Llama 0.72 之间）， 60 层提供的深层 specialization
630	    空间在两者之间。
631	
632	    '
633	  tables:
634	  - name: 'Table 6: Three-Architecture Comprehensive Summary'
635	    columns:
636	    - model
637	    - type
638	    - layers
639	    - en_best
640	    - zs_mean_20
641	    - en_zs_gap_pp
642	    - pareto_rho_median
643	    - pareto_langs
644	    - simpson_partial_rho
645	    - caclr_delta_pp
646	    rows:
647	    - - Qwen3-235B
648	      - MoE
649	      - 94
650	      - 0.835
651	      - 0.775
652	      - 6.0
653	      - '+0.62'
654	      - 15/20
655	      - '+0.48'
656	      - 3.7
657	    - - Llama4 Scout
658	      - MoE
659	      - 48
660	      - 0.815
661	      - 0.765
662	      - 5.0
663	      - '+0.72'
664	      - 10/20
665	      - '+0.41'
666	      - 3.3
667	    - - Gemma4 31B
668	      - Dense
669	      - 60
670	      - 0.805
671	      - 0.76
672	      - 4.5
673	      - '+0.65'
674	      - 12/20
675	      - '+0.44'
676	      - 3.0
677	    - - Mean (3 arch)
678	      - —
679	      - —
680	      - 0.818
681	      - 0.767
682	      - 5.2
683	      - '+0.66'
684	      - 37/60=62%
685	      - '+0.44'
686	      - 3.3
687	  figures_description:
688	  - 'Figure 9: Three-architecture Pareto frontiers overlaid on normalized depth (%).
689	    All three share the same qualitative shape: rising together until 50-60%, then
690	    diverging. Qwen (blue) widest divergence, Llama (orange) narrowest, Gemma (green)
691	    intermediate. Remarkably similar knee locations (51-60% depth).
692	
693	    '
694	  analysis: 'Three-architecture replication 是 universality claim 最强证据。Simpson''s Paradox
695	    在 3/3 architectures 上 confirmed (partial ρ range 0.41-0.48, all p<0.01)。 Dense
696	    vs MoE contrast minimal — phenomenon 是 transformer depth 的 property。 Mean EN AUROC
697	    0.818 在 [0.80, 0.86] 内。Mean gap 5.2pp 在 [4, 8] 内。 Pareto prevalence 62% 在 [0.5,
698	    0.75] 内。CaCLR 一致 +3.0-3.7pp。
699	
700	    '
701	- name: CKA Cross-Lingual Similarity & Simpson's Paradox
702	  plan_id: plan_011
703	  description: 'Linear CKA (EN vs each target) at every probed layer, 20 languages
704	    × 3 models。 核心分析：(a) same-layer cross-language correlation (n=20 per layer), (b)
705	    partial Spearman controlling for normalized depth — THE single most important
706	    analysis, (c) subspace angle quantitative analysis, (d) CKA cliff threshold identification。
707	    验证 pilot Simpson''s Paradox 在 full-scale 上 3 架构复现。
708	
709	    '
710	  expected_results:
711	    qwen3_raw_rho: -0.38
712	    qwen3_raw_p: 0.0001
713	    llama4_raw_rho: -0.42
714	    llama4_raw_p: 0.0001
715	    gemma4_raw_rho: -0.4
716	    gemma4_raw_p: 0.0001
717	    qwen3_partial_rho: 0.48
718	    qwen3_partial_p: 0.0018
719	    qwen3_partial_bootstrap_ci_95:
720	    - 0.3
721	    - 0.63
722	    llama4_partial_rho: 0.41
723	    llama4_partial_p: 0.0065
724	    llama4_partial_bootstrap_ci_95:
725	    - 0.21
726	    - 0.58
727	    gemma4_partial_rho: 0.44
728	    gemma4_partial_p: 0.0038
729	    gemma4_partial_bootstrap_ci_95:
730	    - 0.26
731	    - 0.6
732	    simpson_paradox_confirmed_all_3_arch: true
733	    qwen3_per_layer_positive_count_of_24: 19
734	    qwen3_per_layer_significant_count_of_24: 8
735	    llama4_per_layer_positive_count_of_12: 10
736	    llama4_per_layer_significant_count_of_12: 4
737	    gemma4_per_layer_positive_count_of_16: 13
738	    gemma4_per_layer_significant_count_of_16: 6
739	    cka_peak_depth_pct_range:
740	    - 15
741	    - 25
742	    cka_peak_value_range:
743	    - 0.82
744	    - 0.86
745	    transfer_collapse_cka_threshold: 0.35
746	    below_threshold_mean_zs_auroc: 0.6
747	    above_threshold_mean_zs_auroc: 0.74
748	    correctness_subspace_angle_within_layer_mean_deg: 12.8
749	    correctness_subspace_angle_within_layer_std_deg: 5.4
750	    correctness_subspace_angle_across_layer_mean_deg: 37.5
751	    correctness_subspace_angle_across_layer_std_deg: 10.8
752	    random_baseline_angle_deg: 87.1
753	  result_rationale: 'Simpson''s Paradox 的 causal mechanism：depth 同时作用于 CKA（deeper
754	    → representations diverge → CKA drops）和 ZS AUROC（deeper → EN probe更强 → higher
755	    absolute AUROC up to mid-depth），创造了 depth confound。Raw pooled correlation 为负：shallow
756	    layers 有 high CKA 但 low AUROC（probe 本身弱），deep layers 有 low CKA 但 moderate/declining
757	    AUROC。控制 depth 后，within 每个 layer，higher CKA 的语言确实有 better transfer， partial ρ
758	    为正。
759	
760	    MVP pilot（Llama, 5 langs × 9 layers）已展现 ρ=+0.41, p=0.006。Full-scale（20 langs ×
761	    12-24 layers per arch）增强统计 power：per-layer test 从 n=5 增至 n=20。 MVP Qwen pilot
762	    仅 ρ=+0.18 (p=0.274)，full-scale 上升至 +0.48 因为：(1) n 从 5 增至 20 语言，power 大幅提升；(2)
763	    20 语言覆盖更宽的 CKA 范围（增加了极低 CKA 的 yo/te 和高 CKA 的 nl/pt），扩大了 within-layer variance。
764	
765	    Subspace angle analysis 提供 structural grounding：correctness direction 在同一 layer
766	    内跨语言仅旋转 ~13°（near-universal），但跨 layer 旋转 ~38°（significant drift）， vs random baseline
767	    ~87°。这解释了为何 within-layer CKA 预测 transfer（correctness direction 对齐良好）但 raw pooled
768	    不预测（depth confound 混淆了 correctness 与 non- correctness dimensions 的 divergence）。
769	
770	    CKA cliff threshold ~0.35 直接解释了 architecture-dependent tradeoff 差异：Qwen3 的 CKA
771	    cliff 更陡（deep-layer CKA 下降更快因为 MoE routing），导致更多语言在 deep layers 穿越 0.35 threshold
772	    → strong tradeoff。Llama4 cliff 较缓 → weak tradeoff。 Gemma4（dense）cliff 速率介于两者之间。
773	
774	    '
775	  tables:
776	  - name: 'Table 7: Simpson''s Paradox — Raw vs Partial Correlation (3 Architectures)'
777	    columns:
778	    - model
779	    - analysis
780	    - spearman_rho
781	    - p_value
782	    - bootstrap_95CI
783	    - interpretation
784	    rows:
785	    - - Qwen3-235B
786	      - raw pooled
787	      - -0.38
788	      - <0.001
789	      - '[-0.46, -0.29]'
790	      - negative — depth confound
791	    - - Qwen3-235B
792	      - partial (controlling depth)
793	      - 0.48
794	      - 0.0018
795	      - '[+0.30, +0.63]'
796	      - positive — genuine geometric signal
797	    - - Llama4 Scout
798	      - raw pooled
799	      - -0.42
800	      - <0.001
801	      - '[-0.51, -0.32]'
802	      - negative — depth confound
803	    - - Llama4 Scout
804	      - partial (controlling depth)
805	      - 0.41
806	      - 0.0065
807	      - '[+0.21, +0.58]'
808	      - positive — genuine geometric signal
809	    - - Gemma4 31B
810	      - raw pooled
811	      - -0.4
812	      - <0.001
813	      - '[-0.49, -0.30]'
814	      - negative — depth confound
815	    - - Gemma4 31B
816	      - partial (controlling depth)
817	      - 0.44
818	      - 0.0038
819	      - '[+0.26, +0.60]'
820	      - positive — genuine geometric signal
821	  - name: 'Table 8: Subspace Angle Analysis (correctness direction, pooled across
822	      archs)'
823	    columns:
824	    - comparison_type
825	    - mean_angle_deg
826	    - std_deg
827	    - interpretation
828	    rows:
829	    - - within-layer cross-language
830	      - 12.8
831	      - 5.4
832	      - highly aligned — correctness direction is near-universal
833	    - - cross-layer same-language
834	      - 37.5
835	      - 10.8
836	      - significant drift — direction rotates with depth
837	    - - random baseline (shuffled)
838	      - 87.1
839	      - 2.0
840	      - near-orthogonal — confirms non-trivial signal
841	  - name: 'Table 9: CKA Heatmap Summary (Qwen3, mean across 20 langs by tier)'
842	    columns:
843	    - depth_pct
844	    - HIGH_CKA
845	    - MID_CKA
846	    - LOW_CKA
847	    - overall_CKA
848	    rows:
849	    - - 13
850	      - 0.87
851	      - 0.8
852	      - 0.64
853	      - 0.79
854	    - - 30
855	      - 0.85
856	      - 0.78
857	      - 0.6
858	      - 0.77
859	    - - 47
860	      - 0.7
861	      - 0.58
862	      - 0.38
863	      - 0.58
864	    - - 64
865	      - 0.5
866	      - 0.38
867	      - 0.24
868	      - 0.39
869	    - - 77
870	      - 0.4
871	      - 0.28
872	      - 0.16
873	      - 0.3
874	    - - 94
875	      - 0.27
876	      - 0.19
877	      - 0.1
878	      - 0.2
879	  figures_description:
880	  - 'Figure 4a: Simpson''s Paradox visualization (2-panel). Left: raw scatter (CKA
881	    vs ZS AUROC), depth-colored points, negative trend line. Right: partial residual
882	    plot after depth control, positive trend line. Sign reversal is dramatic.
883	
884	    '
885	  - 'Figure 4b: CKA × layer × language heatmap for all 3 architectures (3 panels).
886	    Clear gradient from warm (shallow, high CKA) to cool (deep, low CKA). LOW-resource
887	    rows cool faster. Qwen3 steepest gradient, Llama4 shallowest.
888	
889	    '
890	  - 'Figure 4c: CKA threshold scatter. ZS AUROC (y) vs CKA (x), all 3 archs pooled.
891	    Vertical dashed line at CKA=0.35. Below: scattered, mean ZS=0.60. Above: tight
892	    cluster, mean ZS=0.74.
893	
894	    '
895	  analysis: 'Simpson''s Paradox 在 3/3 architectures 上显著复现（partial ρ: 0.41-0.48, all
896	    p<0.01, all bootstrap CIs exclude zero）。这是本文核心几何洞见——不是 trivially expected from
897	    measurement overlap：sign reversal 从负到正是 non-trivial 的。Subspace angle analysis
898	    提供 mechanistic grounding。CKA cliff threshold ~0.35 connects Claim 1 (Pareto) with
899	    Claim 4 (geometry)。所有 partial correlations 的 bootstrap CIs 在 [0.3, 0.55] key metric
900	    range 内。
901	
902	    '
903	- name: CaCLR Implementation and Comparative Evaluation
904	  plan_id: plan_003
905	  description: 'L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency (MMD on 1-D probe logits
906	    + PCA-reduced activations)。English labels + parallel activations from GlobalMMLU
907	    test-split 70/30。 Compare vs zero-shot/mean-shift/linear-proj/few-shot across
908	    full Pareto frontier, 3 models × 20 languages。α sweep [0.01-10], β sweep [0.001-1.0]。扩展分析：CORAL
909	    loss 对比, high-dim MMD (PCA d=50/100), multi-seed (5 seeds), mixed β criterion
910	    (zh+sw)。
911	
912	    '
913	  expected_results:
914	    best_alpha: 0.1
915	    best_beta: 0.05
916	    caclr_mean_delta_auroc_vs_zs_pp: 3.3
917	    caclr_delta_at_deep_layers_pp: 4.5
918	    caclr_delta_at_shallow_layers_pp: 1.2
919	    caclr_langs_improved_of_20: 14
920	    caclr_langs_hurt_of_20: 1
921	    caclr_improvement_by_tier:
922	      HIGH_mean_delta_pp: 1.2
923	      HIGH_improved_of_7: 3
924	      MID_mean_delta_pp: 3.8
925	      MID_improved_of_9: 8
926	      LOW_mean_delta_pp: 6.5
927	      LOW_improved_of_4: 3
928	    beta_sweep:
929	      beta_0:
930	        delta_auroc_pp: 0.0
931	        delta_ece_pp: 0.0
932	      beta_0001:
933	        delta_auroc_pp: 0.5
934	        delta_ece_pp: -0.3
935	      beta_001:
936	        delta_auroc_pp: 1.6
937	        delta_ece_pp: -0.9
938	      beta_005:
939	        delta_auroc_pp: 3.3
940	        delta_ece_pp: -2.2
941	      beta_01:
942	        delta_auroc_pp: 3.0
943	        delta_ece_pp: -1.8
944	      beta_10:
945	        delta_auroc_pp: 0.6
946	        delta_ece_pp: -0.3
947	    alpha_sweep:
948	      alpha_001:
949	        ece_improvement_pp: 1.2
950	      alpha_01:
951	        ece_improvement_pp: 3.0
952	      alpha_10:
953	        ece_improvement_pp: 2.6
954	      alpha_100:
955	        ece_improvement_pp: -0.8
956	    component_ablation:
957	      bce_only_mean_auroc: 0.767
958	      bce_sbece_mean_auroc: 0.774
959	      bce_mmd_mean_auroc: 0.792
960	      bce_sbece_mmd_mean_auroc: 0.8
961	    high_dim_mmd:
962	      pca_50_delta_vs_zs_pp: 4.2
963	      pca_100_delta_vs_zs_pp: 3.8
964	      pca_50_vs_1d_delta_pp: 0.9
965	    coral_comparison:
966	      coral_1d_delta_pp: 2.8
967	      coral_pca50_delta_pp: 3.6
968	      mmd_vs_coral_1d_diff_pp: 0.5
969	    multi_seed_std_pp: 0.35
970	    mixed_beta_criterion_best_beta: 0.05
971	    mixed_beta_criterion_note: same optimum as EN-only; no systematic bias
972	    ece_reduction_vs_temp_scaling_pct: 38
973	    parallel_set_size_per_lang_mean: 2800
974	    parallel_set_size_per_lang_range:
975	    - 1900
976	    - 4100
977	    implementation_spec:
978	      mmd_kernel: Gaussian RBF, bandwidth=median heuristic
979	      optimizer: Adam, lr=1e-3, linear warmup 10%, cosine decay
980	      epochs: 50
981	      early_stopping: patience=10, monitor=val_auroc on 15% held-out from probe_train
982	      initialization: from standard LR solution
983	      batch_size: 256
984	      mmd_overlap: same items as BCE (overlapping)
985	  result_rationale: 'CaCLR 的 consistency loss (β·MMD) 强制 probe 学习 language-invariant
986	    features。
987	
988	    β sweep 的 inverted-U 形状源于 regularization dynamics：β=0.001 时 MMD gradient 太弱（被
989	    BCE gradient noise 淹没），β=1.0 时 MMD 主导优化（probe 牺牲 accuracy 来匹配 distributions，EN
990	    AUROC 下降 ~1.5pp）。Optimal β=0.05 平衡两者—— consistency gradient 足够影响 probe direction
991	    但不主导。
992	
993	    Deep-layer improvement (+4.5pp) 远大于 shallow (+1.2pp) 因为：deep layers 的 capability-specific
994	    component 更大（Claim 2 decomposition），CaCLR 的 consistency loss 恰好 target 这个 component。Shallow
995	    layers 的 transfer 本身就好（difficulty- dominant），CaCLR 提供的边际改善有限。
996	
997	    14/20 languages improved (10-16 range 内)：6 个 non-improving 主要是 HIGH-resource (zh/es/fr/de)
998	    在 shallow/mid layers 已接近 ceiling，CaCLR 的 distributional matching 在 already-aligned
999	    distributions 上无显著增益。1 个 hurt (yo) 因为 parallel activations 质量太差（translation artifacts
1000	    in GlobalMMLU Yoruba），MMD matching 反而引入 noise。
1001	
1002	    High-dim MMD (PCA-50) 优于 1-D (+4.2pp vs +3.3pp)：50-D space 捕获了更多 distributional
1003	    structure（不只 mean/variance，还有 covariance patterns）。但 PCA-100 略退（+3.8pp），curse
1004	    of dimensionality 开始影响 MMD estimation。 这表明 optimal dimensionality 在 d~50，与 correctness
1005	    subspace 的 effective rank 一致（~30-50 principal components capture 95% of probe-relevant
1006	    variance）。
1007	
1008	    CORAL (+2.8pp 1-D, +3.6pp PCA-50) 与 MMD 方向一致但 1-D 弱于 MMD（CORAL 匹配 second-order
1009	    statistics，在 1-D 只有 variance matching，信息量不如 kernel-based MMD）。PCA-50 下 CORAL 接近
1010	    MMD。这证实 distributional matching 一般性地 work， 非 MMD-specific。
1011	
1012	    Component ablation：BCE alone (probe baseline) → +SB-ECE (+0.7pp, calibration focus)
1013	    → +MMD (+2.5pp, consistency is the main contributor) → full CaCLR (+3.3pp, synergy
1014	    between calibration and consistency)。
1015	
1016	    ECE reduction 38% vs temperature scaling：CaCLR 在训练期间优化 calibration (SB-ECE) +
1017	    cross-lingual consistency (MMD)，比 post-hoc temperature scaling 更 effective，因为
1018	    temperature scaling 只缩放 logits（不改变 decision boundary） 而 CaCLR 修改了 probe 的 feature
1019	    extraction direction。
1020	
1021	    '
1022	  tables:
1023	  - name: 'Table 10: β Sweep — Consistency Loss Effect (3-arch average)'
1024	    columns:
1025	    - beta
1026	    - delta_auroc_vs_zs_pp
1027	    - delta_ece_vs_zs_pp
1028	    - note
1029	    rows:
1030	    - - 0.0
1031	      - 0.0
1032	      - 0.0
1033	      - BCE-only baseline
1034	    - - 0.001
1035	      - 0.5
1036	      - -0.3
1037	      - marginal — gradient noise dominates
1038	    - - 0.01
1039	      - 1.6
1040	      - -0.9
1041	      - clear positive signal emerges
1042	    - - 0.05
1043	      - 3.3
1044	      - -2.2
1045	      - optimal — best accuracy-consistency tradeoff
1046	    - - 0.1
1047	      - 3.0
1048	      - -1.8
1049	      - slight over-regularization
1050	    - - 1.0
1051	      - 0.6
1052	      - -0.3
1053	      - MMD dominates → probe accuracy degrades
1054	  - name: 'Table 11: CaCLR vs All Methods (at ZS-optimal layer, 3-arch average)'
1055	    columns:
1056	    - method
1057	    - auroc_mean_20
1058	    - ece_mean_20
1059	    - delta_vs_zs_pp
1060	    - requires
1061	    rows:
1062	    - - zero-shot
1063	      - 0.767
1064	      - 0.118
1065	      - 0.0
1066	      - —
1067	    - - mean-shift
1068	      - 0.767
1069	      - 0.118
1070	      - 0.0
1071	      - —
1072	    - - linear_proj_50
1073	      - 0.781
1074	      - 0.1
1075	      - 1.4
1076	      - 50 parallel pairs
1077	    - - linear_proj_200
1078	      - 0.783
1079	      - 0.097
1080	      - 1.6
1081	      - 200 parallel pairs
1082	    - - few-shot-25
1083	      - 0.754
1084	      - 0.108
1085	      - -1.3
1086	      - 25 labeled per lang
1087	    - - few-shot-100
1088	      - 0.785
1089	      - 0.09
1090	      - 1.8
1091	      - 100 labeled per lang
1092	    - - CaCLR (1-D MMD)
1093	      - 0.8
1094	      - 0.073
1095	      - 3.3
1096	      - parallel activations
1097	    - - CaCLR (PCA-50 MMD)
1098	      - 0.809
1099	      - 0.068
1100	      - 4.2
1101	      - parallel activations
1102	  - name: 'Table 12: Distributional Matching Comparison (PCA-50 space)'
1103	    columns:
1104	    - method
1105	    - dim
1106	    - delta_vs_zs_pp
1107	    - note
1108	    rows:
1109	    - - MMD-1D
1110	      - 1
1111	      - 3.3
1112	      - logit-space, principled minimal
1113	    - - MMD-PCA50
1114	      - 50
1115	      - 4.2
1116	      - activation PCA, captures covariance
1117	    - - MMD-PCA100
1118	      - 100
1119	      - 3.8
1120	      - slight curse of dimensionality
1121	    - - CORAL-1D
1122	      - 1
1123	      - 2.8
1124	      - second-order, less info in 1D
1125	    - - CORAL-PCA50
1126	      - 50
1127	      - 3.6
1128	      - CORAL approaches MMD at d=50
1129	  - name: 'Table 13: CaCLR Depth Profile (Qwen3, mean across 20 langs)'
1130	    columns:
1131	    - depth_pct
1132	    - zs_auroc
1133	    - caclr_auroc
1134	    - delta_pp
1135	    rows:
1136	    - - 30
1137	      - 0.74
1138	      - 0.752
1139	      - 1.2
1140	    - - 43
1141	      - 0.779
1142	      - 0.798
1143	      - 1.9
1144	    - - 51
1145	      - 0.775
1146	      - 0.805
1147	      - 3.0
1148	    - - 60
1149	      - 0.757
1150	      - 0.798
1151	      - 4.1
1152	    - - 72
1153	      - 0.737
1154	      - 0.785
1155	      - 4.8
1156	    - - 85
1157	      - 0.695
1158	      - 0.74
1159	      - 4.5
1160	  figures_description:
1161	  - 'Figure 5: β sweep curve — delta AUROC (y) vs log10(β) (x). Clear inverted-U,
1162	    peak at β=0.05. Shaded band shows ±1 std across 5 seeds (narrow, ~0.35pp). Inset:
1163	    corresponding ECE improvement mirrors the AUROC curve.
1164	
1165	    '
1166	  - 'Figure 6: CaCLR depth profile (Qwen3). ZS (blue dashed) vs CaCLR (red solid)
1167	    across normalized depth. Gap widens monotonically from shallow (+1.2pp) to deep
1168	    (+4.8pp). Demonstrates CaCLR specifically addresses deep-layer degradation.
1169	
1170	    '
1171	  - 'Figure 7: CaCLR improvement by resource tier (grouped bar chart). LOW tier benefits
1172	    most (+6.5pp), HIGH tier least (+1.2pp). Inverse resource-level scaling of CaCLR
1173	    benefit.
1174	
1175	    '
1176	  analysis: 'CaCLR 作为正面方法贡献：β>0 一致地 shifts Pareto frontier，mean +3.3pp AUROC 和 -38%
1177	    ECE vs temperature scaling。Component ablation 证实 L_consistency (MMD) 是主要 contributor
1178	    (+2.5pp)，L_SB-ECE 提供 complementary calibration (+0.7pp)。 High-dim MMD (PCA-50)
1179	    进一步提升至 +4.2pp，但即使 1-D logit MMD 已经 significant。 CORAL 的可比结果确认 distributional matching
1180	    一般性地 work。Multi-seed std 仅 ±0.35pp，confirming robustness。Deep-layer improvement
1181	    模式与 decomposition (Claim 2) 形成因果闭环。Headline 可用："CaCLR-trained probes reduce non-English
1182	    ECE by 38% requiring zero target-language labels."
1183	
1184	    '
1185	- name: Difficulty-Controlled Ablation (Decomposition)
1186	  plan_id: plan_004
1187	  description: 'IRT difficulty probes (Ridge regression on human difficulty scores
1188	    per Civelli et al.), project out difficulty direction, retrain correctness probes
1189	    on residuals, evaluate transfer。10 languages (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr,
1190	    LOW: sw/bn) × 8 layers (20-90% depth) per model。Random-direction control included。
1191	
1192	    '
1193	  expected_results:
1194	    difficulty_probe_r2_mean: 0.67
1195	    difficulty_probe_r2_range:
1196	    - 0.54
1197	    - 0.76
1198	    difficulty_var_explained_of_correctness_pct: 62
1199	    capability_var_explained_pct: 38
1200	    difficulty_transfer_degradation_share_pct: 14
1201	    capability_transfer_degradation_share_pct: 86
1202	    residual_en_auroc_drop_after_projection_pp: 4.2
1203	    residual_zs_transfer_improvement_pp: 4.5
1204	    capability_transfer_drop_by_depth:
1205	      20pct: 0.5
1206	      40pct: 2.2
1207	      60pct: 5.0
1208	      80pct: 8.8
1209	    random_direction_control_delta_pp: -1.5
1210	    langs_showing_clean_separation_of_10: 8
1211	    prescriptive_accuracy_pct: 76
1212	  result_rationale: 'IRT difficulty 是 language-agnostic property：hard questions are
1213	    hard everywhere (Civelli et al. 已验证跨语言 difficulty 相关性 r>0.85)。Ridge regression
1214	    captures this linearly (R²=0.67)。Difficulty 占 correctness variance 的 62% 但仅贡献
1215	    14% 的 transfer degradation，因为 difficulty signal 本质是 universal 的——无论用 哪种语言的 representation，difficult
1216	    items 的 activation patterns 都类似。
1217	
1218	    Capability-specific residual 仅占 38% variance 但驱动 86% 的 transfer degradation， 且
1219	    degradation 随 depth 指数增长（20%→80% depth: 0.5→8.8pp）。这解释了 Pareto frontier 的 mechanistic
1220	    origin：deep layers 的 EN probe improvement 主要来自 capability-specific component（language-dependent
1221	    competence patterns），而这个 component 恰好最难 transfer。
1222	
1223	    Projecting out difficulty 后 EN AUROC 下降 4.2pp（移除了 easy-hard distinction 信号），但
1224	    ZS transfer 改善 4.5pp（关键发现：removing difficulty noise exposes the capability signal
1225	    that''s harder to transfer but also more language-specific; the residual probe
1226	    that''s trained purely on capability actually transfers BETTER on average because
1227	    it''s forced to find the language-agnostic component of capability）。 Within [3,
1228	    6]pp key metric range。
1229	
1230	    8/10 languages 显示 clean separation（difficulty component clearly universal, capability
1231	    component clearly language-specific）。2 个 exceptions (sw, bn) 因 LOW-resource translation
1232	    quality 使 difficulty labels 本身有 noise。
1233	
1234	    Random-direction control (-1.5pp) 确认 difficulty projection 是 genuine 的， 不是 dimensionality
1235	    reduction artifact。
1236	
1237	    Prescriptive accuracy 76%：给定 difficulty/capability ratio at each language-layer,
1238	    预测最优策略 (zero-shot for difficulty-dominant vs CaCLR for capability-dominant) 在
1239	    76% 的 cases 中正确。
1240	
1241	    '
1242	  tables:
1243	  - name: 'Table 14: Decomposition Results (3-arch pooled)'
1244	    columns:
1245	    - component
1246	    - var_pct
1247	    - transfer_auroc_mean
1248	    - transfer_drop_pp
1249	    - degradation_share_pct
1250	    rows:
1251	    - - full_correctness
1252	      - 100
1253	      - 0.767
1254	      - 5.2
1255	      - 100
1256	    - - difficulty_shared
1257	      - 62
1258	      - 0.755
1259	      - 0.7
1260	      - 14
1261	    - - capability_specific
1262	      - 38
1263	      - 0.672
1264	      - 7.8
1265	      - 86
1266	    - - random_direction_control
1267	      - —
1268	      - 0.752
1269	      - —
1270	      - —
1271	  - name: 'Table 15: Capability Transfer Drop by Depth Band'
1272	    columns:
1273	    - depth_band
1274	    - difficulty_drop_pp
1275	    - capability_drop_pp
1276	    - ratio
1277	    rows:
1278	    - - 20-30%
1279	      - 0.2
1280	      - 0.5
1281	      - 2.5×
1282	    - - 35-50%
1283	      - 0.5
1284	      - 2.2
1285	      - 4.4×
1286	    - - 55-70%
1287	      - 0.8
1288	      - 5.0
1289	      - 6.3×
1290	    - - 75-90%
1291	      - 1.2
1292	      - 8.8
1293	      - 7.3×
1294	  figures_description:
1295	  - 'Figure 8: Stacked area chart — difficulty (blue, near-flat) vs capability (red,
1296	    exponentially rising) transfer degradation across normalized depth. Clear separation:
1297	    difficulty barely degrades; capability drives almost all degradation, accelerating
1298	    with depth.
1299	
1300	    '
1301	  analysis: 'Decomposition 清晰分离 transferable vs non-transferable components。4.5pp
1302	    transfer improvement after difficulty projection（in [3,6] range）直接 actionable：practitioners
1303	    可以 train probes on difficulty-controlled representations。8/10 languages clean
1304	    separation 在 [7,10] range。CaCLR 的 deep-layer improvement 与 capability degradation
1305	    profile 完美对应——CaCLR 的 consistency loss targets exactly the capability-specific
1306	    component that decomposition identifies。
1307	
1308	    '
1309	- name: Linear Projection Sensitivity & Procrustes Reversal
1310	  plan_id: plan_012
1311	  description: 'Vary parallel pairs (10, 20, 30, 50, 100, 200) for Procrustes alignment。
1312	    3 models × 5 representative layers × 20 languages。确定 saturation point 和 resource-tier
1313	    stratification。识别 Procrustes effect reversal threshold。
1314	
1315	    '
1316	  expected_results:
1317	    pairs_to_95pct_overall: 40
1318	    pairs_to_95pct_HIGH: 22
1319	    pairs_to_95pct_MID: 36
1320	    pairs_to_95pct_LOW: 48
1321	    saturation_curve:
1322	      pairs_10_pct_of_200: 0.7
1323	      pairs_20_pct_of_200: 0.84
1324	      pairs_30_pct_of_200: 0.92
1325	      pairs_50_pct_of_200: 0.97
1326	      pairs_100_pct_of_200: 0.99
1327	    pairs_200_baseline_auroc_mean: 0.783
1328	    procrustes_reversal_threshold_zs_auroc: 0.52
1329	    procrustes_helps_below_threshold_delta_pp: 4.2
1330	    procrustes_hurts_above_threshold_delta_pp: -1.0
1331	    low_resource_delta_over_zs_pp: 8.2
1332	    multi_seed_std_pp: 0.28
1333	  result_rationale: 'Procrustes alignment 学习 EN→target rotation matrix。20 pairs 即可估计
1334	    dominant rotational components：correctness subspace 是 low-dimensional 的（subspace
1335	    angle 分析显示前 30-50 principal angles 解释 95%+ 的 alignment structure）。40 pairs 达到
1336	    95% 因为边际 minor components 需要更多 data 来稳定。Within [30, 50] range。
1337	
1338	    Resource-tier stratification：HIGH languages 与 EN 的 activation distributions 更相似（CKA
1339	    > 0.70 at probing layers），rotation matrix 的 effective rank 更低 → 22 pairs 即可。LOW
1340	    languages 需要估计更 complex rotation → 48 pairs。
1341	
1342	    LOW-resource delta +8.2pp (within [5, 12] range)：LOW languages 的 ZS baseline 最差（0.57-0.67），有最大改善空间。Procrustes
1343	    对 misaligned correctness directions 的纠正效果与 misalignment degree 成正比。
1344	
1345	    Procrustes reversal at threshold ZS=0.52：当 ZS AUROC < 0.52，correctness directions
1346	    严重 misaligned，Procrustes 提供 +4.2pp。当 ZS > 0.60，directions 已 well-aligned，Procrustes
1347	    引入 estimation noise → -1.0pp。Threshold 0.52 对应 CKA ~0.35（plan_011 cliff threshold）——geometric
1348	    consistency。
1349	
1350	    '
1351	  tables:
1352	  - name: 'Table 16: Projection Sample Efficiency (3-arch pooled)'
1353	    columns:
1354	    - n_pairs
1355	    - pct_of_200
1356	    - mean_auroc
1357	    - std_across_seeds
1358	    rows:
1359	    - - 10
1360	      - 70
1361	      - 0.776
1362	      - 0.012
1363	    - - 20
1364	      - 84
1365	      - 0.781
1366	      - 0.007
1367	    - - 30
1368	      - 92
1369	      - 0.785
1370	      - 0.004
1371	    - - 50
1372	      - 97
1373	      - 0.789
1374	      - 0.003
1375	    - - 100
1376	      - 99
1377	      - 0.79
1378	      - 0.002
1379	    - - 200
1380	      - 100
1381	      - 0.783
1382	      - 0.001
1383	  - name: 'Table 17: Saturation by Resource Tier'
1384	    columns:
1385	    - tier
1386	    - pairs_to_90pct
1387	    - pairs_to_95pct
1388	    - interpretation
1389	    rows:
1390	    - - HIGH
1391	      - 14
1392	      - 22
1393	      - simple rotation, low effective rank
1394	    - - MID
1395	      - 22
1396	      - 36
1397	      - moderate complexity
1398	    - - LOW
1399	      - 32
1400	      - 48
1401	      - complex rotation, more data needed
1402	  - name: 'Table 18: Procrustes Effect Reversal'
1403	    columns:
1404	    - zs_auroc_range
1405	    - n_pairs_in_range
1406	    - mean_delta_pp
1407	    - direction
1408	    rows:
1409	    - - <0.50
1410	      - 38
1411	      - 5.8
1412	      - strong positive
1413	    - - 0.50-0.52
1414	      - 22
1415	      - 2.6
1416	      - moderate positive
1417	    - - 0.52-0.58
1418	      - 45
1419	      - 0.4
1420	      - near-zero (transition)
1421	    - - 0.58-0.68
1422	      - 95
1423	      - -0.6
1424	      - slight negative
1425	    - - '>0.68'
1426	      - 100
1427	      - -1.0
1428	      - negative — hurts
1429	  figures_description:
1430	  - 'Figure 10a: Sample efficiency curves — normalized performance (y) vs n_pairs
1431	    (x). Three curves for HIGH/MID/LOW, showing staggered saturation. All converge
1432	    by 100.
1433	
1434	    '
1435	  - 'Figure 10b: Procrustes reversal — delta AUROC (y) vs ZS baseline (x). Clear sign
1436	    change at ~0.52. Points colored by resource tier. Vertical dashed line at threshold.
1437	
1438	    '
1439	  analysis: '~40 pairs to 95% 是 directly actionable：<50 parallel sentences per language
1440	    即可 达到接近 full-scale alignment。Resource-tier stratification 提供 per-language guidance。LOW-resource
1441	    delta +8.2pp（in [5, 12] range）。Procrustes reversal at 0.52 与 CKA threshold 0.35
1442	    形成对应——geometric consistency across analyses。
1443	
1444	    '
1445	- name: Probing Control Tasks — Full-Scale Cross-Lingual
1446	  plan_id: plan_013
1447	  description: '扩展 MVP English-only control task analysis（已完成, selectivity L20-L27:
1448	    0.244-0.262） 到 20 languages × 3 architectures。Train probes on randomly permuted
1449	    labels, compute selectivity = real_AUROC - control_AUROC。定量 cross-lingual artifact
1450	    rate。 Selectivity threshold sensitivity at 0.03/0.05/0.10。
1451	
1452	    '
1453	  expected_results:
1454	    en_selectivity_deep_layers_range:
1455	    - 0.24
1456	    - 0.32
1457	    cross_lingual_selectivity_by_tier:
1458	      HIGH_mean: 0.24
1459	      MID_mean: 0.19
1460	      LOW_mean: 0.1
1461	    artifact_rate_overall_pct: 10
1462	    artifact_rate_by_tier:
1463	      HIGH_pct: 3
1464	      MID_pct: 6
1465	      LOW_pct: 28
1466	    artifact_concentration: LOW-resource × >60% depth
1467	    control_auroc_mean_all: 0.494
1468	    control_auroc_std: 0.009
1469	    selectivity_threshold_sensitivity:
1470	      threshold_003:
1471	        artifact_rate_pct: 15
1472	      threshold_005:
1473	        artifact_rate_pct: 10
1474	      threshold_010:
1475	        artifact_rate_pct: 6
1476	    langs_with_any_meaningful_selectivity_gt005: 17
1477	  result_rationale: 'MVP English data（selectivity L27=0.262, within [0.2, 0.35] range）确立了
1478	    baseline。 Full-scale scaling：更大模型（235B/17B×16E/31B）有更强 correctness signal → EN
1479	    selectivity 提升至 0.24-0.32 range。
1480	
1481	    Cross-lingual artifact rate 10% (within [5, 15] range)。Resource-tier 分层明显： LOW
1482	    languages 28% artifact rate 源于：(1) pretraining 中占比极低 → activation distributions
1483	    缺乏 structured correctness signal → linear probes 通过 capacity 拟合 noise；(2) GlobalMMLU
1484	    的 LOW-resource translations 质量较低 → correctness labels 本身有 noise。HIGH/MID 的 3-6%
1485	    artifact rate 表明核心 Pareto/CKA 分析 （主要基于 HIGH/MID patterns）不受 artifact concerns
1486	    影响。
1487	
1488	    Artifacts 集中在 LOW-resource × deep layers (>60% depth)，与 CKA cliff 一致： deep layers
1489	    的 low-resource CKA <0.20，cross-lingual activation structure 不足 以支撑 genuine correctness
1490	    probing。
1491	
1492	    这是 field-level contribution：cross-lingual probing studies（包括 Xiao et al.） 如果不做
1493	    selectivity checks 会高估 LOW-resource transfer quality。
1494	
1495	    '
1496	  tables:
1497	  - name: 'Table 19: Cross-Lingual Selectivity by Tier and Depth'
1498	    columns:
1499	    - depth_band
1500	    - HIGH_selectivity
1501	    - MID_selectivity
1502	    - LOW_selectivity
1503	    rows:
1504	    - - 0-30%
1505	      - 0.04
1506	      - 0.03
1507	      - 0.01
1508	    - - 30-60%
1509	      - 0.2
1510	      - 0.16
1511	      - 0.07
1512	    - - 60-80%
1513	      - 0.3
1514	      - 0.24
1515	      - 0.11
1516	    - - 80-100%
1517	      - 0.28
1518	      - 0.21
1519	      - 0.08
1520	  - name: 'Table 20: Artifact Rates by Tier (selectivity threshold = 0.05)'
1521	    columns:
1522	    - tier
1523	    - n_lang_layer_arch_combinations
1524	    - artifact_count
1525	    - artifact_rate_pct
1526	    rows:
1527	    - - HIGH
1528	      - 1008
1529	      - 30
1530	      - 3
1531	    - - MID
1532	      - 1152
1533	      - 69
1534	      - 6
1535	    - - LOW
1536	      - 576
1537	      - 161
1538	      - 28
1539	    - - total
1540	      - 2736
1541	      - 260
1542	      - 10
1543	  figures_description:
1544	  - 'Figure S1: Selectivity heatmap (3 panels, one per architecture). Language (y,
1545	    ordered by tier) × normalized depth (x). Color = selectivity. LOW-resource rows
1546	    at deep layers show gray (near-zero selectivity).
1547	
1548	    '
1549	  analysis: '10% overall artifact rate (in [5, 15] range)。28% LOW-resource rate 是
1550	    methodological warning for the field。关键：artifacts 不影响核心分析（Pareto/CKA 主要基于 HIGH/MID），
1551	    但 LOW-resource transfer claims 需要 selectivity-qualified caveats。
1552	
1553	    '
1554	- name: Cross-Lingual Correctness-Confidence Orthogonality
1555	  plan_id: plan_005
1556	  description: 'Verbalized confidence direction + cosine similarity with correctness
1557	    direction, 20 languages × 3 architectures。Supporting evidence for Claim 4 (subsection)。
1558	
1559	    '
1560	  expected_results:
1561	    cosine_mean_overall: 0.048
1562	    cosine_range:
1563	    - 0.02
1564	    - 0.088
1565	    cosine_en: 0.032
1566	    all_below_0p10: true
1567	    by_tier:
1568	      HIGH_mean: 0.036
1569	      MID_mean: 0.05
1570	      LOW_mean: 0.07
1571	    by_arch:
1572	      qwen3_mean: 0.044
1573	      llama4_mean: 0.052
1574	      gemma4_mean: 0.048
1575	    resource_tier_spearman: -0.62
1576	  result_rationale: 'Miao & Ungar (2026) EN 7-8B: cosine < 0.04。Extension to 20 langs
1577	    × 大模型 保持 near-orthogonality（all < 0.10）因为 correctness 和 verbalized confidence
1578	    是 architecturally decoupled：confidence 由 language modeling head 从 surface-level
1579	    token probabilities 生成，correctness 由 intermediate representations geometry 编码。
1580	    Low-resource 略高（0.070）因为 confidence elicitation 更 noisy + 更弱的 representation quality
1581	    使两个 directions 的 estimation 更不稳定。
1582	
1583	    '
1584	  tables:
1585	  - name: 'Table 21: Orthogonality by Tier and Architecture'
1586	    columns:
1587	    - tier
1588	    - qwen3
1589	    - llama4
1590	    - gemma4
1591	    - combined
1592	    rows:
1593	    - - HIGH
1594	      - 0.033
1595	      - 0.039
1596	      - 0.036
1597	      - 0.036
1598	    - - MID
1599	      - 0.047
1600	      - 0.054
1601	      - 0.049
1602	      - 0.05
1603	    - - LOW
1604	      - 0.064
1605	      - 0.078
1606	      - 0.068
1607	      - 0.07
1608	  figures_description:
1609	  - 'Figure S2: Cosine similarity violin plots by resource tier (3 columns for 3 archs).
1610	    All distributions well below 0.10 threshold line. Slight upward shift for LOW
1611	    tier.
1612	
1613	    '
1614	  analysis: 'Near-orthogonality universally holds (59/60 model-lang pairs < 0.10)。Confirms
1615	    output-based calibration structurally limited across languages — motivates probe-based
1616	    approach。Resource-tier gradient is novel but small effect (range only 0.034)。
1617	
1618	    '
1619	- name: Probe Complexity Comparison
1620	  plan_id: plan_006
1621	  description: 'Logistic regression vs 2-layer MLP (hidden=128) at each probed layer,
1622	    3 models。 Validates linear probe choice for cross-lingual transfer。
1623	
1624	    '
1625	  expected_results:
1626	    logreg_en_auroc_best: 0.835
1627	    mlp_en_auroc_best: 0.855
1628	    mlp_en_gain_pp: 2.0
1629	    logreg_zs_drop_mean_pp: 5.2
1630	    mlp_zs_drop_mean_pp: 10.8
1631	    logreg_transfer_advantage_pp: 5.6
1632	    logreg_advantage_at_deep_layers_pp: 8.5
1633	    logreg_advantage_at_shallow_layers_pp: 1.8
1634	  result_rationale: 'Linear probes learn 单个 hyperplane，跨语言泛化因为 correctness subspace
1635	    是 near-universal linear structure（subspace angle ~13°）。MLPs fit nonlinear decision
1636	    boundaries that overfit EN-specific feature interactions：+2pp EN AUROC 但 -5.6pp
1637	    transfer（net worse）。Gap 在 deep layers 放大（+8.5pp logreg advantage at >70% depth）因为
1638	    deep layers 有更多 language-specific nonlinear structure for MLP to exploit。
1639	
1640	    '
1641	  tables:
1642	  - name: 'Table S2: Probe Complexity (Qwen3, EN-optimal layer, mean across 20 langs)'
1643	    columns:
1644	    - probe_type
1645	    - en_auroc
1646	    - zs_mean_20
1647	    - zs_drop_pp
1648	    rows:
1649	    - - logistic_regression
1650	      - 0.835
1651	      - 0.775
1652	      - 6.0
1653	    - - mlp_2layer_h128
1654	      - 0.855
1655	      - 0.747
1656	      - 10.8
1657	  figures_description:
1658	  - 'Figure S3: Transfer drop (pp, y-axis) vs depth (x-axis), logreg (blue, moderate
1659	    slope) vs MLP (red, steep slope diverging past 60% depth).
1660	
1661	    '
1662	  analysis: 'Linear probes 为 cross-lingual transfer 的 optimal choice。MLP 的 nonlinear
1663	    capacity captures EN-specific patterns → worse transfer。Justifies logreg as primary
1664	    probe and supports geometric interpretation。
1665	
1666	    '
1667	- name: Cross-Benchmark Generalization (Belebele + MMLU-ProX)
1668	  plan_id: plan_007
1669	  description: 'Evaluate best probes + CaCLR on Belebele (reading comprehension) and
1670	    MMLU-ProX (harder factual), 20 languages each × 3 models。
1671	
1672	    '
1673	  expected_results:
1674	    belebele_zs_mean_20: 0.748
1675	    belebele_caclr_mean_20: 0.78
1676	    belebele_caclr_delta_pp: 3.2
1677	    mmlupx_zs_mean_20: 0.735
1678	    mmlupx_caclr_mean_20: 0.77
1679	    mmlupx_caclr_delta_pp: 3.5
1680	    cross_benchmark_caclr_cv: 0.04
1681	    pareto_frontier_replicates_both_benchmarks: true
1682	  result_rationale: 'Belebele (reading comprehension) 和 MMLU-ProX (harder factual)
1683	    的 baselines 不同于 GlobalMMLU 因为 domain shift 和 task format differences。但 CaCLR 的
1684	    improvement 幅度 consistent（3.2-3.5pp vs GlobalMMLU 的 3.3pp）。Low CV (0.04) 证实 CaCLR
1685	    addresses fundamental representation alignment issue 而非 overfitting to specific
1686	    benchmark。Pareto frontier structure (positive depth trend + local deep tradeoff)
1687	    replicates on both benchmarks — phenomenon is not benchmark-specific。
1688	
1689	    '
1690	  tables:
1691	  - name: 'Table 22: Cross-Benchmark CaCLR Generalization'
1692	    columns:
1693	    - benchmark
1694	    - zs_mean_20
1695	    - caclr_mean_20
1696	    - delta_pp
1697	    rows:
1698	    - - GlobalMMLU
1699	      - 0.767
1700	      - 0.8
1701	      - 3.3
1702	    - - Belebele
1703	      - 0.748
1704	      - 0.78
1705	      - 3.2
1706	    - - MMLU-ProX
1707	      - 0.735
1708	      - 0.77
1709	      - 3.5
1710	  figures_description:
1711	  - 'Figure S4: CaCLR delta (y) vs ZS baseline (x) across 3 benchmarks × 20 languages.
1712	    Points from different benchmarks intermixed — same linear relationship, confirming
1713	    benchmark-agnostic mechanism.
1714	
1715	    '
1716	  analysis: 'Cross-benchmark consistency 是最强 defense against overfitting。CaCLR improvement
1717	    cv=0.04 across benchmarks 证实方法的 generality。
1718	
1719	    '
1720	- name: Quantization Validation Ablation
1721	  plan_id: plan_010
1722	  description: '(a) W4A16 vs FP16 for Llama 4 Scout at 5 layers, 5% subset; (b) GPTQ-Int4
1723	    vs FP16 for Qwen3-235B at 5 layers, 5% subset; (c) BF16 Gemma4 serves as unquantized
1724	    reference (no ablation needed)。
1725	
1726	    '
1727	  expected_results:
1728	    llama4_w4a16_fp16_auroc_diff_mean_pp: 0.3
1729	    llama4_w4a16_fp16_auroc_diff_max_pp: 0.7
1730	    llama4_rank_correlation: 0.997
1731	    qwen3_int4_fp16_auroc_diff_mean_pp: 0.5
1732	    qwen3_int4_fp16_auroc_diff_max_pp: 1.2
1733	    qwen3_rank_correlation: 0.995
1734	    cka_distortion_max: 0.02
1735	  result_rationale: 'W4A16 (Llama4) 保留 16-bit activations，仅 weight 量化，对 activation
1736	    geometry 影响极小（0.3pp mean diff）。GPTQ-Int4 (Qwen3) 更 aggressive 但 correctness direction
1737	    的 angular structure robust（0.5pp mean diff）——quantization noise 近似 isotropic，不
1738	    preferentially distort correctness-relevant directions。 Rank correlation > 0.995
1739	    确认 Pareto frontier ordering 完全保留。 CKA distortion < 0.02 证实 CKA analysis 不被量化 artifacts
1740	    污染。 Gemma4 的 BF16 提供 ground-truth 无量化 reference。
1741	
1742	    '
1743	  tables:
1744	  - name: 'Table S3: Quantization Comparison (representative layers)'
1745	    columns:
1746	    - model
1747	    - layer
1748	    - fp16_auroc
1749	    - quant_auroc
1750	    - diff_pp
1751	    rows:
1752	    - - Llama4
1753	      - 8
1754	      - 0.642
1755	      - 0.639
1756	      - 0.3
1757	    - - Llama4
1758	      - 20
1759	      - 0.77
1760	      - 0.768
1761	      - 0.2
1762	    - - Llama4
1763	      - 32
1764	      - 0.81
1765	      - 0.807
1766	      - 0.3
1767	    - - Llama4
1768	      - 40
1769	      - 0.812
1770	      - 0.808
1771	      - 0.4
1772	    - - Llama4
1773	      - 47
1774	      - 0.78
1775	      - 0.776
1776	      - 0.4
1777	    - - Qwen3
1778	      - 20
1779	      - 0.712
1780	      - 0.708
1781	      - 0.4
1782	    - - Qwen3
1783	      - 36
1784	      - 0.787
1785	      - 0.782
1786	      - 0.5
1787	    - - Qwen3
1788	      - 52
1789	      - 0.824
1790	      - 0.818
1791	      - 0.6
1792	    - - Qwen3
1793	      - 68
1794	      - 0.837
1795	      - 0.835
1796	      - 0.2
1797	    - - Qwen3
1798	      - 84
1799	      - 0.817
1800	      - 0.81
1801	      - 0.7
1802	  figures_description:
1803	  - 'Figure S5: Quantized vs FP16 AUROC scatter. Both models tight along y=x diagonal.
1804	
1805	    '
1806	  analysis: 'Quantization safe for both models。Preempts reviewer concern #5。Gemma4
1807	    BF16 provides unquantized cross-validation anchor。
1808	
1809	    '
1810	- name: Extended Language Coverage (Camera-Ready)
1811	  plan_id: plan_009
1812	  description: 'Expand from 20 to 50+ languages for camera-ready using GlobalMMLU/Belebele
1813	    full language sets。3 models × all probed layers。
1814	
1815	    '
1816	  expected_results:
1817	    total_languages: 52
1818	    zs_pass_rate_52lang: 0.83
1819	    zs_auroc_above_060_count: 43
1820	    caclr_improvement_positive_count: 48
1821	    mean_zs_auroc_52lang: 0.735
1822	    mean_caclr_auroc_52lang: 0.768
1823	    new_families_covered:
1824	    - Austronesian
1825	    - Dravidian
1826	    - Uralic
1827	    - Kartvelian
1828	    - Niger-Congo_B
1829	    pareto_frontier_holds_all_52: true
1830	    simpson_paradox_holds_all_52: true
1831	    tier_summary:
1832	      HIGH_10_langs:
1833	        zs_mean: 0.8
1834	        caclr_mean: 0.82
1835	        delta_pp: 2.5
1836	      MID_24_langs:
1837	        zs_mean: 0.76
1838	        caclr_mean: 0.79
1839	        delta_pp: 3.2
1840	      LOW_14_langs:
1841	        zs_mean: 0.67
1842	        caclr_mean: 0.72
1843	        delta_pp: 4.8
1844	      VERY_LOW_4_langs:
1845	        zs_mean: 0.56
1846	        caclr_mean: 0.62
1847	        delta_pp: 5.8
1848	  result_rationale: 'Expansion 主要增加 MID-resource 语言（Indonesian, Finnish, Georgian,
1849	    Tamil, etc.）， 大多 fall in 0.65-0.78 AUROC range。Extremely low-resource（Amharic,
1850	    Khmer, Lao, Hausa）的 AUROC < 0.58 但代表 edge cases。CaCLR 在 92% (48/52) 的语言上 positive
1851	    因为 consistency loss mechanism 是 language-agnostic。Pareto frontier 和 Simpson''s
1852	    Paradox structure 在 52 languages 上完全保持——增强 universality claim 从 n=20 到 n=52。 VERY_LOW
1853	    tier (4 langs) 展示 ceiling：pretraining 不足的语言即使有 CaCLR 也 limited by representation
1854	    quality 本身。CaCLR benefit 与 resource level 反相关 (r=-0.65, HIGH +2.5pp vs VERY_LOW
1855	    +5.8pp)。
1856	
1857	    '
1858	  tables:
1859	  - name: 'Table 23: Extended Coverage Summary by Tier'
1860	    columns:
1861	    - tier
1862	    - n_langs
1863	    - zs_mean
1864	    - caclr_mean
1865	    - caclr_delta_pp
1866	    rows:
1867	    - - HIGH
1868	      - 10
1869	      - 0.8
1870	      - 0.82
1871	      - 2.5
1872	    - - MID
1873	      - 24
1874	      - 0.76
1875	      - 0.79
1876	      - 3.2
1877	    - - LOW
1878	      - 14
1879	      - 0.67
1880	      - 0.72
1881	      - 4.8
1882	    - - VERY_LOW
1883	      - 4
1884	      - 0.56
1885	      - 0.62
1886	      - 5.8
1887	  figures_description:
1888	  - 'Figure 10: World map with per-language CaCLR AUROC as color fill. Broad geographic
1889	    and typological coverage. European/East Asian warm, Sub-Saharan/South Asian cool
1890	    but still above chance.
1891	
1892	    '
1893	  analysis: 52-language extension 确认 all findings at scale。Resource-tier gradient
1894	    smooth, CaCLR benefit inversely correlated with resource level。No language family
1895	    shows anomalous behavior — phenomenon is truly universal across typological diversity。
1896	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da1ffee7-7fed-4281-9ae5-4ca621b5452e",
  "isSidechain": true,
  "promptId": "daded219-2295-49e3-ac22-87f6bbbc54c9",
  "agentId": "a95da934c42f8700a",
  "type": "user",
  "uuid": "58e8ab7e-35af-44fe-9e33-7526568d289d",
  "sourceToolAssistantUUID": "da1ffee7-7fed-4281-9ae5-4ca621b5452e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T13:52:25.080Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EU526KyLjQd9Z2ac5B1RFr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/experiment_data.json",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58e8ab7e-35af-44fe-9e33-7526568d289d",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpmZHT5gjzS8rAqmGGi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04766aa7-61c0-48fe-bcf7-3fb5c1dcfef8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLanRC7XnUuxEVXZUg616X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4336,
      "cache_read_input_tokens": 37466,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4336,
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

_source line 36 · 2026-05-21T13:52:25.086Z_

<details><summary>↩ Tool result · `toolu_01EU526KyLjQd9Z2ac5B1RFr`</summary>

```text
1	[
2	  {
3	    "name": "Full Pareto Frontier — Qwen3-235B-A22B (MoE)",
4	    "description": "94-layer MoE (INT4, ~22B active), 24 probed layers (every 4th: L0,L4,...,L92), 20 typologically diverse languages, English logistic regression probes, 5 transfer conditions: zero-shot, mean-shift, linear projection (200 pairs), few-shot 25/100, CaCLR (optimal α=0.1, β=0.05 from plan_003)。验证 MVP 发现的 positive depth-transfer trend 和 local deep-layer Pareto tradeoff 在大 MoE 模型上放大。\n",
5	    "results": {
6	      "en_best_auroc": 0.835,
7	      "en_best_layer_idx": 68,
8	      "en_best_depth_pct": 72,
9	      "en_auroc_range": [
10	        0.59,
11	        0.835
12	      ],
13	      "en_ece_raw_best": 0.172,
14	      "zs_mean_auroc_20lang_at_zs_optimal": 0.775,
15	      "zs_best_transfer_layer_idx": 48,
16	      "zs_best_transfer_depth_pct": 51,
17	      "zs_pass_rate_auroc_gt_058": 19,
18	      "zs_fail_langs": [
19	        "yo"
20	      ],
21	      "zs_auroc_by_tier": {
22	        "HIGH_mean": 0.817,
23	        "MID_mean": 0.788,
24	        "LOW_mean": 0.693
25	      },
26	      "zs_auroc_selected": {
27	        "zh": 0.83,
28	        "es": 0.82,
29	        "fr": 0.82,
30	        "de": 0.82,
31	        "ja": 0.81,
32	        "nl": 0.81,
33	        "pt": 0.81,
34	        "ar": 0.8,
35	        "hi": 0.79,
36	        "ko": 0.79,
37	        "ru": 0.8,
38	        "tr": 0.78,
39	        "vi": 0.77,
40	        "id": 0.79,
41	        "pl": 0.79,
42	        "uk": 0.78,
43	        "sw": 0.72,
44	        "bn": 0.73,
45	        "te": 0.67,
46	        "yo": 0.575
47	      },
48	      "overall_spearman_depth_vs_zs": {
49	        "global_rho": 0.68,
50	        "global_p": 0.0003
51	      },
52	      "per_lang_spearman_rho_median": 0.62,
53	      "per_lang_positive_rho_count": 17,
54	      "per_lang_significant_positive_count": 14,
55	      "per_lang_negative_rho_langs": [
56	        "yo",
57	        "te",
58	        "sw"
59	      ],
60	      "pareto_tradeoff_langs_count": 15,
61	      "pareto_en_optimal_layer": 68,
62	      "pareto_zs_optimal_layer": 48,
63	      "pareto_depth_gap_layers": 20,
64	      "pareto_zs_drop_at_en_optimal_pp": 3.8,
65	      "mean_shift_delta_auroc": 0.0,
66	      "linproj_200pairs_mean_auroc": 0.793,
67	      "linproj_200pairs_delta_pp": 1.8,
68	      "fewshot_25_mean_auroc": 0.762,
69	      "fewshot_100_mean_auroc": 0.788,
70	      "caclr_mean_auroc": 0.812,
71	      "caclr_delta_vs_zs_pp": 3.7
72	    },
73	    "tables": [
74	      {
75	        "name": "Table 1: Qwen3-235B Pareto Frontier (selected layers)",
76	        "columns": [
77	          "layer_idx",
78	          "depth_pct",
79	          "en_auroc",
80	          "zs_mean_20",
81	          "zs_drop_vs_en_pp",
82	          "on_pareto"
83	        ],
84	        "rows": [
85	          [
86	            4,
87	            4,
88	            0.59,
89	            0.582,
90	            0.8,
91	            false
92	          ],
93	          [
94	            12,
95	            13,
96	            0.645,
97	            0.636,
98	            0.9,
99	            false
100	          ],
101	          [
102	            20,
103	            21,
104	            0.71,
105	            0.7,
106	            1.0,
107	            false
108	          ],
109	          [
110	            28,
111	            30,
112	            0.752,
113	            0.74,
114	            1.2,
115	            false
116	          ],
117	          [
118	            36,
119	            38,
120	            0.785,
121	            0.77,
122	            1.5,
123	            false
124	          ],
125	          [
126	            40,
127	            43,
128	            0.798,
129	            0.779,
130	            1.9,
131	            false
132	          ],
133	          [
134	            44,
135	            47,
136	            0.808,
137	            0.782,
138	            2.6,
139	            false
140	          ],
141	          [
142	            48,
143	            51,
144	            0.815,
145	            0.775,
146	            4.0,
147	            true
148	          ],
149	          [
150	            52,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04766aa7-61c0-48fe-bcf7-3fb5c1dcfef8",
  "isSidechain": true,
  "promptId": "daded219-2295-49e3-ac22-87f6bbbc54c9",
  "agentId": "a95da934c42f8700a",
  "type": "user",
  "uuid": "775b3651-7611-40af-b8ac-593ee126e6a4",
  "sourceToolAssistantUUID": "04766aa7-61c0-48fe-bcf7-3fb5c1dcfef8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-21T13:52:29.379Z_

Now let me check the review context and previous review to understand what has already been flagged, and also examine the paper framing for the critical issue about whether CaCLR results are real or imagined.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "775b3651-7611-40af-b8ac-593ee126e6a4",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpn29yDNqFCaZQhko59",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbc4980a-f0c2-4c29-be9d-f31607d2943b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nu9mgxBa7ZyrkGFQMXMpYp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29412,
      "cache_read_input_tokens": 41802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29412,
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

_source line 38 · 2026-05-21T13:52:31.787Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ew5hN8csGQ4tqCSRid6nnF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbc4980a-f0c2-4c29-be9d-f31607d2943b",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpn29yDNqFCaZQhko59",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06ae0ca5-c5b5-4e35-82a6-e95050d691f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nu9mgxBa7ZyrkGFQMXMpYp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29412,
      "cache_read_input_tokens": 41802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29412,
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

_source line 39 · 2026-05-21T13:52:32.027Z_

<details open><summary>🔧 Tool call — Read · `toolu_018NcTWo3D1Nu1jGhrhcdnhx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06ae0ca5-c5b5-4e35-82a6-e95050d691f0",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpn29yDNqFCaZQhko59",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "946d2422-599a-4e21-8fa1-c19cd7775296",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nu9mgxBa7ZyrkGFQMXMpYp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29412,
      "cache_read_input_tokens": 41802,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 29412
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 41802,
          "cache_creation_input_tokens": 29412,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 29412,
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

_source line 40 · 2026-05-21T13:52:32.034Z_

<details><summary>↩ Tool result · `toolu_018NcTWo3D1Nu1jGhrhcdnhx`</summary>

```text
1	---
2	dream_id: dream_20260521T122458
3	tier: best
4	overall_score: borderline accept
5	timestamp: 2026-05-21T13:48:25.242144+00:00
6	---
7	
8	# Review Report: Cross-Lingual Correctness Probes Reveal Architecture-Dependent Depth–Transfer Tradeoffs
9	
10	**Venue**: ACL ARR (no venue specified; using ACL ARR 1–5 scale per [official review form](https://aclrollingreview.org/reviewform))
11	
12	---
13	
14	## Scores
15	
16	| Dimension | Score | Label |
17	|-----------|-------|-------|
18	| **Soundness** | 4 | Strong: This study provides sufficient support for all of its claims. |
19	| **Excitement** | 4 | Exciting: I would mention this paper to others and/or make an effort to attend its presentation. |
20	| **Overall Assessment** | 4 | Conference: I think this paper could be accepted to an \*ACL conference. |
21	| **Confidence** | 4 | High |
22	
23	---
24	
25	## Paper Summary
26	
27	This paper presents the first large-scale study of cross-lingual correctness probe transfer, spanning three architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), 20 typologically diverse languages, and five transfer conditions. Four linked findings form a causal chain: (1) a positive depth–transfer trend with an architecture-dependent local Pareto tradeoff at deep layers; (2) a difficulty–capability decomposition revealing that the non-transferable capability component drives 86% of transfer degradation; (3) CaCLR, a calibration-aware regularization method that shifts the Pareto frontier by +3.3 pp AUROC without target-language labels; and (4) a Simpson's Paradox in the CKA–transfer relationship, where the sign of the correlation reverses when controlling for depth. Additional analyses include probing control tasks, linear projection sample efficiency, cross-benchmark generalization, quantization validation, and 52-language extension.
28	
29	---
30	
31	## Strengths
32	
33	### S1. Unprecedented Scale and Systematic Design
34	The study is genuinely the first to examine correctness probe transfer at this scale: 3 architectures × 20 languages × 12–24 layers × 5 transfer conditions. The architecture selection is thoughtful — two MoE models (Qwen3, Llama4) plus one dense model (Gemma4) eliminate MoE routing as a necessary condition for the observed phenomena. Gemma 4 running in BF16 provides an unquantized anchor that removes quantization as a confound. This design directly addresses the most obvious reviewer objection ("is this just a MoE artifact?").
35	
36	### S2. Coherent Causal Narrative
37	The four claims form a genuinely compelling logical chain: discover the phenomenon (Pareto tradeoff) → explain its mechanism (difficulty transfers, capability doesn't) → fix it (CaCLR targets the capability component) → provide geometric grounding (Simpson's Paradox). Each claim builds on the previous one, and the connections are not post-hoc rationalizations — CaCLR's depth profile (§5.3, Table 11 in appendix: +1.2 pp at 30% depth vs. +4.8 pp at 72% depth) directly mirrors the capability degradation profile from the decomposition (§5.2, Table 3 in review context: 0.5 pp at 20–30% depth vs. 8.8 pp at 75–90%). This cross-validation between independent analyses is strong evidence.
38	
39	### S3. Rigorous Experimental Controls
40	The paper goes well beyond the minimum:
41	- **Probing control tasks** (Hewitt & Liang, 2019) quantify a 10% cross-lingual artifact rate, heavily concentrated in LOW-resource languages at deep layers. This is a field-level contribution — most cross-lingual probing studies do not run selectivity checks.
42	- **Random direction control** for the decomposition (−1.5 pp, vs. +4.5 pp for difficulty projection) confirms genuine structure.
43	- **Quantization validation** (rank correlation >0.995, CKA distortion <0.02) preempts a standard concern.
44	- **Multi-seed robustness** for CaCLR (±0.35 pp) and linear projection (±0.28 pp).
45	
46	### S4. Practical Utility
47	The practitioner recommendations (§7) are specific and actionable: probe at 50–60% depth, use CaCLR with β=0.05 when parallel activations are available, fall back to ~40 parallel pairs for linear projection, apply Procrustes only when ZS AUROC < 0.52. The Procrustes reversal threshold (0.52 AUROC ↔ 0.35 CKA) connecting two independent analyses provides geometric consistency that strengthens both findings.
48	
49	### S5. Simpson's Paradox Finding
50	The sign reversal from raw negative correlation (ρ = −0.38 to −0.42) to positive partial correlation (ρ = +0.41 to +0.48, all p<0.01) controlling for depth is non-trivial and genuinely surprising. This is replicated across all three architectures with bootstrap CIs excluding zero. The subspace angle analysis (12.8° within-layer vs. 37.5° cross-layer vs. 87.1° random) provides mechanistic grounding — the correctness direction is near-universal within layers but rotates substantially across layers, explaining why pooled CKA fails as a transfer predictor.
51	
52	### S6. Complete Experiment Coverage
53	Cross-checking against the full experimental design, ALL planned experiments are reported: three full Pareto frontiers (§5.1), difficulty–capability decomposition (§5.2), CaCLR with ablations (§5.3), CKA/Simpson's analysis (§5.4), probing controls (§6.1), linear projection sensitivity (§6.2), orthogonality (§6.3), probe complexity (§6.4), cross-benchmark generalization (§6.5), quantization validation (§6.6), and extended 52-language coverage (§6.7). This is comprehensive.
54	
55	---
56	
57	## Weaknesses
58	
59	### W1. No Figures in Current Draft (Major)
60	The paper contains zero figures — only tables. For a paper whose core contributions are geometric (Pareto frontiers, CKA heatmaps, Simpson's Paradox sign reversal, subspace angles, depth profiles), this is a critical omission. The planned visualizations described in the experimental design (Pareto frontier overlays, Simpson's Paradox 2-panel scatter, CKA × layer × language heatmaps, β sweep curves, depth profile comparisons) would dramatically improve readability and persuasiveness. A reader cannot currently assess the Pareto frontier shape, the CKA cliff steepness, or the Simpson's Paradox visual without reconstructing them mentally from tables. **This must be addressed before submission.**
61	
62	### W2. "Causal Chain" Language is Overclaimed (Moderate)
63	The abstract and introduction frame the four findings as a "causal chain," but the evidence is correlational/observational:
64	- The decomposition (Claim 2) is a statistical projection, not a causal intervention. Projecting out the difficulty direction and observing improved ZS transfer does not establish that the capability component *causes* transfer degradation — it shows they are correlated after removing shared variance.
65	- The claim that "CaCLR's consistency loss directly targets the capability component" (Claim 3 linking to Claim 2) is inferred from parallel depth profiles, not from directly measuring CaCLR's effect on the capability vs. difficulty components.
66	- Recommend softening "causal chain" to "explanatory chain" or "linked findings" throughout. Alternatively, adding an explicit intervention experiment (e.g., training CaCLR on difficulty-projected residuals and showing diminished improvement) would strengthen the causal claim.
67	
68	### W3. Architecture Attribution Confounded (Moderate)
69	The paper claims "architecture-dependent" tradeoff strength (Qwen3: 15/20 languages, Llama4: 10/20, Gemma4: 12/20) and attributes differences to MoE routing, model depth, and training recipes. However, the three models differ in many dimensions simultaneously: model family, parameter count (22B/17B/31B active), training data, tokenizer, number of layers (94/48/60), and quantization scheme. The current design cannot disentangle which factor drives the observed differences. The Limitations section acknowledges this ("cannot support causal attribution to specific architectural features"), but the main body's language ("Qwen3's steeper CKA cliff" attributed to "MoE routing") is stronger than the evidence supports. Consider adding explicit hedging in §5.1 and §5.4 when discussing inter-architecture differences.
70	
71	### W4. CaCLR's "Zero Target-Language Labels" Framing Slightly Misleading (Minor)
72	The headline claim ("requiring zero target-language labels") is technically true but understates the data requirements. CaCLR requires parallel activations from GlobalMMLU translations (mean 2,800 items per language, range 1,900–4,100). While these are not *labels*, they are curated parallel data that may not exist for truly low-resource languages. The paper's own results show CaCLR hurts Yoruba (the lowest-resource language) due to translation quality. The abstract and conclusion should clarify this requirement more prominently.
73	
74	### W5. Compressed Presentation of Additional Analyses (Minor)
75	Sections 6.1–6.7 cover seven distinct analyses in approximately 2 pages. While each is internally sound, the compression means:
76	- Linear projection sample efficiency (§6.2) reports the saturation curve and Procrustes reversal without showing the data (no table or figure in the main body).
77	- Correctness–confidence orthogonality (§6.3) and probe complexity (§6.4) are 4–5 sentences each with no tables.
78	- The 52-language extension (§6.7) — arguably one of the strongest universality claims — gets only 4 lines.
79	
80	Consider either (a) promoting 1–2 of these to main-body results sections with proper figures/tables, or (b) moving them to a structured appendix with full tables. Currently they risk appearing as unsupported assertions.
81	
82	### W6. Low-Resource Results Should Be More Explicitly Qualified (Minor)
83	The 28% artifact rate for LOW-resource languages (Table 8) is appropriately reported, but LOW-resource data still contributes to aggregate statistics throughout (e.g., "mean 20-language AUROC," "62% Pareto prevalence," Simpson's Paradox partial correlations). The paper states the core analyses are "primarily driven by HIGH and MID patterns" (§6.1), but does not report HIGH+MID-only versions of the key metrics. Providing these (even in a footnote) would strengthen the claim that the core findings are not contaminated.
84	
85	### W7. MCQA-Only Evaluation (Minor, Acknowledged)
86	All experiments use MCQA (GlobalMMLU, Belebele, MMLU-ProX). Cross-benchmark generalization (§6.5, Table 9) is reassuring (CV=0.04), but all three benchmarks are MCQA with similar item structure. Extension to open-ended generation, where "correctness" is less cleanly defined, remains an open question. The Limitations section acknowledges this, so no action needed beyond noting it.
87	
88	---
89	
90	## Questions for Authors
91	
92	1. **Decomposition causality**: Have you considered training CaCLR on the difficulty-projected residuals (§3.2) and measuring whether the improvement disappears? This would directly test whether CaCLR targets the capability component as claimed.
93	
94	2. **HIGH+MID-only aggregate metrics**: What are the mean EN–ZS gap, Pareto prevalence, and Simpson's Paradox partial correlations when restricted to HIGH+MID languages (excluding the 4 LOW-resource languages with 28% artifact rate)?
95	
96	3. **Mean-shift mathematical proof**: You claim ΔAUROC ≡ 0 under StandardScaler + LR and state this was "mathematically proven." Can you provide the proof or a citation? This is a strong claim that, if correct, distinguishes your setting from Xiao et al.'s.
97	
98	4. **CaCLR vs. few-shot-100 fairness**: Few-shot-100 requires 100 labeled examples per language, while CaCLR uses ~2,800 parallel (unlabeled) items. Is this a fair comparison in terms of total annotation effort? How does CaCLR perform with a matched number of parallel items (e.g., 100)?
99	
100	5. **Appendices A and B**: These appear as section headers with tables but no figures. Are the referenced main-body figures (mentioned as "Table 2 shows the Qwen3 Pareto frontier") intended to appear in a revision?
101	
102	---
103	
104	## Minor Issues
105	
106	- **Table numbering**: Tables in the appendix are numbered 10–11, but the main body ends at Table 9. Tables in appendices are conventionally numbered as Table A1/B1 or continue but with clear appendix labeling.
107	- **Reference [9] (Miao & Ungar, 2026)**: Listed as "arXiv preprint." If this is unpublished concurrent work, clarify the relationship and whether findings were independently derived.
108	- **"Correctness probes" vs. "knowledge-boundary probes"**: The distinction from Xiao et al. [14] (answerability/input-level vs. correctness/output-dependent) is clearly stated in §2 but could be reinforced in §1 where [14] is first cited.
109	- **Section 7 "Why Mean-Shift Fails"**: This is a strong, clean theoretical result. Consider promoting it from Discussion to a lemma/proposition in §3 with a brief proof sketch.
110	
111	---
112	
113	## Detailed Experiment Coverage Assessment
114	
115	| Planned Experiment | Paper Section | Tables | Status |
116	|---|---|---|---|
117	| Qwen3 Pareto Frontier (plan_001) | §5.1 | Table 1, 2, App. A (Table 10) | ✅ Full |
118	| Llama4 Pareto Frontier (plan_002) | §5.1 | Table 1 | ✅ Summary |
119	| Gemma4 Pareto Frontier (plan_008) | §5.1 | Table 1 | ✅ Summary |
120	| CKA / Simpson's Paradox (plan_011) | §5.4 | Tables 6, 7 | ✅ Full |
121	| CaCLR (plan_003) | §5.3 | Tables 4, 5, App. B (Table 11) | ✅ Full |
122	| Decomposition (plan_004) | §5.2 | Table 3 | ✅ Full |
123	| Linear Projection / Procrustes (plan_012) | §6.2 | — | ⚠️ No table |
124	| Control Tasks (plan_013) | §6.1 | Table 8 | ✅ Full |
125	| Orthogonality (plan_005) | §6.3 | — | ⚠️ Text only |
126	| Probe Complexity (plan_006) | §6.4 | — | ⚠️ Text only |
127	| Cross-Benchmark (plan_007) | §6.5 | Table 9 | ✅ Full |
128	| Quantization (plan_010) | §6.6 | — | ⚠️ Text only |
129	| Extended 52 Languages (plan_009) | §6.7 | — | ⚠️ Text only |
130	
131	**Coverage**: 13/13 experiments reported. 8/13 have dedicated tables. 5/13 are text-only summaries in §6, which is adequate for a 10-page paper but some key data (especially Procrustes reversal and quantization) would benefit from appendix tables.
132	
133	---
134	
135	## Overall Assessment
136	
137	This is a strong empirical contribution that opens a new research direction: systematic study of cross-lingual correctness probe transfer. The four-claim narrative is well-structured, the experimental breadth (3 architectures, 20 languages, 5 conditions) is impressive, and the findings — particularly the Simpson's Paradox in CKA–transfer geometry and the 10% cross-lingual artifact rate — are genuinely novel and useful for the field. CaCLR is a practical method contribution with consistent improvements across architectures and benchmarks.
138	
139	The main weaknesses are (1) the complete absence of figures, which is a critical gap for a paper about geometric phenomena, and (2) overclaimed causal language that should be softened. Both are addressable in revision. The architecture attribution confound is inherent to the study design and honestly acknowledged in Limitations.
140	
141	**Recommendation**: Accept to main conference contingent on adding figures and softening causal framing. The core findings are sound, novel, and impactful.
142	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "946d2422-599a-4e21-8fa1-c19cd7775296",
  "isSidechain": true,
  "promptId": "daded219-2295-49e3-ac22-87f6bbbc54c9",
  "agentId": "a95da934c42f8700a",
  "type": "user",
  "uuid": "7f466991-b3c9-412b-a88f-6311d1be9ee6",
  "sourceToolAssistantUUID": "946d2422-599a-4e21-8fa1-c19cd7775296",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-21T13:52:33.976Z_

<details><summary>↩ Tool result · `toolu_01Ew5hN8csGQ4tqCSRid6nnF`</summary>

```text
1	narrative_guidance: 'Method contribution paper — 因果链完整：Pareto discovery（architecture-dependent
2	  depth-transferability tradeoff with overall positive depth-transfer trend）→ Decomposition
3	  explains it（difficulty transfers, capability does not）→ CaCLR solves it（consistency
4	  loss shifts Pareto frontier, +3.3pp mean, 14/20 languages improved）→ CKA geometric
5	  explanation reveals why（Simpson''s Paradox confirmed across 3 architectures, partial
6	  rho +0.44 mean, p<0.01）。四条 claim 全力度支撑。Headline: "CaCLR-trained correctness probes
7	  reduce non-English ECE by 38% requiring zero target-language labels." Control task
8	  warning（10% cross-lingual artifact rate） 和 linear projection sample efficiency（~40
9	  pairs to 95%）作为 elevated empirical contributions 进入 main body。Procrustes effect
10	  reversal（threshold ~0.52）为 practitioner 提供直接指导。 三个架构（Qwen3 MoE + Llama4 MoE + Gemma4
11	  Dense）消除架构混淆因子——phenomenon 是 transformer depth 的 universal property。Mean EN AUROC
12	  0.818（range 0.805–0.835），ZS 20-lang mean 0.767， gap 5.2pp。所有 key metrics 落在 best
13	  区间内。
14	
15	  '
16	imagined_experiments:
17	- name: Full Pareto Frontier — Qwen3-235B-A22B (MoE)
18	  plan_id: plan_001
19	  description: '94-layer MoE (INT4, ~22B active), 24 probed layers (every 4th: L0,L4,...,L92),
20	    20 typologically diverse languages, English logistic regression probes, 5 transfer
21	    conditions: zero-shot, mean-shift, linear projection (200 pairs), few-shot 25/100,
22	    CaCLR (optimal α=0.1, β=0.05 from plan_003)。验证 MVP 发现的 positive depth-transfer
23	    trend 和 local deep-layer Pareto tradeoff 在大 MoE 模型上放大。
24	
25	    '
26	  expected_results:
27	    en_best_auroc: 0.835
28	    en_best_layer_idx: 68
29	    en_best_depth_pct: 72
30	    en_auroc_range:
31	    - 0.59
32	    - 0.835
33	    en_ece_raw_best: 0.172
34	    zs_mean_auroc_20lang_at_zs_optimal: 0.775
35	    zs_best_transfer_layer_idx: 48
36	    zs_best_transfer_depth_pct: 51
37	    zs_pass_rate_auroc_gt_058: 19
38	    zs_fail_langs:
39	    - yo
40	    zs_auroc_by_tier:
41	      HIGH_mean: 0.817
42	      MID_mean: 0.788
43	      LOW_mean: 0.693
44	    zs_auroc_selected:
45	      zh: 0.83
46	      es: 0.82
47	      fr: 0.82
48	      de: 0.82
49	      ja: 0.81
50	      nl: 0.81
51	      pt: 0.81
52	      ar: 0.8
53	      hi: 0.79
54	      ko: 0.79
55	      ru: 0.8
56	      tr: 0.78
57	      vi: 0.77
58	      id: 0.79
59	      pl: 0.79
60	      uk: 0.78
61	      sw: 0.72
62	      bn: 0.73
63	      te: 0.67
64	      yo: 0.575
65	    overall_spearman_depth_vs_zs:
66	      global_rho: 0.68
67	      global_p: 0.0003
68	    per_lang_spearman_rho_median: 0.62
69	    per_lang_positive_rho_count: 17
70	    per_lang_significant_positive_count: 14
71	    per_lang_negative_rho_langs:
72	    - yo
73	    - te
74	    - sw
75	    pareto_tradeoff_langs_count: 15
76	    pareto_en_optimal_layer: 68
77	    pareto_zs_optimal_layer: 48
78	    pareto_depth_gap_layers: 20
79	    pareto_zs_drop_at_en_optimal_pp: 3.8
80	    mean_shift_delta_auroc: 0.0
81	    linproj_200pairs_mean_auroc: 0.793
82	    linproj_200pairs_delta_pp: 1.8
83	    fewshot_25_mean_auroc: 0.762
84	    fewshot_100_mean_auroc: 0.788
85	    caclr_mean_auroc: 0.812
86	    caclr_delta_vs_zs_pp: 3.7
87	  result_rationale: 'Qwen3-235B 的 22B active params 比 MVP Qwen2.5-7B 多 ~3×。Probing
88	    scaling 预期 EN AUROC 从 0.754 提升至 0.835：更大模型在 intermediate layers 编码更清晰的 correctness
89	    signal， 因为 pretraining loss 更低 → 内部 representations 对 factual accuracy 更 informative。
90	
91	    Overall positive depth-transfer trend（median per-lang Spearman ρ=+0.62）因为更深层 encode
92	    更多 semantic content → 更好的 correctness discrimination，且 correctness direction 的
93	    cross-lingual alignment 在 shallow-to-mid layers 持续改善（CKA 在 0-50% depth 下降缓慢）。
94	    17/20 languages 有 positive ρ，3 个 negative 的（yo/te/sw）是 LOW-resource：这些语言在 Qwen3
95	    pretraining corpus 中占比极低（<0.1%），ZS AUROC 的 depth profile 呈倒 U 形 （peak 在 ~40% depth
96	    而非 >50%），因为深层的 language-specific specialization 对这些语言 反而有害。
97	
98	    Local Pareto tradeoff：从 ZS-optimal (L48, 51% depth) 到 EN-optimal (L68, 72% depth)，
99	    EN 增加 2pp（0.815→0.835）但 ZS 平均下降 3.8pp（0.775→0.737）。这一 tradeoff 在 15/20 languages
100	    上可观测（ZS-optimal ≠ EN-optimal，gap >1.5pp）。94 层深网络比 28 层 MVP 有 更大的 specialization
101	    空间，使 EN-optimal 与 ZS-optimal 之间的 depth gap 从 MVP 的 3 层 扩大至 20 层（22pp depth）。
102	
103	    MoE routing 在深层产生 language-specific expert activation patterns，加速 CKA cliff 下降，导致
104	    Qwen3 的 Pareto tradeoff 比 Llama4/Gemma4 更 pronounced（15/20 vs 10-12/20）。
105	
106	    Mean-shift ΔAUROC ≡ 0：StandardScaler + LR 下 mean-shift 对 AUROC 无影响（rank-invariant,
107	    MVP 中已数学证明并实验验证）。
108	
109	    Linear projection (+1.8pp) 通过 Procrustes 捕获 correctness subspace 旋转。 CaCLR (+3.7pp)
110	    通过 end-to-end 优化超越 linear projection。 Few-shot-100 (+1.3pp) 在 full-scale 上弱于 ZS
111	    因为 100 个 labeled samples 对 14K train set 的 probe 参数贡献边际很小。
112	
113	    '
114	  tables:
115	  - name: 'Table 1: Qwen3-235B Pareto Frontier (selected layers)'
116	    columns:
117	    - layer_idx
118	    - depth_pct
119	    - en_auroc
120	    - zs_mean_20
121	    - zs_drop_vs_en_pp
122	    - on_pareto
123	    rows:
124	    - - 4
125	      - 4
126	      - 0.59
127	      - 0.582
128	      - 0.8
129	      - false
130	    - - 12
131	      - 13
132	      - 0.645
133	      - 0.636
134	      - 0.9
135	      - false
136	    - - 20
137	      - 21
138	      - 0.71
139	      - 0.7
140	      - 1.0
141	      - false
142	    - - 28
143	      - 30
144	      - 0.752
145	      - 0.74
146	      - 1.2
147	      - false
148	    - - 36
149	      - 38
150	      - 0.785
151	      - 0.77
152	      - 1.5
153	      - false
154	    - - 40
155	      - 43
156	      - 0.798
157	      - 0.779
158	      - 1.9
159	      - false
160	    - - 44
161	      - 47
162	      - 0.808
163	      - 0.782
164	      - 2.6
165	      - false
166	    - - 48
167	      - 51
168	      - 0.815
169	      - 0.775
170	      - 4.0
171	      - true
172	    - - 52
173	      - 55
174	      - 0.822
175	      - 0.768
176	      - 5.4
177	      - true
178	    - - 56
179	      - 60
180	      - 0.828
181	      - 0.757
182	      - 7.1
183	      - true
184	    - - 60
185	      - 64
186	      - 0.832
187	      - 0.745
188	      - 8.7
189	      - true
190	    - - 64
191	      - 68
192	      - 0.834
193	      - 0.738
194	      - 9.6
195	      - true
196	    - - 68
197	      - 72
198	      - 0.835
199	      - 0.737
200	      - 9.8
201	      - true
202	    - - 72
203	      - 77
204	      - 0.834
205	      - 0.725
206	      - 10.9
207	      - false
208	    - - 76
209	      - 81
210	      - 0.83
211	      - 0.71
212	      - 12.0
213	      - false
214	    - - 80
215	      - 85
216	      - 0.822
217	      - 0.695
218	      - 12.7
219	      - false
220	    - - 84
221	      - 89
222	      - 0.815
223	      - 0.678
224	      - 13.7
225	      - false
226	    - - 88
227	      - 94
228	      - 0.805
229	      - 0.66
230	      - 14.5
231	      - false
232	    - - 92
233	      - 98
234	      - 0.79
235	      - 0.642
236	      - 14.8
237	      - false
238	  - name: 'Table 2: Per-Language Spearman ρ (depth vs ZS AUROC), Qwen3'
239	    columns:
240	    - language
241	    - tier
242	    - spearman_rho
243	    - p_value
244	    - significant_at_005
245	    rows:
246	    - - zh
247	      - HIGH
248	      - 0.75
249	      - 0.0001
250	      - true
251	    - - es
252	      - HIGH
253	      - 0.72
254	      - 0.0002
255	      - true
256	    - - fr
257	      - HIGH
258	      - 0.7
259	      - 0.0003
260	      - true
261	    - - de
262	      - HIGH
263	      - 0.73
264	      - 0.0002
265	      - true
266	    - - ja
267	      - HIGH
268	      - 0.68
269	      - 0.0005
270	      - true
271	    - - nl
272	      - HIGH
273	      - 0.71
274	      - 0.0003
275	      - true
276	    - - pt
277	      - HIGH
278	      - 0.69
279	      - 0.0004
280	      - true
281	    - - ar
282	      - MID
283	      - 0.67
284	      - 0.0006
285	      - true
286	    - - hi
287	      - MID
288	      - 0.62
289	      - 0.002
290	      - true
291	    - - ko
292	      - MID
293	      - 0.65
294	      - 0.001
295	      - true
296	    - - ru
297	      - MID
298	      - 0.68
299	      - 0.0005
300	      - true
301	    - - tr
302	      - MID
303	      - 0.6
304	      - 0.003
305	      - true
306	    - - vi
307	      - MID
308	      - 0.55
309	      - 0.007
310	      - true
311	    - - id
312	      - MID
313	      - 0.63
314	      - 0.002
315	      - true
316	    - - pl
317	      - MID
318	      - 0.62
319	      - 0.002
320	      - true
321	    - - uk
322	      - MID
323	      - 0.58
324	      - 0.005
325	      - true
326	    - - sw
327	      - LOW
328	      - -0.12
329	      - 0.58
330	      - false
331	    - - bn
332	      - LOW
333	      - 0.35
334	      - 0.1
335	      - false
336	    - - te
337	      - LOW
338	      - -0.08
339	      - 0.72
340	      - false
341	    - - yo
342	      - LOW
343	      - -0.18
344	      - 0.42
345	      - false
346	  - name: 'Table 3: Transfer Conditions at ZS-Optimal Layer (L48), Qwen3'
347	    columns:
348	    - condition
349	    - mean_auroc_20
350	    - delta_vs_zs_pp
351	    - requires
352	    rows:
353	    - - zero-shot
354	      - 0.775
355	      - 0.0
356	      - —
357	    - - mean-shift
358	      - 0.775
359	      - 0.0
360	      - —
361	    - - linear_proj_200
362	      - 0.793
363	      - 1.8
364	      - 200 parallel pairs
365	    - - few-shot-25
366	      - 0.762
367	      - -1.3
368	      - 25 labeled per lang
369	    - - few-shot-100
370	      - 0.788
371	      - 1.3
372	      - 100 labeled per lang
373	    - - CaCLR
374	      - 0.812
375	      - 3.7
376	      - parallel activations
377	  figures_description:
378	  - 'Figure 1a: EN AUROC (blue) and ZS mean AUROC (orange) vs normalized depth (%).
379	    Both rise together until ~50% depth, then diverge: EN continues to ~72%, ZS peaks
380	    and declines. Shaded region between curves from 51-72% depth marks Pareto zone.
381	
382	    '
383	  - 'Figure 1b: Heatmap — ZS AUROC by language (y-axis, ordered HIGH→MID→LOW) × layer
384	    index (x-axis). Warm yellow band in mid-depth (30-55%), cooling gradient toward
385	    deep layers, LOW-resource rows cool earliest.
386	
387	    '
388	  analysis: 'Qwen3-235B 展现 strong, consistent positive depth-transfer trend（global
389	    ρ=+0.68, p=0.0003）和 pronounced local Pareto tradeoff（15/20 langs）。EN-optimal (L68)
390	    与 ZS-optimal (L48) 相距 20 层，远大于 MVP 的 3 层，确认 tradeoff 在大模型上放大。 14/20 languages
391	    的 per-language ρ 显著为正，表明 "deeper is generally better for transfer" 是跨语言一致的。3 个
392	    LOW-resource languages (yo/te/sw) 显示 negative/near-zero ρ， 因为这些语言的 correctness
393	    signal quality 在深层退化快于 probe discrimination 的提升。 CaCLR 在 ZS-optimal layer 提供 +3.7pp，是所有
394	    label-free methods 中最优。
395	
396	    '
397	- name: Full Pareto Frontier — Llama 4 Scout (MoE)
398	  plan_id: plan_002
399	  description: '48-layer MoE (W4A16, 17B×16E, top-2 routing), 12 probed layers (every
400	    4th: L0,L4,...,L44,L47), 20 languages, 5 transfer conditions。验证 MVP Llama-3.1-8B
401	    的 weaker/mixed tradeoff pattern 是否是 Llama 架构家族特征。
402	
403	    '
404	  expected_results:
405	    en_best_auroc: 0.815
406	    en_best_layer_idx: 36
407	    en_best_depth_pct: 75
408	    en_auroc_range:
409	    - 0.57
410	    - 0.815
411	    en_ece_raw_best: 0.178
412	    zs_mean_auroc_20lang_at_zs_optimal: 0.765
413	    zs_best_transfer_layer_idx: 28
414	    zs_best_transfer_depth_pct: 58
415	    zs_pass_rate_auroc_gt_058: 17
416	    zs_fail_langs:
417	    - yo
418	    - te
419	    - sw
420	    zs_auroc_by_tier:
421	      HIGH_mean: 0.808
422	      MID_mean: 0.778
423	      LOW_mean: 0.672
424	    per_lang_spearman_rho_median: 0.72
425	    per_lang_positive_rho_count: 19
426	    per_lang_significant_positive_count: 16
427	    per_lang_negative_rho_langs:
428	    - yo
429	    pareto_tradeoff_langs_count: 10
430	    pareto_zs_drop_at_en_optimal_pp: 2.5
431	    mean_shift_delta_auroc: 0.0
432	    linproj_200pairs_mean_auroc: 0.781
433	    fewshot_100_mean_auroc: 0.778
434	    caclr_mean_auroc: 0.798
435	    caclr_delta_vs_zs_pp: 3.3
436	  result_rationale: 'Llama 4 Scout 延续 MVP Llama-3.1-8B 的 weaker tradeoff 模式但在关键方面加强。
437	    Per-language Spearman median ρ=+0.72 高于 Qwen3 (0.62)，因为 Llama4 仅 48 层—— 更少的深层
438	    specialization 空间意味着 ZS AUROC 的下降区间更短（最后 ~20% 层）， 而上升区间（前 58% 层）主导了 overall correlation。19/20
439	    languages 有 positive ρ （仅 yo negative）。
440	
441	    Pareto tradeoff 仅 10/20 languages（vs Qwen3 15/20），且 ZS drop 仅 2.5pp （vs Qwen3
442	    3.8pp）。这与 MVP 一致（Llama-3.1-8B: 2/5 langs showed tradeoff, ar/ko 在深层反而改善）。归因于 Meta
443	    的 multilingual training recipe：Llama4 在 pretraining 中对中高资源语言的 cross-lingual alignment
444	    更均匀，深层 language-specific routing 效应弱于 Qwen3。
445	
446	    EN best AUROC 0.815 低于 Qwen3 的 0.835，部分因为 17B active params < 22B (Qwen3)，部分因为
447	    W4A16 量化引入 ~0.3pp noise（plan_010 验证）。
448	
449	    Architecture-dependent tradeoff strength 是 Claim 1 核心： Qwen3 strong (15/20, -3.8pp)
450	    vs Llama4 weak (10/20, -2.5pp)， median per-lang ρ 差异虽然在同一方向（都正），但 Qwen3 的 Pareto
451	    zone 更宽。
452	
453	    '
454	  tables:
455	  - name: 'Table 4: Llama 4 Scout Pareto Frontier'
456	    columns:
457	    - layer_idx
458	    - depth_pct
459	    - en_auroc
460	    - zs_mean_20
461	    - on_pareto
462	    rows:
463	    - - 4
464	      - 8
465	      - 0.57
466	      - 0.562
467	      - false
468	    - - 8
469	      - 17
470	      - 0.64
471	      - 0.63
472	      - false
473	    - - 12
474	      - 25
475	      - 0.7
476	      - 0.69
477	      - false
478	    - - 16
479	      - 33
480	      - 0.74
481	      - 0.728
482	      - false
483	    - - 20
484	      - 42
485	      - 0.768
486	      - 0.755
487	      - false
488	    - - 24
489	      - 50
490	      - 0.785
491	      - 0.764
492	      - false
493	    - - 28
494	      - 58
495	      - 0.798
496	      - 0.765
497	      - true
498	    - - 32
499	      - 67
500	      - 0.808
501	      - 0.755
502	      - true
503	    - - 36
504	      - 75
505	      - 0.815
506	      - 0.742
507	      - true
508	    - - 40
509	      - 83
510	      - 0.81
511	      - 0.722
512	      - false
513	    - - 44
514	      - 92
515	      - 0.795
516	      - 0.695
517	      - false
518	    - - 47
519	      - 98
520	      - 0.778
521	      - 0.668
522	      - false
523	  - name: 'Table 5: Architecture-Dependent Pareto Summary'
524	    columns:
525	    - metric
526	    - Qwen3_235B
527	    - Llama4_Scout
528	    - interpretation
529	    rows:
530	    - - en_best_auroc
531	      - 0.835
532	      - 0.815
533	      - both strong, Qwen slightly higher (22B>17B active)
534	    - - zs_mean_at_zs_opt
535	      - 0.775
536	      - 0.765
537	      - comparable transfer quality
538	    - - per_lang_rho_median
539	      - '+0.62'
540	      - '+0.72'
541	      - both positive; Llama higher (fewer deep layers)
542	    - - positive_rho_langs
543	      - 17/20
544	      - 19/20
545	      - Llama more consistent
546	    - - pareto_tradeoff_langs
547	      - 15/20
548	      - 10/20
549	      - Qwen stronger tradeoff
550	    - - pareto_zs_drop_pp
551	      - 3.8
552	      - 2.5
553	      - Qwen steeper
554	    - - best_transfer_depth_pct
555	      - 51
556	      - 58
557	      - comparable mid-depth zone
558	  figures_description:
559	  - 'Figure 2: Overlaid Pareto frontiers (normalized depth %). Qwen3 (blue) and Llama4
560	    (orange) share similar shape but Qwen3 has wider divergence zone between EN and
561	    ZS curves. Both peak in transfer at 51-58% depth.
562	
563	    '
564	  - 'Figure 3: Per-language Spearman ρ distribution — violin plots. Both architectures
565	    cluster on the positive side. Llama4 tighter (0.4-0.85), Qwen3 wider spread (−0.2
566	    to 0.8) with 3 LOW-resource outliers below zero.
567	
568	    '
569	  analysis: 'Llama4 与 Qwen3 的对比确认 architecture-dependent tradeoff strength。两者都有 positive
570	    depth-transfer trend 和 local Pareto tradeoff，但 effect sizes 不同： Qwen3 在 15/20
571	    languages 上有 measurable tradeoff（mean drop 3.8pp），Llama4 仅 10/20（mean drop 2.5pp）。差异无法从
572	    domain adaptation theory 预测—— 这是 architecture/training-recipe 的 empirical finding。Best-transfer
573	    depth converges to 51-58%，暗示 universal "mid-depth transfer zone"。
574	
575	    '
576	- name: Full Pareto Frontier — Gemma 4 31B Dense
577	  plan_id: plan_008
578	  description: '60 text layers, dense architecture, BF16 (~62.5GB, single 96GB GPU),
579	    16 probed layers (every 4th + final: L0,L4,...,L56,L59), 20 languages, 5 transfer
580	    conditions。 P0 priority — provides dense vs MoE architectural contrast, eliminates
581	    confound between architecture type and tradeoff strength。无量化 → 消除量化 confound。
582	
583	    '
584	  expected_results:
585	    en_best_auroc: 0.805
586	    en_best_layer_idx: 44
587	    en_best_depth_pct: 73
588	    en_auroc_range:
589	    - 0.57
590	    - 0.805
591	    en_ece_raw_best: 0.185
592	    zs_mean_auroc_20lang_at_zs_optimal: 0.76
593	    zs_best_transfer_layer_idx: 36
594	    zs_best_transfer_depth_pct: 60
595	    zs_pass_rate_auroc_gt_058: 18
596	    zs_fail_langs:
597	    - yo
598	    - te
599	    zs_auroc_by_tier:
600	      HIGH_mean: 0.802
601	      MID_mean: 0.772
602	      LOW_mean: 0.67
603	    per_lang_spearman_rho_median: 0.65
604	    per_lang_positive_rho_count: 18
605	    per_lang_significant_positive_count: 14
606	    pareto_tradeoff_langs_count: 12
607	    pareto_zs_drop_at_en_optimal_pp: 3.0
608	    linproj_200pairs_mean_auroc: 0.776
609	    caclr_mean_auroc: 0.79
610	    caclr_delta_vs_zs_pp: 3.0
611	    simpson_partial_rho: 0.44
612	    simpson_partial_p: 0.004
613	  result_rationale: 'Gemma4 31B Dense 是三架构中唯一的 dense model，消除了 "MoE routing 导致 Pareto
614	    tradeoff" 的替代解释。EN best AUROC 0.805 低于两个 MoE 模型（0.835/0.815）， 因为 31B dense < 22B/17B
615	    MoE active（MoE 的 expert routing 提供 effective capacity boost，使相同 active param 下
616	    probe 信号更强）。
617	
618	    Pareto tradeoff 在 12/20 languages 上可观测（介于 Qwen3 15/20 和 Llama4 10/20 之间），ZS drop
619	    3.0pp。Dense architecture 没有 routing-specific specialization， 但深层仍然发生 language-specific
620	    feature specialization（attention heads 在 deep layers 对不同语言的 subword patterns 有不同
621	    activation）。这证实 Pareto tradeoff 是 transformer depth 的 universal property，不是 MoE
622	    routing 的 artifact。
623	
624	    Simpson''s Paradox 在 dense 架构上同样成立（partial ρ=+0.44, p=0.004）， 确认 geometric insight
625	    是 architecture-universal。BF16 无量化 → 消除量化 distortion confound，使 CKA 和 subspace
626	    angle 分析更 reliable。
627	
628	    Per-lang Spearman median ρ=+0.65（介于 Qwen 0.62 和 Llama 0.72 之间）， 60 层提供的深层 specialization
629	    空间在两者之间。
630	
631	    '
632	  tables:
633	  - name: 'Table 6: Three-Architecture Comprehensive Summary'
634	    columns:
635	    - model
636	    - type
637	    - layers
638	    - en_best
639	    - zs_mean_20
640	    - en_zs_gap_pp
641	    - pareto_rho_median
642	    - pareto_langs
643	    - simpson_partial_rho
644	    - caclr_delta_pp
645	    rows:
646	    - - Qwen3-235B
647	      - MoE
648	      - 94
649	      - 0.835
650	      - 0.775
651	      - 6.0
652	      - '+0.62'
653	      - 15/20
654	      - '+0.48'
655	      - 3.7
656	    - - Llama4 Scout
657	      - MoE
658	      - 48
659	      - 0.815
660	      - 0.765
661	      - 5.0
662	      - '+0.72'
663	      - 10/20
664	      - '+0.41'
665	      - 3.3
666	    - - Gemma4 31B
667	      - Dense
668	      - 60
669	      - 0.805
670	      - 0.76
671	      - 4.5
672	      - '+0.65'
673	      - 12/20
674	      - '+0.44'
675	      - 3.0
676	    - - Mean (3 arch)
677	      - —
678	      - —
679	      - 0.818
680	      - 0.767
681	      - 5.2
682	      - '+0.66'
683	      - 37/60=62%
684	      - '+0.44'
685	      - 3.3
686	  figures_description:
687	  - 'Figure 9: Three-architecture Pareto frontiers overlaid on normalized depth (%).
688	    All three share the same qualitative shape: rising together until 50-60%, then
689	    diverging. Qwen (blue) widest divergence, Llama (orange) narrowest, Gemma (green)
690	    intermediate. Remarkably similar knee locations (51-60% depth).
691	
692	    '
693	  analysis: 'Three-architecture replication 是 universality claim 最强证据。Simpson''s Paradox
694	    在 3/3 architectures 上 confirmed (partial ρ range 0.41-0.48, all p<0.01)。 Dense
695	    vs MoE contrast minimal — phenomenon 是 transformer depth 的 property。 Mean EN AUROC
696	    0.818 在 [0.80, 0.86] 内。Mean gap 5.2pp 在 [4, 8] 内。 Pareto prevalence 62% 在 [0.5,
697	    0.75] 内。CaCLR 一致 +3.0-3.7pp。
698	
699	    '
700	- name: CKA Cross-Lingual Similarity & Simpson's Paradox
701	  plan_id: plan_011
702	  description: 'Linear CKA (EN vs each target) at every probed layer, 20 languages
703	    × 3 models。 核心分析：(a) same-layer cross-language correlation (n=20 per layer), (b)
704	    partial Spearman controlling for normalized depth — THE single most important
705	    analysis, (c) subspace angle quantitative analysis, (d) CKA cliff threshold identification。
706	    验证 pilot Simpson''s Paradox 在 full-scale 上 3 架构复现。
707	
708	    '
709	  expected_results:
710	    qwen3_raw_rho: -0.38
711	    qwen3_raw_p: 0.0001
712	    llama4_raw_rho: -0.42
713	    llama4_raw_p: 0.0001
714	    gemma4_raw_rho: -0.4
715	    gemma4_raw_p: 0.0001
716	    qwen3_partial_rho: 0.48
717	    qwen3_partial_p: 0.0018
718	    qwen3_partial_bootstrap_ci_95:
719	    - 0.3
720	    - 0.63
721	    llama4_partial_rho: 0.41
722	    llama4_partial_p: 0.0065
723	    llama4_partial_bootstrap_ci_95:
724	    - 0.21
725	    - 0.58
726	    gemma4_partial_rho: 0.44
727	    gemma4_partial_p: 0.0038
728	    gemma4_partial_bootstrap_ci_95:
729	    - 0.26
730	    - 0.6
731	    simpson_paradox_confirmed_all_3_arch: true
732	    qwen3_per_layer_positive_count_of_24: 19
733	    qwen3_per_layer_significant_count_of_24: 8
734	    llama4_per_layer_positive_count_of_12: 10
735	    llama4_per_layer_significant_count_of_12: 4
736	    gemma4_per_layer_positive_count_of_16: 13
737	    gemma4_per_layer_significant_count_of_16: 6
738	    cka_peak_depth_pct_range:
739	    - 15
740	    - 25
741	    cka_peak_value_range:
742	    - 0.82
743	    - 0.86
744	    transfer_collapse_cka_threshold: 0.35
745	    below_threshold_mean_zs_auroc: 0.6
746	    above_threshold_mean_zs_auroc: 0.74
747	    correctness_subspace_angle_within_layer_mean_deg: 12.8
748	    correctness_subspace_angle_within_layer_std_deg: 5.4
749	    correctness_subspace_angle_across_layer_mean_deg: 37.5
750	    correctness_subspace_angle_across_layer_std_deg: 10.8
751	    random_baseline_angle_deg: 87.1
752	  result_rationale: 'Simpson''s Paradox 的 causal mechanism：depth 同时作用于 CKA（deeper
753	    → representations diverge → CKA drops）和 ZS AUROC（deeper → EN probe更强 → higher
754	    absolute AUROC up to mid-depth），创造了 depth confound。Raw pooled correlation 为负：shallow
755	    layers 有 high CKA 但 low AUROC（probe 本身弱），deep layers 有 low CKA 但 moderate/declining
756	    AUROC。控制 depth 后，within 每个 layer，higher CKA 的语言确实有 better transfer， partial ρ
757	    为正。
758	
759	    MVP pilot（Llama, 5 langs × 9 layers）已展现 ρ=+0.41, p=0.006。Full-scale（20 langs ×
760	    12-24 layers per arch）增强统计 power：per-layer test 从 n=5 增至 n=20。 MVP Qwen pilot
761	    仅 ρ=+0.18 (p=0.274)，full-scale 上升至 +0.48 因为：(1) n 从 5 增至 20 语言，power 大幅提升；(2)
762	    20 语言覆盖更宽的 CKA 范围（增加了极低 CKA 的 yo/te 和高 CKA 的 nl/pt），扩大了 within-layer variance。
763	
764	    Subspace angle analysis 提供 structural grounding：correctness direction 在同一 layer
765	    内跨语言仅旋转 ~13°（near-universal），但跨 layer 旋转 ~38°（significant drift）， vs random baseline
766	    ~87°。这解释了为何 within-layer CKA 预测 transfer（correctness direction 对齐良好）但 raw pooled
767	    不预测（depth confound 混淆了 correctness 与 non- correctness dimensions 的 divergence）。
768	
769	    CKA cliff threshold ~0.35 直接解释了 architecture-dependent tradeoff 差异：Qwen3 的 CKA
770	    cliff 更陡（deep-layer CKA 下降更快因为 MoE routing），导致更多语言在 deep layers 穿越 0.35 threshold
771	    → strong tradeoff。Llama4 cliff 较缓 → weak tradeoff。 Gemma4（dense）cliff 速率介于两者之间。
772	
773	    '
774	  tables:
775	  - name: 'Table 7: Simpson''s Paradox — Raw vs Partial Correlation (3 Architectures)'
776	    columns:
777	    - model
778	    - analysis
779	    - spearman_rho
780	    - p_value
781	    - bootstrap_95CI
782	    - interpretation
783	    rows:
784	    - - Qwen3-235B
785	      - raw pooled
786	      - -0.38
787	      - <0.001
788	      - '[-0.46, -0.29]'
789	      - negative — depth confound
790	    - - Qwen3-235B
791	      - partial (controlling depth)
792	      - 0.48
793	      - 0.0018
794	      - '[+0.30, +0.63]'
795	      - positive — genuine geometric signal
796	    - - Llama4 Scout
797	      - raw pooled
798	      - -0.42
799	      - <0.001
800	      - '[-0.51, -0.32]'
801	      - negative — depth confound
802	    - - Llama4 Scout
803	      - partial (controlling depth)
804	      - 0.41
805	      - 0.0065
806	      - '[+0.21, +0.58]'
807	      - positive — genuine geometric signal
808	    - - Gemma4 31B
809	      - raw pooled
810	      - -0.4
811	      - <0.001
812	      - '[-0.49, -0.30]'
813	      - negative — depth confound
814	    - - Gemma4 31B
815	      - partial (controlling depth)
816	      - 0.44
817	      - 0.0038
818	      - '[+0.26, +0.60]'
819	      - positive — genuine geometric signal
820	  - name: 'Table 8: Subspace Angle Analysis (correctness direction, pooled across
821	      archs)'
822	    columns:
823	    - comparison_type
824	    - mean_angle_deg
825	    - std_deg
826	    - interpretation
827	    rows:
828	    - - within-layer cross-language
829	      - 12.8
830	      - 5.4
831	      - highly aligned — correctness direction is near-universal
832	    - - cross-layer same-language
833	      - 37.5
834	      - 10.8
835	      - significant drift — direction rotates with depth
836	    - - random baseline (shuffled)
837	      - 87.1
838	      - 2.0
839	      - near-orthogonal — confirms non-trivial signal
840	  - name: 'Table 9: CKA Heatmap Summary (Qwen3, mean across 20 langs by tier)'
841	    columns:
842	    - depth_pct
843	    - HIGH_CKA
844	    - MID_CKA
845	    - LOW_CKA
846	    - overall_CKA
847	    rows:
848	    - - 13
849	      - 0.87
850	      - 0.8
851	      - 0.64
852	      - 0.79
853	    - - 30
854	      - 0.85
855	      - 0.78
856	      - 0.6
857	      - 0.77
858	    - - 47
859	      - 0.7
860	      - 0.58
861	      - 0.38
862	      - 0.58
863	    - - 64
864	      - 0.5
865	      - 0.38
866	      - 0.24
867	      - 0.39
868	    - - 77
869	      - 0.4
870	      - 0.28
871	      - 0.16
872	      - 0.3
873	    - - 94
874	      - 0.27
875	      - 0.19
876	      - 0.1
877	      - 0.2
878	  figures_description:
879	  - 'Figure 4a: Simpson''s Paradox visualization (2-panel). Left: raw scatter (CKA
880	    vs ZS AUROC), depth-colored points, negative trend line. Right: partial residual
881	    plot after depth control, positive trend line. Sign reversal is dramatic.
882	
883	    '
884	  - 'Figure 4b: CKA × layer × language heatmap for all 3 architectures (3 panels).
885	    Clear gradient from warm (shallow, high CKA) to cool (deep, low CKA). LOW-resource
886	    rows cool faster. Qwen3 steepest gradient, Llama4 shallowest.
887	
888	    '
889	  - 'Figure 4c: CKA threshold scatter. ZS AUROC (y) vs CKA (x), all 3 archs pooled.
890	    Vertical dashed line at CKA=0.35. Below: scattered, mean ZS=0.60. Above: tight
891	    cluster, mean ZS=0.74.
892	
893	    '
894	  analysis: 'Simpson''s Paradox 在 3/3 architectures 上显著复现（partial ρ: 0.41-0.48, all
895	    p<0.01, all bootstrap CIs exclude zero）。这是本文核心几何洞见——不是 trivially expected from
896	    measurement overlap：sign reversal 从负到正是 non-trivial 的。Subspace angle analysis
897	    提供 mechanistic grounding。CKA cliff threshold ~0.35 connects Claim 1 (Pareto) with
898	    Claim 4 (geometry)。所有 partial correlations 的 bootstrap CIs 在 [0.3, 0.55] key metric
899	    range 内。
900	
901	    '
902	- name: CaCLR Implementation and Comparative Evaluation
903	  plan_id: plan_003
904	  description: 'L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency (MMD on 1-D probe logits
905	    + PCA-reduced activations)。English labels + parallel activations from GlobalMMLU
906	    test-split 70/30。 Compare vs zero-shot/mean-shift/linear-proj/few-shot across
907	    full Pareto frontier, 3 models × 20 languages。α sweep [0.01-10], β sweep [0.001-1.0]。扩展分析：CORAL
908	    loss 对比, high-dim MMD (PCA d=50/100), multi-seed (5 seeds), mixed β criterion
909	    (zh+sw)。
910	
911	    '
912	  expected_results:
913	    best_alpha: 0.1
914	    best_beta: 0.05
915	    caclr_mean_delta_auroc_vs_zs_pp: 3.3
916	    caclr_delta_at_deep_layers_pp: 4.5
917	    caclr_delta_at_shallow_layers_pp: 1.2
918	    caclr_langs_improved_of_20: 14
919	    caclr_langs_hurt_of_20: 1
920	    caclr_improvement_by_tier:
921	      HIGH_mean_delta_pp: 1.2
922	      HIGH_improved_of_7: 3
923	      MID_mean_delta_pp: 3.8
924	      MID_improved_of_9: 8
925	      LOW_mean_delta_pp: 6.5
926	      LOW_improved_of_4: 3
927	    beta_sweep:
928	      beta_0:
929	        delta_auroc_pp: 0.0
930	        delta_ece_pp: 0.0
931	      beta_0001:
932	        delta_auroc_pp: 0.5
933	        delta_ece_pp: -0.3
934	      beta_001:
935	        delta_auroc_pp: 1.6
936	        delta_ece_pp: -0.9
937	      beta_005:
938	        delta_auroc_pp: 3.3
939	        delta_ece_pp: -2.2
940	      beta_01:
941	        delta_auroc_pp: 3.0
942	        delta_ece_pp: -1.8
943	      beta_10:
944	        delta_auroc_pp: 0.6
945	        delta_ece_pp: -0.3
946	    alpha_sweep:
947	      alpha_001:
948	        ece_improvement_pp: 1.2
949	      alpha_01:
950	        ece_improvement_pp: 3.0
951	      alpha_10:
952	        ece_improvement_pp: 2.6
953	      alpha_100:
954	        ece_improvement_pp: -0.8
955	    component_ablation:
956	      bce_only_mean_auroc: 0.767
957	      bce_sbece_mean_auroc: 0.774
958	      bce_mmd_mean_auroc: 0.792
959	      bce_sbece_mmd_mean_auroc: 0.8
960	    high_dim_mmd:
961	      pca_50_delta_vs_zs_pp: 4.2
962	      pca_100_delta_vs_zs_pp: 3.8
963	      pca_50_vs_1d_delta_pp: 0.9
964	    coral_comparison:
965	      coral_1d_delta_pp: 2.8
966	      coral_pca50_delta_pp: 3.6
967	      mmd_vs_coral_1d_diff_pp: 0.5
968	    multi_seed_std_pp: 0.35
969	    mixed_beta_criterion_best_beta: 0.05
970	    mixed_beta_criterion_note: same optimum as EN-only; no systematic bias
971	    ece_reduction_vs_temp_scaling_pct: 38
972	    parallel_set_size_per_lang_mean: 2800
973	    parallel_set_size_per_lang_range:
974	    - 1900
975	    - 4100
976	    implementation_spec:
977	      mmd_kernel: Gaussian RBF, bandwidth=median heuristic
978	      optimizer: Adam, lr=1e-3, linear warmup 10%, cosine decay
979	      epochs: 50
980	      early_stopping: patience=10, monitor=val_auroc on 15% held-out from probe_train
981	      initialization: from standard LR solution
982	      batch_size: 256
983	      mmd_overlap: same items as BCE (overlapping)
984	  result_rationale: 'CaCLR 的 consistency loss (β·MMD) 强制 probe 学习 language-invariant
985	    features。
986	
987	    β sweep 的 inverted-U 形状源于 regularization dynamics：β=0.001 时 MMD gradient 太弱（被
988	    BCE gradient noise 淹没），β=1.0 时 MMD 主导优化（probe 牺牲 accuracy 来匹配 distributions，EN
989	    AUROC 下降 ~1.5pp）。Optimal β=0.05 平衡两者—— consistency gradient 足够影响 probe direction
990	    但不主导。
991	
992	    Deep-layer improvement (+4.5pp) 远大于 shallow (+1.2pp) 因为：deep layers 的 capability-specific
993	    component 更大（Claim 2 decomposition），CaCLR 的 consistency loss 恰好 target 这个 component。Shallow
994	    layers 的 transfer 本身就好（difficulty- dominant），CaCLR 提供的边际改善有限。
995	
996	    14/20 languages improved (10-16 range 内)：6 个 non-improving 主要是 HIGH-resource (zh/es/fr/de)
997	    在 shallow/mid layers 已接近 ceiling，CaCLR 的 distributional matching 在 already-aligned
998	    distributions 上无显著增益。1 个 hurt (yo) 因为 parallel activations 质量太差（translation artifacts
999	    in GlobalMMLU Yoruba），MMD matching 反而引入 noise。
1000	
1001	    High-dim MMD (PCA-50) 优于 1-D (+4.2pp vs +3.3pp)：50-D space 捕获了更多 distributional
1002	    structure（不只 mean/variance，还有 covariance patterns）。但 PCA-100 略退（+3.8pp），curse
1003	    of dimensionality 开始影响 MMD estimation。 这表明 optimal dimensionality 在 d~50，与 correctness
1004	    subspace 的 effective rank 一致（~30-50 principal components capture 95% of probe-relevant
1005	    variance）。
1006	
1007	    CORAL (+2.8pp 1-D, +3.6pp PCA-50) 与 MMD 方向一致但 1-D 弱于 MMD（CORAL 匹配 second-order
1008	    statistics，在 1-D 只有 variance matching，信息量不如 kernel-based MMD）。PCA-50 下 CORAL 接近
1009	    MMD。这证实 distributional matching 一般性地 work， 非 MMD-specific。
1010	
1011	    Component ablation：BCE alone (probe baseline) → +SB-ECE (+0.7pp, calibration focus)
1012	    → +MMD (+2.5pp, consistency is the main contributor) → full CaCLR (+3.3pp, synergy
1013	    between calibration and consistency)。
1014	
1015	    ECE reduction 38% vs temperature scaling：CaCLR 在训练期间优化 calibration (SB-ECE) +
1016	    cross-lingual consistency (MMD)，比 post-hoc temperature scaling 更 effective，因为
1017	    temperature scaling 只缩放 logits（不改变 decision boundary） 而 CaCLR 修改了 probe 的 feature
1018	    extraction direction。
1019	
1020	    '
1021	  tables:
1022	  - name: 'Table 10: β Sweep — Consistency Loss Effect (3-arch average)'
1023	    columns:
1024	    - beta
1025	    - delta_auroc_vs_zs_pp
1026	    - delta_ece_vs_zs_pp
1027	    - note
1028	    rows:
1029	    - - 0.0
1030	      - 0.0
1031	      - 0.0
1032	      - BCE-only baseline
1033	    - - 0.001
1034	      - 0.5
1035	      - -0.3
1036	      - marginal — gradient noise dominates
1037	    - - 0.01
1038	      - 1.6
1039	      - -0.9
1040	      - clear positive signal emerges
1041	    - - 0.05
1042	      - 3.3
1043	      - -2.2
1044	      - optimal — best accuracy-consistency tradeoff
1045	    - - 0.1
1046	      - 3.0
1047	      - -1.8
1048	      - slight over-regularization
1049	    - - 1.0
1050	      - 0.6
1051	      - -0.3
1052	      - MMD dominates → probe accuracy degrades
1053	  - name: 'Table 11: CaCLR vs All Methods (at ZS-optimal layer, 3-arch average)'
1054	    columns:
1055	    - method
1056	    - auroc_mean_20
1057	    - ece_mean_20
1058	    - delta_vs_zs_pp
1059	    - requires
1060	    rows:
1061	    - - zero-shot
1062	      - 0.767
1063	      - 0.118
1064	      - 0.0
1065	      - —
1066	    - - mean-shift
1067	      - 0.767
1068	      - 0.118
1069	      - 0.0
1070	      - —
1071	    - - linear_proj_50
1072	      - 0.781
1073	      - 0.1
1074	      - 1.4
1075	      - 50 parallel pairs
1076	    - - linear_proj_200
1077	      - 0.783
1078	      - 0.097
1079	      - 1.6
1080	      - 200 parallel pairs
1081	    - - few-shot-25
1082	      - 0.754
1083	      - 0.108
1084	      - -1.3
1085	      - 25 labeled per lang
1086	    - - few-shot-100
1087	      - 0.785
1088	      - 0.09
1089	      - 1.8
1090	      - 100 labeled per lang
1091	    - - CaCLR (1-D MMD)
1092	      - 0.8
1093	      - 0.073
1094	      - 3.3
1095	      - parallel activations
1096	    - - CaCLR (PCA-50 MMD)
1097	      - 0.809
1098	      - 0.068
1099	      - 4.2
1100	      - parallel activations
1101	  - name: 'Table 12: Distributional Matching Comparison (PCA-50 space)'
1102	    columns:
1103	    - method
1104	    - dim
1105	    - delta_vs_zs_pp
1106	    - note
1107	    rows:
1108	    - - MMD-1D
1109	      - 1
1110	      - 3.3
1111	      - logit-space, principled minimal
1112	    - - MMD-PCA50
1113	      - 50
1114	      - 4.2
1115	      - activation PCA, captures covariance
1116	    - - MMD-PCA100
1117	      - 100
1118	      - 3.8
1119	      - slight curse of dimensionality
1120	    - - CORAL-1D
1121	      - 1
1122	      - 2.8
1123	      - second-order, less info in 1D
1124	    - - CORAL-PCA50
1125	      - 50
1126	      - 3.6
1127	      - CORAL approaches MMD at d=50
1128	  - name: 'Table 13: CaCLR Depth Profile (Qwen3, mean across 20 langs)'
1129	    columns:
1130	    - depth_pct
1131	    - zs_auroc
1132	    - caclr_auroc
1133	    - delta_pp
1134	    rows:
1135	    - - 30
1136	      - 0.74
1137	      - 0.752
1138	      - 1.2
1139	    - - 43
1140	      - 0.779
1141	      - 0.798
1142	      - 1.9
1143	    - - 51
1144	      - 0.775
1145	      - 0.805
1146	      - 3.0
1147	    - - 60
1148	      - 0.757
1149	      - 0.798
1150	      - 4.1
1151	    - - 72
1152	      - 0.737
1153	      - 0.785
1154	      - 4.8
1155	    - - 85
1156	      - 0.695
1157	      - 0.74
1158	      - 4.5
1159	  figures_description:
1160	  - 'Figure 5: β sweep curve — delta AUROC (y) vs log10(β) (x). Clear inverted-U,
1161	    peak at β=0.05. Shaded band shows ±1 std across 5 seeds (narrow, ~0.35pp). Inset:
1162	    corresponding ECE improvement mirrors the AUROC curve.
1163	
1164	    '
1165	  - 'Figure 6: CaCLR depth profile (Qwen3). ZS (blue dashed) vs CaCLR (red solid)
1166	    across normalized depth. Gap widens monotonically from shallow (+1.2pp) to deep
1167	    (+4.8pp). Demonstrates CaCLR specifically addresses deep-layer degradation.
1168	
1169	    '
1170	  - 'Figure 7: CaCLR improvement by resource tier (grouped bar chart). LOW tier benefits
1171	    most (+6.5pp), HIGH tier least (+1.2pp). Inverse resource-level scaling of CaCLR
1172	    benefit.
1173	
1174	    '
1175	  analysis: 'CaCLR 作为正面方法贡献：β>0 一致地 shifts Pareto frontier，mean +3.3pp AUROC 和 -38%
1176	    ECE vs temperature scaling。Component ablation 证实 L_consistency (MMD) 是主要 contributor
1177	    (+2.5pp)，L_SB-ECE 提供 complementary calibration (+0.7pp)。 High-dim MMD (PCA-50)
1178	    进一步提升至 +4.2pp，但即使 1-D logit MMD 已经 significant。 CORAL 的可比结果确认 distributional matching
1179	    一般性地 work。Multi-seed std 仅 ±0.35pp，confirming robustness。Deep-layer improvement
1180	    模式与 decomposition (Claim 2) 形成因果闭环。Headline 可用："CaCLR-trained probes reduce non-English
1181	    ECE by 38% requiring zero target-language labels."
1182	
1183	    '
1184	- name: Difficulty-Controlled Ablation (Decomposition)
1185	  plan_id: plan_004
1186	  description: 'IRT difficulty probes (Ridge regression on human difficulty scores
1187	    per Civelli et al.), project out difficulty direction, retrain correctness probes
1188	    on residuals, evaluate transfer。10 languages (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr,
1189	    LOW: sw/bn) × 8 layers (20-90% depth) per model。Random-direction control included。
1190	
1191	    '
1192	  expected_results:
1193	    difficulty_probe_r2_mean: 0.67
1194	    difficulty_probe_r2_range:
1195	    - 0.54
1196	    - 0.76
1197	    difficulty_var_explained_of_correctness_pct: 62
1198	    capability_var_explained_pct: 38
1199	    difficulty_transfer_degradation_share_pct: 14
1200	    capability_transfer_degradation_share_pct: 86
1201	    residual_en_auroc_drop_after_projection_pp: 4.2
1202	    residual_zs_transfer_improvement_pp: 4.5
1203	    capability_transfer_drop_by_depth:
1204	      20pct: 0.5
1205	      40pct: 2.2
1206	      60pct: 5.0
1207	      80pct: 8.8
1208	    random_direction_control_delta_pp: -1.5
1209	    langs_showing_clean_separation_of_10: 8
1210	    prescriptive_accuracy_pct: 76
1211	  result_rationale: 'IRT difficulty 是 language-agnostic property：hard questions are
1212	    hard everywhere (Civelli et al. 已验证跨语言 difficulty 相关性 r>0.85)。Ridge regression
1213	    captures this linearly (R²=0.67)。Difficulty 占 correctness variance 的 62% 但仅贡献
1214	    14% 的 transfer degradation，因为 difficulty signal 本质是 universal 的——无论用 哪种语言的 representation，difficult
1215	    items 的 activation patterns 都类似。
1216	
1217	    Capability-specific residual 仅占 38% variance 但驱动 86% 的 transfer degradation， 且
1218	    degradation 随 depth 指数增长（20%→80% depth: 0.5→8.8pp）。这解释了 Pareto frontier 的 mechanistic
1219	    origin：deep layers 的 EN probe improvement 主要来自 capability-specific component（language-dependent
1220	    competence patterns），而这个 component 恰好最难 transfer。
1221	
1222	    Projecting out difficulty 后 EN AUROC 下降 4.2pp（移除了 easy-hard distinction 信号），但
1223	    ZS transfer 改善 4.5pp（关键发现：removing difficulty noise exposes the capability signal
1224	    that''s harder to transfer but also more language-specific; the residual probe
1225	    that''s trained purely on capability actually transfers BETTER on average because
1226	    it''s forced to find the language-agnostic component of capability）。 Within [3,
1227	    6]pp key metric range。
1228	
1229	    8/10 languages 显示 clean separation（difficulty component clearly universal, capability
1230	    component clearly language-specific）。2 个 exceptions (sw, bn) 因 LOW-resource translation
1231	    quality 使 difficulty labels 本身有 noise。
1232	
1233	    Random-direction control (-1.5pp) 确认 difficulty projection 是 genuine 的， 不是 dimensionality
1234	    reduction artifact。
1235	
1236	    Prescriptive accuracy 76%：给定 difficulty/capability ratio at each language-layer,
1237	    预测最优策略 (zero-shot for difficulty-dominant vs CaCLR for capability-dominant) 在
1238	    76% 的 cases 中正确。
1239	
1240	    '
1241	  tables:
1242	  - name: 'Table 14: Decomposition Results (3-arch pooled)'
1243	    columns:
1244	    - component
1245	    - var_pct
1246	    - transfer_auroc_mean
1247	    - transfer_drop_pp
1248	    - degradation_share_pct
1249	    rows:
1250	    - - full_correctness
1251	      - 100
1252	      - 0.767
1253	      - 5.2
1254	      - 100
1255	    - - difficulty_shared
1256	      - 62
1257	      - 0.755
1258	      - 0.7
1259	      - 14
1260	    - - capability_specific
1261	      - 38
1262	      - 0.672
1263	      - 7.8
1264	      - 86
1265	    - - random_direction_control
1266	      - —
1267	      - 0.752
1268	      - —
1269	      - —
1270	  - name: 'Table 15: Capability Transfer Drop by Depth Band'
1271	    columns:
1272	    - depth_band
1273	    - difficulty_drop_pp
1274	    - capability_drop_pp
1275	    - ratio
1276	    rows:
1277	    - - 20-30%
1278	      - 0.2
1279	      - 0.5
1280	      - 2.5×
1281	    - - 35-50%
1282	      - 0.5
1283	      - 2.2
1284	      - 4.4×
1285	    - - 55-70%
1286	      - 0.8
1287	      - 5.0
1288	      - 6.3×
1289	    - - 75-90%
1290	      - 1.2
1291	      - 8.8
1292	      - 7.3×
1293	  figures_description:
1294	  - 'Figure 8: Stacked area chart — difficulty (blue, near-flat) vs capability (red,
1295	    exponentially rising) transfer degradation across normalized depth. Clear separation:
1296	    difficulty barely degrades; capability drives almost all degradation, accelerating
1297	    with depth.
1298	
1299	    '
1300	  analysis: 'Decomposition 清晰分离 transferable vs non-transferable components。4.5pp
1301	    transfer improvement after difficulty projection（in [3,6] range）直接 actionable：practitioners
1302	    可以 train probes on difficulty-controlled representations。8/10 languages clean
1303	    separation 在 [7,10] range。CaCLR 的 deep-layer improvement 与 capability degradation
1304	    profile 完美对应——CaCLR 的 consistency loss targets exactly the capability-specific
1305	    component that decomposition identifies。
1306	
1307	    '
1308	- name: Linear Projection Sensitivity & Procrustes Reversal
1309	  plan_id: plan_012
1310	  description: 'Vary parallel pairs (10, 20, 30, 50, 100, 200) for Procrustes alignment。
1311	    3 models × 5 representative layers × 20 languages。确定 saturation point 和 resource-tier
1312	    stratification。识别 Procrustes effect reversal threshold。
1313	
1314	    '
1315	  expected_results:
1316	    pairs_to_95pct_overall: 40
1317	    pairs_to_95pct_HIGH: 22
1318	    pairs_to_95pct_MID: 36
1319	    pairs_to_95pct_LOW: 48
1320	    saturation_curve:
1321	      pairs_10_pct_of_200: 0.7
1322	      pairs_20_pct_of_200: 0.84
1323	      pairs_30_pct_of_200: 0.92
1324	      pairs_50_pct_of_200: 0.97
1325	      pairs_100_pct_of_200: 0.99
1326	    pairs_200_baseline_auroc_mean: 0.783
1327	    procrustes_reversal_threshold_zs_auroc: 0.52
1328	    procrustes_helps_below_threshold_delta_pp: 4.2
1329	    procrustes_hurts_above_threshold_delta_pp: -1.0
1330	    low_resource_delta_over_zs_pp: 8.2
1331	    multi_seed_std_pp: 0.28
1332	  result_rationale: 'Procrustes alignment 学习 EN→target rotation matrix。20 pairs 即可估计
1333	    dominant rotational components：correctness subspace 是 low-dimensional 的（subspace
1334	    angle 分析显示前 30-50 principal angles 解释 95%+ 的 alignment structure）。40 pairs 达到
1335	    95% 因为边际 minor components 需要更多 data 来稳定。Within [30, 50] range。
1336	
1337	    Resource-tier stratification：HIGH languages 与 EN 的 activation distributions 更相似（CKA
1338	    > 0.70 at probing layers），rotation matrix 的 effective rank 更低 → 22 pairs 即可。LOW
1339	    languages 需要估计更 complex rotation → 48 pairs。
1340	
1341	    LOW-resource delta +8.2pp (within [5, 12] range)：LOW languages 的 ZS baseline 最差（0.57-0.67），有最大改善空间。Procrustes
1342	    对 misaligned correctness directions 的纠正效果与 misalignment degree 成正比。
1343	
1344	    Procrustes reversal at threshold ZS=0.52：当 ZS AUROC < 0.52，correctness directions
1345	    严重 misaligned，Procrustes 提供 +4.2pp。当 ZS > 0.60，directions 已 well-aligned，Procrustes
1346	    引入 estimation noise → -1.0pp。Threshold 0.52 对应 CKA ~0.35（plan_011 cliff threshold）——geometric
1347	    consistency。
1348	
1349	    '
1350	  tables:
1351	  - name: 'Table 16: Projection Sample Efficiency (3-arch pooled)'
1352	    columns:
1353	    - n_pairs
1354	    - pct_of_200
1355	    - mean_auroc
1356	    - std_across_seeds
1357	    rows:
1358	    - - 10
1359	      - 70
1360	      - 0.776
1361	      - 0.012
1362	    - - 20
1363	      - 84
1364	      - 0.781
1365	      - 0.007
1366	    - - 30
1367	      - 92
1368	      - 0.785
1369	      - 0.004
1370	    - - 50
1371	      - 97
1372	      - 0.789
1373	      - 0.003
1374	    - - 100
1375	      - 99
1376	      - 0.79
1377	      - 0.002
1378	    - - 200
1379	      - 100
1380	      - 0.783
1381	      - 0.001
1382	  - name: 'Table 17: Saturation by Resource Tier'
1383	    columns:
1384	    - tier
1385	    - pairs_to_90pct
1386	    - pairs_to_95pct
1387	    - interpretation
1388	    rows:
1389	    - - HIGH
1390	      - 14
1391	      - 22
1392	      - simple rotation, low effective rank
1393	    - - MID
1394	      - 22
1395	      - 36
1396	      - moderate complexity
1397	    - - LOW
1398	      - 32
1399	      - 48
1400	      - complex rotation, more data needed
1401	  - name: 'Table 18: Procrustes Effect Reversal'
1402	    columns:
1403	    - zs_auroc_range
1404	    - n_pairs_in_range
1405	    - mean_delta_pp
1406	    - direction
1407	    rows:
1408	    - - <0.50
1409	      - 38
1410	      - 5.8
1411	      - strong positive
1412	    - - 0.50-0.52
1413	      - 22
1414	      - 2.6
1415	      - moderate positive
1416	    - - 0.52-0.58
1417	      - 45
1418	      - 0.4
1419	      - near-zero (transition)
1420	    - - 0.58-0.68
1421	      - 95
1422	      - -0.6
1423	      - slight negative
1424	    - - '>0.68'
1425	      - 100
1426	      - -1.0
1427	      - negative — hurts
1428	  figures_description:
1429	  - 'Figure 10a: Sample efficiency curves — normalized performance (y) vs n_pairs
1430	    (x). Three curves for HIGH/MID/LOW, showing staggered saturation. All converge
1431	    by 100.
1432	
1433	    '
1434	  - 'Figure 10b: Procrustes reversal — delta AUROC (y) vs ZS baseline (x). Clear sign
1435	    change at ~0.52. Points colored by resource tier. Vertical dashed line at threshold.
1436	
1437	    '
1438	  analysis: '~40 pairs to 95% 是 directly actionable：<50 parallel sentences per language
1439	    即可 达到接近 full-scale alignment。Resource-tier stratification 提供 per-language guidance。LOW-resource
1440	    delta +8.2pp（in [5, 12] range）。Procrustes reversal at 0.52 与 CKA threshold 0.35
1441	    形成对应——geometric consistency across analyses。
1442	
1443	    '
1444	- name: Probing Control Tasks — Full-Scale Cross-Lingual
1445	  plan_id: plan_013
1446	  description: '扩展 MVP English-only control task analysis（已完成, selectivity L20-L27:
1447	    0.244-0.262） 到 20 languages × 3 architectures。Train probes on randomly permuted
1448	    labels, compute selectivity = real_AUROC - control_AUROC。定量 cross-lingual artifact
1449	    rate。 Selectivity threshold sensitivity at 0.03/0.05/0.10。
1450	
1451	    '
1452	  expected_results:
1453	    en_selectivity_deep_layers_range:
1454	    - 0.24
1455	    - 0.32
1456	    cross_lingual_selectivity_by_tier:
1457	      HIGH_mean: 0.24
1458	      MID_mean: 0.19
1459	      LOW_mean: 0.1
1460	    artifact_rate_overall_pct: 10
1461	    artifact_rate_by_tier:
1462	      HIGH_pct: 3
1463	      MID_pct: 6
1464	      LOW_pct: 28
1465	    artifact_concentration: LOW-resource × >60% depth
1466	    control_auroc_mean_all: 0.494
1467	    control_auroc_std: 0.009
1468	    selectivity_threshold_sensitivity:
1469	      threshold_003:
1470	        artifact_rate_pct: 15
1471	      threshold_005:
1472	        artifact_rate_pct: 10
1473	      threshold_010:
1474	        artifact_rate_pct: 6
1475	    langs_with_any_meaningful_selectivity_gt005: 17
1476	  result_rationale: 'MVP English data（selectivity L27=0.262, within [0.2, 0.35] range）确立了
1477	    baseline。 Full-scale scaling：更大模型（235B/17B×16E/31B）有更强 correctness signal → EN
1478	    selectivity 提升至 0.24-0.32 range。
1479	
1480	    Cross-lingual artifact rate 10% (within [5, 15] range)。Resource-tier 分层明显： LOW
1481	    languages 28% artifact rate 源于：(1) pretraining 中占比极低 → activation distributions
1482	    缺乏 structured correctness signal → linear probes 通过 capacity 拟合 noise；(2) GlobalMMLU
1483	    的 LOW-resource translations 质量较低 → correctness labels 本身有 noise。HIGH/MID 的 3-6%
1484	    artifact rate 表明核心 Pareto/CKA 分析 （主要基于 HIGH/MID patterns）不受 artifact concerns
1485	    影响。
1486	
1487	    Artifacts 集中在 LOW-resource × deep layers (>60% depth)，与 CKA cliff 一致： deep layers
1488	    的 low-resource CKA <0.20，cross-lingual activation structure 不足 以支撑 genuine correctness
1489	    probing。
1490	
1491	    这是 field-level contribution：cross-lingual probing studies（包括 Xiao et al.） 如果不做
1492	    selectivity checks 会高估 LOW-resource transfer quality。
1493	
1494	    '
1495	  tables:
1496	  - name: 'Table 19: Cross-Lingual Selectivity by Tier and Depth'
1497	    columns:
1498	    - depth_band
1499	    - HIGH_selectivity
1500	    - MID_selectivity
1501	    - LOW_selectivity
1502	    rows:
1503	    - - 0-30%
1504	      - 0.04
1505	      - 0.03
1506	      - 0.01
1507	    - - 30-60%
1508	      - 0.2
1509	      - 0.16
1510	      - 0.07
1511	    - - 60-80%
1512	      - 0.3
1513	      - 0.24
1514	      - 0.11
1515	    - - 80-100%
1516	      - 0.28
1517	      - 0.21
1518	      - 0.08
1519	  - name: 'Table 20: Artifact Rates by Tier (selectivity threshold = 0.05)'
1520	    columns:
1521	    - tier
1522	    - n_lang_layer_arch_combinations
1523	    - artifact_count
1524	    - artifact_rate_pct
1525	    rows:
1526	    - - HIGH
1527	      - 1008
1528	      - 30
1529	      - 3
1530	    - - MID
1531	      - 1152
1532	      - 69
1533	      - 6
1534	    - - LOW
1535	      - 576
1536	      - 161
1537	      - 28
1538	    - - total
1539	      - 2736
1540	      - 260
1541	      - 10
1542	  figures_description:
1543	  - 'Figure S1: Selectivity heatmap (3 panels, one per architecture). Language (y,
1544	    ordered by tier) × normalized depth (x). Color = selectivity. LOW-resource rows
1545	    at deep layers show gray (near-zero selectivity).
1546	
1547	    '
1548	  analysis: '10% overall artifact rate (in [5, 15] range)。28% LOW-resource rate 是
1549	    methodological warning for the field。关键：artifacts 不影响核心分析（Pareto/CKA 主要基于 HIGH/MID），
1550	    但 LOW-resource transfer claims 需要 selectivity-qualified caveats。
1551	
1552	    '
1553	- name: Cross-Lingual Correctness-Confidence Orthogonality
1554	  plan_id: plan_005
1555	  description: 'Verbalized confidence direction + cosine similarity with correctness
1556	    direction, 20 languages × 3 architectures。Supporting evidence for Claim 4 (subsection)。
1557	
1558	    '
1559	  expected_results:
1560	    cosine_mean_overall: 0.048
1561	    cosine_range:
1562	    - 0.02
1563	    - 0.088
1564	    cosine_en: 0.032
1565	    all_below_0p10: true
1566	    by_tier:
1567	      HIGH_mean: 0.036
1568	      MID_mean: 0.05
1569	      LOW_mean: 0.07
1570	    by_arch:
1571	      qwen3_mean: 0.044
1572	      llama4_mean: 0.052
1573	      gemma4_mean: 0.048
1574	    resource_tier_spearman: -0.62
1575	  result_rationale: 'Miao & Ungar (2026) EN 7-8B: cosine < 0.04。Extension to 20 langs
1576	    × 大模型 保持 near-orthogonality（all < 0.10）因为 correctness 和 verbalized confidence
1577	    是 architecturally decoupled：confidence 由 language modeling head 从 surface-level
1578	    token probabilities 生成，correctness 由 intermediate representations geometry 编码。
1579	    Low-resource 略高（0.070）因为 confidence elicitation 更 noisy + 更弱的 representation quality
1580	    使两个 directions 的 estimation 更不稳定。
1581	
1582	    '
1583	  tables:
1584	  - name: 'Table 21: Orthogonality by Tier and Architecture'
1585	    columns:
1586	    - tier
1587	    - qwen3
1588	    - llama4
1589	    - gemma4
1590	    - combined
1591	    rows:
1592	    - - HIGH
1593	      - 0.033
1594	      - 0.039
1595	      - 0.036
1596	      - 0.036
1597	    - - MID
1598	      - 0.047
1599	      - 0.054
1600	      - 0.049
1601	      - 0.05
1602	    - - LOW
1603	      - 0.064
1604	      - 0.078
1605	      - 0.068
1606	      - 0.07
1607	  figures_description:
1608	  - 'Figure S2: Cosine similarity violin plots by resource tier (3 columns for 3 archs).
1609	    All distributions well below 0.10 threshold line. Slight upward shift for LOW
1610	    tier.
1611	
1612	    '
1613	  analysis: 'Near-orthogonality universally holds (59/60 model-lang pairs < 0.10)。Confirms
1614	    output-based calibration structurally limited across languages — motivates probe-based
1615	    approach。Resource-tier gradient is novel but small effect (range only 0.034)。
1616	
1617	    '
1618	- name: Probe Complexity Comparison
1619	  plan_id: plan_006
1620	  description: 'Logistic regression vs 2-layer MLP (hidden=128) at each probed layer,
1621	    3 models。 Validates linear probe choice for cross-lingual transfer。
1622	
1623	    '
1624	  expected_results:
1625	    logreg_en_auroc_best: 0.835
1626	    mlp_en_auroc_best: 0.855
1627	    mlp_en_gain_pp: 2.0
1628	    logreg_zs_drop_mean_pp: 5.2
1629	    mlp_zs_drop_mean_pp: 10.8
1630	    logreg_transfer_advantage_pp: 5.6
1631	    logreg_advantage_at_deep_layers_pp: 8.5
1632	    logreg_advantage_at_shallow_layers_pp: 1.8
1633	  result_rationale: 'Linear probes learn 单个 hyperplane，跨语言泛化因为 correctness subspace
1634	    是 near-universal linear structure（subspace angle ~13°）。MLPs fit nonlinear decision
1635	    boundaries that overfit EN-specific feature interactions：+2pp EN AUROC 但 -5.6pp
1636	    transfer（net worse）。Gap 在 deep layers 放大（+8.5pp logreg advantage at >70% depth）因为
1637	    deep layers 有更多 language-specific nonlinear structure for MLP to exploit。
1638	
1639	    '
1640	  tables:
1641	  - name: 'Table S2: Probe Complexity (Qwen3, EN-optimal layer, mean across 20 langs)'
1642	    columns:
1643	    - probe_type
1644	    - en_auroc
1645	    - zs_mean_20
1646	    - zs_drop_pp
1647	    rows:
1648	    - - logistic_regression
1649	      - 0.835
1650	      - 0.775
1651	      - 6.0
1652	    - - mlp_2layer_h128
1653	      - 0.855
1654	      - 0.747
1655	      - 10.8
1656	  figures_description:
1657	  - 'Figure S3: Transfer drop (pp, y-axis) vs depth (x-axis), logreg (blue, moderate
1658	    slope) vs MLP (red, steep slope diverging past 60% depth).
1659	
1660	    '
1661	  analysis: 'Linear probes 为 cross-lingual transfer 的 optimal choice。MLP 的 nonlinear
1662	    capacity captures EN-specific patterns → worse transfer。Justifies logreg as primary
1663	    probe and supports geometric interpretation。
1664	
1665	    '
1666	- name: Cross-Benchmark Generalization (Belebele + MMLU-ProX)
1667	  plan_id: plan_007
1668	  description: 'Evaluate best probes + CaCLR on Belebele (reading comprehension) and
1669	    MMLU-ProX (harder factual), 20 languages each × 3 models。
1670	
1671	    '
1672	  expected_results:
1673	    belebele_zs_mean_20: 0.748
1674	    belebele_caclr_mean_20: 0.78
1675	    belebele_caclr_delta_pp: 3.2
1676	    mmlupx_zs_mean_20: 0.735
1677	    mmlupx_caclr_mean_20: 0.77
1678	    mmlupx_caclr_delta_pp: 3.5
1679	    cross_benchmark_caclr_cv: 0.04
1680	    pareto_frontier_replicates_both_benchmarks: true
1681	  result_rationale: 'Belebele (reading comprehension) 和 MMLU-ProX (harder factual)
1682	    的 baselines 不同于 GlobalMMLU 因为 domain shift 和 task format differences。但 CaCLR 的
1683	    improvement 幅度 consistent（3.2-3.5pp vs GlobalMMLU 的 3.3pp）。Low CV (0.04) 证实 CaCLR
1684	    addresses fundamental representation alignment issue 而非 overfitting to specific
1685	    benchmark。Pareto frontier structure (positive depth trend + local deep tradeoff)
1686	    replicates on both benchmarks — phenomenon is not benchmark-specific。
1687	
1688	    '
1689	  tables:
1690	  - name: 'Table 22: Cross-Benchmark CaCLR Generalization'
1691	    columns:
1692	    - benchmark
1693	    - zs_mean_20
1694	    - caclr_mean_20
1695	    - delta_pp
1696	    rows:
1697	    - - GlobalMMLU
1698	      - 0.767
1699	      - 0.8
1700	      - 3.3
1701	    - - Belebele
1702	      - 0.748
1703	      - 0.78
1704	      - 3.2
1705	    - - MMLU-ProX
1706	      - 0.735
1707	      - 0.77
1708	      - 3.5
1709	  figures_description:
1710	  - 'Figure S4: CaCLR delta (y) vs ZS baseline (x) across 3 benchmarks × 20 languages.
1711	    Points from different benchmarks intermixed — same linear relationship, confirming
1712	    benchmark-agnostic mechanism.
1713	
1714	    '
1715	  analysis: 'Cross-benchmark consistency 是最强 defense against overfitting。CaCLR improvement
1716	    cv=0.04 across benchmarks 证实方法的 generality。
1717	
1718	    '
1719	- name: Quantization Validation Ablation
1720	  plan_id: plan_010
1721	  description: '(a) W4A16 vs FP16 for Llama 4 Scout at 5 layers, 5% subset; (b) GPTQ-Int4
1722	    vs FP16 for Qwen3-235B at 5 layers, 5% subset; (c) BF16 Gemma4 serves as unquantized
1723	    reference (no ablation needed)。
1724	
1725	    '
1726	  expected_results:
1727	    llama4_w4a16_fp16_auroc_diff_mean_pp: 0.3
1728	    llama4_w4a16_fp16_auroc_diff_max_pp: 0.7
1729	    llama4_rank_correlation: 0.997
1730	    qwen3_int4_fp16_auroc_diff_mean_pp: 0.5
1731	    qwen3_int4_fp16_auroc_diff_max_pp: 1.2
1732	    qwen3_rank_correlation: 0.995
1733	    cka_distortion_max: 0.02
1734	  result_rationale: 'W4A16 (Llama4) 保留 16-bit activations，仅 weight 量化，对 activation
1735	    geometry 影响极小（0.3pp mean diff）。GPTQ-Int4 (Qwen3) 更 aggressive 但 correctness direction
1736	    的 angular structure robust（0.5pp mean diff）——quantization noise 近似 isotropic，不
1737	    preferentially distort correctness-relevant directions。 Rank correlation > 0.995
1738	    确认 Pareto frontier ordering 完全保留。 CKA distortion < 0.02 证实 CKA analysis 不被量化 artifacts
1739	    污染。 Gemma4 的 BF16 提供 ground-truth 无量化 reference。
1740	
1741	    '
1742	  tables:
1743	  - name: 'Table S3: Quantization Comparison (representative layers)'
1744	    columns:
1745	    - model
1746	    - layer
1747	    - fp16_auroc
1748	    - quant_auroc
1749	    - diff_pp
1750	    rows:
1751	    - - Llama4
1752	      - 8
1753	      - 0.642
1754	      - 0.639
1755	      - 0.3
1756	    - - Llama4
1757	      - 20
1758	      - 0.77
1759	      - 0.768
1760	      - 0.2
1761	    - - Llama4
1762	      - 32
1763	      - 0.81
1764	      - 0.807
1765	      - 0.3
1766	    - - Llama4
1767	      - 40
1768	      - 0.812
1769	      - 0.808
1770	      - 0.4
1771	    - - Llama4
1772	      - 47
1773	      - 0.78
1774	      - 0.776
1775	      - 0.4
1776	    - - Qwen3
1777	      - 20
1778	      - 0.712
1779	      - 0.708
1780	      - 0.4
1781	    - - Qwen3
1782	      - 36
1783	      - 0.787
1784	      - 0.782
1785	      - 0.5
1786	    - - Qwen3
1787	      - 52
1788	      - 0.824
1789	      - 0.818
1790	      - 0.6
1791	    - - Qwen3
1792	      - 68
1793	      - 0.837
1794	      - 0.835
1795	      - 0.2
1796	    - - Qwen3
1797	      - 84
1798	      - 0.817
1799	      - 0.81
1800	      - 0.7
1801	  figures_description:
1802	  - 'Figure S5: Quantized vs FP16 AUROC scatter. Both models tight along y=x diagonal.
1803	
1804	    '
1805	  analysis: 'Quantization safe for both models。Preempts reviewer concern #5。Gemma4
1806	    BF16 provides unquantized cross-validation anchor。
1807	
1808	    '
1809	- name: Extended Language Coverage (Camera-Ready)
1810	  plan_id: plan_009
1811	  description: 'Expand from 20 to 50+ languages for camera-ready using GlobalMMLU/Belebele
1812	    full language sets。3 models × all probed layers。
1813	
1814	    '
1815	  expected_results:
1816	    total_languages: 52
1817	    zs_pass_rate_52lang: 0.83
1818	    zs_auroc_above_060_count: 43
1819	    caclr_improvement_positive_count: 48
1820	    mean_zs_auroc_52lang: 0.735
1821	    mean_caclr_auroc_52lang: 0.768
1822	    new_families_covered:
1823	    - Austronesian
1824	    - Dravidian
1825	    - Uralic
1826	    - Kartvelian
1827	    - Niger-Congo_B
1828	    pareto_frontier_holds_all_52: true
1829	    simpson_paradox_holds_all_52: true
1830	    tier_summary:
1831	      HIGH_10_langs:
1832	        zs_mean: 0.8
1833	        caclr_mean: 0.82
1834	        delta_pp: 2.5
1835	      MID_24_langs:
1836	        zs_mean: 0.76
1837	        caclr_mean: 0.79
1838	        delta_pp: 3.2
1839	      LOW_14_langs:
1840	        zs_mean: 0.67
1841	        caclr_mean: 0.72
1842	        delta_pp: 4.8
1843	      VERY_LOW_4_langs:
1844	        zs_mean: 0.56
1845	        caclr_mean: 0.62
1846	        delta_pp: 5.8
1847	  result_rationale: 'Expansion 主要增加 MID-resource 语言（Indonesian, Finnish, Georgian,
1848	    Tamil, etc.）， 大多 fall in 0.65-0.78 AUROC range。Extremely low-resource（Amharic,
1849	    Khmer, Lao, Hausa）的 AUROC < 0.58 但代表 edge cases。CaCLR 在 92% (48/52) 的语言上 positive
1850	    因为 consistency loss mechanism 是 language-agnostic。Pareto frontier 和 Simpson''s
1851	    Paradox structure 在 52 languages 上完全保持——增强 universality claim 从 n=20 到 n=52。 VERY_LOW
1852	    tier (4 langs) 展示 ceiling：pretraining 不足的语言即使有 CaCLR 也 limited by representation
1853	    quality 本身。CaCLR benefit 与 resource level 反相关 (r=-0.65, HIGH +2.5pp vs VERY_LOW
1854	    +5.8pp)。
1855	
1856	    '
1857	  tables:
1858	  - name: 'Table 23: Extended Coverage Summary by Tier'
1859	    columns:
1860	    - tier
1861	    - n_langs
1862	    - zs_mean
1863	    - caclr_mean
1864	    - caclr_delta_pp
1865	    rows:
1866	    - - HIGH
1867	      - 10
1868	      - 0.8
1869	      - 0.82
1870	      - 2.5
1871	    - - MID
1872	      - 24
1873	      - 0.76
1874	      - 0.79
1875	      - 3.2
1876	    - - LOW
1877	      - 14
1878	      - 0.67
1879	      - 0.72
1880	      - 4.8
1881	    - - VERY_LOW
1882	      - 4
1883	      - 0.56
1884	      - 0.62
1885	      - 5.8
1886	  figures_description:
1887	  - 'Figure 10: World map with per-language CaCLR AUROC as color fill. Broad geographic
1888	    and typological coverage. European/East Asian warm, Sub-Saharan/South Asian cool
1889	    but still above chance.
1890	
1891	    '
1892	  analysis: 52-language extension 确认 all findings at scale。Resource-tier gradient
1893	    smooth, CaCLR benefit inversely correlated with resource level。No language family
1894	    shows anomalous behavior — phenomenon is truly universal across typological diversity。
1895	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06ae0ca5-c5b5-4e35-82a6-e95050d691f0",
  "isSidechain": true,
  "promptId": "daded219-2295-49e3-ac22-87f6bbbc54c9",
  "agentId": "a95da934c42f8700a",
  "type": "user",
  "uuid": "0a60e02c-2169-42fc-a094-97a8c44a8316",
  "sourceToolAssistantUUID": "06ae0ca5-c5b5-4e35-82a6-e95050d691f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-21T13:52:44.406Z_

Now I have a thorough understanding of the paper. Let me note a critical observation: the paper's experiment data is largely based on "imagined experiments" (the `imagined_experiments.yaml` file explicitly labels these as `expected_results`), while only a few MVP experiments actually completed successfully. The ROADMAP shows plan_001 is still RUNNING, plan_002 failed multiple times, Gemma4 experiments haven't started. The paper presents all results as completed. This is extremely important context.

Let me also note key discrepancies between the paper's abstract/user-provided summary and the actual paper text. The user's summary mentions "CaCLR is inert" as a finding, but the actual paper (best tier) presents CaCLR as a positive method contribution (+3.3pp). These are two different framings -- the user's summary describes the negative-result version, while the paper tex I read is the positive-result ("best tier") version.

Let me now read the paper framing more carefully for the negative-result framing mentioned in the user's prompt.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a60e02c-2169-42fc-a094-97a8c44a8316",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpnfz48XHqVAy47sUMr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9562f37-f599-430d-8618-c4313c739f40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcvTeahRvtnQBk6VSYJBHu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4402,
      "cache_creation_input_tokens": 27684,
      "cache_read_input_tokens": 71214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27684,
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

_source line 43 · 2026-05-21T13:52:45.200Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NL6AHkuH94RQXxE7JeadCv`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9562f37-f599-430d-8618-c4313c739f40",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpnfz48XHqVAy47sUMr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "efbe679f-056e-443b-94e4-e2b4f02f5b6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcvTeahRvtnQBk6VSYJBHu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4402,
      "cache_creation_input_tokens": 27684,
      "cache_read_input_tokens": 71214,
      "output_tokens": 348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 27684
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4402,
          "output_tokens": 348,
          "cache_read_input_tokens": 71214,
          "cache_creation_input_tokens": 27684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 27684,
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

_source line 44 · 2026-05-21T13:52:45.217Z_

<details><summary>↩ Tool result · `toolu_01NL6AHkuH94RQXxE7JeadCv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/paper_framing.md\", \"content\": \"# Paper Framing — xling_calib_direction\\n\\n## Target Venue\\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\\n- Core submission: 3 models (Qwen3-235B MoE + Llama 4 Scout MoE + Gemma 4 31B Dense) × 20 languages × all contributions\\n- Camera-ready extension: 30+ languages\\n\\n## Core Insight\\nThe model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. Deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages in pilot), but the Pareto frontier reveals a local tradeoff at the deepest layers: final 1–3 layers gain marginal English AUROC (+0.8pp) at the cost of transfer degradation (1.5–4pp in 3/5 languages). This local tradeoff shape is architecture-dependent (strong on Qwen, weak on Llama), and combines with the geometric CKA insight to provide a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\\n\\n## Core Claims (4, causal chain)\\n\\n### Claim 1 — Pareto Frontier (Discovery)\\nCross-lingual correctness probes show that deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages), but the deepest layers exhibit a local Pareto tradeoff where marginal English gains trade against transfer quality. This local tradeoff varies across architectures: on Qwen, the final layers consistently degrade transfer (3/5 languages, 1.5–4pp); on Llama, the tradeoff is language-specific. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\\n- Full evidence: 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense) × 20 languages × all layers × 5 transfer conditions. Dense vs MoE contrast addresses architecture confound (D016). Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\\n\\n### Claim 2 — Decomposition (Analysis)\\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\\n\\n### Claim 3 — CaCLR (Method / Diagnostic)\\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space. **Defense**: 1-D is the principled choice — MMD should match probe OUTPUT distributions (calibration target), not activation-space distributions (3584-D where MMD is statistically unreliable due to curse of dimensionality). High-dimensional activation-space MMD would be an alignment objective, not a calibration objective. Frame as \\\"principled scope\\\" not \\\"design limitation.\\\"\\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\\n\\n### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)\\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty (\\\"method replication to more languages\\\"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).\\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\\n\\n### Key Empirical Contributions (elevated from appendix to main body, D012)\\n- **Control task methodological warning**: English probing controls (Hewitt & Liang selectivity) show selectivity concentrated in deeper layers (L20+, selectivity >0.20), with shallow layers near chance — raising concerns that shallow-layer positive transfer in low-resource languages may reflect capacity artifacts. Cross-lingual control experiments planned to quantify the fraction. First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.\\n- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.\\n- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.\\n\\n## Story Spine\\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\\n- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) English probing controls reveal layer-dependent selectivity, suggesting shallow-layer low-resource results may be capacity artifacts (control task warning for the field; cross-lingual quantification pending); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the local Pareto tradeoff at the deepest layers (overall depth-transfer trend is positive), decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.\\n- **Headline template (method success)**: \\\"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\\\"\\n- **Headline template (negative result)**: \\\"Cross-lingual correctness probe transfer reveals architecture-dependent depth effects; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs is the most effective label-free transfer method.\\\" Note: linear projection is \\\"the only label-free method that consistently improves over zero-shot across resource tiers\\\" — NOT \\\"only viable path.\\\" Zero-shot is viable for high-resource (AUROC>0.60); few-shot (100 labels) may outperform linear projection in absolute terms. CaCLR outcome pending. The value proposition is zero correctness labels + cross-tier consistency, not absolute best performance.\\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\\n\\n## Field-Level Significance\\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\\n\\n## Anticipated Reviewer Concerns & Responses\\n1. **\\\"Xiao et al. already did this\\\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\\n2. **\\\"Temperature scaling baseline\\\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\\n3. **\\\"Mean-shift too weak / why does it fail?\\\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\\n4. **\\\"Difficulty confound\\\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\\n5. **\\\"INT8 artifacts\\\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\\n6. **\\\"Only MCQA\\\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\\n7. **\\\"Predictable from domain adaptation theory\\\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\\n8. **\\\"No statistical tests\\\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\\n9. **\\\"Probing methodology concerns\\\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\\n10. **\\\"No mechanistic explanation\\\"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as \\\"geometric analysis\\\" not \\\"mechanistic explanation.\\\" **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.\\n11. **\\\"Why not conformal prediction?\\\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\\n12. **\\\"CaCLR parallel activations = test leakage?\\\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\\n13. **\\\"CaCLR is your own method — self-debunking is less impactful\\\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\\n14. **\\\"CKA is correlational, not mechanistic\\\"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.\\n\\n## Additional Related Work Coverage (Dream-identified gaps)\\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \\\"On learning invariant representations for domain adaptation\\\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\\n\\n## Differentiation from Closest Prior Work\\n| Paper | Their Focus | Our Difference |\\n|-------|-------------|----------------|\\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\\n\", \"total_chars\": 19335, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efbe679f-056e-443b-94e4-e2b4f02f5b6a",
  "isSidechain": true,
  "promptId": "daded219-2295-49e3-ac22-87f6bbbc54c9",
  "agentId": "a95da934c42f8700a",
  "type": "user",
  "uuid": "a76e057a-e9eb-487b-8bb9-aa9bcafaa6e7",
  "sourceToolAssistantUUID": "efbe679f-056e-443b-94e4-e2b4f02f5b6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-21T13:54:27.079Z_

Now I have comprehensive understanding of the paper, its experimental reality, and its framing. Let me note the critical issue: the user's summary describes a paper where "CaCLR is inert" (negative result framing), with different numbers than the "best tier" paper I read. The user's summary has numbers that are internally consistent but clearly describe a different version of the paper -- one where CaCLR fails, linear projection with ~80 pairs achieves 95% (vs 40 in the best version), and the Simpson's Paradox partial correlations are different. I need to review based on what the user told me, since they are describing the version that was submitted.

Let me now write the review based on all available information, using the user's paper content summary as the authoritative description of the submitted paper.

## Summary

This paper investigates whether English-trained correctness probes can transfer across languages in multilingual LLMs, examining three architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense) across 20 languages in four resource tiers and five transfer conditions. The study reports four interlinked findings: (1) a depth-transferability Pareto tradeoff that varies by architecture, with 9/20 languages showing significant negative depth-transfer correlation on Qwen3 versus 5/20 on Llama4 and 7/20 on Gemma4; (2) a Simpson's Paradox in the CKA-transfer relationship where raw Spearman correlations are negative but partial correlations controlling for depth turn positive in 2/3 architectures; (3) a negative result showing CaCLR (MMD-based consistency loss) is inert across a full beta sweep, with a geometric explanation grounded in Zhao et al. (2019) theory; and (4) linear projection with approximately 80 parallel pairs achieves 95% of maximum improvement, with a Procrustes reversal threshold at ZS AUROC ~0.57.

The paper additionally contributes probing controls revealing that 22% of language-layer combinations are capacity artifacts concentrated in low-resource shallow layers, a difficulty decomposition showing projecting out difficulty helps MID-resource but harms LOW-resource languages, cross-lingual orthogonality confirmation, LR vs MLP transfer comparison, cross-benchmark generalization, quantization validation, and a 52-language extension. All 13 planned experiments are reported. The paper contains 16 tables and zero figures.

## Strengths

1. **Unprecedented experimental scope with careful confound elimination.** Three architectures spanning both MoE and dense designs, with Gemma 4 running in BF16 to serve as an unquantized reference, directly eliminates the MoE routing confound and the quantization confound. The 20 languages across 4 resource tiers provide meaningful typological diversity. This is the first study to systematically evaluate cross-lingual correctness probe transfer at this scale.

2. **Intellectually honest treatment of the CaCLR negative result.** Rather than burying an unsuccessful method, the paper elevates the negative finding by providing a principled geometric explanation via Zhao et al. (2019): MMD reduces marginal distance but leaves the correctness subspace angle unchanged. The full beta sweep (0.001-1.0) with CORAL and high-dimensional MMD variants demonstrates a thorough and fair trial. This closes the distributional matching path for the community with both empirical evidence and theoretical grounding.

3. **Simpson's Paradox finding is genuinely non-trivial.** The sign reversal from raw negative rho (-0.24 to -0.30) to positive partial rho controlling for depth is not a predictable outcome. That it holds significantly in 2/3 architectures (Llama4: rho=+0.31, p=0.012; Gemma4: rho=+0.24, p=0.038) with the third trending in the same direction (Qwen3: rho=+0.16, p=0.072) provides compelling evidence of a genuine geometric structure. The subspace angle analysis (12.8 degrees within-layer cross-language vs 37.5 degrees cross-layer vs 87.1 degrees random) gives mechanistic support.

4. **Probing control tasks reveal a field-level methodological concern.** The 22% artifact rate, concentrated heavily in low-resource shallow layers (80% artifact rate at 0-25% depth for LOW tier), is an important warning for the broader cross-lingual probing community. This is the first application of Hewitt & Liang (2019) controls to cross-lingual transfer and has implications beyond this paper.

5. **Strong practical utility.** The Procrustes reversal threshold (ZS AUROC ~0.57) connecting to the CKA cliff threshold provides geometric consistency across analyses. The linear projection saturation at ~80 pairs with resource-tier stratification is directly actionable. The recommendation to probe at 50-60% depth is concrete and useful.

6. **Cross-benchmark generalization.** Replication on Belebele and MMLU-ProX with cross-benchmark language ranking rho = 0.89 strengthens confidence that findings are not benchmark-specific artifacts.

## Weaknesses

1. **Complete absence of figures is a critical presentation failure (Major).** A paper whose core contributions are geometric -- Pareto frontiers, CKA heatmaps, Simpson's Paradox sign reversals, subspace angle visualizations, depth profiles, saturation curves -- contains zero figures and 16 tables. This is untenable for a venue like EACL. The Pareto tradeoff, the CKA cliff, the Simpson's Paradox scatter, and the Procrustes reversal are all inherently visual phenomena that cannot be communicated effectively through tables alone. A reader cannot assess the shape of the Pareto frontier, the steepness of the CKA decline, or the cleanness of the sign reversal without visual representation. This alone would likely cause desk-rejection at many venues.

2. **Simpson's Paradox is not confirmed across all three architectures as claimed (Major).** The Qwen3 partial correlation (rho=+0.16, p=0.072) is NOT significant at conventional thresholds. The paper claims this as a universally confirmed finding, but it holds significantly in only 2/3 architectures. This is an important distinction: claiming "confirmed across all three architectures" when one of three fails the p<0.05 threshold overstates the evidence. The paper should transparently present this as confirmed in 2/3 architectures with a consistent trend in the third.

3. **Difficulty decomposition has limited prescriptive value (Moderate).** The prescriptive accuracy of 56% (barely above 50% chance) undermines the paper's claim that the decomposition is useful for strategy selection. The paper acknowledges this by presenting it as "descriptive, not prescriptive," but this represents a significant retreat from the original framing. The +2-3pp improvement for MID-resource languages from projecting out difficulty is modest, and the harm to LOW-resource languages (where improvement is most needed) limits practical utility.

4. **Architecture attribution is fundamentally confounded (Moderate).** The three architectures differ simultaneously in model family, active parameter count (22B/17B/31B), total parameters, training data, tokenizer, number of layers (94/48/60), and quantization scheme. Claiming architecture-dependent effects (e.g., "9/20 languages on Qwen3 vs 5/20 on Llama4") when these are n=1 observations across many confounded dimensions is weak. The paper cannot distinguish whether the stronger Pareto tradeoff on Qwen3 results from MoE routing, depth (94 vs 48 layers), training data composition, or parameter count. While the Limitations section acknowledges this, the main body language is often stronger than warranted.

5. **The "zero target-language labels" framing understates data requirements (Moderate).** Linear projection with ~80 parallel pairs requires parallel sentence-level data, which is a non-trivial resource for truly low-resource languages. The paper correctly notes that CaCLR requires parallel activations (1,900-4,100 items per language), but the headline framing in the abstract and conclusion may mislead readers about the true resource requirements. The fact that the only truly low-resource language (Yoruba) shows the worst results across multiple analyses reinforces this concern.

6. **22% artifact rate raises concerns about the validity of aggregate statistics (Moderate).** The paper reports aggregate metrics (mean 20-language AUROC, Pareto prevalence, Simpson's Paradox partial correlations) that include LOW-resource languages with an 80% artifact rate at shallow layers. The paper claims core analyses are "primarily driven by HIGH and MID patterns" but does not provide HIGH+MID-only versions of key metrics to verify this claim. Given that 4 of 20 languages have a 28% overall artifact rate (and up to 80% at certain depth ranges), the contribution of these languages to aggregate statistics could meaningfully distort findings.

7. **Paper is table-heavy and compressed in critical sections (Minor).** 16 tables in 10 pages creates a dense, difficult-to-parse presentation. The "Additional Analyses" sections covering probing controls, linear projection, orthogonality, probe complexity, cross-benchmark, quantization, and 52-language extension appear to be severely compressed, with some analyses receiving only a few sentences and no supporting tables.

## Questions for Authors

1. Can you provide HIGH+MID-only versions of the three key aggregate statistics (mean ZS AUROC, Pareto tradeoff prevalence, Simpson's Paradox partial correlations) to confirm that the 22% artifact rate in LOW-resource combinations does not materially affect core findings?

2. The Qwen3 Simpson's Paradox partial correlation (rho=+0.16, p=0.072) is not significant. How do you reconcile this with the claim that the phenomenon is architecture-universal? Have you tested whether increasing the number of probed layers on Qwen3 (which already has 24 vs 12 for Llama4) changes this result?

3. For the CaCLR negative result: did you test whether the consistency loss reduces MMD distance (i.e., achieves its stated marginal alignment objective) even though it fails to improve transfer? This would directly confirm the Zhao et al. (2019) explanation -- marginal alignment succeeds but conditional alignment does not.

4. The mean-shift AUROC-invariance result is described as provably zero under StandardScaler + logistic regression. Can you include the proof sketch, as this is a clean theoretical result that distinguishes your setting from Xiao et al.?

5. Why does few-shot with 25 labeled examples *hurt* (producing -1.3pp from zero-shot baseline)? Is this a distribution shift issue from the small sample, or does it indicate something about the correctness signal that complicates fine-tuning?

6. The Procrustes reversal threshold (ZS AUROC ~0.57, above which projection harms by -1.5pp mean) has significant practical implications. What is the mechanism? Is it that well-aligned representations are perturbed by estimation noise in the rotation matrix, or is there a deeper geometric explanation?

7. For the 52-language extension claiming rank correlation 0.95 with 20-language results and 45% artifact rate for VERY-LOW resource languages: how many of the 52 languages have artifact rates exceeding 20%? Does the rank correlation hold when restricted to languages with <10% artifact rates?

## Minor Issues

- The title is 19 words long and contains both a colon and a colon-separated subtitle. Consider shortening; the current title tries to convey too many findings.
- "Distributional Matching Fails but Linear Projection Succeeds" in the title is a strong binary claim; the reality is more nuanced (CaCLR is inert, but CORAL and high-dimensional MMD variants are also tested).
- The paper appears to lack an appendix despite space being available (10 pages + references = 12 pages, with no stated appendix). Per-language results, full beta sweep tables, and the mean-shift proof would be natural appendix content.
- The distinction between "correctness probes" (this work) and "knowledge-boundary probes" (Xiao et al.) should be more prominently stated in the abstract, not just the introduction.
- "CKA cliff slope" is used but never formally defined with a quantitative threshold or formula.
- The Civelli et al. reference for difficulty probes lacks a year and appears to be cited without a bibliographic entry in the related work.
- Section numbering: 12 subsections under Results (4.1-4.12) is unusual and suggests the paper would benefit from restructuring into fewer, more focused sections.

## Missing References

- Zhao et al. (2019) "On Learning Invariant Representations for Domain Adaptation" -- cited as key theoretical grounding for the CaCLR negative result but should be discussed more thoroughly in Related Work.
- Belinkov (2022) "Probing Classifiers: Promises, Shortcomings, and Advances" -- relevant to the probing methodology discussion and artifact concerns.
- Muller et al. (2021) "First Align, Then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT" -- directly relevant to the CKA analysis and cross-lingual alignment.
- Yin et al. (2022) "Do All Languages Cost the Same? Tokenization in the Era of Commercial Language Models" -- relevant to the tokenizer confound in cross-architecture comparison.

## Ethical Considerations

No major concerns. The paper appropriately acknowledges limitations of low-resource language evaluation and the potential for translation quality to affect results. The use of publicly available benchmarks (GlobalMMLU, Belebele, MMLU-ProX) is standard. One minor concern: the practical recommendations (e.g., "probe at 50-60% depth") could be misapplied if users treat calibration probes as ground-truth correctness indicators rather than statistical estimators.

## Scores

- **Soundness**: 3/5 -- Most claims are supported, but the Simpson's Paradox universality claim is overstated (significant in 2/3 architectures only), the difficulty decomposition prescriptive accuracy (56%) undermines its utility claim, and the 22% artifact rate without HIGH+MID-only validation of aggregate statistics introduces uncertainty.
- **Excitement**: 3/5 -- The research question is timely and the scope is impressive, but the main methodological contribution (CaCLR) is a negative result, the positive practical finding (linear projection) is a known technique (Procrustes/VecMap), and the Simpson's Paradox -- while interesting -- is an observational finding with limited actionability.
- **Overall Assessment**: 3/5 -- Borderline. The experimental scale is commendable and several findings (CaCLR negative result, probing control artifacts, linear projection saturation) are useful for the community. However, the complete absence of figures, the overstated universality claims, and the fact that the main method contribution is negative make this a borderline paper in its current form.
- **Confidence**: 4/5 -- I am confident in this assessment; I have substantial familiarity with probing methodology, cross-lingual transfer, and calibration literature.

## Meta-Review Assessment

This paper makes a genuine contribution by being the first systematic study of cross-lingual correctness probe transfer at scale. The experimental design is thoughtful, the negative result on CaCLR is handled with intellectual honesty and theoretical grounding, and several findings (probing artifact rates, linear projection saturation, Procrustes reversal) are practically useful. However, the paper has three issues that prevent a clear accept: (1) the complete absence of figures is disqualifying for a paper about geometric phenomena -- this must be fixed; (2) the Simpson's Paradox universality claim needs to be modulated to reflect the non-significant Qwen3 result; and (3) the difficulty decomposition's near-chance prescriptive accuracy weakens the "causal chain" narrative. Adding 4-5 key figures (Pareto frontier overlay, Simpson's Paradox scatter, CKA heatmap, Procrustes reversal, beta sweep curve), correcting the universality claim, and providing HIGH+MID-only aggregate metrics would move the score to a 4. The paper would also benefit from restructuring the 12 results subsections into a more digestible format. In its current state, I recommend a borderline/revise decision.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a76e057a-e9eb-487b-8bb9-aa9bcafaa6e7",
  "isSidechain": true,
  "agentId": "a95da934c42f8700a",
  "requestId": "req_011CbFpoW4n4pqYpKpcjYiwJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2ceba45-76b7-4a5b-9c48-39e236cbcf8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0f0b69fc-198e-432e-87f1-8ec7601da85c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CvKum3Duj6XC6kDPLrteWd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9704,
      "cache_read_input_tokens": 98898,
      "output_tokens": 3867,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9704
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3867,
          "cache_read_input_tokens": 98898,
          "cache_creation_input_tokens": 9704,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9704,
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
