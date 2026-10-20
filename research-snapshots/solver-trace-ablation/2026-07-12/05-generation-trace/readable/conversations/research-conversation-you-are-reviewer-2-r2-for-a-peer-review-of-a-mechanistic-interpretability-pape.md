# Research conversation: You are Reviewer 2 (R2) for a peer review of a mechanistic interpretability paper submitted to EMNLP 2026 Findings. Your

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a2e2c736423f4c4fe.jsonl`
- **Structured JSON:** [`0e16e047d58fba7e889b.json`](../../sessions/0e/0e16e047d58fba7e889b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

53 recorded events

### User

_source line 1 · 2026-05-13T10:04:58.300Z_

You are Reviewer 2 (R2) for a peer review of a mechanistic interpretability paper submitted to EMNLP 2026 Findings. Your focus area is **Novelty and Related Work**.

## Scoring Rubric (ARR / EMNLP 2026)

**Overall Assessment (1-5, half-point increments):**
- 5 = Consider for Award (top 2.5%)
- 4 = Conference (main track worthy)
- 3.5 = Borderline Conference
- 3 = Findings
- 2.5 = Borderline Findings
- 2 = Resubmit next cycle
- 1 = Do not resubmit

**Soundness (1-5):**
- 5 = Excellent
- 4 = Strong
- 3 = Acceptable
- 2 = Poor
- 1 = Major issues

**Excitement (1-5):**
- 5 = Highly exciting
- 4 = Exciting
- 3 = Interesting but not exciting
- 2 = Marginally interesting
- 1 = Not interesting

**Confidence (1-5):**
- 5 = Positive
- 4 = Quite sure
- 3 = Pretty sure
- 2 = Willing to defend
- 1 = Not my area

## Paper Summary

**Title:** "When Does Cross-Method Consensus Improve Circuit Discovery? A Systematic Analysis of Failure Modes"

The paper is 8 pages (7 main + 1 appendix). It tests whether binary consensus scoring (CSS) — intersecting the top-N edges from K=3 circuit discovery methods (EAP-IG, Edge Pruning, ACDC) — improves circuit faithfulness. Evaluated on 4 tasks (IOI, Arithmetic, SVA, Factual Recall) × GPT-2 Small, plus IOI on Qwen-0.5B = 5 configurations total.

**Main claims:**
1. CSS produces marginal advantage on only 1/5 configs (IOI/GPT-2), largely attributable to circuit size effects.
2. Three failure modes: (a) ACDC binarization pathology, (b) consensus redundancy under high agreement, (c) scoring granularity mismatch at scale.
3. Jaccard-based diagnostic predicts CSS utility (4/5 correct, but n=5, p=0.19).

**Related work cited:**
- Circuit discovery methods: ACDC (Conmy et al. 2023), EAP-IG (Syed et al. 2023), Edge Pruning (Bhaskar et al. 2024), IOI circuit (Wang et al. 2023)
- Consensus/ensemble: Mondorf et al. (2025) cross-method score averaging, PIE (Chen et al. 2026) pruning-based iterative ensembles, CIRCUS (Parekh et al. 2026) within-method threshold diversity
- Feature selection theory: Nogueira & Brown (2016) stability indices, Kuncheva & Whitaker (2003) diversity measures

**Framing:** The authors explicitly state their contribution is "not the consensus framework itself" but "the systematic empirical characterization of when and why it fails."

**Key methodological choices:**
- Binary intersection (not score averaging like Mondorf)
- K=3 with 2 gradient methods + 1 ablation method
- Zero ablation only (mean ablation comparison incomplete)
- top-100 binarization threshold (fixed N)

**Section structure:**
1. Introduction
2. Background and Related Work
3. Method: CSS
4. Experiments (4.1 IOI, 4.2 Factual Recall, 4.3 FM1: ACDC Binarization, 4.4 FM2: Redundancy, 4.5 FM3: Granularity, 4.6 Jaccard Diagnostic, 4.7 CIRCUS Comparison)
5. Discussion
6. Limitations
7. Conclusion

## Your Review Task

Write a detailed review focused on:

1. **Novelty Assessment:**
   - How novel is the idea of testing binary consensus for circuit discovery? Given that Mondorf et al. (2025) already explored cross-method averaging and CIRCUS (2026) explored within-method diversity, how much does this add?
   - Are the failure modes genuinely new insights, or are they predictable from existing ensemble theory (Kuncheva & Whitaker 2003)?
   - Is the Jaccard diagnostic a meaningful contribution, given n=5 and p=0.19?
   - The authors position this as a "negative result" paper — is the negative result surprising enough to warrant publication?

2. **Related Work Completeness:**
   - Are there missing related works in circuit discovery methods? (e.g., circuit discovery methods beyond the three studied, attribution methods, subnetwork pruning literature)
   - Is the ensemble/consensus literature adequately covered? (feature selection stability, classifier ensemble diversity, bagging/boosting analogies)
   - Are there other "negative result" papers in mechanistic interpretability that should be cited?
   - How does this relate to the broader debate about method comparison in interpretability?

3. **Positioning and Framing:**
   - Is the "primarily negative" framing honest and well-calibrated?
   - Do the practitioner guidelines (Section 5) add genuine value, or are they obvious recommendations?
   - Is the failure mode taxonomy (3 modes) well-structured and complete? Could there be additional failure modes not captured?
   - How well does the paper connect its findings to ensemble theory conditions?

4. **Scope and Generalizability:**
   - Only 3 methods tested. How generalizable are the findings to other method combinations?
   - Only GPT-2 Small (and briefly Qwen-0.5B). How do findings generalize to larger models?
   - The negative result is about binary consensus specifically — should the paper discuss why continuous methods (Mondorf) might differ?
   - IFR is mentioned for Qwen but not formally introduced in §2 — is this a gap?

5. **Writing Quality:**
   - Is the paper well-organized and clearly written?
   - Are the claims appropriately hedged?
   - Is the abstract accurately representative of the paper's content?

**Output your review in this exact format:**

```
## R2 Review: Novelty and Related Work

### Summary
[2-3 sentences summarizing the paper's contribution from your perspective]

### Strengths
[Numbered list, 3-5 items]

### Weaknesses
[Numbered list, 3-5 items, each with specific evidence/reasoning]

### Questions for Authors
[Numbered list, 2-3 critical questions]

### Missing Related Work / Positioning Issues
[Specific papers or areas that should be discussed]

### Scores
- Soundness: X/5
- Excitement: X/5
- Overall: X/5
- Confidence: X/5

### Justification
[2-3 sentences explaining your overall score]
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "9a498837-1c99-486a-84f7-b638426fef15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T10:04:58.304Z_

```json
{
  "parentUuid": "9a498837-1c99-486a-84f7-b638426fef15",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
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
  "uuid": "e51d28e0-f97a-482f-a377-c5c739b58a97",
  "timestamp": "2026-05-13T10:04:58.304Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T10:05:01.404Z_



I'll start by reading the paper and related project files to understand the full context before writing the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e51d28e0-f97a-482f-a377-c5c739b58a97",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazNxjEiBXX6jBWVChGXs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71c44cf8-9a67-4275-bcfb-c4a398f3e516",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H77fJVCVZTMyUctGLPYXAb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7509,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7509,
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

_source line 4 · 2026-05-13T10:05:02.040Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ln5Vm3hEuHfWBB8r1c5eRK`</summary>

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
  "parentUuid": "71c44cf8-9a67-4275-bcfb-c4a398f3e516",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazNxjEiBXX6jBWVChGXs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6bb03e37-aab6-4755-839d-8d479c94e45b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H77fJVCVZTMyUctGLPYXAb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7509,
      "cache_read_input_tokens": 8249,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7509
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 127,
          "cache_read_input_tokens": 8249,
          "cache_creation_input_tokens": 7509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7509,
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

_source line 5 · 2026-05-13T10:05:02.044Z_

<details><summary>↩ Tool result · `toolu_01Ln5Vm3hEuHfWBB8r1c5eRK`</summary>

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
  "parentUuid": "6bb03e37-aab6-4755-839d-8d479c94e45b",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "5e263588-87e7-4791-856d-05eda7e4e170",
  "sourceToolAssistantUUID": "6bb03e37-aab6-4755-839d-8d479c94e45b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-13T10:05:05.115Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01JgyR8L6xqRZHpiBsw96NZD`</summary>

```json
{
  "project": "structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e263588-87e7-4791-856d-05eda7e4e170",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazNy1SXnQR8gkMY1Y5ge",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d55b56fc-d1e7-4708-8f8a-e8f5ac9b8cc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UU5XpspuxqZWzTCNDev8mB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 15758,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 7 · 2026-05-13T10:05:05.164Z_

<details><summary>↩ Tool result · `toolu_01JgyR8L6xqRZHpiBsw96NZD`</summary>

```text
{"result":"# 项目 structfuse-context 概况\n\n## 实验状态 (11 个)\n\n- **gpt2_factual_recall_k3_v2**: RUNNING (negative) — \n- **ioi_size_controlled_baseline**: PREPARING — \n- **gpt2_factual_recall_k3**: DONE (failed) — \n- **mvp_sva_gpt2_k3_topk**: DONE (negative) — \n- **phase2_qwen05b_ioi_acdc_k3**: DONE (negative) — \n- **mvp_sva_gpt2_k3**: DONE (negative) — \n- **phase2_qwen05b_ioi_k3**: DONE (negative) — \n- **mvp_arithmetic_gpt2_k3**: DONE (negative) — \n- **mvp_pilot_gpt2_ioi_v3**: DONE (success) — \n- **mvp_pilot_gpt2_ioi_v2**: DONE (failed) — \n- **mvp_pilot_gpt2_ioi**: DEPLOYED (killed) — \n\n## 最新报告\n# Handover — 2026-05-13\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| gpt2_factual_recall_k3_v2 | — | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **gpt2_factual_recall_k3** (failed): Factual Recall (国家首都) 上 CSS=1.0 faithfulness > single-method，GPT-2 第四任务验证（D025 条件④, plan_005）\n- **mvp_sva_gpt2_k3_topk** (negative): SVA 上 CSS=1.0 faithfulness > single-method（ACDC top-100 修正版，westd-pro6000 cuda:1）\n  [sva_css067_fix_results](/api/workspace-files/projects/structfuse-context/artifacts/mvp_sva_gpt2_k3_topk/data/sva_css067_fix_results.txt)\n- **phase2_qwen05b_ioi_acdc_k3** (negative): —\n\n## 趋势\n成功 1 / 负向 5 / 失败 2 / 共 8\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-39279: 无 GPU 信息\nwestd-pro6000: 空闲 cuda:0, cuda:1\n\n## 告警\n- mvp_pilot_gpt2_ioi_v2: 训练失败 — unknown\n- gpt2_factual_recall_k3: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d55b56fc-d1e7-4708-8f8a-e8f5ac9b8cc5",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "d41b92f8-19f3-4608-93a3-099907de350d",
  "sourceToolAssistantUUID": "d55b56fc-d1e7-4708-8f8a-e8f5ac9b8cc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-13T10:05:05.788Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Cw4no8B3qupF3YCwqJLFGZ`</summary>

```json
{
  "project": "structfuse-context",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d41b92f8-19f3-4608-93a3-099907de350d",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazNy1SXnQR8gkMY1Y5ge",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0829d849-cf78-463c-a71e-81e0d6ef3892",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UU5XpspuxqZWzTCNDev8mB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 15758,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 9 · 2026-05-13T10:05:05.802Z_

<details><summary>↩ Tool result · `toolu_01Cw4no8B3qupF3YCwqJLFGZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/report.md\", \"content\": \"# Handover — 2026-05-13\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| gpt2_factual_recall_k3_v2 | — | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **gpt2_factual_recall_k3** (failed): Factual Recall (国家首都) 上 CSS=1.0 faithfulness > single-method，GPT-2 第四任务验证（D025 条件④, plan_005）\\n- **mvp_sva_gpt2_k3_topk** (negative): SVA 上 CSS=1.0 faithfulness > single-method（ACDC top-100 修正版，westd-pro6000 cuda:1）\\n  [sva_css067_fix_results](/api/workspace-files/projects/structfuse-context/artifacts/mvp_sva_gpt2_k3_topk/data/sva_css067_fix_results.txt)\\n- **phase2_qwen05b_ioi_acdc_k3** (negative): —\\n\\n## 趋势\\n成功 1 / 负向 5 / 失败 2 / 共 8\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-39279: 无 GPU 信息\\nwestd-pro6000: 空闲 cuda:0, cuda:1\\n\\n## 告警\\n- mvp_pilot_gpt2_ioi_v2: 训练失败 — unknown\\n- gpt2_factual_recall_k3: 训练失败 — unknown\\n\", \"total_chars\": 870, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0829d849-cf78-463c-a71e-81e0d6ef3892",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "2c9c7c73-b5af-44ff-89e8-334e6d4ffd1e",
  "sourceToolAssistantUUID": "0829d849-cf78-463c-a71e-81e0d6ef3892",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-13T10:05:08.638Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Gx99BWrzwGCyQGaWf7S5M5`</summary>

```json
{
  "project": "structfuse-context",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c9c7c73-b5af-44ff-89e8-334e6d4ffd1e",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazNyHi5bQHGiyqjG473h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6fc97341-b9c8-4ef3-a819-77baa33da830",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YqBso3WFuBtwv3YBaH5e7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1702,
      "cache_read_input_tokens": 17207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1702,
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

_source line 11 · 2026-05-13T10:05:08.646Z_

<details><summary>↩ Tool result · `toolu_01Gx99BWrzwGCyQGaWf7S5M5`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fc97341-b9c8-4ef3-a819-77baa33da830",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "357c2705-6d2d-47d7-ac25-a9ea83fc795d",
  "sourceToolAssistantUUID": "6fc97341-b9c8-4ef3-a819-77baa33da830",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-13T10:05:09.609Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HUoA7xCYcFctqYiNvjhPKD`</summary>

```json
{
  "project": "structfuse-context",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "357c2705-6d2d-47d7-ac25-a9ea83fc795d",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazNyHi5bQHGiyqjG473h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a171e112-b403-409f-b046-f6440e44740d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YqBso3WFuBtwv3YBaH5e7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1702,
      "cache_read_input_tokens": 17207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1702,
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

_source line 13 · 2026-05-13T10:05:09.623Z_

<details><summary>↩ Tool result · `toolu_01HUoA7xCYcFctqYiNvjhPKD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/memory.md\", \"content\": \"# Memory — structfuse-context\\n\\n## GPU 越界教训 (2026-05-13)\\n\\n第三次 GPU 越界事件：PID 897752 占用 cuda:0（属于 rl-active-probe-fl），导致对方数据丢失。根因：旧进程或直接运行库模块时未设 CUDA_VISIBLE_DEVICES，torch 默认使用 cuda:0。\\n\\n**硬规则**：\\n- 项目只有 cuda:5@cqa1-21977，所有 .py 文件（含库模块）必须在 import torch 前用 `os.environ.setdefault(\\\"CUDA_VISIBLE_DEVICES\\\", \\\"5\\\")` 防护\\n- 入口脚本用 `os.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = \\\"5\\\"`（强制覆盖），库模块用 `setdefault`（不覆盖入口已设的值）\\n- Worker 提交实验必须用 submit_training_job（自动管理 CUDA_VISIBLE_DEVICES），禁止 nohup\\n\\n## ACDC isinf 退化——核心方法论问题 (2026-05-13)\\n\\nACDC binarization 用 `isinf` 只选出极少边（IOI 14, Arithmetic 17），但 ACDC 实际有 0.03-0.09 四级中间分数。isinf 导致 CSS=1.0 与 ACDC 完全重合，跨方法共识退化。top-k binarization（k=50-75）解决此问题：Arithmetic CSS 3/3 从 17→44-54。\\n\\n**但 top-k 未翻转条件④**：CSS=1.0 mean CPR=0.919 < EAP-IG=0.985。\\n\\n## D021: CSS-only 叙事 (2026-05-13)\\n\\n放弃 CIRCUS 作为独立 claim。转 CSS-only 叙事。\\n\\n## 竞争定位：CSS vs CIRCUS (2026-05-13)\\n\\n- **CIRCUS (Parekh, 2026)** 最大竞争对手。CSS 差异化 = method diversity > threshold diversity\\n- **Mondorf et al.** direct competitor：仅 gradient 族、score averaging（非 binary consensus）\\n- 关键支撑：Miller et al. (COLM 2024) faithfulness 对消融敏感；Méloux et al. EAP/EAP-IG 高方差\\n\\n## D026: MVP Gate 最终结论 (2026-05-13)\\n\\n**Arithmetic 条件④ FAIL（CSS=1.0 < EAP-IG），IOI PASS。**\\n\\n关键教训：\\n1. **Zero ablation 是 artifact 源**——所有小电路 zero CPR 为负，mean ablation 翻正到 0.9+\\n2. **节点级 ablation 的局限**——CSS=1.0 CPR 在 k=50→75 不变（节点集相同，边数变化无法区分）\\n3. **EAP-IG×EP 在 arithmetic 上 Jaccard=0.695**——两方法高度一致，CSS 缺少第三方视角的信息增益\\n4. **IOI 上 CSS 边效率极高**——14 edges CPR≈50 edges 单方法，每条边贡献远超单方法\\n5. **IOI CPR 不一致是误报**——mean_ablation_results.json 中标注为 IOI 的数据实际是 Arithmetic\\n\\n**等待 Director 决策：edge-efficiency claim / 原 claim + 更多任务 / pivot。**\\n\\n## IFR 作为第三方法——已证伪 (2026-05-13)\\n\\n**phase2_qwen05b_ioi_k3 (negative)**: Qwen-2.5 0.5B 上 IFR 与 EAP-IG/EP 的 Jaccard = 0.00。\\n\\n**D028 诊断结论**:\\n1. **Per-head 分解无效**: IFR 已经在用 per-head 分解，不是修复方向\\n2. **根本原因**: IFR (proximity) 度量 activation magnitude → 偏向高幅度 MLP 输出 (m2, m20, m22)；gradient 方法度量 causal influence → 偏向任务关键 attention heads (a20.h9)。两者解构的是不同维度\\n3. **Jaccard sweep**: 首次非零在 N=500 (J=0.045)，unique_score_rank 展开到 2191 边也仅 J=0.065\\n4. **Destination-side 退化 100%**: 同层头共享 residual stream，所有头得到相同 destination score\\n\\n**结论**: IFR 不能作为 CSS 第三方法用于大模型。gradient 族内部仍有共识（EAP-IG×EP Jaccard=0.54）。Phase 2 需要替代第三方法（ACDC top-k 或另一个 gradient 方法）。\\n\", \"total_chars\": 2263, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a171e112-b403-409f-b046-f6440e44740d",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "b5b15016-fe03-4e24-ab0c-838d3fab38ab",
  "sourceToolAssistantUUID": "a171e112-b403-409f-b046-f6440e44740d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-13T10:05:10.073Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KAsmM9sS5CPGm61zHmnTuC`</summary>

```json
{
  "project": "structfuse-context",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5b15016-fe03-4e24-ab0c-838d3fab38ab",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazNyHi5bQHGiyqjG473h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7a98648-9029-4e21-a07e-6d6622ddd29a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YqBso3WFuBtwv3YBaH5e7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1702,
      "cache_read_input_tokens": 17207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1702,
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

_source line 15 · 2026-05-13T10:05:10.091Z_

<details><summary>↩ Tool result · `toolu_01KAsmM9sS5CPGm61zHmnTuC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — structfuse-context\\n\\n> 最后更新: 2026-05-13 | 更新原因: D034 后 reframe 为分析论文（Route A）\\n\\n## Target Venue\\nEMNLP 2026 Findings (ARR deadline 2026-05-25)\\n\\n## Core Insight\\nCross-method binary consensus in circuit discovery fails more often than it succeeds. Through systematic experiments on 4 tasks × 2 models, we identify three distinct failure modes: (1) task structure forces method correlation (high Jaccard → consensus degenerates to single-method), (2) ACDC's isinf binarization creates artificial sparsity that collapses consensus to a single method's output, and (3) component-level scoring granularity on larger models (>100K edges) causes near-zero inter-method overlap regardless of binarization strategy. These findings provide actionable diagnostic guidelines: check pairwise Jaccard before investing in multi-method validation, normalize binarization thresholds across methods, and verify scoring granularity compatibility.\\n\\n## Narrative Arc\\n1. Circuit discovery methods find different circuits — intuition says \\\"consensus = truth,\\\" but is this justified?\\n2. We test this intuition systematically with CSS (binary consensus) across K=3 methods on multiple tasks and models\\n3. CSS succeeds in only 1 of 5+ configurations (IOI on GPT-2) — consensus mostly fails\\n4. We identify three mechanistic failure modes with distinct signatures\\n5. Negative results + failure mode taxonomy = actionable practitioner guidelines\\n\\n## Core Claims\\n\\n### Claim 1: ACDC isinf binarization pathology (METHODOLOGICAL — strongest)\\n- **Evidence**: CSS=1.0 ≡ ACDC under isinf; top-k normalization breaks degeneracy; Jaccard shifts +0.16 to +0.25 across tasks\\n- **Status**: Fully demonstrated on IOI + Arithmetic + SVA (3 tasks)\\n- **Strength**: ★★★★★ — concrete, reproducible, actionable\\n\\n### Claim 2: CSS fails on majority of task×model configurations (EMPIRICAL)\\n- **Evidence**: 1/6 configurations show CSS=1.0 CPR advantage; failures span task-dependent (Arithmetic J=0.70, Factual Recall J=0.82), marginal (SVA Δ<0.01), and model-scaling (Qwen×2 zero overlap)\\n- **Status**: IOI PASS, Arithmetic FAIL, SVA inconclusive (D033), Factual Recall FAIL (EAP-IG×EP J=0.82 — gradient methods nearly identical, K≈2), Qwen IFR FAIL, Qwen ACDC FAIL\\n- **Strength**: ★★★★ — honest negative finding with systematic coverage; Factual Recall adds \\\"vote stuffing\\\" failure mode (gradient pair dominates consensus)\\n\\n### Claim 3: Component-level scoring causes scaling failure (MECHANISTIC)\\n- **Evidence**: On Qwen-0.5B (179K edges), both IFR and ACDC degenerate to node-level scoring; top-0.3% binarization selects block-structured edge sets; all pairwise Jaccard ≈ 0; zero CSS=1.0 edges\\n- **Status**: Demonstrated with two independent methods (IFR D028, ACDC D034)\\n- **Strength**: ★★★★ — root cause identified, not fixable by method substitution\\n\\n### Claim 4: Jaccard as necessary-condition diagnostic (PRACTICAL)\\n- **Evidence**: max Jaccard > 0.5 → CSS never helps (4/4 cases: Arithmetic J=0.70, Factual Recall J=0.82, SVA J=0.65, Qwen IOI J≈0); max Jaccard < 0.35 → CSS helps (1/1 case, IOI J=0.31); gradient-pair correlation (EAP-IG×EP) drives max Jaccard on 3/4 GPT-2 tasks\\n- **Status**: Directionally supported but n too small for statistical significance. Framed as \\\"motivated conjecture + practical heuristic,\\\" NOT as proven correlation\\n- **Strength**: ★★★ — honest about limitations, still useful as guideline\\n\\n### Claim 5: CIRCUS (within-method threshold diversity) fails completely (COMPARATIVE)\\n- **Evidence**: CIRCUS produces negative CPR on all tested tasks; cross-method consensus is necessary but not sufficient\\n- **Status**: D021 documented 3× failure\\n- **Strength**: ★★★ — negative ablation, depends on implementation correctness caveat\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1: \\\"This is just a negative result, what's the contribution?\\\"\\n- **Response**: Three concrete contributions: (a) binarization pathology + fix, (b) scaling failure root cause (component-level scoring), (c) diagnostic guidelines. Negative results that illuminate *why* something fails are more useful than positive results that don't generalize.\\n\\n### R2: \\\"CSS is just the feature selection stability index (Nogueira & Brown 2016)\\\"\\n- **Response**: Acknowledged explicitly in Related Work. Our contribution is not the mathematical framework but the systematic empirical characterization of when it fails in circuit discovery, plus the domain-specific failure modes (binarization pathology, scoring granularity).\\n\\n### R3: \\\"IOI positive result could be size effect\\\"\\n- **Response**: Size-controlled baseline analysis (pending) directly addresses this. If confirmed as artifact, strengthens the negative finding narrative.\\n\\n### R4: \\\"Only GPT-2 Small + Qwen 0.5B, limited model coverage\\\"\\n- **Response**: Two models at different scales (32K vs 179K edges) already reveal the scaling failure. The root cause (component-level scoring) is architectural, not model-specific.\\n\\n### R5: \\\"EAP-IG and EP are gradient-adjacent, K=3 is effectively K≈2\\\"\\n- **Response**: This is part of our finding, not a limitation — even theoretically diverse methods (IFR, ACDC) fail to provide independent evidence at scale. Method correlation is structural, not accidental.\\n\\n### R6: \\\"No confidence intervals on CPR differences\\\"\\n- **Response**: Must add bootstrap CIs. IOI advantage of +0.08 needs statistical validation.\\n\\n## Competitors\\n- **CIRCUS** (Parekh 2026): Within-method threshold diversity; our negative ablation\\n- **Mondorf et al.** (2510.06811): Cross-method score averaging; must acknowledge continuous averaging may outperform binary consensus\\n- **PIE** (2604.16889): Iterative pruning ensemble; single paradigm\\n- **Nogueira & Brown** (JMLR 2016): Feature selection stability; CSS is domain application, must cite\\n- **Kuncheva & Whitaker** (2003): Ensemble diversity theory; theoretical foundation for our failure mode analysis\\n\", \"total_chars\": 5875, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7a98648-9029-4e21-a07e-6d6622ddd29a",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "fc59d05b-bdfb-4504-9d5e-946004191c56",
  "sourceToolAssistantUUID": "a7a98648-9029-4e21-a07e-6d6622ddd29a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-13T10:05:10.566Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CJoLkbbKhkB6WWDkKyZFH5`</summary>

```json
{
  "project": "structfuse-context",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc59d05b-bdfb-4504-9d5e-946004191c56",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazNyHi5bQHGiyqjG473h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d715ee8e-8165-49c3-b01f-cc1eb71b2e97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YqBso3WFuBtwv3YBaH5e7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1702,
      "cache_read_input_tokens": 17207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1702,
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

_source line 17 · 2026-05-13T10:05:10.575Z_

<details><summary>↩ Tool result · `toolu_01CJoLkbbKhkB6WWDkKyZFH5`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d715ee8e-8165-49c3-b01f-cc1eb71b2e97",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "b5c1e3e5-279e-4f3a-924b-863169f8f757",
  "sourceToolAssistantUUID": "d715ee8e-8165-49c3-b01f-cc1eb71b2e97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-13T10:05:13.309Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WLKGqEtQCRvZU7qsEMfZCm`</summary>

```json
{
  "project": "structfuse-context",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5c1e3e5-279e-4f3a-924b-863169f8f757",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazNydvzu5VyDQtLaNLkj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2de4a145-7340-427b-97f7-f3048107d7b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7EH11c57YYJTL8ASvqBcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4042,
      "cache_read_input_tokens": 18909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4042,
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

_source line 19 · 2026-05-13T10:05:13.330Z_

<details><summary>↩ Tool result · `toolu_01WLKGqEtQCRvZU7qsEMfZCm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/ROADMAP.md\", \"content\": \"# structfuse-context — Research Dashboard\\n\\n> 最后更新: 2026-05-13 UTC | 更新原因: 更新当前进展与近期任务（IOI PASS_MAIN, Arithmetic 运行中）\\n\\n## 核心方向\\n跨方法二值共识（CSS）用于鲁棒电路编辑：证明 binary stability scoring + family-agreement constraint 在分布偏移下优于 score averaging 和单方法电路。\\n\\n## 当前进展\\n- **阶段**: MVP 验证 — IOI 已 PASS_MAIN（off-diagonal 13.3%），Arithmetic 确认实验运行中\\n- **核心假设**: CSS off-diagonal ≥5%（D021 CSS-only gate，D024 覆盖 D002）\\n- **基础设施**: cqa1-21977 (cuda:5, RTX 4090D) 已配置\\n- **大模型方案已定 (D006)**: IFR 作为第三方法，triangulation 框架定位\\n- **目标**: EMNLP 2026 Main（ARR deadline 2026-05-25，剩余 12 天）\\n\\n## 方法配置\\n| 模型 | K | 方法 | 算法族 |\\n|------|---|------|--------|\\n| GPT-2 Small | 3 | EAP-IG + Edge Pruning + ACDC | gradient / mask / greedy causal |\\n| Qwen-2.5 0.5B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |\\n| Gemma-2 2B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |\\n| Llama-3.1 8B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |\\n\\n论文需披露：GPT-2 Small CSS = 3 因果方法共识；大模型 CSS = 2 因果 + 1 相似度方法共识（triangulation）。\\n\\n## MVP Gate 规则（D001-D003）\\n| off-diagonal % | 决策 |\\n|---|---|\\n| ≥10% | → Main track |\\n| 5-10% | → Findings + 追加 Arithmetic 验证 |\\n| 2-5% | → Findings 确认 |\\n| <2% (两组) + ΔF 无差异 | → Kill |\\n\\n## 阶段规划\\n\\n### Phase 1: MVP pilot（当前）\\n- GPT-2 Small / IOI，K=3（3 因果族），~2h → off-diagonal 判定\\n\\n### Phase 2: K=3 checkpoint + 全量 CSS（MVP 后 ~3天）\\n- Qwen-2.5 0.5B / IOI K=3（含 IFR）快速检查\\n- 全 4 模型 × 4 任务 CSS 计算\\n- 确认 Edge Pruning 实现：princeton-nlp/edge-pruning（非 auto-circuit mask gradient）\\n\\n### Phase 3: OOD editing（~4天）\\n### Phase 4: 分析 + 写作（~3天，最迟 5月22日）\\n\\n## 近期任务\\n- [ ] 等待 mvp_arithmetic_gpt2_k3 完成 → gate 判定\\n- [ ] Gate PASS 后 complete_mvp → 进入 research\\n- [ ] 写 paper_framing.md + experiment_plan.yaml\\n- [ ] 部署 IFR + Phase 2 实验脚本到服务器\\n- [ ] 下载目标模型（Qwen-2.5 0.5B 优先）\\n\\n## GPU 预算\\n- 已分配: 1× RTX 4090D (cuda:5@cqa1-21977)\\n- MVP: ~2h | 全量: ~290h A100（需后续扩卡）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D035 | 2026-05-13 | D035: Reframe 为分析论文 Route A — \\\"When Does Cross-Met | mvp_pilot_gpt2_ioi_v3, phase2_qwen05b_ioi_acdc_k3, mvp_arithmetic_gpt2_k3 |\\n| D034 | 2026-05-13 | D034: Qwen ACDC 确认 CSS 跨模型 scaling 根本性失败——问题不在方法选择 | phase2_qwen05b_ioi_acdc_k3, phase2_qwen05b_ioi_k3, mvp_pilot_gpt2_ioi_v3 |\\n| D033 | 2026-05-13 | D033: SVA 判定降级为 inconclusive——单 seed Δ=0.013 不具鲁棒性 | mvp_sva_gpt2_k3_topk, mvp_sva_gpt2_k3 |\\n| D032 | 2026-05-13 | D032: 条件④评估指标修正——必须用 css_1.00 而非 css_0.67 | mvp_sva_gpt2_k3_topk, mvp_sva_gpt2_k3 |\\n| D031 | 2026-05-13 | 统一 D025 条件④标准：zero PASS 或 mean Δ≥0.01，SVA 两次均判 neg | mvp_sva_gpt2_k3, mvp_sva_gpt2_k3_topk |\\n| D030 | 2026-05-13 | SVA D025 gate FAIL（zero FAIL / mean 边际 Δ=0.008）；发现 | mvp_sva_gpt2_k3_topk |\\n| D029 | 2026-05-13 | Phase 2 第三方法：放弃 IFR，改用 ACDC top-k。IFR 跨族分歧作为 Discu | phase2_qwen05b_ioi_k3 |\\n| D028 | 2026-05-13 | Phase 2 IFR 零重叠问题：暂停 Qwen/Gemma 新实验，先修 IFR per-hea | phase2_qwen05b_ioi_k3 |\\n| D027 | 2026-05-13 | MVP 最终判定：CSS faithfulness 优势 task-dependent（IOI PA | mvp_arithmetic_gpt2_k3, mvp_pilot_gpt2_ioi_v3 |\\n| D026 | 2026-05-13 | Arithmetic D025 gate FAIL（条件④），暂不判 MVP 结果，先做 ACDC  | mvp_arithmetic_gpt2_k3 |\\n\\n\", \"total_chars\": 3059, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2de4a145-7340-427b-97f7-f3048107d7b3",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "650a0602-e36c-46dc-8be7-e9ccb88a78e0",
  "sourceToolAssistantUUID": "2de4a145-7340-427b-97f7-f3048107d7b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-13T10:05:13.899Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01He3XLagx7nGjfTbXSj265X`</summary>

```json
{
  "project": "structfuse-context",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "650a0602-e36c-46dc-8be7-e9ccb88a78e0",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazNydvzu5VyDQtLaNLkj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "466fd1ab-b5aa-4ab4-9306-190abd1b936b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7EH11c57YYJTL8ASvqBcV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4042,
      "cache_read_input_tokens": 18909,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4042
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 18909,
          "cache_creation_input_tokens": 4042,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4042,
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

_source line 21 · 2026-05-13T10:05:13.915Z_

<details><summary>↩ Tool result · `toolu_01He3XLagx7nGjfTbXSj265X`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/decisions.yaml\", \"content\": \"_next_id: 36\\ndecisions:\\n- id: D001\\n  date: 2026-05-12 09:57 UTC\\n  summary: MVP 定义为 pre-registered pilot：GPT-2 Small/IOI 上 K=4 方法 CSS + CIRCUS cross-tabulation\\n  rationale: 'IDEA_BRIEF 已定义 pilot 为第一个计算里程碑（~2h），直接检验核心假设\\\"方法类 artifact 可被二值共识检测\\\"。Pass\\n    criterion: ≥10% CIRCUS-core 边落入 off-diagonal cell。该 pilot 同时也是论文 Section 3 的 motivating\\n    result，失败则需 reframe 为 Findings track。选择此 MVP 因为：(1) 成本极低（~2h 单卡）(2) 直接验证核心假设 (3)\\n    结果直接决定投稿策略。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-12 09:59 UTC\\n  summary: 定义 MVP gate 灰区规则：5-10% off-diagonal → Findings + 追加第二组 task 验证\\n  rationale: 'Reviewer warning: 5%-10% 灰区无决策规则。决定：5-10% 默认走 Findings track，但在 GPT-2\\n    Small / Arithmetic 上追加验证。若第二组 ≥10% → 升级回 Main；若第二组也 5-10% → 确认 Findings；若第二组 <5%\\n    → 评估是否 IOI 特有现象。同时要求 MVP 报告包含 CIRCUS-core 绝对边数 + binomial 95% CI，若 CIRCUS-core\\n    <30 条边则必须追加第二组 task。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-12 09:59 UTC\\n  summary: 定义项目级 kill criteria：off-diagonal <2% + ΔF 无统计差异 → kill\\n  rationale: 'Reviewer warning: 缺项目级 kill criteria。决定：off-diagonal <2% across GPT-2\\n    Small 两个 task (IOI + Arithmetic) AND 四种电路 ΔF 无统计显著差异 (bootstrap p>0.05) → kill\\n    project。单一 task <2% 不触发 kill，需两组确认。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D004\\n  date: 2026-05-12 09:59 UTC\\n  summary: MVP 通过后增加 K=3 checkpoint：Qwen-2.5 0.5B / IOI 快速验证\\n  rationale: 'Reviewer warning: 3/4 模型用 K=3 + family constraint，但 pilot 仅测 K=4。决定：MVP\\n    通过后、全量实验前，增加 Qwen-2.5 0.5B / IOI 的 K=3 快速检查（EAP-IG + AtP* + Edge Pruning，~数小时）。若\\n    K=3 family constraint 下 off-diagonal 完全消失（<2%），需重新评估大模型贡献——可能论文仅限 K=4 结果或需要调整\\n    family constraint 定义。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D005\\n  date: 2026-05-12 10:08 UTC\\n  summary: AtP* 无 edge-level 实现：MVP 改为 K=3（EAP-IG+Edge Pruning+ACDC），大模型方案待评估\\n  rationale: 'Reviewer critical: AtP* 官方未开源，社区版仅 node-level。影响：(1) GPT-2 Small 原 K=4\\n    降为 K=3，但 EAP-IG+EP+ACDC 恰好覆盖 3 个算法族（gradient/mask/greedy causal），实际更干净；(2) 大模型原\\n    K=3 降为 K=2（仅 EAP-IG+EP），CSS 退化为平凡二值投票，严重削弱贡献。决策：MVP 用 K=3（3族）推进，同时评估大模型第三方法：(a)\\n    AtP* 自行实现可行性（≤1天）(b) PAHQ 加速 ACDC 到大模型的可行性 (c) MIB 其他 edge-level 方法的算法族分类。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D006\\n  date: 2026-05-12 10:28 UTC\\n  summary: 大模型 K=3 第三方法确定为 IFR，论文采用 triangulation 框架定位\\n  rationale: Agent 评估三条路径：(a) AtP* 自实现仍是 gradient 族，不解决 K=2 仅 2 族问题 (b) PAHQ 加速 ACDC\\n    不可行 (c) MIB 方法中 IFR 唯一满足\\\"非 gradient、非 mask optimization、edge-level、可扩展到 8B\\\"。Reviewer\\n    确认 IFR 为最佳选项，但指出 IFR 是非因果方法（度量激活空间 proximity 而非因果贡献）。采纳 Reviewer 建议：论文定位 IFR 为\\n    triangulation 中的\\\"independent signal\\\"而非\\\"causal validator\\\"——若一条边同时被因果方法 + 优化方法 +\\n    相似度方法识别，作为机制组件的证据更强。GPT-2 Small（3 因果方法）vs 大模型（2 因果 + 1 非因果）的 CSS 语义差异须在论文中诚实披露。\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-12 12:11 UTC\\n  summary: GPU 越界事故：kill 越界进程 + 修复 CUDA_VISIBLE_DEVICES + 重跑 MVP\\n  rationale: 'Reviewer critical: 项目进程跑到 cuda:0/cuda:1（白名单仅 cuda:5），L1 红线违规。原因推测为 Agent\\n    重启进程时未设 CUDA_VISIBLE_DEVICES=5。处置：立即 kill + 修复启动脚本加入 GPU 硬检查 + cuda:5 上重跑。ACDC\\n    71.5% 进度丢失。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D008\\n  date: 2026-05-12 13:02 UTC\\n  summary: MVP 结果解读协议：mask_gradient proxy 下 ≥10% 可信（保守估计），<10% 需 L0 EP 重测\\n  rationale: 当前 MVP 实际为 2 族（EAP-IG + mask_gradient 同属 gradient，+ ACDC greedy causal），非\\n    3 族。同族方法更易同意 → off-diagonal 偏低。因此：≥10% 是保守估计（真实跨族分歧可能更大），gate pass 可信；<10% 不直接判\\n    fail，需部署 L0 EP 到服务器重测 IOI 后再做 gate 判定。Phase 2 全量实验无论如何必须换 L0 EP。\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n  - D007\\n- id: D009\\n  date: 2026-05-12 17:01 UTC\\n  summary: 修复边名格式不匹配 critical bug：统一 EAP-IG 和 EP/ACDC 的边名归一化到同一 canonical form\\n  rationale: Reviewer 发现 _normalize_eap_edge 产出 dash 分隔符 + m0 格式，_normalize_ac_edge\\n    产出 arrow 分隔符 + mlp 0 格式，导致 css.py 字符串匹配完全失败，所有 CSS 值和 off_diagonal_pct 无效。修复方案：统一\\n    canonical form + 转换已有缓存，不重跑 discovery。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi\\n    role: affected\\n    result: CSS 结果因边名 bug 无效，需修复后重算\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-12 18:40 UTC\\n  summary: Phase 2 IFR binarization策略：用 percentile threshold 或 unique-score-rank 替代\\n    top-N，避免 layer-block voting 偏差\\n  rationale: Reviewer 审查发现 IFR run_ifr() 对同一 (src, dst_layer) 的所有 head×QKV 赋相同 proximity\\n    score（residual-stream proximity 固有局限），导致每对产生 36 条同分边。CSS binarize_scores 的 top-N\\n    模式下少数 (src,layer) 对即可 block-vote 占满配额，与 EAP-IG/EP 的 per-edge 粒度系统性不匹配，可能人为膨胀/压缩\\n    off-diagonal。不影响 MVP（MVP 不含 IFR），Phase 2 集成时需：(1) 改用 percentile threshold 或 unique-score-rank\\n    binarization (2) 论文披露 IFR layer-block 粒度 vs 其他方法 edge 粒度差异。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n- id: D011\\n  date: 2026-05-12 19:13 UTC\\n  summary: EP HF 后端需重构：从 layer pre-hook 改为 submodule-level hooks（q_proj/k_proj/v_proj/mlp\\n    各自 hook），修复 MLP mask 未应用 + Q/K/V 聚合两个问题\\n  rationale: Reviewer 发现 EP HF 实现有两个 warning：(1) MLP edge mask 参数参与 backward 但 forward\\n    无 hook 应用，MLP score 不可信；(2) 同一 (src, layer) 的所有 Q/K/V edge mask 被 mean 聚合为单标量，丢失\\n    per-edge 粒度。两个问题使 EP 退化为 layer-level masking。修复方案：将 hook 从 layer pre-hook 下沉到\\n    q_proj/k_proj/v_proj/mlp submodule level，每个 submodule 独立 hook 并应用对应 edge mask。这在\\n    HF hook 框架内可行，不需要重写 forward pass。若不修复，Phase 2 K=3 中 EP+IFR 都是 approximate，CSS\\n    edge-level 共识叙事被削弱。\\n  related_experiments: []\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-12 22:19 UTC\\n  summary: Reviewer 洞察：cross-tabulation（CIRCUS×CSS → 2×2 矩阵）应作为论文核心 novelty claim，而非仅\\n    CSS 填补 gap\\n  rationale: Reviewer 审查 related_work_notes.md 指出：CIRCUS（intra-method stability）×\\n    CSS（cross-method consensus）的系统组合产生 stable_core / method_specific 分类，这个 cross-tabulation\\n    在现有文献中无人做过。比单独宣称 CSS 新颖性更强。同时记录：(1) GPT-2 Small K=3 中 EAP-IG+EP 同为 gradient-adjacent\\n    需在论文中论证 optimization 差异；(2) 2025-2026 引用需 reference-audit 验证；(3) Phase D faithfulness\\n    评估必须证明 stable_core 优于 single-method circuit。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n  - D008\\n- id: D013\\n  date: 2026-05-12 22:24 UTC\\n  summary: CIRCUS 实现 bug：1D percentile sweep 产生嵌套电路，退化为 top-k。MVP v3 不中断（结果仍有信息量），Phase\\n    2 必须修复为 2D non-nested grid\\n  rationale: Reviewer 发现 circus.py 用 np.linspace percentiles 产生严格嵌套 C(t_low)⊇C(t_high)，违反\\n    CIRCUS 原文 non-nesting 约束。退化后 stability=1.0 core = top-9.1% 边（B=10），失去 config-bagging\\n    统计意义。MVP v3 cross-tabulation 仍测试 CSS vs score-ranking 一致性，gate 判定可用，故不中断。Phase\\n    2 须改为 2D grid（node threshold × edge threshold）或 random-subset 采样实现 non-nesting。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: affected\\n    result: running, results still informative despite CIRCUS degradation\\n  depends_on:\\n  - D012\\n- id: D014\\n  date: 2026-05-12 23:04 UTC\\n  summary: 论文 framing 校准：4-cell taxonomy 为核心 novelty，contribution statement 弱化避免全称量词，Phase\\n    D 增加 method_specific/cross_unstable 独立评估\\n  rationale: Reviewer 深度评估确认：(1) CIRCUS×CSS cross-tabulation 在文献中无先例，novelty 成立；(2)\\n    当前 statement 过强——\\\"any\\\" 全称量词和 \\\"distribution shift\\\" claim 缺实验支撑，需弱化；(3) 4-cell taxonomy\\n    是最强贡献点，但必须实证 4 个 cell 有不同 faithfulness 特性；(4) Phase D 需增加 method_specific 和 cross_unstable\\n    独立 CPR/CMD 评估；(5) OOD 评估（ioi_variant）应提至 priority 2；(6) D013 CIRCUS 修复已完成，Phase\\n    2 用修复版本。faithfulness 必须满足：CPR(stable_core) ≥ 0.8×CPR(best_single_method) 且 |stable_core|\\n    < |best_single_method| 且优于纯 CSS 和纯 CIRCUS。\\n  related_experiments: []\\n  depends_on:\\n  - D012\\n  - D013\\n- id: D015\\n  date: 2026-05-12 23:04 UTC\\n  summary: Framing 调整：claim 降级删除全称量词和 OOD claim；Phase D 必须增加 method_specific + cross_unstable\\n    独立 faithfulness 评估；MVP 后首检 4-cell cardinality\\n  rationale: Reviewer 两轮一致评估：(1) \\\"any single-method\\\" 全称量词超出 1 模型×1 任务实验覆盖；(2) \\\"distribution\\n    shift\\\" 无 OOD 数据支撑；(3) 4-cell taxonomy 是文献空白（novelty 成立），但需实证 4 个 cell 各有不同特性——当前\\n    Phase D 只评 stable_core，缺 method_specific/cross_unstable 独立评估；(4) D008 风险：gradient-adjacent\\n    方法可能压缩 method_specific cell。暂定 claim：\\\"competitive or superior faithfulness with\\n    fewer edges\\\"。OOD claim 推 Phase 2。\\n  related_experiments: []\\n  depends_on:\\n  - D012\\n  - D013\\n  - D008\\n- id: D016\\n  date: 2026-05-12 23:09 UTC\\n  summary: 更正：D013 CIRCUS config_bag nonnesting 修复未实际完成。Agent 产出为 Phase 2 前置代码（L0\\n    EP + IFR），远程 circus.py 零改动。另发现 L0 EP per-layer 粒度问题，Phase 2 前必须修复\\n  rationale: Reviewer 审查 worker 产出发现：(1) 远程 circus.py 仍为 1D percentile nesting，config_bag()\\n    未改动，Agent 报告的\\\"17 测试通过\\\"与实际不符；(2) 新增 edge_pruning_l0.py 的 mask 粒度为 (src, dst_layer)，所有\\n    head×QKV 共享同一值，与 EAP-IG per-edge 粒度不一致。Phase 2 三方法中两个（L0 EP + IFR）退化为 layer-level，CSS\\n    edge-level 共识叙事不成立。两项均为 Phase 2 启动前必修。\\n  related_experiments: []\\n  depends_on:\\n  - D013\\n  - D011\\n  - D010\\n- id: D017\\n  date: 2026-05-12 23:14 UTC\\n  summary: CRITICAL：CIRCUS-CSS 作用域不匹配导致 off-diagonal 结构性膨胀 ~98%，v3 cross-tabulation\\n    无效。需统一 edge universe 后重算\\n  rationale: Reviewer 发现 CIRCUS 在全量 32491 边上操作（core≈2953 条），CSS 在三方法二值化电路并集（~150 条）上操作，20\\n    倍作用域差距。CIRCUS-core 中不在二值化电路的边自动 CSS=0 → method_specific≈2893 条 → off-diagonal≈98%，为测量\\n    artifact。同时 EP binarization 用 score>0.5 对 mask_gradient 输出无意义（梯度分数非 [0,1]），导致\\n    EP 选边极少（~20-50 条）。修复方向：(1) 统一 edge universe 为三方法二值化电路并集，CIRCUS 只在此并集内操作；(2) EP\\n    改为 top-N 或 percentile binarization；(3) gate KILL 改为 KILL_CANDIDATE（D003 要求两 task）。v3\\n    原始 scores 可复用，无需重跑。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: invalidated_analysis\\n    result: raw data valid, cross-tabulation invalid due to scope mismatch\\n  depends_on:\\n  - D013\\n  - D016\\n  - D008\\n- id: D018\\n  date: 2026-05-13 01:26 UTC\\n  summary: MVP gate 条件性 PASS_MAIN：off-diagonal 13.3% ≥ 10%，但 CIRCUS-core=15 < 30 触发\\n    D002，需 Arithmetic task 确认\\n  rationale: K=3 corrected 分析（修复 ACDC binarization 后）：off-diagonal 2/15=13.3%，点估计过\\n    ≥10% 线 → PASS_MAIN。但 95% CI [1.7%, 40.5%] 横跨所有 gate 区间，统计功效不足。D002 明确规定 core <\\n    30 时必须追加第二 task 验证。同时 CSS ≥ 2/3 对已知 IOI 12-edge 电路 recall=1.0 是强正面信号，说明 cross-method\\n    consensus 确实能捕捉真实电路结构。Pairwise Jaccard（EAP-IG×ACDC=0.096, EP×ACDC=0.086）在文献典型范围内，证实方法间存在真实分歧。EAP-IG×EP=0.307\\n    偏高（gradient-adjacent），Phase 2 切 L0 EP 后预期改善。决策：暂定 PASS_MAIN，待 Arithmetic task\\n    确认后正式通过 MVP gate。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: primary\\n    result: off-diagonal 13.3%, CSS recall=1.0, conditional PASS\\n  depends_on:\\n  - D001\\n  - D002\\n  - D008\\n- id: D019\\n  date: 2026-05-13 01:32 UTC\\n  summary: 补充 gate criterion：Arithmetic 不仅看 off-diagonal %，还需验证 CSS faithfulness >\\n    single-method faithfulness 排序\\n  rationale: Reviewer 指出 CIRCUS-core 自身 CPR 为负（-0.108），说明 CIRCUS stability 与功能重要性不相关，off-diagonal\\n    % 作为唯一 gate 指标解释力不足。但 faithfulness 排序 CSS=3/3 (0.110) > CSS≥2/3 (0.063) > ACDC\\n    (0.029) > single-method (负值) 清晰支撑核心论点\\\"跨方法共识 → 更高质量电路\\\"。决定：Arithmetic gate 判定同时要求\\n    (1) off-diagonal 存在（>0%，证明方法特异性 artifact 存在）(2) CSS faithfulness > best single-method\\n    faithfulness（证明 consensus 的功能价值）。两条都满足 → PASS_MAIN；只满足一条 → 评估是否 task-specific；都不满足\\n    → 重新评估方向。同时要求 Arithmetic Phase D 使用 mean ablation 作为 zero ablation 的对比，排除 ablation\\n    方式的影响。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: evidence\\n    result: faithfulness ranking supports CSS > single-method\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: planned\\n    result: pending - must verify both off-diagonal + faithfulness ordering\\n  depends_on:\\n  - D018\\n  - D002\\n- id: D020\\n  date: 2026-05-13 01:34 UTC\\n  summary: 'CRITICAL: stable_core faithfulness 三重 FAIL，暂停 MVP pass 判定。根因是 D013 CIRCUS\\n    退化未修复——stable_core CPR=-0.187 远差于 CSS≥0.67 (CPR=+0.063)。必须先修复 CIRCUS (2D non-nested\\n    grid) 再重评。'\\n  rationale: Reviewer 深度验证发现：(1) stable_core IOI recall 仅 0.17 (2/12)，因为 CIRCUS-core\\n    系统性选中 Negative Name Mover 通路而非核心 IOI 正向信号边；(2) 这是 D013 CIRCUS 1D percentile →\\n    top-k EAP-IG 退化的直接后果；(3) CSS≥0.67 单独就达到 12/12 IOI recall + 正向 CPR，说明 cross-tabulation\\n    的\\\"附加价值\\\"目前为负；(4) D018 条件性 pass (off-diagonal 13.3%) 在 faithfulness 硬伤未修复前无效。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: evidence\\n    result: stable_core CPR=-0.187, IOI recall=0.17; CSS≥0.67 CPR=+0.063, recall=1.00\\n  depends_on:\\n  - D018\\n  - D013\\n  - D014\\n- id: D021\\n  date: 2026-05-13 02:07 UTC\\n  summary: 放弃 CIRCUS 作为独立 claim，转 CSS-only 叙事。CIRCUS 三次修复均失败，降级为 negative ablation\\n  rationale: CIRCUS 经历三轮修复全部失败：(1) D013 发现 1D percentile 嵌套退化为 top-k；(2) D020 stable_core\\n    faithfulness 三重 FAIL；(3) random-subset fix 后 stable_core CPR=-0.023, IOI recall=0/12，比旧版更差。根本问题是\\n    faithfulness-based stability scoring 在当前 circuit 粒度下无法产出有意义的 stable core。ARR DDL\\n    剩 12 天，不能再投入时间调试。CSS off-diagonal 13.3% 已过 gate，CSS-only 叙事足够支撑论文。CIRCUS 失败作为\\n    negative ablation 保留（\\\"structural consensus > faithfulness scoring\\\"），反而强化 CSS 的\\n    claim。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: evidence\\n    result: CSS off-diagonal 13.3% pass, but CIRCUS stable_core triple fail\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: ongoing\\n    result: Arithmetic validation running, independent of CIRCUS\\n  depends_on:\\n  - D020\\n  - D018\\n  - D013\\n- id: D022\\n  date: 2026-05-13 02:11 UTC\\n  summary: 紧急处理第三次 GPU 越界事件：杀 PID 897752 + 根因排查 + 强制 CUDA_VISIBLE_DEVICES=5\\n  rationale: Manager 报告进程 PID 897752 (17GB, 100% util) 越界占用 cuda:0（属于 rl-active-probe-fl\\n    项目），已导致对方代码和数据丢失。这是 cqa1-21977 上第三次越界事件，Manager 警告再犯将回收 GPU。根因待 Agent 排查（CUDA_VISIBLE_DEVICES\\n    未正确设置或被覆盖）。要求所有后续实验脚本开头强制 export CUDA_VISIBLE_DEVICES=5。\\n  related_experiments:\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: suspected_source\\n    result: 疑似越界进程来源，待确认\\n  depends_on: []\\n- id: D023\\n  date: 2026-05-13 02:18 UTC\\n  summary: 澄清 D021 与 D002 灰区关系：Arithmetic 实验 gate 统一为 CSS off-diagonal ≥5%，D002 的\\n    5-10% 灰区规则不再适用\\n  rationale: D002 原定义基于 CIRCUS-core edges：≥10% PASS_MAIN，5-10% 灰区走 Findings track。D021\\n    已从 CIRCUS 转向 CSS-only，指标体系变化，原灰区阈值不再有意义。Arithmetic 实验 gate 统一为 CSS off-diagonal\\n    ≥5% = PASS（确认跨任务泛化性），<5% = FAIL。D002 的 5-10% 灰区规则被 D021 显式 deprecate。\\n  related_experiments:\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: gate_experiment\\n    result: running\\n  depends_on:\\n  - D002\\n  - D021\\n- id: D024\\n  date: 2026-05-13 02:18 UTC\\n  summary: D021 覆盖 D002 灰区定义：arithmetic CSS off-diagonal ≥5% 即为 PASS，不再区分灰区\\n  rationale: D002 原定 5-10% 为灰区（走 Findings track），≥10% 为 PASS_MAIN。D021 pivot 为 CSS-only\\n    后将 arithmetic gate 改为 ≥5%。Reviewer 指出两者语义冲突。决定：D021 显式覆盖 D002 的灰区规则。理由：CSS-only\\n    pivot 后 off-diagonal 的意义更明确（纯 consensus 信号），5% 阈值已足够表明 cross-method structural\\n    agreement 非 task-specific。D002 的 5-10% 灰区基于 CIRCUS+CSS 混合框架下的不确定性，该前提已不存在。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n  - D021\\n- id: D025\\n  date: 2026-05-13 03:14 UTC\\n  summary: 更新 Arithmetic gate 为 CSS-only 四条件标准（替代 D024 的单一 5% 阈值）\\n  rationale: Reviewer 审查发现：(1) run_arithmetic.py 代码仍跑 CIRCUS cross-tabulation + D002\\n    旧阈值，D024 未落地到代码；(2) CIRCUS 已知 broken（D013 nesting + D017 scope mismatch），基于 CIRCUS\\n    的 off-diagonal % 无意义。采纳 Reviewer 建议的 CSS-only 四条件 gate：① Pairwise Jaccard 任意方法对\\n    < 0.70 ② CSS ≥2/3 edge count ≥ 10 ③ CSS = 1.0 edge count ≥ 3 ④ CSS faithfulness\\n    > single-method（D019）。四条全满足 = PASS。实验不中断（ACDC 75%+），结果出来后忽略代码 gate_verdict，人工按新标准判定。\\n  related_experiments:\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: target\\n    result: RUNNING\\n  depends_on:\\n  - D024\\n  - D021\\n  - D019\\n- id: D026\\n  date: 2026-05-13 03:39 UTC\\n  summary: Arithmetic D025 gate FAIL（条件④），暂不判 MVP 结果，先做 ACDC 阈值 ablation + mean ablation\\n    诊断\\n  rationale: Arithmetic CSS=1.0 CPR=-0.197 < EAP-IG CPR=-0.142，条件④失败。但 Reviewer 同时发现两个方法论问题：(1)\\n    ACDC isinf 仅保留 17 边，与 EAP-IG/EP 各 100 边形成 6:1 不对称，CSS=1.0 退化为纯 ACDC 输出；(2) 所有小电路\\n    CPR 均为负，zero ablation 可能对 Greaterthan 过于苛刻。这两个问题在 IOI 上同样存在但被正结果掩盖。在排除 binarization\\n    artifact 和 ablation method artifact 之前，不应判定 CSS 方法论失败。诊断方案：(a) ACDC top-k 阈值 sweep（k=50/100/150，CPU\\n    分析，不需新 GPU 实验）；(b) mean ablation 替代 zero ablation 重算 Phase D。两者均可在已有 raw scores\\n    上快速完成。\\n  related_experiments:\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: primary\\n    result: D025 gate FAIL (condition ④)\\n  depends_on:\\n  - D025\\n  - D019\\n- id: D027\\n  date: 2026-05-13 04:37 UTC\\n  summary: MVP 最终判定：CSS faithfulness 优势 task-dependent（IOI PASS / Arithmetic FAIL），不\\n    kill，reframe claim scope\\n  rationale: Arithmetic D025 条件④在 2 ablation × 4 k = 8 个配置下全部 FAIL，排除了 isinf 退化和 zero\\n    ablation artifact。IOI 在 zero ablation 下一致 PASS（k=isinf/50/100 均通过）。CSS 不是普遍优于单方法，而是在\\n    localized-circuit 任务（IOI 有明确的 Name Mover 等组件）上有效，在 distributed-computation 任务（Greaterthan）上无效。D003\\n    kill criteria 未触发（两任务 off-diagonal 均 >2%）。方向决策：(1) 不 kill 项目 (2) Reframe：从\\\"CSS\\n    always better\\\"转为\\\"CSS identifies faithful consensus when circuits are localized;\\n    reveals task structure when they're not\\\" (3) 补 1-2 个任务建立 localized vs distributed\\n    模式 (4) 这个发现本身比 universal claim 更有学术价值——审稿人更 appreciate nuanced finding。\\n  related_experiments:\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: primary\\n    result: FAIL (condition ④ across all 8 configs)\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: reference\\n    result: PASS (consistent across k and ablation)\\n  depends_on:\\n  - D026\\n  - D025\\n  - D021\\n- id: D028\\n  date: 2026-05-13 07:31 UTC\\n  summary: Phase 2 IFR 零重叠问题：暂停 Qwen/Gemma 新实验，先修 IFR per-head 分解 + 调 binarization\\n    比例\\n  rationale: Qwen-0.5B IOI K=3 实验显示 IFR×EAP-IG Jaccard=0.000, IFR×EP Jaccard=0.000，CSS=1.0=0\\n    条边。根因是 D010 已标记的 IFR layer-block voting：同层所有 head×QKV 共享 score，top-100 选出的边与 per-head\\n    方法完全正交。附加问题：179K 边取 top-100=0.06%，远低于 GPT-2 的 0.3%。两个修复方向并行验证：(1) ifr_scoring.py\\n    的 _decompose_per_head() 分解每头输出；(2) 改用 proportional binarization top-0.3%（~538\\n    边）。修复验证前暂停 Qwen/Gemma 新实验。SVA（GPT-2 + ACDC）不受影响，继续跑。\\n  related_experiments:\\n  - exp_id: phase2_qwen05b_ioi_k3\\n    role: primary\\n    result: CSS=1.0=0 edges, IFR zero overlap\\n  depends_on:\\n  - D027\\n- id: D029\\n  date: 2026-05-13 07:59 UTC\\n  summary: Phase 2 第三方法：放弃 IFR，改用 ACDC top-k。IFR 跨族分歧作为 Discussion finding。\\n  rationale: D028 两项诊断均失败：(1) per-head 分解已在使用，IFR 根本性偏向 MLP/early layers 而 gradient\\n    方法偏向 attention/late layers；(2) proportional binarization 到 3.5%（~6000 edges）才出现\\n    1 条 CSS=1.0 边。IFR×gradient Jaccard 结构性为零，不是调参能解决。ACDC top-k 是唯一已验证的跨族方法（GPT-2\\n    上与 gradient 有合理重叠）。计算成本高（30min-2h vs 1s）但 96GB 卡可承受。不选 AtP 因为与 EAP-IG/EP 同为 gradient\\n    族（K≈2 问题不解决）。IFR×gradient 分歧本身是有价值的 finding，放入论文 Discussion。\\n  related_experiments:\\n  - exp_id: phase2_qwen05b_ioi_k3\\n    role: evidence\\n    result: IFR zero overlap confirmed\\n  depends_on:\\n  - D028\\n- id: D030\\n  date: 2026-05-13 08:01 UTC\\n  summary: SVA D025 gate FAIL（zero FAIL / mean 边际 Δ=0.008）；发现 css_0.67 评估 bug 影响所有历史实验\\n  rationale: SVA GPT-2 K=3 (ACDC top-100) 结果：zero ablation CSS=1.0 CPR=-0.703 < EAP-IG=-0.348（FAIL）；mean\\n    ablation CSS=1.0 CPR=1.180 vs ACDC=1.172（Δ=0.008，噪声范围，无统计意义）。跨任务 pattern 确认：CSS=1.0\\n    faithfulness 优势仅在 IOI+GPT-2 + zero ablation 下成立（1/3 任务）。另发现 css_0.67 评估 bug：css_0.67\\n    实际在评估 css_1.0 的边集（阈值过滤逻辑错误），影响所有历史实验的 css≥0.67 数据。需立即修复后重评。\\n  related_experiments:\\n  - exp_id: mvp_sva_gpt2_k3_topk\\n    role: primary\\n    result: condition④ FAIL (zero) / marginal PASS (mean Δ=0.008)\\n  depends_on:\\n  - D027\\n  - D025\\n- id: D031\\n  date: 2026-05-13 08:04 UTC\\n  summary: 统一 D025 条件④标准：zero PASS 或 mean Δ≥0.01，SVA 两次均判 negative；修正 cqa1 registry\\n  rationale: Reviewer 发现 cqa1 SVA (conclusion=success) 与 westd SVA (conclusion=negative)\\n    对同一 pattern（zero FAIL + mean Δ=0.006）给出矛盾判定。统一标准：条件④要求 (a) zero ablation CSS >\\n    best single-method，或 (b) mean ablation CSS > best single-method 且 Δ ≥ 0.01。Δ=0.006/0.008\\n    在单 seed 单次运行下无统计意义（ACDC 跨硬件差异本身就有这个量级）。两次 SVA 均判 negative。cqa1 registry 需修正 conclusion=negative。\\n  related_experiments:\\n  - exp_id: mvp_sva_gpt2_k3\\n    role: primary\\n    result: corrected to negative\\n  - exp_id: mvp_sva_gpt2_k3_topk\\n    role: reference\\n    result: negative confirmed\\n  depends_on:\\n  - D030\\n  - D025\\n- id: D032\\n  date: 2026-05-13 08:12 UTC\\n  summary: 'D032: 条件④评估指标修正——必须用 css_1.00 而非 css_0.67'\\n  rationale: Reviewer 发现 D025 条件④定义为 \\\"CSS=1.0 > best single-method\\\"，但实际评估代码检查了 css_0.67\\n    的 CPR。这是一个与 css_0.67 filtering bug 相关但独立的问题：即使 css_0.67 的边集计算正确，条件④也应该用 css_1.00\\n    的 CPR。westd SVA 数据：css_1.00 mean CPR=1.1873 vs ACDC=1.1746, Δ=0.0127≥0.01（D031\\n    门槛），可能从 negative 翻转为 marginal PASS。需要 Agent 在 css_0.67 bug 修复后，用 css_1.00 重新跑条件④判定。\\n  related_experiments:\\n  - exp_id: mvp_sva_gpt2_k3_topk\\n    role: re-evaluate\\n    result: westd css_1.00 Δ=0.0127, pending re-evaluation\\n  - exp_id: mvp_sva_gpt2_k3\\n    role: invalidate\\n    result: cqa1 isinf + css_0.67 bug, conclusion unreliable → negative\\n  depends_on:\\n  - D031\\n  - D030\\n  - D025\\n- id: D033\\n  date: 2026-05-13 08:30 UTC\\n  summary: 'D033: SVA 判定降级为 inconclusive——单 seed Δ=0.013 不具鲁棒性'\\n  rationale: D032 将 westd SVA 从 negative 改为 success（css_1.00 Δ=0.0127≥0.01）。但 Reviewer\\n    指出：(1) cqa1 同任务/模型/seed Δ=0.006<0.01 仍为 negative，(2) 两台服务器结论分裂是 ACDC 硬件不确定性导致，(3)\\n    论文不能 cherry-pick 一台的结果。跨服务器平均 Δ=(0.013+0.006)/2=0.0095<0.01。因此 SVA 整体判定为 inconclusive/marginal，不计入\\n    clear success。论文中需如实报告两台结果并注明 marginal。当前真实成绩：IOI clear PASS, SVA inconclusive,\\n    Arithmetic FAIL。\\n  related_experiments:\\n  - exp_id: mvp_sva_gpt2_k3_topk\\n    role: downgrade\\n    result: success → inconclusive (Δ=0.013 not robust)\\n  - exp_id: mvp_sva_gpt2_k3\\n    role: context\\n    result: negative (Δ=0.006, same task different server)\\n  depends_on:\\n  - D032\\n  - D031\\n- id: D034\\n  date: 2026-05-13 08:37 UTC\\n  summary: 'D034: Qwen ACDC 确认 CSS 跨模型 scaling 根本性失败——问题不在方法选择而在模型规模'\\n  rationale: D029 将 IFR 替换为 ACDC top-0.3%，结果与 IFR 版本相同：CSS=1.0=0 边，所有 pairwise Jaccard≈0。关键发现：(1)\\n    ACDC 在 Qwen 上退化为 node-level scoring（与 IFR block-voting 同一问题），(2) 相同 binarization\\n    比例（0.3%），GPT-2(32k边) Jaccard=0.09-0.69 vs Qwen(179k边) Jaccard=0.00-0.04，差一个数量级，(3)\\n    单方法 faithfulness 也极低（EP CPR=0.055）。结论：CSS 跨模型 scaling 失败是结构性的，不可通过换方法修复。当前真实成绩：IOI\\n    GPT-2 明确 PASS，其余全部 FAIL 或 inconclusive。原 paper framing（CSS 作为正向方法贡献）不再可行。\\n  related_experiments:\\n  - exp_id: phase2_qwen05b_ioi_acdc_k3\\n    role: primary\\n    result: CSS=1.0=0 edges, all Jaccard≈0, FAIL\\n  - exp_id: phase2_qwen05b_ioi_k3\\n    role: context\\n    result: IFR version also 0 CSS=1.0 edges\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: contrast\\n    result: GPT-2 IOI PASS, same methods work at 32k scale\\n  depends_on:\\n  - D029\\n  - D025\\n- id: D035\\n  date: 2026-05-13 09:21 UTC\\n  summary: 'D035: Reframe 为分析论文 Route A — \\\"When Does Cross-Method Consensus Fail in\\n    Circuit Discovery?\\\" 目标 EMNLP Findings'\\n  rationale: Dream 三档结果（best 2/6 Reject, median/worst 3/6 Weak Reject）+ 实际实验结果（1/5\\n    PASS，Qwen scaling 根本性失败）共同表明：(1) 正向方法贡献论文不可行——即使 best case 也被 reject，(2) CSS =\\n    feature selection stability index，原框架有致命新颖性问题。Route A 将叙事从\\\"提出 CSS 方法\\\"转为\\\"系统性分析\\n    cross-method consensus 的失败模式\\\"：ACDC binarization pathology（三档一致最强贡献）、component-level\\n    scoring scaling failure、method correlation diagnostics。目标降为 EMNLP Findings。paper_framing.md\\n    和 experiment_plan.yaml 已更新。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: lone positive\\n    result: CSS PASS, but size confound pending\\n  - exp_id: phase2_qwen05b_ioi_acdc_k3\\n    role: scaling failure\\n    result: zero CSS=1.0 edges, node-level degeneration\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: task-dependent failure\\n    result: high Jaccard → CSS degenerates\\n  depends_on:\\n  - D034\\n  - D033\\n  - D029\\n\", \"total_chars\": 22880, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "466fd1ab-b5aa-4ab4-9306-190abd1b936b",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "00b51d32-7ec8-4ca6-b88e-1f469e76dfcd",
  "sourceToolAssistantUUID": "466fd1ab-b5aa-4ab4-9306-190abd1b936b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-13T10:05:16.704Z_

Now let me look at the actual paper artifacts and any writing plan.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00b51d32-7ec8-4ca6-b88e-1f469e76dfcd",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazNyt9GQACyUxyv1XSih",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1bcea038-2bd4-4e58-b6c7-74911750f1e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fe5bdM14uhZLyPUsWvJSkN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15372,
      "cache_read_input_tokens": 22951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15372,
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

_source line 23 · 2026-05-13T10:05:18.730Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014asxK4vReC7cPDKgyuen5E`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bcea038-2bd4-4e58-b6c7-74911750f1e1",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazNyt9GQACyUxyv1XSih",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61e7855a-bdd8-4f34-8c96-549a8e351d5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fe5bdM14uhZLyPUsWvJSkN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15372,
      "cache_read_input_tokens": 22951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15372,
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

_source line 24 · 2026-05-13T10:05:18.759Z_

<details><summary>↩ Tool result · `toolu_014asxK4vReC7cPDKgyuen5E`</summary>

```text
artifacts/dream_reports/dream_20260513T054654/best/paper.tex
artifacts/dream_reports/dream_20260513T054654/median/paper.tex
artifacts/dream_reports/dream_20260513T054654/worst/paper.tex
artifacts/dream_reports/dream_20260513T081242/best/paper.tex
artifacts/dream_reports/dream_20260513T081242/worst/paper.tex
artifacts/dream_reports/dream_20260513T092135/best/paper.tex
artifacts/dream_reports/dream_20260513T092135/median/paper.tex
artifacts/dream_reports/dream_20260513T092135/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61e7855a-bdd8-4f34-8c96-549a8e351d5f",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "8dc29be8-220b-4701-964e-1e00cdc288e6",
  "sourceToolAssistantUUID": "61e7855a-bdd8-4f34-8c96-549a8e351d5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T10:05:19.536Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01VKZ8oNefzGJ5g5MMLQjdR3`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dc29be8-220b-4701-964e-1e00cdc288e6",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazNyt9GQACyUxyv1XSih",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b890023-164d-46cf-ab32-8fd4d0792562",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fe5bdM14uhZLyPUsWvJSkN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15372,
      "cache_read_input_tokens": 22951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15372,
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

_source line 26 · 2026-05-13T10:05:19.554Z_

<details><summary>↩ Tool result · `toolu_01VKZ8oNefzGJ5g5MMLQjdR3`</summary>

```text
artifacts/dream_reports/dream_20260513T054654/best/paper.pdf
artifacts/dream_reports/dream_20260513T054654/median/paper.pdf
artifacts/dream_reports/dream_20260513T054654/worst/paper.pdf
artifacts/dream_reports/dream_20260513T081242/best/paper.pdf
artifacts/dream_reports/dream_20260513T081242/worst/paper.pdf
artifacts/dream_reports/dream_20260513T092135/best/paper.pdf
artifacts/dream_reports/dream_20260513T092135/median/paper.pdf
artifacts/dream_reports/dream_20260513T092135/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b890023-164d-46cf-ab32-8fd4d0792562",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "ba7a9892-ef71-4349-9077-cd750cfabe3d",
  "sourceToolAssistantUUID": "6b890023-164d-46cf-ab32-8fd4d0792562",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T10:05:20.131Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0178cDD9AdgdkmoFX5hk4QmN`</summary>

```json
{
  "project": "structfuse-context",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba7a9892-ef71-4349-9077-cd750cfabe3d",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazNyt9GQACyUxyv1XSih",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4ffb66b-6632-42ff-b66a-80a92c062cda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fe5bdM14uhZLyPUsWvJSkN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15372,
      "cache_read_input_tokens": 22951,
      "output_tokens": 285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15372
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 285,
          "cache_read_input_tokens": 22951,
          "cache_creation_input_tokens": 15372,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15372,
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

_source line 28 · 2026-05-13T10:05:20.141Z_

<details><summary>↩ Tool result · `toolu_0178cDD9AdgdkmoFX5hk4QmN`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4ffb66b-6632-42ff-b66a-80a92c062cda",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "2c52b4e3-905d-4dbb-ba77-de3ea36d8abb",
  "sourceToolAssistantUUID": "d4ffb66b-6632-42ff-b66a-80a92c062cda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-13T10:05:22.956Z_

Let me read the most recent dream report paper (the Route A reframed version) to understand the actual paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c52b4e3-905d-4dbb-ba77-de3ea36d8abb",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazNzLr81LpnHzKGtuBZA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5aaa67f8-d929-4378-b5b2-ba071686fba8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qe8rYQr51uUKDT9dj6fnSU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 761,
      "cache_read_input_tokens": 38323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 761,
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

_source line 30 · 2026-05-13T10:05:23.525Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JxQfRdbYgEenU4GJ2Vi6zQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T092135/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5aaa67f8-d929-4378-b5b2-ba071686fba8",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazNzLr81LpnHzKGtuBZA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffbbb0e7-f7ab-4006-87cb-15b81bc73c6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qe8rYQr51uUKDT9dj6fnSU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 761,
      "cache_read_input_tokens": 38323,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 761
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 38323,
          "cache_creation_input_tokens": 761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 761,
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

_source line 31 · 2026-05-13T10:05:23.818Z_

<details><summary>↩ Tool result · `toolu_01JxQfRdbYgEenU4GJ2Vi6zQ`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=2.5cm]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{microtype}
12	\usepackage[hidelinks]{hyperref}
13	\usepackage{url}
14	\usepackage{cite}
15	
16	\newcommand{\css}{\textsc{CSS}}
17	\newcommand{\cpr}{\textsc{CPR}}
18	\newcommand{\cmd}{\textsc{CMD}}
19	\newcommand{\eapig}{\textsc{EAP-IG}}
20	\newcommand{\acdc}{\textsc{ACDC}}
21	\newcommand{\ep}{\textsc{EP}}
22	\newcommand{\ifr}{\textsc{IFR}}
23	
24	\title{When Does Circuit Consensus Fail? \\ A Systematic Analysis of Cross-Method Agreement in Mechanistic Interpretability}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	\maketitle
30	
31	\begin{abstract}
32	Circuit discovery in mechanistic interpretability aims to identify minimal subgraphs that explain model behavior. An intuitive strategy is to trust edges endorsed by multiple discovery methods---a \emph{consensus} approach. We formalize this intuition as the \emph{Circuit Selection Score} (\css{}), a binary consensus metric computed over $K{=}3$ methods (\eapig{}, \ep{}, \acdc{}), and evaluate it across 4~tasks and 2~model architectures (GPT-2 Small, Qwen-0.5B), yielding 6~configurations. Consensus succeeds in only 1 of 6 configurations (IOI on GPT-2, $\Delta\cpr{}=+0.085$, $p{=}0.002$), while failing in the remaining 5 through three distinct mechanisms: (1)~task structure forces method correlation, collapsing consensus to obvious-edge selection (Arithmetic, Factual Recall, SVA); (2)~component-level scoring granularity on larger models causes near-zero inter-method overlap (Qwen-0.5B); and (3)~high pairwise Jaccard ($>0.5$) reliably predicts consensus failure (5/6 diagnostic accuracy, Spearman $\rho{=}{-}0.90$, $p{=}0.037$). A size-controlled baseline confirms that the sole success case reflects genuine selection quality, with 76\% of the advantage retained after controlling for edge count. These findings yield actionable guidelines: practitioners should compute pairwise Jaccard \emph{before} investing in multi-method validation, and verify that each method operates at true edge-level scoring granularity.
33	\end{abstract}
34	
35	%--------------------------------------------------
36	\section{Introduction}
37	\label{sec:intro}
38	%--------------------------------------------------
39	
40	Mechanistic interpretability seeks to reverse-engineer neural network computations by identifying \emph{circuits}---sparse subgraphs of the computational graph that are both necessary and sufficient for a given behavior \cite{elhage2021mathematical, conmy2023towards, wang2023interpretability}. Multiple circuit discovery methods now exist, each using different scoring mechanisms: gradient-based approaches (\eapig{}, \ep{}), activation patching (\acdc{}), and representation similarity (\ifr{}). An appealing idea is that edges endorsed by multiple independent methods constitute a more reliable circuit than any single method's output.
41	
42	We call this the \emph{consensus hypothesis}: cross-method agreement should identify a functionally faithful circuit core. Despite its intuitive appeal, this hypothesis has not been systematically tested. In this paper, we formalize consensus as the \emph{Circuit Selection Score} (\css{})---the fraction of methods selecting each edge---and evaluate whether high-consensus edges ($\css{}=1.0$, selected by all $K{=}3$ methods) outperform individual methods on circuit faithfulness metrics.
43	
44	Our experiments span 4~tasks (Indirect Object Identification, Arithmetic, Subject--Verb Agreement, Factual Recall) and 2~models (GPT-2 Small with 32K edges, Qwen-0.5B with 179K edges), yielding 6~model$\times$task configurations. The central finding is negative: \textbf{consensus fails in 5 of 6 configurations}, with only IOI on GPT-2 showing a statistically significant advantage ($\Delta\cpr{}=+0.085$, bootstrap $p{=}0.002$).
45	
46	We identify three mechanistic failure modes:
47	\begin{enumerate}
48	    \item \textbf{Task-induced method correlation} (\S\ref{sec:failure-correlation}): When task computation concentrates on bottleneck layers (e.g., MLP storage in Factual Recall), methods converge on the same obvious edges, and consensus degenerates to a strict subset of any single method.
49	    \item \textbf{Component-level scoring degeneration} (\S\ref{sec:failure-scaling}): On Qwen-0.5B (179K edges), both \ifr{} and \acdc{} degenerate from edge-level to node- or layer-level scoring, producing near-zero inter-method overlap and making edge-level consensus impossible.
50	    \item \textbf{Jaccard-predictable failure} (\S\ref{sec:diagnostic}): Maximum pairwise Jaccard $>0.5$ predicts consensus failure with 5/6 accuracy (Spearman $\rho=-0.90$, $p=0.037$ excluding scaling outlier), providing an actionable pre-check.
51	\end{enumerate}
52	
53	These results contribute: (a) the first systematic negative evaluation of cross-method consensus in circuit discovery; (b) a taxonomy of three distinct failure modes with mechanistic explanations; and (c) practical diagnostic guidelines that can save practitioners the computational cost of multi-method validation when consensus is unlikely to help.
54	
55	%--------------------------------------------------
56	\section{Background and Related Work}
57	\label{sec:related}
58	%--------------------------------------------------
59	
60	\paragraph{Circuit discovery methods.}
61	\eapig{} \cite{syed2023attribution} scores edges by the integrated gradient of the attribution-patching objective. \ep{} \cite{kramarcost} uses gradient-weighted edge pruning. \acdc{} \cite{conmy2023towards} iteratively removes edges via activation patching. \ifr{} \cite{zhang2024best} scores edges by intermediate representation similarity. These methods use fundamentally different scoring mechanisms (gradient products, pruning sensitivity, clean--corrupt substitution, cosine similarity), motivating the hypothesis that their agreement should be informative.
62	
63	\paragraph{Ensemble approaches.}
64	\cite{nogueira2016measuring} formalize feature selection stability via consensus indices in machine learning. \cite{kuncheva2003measures} characterize ensemble diversity and its relationship to accuracy. In circuit discovery, CIRCUS \cite{parekh2026circus} explores within-method threshold diversity, while \cite{mondorf2025comparing} average continuous scores across methods. PIE \cite{pie2026} uses iterative pruning ensembles within a single paradigm. Our work differs in testing \emph{binary} cross-method consensus---the simplest aggregation strategy---and characterizing its failure modes.
65	
66	\paragraph{Evaluation metrics.}
67	We adopt the Circuit Performance Recovery (\cpr{}) and Circuit Metric Degradation (\cmd{}) framework of \cite{conmy2023towards}. \cpr{} measures the fraction of the original model's task-specific metric recovered by the circuit; \cmd{} measures the degradation when the circuit is ablated.
68	
69	%--------------------------------------------------
70	\section{Method}
71	\label{sec:method}
72	%--------------------------------------------------
73	
74	\subsection{Circuit Selection Score}
75	
76	Given $K$ circuit discovery methods and a computational graph $G=(V,E)$, each method $k$ produces a binary edge mask $m_k: E \to \{0,1\}$ after binarization. The \emph{Circuit Selection Score} of edge $e$ is:
77	\begin{equation}
78	    \css{}(e) = \frac{1}{K}\sum_{k=1}^{K} m_k(e)
79	\end{equation}
80	We use $K{=}3$ methods (\eapig{}, \ep{}, \acdc{}) with top-$n$ binarization to equalize edge counts across methods. The consensus circuit $C_\theta = \{e : \css{}(e) \geq \theta\}$ selects edges meeting a consensus threshold $\theta$. We focus on $\css{}=1.0$ (full consensus: all three methods agree).
81	
82	\subsection{Binarization}
83	All methods are binarized to the same edge count (top-$n$) to ensure commensurability. For GPT-2 Small experiments, $n \in \{50, 100\}$; edge counts are matched per experiment. We note that \acdc{} natively uses an \texttt{isinf} threshold that can produce highly sparse outputs, and we analyze this pathology in \S\ref{sec:failure-correlation}.
84	
85	\subsection{Evaluation Protocol}
86	Circuits are evaluated under two ablation regimes:
87	\begin{itemize}
88	    \item \textbf{Zero ablation}: Complement edges set to zero. More destructive; standard in the literature.
89	    \item \textbf{Mean ablation}: Complement edges set to training-set activation means. More conservative; used for robustness checks.
90	\end{itemize}
91	For each configuration, we compute \cpr{} over 100 evaluation examples and report paired bootstrap confidence intervals ($B{=}10{,}000$, BCa correction).
92	
93	\subsection{Jaccard Diagnostic}
94	To characterize method agreement, we compute pairwise Jaccard similarity between all $\binom{K}{2}$ pairs of binary edge masks:
95	\begin{equation}
96	    J(m_i, m_j) = \frac{|m_i \cap m_j|}{|m_i \cup m_j|}
97	\end{equation}
98	The maximum pairwise Jaccard serves as a summary statistic for method correlation. We test whether this predicts \css{} outcome.
99	
100	%--------------------------------------------------
101	\section{Experiments}
102	\label{sec:experiments}
103	%--------------------------------------------------
104	
105	We evaluate \css{} on 6 model$\times$task configurations spanning two architectures and four behavioral tasks.
106	
107	\subsection{Experimental Setup}
108	
109	\paragraph{Models.} GPT-2 Small \cite{radford2019language} (12 layers, 12 heads, $\sim$32K edges) and Qwen-0.5B \cite{bai2023qwen} (24 layers, 14 heads with GQA, $\sim$179K edges).
110	
111	\paragraph{Tasks.} (1)~\textbf{Indirect Object Identification (IOI)}: Predicting the indirect object in sentences like ``Mary and John went to the store. John gave the bag to \underline{\hspace{1cm}}'' \cite{wang2023interpretability}. (2)~\textbf{Arithmetic}: Two-digit addition carry detection. (3)~\textbf{Subject--Verb Agreement (SVA)}: Number agreement across attractors. (4)~\textbf{Factual Recall}: Country$\to$capital knowledge retrieval (``The capital of France is \underline{\hspace{1cm}}'').
112	
113	\paragraph{Methods.} \eapig{}, \ep{}, and \acdc{} on GPT-2; \eapig{}, \ep{}, and \ifr{}/\acdc{} on Qwen-0.5B (two configurations due to method availability).
114	
115	%--------------------------------------------------
116	\subsection{Main Results: CSS Success Rate}
117	\label{sec:main-results}
118	%--------------------------------------------------
119	
120	Table~\ref{tab:main-results} summarizes all 6 configurations. \css{}$=1.0$ produces a \cpr{} advantage over the best single method in only 1 of 6 cases.
121	
122	\begin{table*}[t]
123	\centering
124	\small
125	\begin{tabular}{llcccccc}
126	\toprule
127	\textbf{Task} & \textbf{Model} & \textbf{Max Jaccard} & \textbf{CSS=1.0 Edges} & \textbf{CSS \cpr{}} & \textbf{Best Single \cpr{}} & $\boldsymbol{\Delta}$ & \textbf{Verdict} \\
128	\midrule
129	IOI        & GPT-2   & 0.307 & 7   & 0.109 & 0.029 (ACDC) & +0.085$^{**}$ & PASS \\
130	Factual Recall & GPT-2 & 0.620 & 10 & 0.905 & 0.975 (EAP-IG) & $-$0.070$^{**}$ & FAIL \\
131	SVA        & GPT-2   & 0.653 & --- & ---   & ---          & +0.013\textsuperscript{ns} & FAIL \\
132	Arithmetic & GPT-2   & 0.695 & --- & ---   & ---          & $-$0.063$^{**}$ & FAIL \\
133	IOI (IFR)  & Qwen    & 0.540 & 0   & ---   & ---          & 0.000 & FAIL \\
134	IOI (ACDC) & Qwen    & 0.043 & 0   & ---   & ---          & $-$0.055 & FAIL \\
135	\bottomrule
136	\end{tabular}
137	\caption{Summary of \css{} performance across all configurations. \cpr{} values are under zero ablation. $\Delta$ = CSS=1.0 \cpr{} minus best single-method \cpr{} (positive = consensus helps). $^{**}$: $p<0.01$ by paired bootstrap; \textsuperscript{ns}: not significant ($p=0.482$). IOI on GPT-2 is the sole PASS case ($\Delta=+0.085$, $p=0.002$).}
138	\label{tab:main-results}
139	\end{table*}
140	
141	\paragraph{IOI (GPT-2): The sole success.} The 7 edges at \css{}$=1.0$ correspond to name-mover heads (9.9, 9.6, 10.0) and S-inhibition heads (7.3, 8.6)---the well-characterized functional core of the IOI circuit \cite{wang2023interpretability}. With max pairwise Jaccard $= 0.307$, the three methods provide genuinely diverse rankings, and their intersection isolates high-quality edges.
142	
143	\paragraph{Factual Recall (GPT-2): MLP bottleneck forces convergence.} All three methods converge on MLP storage layers 5--9 \cite{meng2022locating}. EAP-IG$\times$EP Jaccard $= 0.62$; the 10 consensus edges are dominated by bottleneck MLP edges. These are the most ``obvious'' edges---their \cpr{} of 0.905 is lower than EAP-IG's 50-edge circuit (0.975) because consensus discards method-specific but functionally relevant routing edges.
144	
145	\paragraph{Arithmetic and SVA (GPT-2): High Jaccard, no advantage.} Both configurations show max Jaccard $>0.65$, indicating that methods largely agree. Consensus cannot improve over individual methods when the methods already select similar edges. For SVA, the bootstrap CI crosses zero ($[-0.025, 0.052]$, $p=0.482$), confirming statistical non-significance.
146	
147	\paragraph{Qwen-0.5B: Scaling failure.} Neither \ifr{} nor \acdc{} produces any \css{}$=1.0$ edges. Both methods degenerate to component-level scoring (see \S\ref{sec:failure-scaling}).
148	
149	%--------------------------------------------------
150	\subsection{Factual Recall: A New Failure Case}
151	\label{sec:factual-recall}
152	%--------------------------------------------------
153	
154	\begin{table}[t]
155	\centering
156	\small
157	\begin{tabular}{lrcc}
158	\toprule
159	\textbf{Method} & \textbf{Edges} & \textbf{Mean \cpr{}} & \textbf{Mean \cmd{}} \\
160	\midrule
161	\eapig{}    & 50 & 0.975 & 0.112 \\
162	\ep{}       & 50 & 0.952 & 0.214 \\
163	\acdc{}     & 50 & 0.938 & 0.278 \\
164	CSS$\geq$2/3 & 40 & 0.932 & 0.385 \\
165	CSS$=$1.0  & 10 & 0.905 & 0.418 \\
166	\bottomrule
167	\end{tabular}
168	\caption{Factual Recall circuit evaluation (mean ablation). CSS$=$1.0 selects 10 edges at \cpr{}$=$0.905, underperforming \eapig{}'s 50 edges at 0.975 ($\Delta=-0.070$, $p=0.005$).}
169	\label{tab:factual-recall}
170	\end{table}
171	
172	\begin{table}[t]
173	\centering
174	\small
175	\begin{tabular}{lccc}
176	\toprule
177	 & \textbf{EAP-IG} & \textbf{EP} & \textbf{ACDC} \\
178	\midrule
179	\textbf{EAP-IG} & --- & 0.62 & 0.38 \\
180	\textbf{EP}     & 0.62 & --- & 0.33 \\
181	\textbf{ACDC}   & 0.38 & 0.33 & --- \\
182	\bottomrule
183	\end{tabular}
184	\caption{Pairwise Jaccard matrix for Factual Recall (top-50). High EAP-IG$\times$EP agreement (0.62) reflects shared sensitivity to MLP bottleneck edges.}
185	\label{tab:factual-recall-jaccard}
186	\end{table}
187	
188	Factual recall relies on MLP layers 5--9 for key--value knowledge storage \cite{meng2022locating}. Table~\ref{tab:factual-recall} shows that consensus monotonically degrades performance as the threshold increases: CSS$\geq$2/3 (40 edges, \cpr{}=0.932) already underperforms individual methods, and CSS$=$1.0 (10 edges, \cpr{}=0.905) removes method-specific routing edges that are functionally important despite lacking cross-method agreement. Table~\ref{tab:factual-recall-jaccard} confirms high method correlation (max Jaccard = 0.62), consistent with the MLP bottleneck forcing convergence.
189	
190	This result parallels Arithmetic ($\Delta=-0.063$): both are MLP-bottleneck tasks where the critical computation is concentrated in a small number of layers, forcing all methods to select overlapping edges regardless of their scoring mechanism.
191	
192	%--------------------------------------------------
193	\subsection{Size-Controlled Baseline (IOI)}
194	\label{sec:size-controlled}
195	%--------------------------------------------------
196	
197	\begin{table}[t]
198	\centering
199	\small
200	\begin{tabular}{lrcc}
201	\toprule
202	\textbf{Subcircuit} & \textbf{Edges} & \textbf{Zero \cpr{}} & \textbf{vs CSS $\Delta$}\\
203	\midrule
204	CSS$=$1.0         & 7 & 0.109 & --- \\
205	Top-7 \eapig{}    & 7 & 0.048 & $-$0.061 \\
206	Top-7 \acdc{}     & 7 & 0.042 & $-$0.067 \\
207	Top-7 \ep{}       & 7 & 0.035 & $-$0.074 \\
208	Random-7 ($\mu \pm \sigma$)  & 7 & $0.003 \pm 0.012$ & $-$0.106 \\
209	\bottomrule
210	\end{tabular}
211	\caption{Size-controlled comparison on IOI (all subcircuits contain exactly 7 edges). CSS$=$1.0 outperforms all single-method top-7 selections. Random-7 baseline: mean over 50 samples. Original $\Delta=0.080$; size-controlled $\Delta=0.061$; advantage retained = 76.3\%.}
212	\label{tab:size-controlled}
213	\end{table}
214	
215	A natural concern is that the IOI consensus advantage is a size artifact: CSS$=$1.0 selects only 7 edges vs.\ the 100 edges in single-method circuits, and fewer edges mean less collateral damage under zero ablation. Table~\ref{tab:size-controlled} controls for this by comparing CSS$=$1.0 against the top-7 edges from each individual method under identical conditions.
216	
217	CSS$=$1.0 (\cpr{}$=$0.109) significantly outperforms all top-7 baselines (best: \eapig{} at 0.048; random: $0.003 \pm 0.012$, $p < 0.001$). The size-controlled advantage ($\Delta = 0.061$) retains 76.3\% of the original advantage ($\Delta = 0.080$), confirming that the consensus benefit is predominantly a \emph{selection quality} effect, not a size artifact. The remaining 23.7\% likely reflects residual collateral damage differences.
218	
219	Edge identity analysis reveals that CSS$=$1.0 edges are not ``unique'' discoveries---5 of 7 overlap with EAP-IG's top-7, and 4 of 7 with ACDC's. The advantage comes from \emph{filtering out} method-specific false positives (e.g., early-layer position embedding edges with high gradient signal but low functional contribution), not from discovering edges invisible to individual methods.
220	
221	%--------------------------------------------------
222	\subsection{Bootstrap Confidence Intervals}
223	\label{sec:bootstrap}
224	%--------------------------------------------------
225	
226	\begin{table}[t]
227	\centering
228	\small
229	\begin{tabular}{lcccl}
230	\toprule
231	\textbf{Config} & $\boldsymbol{\Delta}$ & \textbf{95\% CI} & $\boldsymbol{p}$ & \textbf{Verdict} \\
232	\midrule
233	IOI (GPT-2) & +0.085 & [0.035, 0.138] & 0.002 & Sig.\ PASS \\
234	Arithmetic  & $-$0.063 & [$-$0.112, $-$0.018] & 0.008 & Sig.\ FAIL \\
235	Factual Rec.& $-$0.068 & [$-$0.118, $-$0.022] & 0.005 & Sig.\ FAIL \\
236	SVA         & +0.013 & [$-$0.025, 0.052] & 0.482 & Non-sig. \\
237	Qwen IFR    & \multicolumn{4}{c}{N/A (0 CSS$=$1.0 edges)} \\
238	Qwen ACDC   & \multicolumn{4}{c}{N/A (0 CSS$=$1.0 edges)} \\
239	\bottomrule
240	\end{tabular}
241	\caption{Paired bootstrap CIs ($B{=}10{,}000$, BCa) for $\Delta$\cpr{} (CSS$=$1.0 vs.\ best single method). IOI is the sole configuration with a CI entirely above zero.}
242	\label{tab:bootstrap}
243	\end{table}
244	
245	Table~\ref{tab:bootstrap} reports paired bootstrap confidence intervals for all configurations where CSS$=$1.0 edges exist. IOI is the sole significant positive result ($p=0.002$, CI entirely above zero). Arithmetic and Factual Recall are significantly \emph{worse} than the best single method ($p=0.008$ and $p=0.005$, respectively). SVA's CI spans zero ($[-0.025, 0.052]$, $p=0.482$), confirming its classification as FAIL: the consensus advantage is not statistically distinguishable from noise.
246	
247	The two Qwen configurations produce zero CSS$=$1.0 edges, precluding bootstrap analysis---this is itself evidence of failure mode 2 (component-level scoring degeneration, \S\ref{sec:failure-scaling}).
248	
249	%--------------------------------------------------
250	\section{Failure Mode Analysis}
251	\label{sec:failure-modes}
252	%--------------------------------------------------
253	
254	\subsection{Failure Mode 1: Task-Induced Method Correlation}
255	\label{sec:failure-correlation}
256	
257	When a task's critical computation concentrates on a small set of bottleneck components (e.g., MLP knowledge-storage layers in Factual Recall, carry-propagation heads in Arithmetic), all discovery methods---regardless of scoring mechanism---converge on these components. The resulting high Jaccard ($>0.5$) means that consensus adds no information beyond what any single method already provides, while the strict intersection \emph{removes} method-specific edges that may be functionally important.
258	
259	Factual Recall illustrates this clearly: EAP-IG$\times$EP Jaccard $= 0.62$, with both methods selecting MLP layers 5--9 as their top-ranked edges. CSS$=$1.0 edges are almost exclusively these bottleneck edges---the ``triple-verified'' core that is also the most obvious. Meanwhile, EAP-IG's gradient signal captures attention routing edges that are method-specific but contribute to the 0.975 \cpr{} that consensus cannot match.
260	
261	\subsection{Failure Mode 2: Component-Level Scoring Degeneration}
262	\label{sec:failure-scaling}
263	
264	\begin{table}[t]
265	\centering
266	\small
267	\begin{tabular}{lcccc}
268	\toprule
269	\textbf{Method} & \textbf{Scoring} & \textbf{Granularity} & \textbf{$J$ vs \eapig{}} & \textbf{$J$ vs \ep{}} \\
270	\midrule
271	\eapig{}  & Gradient$\times$act & Edge  & --- & 0.15 \\
272	\ep{}     & Gradient prune & Edge  & 0.15 & --- \\
273	\ifr{}    & Cosine sim.    & Layer & 0.00 & 0.00 \\
274	\acdc{}   & Act.\ patching & Node  & 0.022 & 0.021 \\
275	\bottomrule
276	\end{tabular}
277	\caption{Scoring granularity on Qwen-0.5B IOI (179K edges). \ifr{} degenerates to layer-level (GQA absorbs edge perturbations); \acdc{} degenerates to node-level (greedy pruning over 179K edges). Both produce near-zero Jaccard with gradient methods.}
278	\label{tab:scaling}
279	\end{table}
280	
281	On Qwen-0.5B, the computational graph contains $\sim$179K edges---5.6$\times$ more than GPT-2 Small. Table~\ref{tab:scaling} shows that two non-gradient methods degenerate:
282	
283	\paragraph{IFR degeneration.} Qwen uses Grouped Query Attention (GQA), where heads within a group share K/V projections. Removing a single attention edge is absorbed by co-group heads, driving \ifr{}'s cosine similarity scores to near-zero for individual edges. \ifr{} consequently selects only early-layer MLP edges (layers 0--5)---a bias detector, not an IOI circuit finder. Overlap with gradient methods: $J = 0.0$.
284	
285	\paragraph{ACDC degeneration.} \acdc{}'s greedy pruning evaluates edges sequentially. At 179K edges, per-edge evaluation becomes prohibitively expensive, causing \acdc{} to operate at node level (evaluating entire attention heads). The result is block-structured edge selection (all edges of a head selected or excluded together). Max Jaccard with gradient methods: 0.043.
286	
287	The CSS framework requires each method to provide independent edge-level scores. When methods degenerate to coarser granularities, the mathematical basis for edge-level consensus breaks down: the ``edges'' selected by different methods correspond to different levels of abstraction (individual edges vs.\ head blocks vs.\ layer ranges), making intersection semantically meaningless.
288	
289	\begin{table}[t]
290	\centering
291	\small
292	\begin{tabular}{lccccc}
293	\toprule
294	& \textbf{Edges} & \textbf{ACDC} & \textbf{IFR} & \textbf{Max $J$} & \textbf{CSS$=$1.0}\\
295	\midrule
296	GPT-2 & 32K & Edge & --- & 0.307 & 7 \\
297	Qwen  & 179K & Node & Layer & 0.043 & 0 \\
298	\bottomrule
299	\end{tabular}
300	\caption{Scale-dependent method behavior. On GPT-2, \acdc{} operates at edge level; on Qwen, both \acdc{} and \ifr{} degenerate to coarser granularity.}
301	\label{tab:gpt2-vs-qwen}
302	\end{table}
303	
304	%--------------------------------------------------
305	\subsection{Failure Mode 3: Jaccard Diagnostic}
306	\label{sec:diagnostic}
307	%--------------------------------------------------
308	
309	\begin{table*}[t]
310	\centering
311	\small
312	\begin{tabular}{llccccccc}
313	\toprule
314	\textbf{Task} & \textbf{Model} & \textbf{Methods} & \textbf{Max $J$} & \textbf{CSS \cpr{}} & \textbf{Best Single \cpr{}} & $\boldsymbol{\Delta}$ & \textbf{Prediction} & \textbf{Correct?} \\
315	\midrule
316	IOI          & GPT-2 & EAP/EP/ACDC & 0.307 & 0.109 & 0.029 & +0.085 & PASS ($<$0.35) & \checkmark \\
317	IOI (ACDC)   & Qwen  & EAP/EP/ACDC & 0.043 & ---   & ---   & $-$0.055 & PASS ($<$0.35) & $\times$\textsuperscript{$\dagger$} \\
318	IOI (IFR)    & Qwen  & EAP/EP/IFR  & 0.540 & ---   & ---   & 0.000 & FAIL ($>$0.50) & \checkmark \\
319	Factual Rec. & GPT-2 & EAP/EP/ACDC & 0.620 & 0.905 & 0.975 & $-$0.070 & FAIL ($>$0.50) & \checkmark \\
320	SVA          & GPT-2 & EAP/EP/ACDC & 0.653 & ---   & ---   & +0.013 & FAIL ($>$0.50) & \checkmark \\
321	Arithmetic   & GPT-2 & EAP/EP/ACDC & 0.695 & ---   & ---   & $-$0.063 & FAIL ($>$0.50) & \checkmark \\
322	\bottomrule
323	\end{tabular}
324	\caption{Jaccard diagnostic accuracy across all 6 configurations (sorted by max pairwise Jaccard). The diagnostic correctly predicts 5/6 outcomes. $^\dagger$The sole miss (Qwen ACDC) fails due to component-level scoring degeneration (Failure Mode 2), not method correlation---an orthogonal failure that Jaccard cannot detect. Spearman $\rho = -0.90$ ($p = 0.037$) excluding the scaling outlier; $\rho = -0.714$ ($p = 0.111$) on all 6. GPT-2 subset (4 tasks): $\rho = -1.0$ ($p = 0.042$).}
325	\label{tab:diagnostic}
326	\end{table*}
327	
328	Table~\ref{tab:diagnostic} aggregates all configurations into a diagnostic summary. The maximum pairwise Jaccard serves as a strong predictor of CSS outcome:
329	
330	\begin{itemize}
331	    \item \textbf{Max Jaccard $< 0.35$}: CSS beneficial (1/1 correct---IOI on GPT-2).
332	    \item \textbf{Max Jaccard $> 0.50$}: CSS ineffective (4/4 correct---Factual Recall, SVA, Arithmetic, Qwen IFR).
333	    \item \textbf{Gap zone (0.35--0.50)}: No data points; proceed with caution.
334	\end{itemize}
335	
336	The sole diagnostic miss is Qwen ACDC (max $J = 0.043$, predicted PASS, actual FAIL). This outlier reflects Failure Mode 2: low Jaccard coexists with failure because the methods have degenerated to different scoring granularities, not because they provide diverse edge-level perspectives. The Jaccard diagnostic correctly captures method-correlation failures (Failure Mode 1) but cannot detect method-degeneration failures (Failure Mode 2).
337	
338	Within the GPT-2 subset (4 tasks where all methods operate at edge level), the rank correlation is perfect: $\rho = -1.0$ ($p = 0.042$). This supports the Jaccard diagnostic as a reliable heuristic when methods are known to function at edge-level granularity.
339	
340	We acknowledge that $n=6$ is underpowered for strong statistical claims. We frame the diagnostic as an \emph{empirically supported heuristic}, not a proven law, and recommend that future work validate it on additional tasks and models.
341	
342	%--------------------------------------------------
343	\subsection{Ablation Method Robustness (IOI)}
344	\label{sec:ablation-robustness}
345	%--------------------------------------------------
346	
347	\begin{table}[t]
348	\centering
349	\small
350	\begin{tabular}{lccccc}
351	\toprule
352	\textbf{Ablation} & \textbf{CSS \cpr{}} & \textbf{ACDC} & \textbf{EAP-IG} & \textbf{EP} & $\boldsymbol{\Delta}$ \\
353	\midrule
354	Zero & 0.109 & 0.029 & --- & --- & +0.080 \\
355	Mean & 0.182 & 0.117 & 0.078 & 0.052 & +0.065 \\
356	\bottomrule
357	\end{tabular}
358	\caption{IOI CSS advantage under zero vs.\ mean ablation. $\Delta$ = CSS$=$1.0 minus best single method. Advantage retained under mean ablation: 81.3\%.}
359	\label{tab:ablation-robustness}
360	\end{table}
361	
362	Table~\ref{tab:ablation-robustness} verifies that the IOI consensus advantage is not an artifact of the zero-ablation evaluation protocol. Under mean ablation, all \cpr{} values increase (complement edges retain mean-level signal), but the relative advantage persists: $\Delta = 0.065$ (mean) vs.\ $\Delta = 0.080$ (zero), retaining 81.3\% of the advantage. This rules out the hypothesis that consensus edges benefit disproportionately from the destructive nature of zero ablation.
363	
364	%--------------------------------------------------
365	\section{Discussion}
366	\label{sec:discussion}
367	%--------------------------------------------------
368	
369	\paragraph{Why does IOI succeed?}
370	IOI on GPT-2 is the sole configuration where consensus helps. The distinguishing feature is low method correlation (max Jaccard $= 0.307$): the three methods provide genuinely independent rankings, and their intersection filters out method-specific noise. The IOI circuit's well-characterized modular structure \cite{wang2023interpretability}---with distinct functional roles (name movers, S-inhibition heads, duplicate token detectors)---may enable methods to ``agree for the right reasons'' on the functional core while diverging on peripheral edges.
371	
372	\paragraph{Practitioner guidelines.}
373	Our results suggest a two-step protocol before investing in multi-method circuit validation:
374	\begin{enumerate}
375	    \item \textbf{Verify scoring granularity}: Ensure each method operates at true edge-level resolution. Check for block-structured edge selection (\acdc{} on large models) or layer-concentrated selection (\ifr{} with GQA). If any method has degenerated, exclude it before computing consensus.
376	    \item \textbf{Compute pairwise Jaccard}: If max pairwise Jaccard $> 0.50$, consensus is unlikely to help---use the best single method instead. If $< 0.35$, consensus may provide genuine selection-quality improvement.
377	\end{enumerate}
378	
379	\paragraph{Limitations.}
380	Our evaluation covers 2 models and 4 tasks. While the failure modes we identify are mechanistically grounded and likely general, the Jaccard thresholds (0.35, 0.50) are empirical and may require adjustment on different architectures. The $n=6$ sample size is insufficient for robust threshold estimation; we recommend these as starting points for further validation, not as established thresholds.
381	
382	%--------------------------------------------------
383	\section{Conclusion}
384	\label{sec:conclusion}
385	%--------------------------------------------------
386	
387	We present the first systematic evaluation of cross-method binary consensus in circuit discovery. Across 6 model$\times$task configurations, consensus succeeds in only one case (IOI on GPT-2, $\Delta=+0.085$, $p=0.002$), with a size-controlled baseline confirming that 76\% of this advantage reflects genuine selection quality. The remaining 5 configurations fail through three distinct, mechanistically explained failure modes: task-induced method correlation, component-level scoring degeneration at scale, and high pairwise Jaccard as a diagnostic predictor of failure. These findings provide actionable guidelines for practitioners: compute pairwise Jaccard and verify method granularity before committing to multi-method validation. The consensus hypothesis---that cross-method agreement identifies better circuits---is not wrong in principle, but its applicability is far narrower than commonly assumed.
388	
389	%--------------------------------------------------
390	% References
391	%--------------------------------------------------
392	\begin{thebibliography}{20}
393	
394	\bibitem{bai2023qwen}
395	J.~Bai et al.
396	Qwen technical report.
397	{\em arXiv:2309.16609}, 2023.
398	
399	\bibitem{conmy2023towards}
400	A.~Conmy, A.~Mavor-Parker, A.~Lynch, S.~Heimersheim, and A.~Garriga-Alonso.
401	Towards automated circuit discovery for mechanistic interpretability.
402	In {\em NeurIPS}, 2023.
403	
404	\bibitem{elhage2021mathematical}
405	N.~Elhage, N.~Nanda, C.~Olsson, et al.
406	A mathematical framework for transformer circuits.
407	{\em Transformer Circuits Thread}, 2021.
408	
409	\bibitem{kramarcost}
410	J.~Kram{\'a}r, T.~Lieberum, R.~Shah, and N.~Nanda.
411	AtP*: An efficient and scalable method for localizing LLM behaviour to components.
412	{\em arXiv:2403.00745}, 2024.
413	
414	\bibitem{kuncheva2003measures}
415	L.~I.~Kuncheva and C.~J.~Whitaker.
416	Measures of diversity in classifier ensembles and their relationship with the ensemble accuracy.
417	{\em Machine Learning}, 51(2):181--207, 2003.
418	
419	\bibitem{meng2022locating}
420	K.~Meng, D.~Bau, A.~Andonian, and Y.~Belinkov.
421	Locating and editing factual associations in GPT.
422	In {\em NeurIPS}, 2022.
423	
424	\bibitem{mondorf2025comparing}
425	P.~Mondorf, L.~Strobl, and B.~Plank.
426	Comparing circuit discovery methods for mechanistic interpretability.
427	{\em arXiv:2510.06811}, 2025.
428	
429	\bibitem{nogueira2016measuring}
430	S.~Nogueira and G.~Brown.
431	Measuring the stability of feature selection.
432	In {\em ECML-PKDD}, 2016.
433	
434	\bibitem{parekh2026circus}
435	P.~Parekh et al.
436	CIRCUS: Within-method threshold diversity for circuit discovery.
437	{\em arXiv preprint}, 2026.
438	
439	\bibitem{pie2026}
440	Anonymous.
441	PIE: Pruning iterative ensembles for circuit discovery.
442	{\em arXiv:2604.16889}, 2026.
443	
444	\bibitem{radford2019language}
445	A.~Radford, J.~Wu, R.~Child, D.~Luan, D.~Amodei, and I.~Sutskever.
446	Language models are unsupervised multitask learners.
447	{\em OpenAI Blog}, 2019.
448	
449	\bibitem{syed2023attribution}
450	A.~Syed, C.~Rager, and A.~Conmy.
451	Attribution patching outperforms automated circuit discovery.
452	{\em arXiv:2310.10348}, 2023.
453	
454	\bibitem{wang2023interpretability}
455	K.~Wang, A.~Variengien, A.~Conmy, B.~Shlegeris, and J.~Steinhardt.
456	Interpretability in the wild: A circuit for indirect object identification in GPT-2 small.
457	In {\em ICLR}, 2023.
458	
459	\bibitem{zhang2024best}
460	F.~Zhang and N.~Nanda.
461	Best practices for circuit discovery with automated interpretability.
462	{\em arXiv preprint}, 2024.
463	
464	\end{thebibliography}
465	
466	\end{document}
467	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffbbb0e7-f7ab-4006-87cb-15b81bc73c6e",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "35d00449-e98b-4148-8ffa-57babfd11747",
  "sourceToolAssistantUUID": "ffbbb0e7-f7ab-4006-87cb-15b81bc73c6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-13T10:05:27.202Z_

Now let me also read the median and worst dream reports to understand the reviewer concerns, and check for the dream review report itself.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35d00449-e98b-4148-8ffa-57babfd11747",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazNzcGp5evAUn1DtXAHm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "275bfa00-5b6e-4cbc-b73c-abc3eb5ecf2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NHuLEZ6u8XGghJvNQ9EpnF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11585,
      "cache_read_input_tokens": 39084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11585,
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

_source line 33 · 2026-05-13T10:05:29.571Z_

<details open><summary>🔧 Tool call — Read · `toolu_0179D45mBtE2PhryaHwneTEh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T092135/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "275bfa00-5b6e-4cbc-b73c-abc3eb5ecf2e",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazNzcGp5evAUn1DtXAHm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ada415b1-3b4c-45b3-bc82-b67af1d349b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NHuLEZ6u8XGghJvNQ9EpnF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11585,
      "cache_read_input_tokens": 39084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11585,
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

_source line 34 · 2026-05-13T10:05:29.934Z_

<details><summary>↩ Tool result · `toolu_0179D45mBtE2PhryaHwneTEh`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{enumitem}
12	\usepackage{natbib}
13	\usepackage[hidelinks]{hyperref}
14	
15	\newcommand{\css}{\textsc{CSS}}
16	\newcommand{\cpr}{\textsc{CPR}}
17	\newcommand{\cmd}{\textsc{CMD}}
18	
19	\title{When Does Cross-Method Consensus Improve Circuit Discovery?\\A Systematic Analysis of Failure Modes}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	Mechanistic interpretability increasingly relies on automated circuit discovery to identify minimal subgraphs that explain model behavior. When multiple discovery methods exist, a natural hypothesis is that their consensus---edges selected by all methods---yields more faithful circuits. We test this hypothesis systematically by applying binary consensus scoring (\css{}) across three methods (EAP-IG, Edge Pruning, ACDC) on four tasks and two model scales (GPT-2 Small, 32K edges; Qwen-0.5B, 179K edges). Consensus produces a marginal advantage on only 1 of 5 configurations (IOI on GPT-2, $\Delta\cpr{}=0.08$, $p=0.09$), which attenuates to $\Delta=0.02$ ($p=0.27$) after controlling for circuit size. We identify three distinct failure modes: (1) ACDC's \texttt{isinf} binarization collapses consensus to a single method's output, (2) high inter-method agreement (Jaccard $>0.5$) renders consensus redundant, and (3) component-level scoring granularity on larger models produces near-zero cross-method overlap. These findings yield practical diagnostic guidelines: practitioners should check pairwise Jaccard similarity and scoring granularity compatibility \emph{before} investing in multi-method consensus pipelines.
28	\end{abstract}
29	
30	%===================================================================
31	\section{Introduction}
32	%===================================================================
33	
34	Circuit discovery aims to identify minimal computational subgraphs within neural networks that are sufficient to reproduce a target behavior \cite{conmy2023towards,wang2023interpretability}. Several automated methods now exist---gradient-based approaches such as EAP-IG \cite{syed2023attribution} and Edge Pruning \cite{bhaskar2024finding}, ablation-based methods such as ACDC \cite{conmy2023towards}, and hybrid approaches like Iterative Feature Refinement (IFR).
35	
36	When multiple methods are available for the same problem, ensemble strategies from machine learning suggest that their agreement should be more reliable than any individual method. This intuition is formalized in feature selection stability theory \cite{nogueira2016measuring}: the intersection of independently selected feature sets should be enriched for genuinely important features. Applied to circuit discovery, this motivates \emph{Cross-method Consensus Scoring} (\css{}): binarize each method's output and take their intersection.
37	
38	We test this hypothesis systematically across four tasks (Indirect Object Identification, Greater-Than Arithmetic, Subject-Verb Agreement, Country-Capital Factual Recall) and two model scales (GPT-2 Small with ${\sim}32$K edges, Qwen-0.5B with ${\sim}179$K edges). Our main findings are:
39	
40	\begin{enumerate}[nosep,leftmargin=*]
41	    \item \css{} produces a marginal faithfulness advantage on only 1 of 5 configurations (IOI on GPT-2), with the advantage largely attributable to circuit size effects (\S\ref{sec:size-confound}).
42	    \item We identify three mechanistically distinct failure modes: binarization pathology (\S\ref{sec:binarization}), consensus redundancy under high agreement (\S\ref{sec:redundancy}), and scoring granularity mismatch at scale (\S\ref{sec:granularity}).
43	    \item A simple Jaccard-based diagnostic correctly predicts \css{} utility in 4 of 5 configurations, though statistical power is insufficient for formal validation (\S\ref{sec:diagnostic}).
44	\end{enumerate}
45	
46	Our contribution is not the consensus framework itself---which follows directly from stability indices \cite{nogueira2016measuring,kuncheva2003measures}---but the systematic empirical characterization of \emph{when and why} it fails in the circuit discovery setting, yielding actionable practitioner guidelines.
47	
48	%===================================================================
49	\section{Background and Related Work}
50	%===================================================================
51	
52	\paragraph{Circuit discovery methods.}
53	We study three representative methods spanning two paradigms. \textbf{EAP-IG} \cite{syed2023attribution} computes integrated-gradient attributions for each edge in the computational graph. \textbf{Edge Pruning} (EP; \citealp{bhaskar2024finding}) optimizes continuous edge masks via gradient descent. Both are gradient-based and score at edge-level granularity. \textbf{ACDC} \cite{conmy2023towards} iteratively removes edges via activation patching, scoring at node level and propagating scores to edges.
54	
55	\paragraph{Consensus and ensemble methods.}
56	The idea of aggregating multiple discovery methods has been explored in concurrent work. \citet{mondorf2025cross} propose cross-method score averaging over continuous attribution values. PIE \cite{chen2026pie} uses iterative pruning ensembles within a single paradigm. CIRCUS \cite{parekh2026circus} applies within-method threshold diversity rather than cross-method consensus. Our approach differs in using binary consensus (intersection), which enables direct failure mode analysis without conflating score-scale incompatibilities.
57	
58	\paragraph{Feature selection stability.}
59	Binary consensus is an instance of the stability index framework of \citet{nogueira2016measuring}. The theoretical conditions under which ensemble intersection improves over individual selectors are well-characterized \cite{kuncheva2003measures}: methods must be (a) individually accurate and (b) sufficiently diverse (low pairwise correlation). Our failure modes map directly onto violations of these conditions.
60	
61	%===================================================================
62	\section{Method: Cross-Method Consensus Scoring}
63	\label{sec:method}
64	%===================================================================
65	
66	\paragraph{Setup.}
67	Given a language model $\mathcal{M}$ with computational graph $G=(V,E)$ where $|E|$ can range from ${\sim}32$K (GPT-2 Small) to ${\sim}179$K (Qwen-0.5B), and a set of $K$ circuit discovery methods $\{M_1, \ldots, M_K\}$, each method produces a ranking $r_k: E \to \mathbb{R}$.
68	
69	\paragraph{Binarization.}
70	We convert each continuous ranking to a binary mask. For gradient-based methods (EAP-IG, EP), we select the top-$N$ edges by attribution magnitude. For ACDC, which produces a binary circuit, we use its native output (which we show in \S\ref{sec:binarization} to be problematic). As a normalization, we also evaluate top-$N$ binarization uniformly across all methods.
71	
72	\paragraph{Consensus scoring.}
73	For each edge $e \in E$, we compute:
74	\begin{equation}
75	    \css{}(e) = \frac{1}{K} \sum_{k=1}^{K} \mathbf{1}[e \in \text{top-}N(M_k)]
76	\end{equation}
77	Edges with $\css{}=1.0$ (selected by all $K$ methods) form the consensus circuit. We also examine $\css{}\geq 2/3$ (majority consensus).
78	
79	\paragraph{Evaluation metrics.}
80	We evaluate circuits using \textbf{Circuit Performance Recovery} (\cpr{}): the fraction of clean model performance recovered when running only the circuit edges (with remaining edges ablated). We use zero ablation throughout (see \S\ref{sec:limitations} for discussion). We also report \textbf{Circuit Mean Degradation} (\cmd{} $= 1 - \cpr{}$).
81	
82	%===================================================================
83	\section{Experiments}
84	\label{sec:experiments}
85	%===================================================================
86	
87	We evaluate \css{} with $K=3$ methods (EAP-IG, EP, ACDC) across four tasks on GPT-2 Small, and additionally test scaling behavior on Qwen-0.5B for IOI.
88	
89	%-------------------------------------------------------------------
90	\subsection{IOI: The Marginal Positive Case}
91	\label{sec:ioi}
92	%-------------------------------------------------------------------
93	
94	Indirect Object Identification (IOI; \citealp{wang2023interpretability}) is a well-studied task where the model must identify ``Mary'' in ``When John and Mary went to the store, John gave a drink to \underline{\hspace{1em}}.''
95	
96	On GPT-2 Small with top-100 binarization, the \css{}$=1.0$ consensus circuit contains only 7 edges. In the original (uncontrolled) comparison, this circuit achieves $\cpr{}=0.109$, outperforming all single-method top-100 circuits. However, this comparison conflates the consensus effect with circuit size: a 7-edge circuit naturally suffers less ablation damage than a 100-edge circuit.
97	
98	\paragraph{Size confound analysis.}
99	\label{sec:size-confound}
100	To isolate the consensus effect from circuit size, we compare \css{}$=1.0$ (7 edges) against the top-7 edges from each individual method and a random baseline. Table~\ref{tab:ioi-size} presents the results.
101	
102	\begin{table}[t]
103	\centering
104	\small
105	\begin{tabular}{lcccc}
106	\toprule
107	\textbf{Circuit} & \textbf{N} & \textbf{\cpr{}} & \textbf{\cmd{}} & \textbf{$\Delta$} \\
108	\midrule
109	\css{}$=1.0$ & 7 & 0.109 & 0.911 & --- \\
110	ACDC top-7 & 7 & 0.092 & 0.928 & $-0.017$ \\
111	EAP-IG top-7 & 7 & 0.078 & 0.942 & $-0.031$ \\
112	EP top-7 & 7 & 0.065 & 0.955 & $-0.044$ \\
113	Random-7 & 7 & $-0.031_{\pm 0.045}$ & $1.051_{\pm 0.045}$ & $-0.140$ \\
114	\bottomrule
115	\end{tabular}
116	\caption{IOI size-controlled comparison ($N=7$ edges, zero ablation). \css{} retains a small advantage over individual methods' top-7 edges, but the margin is substantially reduced from the uncontrolled comparison.}
117	\label{tab:ioi-size}
118	\end{table}
119	
120	\begin{table}[t]
121	\centering
122	\small
123	\begin{tabular}{lccc}
124	\toprule
125	\textbf{Comparison} & \textbf{Orig.~$\Delta$} & \textbf{Size-ctrl $\Delta$} & \textbf{Retained} \\
126	\midrule
127	CSS vs ACDC & $0.081$ & $0.017$ & 42\% \\
128	CSS vs EAP-IG & $0.218$ & $0.031$ & 14\% \\
129	CSS vs EP & $0.350$ & $0.044$ & 13\% \\
130	\bottomrule
131	\end{tabular}
132	\caption{Size confound decomposition for IOI. Controlling for circuit size reduces the \css{} advantage by 58--87\%, indicating that the majority of the original advantage is attributable to circuit size rather than consensus quality.}
133	\label{tab:size-decomp}
134	\end{table}
135	
136	After size control, \css{}$=1.0$ retains a residual advantage of $\Delta\cpr{}=0.017$ over the best single method (ACDC top-7). While directionally consistent with the consensus hypothesis, this margin is small and, as we show next, not statistically significant.
137	
138	\paragraph{Bootstrap confidence intervals.}
139	Table~\ref{tab:bootstrap} presents bootstrap 95\% confidence intervals ($B=10{,}000$ resamples) for \cpr{} differences across all configurations. The size-controlled IOI advantage has a wide CI of $[-0.038, 0.071]$ ($p=0.27$), failing to exclude zero. Even the original (uncontrolled) IOI advantage is only marginally significant ($p=0.089$, CI $[-0.012, 0.174]$).
140	
141	\begin{table}[t]
142	\centering
143	\small
144	\begin{tabular}{llcccc}
145	\toprule
146	\textbf{Task} & \textbf{Comparison} & \textbf{$\Delta$\cpr{}} & \textbf{95\% CI} & \textbf{$p$} & \textbf{Sig.} \\
147	\midrule
148	IOI & CSS vs ACDC (orig.) & $0.081$ & $[-0.01, 0.17]$ & $.089$ & No \\
149	IOI & CSS vs ACDC (size-ctrl) & $0.017$ & $[-0.04, 0.07]$ & $.270$ & No \\
150	IOI & CSS vs EAP-IG (orig.) & $0.218$ & $[0.10, 0.34]$ & $.002$ & Yes$^*$ \\
151	Arith. & CSS vs EAP-IG & $-0.066$ & $[-0.14, 0.01]$ & $.960$ & No \\
152	SVA & CSS vs ACDC & $0.013$ & $[-0.05, 0.08]$ & $.350$ & No \\
153	\bottomrule
154	\end{tabular}
155	\caption{Bootstrap 95\% CIs for \cpr{} differences ($B=10{,}000$). $^*$Significant but confounded by circuit size (see Table~\ref{tab:size-decomp}).}
156	\label{tab:bootstrap}
157	\end{table}
158	
159	We therefore characterize IOI as a \emph{marginal} positive: \css{} shows a directionally correct but statistically weak advantage that is largely attributable to circuit size effects.
160	
161	%-------------------------------------------------------------------
162	\subsection{Factual Recall: An Inconclusive Configuration}
163	\label{sec:factual}
164	%-------------------------------------------------------------------
165	
166	Country-Capital factual recall on GPT-2 Small tests knowledge retrieval circuits, which are expected to be MLP-heavy. We apply the same $K=3$ methods with top-100 binarization. Table~\ref{tab:factual} summarizes the results.
167	
168	\begin{table}[t]
169	\centering
170	\small
171	\begin{tabular}{lccc}
172	\toprule
173	\textbf{Circuit} & \textbf{Edges} & \textbf{\cpr{}$\uparrow$} & \textbf{\cmd{}$\downarrow$} \\
174	\midrule
175	\css{}$=1.0$ & 12 & $0.83$ & $0.41$ \\
176	\css{}$\geq 0.67$ & 38 & $0.79$ & $0.48$ \\
177	EAP-IG top-100 & 100 & $0.88$ & $0.32$ \\
178	EP top-100 & 100 & $0.82$ & $0.43$ \\
179	ACDC top-100 & 100 & $0.85$ & $0.37$ \\
180	\bottomrule
181	\end{tabular}
182	\caption{Factual Recall \cpr{} comparison (zero ablation). \css{}$=1.0$ does not outperform the best single method (EAP-IG, $\cpr{}=0.88$ vs $0.83$).}
183	\label{tab:factual}
184	\end{table}
185	
186	The consensus circuit ($\css{}=1.0$, 12 edges) achieves $\cpr{}=0.83$, which is \emph{lower} than EAP-IG alone ($\cpr{}=0.88$, $\Delta=-0.05$). Pairwise Jaccard indices are low overall (EAP-IG$\times$EP: 0.42, EAP-IG$\times$ACDC: 0.18, EP$\times$ACDC: 0.15, three-way: 0.11), with 89\% of edges appearing in the off-diagonal region of the CSS distribution.
187	
188	The failure pattern here differs from other configurations: methods disagree not because of binarization artifacts or scaling issues, but because of \emph{component-type preference}---gradient methods favor attention edges (where gradients through softmax are larger), while ACDC's ablation-based approach better localizes MLP contributions. This creates low Jaccard scores despite each method individually achieving reasonable \cpr{}. The result is inconclusive: \css{} neither helps nor catastrophically fails, but cannot recover the complementary information that different methods capture about different component types.
189	
190	%-------------------------------------------------------------------
191	\subsection{Failure Mode 1: ACDC Binarization Pathology}
192	\label{sec:binarization}
193	%-------------------------------------------------------------------
194	
195	ACDC produces circuits via iterative activation patching with an \texttt{isinf}-like threshold: edges whose ablation effect exceeds a threshold are retained. This creates a structural asymmetry with gradient-based methods: ACDC's output is already binary and typically much sparser.
196	
197	Under the standard pipeline, \css{}$=1.0$ edges are necessarily a subset of ACDC's output (since ACDC contributes a binary $\{0,1\}$ vote). In configurations where ACDC selects fewer edges than the top-$N$ used for gradient methods, the consensus circuit degenerates to a subset of ACDC's circuit. We observed this pattern on IOI (5--6 of 7 consensus edges originate from ACDC), Arithmetic, and SVA.
198	
199	Switching to uniform top-$N$ binarization across all methods breaks this degeneracy and shifts pairwise Jaccard by $+0.16$ to $+0.25$, confirming that the pathology is an artifact of binarization strategy rather than genuine method agreement.
200	
201	%-------------------------------------------------------------------
202	\subsection{Failure Mode 2: Consensus Redundancy}
203	\label{sec:redundancy}
204	%-------------------------------------------------------------------
205	
206	On Greater-Than Arithmetic and Subject-Verb Agreement (SVA), pairwise Jaccard indices are high (Arithmetic: max 0.695; SVA: max 0.653). When methods already agree substantially, consensus provides no new information---the intersection is essentially a single method's output with slightly fewer edges. For Arithmetic, \css{} produces $\Delta\cpr{}=-0.066$ versus the best single method (bootstrap CI $[-0.14, 0.01]$, $p=0.96$), indicating that the intersection actually \emph{removes} useful edges that not all methods select. SVA shows a near-zero effect ($\Delta=0.013$, CI $[-0.05, 0.08]$).
207	
208	%-------------------------------------------------------------------
209	\subsection{Failure Mode 3: Scoring Granularity Mismatch}
210	\label{sec:granularity}
211	%-------------------------------------------------------------------
212	
213	On Qwen-0.5B (${\sim}179$K edges), we observe a qualitatively different failure: near-zero inter-method overlap regardless of binarization. Root cause analysis reveals that both non-gradient methods degenerate to coarser-than-edge scoring:
214	
215	\begin{table}[t]
216	\centering
217	\small
218	\begin{tabular}{lccc}
219	\toprule
220	\textbf{Method} & \textbf{Scoring Level} & \textbf{Eff.~Resolution} & \textbf{Unique / 100} \\
221	\midrule
222	EAP-IG & edge & 1 edge & 100 \\
223	EP & edge & 1 edge & 100 \\
224	IFR & block (layer) & ${\sim}200$ edges & ${\sim}3$--5 \\
225	ACDC & node (head/MLP) & ${\sim}500$--2K edges & ${\sim}8$--12 \\
226	\bottomrule
227	\end{tabular}
228	\caption{Scoring granularity comparison on Qwen-0.5B. Non-gradient methods assign identical scores to all edges within a component, producing block-structured selections with few unique score values.}
229	\label{tab:granularity}
230	\end{table}
231	
232	IFR assigns identical scores to all edges within a layer block (${\sim}200$ edges per block), while ACDC assigns identical scores to all edges from the same attention head or MLP block (${\sim}500$--2{,}000 edges per node). Table~\ref{tab:granularity-jaccard} shows the resulting pairwise Jaccard values.
233	
234	\begin{table}[t]
235	\centering
236	\small
237	\begin{tabular}{lcc}
238	\toprule
239	\textbf{Pair} & \textbf{Jaccard} & \textbf{Same Gran.?} \\
240	\midrule
241	EAP-IG $\times$ EP & 0.54 & Yes (edge--edge) \\
242	EAP-IG $\times$ IFR & 0.00 & No (edge--block) \\
243	EAP-IG $\times$ ACDC & 0.04 & No (edge--node) \\
244	EP $\times$ IFR & 0.00 & No (edge--block) \\
245	EP $\times$ ACDC & 0.04 & No (edge--node) \\
246	IFR $\times$ ACDC & 0.00 & No (block--node) \\
247	\bottomrule
248	\end{tabular}
249	\caption{Pairwise Jaccard on Qwen-0.5B by scoring granularity. Methods operating at different granularities have near-zero overlap.}
250	\label{tab:granularity-jaccard}
251	\end{table}
252	
253	This is not an implementation bug but an architectural limitation: IFR's forward intervention is inherently layer-granular, and ACDC's activation patching operates at node granularity. With $K=3$ methods where the two gradient methods are highly correlated (Jaccard $=0.54$), the effective number of independent information sources drops from $K=3$ to $K \approx 1.5$, rendering consensus meaningless.
254	
255	%-------------------------------------------------------------------
256	\subsection{Jaccard Diagnostic}
257	\label{sec:diagnostic}
258	%-------------------------------------------------------------------
259	
260	Aggregating across all 5 task$\times$model configurations, we observe a negative relationship between maximum pairwise Jaccard and \css{} advantage ($\Delta\cpr{}$), as shown in Table~\ref{tab:jaccard-scatter}.
261	
262	\begin{table}[t]
263	\centering
264	\small
265	\begin{tabular}{lccc}
266	\toprule
267	\textbf{Configuration} & \textbf{Max Jaccard} & \textbf{$\Delta$\cpr{}} & \textbf{CSS Helps?} \\
268	\midrule
269	IOI / GPT-2 & 0.307 & $+0.081$ & Yes (marginal) \\
270	Factual Recall / GPT-2 & 0.420 & $-0.050$ & No \\
271	IOI / Qwen-0.5B & 0.540 & $0.000$ & No \\
272	SVA / GPT-2 & 0.653 & $+0.013$ & No \\
273	Arithmetic / GPT-2 & 0.695 & $-0.066$ & No \\
274	\bottomrule
275	\end{tabular}
276	\caption{Max pairwise Jaccard vs \css{} advantage across all configurations. \css{} shows a positive effect only in the lowest-Jaccard configuration.}
277	\label{tab:jaccard-scatter}
278	\end{table}
279	
280	A simple threshold rule emerges: configurations with max Jaccard $< 0.35$ benefit from \css{} (1/1), while those with max Jaccard $> 0.50$ never do (0/3). The gap zone ($0.35$--$0.50$, Factual Recall) yields an incorrect prediction. Spearman $\rho = -0.70$, but with $n=5$, $p=0.19$---far from significant.
281	
282	We frame this as a \emph{motivated conjecture}: the pattern is directionally consistent and mechanistically plausible (low Jaccard implies diverse methods, a prerequisite for useful consensus), but $n=5$ configurations are insufficient for statistical validation. Practitioners may find the Jaccard check useful as a cheap pre-screening heuristic, but it should not be treated as a validated decision boundary.
283	
284	%-------------------------------------------------------------------
285	\subsection{CIRCUS Comparison}
286	\label{sec:circus}
287	%-------------------------------------------------------------------
288	
289	As an ablation, we compare \css{} (cross-method consensus) against CIRCUS-style within-method threshold diversity: varying the binarization threshold within a single method to generate multiple circuit ``voters.'' CIRCUS produces negative \cpr{} on all three tested tasks (IOI, Arithmetic, SVA), confirming that cross-method diversity provides signal that within-method threshold variation cannot replicate.
290	
291	%===================================================================
292	\section{Discussion}
293	%===================================================================
294	
295	\paragraph{Failure mode taxonomy.}
296	Our three failure modes map onto known conditions from ensemble theory \cite{kuncheva2003measures}. Mode~1 (binarization pathology) violates the \emph{independence} assumption: one method's binarization dominates the consensus. Mode~2 (high agreement) violates the \emph{diversity} requirement: highly correlated methods provide redundant votes. Mode~3 (granularity mismatch) violates the \emph{commensurability} assumption: methods must operate on the same feature space for intersection to be meaningful.
297	
298	\paragraph{Practitioner guidelines.}
299	Based on our findings, we recommend: (1)~normalize binarization across methods (use top-$N$ uniformly rather than mixing native thresholds); (2)~compute pairwise Jaccard before investing in consensus---if max Jaccard $> 0.5$, consensus is unlikely to help; (3)~verify that all methods score at the same granularity, especially on models with $> 100$K edges.
300	
301	%===================================================================
302	\section{Limitations}
303	\label{sec:limitations}
304	%===================================================================
305	
306	\paragraph{Size confound.}
307	The sole positive configuration (IOI on GPT-2) is substantially confounded by circuit size. In the original comparison, \css{}$=1.0$ (7 edges) is evaluated against single-method top-100 circuits, creating a $14\times$ size disparity. After controlling for size (Table~\ref{tab:ioi-size}), the \css{} advantage shrinks from $\Delta=0.081$ to $\Delta=0.017$---a 79\% reduction. The residual advantage, while directionally correct, is not statistically significant ($p=0.27$). We cannot rule out that the entire \css{} effect on IOI is a size artifact.
308	
309	\paragraph{Statistical power.}
310	Bootstrap confidence intervals are wide throughout: the IOI original-comparison CI spans $[-0.012, 0.174]$, with the lower bound near zero. Our evaluation set (100 prompts $\times$ 7 edges) provides limited statistical power. The Jaccard diagnostic analysis covers only $n=5$ configurations, insufficient for correlation testing ($p=0.19$). All quantitative claims should be interpreted as directional evidence, not definitive conclusions.
311	
312	\paragraph{Task coverage.}
313	We evaluate on four tasks (IOI, Arithmetic, SVA, Factual Recall) across two models, totaling 5 complete configurations. This is insufficient to generalize failure mode prevalence or validate the Jaccard threshold. Notably, we have only one configuration with max Jaccard $< 0.35$, making it impossible to assess \css{}'s success rate in the low-Jaccard regime.
314	
315	\paragraph{Ablation method.}
316	All evaluations use zero ablation. Zero ablation has known biases for small circuits: ablating $N-k$ edges to zero (where $k \ll N$) can amplify or suppress performance differences relative to mean ablation. We did not complete a systematic comparison of zero vs.\ mean ablation due to time constraints. Our results may be sensitive to this choice, particularly the IOI positive finding where the circuit contains only 7 edges.
317	
318	\paragraph{Method selection.}
319	Our $K=3$ method set includes two gradient-based methods (EAP-IG, EP) that are inherently correlated (Jaccard $= 0.54$ on Qwen-0.5B). This reduces effective diversity. Alternative method sets (e.g., replacing EP with a non-gradient method) might yield different consensus behavior. We chose these methods for their public availability and widespread use, but acknowledge this limits the generality of our negative findings.
320	
321	%===================================================================
322	\section{Conclusion}
323	%===================================================================
324	
325	We presented a systematic evaluation of cross-method binary consensus (\css{}) for circuit discovery across four tasks and two model scales. Our main finding is negative: consensus succeeds marginally on only 1 of 5 configurations, with the advantage largely attributable to circuit size effects. We identified three mechanistically distinct failure modes---binarization pathology, consensus redundancy, and scoring granularity mismatch---each with a diagnostic signature. While our task and model coverage is limited ($n=5$ configurations) and statistical power is low, the failure modes are mechanistically grounded and yield concrete practitioner guidelines.
326	
327	The broader lesson is that multi-method consensus is not a free lunch in circuit discovery. The conditions under which ensemble approaches improve over individual methods are specific and verifiable. We hope that making these failure modes explicit encourages the community to develop consensus methods that are robust to binarization artifacts, adaptive to method diversity, and aware of scoring granularity---or to invest in improving individual methods rather than ensembling flawed ones.
328	
329	\paragraph{Future work.}
330	Validating the Jaccard diagnostic on a broader set of tasks and models is a priority. A systematic comparison of ablation methods (zero vs.\ mean) on all configurations would clarify whether the IOI positive finding is robust. Continuous consensus methods \cite{mondorf2025cross} that avoid binarization entirely may circumvent Failure Mode~1 and deserve comparative evaluation.
331	
332	\begin{thebibliography}{20}
333	
334	\bibitem[Bhaskar et~al.(2024)]{bhaskar2024finding}
335	Adithya Bhaskar, Alexander Wettig, Dan Friedman, and Danqi Chen.
336	\newblock Finding transformer circuits with edge pruning.
337	\newblock \emph{arXiv preprint arXiv:2406.16778}, 2024.
338	
339	\bibitem[Chen et~al.(2026)]{chen2026pie}
340	Xiao Chen et~al.
341	\newblock PIE: Pruning-based iterative ensembles for circuit discovery.
342	\newblock \emph{arXiv preprint arXiv:2604.16889}, 2026.
343	
344	\bibitem[Conmy et~al.(2023)]{conmy2023towards}
345	Arthur Conmy, Augustine Mavor-Parker, Aaquib Lynch, Stefan Heimersheim, and Adri\`{a} Garriga-Alonso.
346	\newblock Towards automated circuit discovery for mechanistic interpretability.
347	\newblock In \emph{NeurIPS}, 2023.
348	
349	\bibitem[Kuncheva and Whitaker(2003)]{kuncheva2003measures}
350	Ludmila~I. Kuncheva and Christopher~J. Whitaker.
351	\newblock Measures of diversity in classifier ensembles and their relationship with the ensemble accuracy.
352	\newblock \emph{Machine Learning}, 51(2):181--207, 2003.
353	
354	\bibitem[Mondorf et~al.(2025)]{mondorf2025cross}
355	Manuel Mondorf et~al.
356	\newblock Cross-method score averaging for circuit discovery.
357	\newblock \emph{arXiv preprint arXiv:2510.06811}, 2025.
358	
359	\bibitem[Nogueira and Brown(2016)]{nogueira2016measuring}
360	Sarah Nogueira and Gavin Brown.
361	\newblock Measuring the stability of feature selection.
362	\newblock \emph{JMLR}, 2016.
363	
364	\bibitem[Parekh et~al.(2026)]{parekh2026circus}
365	Jayneel Parekh et~al.
366	\newblock CIRCUS: Within-method threshold diversity for circuit discovery.
367	\newblock \emph{arXiv preprint}, 2026.
368	
369	\bibitem[Syed et~al.(2023)]{syed2023attribution}
370	Aaquib Syed, Can Rager, and Arthur Conmy.
371	\newblock Attribution patching outperforms automated circuit discovery.
372	\newblock \emph{arXiv preprint arXiv:2310.10348}, 2023.
373	
374	\bibitem[Wang et~al.(2023)]{wang2023interpretability}
375	Kevin Wang, Alexandre Variengien, Arthur Conmy, Buck Shlegeris, and Jacob Steinhardt.
376	\newblock Interpretability in the wild: a circuit for indirect object identification in GPT-2 Small.
377	\newblock In \emph{ICLR}, 2023.
378	
379	\end{thebibliography}
380	
381	\appendix
382	\section{Experimental Details}
383	\label{app:details}
384	
385	All experiments use the TransformerLens library for model hooks and circuit extraction. For EAP-IG, we use 10-step integrated gradients. For Edge Pruning, we train continuous masks for 500 steps with $L_1$ regularization ($\lambda=0.01$). For ACDC, we use the default threshold ($\tau=0.01$) with iterative node-level patching.
386	
387	Evaluation uses 100 prompts per task, sampled from the standard evaluation sets. Bootstrap confidence intervals use $B=10{,}000$ resamples with bias-corrected and accelerated (BCa) percentile intervals.
388	
389	GPT-2 Small has 12 layers, 12 attention heads, and approximately 32K edges in the computational graph. Qwen-0.5B has 24 layers, 16 attention heads, and approximately 179K edges.
390	
391	\end{document}
392	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ada415b1-3b4c-45b3-bc82-b67af1d349b8",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "09b4a7ce-4266-45cb-8f3a-9b94b2effd76",
  "sourceToolAssistantUUID": "ada415b1-3b4c-45b3-bc82-b67af1d349b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-13T10:05:29.986Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019uwAEZUMe5Fc2wXnJJZz2L`</summary>

```json
{
  "pattern": "**/dream_20260513T092135/**review*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09b4a7ce-4266-45cb-8f3a-9b94b2effd76",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazNzcGp5evAUn1DtXAHm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9d1047d-f9c5-4a6f-bcbe-6923d194da7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NHuLEZ6u8XGghJvNQ9EpnF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11585,
      "cache_read_input_tokens": 39084,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11585
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 39084,
          "cache_creation_input_tokens": 11585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11585,
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

_source line 36 · 2026-05-13T10:05:29.997Z_

<details><summary>↩ Tool result · `toolu_019uwAEZUMe5Fc2wXnJJZz2L`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9d1047d-f9c5-4a6f-bcbe-6923d194da7d",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "5c89c16a-8462-4a75-8892-5f12e4d675bf",
  "sourceToolAssistantUUID": "b9d1047d-f9c5-4a6f-bcbe-6923d194da7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-13T10:05:36.731Z_

Now let me check for any existing dream review reports.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c89c16a-8462-4a75-8892-5f12e4d675bf",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazP15XQeTNDNpMc8pLMY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "428727f1-66e6-4ce0-bcc3-5f29bef4a955",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gQkCjhuRYpAomFxzVgZeh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9638,
      "cache_read_input_tokens": 50669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9638,
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

_source line 38 · 2026-05-13T10:05:38.545Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Sk6uUoRq9CgDnW77MxhhMH`</summary>

```json
{
  "pattern": "**/dream_20260513T092135/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "428727f1-66e6-4ce0-bcc3-5f29bef4a955",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazP15XQeTNDNpMc8pLMY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bf5766f-297e-411a-b55e-3de31c11bec3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gQkCjhuRYpAomFxzVgZeh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9638,
      "cache_read_input_tokens": 50669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9638,
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

_source line 39 · 2026-05-13T10:05:38.563Z_

<details><summary>↩ Tool result · `toolu_01Sk6uUoRq9CgDnW77MxhhMH`</summary>

```text
artifacts/dream_reports/dream_20260513T092135/logs/orchestrator.log
artifacts/dream_reports/dream_20260513T092135/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260513T092135/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260513T092135/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260513T092135/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T092135/best/experiment_data.json
artifacts/dream_reports/dream_20260513T092135/best/paper_framing.md
artifacts/dream_reports/dream_20260513T092135/best/paper.tex
artifacts/dream_reports/dream_20260513T092135/best/paper.aux
artifacts/dream_reports/dream_20260513T092135/best/paper.out
artifacts/dream_reports/dream_20260513T092135/best/paper.pdf
artifacts/dream_reports/dream_20260513T092135/best/paper.log
artifacts/dream_reports/dream_20260513T092135/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260513T092135/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T092135/median/experiment_data.json
artifacts/dream_reports/dream_20260513T092135/median/paper_framing.md
artifacts/dream_reports/dream_20260513T092135/median/paper.tex
artifacts/dream_reports/dream_20260513T092135/median/paper.aux
artifacts/dream_reports/dream_20260513T092135/median/paper.out
artifacts/dream_reports/dream_20260513T092135/median/paper.pdf
artifacts/dream_reports/dream_20260513T092135/median/paper.log
artifacts/dream_reports/dream_20260513T092135/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260513T092135/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T092135/worst/experiment_data.json
artifacts/dream_reports/dream_20260513T092135/worst/paper_framing.md
artifacts/dream_reports/dream_20260513T092135/worst/paper.tex
artifacts/dream_reports/dream_20260513T092135/worst/paper.aux
artifacts/dream_reports/dream_20260513T092135/worst/paper.out
artifacts/dream_reports/dream_20260513T092135/worst/paper.pdf
artifacts/dream_reports/dream_20260513T092135/worst/paper.log
artifacts/dream_reports/dream_20260513T092135/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260513T092135/best/review_context.yaml
artifacts/dream_reports/dream_20260513T092135/best/review_report.md
artifacts/dream_reports/dream_20260513T092135/logs/review_best.log
artifacts/dream_reports/dream_20260513T092135/median/review_context.yaml
artifacts/dream_reports/dream_20260513T092135/logs/review_median.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bf5766f-297e-411a-b55e-3de31c11bec3",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "e2a7aaf0-1878-4dbf-9cd0-623d507d03ff",
  "sourceToolAssistantUUID": "5bf5766f-297e-411a-b55e-3de31c11bec3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-13T10:05:41.503Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RkfmNsBtQSzJ54NoRzxfcJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T092135/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2a7aaf0-1878-4dbf-9cd0-623d507d03ff",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazP1hhGnRU2J1uigUdbz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06a8c034-05a5-485e-961e-0bf064f05429",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLaMdqkkNncNj8ZQaSczbv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 976,
      "cache_read_input_tokens": 60307,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 976,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 41 · 2026-05-13T10:05:41.508Z_

<details><summary>↩ Tool result · `toolu_01RkfmNsBtQSzJ54NoRzxfcJ`</summary>

```text
1	---
2	dream_id: dream_20260513T092135
3	tier: best
4	overall_score: Borderline Findings (2.5/5)
5	timestamp: 2026-05-13T10:02:19.047972+00:00
6	---
7	
8	# Dream Review Report: "When Does Circuit Consensus Fail?"
9	
10	**Venue:** EMNLP 2026 Findings (ARR review form)
11	**Review Mode:** Full (2 Reviewers + 4-step Roundtable)
12	**Date:** 2026-05-13
13	
14	---
15	
16	## Reviewer Panel
17	
18	| Reviewer | Focus | Soundness | Excitement | Overall | Reproducibility | Confidence |
19	|----------|-------|-----------|------------|---------|-----------------|------------|
20	| R1 | Methods + Experiments | 3.0 | 3.0 | 3.0 | 3.0 | 4.0 |
21	| R2 | Novelty + Related Work | 3.0 | 2.5 | 2.5 | 4.0 | 4.0 |
22	| **Converged** | — | **3.0** | **2.5** | **2.5** | **3.5** | **4.0** |
23	
24	**Converged Verdict:** Borderline Findings (2.5/5)
25	
26	---
27	
28	## 1. Paper Summary
29	
30	The paper formalizes cross-method binary consensus in circuit discovery as the Circuit Selection Score (CSS = fraction of K=3 methods selecting each edge), and tests whether CSS=1.0 edges outperform individual methods on circuit faithfulness (CPR). Across 6 model×task configurations (4 tasks × {GPT-2 Small, Qwen-0.5B}), consensus succeeds in only 1/6 (IOI on GPT-2, ΔCPR=+0.085, p=0.002). Three failure modes are identified: (1) task-induced method correlation collapsing consensus to obvious-edge selection, (2) component-level scoring degeneration on larger models making edge-level consensus impossible, and (3) max pairwise Jaccard > 0.5 as a diagnostic predictor of failure. A size-controlled baseline confirms 76% of the IOI advantage is genuine selection quality. Practical guidelines are proposed: check method scoring granularity and compute Jaccard before investing in multi-method validation.
31	
32	---
33	
34	## 2. Consolidated Strengths
35	
36	**S1: The negative result is genuinely informative and well-structured.** [R1, R2 agree] The consensus hypothesis is widely held but previously untested. Demonstrating systematic failure in 5/6 configurations with mechanistic explanations constitutes a legitimate contribution. The three-failure-mode taxonomy provides actionable structure for the community.
37	
38	**S2: Size-controlled baseline is the paper's strongest experiment.** [R1 primary, R2 concurs] Comparing CSS=1.0 (7 edges) against top-7 from each individual method and random-7 (50 samples) at identical edge counts directly addresses the most obvious confound. The 76.3% retained advantage is convincing evidence that IOI success reflects selection quality, not a size artifact.
39	
40	**S3: Rigorous statistical practice.** [R1, R2 agree] Paired bootstrap CIs with BCa correction (B=10,000) are appropriate. Classifying SVA as FAIL based on CI crossing zero (p=0.482) rather than on point estimate direction is honest. Framing the Jaccard diagnostic as "empirically supported heuristic" rather than proven law is epistemically responsible.
41	
42	**S4: Component-level scoring degeneration (Failure Mode 2) is novel and practically important.** [R1, R2 agree] The mechanistic explanations — IFR degenerating to layer-level due to GQA KV sharing, ACDC degenerating to node-level at 179K edges — provide genuinely new architectural insight that transcends this paper's specific framework. This is the most original finding.
43	
44	**S5: Ablation method robustness check adds credibility.** [R1 primary] Testing zero vs. mean ablation on the sole success case (81.3% advantage retained) rules out the evaluation-protocol-artifact hypothesis.
45	
46	---
47	
48	## 3. Consolidated Weaknesses
49	
50	### Major
51	
52	**W1 [R1]: Edge-level CSS vs. node-level evaluation disconnect.** The CSS framework computes consensus at the edge level, but the ablation evaluation (CPR) operates at the node level — entire attention heads and MLP layers are zeroed/mean-replaced, not individual edges. Two circuits with different edge sets but identical node coverage would produce identical CPR values. This is a fundamental confound never discussed in the paper. The size-controlled baseline partially mitigates this (different methods' top-7 edges likely cover different nodes), but the Factual Recall analysis (Table 2) may really be measuring node coverage, not edge selection quality. **This undermines the central claim about edge selection quality.**
53	
54	**W2 [R2]: CSS is not methodologically novel.** CSS = (1/K)Σm_k(e) is a direct application of the feature selection stability index (Nogueira & Brown 2016) to binary edge masks. The entire Method section (§3) could be replaced by a single sentence. The paper's novelty must rest entirely on the empirical findings and failure mode analysis — which are interesting but thin at n=6.
55	
56	**W3 [R2]: Insufficient engagement with Mondorf et al. (2025).** This is the most directly comparable work: they test continuous score averaging across the same methods and find it outperforms binary intersection. Key question left unanswered: does continuous averaging succeed where binary CSS fails? If so, the failure modes identified here are about binarization, not about consensus per se — significantly narrowing the contribution.
57	
58	**W4 [R1, R2 converged]: n=6 is critically underpowered for the Jaccard diagnostic.** The Spearman ρ=−0.90 (p=0.037) requires excluding the Qwen-ACDC outlier; on all 6 points, ρ=−0.714 (p=0.111, not significant). The 0.35 and 0.50 thresholds are derived from exactly 1 data point below 0.35 and 4 above 0.50, with zero points in between. Any 4 points in strictly monotone order yield ρ=−1.0. The diagnostic is presented with more statistical ceremony than the sample size warrants.
59	
60	**W5 [R2]: EAP-IG and EP are gradient-adjacent, so K=3 is effectively K≈2.** Both are gradient-based (EAP-IG: integrated gradients of attribution-patching; EP: gradient-based mask optimization). The paper's own data confirms this: EAP-IG×EP Jaccard is consistently the highest pairwise value. The claim of "three independent algorithmic families" is overstated.
61	
62	**W6 [R1]: Binarization sensitivity is unexplored.** The paper uses top-n (n=50 or 100) but never varies n. Internal evidence suggests Jaccard shifts +0.16 to +0.25 when switching binarization strategies. How sensitive is the PASS/FAIL classification to the choice of n? Could IOI become FAIL at n=200, or Factual Recall become PASS at n=25? At minimum, one sweep (n ∈ {25, 50, 100, 200}) on IOI should be reported.
63	
64	### Moderate
65	
66	**W7 [R2]: Reference list is sparse (14 references).** Missing important citations include: Bhaskar et al. (2024, NeurIPS Spotlight) for Edge Pruning itself; Meloux et al. (2025) on intra-method instability; Hanna et al. (2024, COLM) on EAP-IG overlap vs. faithfulness; Miller et al. (2024, COLM) on faithfulness metric robustness; Sharkey et al. (2025) "Open Problems in MI"; InterpBench (NeurIPS 2024 D&B). A typical EMNLP paper in this area cites 30-40 references.
67	
68	**W8 [R1]: CPR values are inconsistently reported and CMD is underutilized.** IOI's "successful" CSS=1.0 circuit recovers only 10.9% of the model's logit difference (CPR=0.109). The paper never discusses what constitutes a practically meaningful CPR level. CMD is defined but absent from Table 1 and most analyses.
69	
70	**W9 [R1]: Multiple testing not addressed.** Four bootstrap tests are conducted; IOI (p=0.002) survives Bonferroni correction (0.05/4=0.0125), but this is never discussed. The probability of finding at least one significant result by chance under the null is ~18.5%.
71	
72	**W10 [R1]: Only small-scale models tested.** GPT-2 Small (124M) and Qwen-0.5B (500M) are both small. The scaling failure modes may manifest differently at 2B-7B scale where edge counts could reach millions.
73	
74	---
75	
76	## 4. Key Questions for Authors
77	
78	**Q1 [R1, critical]:** The evaluation implements node-level ablation, not edge-level ablation. How does this affect your conclusions? For the IOI size-controlled comparison (Table 4), did you verify that CSS=1.0 edges and top-7 EAP-IG edges cover different node sets?
79	
80	**Q2 [R2, critical]:** Have you tested whether continuous score averaging (as in Mondorf et al. 2025) succeeds in configurations where binary CSS fails? If not, the failure modes may be specific to binary consensus, not cross-method agreement in general.
81	
82	**Q3 [R1]:** How sensitive are the PASS/FAIL classifications to the choice of top-n? One binarization sweep (n ∈ {25, 50, 100, 200}) on IOI would substantially strengthen the paper.
83	
84	**Q4 [R2]:** Given that EAP-IG and EP are both gradient-based, have you considered testing with a genuinely non-gradient third method (e.g., probing, causal scrubbing) to provide truly independent algorithmic diversity?
85	
86	**Q5 [R1]:** Table 1 reports Δ=+0.085 for IOI, but Table 9 reports zero-ablation Δ=+0.080. This discrepancy (likely different baselines) should be reconciled.
87	
88	**Q6 [R2]:** The sole positive result (IOI on GPT-2) is the most studied circuit in the literature with a well-characterized 12-edge ground truth. Could CSS success here simply reflect that IOI is an "easy" circuit where methods trivially converge on the correct answer?
89	
90	---
91	
92	## 5. Minor Issues
93	
94	- Table 1: SVA and Arithmetic rows show "—" for CSS=1.0 Edges/CPR without explanation. Clarify whether CSS=1.0 edges exist.
95	- Table 2 caption says "mean ablation" but the text discusses it alongside zero ablation results.
96	- EP citation (Kramár et al. [4], "AtP*") may not be the actual method used; Bhaskar et al. (2024) for Edge Pruning is uncited.
97	- CIRCUS citation (Parekh et al. 2026) is incomplete — no venue, placeholder format.
98	- PIE citation is "Anonymous" despite having an arXiv ID.
99	- Equation 1 defines CSS for arbitrary K but only K=3 is used. State whether the framework generalizes.
100	- Istanbul listed as the capital of Turkey in the Factual Recall dataset is factually incorrect (it is Ankara). This affects data quality.
101	
102	---
103	
104	## 6. Experiment Coverage Assessment
105	
106	Comparing against the experiment design reference (review_context.yaml):
107	
108	| Planned Experiment | Covered in Paper? | Quality |
109	|---|---|---|
110	| GPT-2 Factual Recall K=3 CSS (v2) | Yes (§4.3, Tables 2-3) | Adequate |
111	| IOI Size-Controlled Baseline | Yes (§4.4, Table 4) | Strong — best experiment |
112	| Bootstrap Confidence Intervals | Yes (§4.5, Table 5) | Adequate |
113	| Ablation Method Comparison (Zero vs Mean) | Yes (§5.4, Table 9) | Adequate |
114	| IFR vs ACDC Divergence Analysis | Yes (§5.2, Tables 6-7) | Adequate |
115	| Jaccard-CSS Diagnostic | Yes (§5.3, Table 8) | Underpowered (n=6) |
116	
117	All planned experiments are represented. The paper covers the experiment plan comprehensively. However, several planned visualization elements (forest plot of CIs, Jaccard-CSS scatter plot, layer distribution histograms) are absent from the paper — these were described in the plan but apparently not included, reducing visual communication of results.
118	
119	---
120	
121	## 7. Roundtable Convergence Summary
122	
123	**Areas of strong agreement:**
124	- The negative result is a legitimate contribution (both reviewers)
125	- Failure Mode 2 (scoring degeneration) is the most novel and important finding (both)
126	- n=6 is underpowered for the Jaccard diagnostic claims (both)
127	- Statistical reporting is honest and appropriate (both)
128	- The size-controlled baseline is excellent (both)
129	
130	**Areas where reviewers converged after cross-sharing:**
131	- Edge-vs-node evaluation confound (R1 raised, R2 accepted as serious after cross-sharing)
132	- Mondorf et al. engagement gap (R2 raised, R1 accepted as important after cross-sharing)
133	- CSS methodological novelty is thin (R2 raised, R1 concurred)
134	
135	**Residual disagreement:**
136	- R1 leans toward 3.0 (Findings-acceptable), R2 toward 2.5 (Borderline Findings)
137	- After roundtable, both agree the paper is in the 2.5–3.0 range
138	- Final convergence at **2.5 (Borderline Findings)**, primarily because: (a) the edge-vs-node confound (W1) undermines the central evaluation framework, (b) the lack of engagement with continuous alternatives (W3) leaves open whether the failure modes are about binary consensus specifically or cross-method agreement generally, and (c) the reference coverage is below venue standards
139	
140	**What would move this to 3.0 (Findings accept):**
141	1. Address the edge-vs-node evaluation confound (W1) — even a brief analysis of node coverage overlap between CSS and single-method circuits
142	2. Test continuous score averaging on at least IOI and one FAIL case (W3)
143	3. Add one binarization sensitivity sweep (W6)
144	4. Expand references to 25+ with substantive engagement on Mondorf et al. and Bhaskar et al.
145	5. Add the planned but missing visualizations (forest plot, scatter plot)
146	
147	---
148	
149	## 8. Recommendation
150	
151	**Borderline Findings (2.5/5).** The paper addresses a real question with honest methods and arrives at a useful negative answer. The failure mode taxonomy — especially the component-level scoring degeneration finding — is a genuine contribution. However, the combination of (a) a fundamental edge-vs-node evaluation confound, (b) thin methodological novelty (CSS is a known stability index), (c) insufficient engagement with the most directly comparable work (Mondorf et al.), and (d) underpowered Jaccard diagnostic claims prevents a clear Findings recommendation. The paper is close to the acceptance threshold and could reach it with targeted revisions addressing W1, W3, and W7.
152	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06a8c034-05a5-485e-961e-0bf064f05429",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "dcad2ca4-20d1-4696-9ebf-91cfef63799f",
  "sourceToolAssistantUUID": "06a8c034-05a5-485e-961e-0bf064f05429",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-13T10:05:42.060Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FGXKgdYMgNJextD6X2gq4a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T092135/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcad2ca4-20d1-4696-9ebf-91cfef63799f",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazP1hhGnRU2J1uigUdbz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d6325f7-6387-468e-81e3-7994a8c9be52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLaMdqkkNncNj8ZQaSczbv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 976,
      "cache_read_input_tokens": 60307,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 976
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 60307,
          "cache_creation_input_tokens": 976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 976,
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

_source line 43 · 2026-05-13T10:05:42.066Z_

<details><summary>↩ Tool result · `toolu_01FGXKgdYMgNJextD6X2gq4a`</summary>

```text
1	narrative_guidance: 'Route A framing 完全成立。Factual Recall v2 产出清晰 FAIL（CSS-1.0 mean
2	  CPR=0.905 < EAP-IG=0.975，Δ=-0.070）， 提供第5个 FAIL 数据点，使总配置达 1 PASS / 5 FAIL（6 configs）。Size-controlled
3	  baseline 证实 IOI CSS 优势 76%归因于 selection quality 而非 edge count（top-7 EAP-IG CPR=0.048
4	  vs CSS=1.0 CPR=0.109）。Bootstrap CIs 确认 IOI Δ=0.085 显著（95% CI [0.035, 0.138]，p=0.002），SVA
5	  CI 跨零（[-0.025, 0.052]）验证其 FAIL 归类。 Ablation comparison 排除 zero-ablation artifact（IOI
6	  mean ablation Δ=0.065 仍为正）。Jaccard diagnostic 在全部 6 configs 上 5/6 正确（唯一失误是 Qwen
7	  ACDC 的 component-level scoring failure，属 Claim 3 而非 Claim 4 范畴）。 Claims 1-4 全部保留原始强度，Claim
8	  4 从 ''motivated conjecture'' 升级为 ''empirically supported heuristic''。 论文标题不变，投 Findings
9	  绰绰有余。
10	
11	  '
12	imagined_experiments:
13	- name: GPT-2 Factual Recall K=3 CSS (v2)
14	  plan_id: plan_004
15	  description: 'GPT-2 Small 上运行 country→capital factual recall（如 "The capital of France
16	    is" → "Paris"）。 K=3 方法（EAP-IG + EP + ACDC），top-50 binarization。MLP-based knowledge
17	    retrieval circuit 导致方法在 MLP bottleneck edges 上高度收敛，预期 max Jaccard > 0.5，CSS FAIL。
18	
19	    '
20	  expected_results:
21	    binarization: top-50
22	    edge_counts:
23	      eap_ig: 50
24	      ep: 50
25	      acdc: 50
26	    pairwise_jaccard:
27	      eapig_x_ep: 0.62
28	      acdc_x_eapig: 0.38
29	      acdc_x_ep: 0.33
30	    max_pairwise_jaccard: 0.62
31	    three_way_jaccard: 0.205
32	    css_distribution:
33	      '0.33': 74
34	      '0.67': 30
35	      '1.00': 10
36	    evaluation_mean:
37	      css_1.00:
38	        edges: 10
39	        CPR: 0.905
40	        CMD: 0.418
41	      css_0.67:
42	        edges: 40
43	        CPR: 0.932
44	        CMD: 0.385
45	      eap_ig:
46	        edges: 50
47	        CPR: 0.975
48	        CMD: 0.112
49	      ep:
50	        edges: 50
51	        CPR: 0.952
52	        CMD: 0.214
53	      acdc:
54	        edges: 50
55	        CPR: 0.938
56	        CMD: 0.278
57	    evaluation_zero:
58	      css_1.00:
59	        edges: 10
60	        CPR: -0.032
61	        CMD: 1.045
62	      eap_ig:
63	        edges: 50
64	        CPR: -0.085
65	        CMD: 1.198
66	      acdc:
67	        edges: 50
68	        CPR: -0.112
69	        CMD: 1.247
70	    d025_conditions:
71	      cond1_jaccard_lt070: PASS (0.62)
72	      cond2_css_ge23_ge10: PASS (30)
73	      cond3_css_10_ge3: PASS (10)
74	      cond4_cpr_dominance: 'FAIL (mean: css_1.00=0.905 < EAP-IG=0.975, Δ=-0.070)'
75	    factual_recall_css_vs_best_single_delta: -0.07
76	    jaccard_diagnostic_prediction: '>0.5 → FAIL'
77	    jaccard_diagnostic_correct: true
78	  result_rationale: 'Factual recall 依赖 MLP layer 5-9 的 key-value 知识存储机制（Meng et al.
79	    2022）和多层 attention head 的 subject→last-token routing。三种方法在 MLP 存储层的边上被迫高度共识——这些边是知识检索的
80	    不可替代瓶颈，无论用梯度、剪枝还是 activation patching 评估都会被选中。EAP-IG×EP Jaccard=0.62： 两种 gradient-adjacent
81	    方法在 MLP bottleneck edges 上几乎完全一致，分歧仅在 attention routing 边的 排序上。ACDC×gradient Jaccard
82	    较低（0.38/0.33）因为 ACDC 的 clean→corrupt substitution 在 routing edges 上给出不同排序，但仍然收敛于相同的
83	    MLP 核心。css_1.00 的 10 条边几乎全部是 MLP 存储层的 bottleneck edges——它们是三种算法视角的交集，但恰恰是最 obvious
84	    的边。这些边的 mean CPR=0.905 低于 EAP-IG 的 0.975， 因为 EAP-IG 的 50 条边额外捕获了 attention routing
85	    edges 中的 high-gradient 子集，这些 routing edges 虽然方法间不一致，但 EAP-IG 选中的那部分确实是 functionally
86	    important 的。CSS consensus 过滤掉了 这些 method-specific 但 functionally relevant 的 routing
87	    edges，导致 faithfulness 下降。 这与 Arithmetic 的失败模式一致：当任务的关键计算集中在少数 bottleneck 层时，方法收敛使
88	    consensus 退化为 obvious-edge selection，不优于最佳单方法。
89	
90	    '
91	  tables:
92	  - name: 'Table: Factual Recall Circuit Discovery Summary'
93	    description: '行: EAP-IG, EP, ACDC, CSS≥2/3, CSS=1.0 列: Edges, Mean CPR, Mean CMD,
94	      Δ(vs best single) CSS=1.0 的 10 edges mean CPR=0.905 < EAP-IG 50 edges CPR=0.975，Δ=-0.070
95	
96	      '
97	  - name: 'Table: Factual Recall Pairwise Jaccard Matrix'
98	    description: '3×3 对称矩阵：EAP-IG×EP=0.62, ACDC×EAP-IG=0.38, ACDC×EP=0.33。 与 Arithmetic
99	      (max_J=0.695) 并列，展示 MLP-heavy tasks 的方法收敛模式
100	
101	      '
102	  figures_description:
103	  - '加入 cross-task CPR bar chart 作为第四个 subplot。CSS=1.0 bar (0.905) 明显低于 EAP-IG bar
104	    (0.975)， 与 Arithmetic 类似的 FAIL pattern。视觉化 MLP-bottleneck task 上 consensus 失败。
105	
106	    '
107	  analysis: 'Factual Recall FAIL 使 pass/fail ratio 从 1/4 变为 1/5，进一步巩固 "consensus fails
108	    more often than it succeeds" 的核心叙事。max_J=0.62 落在 Arithmetic(0.695) 和 SVA(0.653)
109	    之间， Δ=-0.070 与 Arithmetic 的 Δ=-0.066 量级一致——两个 MLP-bottleneck 任务的平行失败 构成 failure
110	    mode 1（task structure forces method correlation）的强化证据。 对 Claim 4 的贡献：第6个数据点落在
111	    Jaccard > 0.5 区域且 FAIL， 使 >0.5 区域 FAIL rate 从 3/4 变为 4/5（排除 SVA 的 marginal case
112	    则为 3/3→4/4）， diagnostic accuracy 继续成立。
113	
114	    '
115	- name: IOI Size-Controlled Baseline
116	  plan_id: plan_008
117	  description: 'IOI 上控制 edge count：将 CSS=1.0（7 edges）与 top-7 of EAP-IG、top-7 of EP、top-7
118	    of ACDC、 random-7 edges 在相同 edge 数量下比较 zero ablation CPR。排除 "CSS 优势仅因 fewer edges"
119	    的 size confound。
120	
121	    '
122	  expected_results:
123	    css_1.00:
124	      edges: 7
125	      CPR_zero: 0.109
126	    top7_eapig:
127	      edges: 7
128	      CPR_zero: 0.048
129	    top7_acdc:
130	      edges: 7
131	      CPR_zero: 0.042
132	    top7_ep:
133	      edges: 7
134	      CPR_zero: 0.035
135	    random7:
136	      edges: 7
137	      CPR_zero: 0.003
138	      CPR_zero_std: 0.012
139	      n_random_samples: 50
140	    original_best_single_cpr: 0.029
141	    original_delta: 0.08
142	    size_controlled_delta: 0.061
143	    size_controlled_advantage_retained_pct: 76.3
144	    css_beats_all_top7: true
145	    css_beats_random_p_value: <0.001
146	  result_rationale: 'CSS=1.0 的 7 条边是 EAP-IG、EP、ACDC 三种独立算法视角的交集——它们对应 IOI circuit
147	    中 name mover heads（9.9, 9.6, 10.0）和 S-inhibition heads（7.3, 8.6）的关键 attention
148	    edges， 加上 1-2 条必要的 MLP routing edges。这些边被三种完全不同的评分机制（gradient×activation product、
149	    pruning sensitivity、clean→corrupt activation difference）共同认定为最重要， 构成了 IOI circuit
150	    的 "triple-verified functional core"。 相比之下，top-7 of EAP-IG（CPR=0.048）包含一些 gradient
151	    signal 强但功能贡献弱的边 （如 early-layer position embedding edges，gradient 高但 ablation
152	    后可被其他路径补偿）。 Top-7 of EP（CPR=0.035）包含 pruning-sensitive 但非 functionally-critical
153	    的边 （如 LayerNorm→attention edges，移除后 attention pattern 改变但不影响 name-moving 功能）。
154	    Top-7 of ACDC（CPR=0.042）质量略好于 EP（ACDC 的 activation patching 更直接衡量功能贡献）， 但仍包含 2-3
155	    条 ACDC-specific 的 false positives（其他方法未选中的边）。 Random-7 CPR≈0.003（50 次采样均值），确认
156	    7 条随机边几乎无功能意义。 Size-controlled advantage retained = (0.109-0.048)/0.080 = 76.3%：
157	    原始 CSS 优势的四分之三归因于 selection quality（consensus 过滤 method-specific noise）， 仅四分之一可能与
158	    size effect 相关。这直接回应 R3 的 size artifact 质疑。
159	
160	    '
161	  tables:
162	  - name: 'Table: Size-Controlled Baseline Comparison (IOI)'
163	    description: '行: CSS=1.0, Top-7 EAP-IG, Top-7 ACDC, Top-7 EP, Random-7 (mean±std,
164	      n=50) 列: Edges, Zero CPR, CMD, vs CSS Δ 底部: Advantage retained = 76.3%
165	
166	      '
167	  - name: 'Table: Edge Identity Analysis'
168	    description: 'CSS=1.0 的 7 条边与各 top-7 的 overlap 分析。 CSS∩EAP-IG_top7: 5/7, CSS∩ACDC_top7:
169	      4/7, CSS∩EP_top7: 4/7。 CSS-unique edges（仅 consensus 选中）: 0-1 条。证明 CSS 的优势不在于发现
170	      unique edges， 而在于从多个 top-ranked lists 的交集中过滤出 most reliable edges。
171	
172	      '
173	  figures_description:
174	  - 'Bar chart: x=method (CSS=1.0, EAP-IG top-7, ACDC top-7, EP top-7, Random-7),
175	    y=zero CPR。所有 bar 相同 edge count (N=7)。CSS=1.0 bar 显著高于其他。 Error bar on Random-7
176	    (±std from 50 samples)。灰色虚线 y=0。 右侧标注 "76% of advantage from selection quality"。
177	
178	    '
179	  analysis: 'Size-controlled baseline 排除了最直接的 confound。76.3% retained advantage 意味着：
180	    即使控制 edge count，consensus 选出的 7 条边仍显著优于任何单方法选出的 7 条边。 剩余 23.7% 的 "size effect"
181	    可能来自 original comparison 中 single methods 使用 100 edges 而 CSS 仅 7 edges——更多边意味着更多
182	    collateral damage under zero ablation。 这为 Claim 2 提供了 decisive control experiment：IOI
183	    的 CSS 成功是真正的 selection quality 效应，不是 size artifact。
184	
185	    '
186	- name: Bootstrap Confidence Intervals on CPR
187	  plan_id: plan_009
188	  description: '对所有完成实验的 CPR Δ（CSS=1.0 vs best single method）进行 paired bootstrap（B=10000），
189	    报告 95% BCa CIs。重点验证 IOI Δ 显著性（CI 不跨零）和 SVA 非显著性（CI 跨零 → 确认 FAIL 归类）。
190	
191	    '
192	  expected_results:
193	    ioi_gpt2:
194	      delta_point: 0.085
195	      delta_ci_95:
196	      - 0.035
197	      - 0.138
198	      p_value: 0.002
199	      n_eval_examples: 100
200	      bootstrap_samples: 10000
201	      significant: true
202	      note: paired bootstrap on per-example CPR differences; BCa correction for skewness
203	    arithmetic_gpt2:
204	      delta_point: -0.063
205	      delta_ci_95:
206	      - -0.112
207	      - -0.018
208	      p_value: 0.008
209	      significant: true
210	      direction: CSS significantly WORSE than EAP-IG
211	    sva_gpt2:
212	      delta_point: 0.013
213	      delta_ci_95:
214	      - -0.025
215	      - 0.052
216	      p_value: 0.482
217	      significant: false
218	      note: CI crosses zero, confirms SVA as FAIL (advantage not statistically significant)
219	    factual_recall_gpt2:
220	      delta_point: -0.068
221	      delta_ci_95:
222	      - -0.118
223	      - -0.022
224	      p_value: 0.005
225	      significant: true
226	      direction: CSS significantly WORSE than EAP-IG
227	    qwen_ifr:
228	      note: N/A — zero CSS=1.0 edges, bootstrap not applicable
229	    qwen_acdc:
230	      note: N/A — zero CSS=1.0 edges, bootstrap not applicable
231	    summary:
232	      significant_pass: 1
233	      significant_fail: 2
234	      non_significant: 1
235	      not_applicable: 2
236	  result_rationale: 'Paired bootstrap 是这些小样本 CPR 比较的最合适统计方法：每个评估示例同时计算 CSS 和 single-method
237	    CPR， 差值的 bootstrap 分布直接反映 CSS 优势的不确定性。BCa（bias-corrected and accelerated）修正 处理
238	    CPR 分布的偏斜（zero ablation CPR 常右偏）。 IOI Δ=0.085 (CI [0.035, 0.138])：100 个 IOI 评估示例中，CSS=1.0
239	    在大多数示例上优于 ACDC， per-example Δ 的标准差约 0.025，除以 sqrt(100)≈10 给出 SE≈0.025，95% CI 宽度约
240	    0.10。 CI 下界 0.035 > 0，p=0.002，IOI PASS 的统计显著性确认。 Arithmetic Δ=-0.063 (CI [-0.112,
241	    -0.018])：CI 完全在负区域，CSS 显著不如 EAP-IG， 确认 FAIL 结论。per-example 差异的方差较大（Arithmetic
242	    各示例的 difficulty 差异更大），CI 略宽。 SVA Δ=0.013 (CI [-0.025, 0.052])：CI 跨零，p=0.482，advantage
243	    统计不显著。 这是 best tier 的关键结果——SVA 从 "inconclusive" 正式归类为 FAIL（优势不显著 = 不支持 CSS 有效）。
244	    Factual Recall Δ=-0.068 (CI [-0.118, -0.022])：与 Arithmetic 模式一致的显著 FAIL。 两个 Qwen
245	    实验因 CSS=1.0=0 edges 无法计算 bootstrap（不是缺陷，而是反映 Claim 3 的 method degeneration）。
246	
247	    '
248	  tables:
249	  - name: 'Table: Bootstrap CI Summary (All Configurations)'
250	    description: '行: IOI, Arithmetic, SVA, Factual Recall, Qwen IFR (N/A), Qwen ACDC
251	      (N/A) 列: Δ Point, 95% CI Lower, 95% CI Upper, p-value, Verdict IOI 行高亮（唯一 CI
252	      完全正的配置）
253	
254	      '
255	  - name: 'Table: IOI Per-Example CPR Distribution'
256	    description: 'Histogram data: CSS=1.0 per-example CPR vs ACDC per-example CPR。
257	      展示 paired difference 分布的形状（轻微右偏，中位数 > 0）
258	
259	      '
260	  figures_description:
261	  - 'Forest plot: 每个 configuration 一行，点估计 + 95% CI 横线。 垂直虚线 x=0。IOI 的 CI 完全在正区域（蓝色），Arithmetic
262	    和 Factual Recall 完全在负区域（红色）， SVA 跨零（灰色）。Qwen 两行标注 "N/A"。 右侧标注 p-value。视觉化一目了然：IOI
263	    是唯一统计显著的 PASS。
264	
265	    '
266	  analysis: 'Bootstrap CIs 将整个实验体系的统计严谨性提升到 Findings 要求。 核心发现：IOI 是唯一 CI 不跨零的正向结果（p=0.002），
267	    SVA 的 CI 跨零（p=0.482）彻底消除了 D033 cross-server 分析的歧义—— SVA 不是 "inconclusive"，而是 "statistically
268	    confirmed FAIL"。 这使 pass/fail classification 完全由统计检验驱动，不依赖 ad hoc thresholds。
269	    直接回应 R6（"No confidence intervals on CPR differences"）。
270	
271	    '
272	- name: Ablation Method Comparison (Zero vs Mean) on IOI
273	  plan_id: plan_011
274	  description: '在 IOI 上比较 zero ablation 和 mean ablation 下 CSS=1.0 的 CPR advantage。
275	    排除 "IOI CSS 优势仅在 zero ablation 下成立" 的 evaluation artifact 质疑。
276	
277	    '
278	  expected_results:
279	    ioi_zero:
280	      css_1.00_CPR: 0.109
281	      best_single_CPR: 0.029
282	      delta: 0.08
283	      best_single_method: ACDC (14 edges)
284	    ioi_mean:
285	      css_1.00_CPR: 0.182
286	      best_single_CPR: 0.117
287	      delta: 0.065
288	      best_single_method: ACDC (14 edges)
289	      eapig_CPR: 0.078
290	      ep_CPR: 0.052
291	    advantage_ratio_mean_vs_zero: 0.813
292	    advantage_positive_both: true
293	    conclusion: CSS advantage robust across ablation methods
294	  result_rationale: 'Zero ablation 将 complement edges 的 activation 设为零，mean ablation
295	    替换为 training-set 均值。 Mean ablation 更 "温和"——保留了残余信号的均值统计特征，因此所有 CPR 值上升（CSS=1.0
296	    从 0.109→0.182， ACDC 从 0.029→0.117）。关键是 relative advantage 是否保持。 CSS=1.0 的 7 条边在
297	    mean ablation 下 CPR=0.182：这些边对应 IOI 的 functional core （name mover + S-inhibition
298	    heads），即使 complement 用均值替代（而非零化）， 这些核心边仍然承载着 IOI task 的主要 logit difference。ACDC
299	    的 14 条边在 mean ablation 下 CPR=0.117：ACDC isinf edges 质量不错但包含 7 条 non-consensus
300	    edges， 其中 2-3 条在 mean ablation 下被证明是 "zero-ablation-sensitive but functionally
301	    replaceable" ——它们在 zero ablation 下似乎重要（移除导致大破坏），但 mean ablation 表明 其功能可被残余均值信号部分补偿。
302	    Δ 从 0.080（zero）降至 0.065（mean），retained ratio = 81.3%。 CSS advantage 在两种 ablation
303	    下均为正，确认 IOI CSS PASS 不是 evaluation artifact。 这直接回应 Dream worst-tier 的核心 concern（zero
304	    ablation bias as IOI confound）。
305	
306	    '
307	  tables:
308	  - name: 'Table: IOI Ablation Method Robustness'
309	    description: '行: Zero Ablation, Mean Ablation 列: CSS=1.0 CPR, ACDC CPR, EAP-IG
310	      CPR, EP CPR, Δ(CSS vs best single) 底部: Advantage retained under mean = 81.3%
311	
312	      '
313	  figures_description:
314	  - 'Grouped bar chart: 两组 (Zero, Mean)，每组 4 bars (CSS=1.0, ACDC, EAP-IG, EP)。 CSS=1.0
315	    bar 在两组中均最高。标注 Δ 值。视觉化 CSS advantage 的 ablation-robustness。
316	
317	    '
318	  analysis: '此实验为 Appendix 提供关键 robustness check。Zero vs mean 给出 Δ=0.080 vs 0.065，
319	    CSS advantage 在两种 evaluation 下一致为正。这排除了 "CSS 仅在 destructive zero ablation 下 人为获胜"
320	    的假说，也为 future work 推荐 mean ablation 作为更温和的默认评估方式。 与 SVA 形成对比：SVA 的 CSS advantage
321	    在 zero ablation 下为负（已知）， mean ablation 下仅 Δ=0.013（non-significant by bootstrap）——
322	    进一步证实 IOI 和 SVA 的 CSS outcome 差异是 task-driven 而非 evaluation-driven。
323	
324	    '
325	- name: IFR vs ACDC vs Gradient Method Divergence Analysis
326	  plan_id: plan_012
327	  description: '系统文档化 Qwen-0.5B 上 IFR 和 ACDC 的退化机制，作为 Claim 3（component-level scoring
328	    scaling failure） 的 case study。纯分析，使用 plan_006/plan_007 已有数据，0 GPU hours。
329	
330	    '
331	  expected_results:
332	    ifr_failure_analysis:
333	      scoring_mechanism: intermediate representation cosine similarity
334	      failure_mode: GQA 的 KV sharing 使 deep-layer attention edge 的 representation
335	        变化被同组 heads 吸收
336	      selected_layer_range: layers 0-5 (early MLP→Attn routing)
337	      gradient_layer_range: layers 18-23 (deep attention heads)
338	      overlap_with_gradient: 0.0
339	      diagnosis: IFR 退化为 early-layer MLP bias detector
340	    acdc_failure_analysis:
341	      scoring_mechanism: activation patching (clean→corrupt substitution)
342	      failure_mode: 179K edges 上 node-level scoring，top-0.3% 选出 block-structured edge
343	        sets
344	      max_jaccard_with_gradient: 0.043
345	      css_3of3: 0
346	      diagnosis: ACDC 也退化为 component-level scoring，与 gradient 方法零重叠
347	    comparative:
348	      ifr_jaccard_eapig: 0.0
349	      ifr_jaccard_ep: 0.0
350	      acdc_jaccard_eapig: 0.022
351	      acdc_jaccard_ep: 0.021
352	      conclusion: 两种非 gradient 方法均因不同机制退化到 component-level，使 CSS consensus 不可能成立
353	    root_cause: 'Component-level scoring 是 architectural 问题而非 method-specific 缺陷：
354	      (1) IFR 因 GQA KV sharing 丢失 edge-level sensitivity (2) ACDC 因 179K 边的搜索空间过大退化为
355	      node-level pruning (3) Gradient 方法（EAP-IG/EP）保持 edge-level scoring 但计算成本高 三种
356	      failure 机制独立，不可通过 method substitution 修复
357	
358	      '
359	  result_rationale: '此分析整合 plan_006 (IFR, D028) 和 plan_007 (ACDC, D034) 的已有数据。 IFR
360	    的失败有明确的 architectural root cause：Qwen-2.5 使用 Grouped Query Attention (GQA)， 同组
361	    heads 共享 K/V projection。当移除一条 attention edge 时，同组其他 heads 的 KV buffer 吸收了 representation
362	    变化，IFR 的 cosine similarity 评分趋近于零。IFR 因此只选中 early-layer MLP edges（representation
363	    影响大但位于 IOI circuit 之外）。 ACDC 在 GPT-2 (32K edges) 上正常工作（isinf 给出 14 条 edge-level
364	    edges）， 但在 Qwen (179K edges) 上搜索空间过大，ACDC 的 greedy pruning 退化为 node-level 操作——
365	    每步评估整个 attention head 而非单条边，因为逐边评估 179K 边的时间成本不可接受。 结果：ACDC 选出的 edges 呈 block
366	    structure（同一 head 的所有边同时被选中或同时排除）， 与 gradient 方法的 fine-grained edge selection
367	    零重叠。 两种非 gradient 方法因完全不同的机制退化到 component-level， 使三方法 consensus 在 Qwen 上不可能成立——这是
368	    Claim 3 的 definitive evidence。
369	
370	    '
371	  tables:
372	  - name: 'Table: Method Scoring Granularity Comparison (Qwen-0.5B IOI)'
373	    description: '行: IFR, ACDC, EAP-IG, EP 列: Scoring Mechanism, Effective Granularity
374	      (edge/node/layer), Selected Layer Range, Jaccard with EAP-IG, Jaccard with EP,
375	      CPR
376	
377	      '
378	  - name: 'Table: GPT-2 vs Qwen Method Behavior'
379	    description: '行: GPT-2 Small (32K edges), Qwen-0.5B (179K edges) 列: ACDC Granularity,
380	      ACDC Edges (isinf), IFR Available, Max Pairwise Jaccard, CSS=1.0 Edges 展示 scale-dependent
381	      method degeneration
382	
383	      '
384	  figures_description:
385	  - 'Layer distribution histogram（三面板）: x=layer (0-23), y=selected edge count。 Panel
386	    1: IFR (红, 集中在 layer 0-5)。 Panel 2: Gradient methods (蓝, layer 18-23)。 Panel 3:
387	    ACDC (绿, block-structured, 集中在 3-4 个 attention heads 的全部边)。 视觉化三种方法在 Qwen 上的退化模式差异。
388	
389	    '
390	  analysis: '此 case study 为 Discussion 提供 Claim 3 的 mechanistic 证据。 核心 insight：CSS
391	    的前提是"每种方法独立地在 edge-level 提供有效评分"。 当方法退化到 component-level（IFR→layer, ACDC→node），
392	    edge-level consensus 的数学基础不成立（三种方法选出的 "edges" 实际上是不同层级的 components， 无法在边级别求交集）。
393	    这为 practitioner guidelines 增加第三条：使用 CSS 前， 验证每种方法的 scoring granularity 是否为 true
394	    edge-level。 如果 ACDC 的选边呈 block structure 或 IFR 的选边集中在窄层范围， 说明该方法已退化，应排除后再计算 consensus。
395	
396	    '
397	- name: Jaccard-CSS Diagnostic Scatter Plot + Correlation
398	  plan_id: plan_013
399	  description: '汇总全部 6 个 model×task 配置的 (max pairwise Jaccard, CSS CPR advantage)，
400	    计算 Spearman rank correlation，验证 Jaccard diagnostic（<0.35→PASS, >0.5→FAIL）的准确率。
401	    明确报告为 n=6 underpowered 但 directionally consistent。
402	
403	    '
404	  expected_results:
405	    data_points:
406	    - label: IOI (GPT-2)
407	      model: GPT-2 Small
408	      max_jaccard: 0.307
409	      css_cpr_advantage: 0.085
410	      css_pass: true
411	      diagnostic_prediction: PASS (< 0.35)
412	      diagnostic_correct: true
413	    - label: Qwen IOI (IFR)
414	      model: Qwen-0.5B
415	      max_jaccard: 0.54
416	      css_cpr_advantage: 0.0
417	      css_pass: false
418	      diagnostic_prediction: FAIL (> 0.5)
419	      diagnostic_correct: true
420	      note: IFR degeneration → all CPR≈0, CSS=1.0=0 edges
421	    - label: Factual Recall (GPT-2)
422	      model: GPT-2 Small
423	      max_jaccard: 0.62
424	      css_cpr_advantage: -0.07
425	      css_pass: false
426	      diagnostic_prediction: FAIL (> 0.5)
427	      diagnostic_correct: true
428	    - label: SVA (GPT-2)
429	      model: GPT-2 Small
430	      max_jaccard: 0.653
431	      css_cpr_advantage: 0.013
432	      css_pass: false
433	      diagnostic_prediction: FAIL (> 0.5)
434	      diagnostic_correct: true
435	      note: Bootstrap CI crosses zero → reclassified as FAIL
436	    - label: Arithmetic (GPT-2)
437	      model: GPT-2 Small
438	      max_jaccard: 0.695
439	      css_cpr_advantage: -0.063
440	      css_pass: false
441	      diagnostic_prediction: FAIL (> 0.5)
442	      diagnostic_correct: true
443	    - label: Qwen IOI (ACDC)
444	      model: Qwen-0.5B
445	      max_jaccard: 0.043
446	      css_cpr_advantage: -0.055
447	      css_pass: false
448	      diagnostic_prediction: PASS (< 0.35)
449	      diagnostic_correct: false
450	      note: Outlier — fails due to component-level scoring (Claim 3), not method correlation
451	        (Claim 4)
452	    n_data_points: 6
453	    diagnostic_accuracy: 5/6 (83.3%)
454	    diagnostic_miss_explanation: 'Qwen ACDC (max_J=0.043, FAIL) is the sole exception:
455	      low Jaccard coexists with FAIL because the failure mode is component-level scoring
456	      degeneration (Claim 3), not method correlation (Claim 4). The diagnostic correctly
457	      predicts when methods function at edge-level; it cannot predict method-degeneration
458	      failures.
459	
460	      '
461	    spearman_rho_all_6: -0.714
462	    spearman_p_all_6: 0.111
463	    spearman_rho_excluding_outlier: -0.9
464	    spearman_p_excluding_outlier: 0.037
465	    gpt2_only_4_points:
466	      spearman_rho: -1.0
467	      spearman_p: 0.042
468	      note: Perfect negative rank correlation on 4 GPT-2 tasks
469	    fitted_threshold_jaccard: 0.5
470	    threshold_interpretation: 'max pairwise Jaccard < 0.35 → CSS likely beneficial
471	      (1/1 correct). max pairwise Jaccard > 0.50 → CSS likely ineffective (4/4 correct,
472	      excluding scaling failures). Gap zone 0.35-0.50: no data points in this range,
473	      recommendation is to proceed with caution.
474	
475	      '
476	  result_rationale: '6 个配置横跨 2 个模型架构（GPT-2, Qwen）、4 个任务（IOI, Arithmetic, SVA, Factual
477	    Recall）。 在排除 Qwen ACDC outlier 后，5 个数据点的 Spearman ρ=-0.900 (p=0.037) 表明 max pairwise
478	    Jaccard 与 CSS advantage 之间存在统计显著的负相关—— method diversity 越高（Jaccard 越低），CSS consensus
479	    的 CPR advantage 越大。 包含 outlier 时 ρ=-0.714 (p=0.111)，不显著—— 因为 Qwen ACDC 的低 Jaccard
480	    + FAIL 组合严重违反了线性趋势。 但这不是 diagnostic 的缺陷，而是反映了两种独立的 failure mode： (1) Claim 4 的
481	    method-correlation failure：高 Jaccard → CSS 无效（4/4 正确预测） (2) Claim 3 的 component-level
482	    scoring failure：方法退化 → CSS 不可能成立（与 Jaccard 无关） 仅用 GPT-2 的 4 个任务时 ρ=-1.0 (perfect
483	    negative rank correlation, p=0.042)， 说明在单模型内 Jaccard diagnostic 是 perfect predictor。
484	    跨模型时 Qwen 引入了 Claim 3 的新 failure mode，使 Jaccard 不再是 sole predictor—— 这恰恰是论文需要
485	    Claim 3 + Claim 4 两个独立 claim 的原因。
486	
487	    '
488	  tables:
489	  - name: 'Table: Jaccard-CSS Diagnostic Data (Main Result, Table 3 or 4)'
490	    description: '行: 6 个 model×task 配置（按 max Jaccard 升序排列） 列: Task, Model, Methods,
491	      Max Jaccard, CSS=1.0 CPR, Best Single CPR, Δ, Diagnostic Prediction, Actual,
492	      Correct? 底部: Accuracy = 5/6。Qwen ACDC 行标注为 "scaling failure outlier"。 辅助行: Spearman
493	      ρ=-0.900 (p=0.037, excluding outlier), ρ=-0.714 (p=0.111, all 6)
494	
495	      '
496	  - name: 'Table: GPT-2 Subset (4 tasks)'
497	    description: '仅 IOI, Factual Recall, SVA, Arithmetic on GPT-2。ρ=-1.0, p=0.042。
498	      展示 within-model 的 perfect negative rank correlation。
499	
500	      '
501	  figures_description:
502	  - '核心 Figure（论文 Figure 3 或 4）: Scatter plot, x=max pairwise Jaccard, y=CSS CPR advantage
503	    (Δ)。 6 个数据点，颜色区分模型（GPT-2 蓝, Qwen 橙），形状区分结果（圆=PASS, ×=FAIL）。 灰色虚线 y=0 分隔 positive/negative
504	    region。 垂直虚线 x=0.35 和 x=0.50 标注 diagnostic thresholds。 Qwen ACDC 点（左下角,×）用虚线圈标注
505	    "scaling failure (Claim 3)"，与 regression 分开。 排除 outlier 后的 regression line 从右下到左上（负斜率）。
506	    右上角: ρ=-0.900, p=0.037 (excl. outlier)。 这是全文最重要的图——将 Claim 3 和 Claim 4 的关系浓缩为一张可视化。
507	
508	    '
509	  analysis: 'Jaccard-CSS scatter 是论文的 crown jewel figure。它同时展示了两个核心发现： (1) 在方法正常工作的
510	    5 个配置中，max Jaccard 是 CSS outcome 的强预测因子（ρ=-0.900, p=0.037） (2) Qwen ACDC outlier
511	    直观地展示了 Claim 3 的独立 failure mode 论文的 practical guideline 可以从这张图直接读出： Step 1: 验证方法
512	    scoring granularity（排除 Claim 3 failure） Step 2: 计算 max pairwise Jaccard（< 0.35
513	    proceed, > 0.50 use best single method） Claim 4 从 "motivated conjecture" 升级为 "empirically
514	    supported heuristic"—— 5/6 diagnostic accuracy + p=0.037 correlation + clear mechanistic
515	    explanation 对 n=6 的 underpowered caveat 保持诚实，但指出 within-model perfect correlation
516	    (ρ=-1.0) 和 cross-model consistency 共同支撑 heuristic 的可靠性。'
517	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d6325f7-6387-468e-81e3-7994a8c9be52",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "741d72ed-ec9d-49c4-af9b-a49f921545a5",
  "sourceToolAssistantUUID": "4d6325f7-6387-468e-81e3-7994a8c9be52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-13T10:05:46.004Z_

Now I have a thorough understanding of the paper, the project history, the existing R1 review, and the experimental data. Let me also read the worst-case paper to understand the range of possible presentations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "741d72ed-ec9d-49c4-af9b-a49f921545a5",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazP1xH7jgt6Ng7kfy47U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d789feee-fe63-43a5-8081-3647f0c40ce3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012NgqAapSjTwzqspT9PeLcB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16133,
      "cache_read_input_tokens": 61283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16133,
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

_source line 45 · 2026-05-13T10:05:48.456Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P1Bdemyf72FPRJ4xEGyXF5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T092135/worst/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d789feee-fe63-43a5-8081-3647f0c40ce3",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazP1xH7jgt6Ng7kfy47U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75b0dbe6-6a6e-4558-9646-cd243b89450c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012NgqAapSjTwzqspT9PeLcB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16133,
      "cache_read_input_tokens": 61283,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16133
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 61283,
          "cache_creation_input_tokens": 16133,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16133,
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

_source line 46 · 2026-05-13T10:05:48.462Z_

<details><summary>↩ Tool result · `toolu_01P1Bdemyf72FPRJ4xEGyXF5`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage{amsmath,amssymb}
6	\usepackage{booktabs}
7	\usepackage{graphicx}
8	\usepackage{hyperref}
9	\usepackage{xcolor}
10	\usepackage[margin=2.5cm]{geometry}
11	\usepackage{natbib}
12	\usepackage{multirow}
13	\usepackage{tablefootnote}
14	
15	\title{Binary Consensus Does Not Improve Circuit Discovery}
16	
17	\author{
18	  Anonymous Authors\\
19	  \textit{Anonymous Institution}
20	}
21	
22	\date{}
23	
24	\begin{document}
25	\maketitle
26	
27	% ============================================================
28	\begin{abstract}
29	Mechanistic interpretability increasingly relies on automated circuit discovery methods, yet different methods often identify divergent circuits for the same task. A natural response is to take the consensus --- edges agreed upon by multiple methods --- as a higher-fidelity circuit. We systematically evaluate this binary consensus strategy (CSS) across 4 tasks on GPT-2 Small and 1 task on Qwen-0.5B, using three discovery methods (EAP-IG, Edge Pruning, ACDC). Across all six task$\times$model configurations tested, CSS provides \emph{no statistically significant advantage} over the best individual method ($0/6$ significant positive $\Delta$CPR at $\alpha{=}0.05$). The sole apparent success (IOI on GPT-2) dissolves under size-controlled baselines: top-$k$ edges from any single method match or exceed CSS performance when circuit size is held constant. We identify two mechanistic failure modes: (1)~ACDC's \texttt{isinf}-based binarization collapses consensus to a single method's output, and (2)~component-level scoring granularity on models with $>$100K edges produces near-zero inter-method overlap regardless of method independence. These findings challenge the implicit assumption that multi-method agreement validates circuit quality, and suggest that the consensus-as-validation paradigm is fundamentally flawed for current circuit discovery methods.
30	\end{abstract}
31	
32	% ============================================================
33	\section{Introduction}
34	
35	Automated circuit discovery aims to identify the minimal subnetwork (circuit) within a neural network that is responsible for a specific behavior \citep{conmy2023towards,wang2023interpretability}. As multiple discovery methods have emerged --- including gradient-based attribution (EAP-IG; \citealp{syed2023attribution}), edge pruning (EP; \citealp{li2024circuit}), and ACDC \citep{conmy2023towards} --- practitioners face a fundamental question: when methods disagree, which circuit should we trust?
36	
37	An intuitive answer is \emph{consensus}: edges identified by multiple independent methods should be more reliable than those found by any single method alone. This reasoning mirrors ensemble methods in machine learning and feature selection stability analysis \citep{nogueira2016measuring,kuncheva2003measures}. In circuit discovery, binary consensus takes the intersection (or super-majority) of binarized circuit outputs from $K$ methods.
38	
39	We call this approach the \textbf{Circuit Selection by Consensus} (CSS) framework and test it systematically. Specifically, we define $\text{CSS}(\tau)$ as the set of edges receiving agreement from at least $\lceil \tau \cdot K \rceil$ methods, where $\tau \in [0, 1]$ controls the consensus threshold. At $\tau{=}1.0$ (unanimous agreement), CSS selects only edges found by all $K$ methods.
40	
41	Our results are unequivocally negative. Across six task$\times$model configurations spanning four tasks (Indirect Object Identification, Greater-Than Arithmetic, Subject-Verb Agreement, Country-Capital Factual Recall) and two models (GPT-2 Small with 32K edges, Qwen-0.5B with 179K edges), CSS at $\tau{=}1.0$ \emph{never} provides a statistically significant advantage over the best individual method. In three configurations, CSS actively \emph{hurts} performance (significantly negative $\Delta$CPR).
42	
43	We identify two distinct mechanistic failure modes that explain this universal failure:
44	
45	\begin{enumerate}
46	    \item \textbf{Binarization pathology} (\S\ref{sec:binarization}): ACDC's \texttt{isinf}-based edge scoring produces an extremely sparse binary mask (7--14 edges out of 32K), causing $\text{CSS}(\tau{=}1.0)$ to degenerate to the ACDC output alone. Consensus becomes a single-method circuit relabeled as ``multi-method agreement.''
47	
48	    \item \textbf{Component-level scoring collapse} (\S\ref{sec:scaling}): On Qwen-0.5B, both IFR and ACDC perform node-level or block-level scoring rather than edge-level discrimination. With 179K candidate edges, this produces layer-concentrated selections with zero inter-method overlap at the edge level, making consensus vacuous.
49	\end{enumerate}
50	
51	These failure modes are not implementation bugs --- they reflect structural properties of existing circuit discovery methods that make binary consensus fundamentally unsuited as a validation strategy. Our contribution is threefold: (1)~the first systematic negative evaluation of consensus in circuit discovery, (2)~mechanistic explanations for \emph{why} consensus fails, and (3)~evidence that the community's implicit assumption --- that multi-method agreement signals circuit quality --- is not supported by current methods.
52	
53	% ============================================================
54	\section{Related Work}
55	
56	\paragraph{Circuit discovery methods.}
57	Automated circuit discovery has progressed rapidly. ACDC \citep{conmy2023towards} uses activation patching with iterative pruning. EAP-IG \citep{syed2023attribution} applies integrated gradients to edge attributions. Edge Pruning \citep{li2024circuit} optimizes continuous edge masks via gradient descent. More recently, IFR extends activation patching to block-level interventions, and methods like PIE \citep{zhang2026pie} propose iterative pruning ensembles. Each method embodies different inductive biases about what constitutes a ``circuit,'' leading to divergent outputs on the same task.
58	
59	\paragraph{Multi-method consensus.}
60	The idea that agreement among methods signals reliability has roots in feature selection stability \citep{nogueira2016measuring} and ensemble diversity theory \citep{kuncheva2003measures}. \citet{mondorf2025beyond} propose cross-method score averaging as an alternative to binary consensus. CIRCUS \citep{parekh2026circus} explores within-method threshold diversity. Our work differs by providing the first systematic \emph{negative} evaluation of binary consensus in circuit discovery, with mechanistic explanations for its failure.
61	
62	\paragraph{The consensus assumption in practice.}
63	Despite the absence of formal evaluation, multi-method agreement is widely used as informal validation in interpretability research. Studies routinely report that ``our circuit is confirmed by method X'' without testing whether consensus provides performance gains. We argue this practice rests on an untested assumption that our experiments directly refute.
64	
65	% ============================================================
66	\section{Method: Circuit Selection by Consensus}
67	\label{sec:method}
68	
69	\paragraph{Notation.}
70	Let $\mathcal{M} = \{m_1, \ldots, m_K\}$ be a set of $K$ circuit discovery methods. Each method $m_k$ produces a binary circuit $C_k \subseteq \mathcal{E}$, where $\mathcal{E}$ is the set of all edges in the computational graph. We define:
71	\begin{equation}
72	    \text{CSS}(\tau) = \left\{ e \in \mathcal{E} \;\middle|\; \frac{1}{K}\sum_{k=1}^{K} \mathbf{1}[e \in C_k] \geq \tau \right\}
73	\end{equation}
74	
75	At $\tau = 1.0$, $\text{CSS}(1.0) = \bigcap_{k=1}^{K} C_k$ (unanimous consensus). At $\tau = 2/3$ with $K=3$, an edge must appear in at least 2 of 3 methods.
76	
77	\paragraph{Evaluation metric: Circuit Performance Recovery (CPR).}
78	We evaluate circuits using CPR, defined as:
79	\begin{equation}
80	    \text{CPR}(C) = 1 - \frac{L_{\text{ablated}}(C) - L_{\text{full}}}{L_{\text{random}} - L_{\text{full}}}
81	\end{equation}
82	where $L_{\text{ablated}}(C)$ is the loss when all edges \emph{not} in circuit $C$ are ablated (set to zero or mean activation), $L_{\text{full}}$ is the unablated model loss, and $L_{\text{random}}$ is the loss with a random circuit of equal size. CPR $= 1$ indicates full recovery; CPR $\leq 0$ indicates no better than random.
83	
84	\paragraph{Decision gate (D025 protocol).}
85	We define four conditions for CSS to ``pass'' on a given configuration:
86	\begin{enumerate}
87	    \item[C1:] Maximum pairwise Jaccard $< 0.70$ (methods are not trivially correlated)
88	    \item[C2:] $|\text{CSS}(\tau{\geq}2/3)| \geq 10$ (sufficient consensus edges)
89	    \item[C3:] $|\text{CSS}(1.0)| \geq 3$ (non-vacuous unanimous consensus)
90	    \item[C4:] $\text{CPR}(\text{CSS}(1.0)) > \max_k \text{CPR}(C_k)$ (consensus outperforms best single method)
91	\end{enumerate}
92	All four conditions must hold for a configuration to be deemed a CSS success.
93	
94	\paragraph{Methods.}
95	We use $K{=}3$ methods: \textbf{EAP-IG} (gradient-based edge attribution with integrated gradients), \textbf{EP} (edge pruning via continuous mask optimization), and \textbf{ACDC} (activation patching with iterative pruning). Each method produces a binarized circuit using its default thresholding strategy.
96	
97	% ============================================================
98	\section{Experimental Setup}
99	\label{sec:setup}
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75b0dbe6-6a6e-4558-9646-cd243b89450c",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "8f7850e0-1e8f-42a7-8c7c-45f6d23ab07c",
  "sourceToolAssistantUUID": "75b0dbe6-6a6e-4558-9646-cd243b89450c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-13T10:05:52.161Z_

I now have comprehensive context on both paper versions (best, median, worst), the full experimental history (decisions D001-D035), the paper framing document, and the existing R1 review. Let me now load the tool needed to submit the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f7850e0-1e8f-42a7-8c7c-45f6d23ab07c",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazP2Rq4xQNvhw4s1tsKb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8603b5ef-07a8-4b2e-b464-0b84476b798c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PbxPVMRCH4uyLgyNmUkhtC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2917,
      "cache_read_input_tokens": 77416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2917,
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

_source line 48 · 2026-05-13T10:05:53.224Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JZDjeTRnrfnMReCQqgr8fa`</summary>

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
  "parentUuid": "8603b5ef-07a8-4b2e-b464-0b84476b798c",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazP2Rq4xQNvhw4s1tsKb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f8de42d-14d9-4c79-bb6b-81b6c11d4ad2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PbxPVMRCH4uyLgyNmUkhtC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2917,
      "cache_read_input_tokens": 77416,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2917
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 77416,
          "cache_creation_input_tokens": 2917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2917,
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

_source line 49 · 2026-05-13T10:05:53.226Z_

<details><summary>↩ Tool result · `toolu_01JZDjeTRnrfnMReCQqgr8fa`</summary>

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
  "parentUuid": "2f8de42d-14d9-4c79-bb6b-81b6c11d4ad2",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "21494050-3934-4509-886a-046f05038378",
  "sourceToolAssistantUUID": "2f8de42d-14d9-4c79-bb6b-81b6c11d4ad2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-13T10:05:58.649Z_



Now I have all the context needed to write a thorough R2 review focused on Novelty and Related Work. I'll review both the "best" and "median" paper versions (since the task description matches the median version's title more closely, but the best version is the most recent reframing). The review should synthesize insights from both versions and the full experimental history.

Let me compose the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21494050-3934-4509-886a-046f05038378",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazP2nifvuLP5A1Nrx1pi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d115d25f-25f2-46bd-b064-2efe9ecc3942",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AY4PLY8o3Lr6EGciVgM3zK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 722,
      "cache_read_input_tokens": 80333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 722,
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

_source line 51 · 2026-05-13T10:07:26.628Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01Ad4dVE8pKuyk5PUgW6Kgb5`</summary>

```json
{
  "project": "structfuse-context",
  "tier": "best",
  "dream_id": "dream_20260513T092135",
  "overall_score": "Borderline Findings (2.5/5)",
  "report": "## R2 Review: Novelty and Related Work\n\n### Summary\nThe paper formalizes binary cross-method consensus (CSS) for circuit discovery, tests it across 6 model x task configurations (4 tasks on GPT-2 Small, IOI on Qwen-0.5B with two third-method variants), and finds it succeeds in only 1/6 cases. Three failure modes are identified: task-induced method correlation, component-level scoring degeneration at scale, and a Jaccard-based diagnostic for predicting failure. The paper positions itself as a \"systematic negative result\" contribution with practitioner guidelines. My review focuses on whether the novelty is sufficient for EMNLP Findings and whether the related work coverage is adequate.\n\n### Strengths\n\n1. **Honest negative-result framing is commendable.** The authors explicitly state (Section 1) that \"our contribution is not the consensus framework itself\" but the empirical characterization of failure modes. This is epistemically responsible and avoids overclaiming. The pivot from a positive-method paper to a failure-analysis paper (evident from the framing) reflects genuine intellectual honesty.\n\n2. **Failure Mode 2 (component-level scoring degeneration) is genuinely novel.** The observation that IFR degenerates to layer-level scoring due to GQA KV sharing and ACDC degenerates to node-level scoring at 179K edges is a new architectural insight. This transcends the specific CSS framework and is useful to anyone applying these methods to models beyond GPT-2 Small. The mechanistic explanation (Table 6/7 in best version) is clear and well-grounded. This is the paper's strongest novelty contribution.\n\n3. **Size-controlled baseline (Section 4.4/Table 4) is excellent experimental design.** Comparing CSS=1.0 (7 edges) against top-7 from each individual method and random-7 at identical edge counts is the right control. The 76.3% retained advantage (best version) or the near-dissolution of advantage (median version) -- either way, this is the kind of careful analysis that raises the paper's credibility. Few papers in mechanistic interpretability include this level of ablation control.\n\n4. **Statistical reporting is appropriate for the sample size.** The use of paired bootstrap CIs with BCa correction (B=10,000), the honest acknowledgment that n=6 is underpowered for the Jaccard diagnostic, and the framing of the diagnostic as a \"heuristic\" rather than a \"law\" all reflect good statistical practice. The classification of SVA as FAIL based on CI crossing zero (p=0.482) rather than point estimate is the right call.\n\n5. **The paper connects failure modes to ensemble theory conditions (Kuncheva & Whitaker 2003).** The mapping of FM1 to diversity violation, FM2 to commensurability violation, and the implicit FM3 (Jaccard diagnostic) to a testable necessary condition is a useful conceptual bridge between circuit discovery and established ensemble theory.\n\n### Weaknesses\n\n1. **CSS is not methodologically novel -- it is a direct application of the Nogueira & Brown (2016) stability index to binary edge masks.** The entire Method section (Section 3) defines CSS(e) = (1/K) * sum(m_k(e)), which is equation (1) from Nogueira & Brown applied to a different domain. The binarization step (top-N) is standard. The Jaccard diagnostic is the pairwise stability measure from the same framework. The paper acknowledges this (\"our contribution is not the consensus framework itself\"), but the consequence is that the novelty rests entirely on the empirical findings -- and at n=6 configurations with only 1 positive case, the empirical base is thin. **The question is whether \"applying a known framework to a new domain and finding it mostly doesn't work\" clears the novelty bar for EMNLP Findings.** I believe it does, but barely, and only because of the mechanistic failure mode analysis (especially FM2).\n\n2. **Insufficient engagement with Mondorf et al. (2025), the most directly comparable work.** Mondorf et al. test continuous score averaging across the same methods (EAP-IG, ACDC, and others) and report that averaging outperforms individual methods. The paper's Related Work gives them a single sentence. The critical unanswered question: does continuous averaging succeed where binary CSS fails? If yes, then the failure modes identified here are about *binarization*, not about *consensus* -- and the paper's title (\"When Does Circuit Consensus Fail?\") is misleading. The paper should either (a) test continuous averaging on at least IOI and one FAIL case as a comparative ablation, or (b) explicitly discuss why their binary-specific findings still matter given the existence of a continuous alternative that may work. The current treatment is a significant gap.\n\n3. **EAP-IG and Edge Pruning are gradient-adjacent methods, making K=3 effectively K~2.** EAP-IG computes integrated gradients of the attribution-patching objective; EP optimizes continuous edge masks via gradient descent. Both produce edge scores via gradient-based operations. The paper's own data confirms this: EAP-IG x EP consistently has the highest pairwise Jaccard (0.307 on IOI, 0.54 on Qwen, 0.62 on Factual Recall). The claim of \"three independent algorithmic families\" (gradient/mask/greedy causal) is overstated -- EP is more accurately \"gradient-based mask optimization,\" not a separate paradigm from gradient attribution. With K_effective ~ 2, the consensus framework is structurally weaker than presented. The paper should acknowledge this more explicitly and discuss whether adding a genuinely non-gradient method (e.g., probing-based circuit discovery, causal scrubbing) would change the findings.\n\n4. **The Jaccard diagnostic is underpowered and over-presented.** The Spearman rho=-0.90 (p=0.037) requires excluding the Qwen-ACDC outlier; on all 6 points, rho=-0.714 (p=0.111), which is not significant. The 0.35 and 0.50 thresholds derive from exactly 1 data point below 0.35 and 4 above 0.50, with zero in between. Any 4 points in strict monotone order yield rho=-1.0 mechanically. The paper presents Table 8 (diagnostic accuracy table) with checkmarks and cross-marks and a \"5/6 accuracy\" headline, which lends more statistical ceremony than the data warrants. The Jaccard-predictability finding is directionally plausible but should be presented as a preliminary observation (2-3 sentences), not elevated to a full subsection (Section 5.3) with its own table and as the third \"failure mode.\"\n\n5. **The failure mode taxonomy may be incomplete and partially predictable from first principles.** FM1 (task-induced method correlation -> consensus redundancy) is essentially the diversity condition from Kuncheva & Whitaker (2003) applied to circuits. Anyone familiar with ensemble theory would predict that high inter-method agreement renders consensus useless. FM2 (scoring granularity mismatch) is genuinely novel. FM3 (Jaccard diagnostic) is a restatement of \"check diversity before ensembling,\" which is standard practice. A reviewer could reasonably argue that 2 of 3 failure modes are predictable from existing theory, and only FM2 constitutes a new finding. The paper would benefit from explicitly asking: \"what failure modes are *not* predictable from ensemble theory?\" and emphasizing FM2 as the primary empirical contribution.\n\n### Questions for Authors\n\n1. **Have you tested continuous score averaging (Mondorf et al. 2025) on your configurations?** If continuous averaging succeeds where binary CSS fails, the paper's contribution narrows from \"consensus fails in circuit discovery\" to \"binary binarization-based consensus fails.\" This is a critical distinction for framing. Even a partial comparison (e.g., IOI + Arithmetic) would substantially strengthen the paper by disambiguating whether the problem is consensus or binarization.\n\n2. **For the IOI success case, could the result simply reflect that IOI has a well-characterized ground-truth circuit (Wang et al. 2023) with modular structure that makes it \"easy\" for all methods?** The 7 CSS=1.0 edges correspond to known name-mover and S-inhibition heads. Is this \"consensus identifies the right circuit\" or \"consensus identifies the obvious circuit that every method gets right?\" If the latter, the positive finding is less interesting, and the paper is really 0/6 for non-trivial cases.\n\n3. **What is the paper's position on whether the negative results generalize to K>3 or to fundamentally different method combinations (e.g., replacing EP with probing or causal scrubbing)?** The current K=3 with two gradient methods is a relatively narrow test of the consensus hypothesis. If the negative result is specific to this method combination, the contribution is more limited.\n\n### Missing Related Work / Positioning Issues\n\n**Circuit discovery methods beyond the three studied:**\n- Bhaskar et al. (2024, NeurIPS Spotlight) for Edge Pruning -- the EP citation currently points to Kramar et al. (AtP*), which appears to be a different method. This is a factual error in the bibliography that must be corrected.\n- Hanna et al. (2024, COLM) on the relationship between EAP-IG attribution overlap and circuit faithfulness -- directly relevant to the Jaccard diagnostic claim.\n- Marks et al. (2024) on sparse feature circuits, which represents a different paradigm (SAE-based) not covered by any of the three methods.\n\n**Faithfulness evaluation:**\n- Miller et al. (2024, COLM) on faithfulness metric robustness across ablation methods -- directly relevant given the paper's reliance on zero ablation and the sensitivity of results to ablation choice.\n- The paper uses zero ablation throughout (with mean ablation only as a robustness check on IOI). Miller et al. show that faithfulness rankings can flip under different ablation regimes, which the paper should cite and discuss.\n\n**Method comparison and negative results in MI:**\n- Meloux et al. (2025) on intra-method instability of EAP/EAP-IG -- relevant because high within-method variance could explain low between-method agreement.\n- Sharkey et al. (2025) \"Open Problems in Mechanistic Interpretability\" -- provides community context for why method comparison matters.\n- InterpBench (NeurIPS 2024 D&B track) -- provides standardized evaluation framework that this paper could position against.\n\n**Ensemble theory:**\n- The connection to bagging/boosting is mentioned but not developed. The paper should note that binary intersection is the *most aggressive* ensemble strategy (equivalent to unanimous voting), and that softer aggregation (e.g., majority voting at CSS>=2/3, or continuous averaging) is standard in ensemble theory precisely because intersection is known to be overly conservative. This would contextualize why binary CSS fails and whether the result is surprising.\n\n**Reference count:**\n- The paper cites only 14 references. A typical EMNLP paper in mechanistic interpretability cites 30-40. The reference list is notably sparse, particularly for the Related Work section, which is my assigned focus area. This alone is below venue standards.\n\n**CIRCUS and PIE citations:**\n- CIRCUS (Parekh et al. 2026) has an incomplete citation -- no venue, placeholder format.\n- PIE is cited as \"Anonymous\" despite having an arXiv ID (2604.16889). This should be resolved.\n\n**IFR:**\n- IFR is used in the Qwen experiments but is not formally introduced in Section 2 (Background). The citation (Zhang & Nanda 2024) is vague (\"best practices for circuit discovery\"). The reader has no information about what IFR actually computes until the failure analysis in Section 5.2.\n\n### Scores\n- Soundness: 3/5\n- Excitement: 2.5/5\n- Overall: 2.5/5\n- Confidence: 4/5\n\n### Justification\nThe paper addresses a real question (does cross-method consensus improve circuit discovery?) with honest methods and arrives at a useful negative answer. The component-level scoring degeneration finding (FM2) is genuinely novel and practically valuable. However, the combination of (a) thin methodological novelty (CSS is a known stability index), (b) insufficient engagement with the most directly comparable work (Mondorf et al. continuous averaging), (c) an underpowered Jaccard diagnostic elevated beyond what the data supports, (d) only 14 references in a field where 30+ is standard, and (e) two of three failure modes being predictable from existing ensemble theory places this at the borderline of Findings acceptability. The paper could reach a clear 3.0 (Findings accept) with targeted revisions: test or substantively discuss continuous averaging, expand references to 25+ with genuine engagement, and rebalance the presentation to emphasize FM2 as the primary novel contribution while downweighting the Jaccard diagnostic."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d115d25f-25f2-46bd-b064-2efe9ecc3942",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazP2nifvuLP5A1Nrx1pi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33a813bd-44b0-4851-9e1a-5e2aab0582c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AY4PLY8o3Lr6EGciVgM3zK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 722,
      "cache_read_input_tokens": 80333,
      "output_tokens": 3316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 722
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3316,
          "cache_read_input_tokens": 80333,
          "cache_creation_input_tokens": 722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 722,
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

_source line 52 · 2026-05-13T10:07:30.231Z_

<details><summary>↩ Tool result · `toolu_01Ad4dVE8pKuyk5PUgW6Kgb5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T092135/best/review_report.md\", \"dream_id\": \"dream_20260513T092135\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33a813bd-44b0-4851-9e1a-5e2aab0582c4",
  "isSidechain": true,
  "promptId": "8fe71e72-1736-4520-b3be-9632609cd9ae",
  "agentId": "a2e2c736423f4c4fe",
  "type": "user",
  "uuid": "67d0ebfb-2412-4123-8f05-ec42aa590cdc",
  "sourceToolAssistantUUID": "33a813bd-44b0-4851-9e1a-5e2aab0582c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-13T10:07:40.356Z_

The R2 review has been submitted. Here is a summary of the key findings:

**Overall Score: Borderline Findings (2.5/5)**

**Core assessment:** The paper addresses a legitimate question with honest methods and identifies one genuinely novel finding (component-level scoring degeneration at scale), but falls short in several areas critical for Novelty and Related Work evaluation.

**Key strengths identified:**
- FM2 (scoring degeneration due to GQA KV sharing and node-level ACDC collapse) is genuinely novel and transcends the paper's framework
- Size-controlled baseline is excellent experimental design
- Statistical reporting is honest and appropriately calibrated to the sample size
- The negative-result framing is epistemically responsible

**Key weaknesses identified:**
1. CSS is a direct application of Nogueira & Brown (2016) stability index -- zero methodological novelty
2. Critical gap: no engagement with Mondorf et al. (2025) continuous averaging, which may succeed where binary CSS fails -- this potentially reduces the contribution from "consensus fails" to "binarization fails"
3. K=3 is effectively K~2 because EAP-IG and EP are both gradient-based
4. Jaccard diagnostic is underpowered (n=6, p=0.111 on full data) but presented with disproportionate statistical ceremony
5. Two of three failure modes are predictable from standard ensemble theory (Kuncheva & Whitaker 2003)
6. Only 14 references versus the 30-40 typical for this venue; multiple citation errors (EP cites AtP* instead of Bhaskar et al. 2024)

**Path to 3.0 (Findings accept):** Test or substantively discuss continuous averaging, expand references to 25+, rebalance presentation to emphasize FM2 as primary contribution, and downweight the Jaccard diagnostic.

The review was saved to `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T092135/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67d0ebfb-2412-4123-8f05-ec42aa590cdc",
  "isSidechain": true,
  "agentId": "a2e2c736423f4c4fe",
  "requestId": "req_011CazP9vkojdwimY6XD8L7K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fea4046-8e52-4ff3-a226-3bc60fe86063",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "f2e9568a-8920-4443-b16c-735005e3494c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DrU1581jNmA3366kyi53BE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3445,
      "cache_read_input_tokens": 81055,
      "output_tokens": 494,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3445
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 494,
          "cache_read_input_tokens": 81055,
          "cache_creation_input_tokens": 3445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3445,
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
