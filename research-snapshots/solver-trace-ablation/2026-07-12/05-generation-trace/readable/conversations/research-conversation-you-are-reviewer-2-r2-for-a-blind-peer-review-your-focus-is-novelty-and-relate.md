# Research conversation: You are Reviewer 2 (R2) for a blind peer review. Your focus is **Novelty and Related Work**. ## Venue & Scoring Rubric (

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a801083aee3377eeb.jsonl`
- **Structured JSON:** [`5e278c8a71e715e38098.json`](../../sessions/5e/5e278c8a71e715e38098.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

53 recorded events

### User

_source line 1 · 2026-05-13T09:56:17.166Z_

You are Reviewer 2 (R2) for a blind peer review. Your focus is **Novelty and Related Work**.

## Venue & Scoring Rubric (EMNLP 2026 via ARR)

Use these scales (0.5 increments):
- **Soundness** (1-5): 5=Exceptional, 4=Strong (sufficient support for all claims), 3=Acceptable (sufficient for main claims), 2=Poor (main claims not sufficiently supported), 1=Major issues
- **Excitement** (1-5): 5=Highly exciting, 4=Exciting, 3=Interesting, 2=Potentially interesting, 1=Not exciting
- **Overall** (1-5): 5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle
- **Reproducibility** (1-5): 5=Easily reproducible, 4=Mostly reproducible, 3=Some difficulty, 2=Difficult, 1=Cannot reproduce
- **Confidence** (1-5): 5=Positive my evaluation is correct, 4=Quite sure, 3=Pretty sure, 2=Willing to defend but may have missed details, 1=Not my area

## Paper Summary

**Title:** "When Does Circuit Consensus Fail? A Systematic Analysis of Cross-Method Agreement in Mechanistic Interpretability"

The paper formalizes a "Circuit Selection Score" (CSS) — the fraction of K=3 circuit discovery methods (EAP-IG, EP, ACDC) selecting each edge — and tests whether high-consensus edges (CSS=1.0) outperform individual methods. Evaluated across 4 tasks × 2 models = 6 configurations. Central finding: consensus succeeds in only 1/6 cases (IOI on GPT-2).

Three failure modes:
1. Task-induced method correlation (bottleneck tasks force convergence → high Jaccard → consensus just selects obvious edges)
2. Component-level scoring degeneration (Qwen-0.5B: IFR→layer-level due to GQA KV sharing; ACDC→node-level due to 179K edge search space)
3. Jaccard-predictable failure (max pairwise Jaccard > 0.5 predicts failure, 5/6 accuracy, ρ=−0.90)

Practical guidelines: (1) verify each method operates at edge-level granularity, (2) compute pairwise Jaccard before investing in multi-method validation (>0.50 → use best single method).

## Related Work Section (from paper §2)

The paper cites:
- **Circuit discovery methods**: EAP-IG [Syed et al. 2023], EP [Kramár et al. 2024], ACDC [Conmy et al. 2023], IFR [Zhang & Nanda 2024]
- **Ensemble approaches**: Feature selection stability [Nogueira & Brown 2016], ensemble diversity [Kuncheva & Whitaker 2003], CIRCUS [Parekh et al. 2026] (within-method threshold diversity), continuous score averaging [Mondorf et al. 2025], PIE [Anonymous 2026] (iterative pruning ensembles)
- **Evaluation**: CPR/CMD from [Conmy et al. 2023]
- **Tasks**: IOI circuit [Wang et al. 2023], Factual associations [Meng et al. 2022]
- **Models**: GPT-2 [Radford et al. 2019], Qwen [Bai et al. 2023]

Total: 14 references.

## Your Review Focus (Novelty + Related Work)

Evaluate:
1. **Novelty of contribution**: Is CSS genuinely new or just a formalization of something obvious? Is the "negative result" sufficiently insightful? Do the failure mode analyses provide new understanding?
2. **Positioning relative to prior work**: 
   - Mondorf et al. 2025 ("Comparing circuit discovery methods") — how does this paper differ? Is the comparison adequate?
   - CIRCUS (Parekh et al. 2026) — within-method threshold diversity vs cross-method consensus. Is the distinction clear?
   - PIE (Anonymous 2026) — pruning ensembles. Overlapping territory?
3. **Missing related work**: Are there important works not cited? Consider:
   - Other consensus/ensemble methods in interpretability
   - Broader feature selection literature
   - Other circuit evaluation beyond CPR/CMD
   - Multi-method comparisons in XAI more broadly
4. **Scope of claims vs evidence**: With n=6 configurations, 2 models, 4 tasks — are the claims appropriately scoped? The "empirically supported heuristic" framing for Jaccard diagnostic — sufficient?
5. **Significance for the community**: Will practitioners actually use these guidelines? Does this change how people do circuit discovery?
6. **Related work completeness**: Only 14 references for an EMNLP paper — is this enough? Missing important citations?

## Output Format

Provide your review in this structure:
```
## R2 Review: Novelty & Related Work

### Summary (2-3 sentences)

### Strengths
- S1: ...
- S2: ...
- S3: ...

### Weaknesses
- W1: ...
- W2: ...
- W3: ...

### Questions for Authors
- Q1: ...
- Q2: ...

### Minor Issues
- ...

### Scores
- Soundness: X/5
- Excitement: X/5
- Overall: X/5
- Reproducibility: X/5
- Confidence: X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "d50b9c71-b791-42fc-be4c-af5439f8fdc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T09:56:17.169Z_

```json
{
  "parentUuid": "d50b9c71-b791-42fc-be4c-af5439f8fdc3",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
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
  "uuid": "f1558ba1-a7a8-408e-9330-81ce12f7af9c",
  "timestamp": "2026-05-13T09:56:17.169Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T09:56:19.634Z_



I'll start by reading the paper and related materials to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1558ba1-a7a8-408e-9330-81ce12f7af9c",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNJK6LgB7d5YPnET7yr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65c602f8-8b4e-44c1-8255-c9190fb73044",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GAuqmhEd4Zj6W16Ch8TKXk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7221,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7221,
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

_source line 4 · 2026-05-13T09:56:21.145Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017ZewYmGdDDer8FrZReZjtM`</summary>

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
  "parentUuid": "65c602f8-8b4e-44c1-8255-c9190fb73044",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNJK6LgB7d5YPnET7yr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8d950d8-e605-4ce4-aac9-5a68d9bc895c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GAuqmhEd4Zj6W16Ch8TKXk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7221,
      "cache_read_input_tokens": 8249,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7221
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 123,
          "cache_read_input_tokens": 8249,
          "cache_creation_input_tokens": 7221,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7221,
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

_source line 5 · 2026-05-13T09:56:21.148Z_

<details><summary>↩ Tool result · `toolu_017ZewYmGdDDer8FrZReZjtM`</summary>

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
  "parentUuid": "b8d950d8-e605-4ce4-aac9-5a68d9bc895c",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "9e9d42db-f047-4479-8a30-472a8d61c21e",
  "sourceToolAssistantUUID": "b8d950d8-e605-4ce4-aac9-5a68d9bc895c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-13T09:56:23.682Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01H54A9XNxQtXXEezhetZhnQ`</summary>

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
  "parentUuid": "9e9d42db-f047-4479-8a30-472a8d61c21e",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNJc6XmSHNnU9myVKnG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7865af0-ef45-4215-9c0c-07df86af4066",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019J3fC97RNBrcrvhBkEZX7Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1445,
      "cache_read_input_tokens": 15470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1445,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

_source line 7 · 2026-05-13T09:56:23.729Z_

<details><summary>↩ Tool result · `toolu_01H54A9XNxQtXXEezhetZhnQ`</summary>

```text
{"result":"# 项目 structfuse-context 概况\n\n## 实验状态 (10 个)\n\n- **gpt2_factual_recall_k3_v2**: RUNNING — \n- **gpt2_factual_recall_k3**: DONE (failed) — \n- **mvp_sva_gpt2_k3_topk**: DONE (negative) — \n- **phase2_qwen05b_ioi_acdc_k3**: DONE (negative) — \n- **mvp_sva_gpt2_k3**: DONE (negative) — \n- **phase2_qwen05b_ioi_k3**: DONE (negative) — \n- **mvp_arithmetic_gpt2_k3**: DONE (negative) — \n- **mvp_pilot_gpt2_ioi_v3**: DONE (success) — \n- **mvp_pilot_gpt2_ioi_v2**: DONE (failed) — \n- **mvp_pilot_gpt2_ioi**: DEPLOYED (killed) — \n\n## 最新报告\n# Handover — 2026-05-13\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| gpt2_factual_recall_k3_v2 | — | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **gpt2_factual_recall_k3** (failed): Factual Recall (国家首都) 上 CSS=1.0 faithfulness > single-method，GPT-2 第四任务验证（D025 条件④, plan_005）\n- **mvp_sva_gpt2_k3_topk** (negative): SVA 上 CSS=1.0 faithfulness > single-method（ACDC top-100 修正版，westd-pro6000 cuda:1）\n  [sva_css067_fix_results](/api/workspace-files/projects/structfuse-context/artifacts/mvp_sva_gpt2_k3_topk/data/sva_css067_fix_results.txt)\n- **phase2_qwen05b_ioi_acdc_k3** (negative): —\n\n## 趋势\n成功 1 / 负向 5 / 失败 2 / 共 8\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-39279: 无 GPU 信息\nwestd-pro6000: 空闲 cuda:0, cuda:1\n\n## 告警\n- mvp_pilot_gpt2_ioi_v2: 训练失败 — unknown\n- gpt2_factual_recall_k3: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7865af0-ef45-4215-9c0c-07df86af4066",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "3cb4c464-1e04-49b4-880a-7c1b99738af9",
  "sourceToolAssistantUUID": "a7865af0-ef45-4215-9c0c-07df86af4066",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-13T09:56:24.310Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0137Eq3nicR1JbqFXByHFEXc`</summary>

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
  "parentUuid": "3cb4c464-1e04-49b4-880a-7c1b99738af9",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNJc6XmSHNnU9myVKnG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c630ea4-7c0a-46e1-8ba7-7cfd2f5320af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019J3fC97RNBrcrvhBkEZX7Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1445,
      "cache_read_input_tokens": 15470,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1445
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 160,
          "cache_read_input_tokens": 15470,
          "cache_creation_input_tokens": 1445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1445,
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

_source line 9 · 2026-05-13T09:56:24.319Z_

<details><summary>↩ Tool result · `toolu_0137Eq3nicR1JbqFXByHFEXc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/report.md\", \"content\": \"# Handover — 2026-05-13\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| gpt2_factual_recall_k3_v2 | — | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **gpt2_factual_recall_k3** (failed): Factual Recall (国家首都) 上 CSS=1.0 faithfulness > single-method，GPT-2 第四任务验证（D025 条件④, plan_005）\\n- **mvp_sva_gpt2_k3_topk** (negative): SVA 上 CSS=1.0 faithfulness > single-method（ACDC top-100 修正版，westd-pro6000 cuda:1）\\n  [sva_css067_fix_results](/api/workspace-files/projects/structfuse-context/artifacts/mvp_sva_gpt2_k3_topk/data/sva_css067_fix_results.txt)\\n- **phase2_qwen05b_ioi_acdc_k3** (negative): —\\n\\n## 趋势\\n成功 1 / 负向 5 / 失败 2 / 共 8\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-39279: 无 GPU 信息\\nwestd-pro6000: 空闲 cuda:0, cuda:1\\n\\n## 告警\\n- mvp_pilot_gpt2_ioi_v2: 训练失败 — unknown\\n- gpt2_factual_recall_k3: 训练失败 — unknown\\n\", \"total_chars\": 870, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c630ea4-7c0a-46e1-8ba7-7cfd2f5320af",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "2586dd9e-a52f-4431-8a65-6864ef29ad03",
  "sourceToolAssistantUUID": "5c630ea4-7c0a-46e1-8ba7-7cfd2f5320af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-13T09:56:27.083Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019wd8CLdqqMFm22h7uVvZWM`</summary>

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
  "parentUuid": "2586dd9e-a52f-4431-8a65-6864ef29ad03",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNJqqH9UGWbR1fZcUUE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0fae1cd9-db55-4464-8e79-4a06681da207",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115vEKHMB37k2NuM91KzBen",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1683,
      "cache_read_input_tokens": 16915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1683,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 11 · 2026-05-13T09:56:27.092Z_

<details><summary>↩ Tool result · `toolu_019wd8CLdqqMFm22h7uVvZWM`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fae1cd9-db55-4464-8e79-4a06681da207",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "dabdb136-42c8-4f67-94df-e6d94f11332b",
  "sourceToolAssistantUUID": "0fae1cd9-db55-4464-8e79-4a06681da207",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-13T09:56:27.557Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012eB6A3RQ67BXFFDwS5GJ3C`</summary>

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
  "parentUuid": "dabdb136-42c8-4f67-94df-e6d94f11332b",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNJqqH9UGWbR1fZcUUE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1393f96-78ce-4aee-9f04-a90a714359f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115vEKHMB37k2NuM91KzBen",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1683,
      "cache_read_input_tokens": 16915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1683,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 13 · 2026-05-13T09:56:27.565Z_

<details><summary>↩ Tool result · `toolu_012eB6A3RQ67BXFFDwS5GJ3C`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/memory.md\", \"content\": \"# Memory — structfuse-context\\n\\n## GPU 越界教训 (2026-05-13)\\n\\n第三次 GPU 越界事件：PID 897752 占用 cuda:0（属于 rl-active-probe-fl），导致对方数据丢失。根因：旧进程或直接运行库模块时未设 CUDA_VISIBLE_DEVICES，torch 默认使用 cuda:0。\\n\\n**硬规则**：\\n- 项目只有 cuda:5@cqa1-21977，所有 .py 文件（含库模块）必须在 import torch 前用 `os.environ.setdefault(\\\"CUDA_VISIBLE_DEVICES\\\", \\\"5\\\")` 防护\\n- 入口脚本用 `os.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = \\\"5\\\"`（强制覆盖），库模块用 `setdefault`（不覆盖入口已设的值）\\n- Worker 提交实验必须用 submit_training_job（自动管理 CUDA_VISIBLE_DEVICES），禁止 nohup\\n\\n## ACDC isinf 退化——核心方法论问题 (2026-05-13)\\n\\nACDC binarization 用 `isinf` 只选出极少边（IOI 14, Arithmetic 17），但 ACDC 实际有 0.03-0.09 四级中间分数。isinf 导致 CSS=1.0 与 ACDC 完全重合，跨方法共识退化。top-k binarization（k=50-75）解决此问题：Arithmetic CSS 3/3 从 17→44-54。\\n\\n**但 top-k 未翻转条件④**：CSS=1.0 mean CPR=0.919 < EAP-IG=0.985。\\n\\n## D021: CSS-only 叙事 (2026-05-13)\\n\\n放弃 CIRCUS 作为独立 claim。转 CSS-only 叙事。\\n\\n## 竞争定位：CSS vs CIRCUS (2026-05-13)\\n\\n- **CIRCUS (Parekh, 2026)** 最大竞争对手。CSS 差异化 = method diversity > threshold diversity\\n- **Mondorf et al.** direct competitor：仅 gradient 族、score averaging（非 binary consensus）\\n- 关键支撑：Miller et al. (COLM 2024) faithfulness 对消融敏感；Méloux et al. EAP/EAP-IG 高方差\\n\\n## D026: MVP Gate 最终结论 (2026-05-13)\\n\\n**Arithmetic 条件④ FAIL（CSS=1.0 < EAP-IG），IOI PASS。**\\n\\n关键教训：\\n1. **Zero ablation 是 artifact 源**——所有小电路 zero CPR 为负，mean ablation 翻正到 0.9+\\n2. **节点级 ablation 的局限**——CSS=1.0 CPR 在 k=50→75 不变（节点集相同，边数变化无法区分）\\n3. **EAP-IG×EP 在 arithmetic 上 Jaccard=0.695**——两方法高度一致，CSS 缺少第三方视角的信息增益\\n4. **IOI 上 CSS 边效率极高**——14 edges CPR≈50 edges 单方法，每条边贡献远超单方法\\n5. **IOI CPR 不一致是误报**——mean_ablation_results.json 中标注为 IOI 的数据实际是 Arithmetic\\n\\n**等待 Director 决策：edge-efficiency claim / 原 claim + 更多任务 / pivot。**\\n\\n## IFR 作为第三方法——已证伪 (2026-05-13)\\n\\n**phase2_qwen05b_ioi_k3 (negative)**: Qwen-2.5 0.5B 上 IFR 与 EAP-IG/EP 的 Jaccard = 0.00。\\n\\n**D028 诊断结论**:\\n1. **Per-head 分解无效**: IFR 已经在用 per-head 分解，不是修复方向\\n2. **根本原因**: IFR (proximity) 度量 activation magnitude → 偏向高幅度 MLP 输出 (m2, m20, m22)；gradient 方法度量 causal influence → 偏向任务关键 attention heads (a20.h9)。两者解构的是不同维度\\n3. **Jaccard sweep**: 首次非零在 N=500 (J=0.045)，unique_score_rank 展开到 2191 边也仅 J=0.065\\n4. **Destination-side 退化 100%**: 同层头共享 residual stream，所有头得到相同 destination score\\n\\n**结论**: IFR 不能作为 CSS 第三方法用于大模型。gradient 族内部仍有共识（EAP-IG×EP Jaccard=0.54）。Phase 2 需要替代第三方法（ACDC top-k 或另一个 gradient 方法）。\\n\", \"total_chars\": 2263, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1393f96-78ce-4aee-9f04-a90a714359f1",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "9dc0b314-82fa-44a6-8dae-12fa9291f6ee",
  "sourceToolAssistantUUID": "c1393f96-78ce-4aee-9f04-a90a714359f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-13T09:56:28.493Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PiPPLxbMQPBnTjpAbhip3P`</summary>

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
  "parentUuid": "9dc0b314-82fa-44a6-8dae-12fa9291f6ee",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNJqqH9UGWbR1fZcUUE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "827c090a-641e-4b91-97fb-6c3bf2e07a0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115vEKHMB37k2NuM91KzBen",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1683,
      "cache_read_input_tokens": 16915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1683,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 15 · 2026-05-13T09:56:28.504Z_

<details><summary>↩ Tool result · `toolu_01PiPPLxbMQPBnTjpAbhip3P`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "827c090a-641e-4b91-97fb-6c3bf2e07a0b",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "814ba17c-b3bc-4637-bafc-307f51489aaa",
  "sourceToolAssistantUUID": "827c090a-641e-4b91-97fb-6c3bf2e07a0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-13T09:56:28.843Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01EytuDHa41vVk89qzbaT9gU`</summary>

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
  "parentUuid": "814ba17c-b3bc-4637-bafc-307f51489aaa",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNJqqH9UGWbR1fZcUUE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b9900d5-33a0-4557-aae5-6e30063cbf54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115vEKHMB37k2NuM91KzBen",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1683,
      "cache_read_input_tokens": 16915,
      "output_tokens": 378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1683
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 378,
          "cache_read_input_tokens": 16915,
          "cache_creation_input_tokens": 1683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1683,
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

_source line 17 · 2026-05-13T09:56:28.852Z_

<details><summary>↩ Tool result · `toolu_01EytuDHa41vVk89qzbaT9gU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — structfuse-context\\n\\n> 最后更新: 2026-05-13 | 更新原因: D034 后 reframe 为分析论文（Route A）\\n\\n## Target Venue\\nEMNLP 2026 Findings (ARR deadline 2026-05-25)\\n\\n## Core Insight\\nCross-method binary consensus in circuit discovery fails more often than it succeeds. Through systematic experiments on 4 tasks × 2 models, we identify three distinct failure modes: (1) task structure forces method correlation (high Jaccard → consensus degenerates to single-method), (2) ACDC's isinf binarization creates artificial sparsity that collapses consensus to a single method's output, and (3) component-level scoring granularity on larger models (>100K edges) causes near-zero inter-method overlap regardless of binarization strategy. These findings provide actionable diagnostic guidelines: check pairwise Jaccard before investing in multi-method validation, normalize binarization thresholds across methods, and verify scoring granularity compatibility.\\n\\n## Narrative Arc\\n1. Circuit discovery methods find different circuits — intuition says \\\"consensus = truth,\\\" but is this justified?\\n2. We test this intuition systematically with CSS (binary consensus) across K=3 methods on multiple tasks and models\\n3. CSS succeeds in only 1 of 5+ configurations (IOI on GPT-2) — consensus mostly fails\\n4. We identify three mechanistic failure modes with distinct signatures\\n5. Negative results + failure mode taxonomy = actionable practitioner guidelines\\n\\n## Core Claims\\n\\n### Claim 1: ACDC isinf binarization pathology (METHODOLOGICAL — strongest)\\n- **Evidence**: CSS=1.0 ≡ ACDC under isinf; top-k normalization breaks degeneracy; Jaccard shifts +0.16 to +0.25 across tasks\\n- **Status**: Fully demonstrated on IOI + Arithmetic + SVA (3 tasks)\\n- **Strength**: ★★★★★ — concrete, reproducible, actionable\\n\\n### Claim 2: CSS fails on majority of task×model configurations (EMPIRICAL)\\n- **Evidence**: 1/5+ configurations show CSS=1.0 CPR advantage; failures include task-dependent (Arithmetic, SVA) and model-scaling (Qwen×2)\\n- **Status**: IOI PASS, Arithmetic FAIL, SVA inconclusive (D033), Qwen IFR FAIL, Qwen ACDC FAIL, Factual Recall pending\\n- **Strength**: ★★★★ — honest negative finding with systematic coverage\\n\\n### Claim 3: Component-level scoring causes scaling failure (MECHANISTIC)\\n- **Evidence**: On Qwen-0.5B (179K edges), both IFR and ACDC degenerate to node-level scoring; top-0.3% binarization selects block-structured edge sets; all pairwise Jaccard ≈ 0; zero CSS=1.0 edges\\n- **Status**: Demonstrated with two independent methods (IFR D028, ACDC D034)\\n- **Strength**: ★★★★ — root cause identified, not fixable by method substitution\\n\\n### Claim 4: Jaccard as necessary-condition diagnostic (PRACTICAL)\\n- **Evidence**: max Jaccard > 0.5 → CSS never helps (3/3 cases); max Jaccard < 0.35 → CSS helps (1/1 case, IOI); gap zone 0.35-0.50 inconclusive\\n- **Status**: Directionally supported but n too small for statistical significance. Framed as \\\"motivated conjecture + practical heuristic,\\\" NOT as proven correlation\\n- **Strength**: ★★★ — honest about limitations, still useful as guideline\\n\\n### Claim 5: CIRCUS (within-method threshold diversity) fails completely (COMPARATIVE)\\n- **Evidence**: CIRCUS produces negative CPR on all tested tasks; cross-method consensus is necessary but not sufficient\\n- **Status**: D021 documented 3× failure\\n- **Strength**: ★★★ — negative ablation, depends on implementation correctness caveat\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1: \\\"This is just a negative result, what's the contribution?\\\"\\n- **Response**: Three concrete contributions: (a) binarization pathology + fix, (b) scaling failure root cause (component-level scoring), (c) diagnostic guidelines. Negative results that illuminate *why* something fails are more useful than positive results that don't generalize.\\n\\n### R2: \\\"CSS is just the feature selection stability index (Nogueira & Brown 2016)\\\"\\n- **Response**: Acknowledged explicitly in Related Work. Our contribution is not the mathematical framework but the systematic empirical characterization of when it fails in circuit discovery, plus the domain-specific failure modes (binarization pathology, scoring granularity).\\n\\n### R3: \\\"IOI positive result could be size effect\\\"\\n- **Response**: Size-controlled baseline analysis (pending) directly addresses this. If confirmed as artifact, strengthens the negative finding narrative.\\n\\n### R4: \\\"Only GPT-2 Small + Qwen 0.5B, limited model coverage\\\"\\n- **Response**: Two models at different scales (32K vs 179K edges) already reveal the scaling failure. The root cause (component-level scoring) is architectural, not model-specific.\\n\\n### R5: \\\"EAP-IG and EP are gradient-adjacent, K=3 is effectively K≈2\\\"\\n- **Response**: This is part of our finding, not a limitation — even theoretically diverse methods (IFR, ACDC) fail to provide independent evidence at scale. Method correlation is structural, not accidental.\\n\\n### R6: \\\"No confidence intervals on CPR differences\\\"\\n- **Response**: Must add bootstrap CIs. IOI advantage of +0.08 needs statistical validation.\\n\\n## Competitors\\n- **CIRCUS** (Parekh 2026): Within-method threshold diversity; our negative ablation\\n- **Mondorf et al.** (2510.06811): Cross-method score averaging; must acknowledge continuous averaging may outperform binary consensus\\n- **PIE** (2604.16889): Iterative pruning ensemble; single paradigm\\n- **Nogueira & Brown** (JMLR 2016): Feature selection stability; CSS is domain application, must cite\\n- **Kuncheva & Whitaker** (2003): Ensemble diversity theory; theoretical foundation for our failure mode analysis\\n\", \"total_chars\": 5555, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b9900d5-33a0-4557-aae5-6e30063cbf54",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "d72a9898-a479-4b0b-b525-aa13e476d959",
  "sourceToolAssistantUUID": "7b9900d5-33a0-4557-aae5-6e30063cbf54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-13T09:56:33.362Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UvtNxvq2pbf8Aix2BxnJfV`</summary>

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
  "parentUuid": "d72a9898-a479-4b0b-b525-aa13e476d959",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNKBD6gsUgkABZ9TRFF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c27b6d6-d1b9-4a87-ae56-a3eeb2093b11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQMGGHR8yzxv8umkTSbsK6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3904,
      "cache_read_input_tokens": 18598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3904,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 19 · 2026-05-13T09:56:33.372Z_

<details><summary>↩ Tool result · `toolu_01UvtNxvq2pbf8Aix2BxnJfV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/decisions.yaml\", \"content\": \"_next_id: 36\\ndecisions:\\n- id: D001\\n  date: 2026-05-12 09:57 UTC\\n  summary: MVP 定义为 pre-registered pilot：GPT-2 Small/IOI 上 K=4 方法 CSS + CIRCUS cross-tabulation\\n  rationale: 'IDEA_BRIEF 已定义 pilot 为第一个计算里程碑（~2h），直接检验核心假设\\\"方法类 artifact 可被二值共识检测\\\"。Pass\\n    criterion: ≥10% CIRCUS-core 边落入 off-diagonal cell。该 pilot 同时也是论文 Section 3 的 motivating\\n    result，失败则需 reframe 为 Findings track。选择此 MVP 因为：(1) 成本极低（~2h 单卡）(2) 直接验证核心假设 (3)\\n    结果直接决定投稿策略。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-12 09:59 UTC\\n  summary: 定义 MVP gate 灰区规则：5-10% off-diagonal → Findings + 追加第二组 task 验证\\n  rationale: 'Reviewer warning: 5%-10% 灰区无决策规则。决定：5-10% 默认走 Findings track，但在 GPT-2\\n    Small / Arithmetic 上追加验证。若第二组 ≥10% → 升级回 Main；若第二组也 5-10% → 确认 Findings；若第二组 <5%\\n    → 评估是否 IOI 特有现象。同时要求 MVP 报告包含 CIRCUS-core 绝对边数 + binomial 95% CI，若 CIRCUS-core\\n    <30 条边则必须追加第二组 task。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-12 09:59 UTC\\n  summary: 定义项目级 kill criteria：off-diagonal <2% + ΔF 无统计差异 → kill\\n  rationale: 'Reviewer warning: 缺项目级 kill criteria。决定：off-diagonal <2% across GPT-2\\n    Small 两个 task (IOI + Arithmetic) AND 四种电路 ΔF 无统计显著差异 (bootstrap p>0.05) → kill\\n    project。单一 task <2% 不触发 kill，需两组确认。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D004\\n  date: 2026-05-12 09:59 UTC\\n  summary: MVP 通过后增加 K=3 checkpoint：Qwen-2.5 0.5B / IOI 快速验证\\n  rationale: 'Reviewer warning: 3/4 模型用 K=3 + family constraint，但 pilot 仅测 K=4。决定：MVP\\n    通过后、全量实验前，增加 Qwen-2.5 0.5B / IOI 的 K=3 快速检查（EAP-IG + AtP* + Edge Pruning，~数小时）。若\\n    K=3 family constraint 下 off-diagonal 完全消失（<2%），需重新评估大模型贡献——可能论文仅限 K=4 结果或需要调整\\n    family constraint 定义。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D005\\n  date: 2026-05-12 10:08 UTC\\n  summary: AtP* 无 edge-level 实现：MVP 改为 K=3（EAP-IG+Edge Pruning+ACDC），大模型方案待评估\\n  rationale: 'Reviewer critical: AtP* 官方未开源，社区版仅 node-level。影响：(1) GPT-2 Small 原 K=4\\n    降为 K=3，但 EAP-IG+EP+ACDC 恰好覆盖 3 个算法族（gradient/mask/greedy causal），实际更干净；(2) 大模型原\\n    K=3 降为 K=2（仅 EAP-IG+EP），CSS 退化为平凡二值投票，严重削弱贡献。决策：MVP 用 K=3（3族）推进，同时评估大模型第三方法：(a)\\n    AtP* 自行实现可行性（≤1天）(b) PAHQ 加速 ACDC 到大模型的可行性 (c) MIB 其他 edge-level 方法的算法族分类。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D006\\n  date: 2026-05-12 10:28 UTC\\n  summary: 大模型 K=3 第三方法确定为 IFR，论文采用 triangulation 框架定位\\n  rationale: Agent 评估三条路径：(a) AtP* 自实现仍是 gradient 族，不解决 K=2 仅 2 族问题 (b) PAHQ 加速 ACDC\\n    不可行 (c) MIB 方法中 IFR 唯一满足\\\"非 gradient、非 mask optimization、edge-level、可扩展到 8B\\\"。Reviewer\\n    确认 IFR 为最佳选项，但指出 IFR 是非因果方法（度量激活空间 proximity 而非因果贡献）。采纳 Reviewer 建议：论文定位 IFR 为\\n    triangulation 中的\\\"independent signal\\\"而非\\\"causal validator\\\"——若一条边同时被因果方法 + 优化方法 +\\n    相似度方法识别，作为机制组件的证据更强。GPT-2 Small（3 因果方法）vs 大模型（2 因果 + 1 非因果）的 CSS 语义差异须在论文中诚实披露。\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-12 12:11 UTC\\n  summary: GPU 越界事故：kill 越界进程 + 修复 CUDA_VISIBLE_DEVICES + 重跑 MVP\\n  rationale: 'Reviewer critical: 项目进程跑到 cuda:0/cuda:1（白名单仅 cuda:5），L1 红线违规。原因推测为 Agent\\n    重启进程时未设 CUDA_VISIBLE_DEVICES=5。处置：立即 kill + 修复启动脚本加入 GPU 硬检查 + cuda:5 上重跑。ACDC\\n    71.5% 进度丢失。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D008\\n  date: 2026-05-12 13:02 UTC\\n  summary: MVP 结果解读协议：mask_gradient proxy 下 ≥10% 可信（保守估计），<10% 需 L0 EP 重测\\n  rationale: 当前 MVP 实际为 2 族（EAP-IG + mask_gradient 同属 gradient，+ ACDC greedy causal），非\\n    3 族。同族方法更易同意 → off-diagonal 偏低。因此：≥10% 是保守估计（真实跨族分歧可能更大），gate pass 可信；<10% 不直接判\\n    fail，需部署 L0 EP 到服务器重测 IOI 后再做 gate 判定。Phase 2 全量实验无论如何必须换 L0 EP。\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n  - D007\\n- id: D009\\n  date: 2026-05-12 17:01 UTC\\n  summary: 修复边名格式不匹配 critical bug：统一 EAP-IG 和 EP/ACDC 的边名归一化到同一 canonical form\\n  rationale: Reviewer 发现 _normalize_eap_edge 产出 dash 分隔符 + m0 格式，_normalize_ac_edge\\n    产出 arrow 分隔符 + mlp 0 格式，导致 css.py 字符串匹配完全失败，所有 CSS 值和 off_diagonal_pct 无效。修复方案：统一\\n    canonical form + 转换已有缓存，不重跑 discovery。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi\\n    role: affected\\n    result: CSS 结果因边名 bug 无效，需修复后重算\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-12 18:40 UTC\\n  summary: Phase 2 IFR binarization策略：用 percentile threshold 或 unique-score-rank 替代\\n    top-N，避免 layer-block voting 偏差\\n  rationale: Reviewer 审查发现 IFR run_ifr() 对同一 (src, dst_layer) 的所有 head×QKV 赋相同 proximity\\n    score（residual-stream proximity 固有局限），导致每对产生 36 条同分边。CSS binarize_scores 的 top-N\\n    模式下少数 (src,layer) 对即可 block-vote 占满配额，与 EAP-IG/EP 的 per-edge 粒度系统性不匹配，可能人为膨胀/压缩\\n    off-diagonal。不影响 MVP（MVP 不含 IFR），Phase 2 集成时需：(1) 改用 percentile threshold 或 unique-score-rank\\n    binarization (2) 论文披露 IFR layer-block 粒度 vs 其他方法 edge 粒度差异。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n- id: D011\\n  date: 2026-05-12 19:13 UTC\\n  summary: EP HF 后端需重构：从 layer pre-hook 改为 submodule-level hooks（q_proj/k_proj/v_proj/mlp\\n    各自 hook），修复 MLP mask 未应用 + Q/K/V 聚合两个问题\\n  rationale: Reviewer 发现 EP HF 实现有两个 warning：(1) MLP edge mask 参数参与 backward 但 forward\\n    无 hook 应用，MLP score 不可信；(2) 同一 (src, layer) 的所有 Q/K/V edge mask 被 mean 聚合为单标量，丢失\\n    per-edge 粒度。两个问题使 EP 退化为 layer-level masking。修复方案：将 hook 从 layer pre-hook 下沉到\\n    q_proj/k_proj/v_proj/mlp submodule level，每个 submodule 独立 hook 并应用对应 edge mask。这在\\n    HF hook 框架内可行，不需要重写 forward pass。若不修复，Phase 2 K=3 中 EP+IFR 都是 approximate，CSS\\n    edge-level 共识叙事被削弱。\\n  related_experiments: []\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-12 22:19 UTC\\n  summary: Reviewer 洞察：cross-tabulation（CIRCUS×CSS → 2×2 矩阵）应作为论文核心 novelty claim，而非仅\\n    CSS 填补 gap\\n  rationale: Reviewer 审查 related_work_notes.md 指出：CIRCUS（intra-method stability）×\\n    CSS（cross-method consensus）的系统组合产生 stable_core / method_specific 分类，这个 cross-tabulation\\n    在现有文献中无人做过。比单独宣称 CSS 新颖性更强。同时记录：(1) GPT-2 Small K=3 中 EAP-IG+EP 同为 gradient-adjacent\\n    需在论文中论证 optimization 差异；(2) 2025-2026 引用需 reference-audit 验证；(3) Phase D faithfulness\\n    评估必须证明 stable_core 优于 single-method circuit。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n  - D008\\n- id: D013\\n  date: 2026-05-12 22:24 UTC\\n  summary: CIRCUS 实现 bug：1D percentile sweep 产生嵌套电路，退化为 top-k。MVP v3 不中断（结果仍有信息量），Phase\\n    2 必须修复为 2D non-nested grid\\n  rationale: Reviewer 发现 circus.py 用 np.linspace percentiles 产生严格嵌套 C(t_low)⊇C(t_high)，违反\\n    CIRCUS 原文 non-nesting 约束。退化后 stability=1.0 core = top-9.1% 边（B=10），失去 config-bagging\\n    统计意义。MVP v3 cross-tabulation 仍测试 CSS vs score-ranking 一致性，gate 判定可用，故不中断。Phase\\n    2 须改为 2D grid（node threshold × edge threshold）或 random-subset 采样实现 non-nesting。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: affected\\n    result: running, results still informative despite CIRCUS degradation\\n  depends_on:\\n  - D012\\n- id: D014\\n  date: 2026-05-12 23:04 UTC\\n  summary: 论文 framing 校准：4-cell taxonomy 为核心 novelty，contribution statement 弱化避免全称量词，Phase\\n    D 增加 method_specific/cross_unstable 独立评估\\n  rationale: Reviewer 深度评估确认：(1) CIRCUS×CSS cross-tabulation 在文献中无先例，novelty 成立；(2)\\n    当前 statement 过强——\\\"any\\\" 全称量词和 \\\"distribution shift\\\" claim 缺实验支撑，需弱化；(3) 4-cell taxonomy\\n    是最强贡献点，但必须实证 4 个 cell 有不同 faithfulness 特性；(4) Phase D 需增加 method_specific 和 cross_unstable\\n    独立 CPR/CMD 评估；(5) OOD 评估（ioi_variant）应提至 priority 2；(6) D013 CIRCUS 修复已完成，Phase\\n    2 用修复版本。faithfulness 必须满足：CPR(stable_core) ≥ 0.8×CPR(best_single_method) 且 |stable_core|\\n    < |best_single_method| 且优于纯 CSS 和纯 CIRCUS。\\n  related_experiments: []\\n  depends_on:\\n  - D012\\n  - D013\\n- id: D015\\n  date: 2026-05-12 23:04 UTC\\n  summary: Framing 调整：claim 降级删除全称量词和 OOD claim；Phase D 必须增加 method_specific + cross_unstable\\n    独立 faithfulness 评估；MVP 后首检 4-cell cardinality\\n  rationale: Reviewer 两轮一致评估：(1) \\\"any single-method\\\" 全称量词超出 1 模型×1 任务实验覆盖；(2) \\\"distribution\\n    shift\\\" 无 OOD 数据支撑；(3) 4-cell taxonomy 是文献空白（novelty 成立），但需实证 4 个 cell 各有不同特性——当前\\n    Phase D 只评 stable_core，缺 method_specific/cross_unstable 独立评估；(4) D008 风险：gradient-adjacent\\n    方法可能压缩 method_specific cell。暂定 claim：\\\"competitive or superior faithfulness with\\n    fewer edges\\\"。OOD claim 推 Phase 2。\\n  related_experiments: []\\n  depends_on:\\n  - D012\\n  - D013\\n  - D008\\n- id: D016\\n  date: 2026-05-12 23:09 UTC\\n  summary: 更正：D013 CIRCUS config_bag nonnesting 修复未实际完成。Agent 产出为 Phase 2 前置代码（L0\\n    EP + IFR），远程 circus.py 零改动。另发现 L0 EP per-layer 粒度问题，Phase 2 前必须修复\\n  rationale: Reviewer 审查 worker 产出发现：(1) 远程 circus.py 仍为 1D percentile nesting，config_bag()\\n    未改动，Agent 报告的\\\"17 测试通过\\\"与实际不符；(2) 新增 edge_pruning_l0.py 的 mask 粒度为 (src, dst_layer)，所有\\n    head×QKV 共享同一值，与 EAP-IG per-edge 粒度不一致。Phase 2 三方法中两个（L0 EP + IFR）退化为 layer-level，CSS\\n    edge-level 共识叙事不成立。两项均为 Phase 2 启动前必修。\\n  related_experiments: []\\n  depends_on:\\n  - D013\\n  - D011\\n  - D010\\n- id: D017\\n  date: 2026-05-12 23:14 UTC\\n  summary: CRITICAL：CIRCUS-CSS 作用域不匹配导致 off-diagonal 结构性膨胀 ~98%，v3 cross-tabulation\\n    无效。需统一 edge universe 后重算\\n  rationale: Reviewer 发现 CIRCUS 在全量 32491 边上操作（core≈2953 条），CSS 在三方法二值化电路并集（~150 条）上操作，20\\n    倍作用域差距。CIRCUS-core 中不在二值化电路的边自动 CSS=0 → method_specific≈2893 条 → off-diagonal≈98%，为测量\\n    artifact。同时 EP binarization 用 score>0.5 对 mask_gradient 输出无意义（梯度分数非 [0,1]），导致\\n    EP 选边极少（~20-50 条）。修复方向：(1) 统一 edge universe 为三方法二值化电路并集，CIRCUS 只在此并集内操作；(2) EP\\n    改为 top-N 或 percentile binarization；(3) gate KILL 改为 KILL_CANDIDATE（D003 要求两 task）。v3\\n    原始 scores 可复用，无需重跑。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: invalidated_analysis\\n    result: raw data valid, cross-tabulation invalid due to scope mismatch\\n  depends_on:\\n  - D013\\n  - D016\\n  - D008\\n- id: D018\\n  date: 2026-05-13 01:26 UTC\\n  summary: MVP gate 条件性 PASS_MAIN：off-diagonal 13.3% ≥ 10%，但 CIRCUS-core=15 < 30 触发\\n    D002，需 Arithmetic task 确认\\n  rationale: K=3 corrected 分析（修复 ACDC binarization 后）：off-diagonal 2/15=13.3%，点估计过\\n    ≥10% 线 → PASS_MAIN。但 95% CI [1.7%, 40.5%] 横跨所有 gate 区间，统计功效不足。D002 明确规定 core <\\n    30 时必须追加第二 task 验证。同时 CSS ≥ 2/3 对已知 IOI 12-edge 电路 recall=1.0 是强正面信号，说明 cross-method\\n    consensus 确实能捕捉真实电路结构。Pairwise Jaccard（EAP-IG×ACDC=0.096, EP×ACDC=0.086）在文献典型范围内，证实方法间存在真实分歧。EAP-IG×EP=0.307\\n    偏高（gradient-adjacent），Phase 2 切 L0 EP 后预期改善。决策：暂定 PASS_MAIN，待 Arithmetic task\\n    确认后正式通过 MVP gate。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: primary\\n    result: off-diagonal 13.3%, CSS recall=1.0, conditional PASS\\n  depends_on:\\n  - D001\\n  - D002\\n  - D008\\n- id: D019\\n  date: 2026-05-13 01:32 UTC\\n  summary: 补充 gate criterion：Arithmetic 不仅看 off-diagonal %，还需验证 CSS faithfulness >\\n    single-method faithfulness 排序\\n  rationale: Reviewer 指出 CIRCUS-core 自身 CPR 为负（-0.108），说明 CIRCUS stability 与功能重要性不相关，off-diagonal\\n    % 作为唯一 gate 指标解释力不足。但 faithfulness 排序 CSS=3/3 (0.110) > CSS≥2/3 (0.063) > ACDC\\n    (0.029) > single-method (负值) 清晰支撑核心论点\\\"跨方法共识 → 更高质量电路\\\"。决定：Arithmetic gate 判定同时要求\\n    (1) off-diagonal 存在（>0%，证明方法特异性 artifact 存在）(2) CSS faithfulness > best single-method\\n    faithfulness（证明 consensus 的功能价值）。两条都满足 → PASS_MAIN；只满足一条 → 评估是否 task-specific；都不满足\\n    → 重新评估方向。同时要求 Arithmetic Phase D 使用 mean ablation 作为 zero ablation 的对比，排除 ablation\\n    方式的影响。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: evidence\\n    result: faithfulness ranking supports CSS > single-method\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: planned\\n    result: pending - must verify both off-diagonal + faithfulness ordering\\n  depends_on:\\n  - D018\\n  - D002\\n- id: D020\\n  date: 2026-05-13 01:34 UTC\\n  summary: 'CRITICAL: stable_core faithfulness 三重 FAIL，暂停 MVP pass 判定。根因是 D013 CIRCUS\\n    退化未修复——stable_core CPR=-0.187 远差于 CSS≥0.67 (CPR=+0.063)。必须先修复 CIRCUS (2D non-nested\\n    grid) 再重评。'\\n  rationale: Reviewer 深度验证发现：(1) stable_core IOI recall 仅 0.17 (2/12)，因为 CIRCUS-core\\n    系统性选中 Negative Name Mover 通路而非核心 IOI 正向信号边；(2) 这是 D013 CIRCUS 1D percentile →\\n    top-k EAP-IG 退化的直接后果；(3) CSS≥0.67 单独就达到 12/12 IOI recall + 正向 CPR，说明 cross-tabulation\\n    的\\\"附加价值\\\"目前为负；(4) D018 条件性 pass (off-diagonal 13.3%) 在 faithfulness 硬伤未修复前无效。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: evidence\\n    result: stable_core CPR=-0.187, IOI recall=0.17; CSS≥0.67 CPR=+0.063, recall=1.00\\n  depends_on:\\n  - D018\\n  - D013\\n  - D014\\n- id: D021\\n  date: 2026-05-13 02:07 UTC\\n  summary: 放弃 CIRCUS 作为独立 claim，转 CSS-only 叙事。CIRCUS 三次修复均失败，降级为 negative ablation\\n  rationale: CIRCUS 经历三轮修复全部失败：(1) D013 发现 1D percentile 嵌套退化为 top-k；(2) D020 stable_core\\n    faithfulness 三重 FAIL；(3) random-subset fix 后 stable_core CPR=-0.023, IOI recall=0/12，比旧版更差。根本问题是\\n    faithfulness-based stability scoring 在当前 circuit 粒度下无法产出有意义的 stable core。ARR DDL\\n    剩 12 天，不能再投入时间调试。CSS off-diagonal 13.3% 已过 gate，CSS-only 叙事足够支撑论文。CIRCUS 失败作为\\n    negative ablation 保留（\\\"structural consensus > faithfulness scoring\\\"），反而强化 CSS 的\\n    claim。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: evidence\\n    result: CSS off-diagonal 13.3% pass, but CIRCUS stable_core triple fail\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: ongoing\\n    result: Arithmetic validation running, independent of CIRCUS\\n  depends_on:\\n  - D020\\n  - D018\\n  - D013\\n- id: D022\\n  date: 2026-05-13 02:11 UTC\\n  summary: 紧急处理第三次 GPU 越界事件：杀 PID 897752 + 根因排查 + 强制 CUDA_VISIBLE_DEVICES=5\\n  rationale: Manager 报告进程 PID 897752 (17GB, 100% util) 越界占用 cuda:0（属于 rl-active-probe-fl\\n    项目），已导致对方代码和数据丢失。这是 cqa1-21977 上第三次越界事件，Manager 警告再犯将回收 GPU。根因待 Agent 排查（CUDA_VISIBLE_DEVICES\\n    未正确设置或被覆盖）。要求所有后续实验脚本开头强制 export CUDA_VISIBLE_DEVICES=5。\\n  related_experiments:\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: suspected_source\\n    result: 疑似越界进程来源，待确认\\n  depends_on: []\\n- id: D023\\n  date: 2026-05-13 02:18 UTC\\n  summary: 澄清 D021 与 D002 灰区关系：Arithmetic 实验 gate 统一为 CSS off-diagonal ≥5%，D002 的\\n    5-10% 灰区规则不再适用\\n  rationale: D002 原定义基于 CIRCUS-core edges：≥10% PASS_MAIN，5-10% 灰区走 Findings track。D021\\n    已从 CIRCUS 转向 CSS-only，指标体系变化，原灰区阈值不再有意义。Arithmetic 实验 gate 统一为 CSS off-diagonal\\n    ≥5% = PASS（确认跨任务泛化性），<5% = FAIL。D002 的 5-10% 灰区规则被 D021 显式 deprecate。\\n  related_experiments:\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: gate_experiment\\n    result: running\\n  depends_on:\\n  - D002\\n  - D021\\n- id: D024\\n  date: 2026-05-13 02:18 UTC\\n  summary: D021 覆盖 D002 灰区定义：arithmetic CSS off-diagonal ≥5% 即为 PASS，不再区分灰区\\n  rationale: D002 原定 5-10% 为灰区（走 Findings track），≥10% 为 PASS_MAIN。D021 pivot 为 CSS-only\\n    后将 arithmetic gate 改为 ≥5%。Reviewer 指出两者语义冲突。决定：D021 显式覆盖 D002 的灰区规则。理由：CSS-only\\n    pivot 后 off-diagonal 的意义更明确（纯 consensus 信号），5% 阈值已足够表明 cross-method structural\\n    agreement 非 task-specific。D002 的 5-10% 灰区基于 CIRCUS+CSS 混合框架下的不确定性，该前提已不存在。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n  - D021\\n- id: D025\\n  date: 2026-05-13 03:14 UTC\\n  summary: 更新 Arithmetic gate 为 CSS-only 四条件标准（替代 D024 的单一 5% 阈值）\\n  rationale: Reviewer 审查发现：(1) run_arithmetic.py 代码仍跑 CIRCUS cross-tabulation + D002\\n    旧阈值，D024 未落地到代码；(2) CIRCUS 已知 broken（D013 nesting + D017 scope mismatch），基于 CIRCUS\\n    的 off-diagonal % 无意义。采纳 Reviewer 建议的 CSS-only 四条件 gate：① Pairwise Jaccard 任意方法对\\n    < 0.70 ② CSS ≥2/3 edge count ≥ 10 ③ CSS = 1.0 edge count ≥ 3 ④ CSS faithfulness\\n    > single-method（D019）。四条全满足 = PASS。实验不中断（ACDC 75%+），结果出来后忽略代码 gate_verdict，人工按新标准判定。\\n  related_experiments:\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: target\\n    result: RUNNING\\n  depends_on:\\n  - D024\\n  - D021\\n  - D019\\n- id: D026\\n  date: 2026-05-13 03:39 UTC\\n  summary: Arithmetic D025 gate FAIL（条件④），暂不判 MVP 结果，先做 ACDC 阈值 ablation + mean ablation\\n    诊断\\n  rationale: Arithmetic CSS=1.0 CPR=-0.197 < EAP-IG CPR=-0.142，条件④失败。但 Reviewer 同时发现两个方法论问题：(1)\\n    ACDC isinf 仅保留 17 边，与 EAP-IG/EP 各 100 边形成 6:1 不对称，CSS=1.0 退化为纯 ACDC 输出；(2) 所有小电路\\n    CPR 均为负，zero ablation 可能对 Greaterthan 过于苛刻。这两个问题在 IOI 上同样存在但被正结果掩盖。在排除 binarization\\n    artifact 和 ablation method artifact 之前，不应判定 CSS 方法论失败。诊断方案：(a) ACDC top-k 阈值 sweep（k=50/100/150，CPU\\n    分析，不需新 GPU 实验）；(b) mean ablation 替代 zero ablation 重算 Phase D。两者均可在已有 raw scores\\n    上快速完成。\\n  related_experiments:\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: primary\\n    result: D025 gate FAIL (condition ④)\\n  depends_on:\\n  - D025\\n  - D019\\n- id: D027\\n  date: 2026-05-13 04:37 UTC\\n  summary: MVP 最终判定：CSS faithfulness 优势 task-dependent（IOI PASS / Arithmetic FAIL），不\\n    kill，reframe claim scope\\n  rationale: Arithmetic D025 条件④在 2 ablation × 4 k = 8 个配置下全部 FAIL，排除了 isinf 退化和 zero\\n    ablation artifact。IOI 在 zero ablation 下一致 PASS（k=isinf/50/100 均通过）。CSS 不是普遍优于单方法，而是在\\n    localized-circuit 任务（IOI 有明确的 Name Mover 等组件）上有效，在 distributed-computation 任务（Greaterthan）上无效。D003\\n    kill criteria 未触发（两任务 off-diagonal 均 >2%）。方向决策：(1) 不 kill 项目 (2) Reframe：从\\\"CSS\\n    always better\\\"转为\\\"CSS identifies faithful consensus when circuits are localized;\\n    reveals task structure when they're not\\\" (3) 补 1-2 个任务建立 localized vs distributed\\n    模式 (4) 这个发现本身比 universal claim 更有学术价值——审稿人更 appreciate nuanced finding。\\n  related_experiments:\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: primary\\n    result: FAIL (condition ④ across all 8 configs)\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: reference\\n    result: PASS (consistent across k and ablation)\\n  depends_on:\\n  - D026\\n  - D025\\n  - D021\\n- id: D028\\n  date: 2026-05-13 07:31 UTC\\n  summary: Phase 2 IFR 零重叠问题：暂停 Qwen/Gemma 新实验，先修 IFR per-head 分解 + 调 binarization\\n    比例\\n  rationale: Qwen-0.5B IOI K=3 实验显示 IFR×EAP-IG Jaccard=0.000, IFR×EP Jaccard=0.000，CSS=1.0=0\\n    条边。根因是 D010 已标记的 IFR layer-block voting：同层所有 head×QKV 共享 score，top-100 选出的边与 per-head\\n    方法完全正交。附加问题：179K 边取 top-100=0.06%，远低于 GPT-2 的 0.3%。两个修复方向并行验证：(1) ifr_scoring.py\\n    的 _decompose_per_head() 分解每头输出；(2) 改用 proportional binarization top-0.3%（~538\\n    边）。修复验证前暂停 Qwen/Gemma 新实验。SVA（GPT-2 + ACDC）不受影响，继续跑。\\n  related_experiments:\\n  - exp_id: phase2_qwen05b_ioi_k3\\n    role: primary\\n    result: CSS=1.0=0 edges, IFR zero overlap\\n  depends_on:\\n  - D027\\n- id: D029\\n  date: 2026-05-13 07:59 UTC\\n  summary: Phase 2 第三方法：放弃 IFR，改用 ACDC top-k。IFR 跨族分歧作为 Discussion finding。\\n  rationale: D028 两项诊断均失败：(1) per-head 分解已在使用，IFR 根本性偏向 MLP/early layers 而 gradient\\n    方法偏向 attention/late layers；(2) proportional binarization 到 3.5%（~6000 edges）才出现\\n    1 条 CSS=1.0 边。IFR×gradient Jaccard 结构性为零，不是调参能解决。ACDC top-k 是唯一已验证的跨族方法（GPT-2\\n    上与 gradient 有合理重叠）。计算成本高（30min-2h vs 1s）但 96GB 卡可承受。不选 AtP 因为与 EAP-IG/EP 同为 gradient\\n    族（K≈2 问题不解决）。IFR×gradient 分歧本身是有价值的 finding，放入论文 Discussion。\\n  related_experiments:\\n  - exp_id: phase2_qwen05b_ioi_k3\\n    role: evidence\\n    result: IFR zero overlap confirmed\\n  depends_on:\\n  - D028\\n- id: D030\\n  date: 2026-05-13 08:01 UTC\\n  summary: SVA D025 gate FAIL（zero FAIL / mean 边际 Δ=0.008）；发现 css_0.67 评估 bug 影响所有历史实验\\n  rationale: SVA GPT-2 K=3 (ACDC top-100) 结果：zero ablation CSS=1.0 CPR=-0.703 < EAP-IG=-0.348（FAIL）；mean\\n    ablation CSS=1.0 CPR=1.180 vs ACDC=1.172（Δ=0.008，噪声范围，无统计意义）。跨任务 pattern 确认：CSS=1.0\\n    faithfulness 优势仅在 IOI+GPT-2 + zero ablation 下成立（1/3 任务）。另发现 css_0.67 评估 bug：css_0.67\\n    实际在评估 css_1.0 的边集（阈值过滤逻辑错误），影响所有历史实验的 css≥0.67 数据。需立即修复后重评。\\n  related_experiments:\\n  - exp_id: mvp_sva_gpt2_k3_topk\\n    role: primary\\n    result: condition④ FAIL (zero) / marginal PASS (mean Δ=0.008)\\n  depends_on:\\n  - D027\\n  - D025\\n- id: D031\\n  date: 2026-05-13 08:04 UTC\\n  summary: 统一 D025 条件④标准：zero PASS 或 mean Δ≥0.01，SVA 两次均判 negative；修正 cqa1 registry\\n  rationale: Reviewer 发现 cqa1 SVA (conclusion=success) 与 westd SVA (conclusion=negative)\\n    对同一 pattern（zero FAIL + mean Δ=0.006）给出矛盾判定。统一标准：条件④要求 (a) zero ablation CSS >\\n    best single-method，或 (b) mean ablation CSS > best single-method 且 Δ ≥ 0.01。Δ=0.006/0.008\\n    在单 seed 单次运行下无统计意义（ACDC 跨硬件差异本身就有这个量级）。两次 SVA 均判 negative。cqa1 registry 需修正 conclusion=negative。\\n  related_experiments:\\n  - exp_id: mvp_sva_gpt2_k3\\n    role: primary\\n    result: corrected to negative\\n  - exp_id: mvp_sva_gpt2_k3_topk\\n    role: reference\\n    result: negative confirmed\\n  depends_on:\\n  - D030\\n  - D025\\n- id: D032\\n  date: 2026-05-13 08:12 UTC\\n  summary: 'D032: 条件④评估指标修正——必须用 css_1.00 而非 css_0.67'\\n  rationale: Reviewer 发现 D025 条件④定义为 \\\"CSS=1.0 > best single-method\\\"，但实际评估代码检查了 css_0.67\\n    的 CPR。这是一个与 css_0.67 filtering bug 相关但独立的问题：即使 css_0.67 的边集计算正确，条件④也应该用 css_1.00\\n    的 CPR。westd SVA 数据：css_1.00 mean CPR=1.1873 vs ACDC=1.1746, Δ=0.0127≥0.01（D031\\n    门槛），可能从 negative 翻转为 marginal PASS。需要 Agent 在 css_0.67 bug 修复后，用 css_1.00 重新跑条件④判定。\\n  related_experiments:\\n  - exp_id: mvp_sva_gpt2_k3_topk\\n    role: re-evaluate\\n    result: westd css_1.00 Δ=0.0127, pending re-evaluation\\n  - exp_id: mvp_sva_gpt2_k3\\n    role: invalidate\\n    result: cqa1 isinf + css_0.67 bug, conclusion unreliable → negative\\n  depends_on:\\n  - D031\\n  - D030\\n  - D025\\n- id: D033\\n  date: 2026-05-13 08:30 UTC\\n  summary: 'D033: SVA 判定降级为 inconclusive——单 seed Δ=0.013 不具鲁棒性'\\n  rationale: D032 将 westd SVA 从 negative 改为 success（css_1.00 Δ=0.0127≥0.01）。但 Reviewer\\n    指出：(1) cqa1 同任务/模型/seed Δ=0.006<0.01 仍为 negative，(2) 两台服务器结论分裂是 ACDC 硬件不确定性导致，(3)\\n    论文不能 cherry-pick 一台的结果。跨服务器平均 Δ=(0.013+0.006)/2=0.0095<0.01。因此 SVA 整体判定为 inconclusive/marginal，不计入\\n    clear success。论文中需如实报告两台结果并注明 marginal。当前真实成绩：IOI clear PASS, SVA inconclusive,\\n    Arithmetic FAIL。\\n  related_experiments:\\n  - exp_id: mvp_sva_gpt2_k3_topk\\n    role: downgrade\\n    result: success → inconclusive (Δ=0.013 not robust)\\n  - exp_id: mvp_sva_gpt2_k3\\n    role: context\\n    result: negative (Δ=0.006, same task different server)\\n  depends_on:\\n  - D032\\n  - D031\\n- id: D034\\n  date: 2026-05-13 08:37 UTC\\n  summary: 'D034: Qwen ACDC 确认 CSS 跨模型 scaling 根本性失败——问题不在方法选择而在模型规模'\\n  rationale: D029 将 IFR 替换为 ACDC top-0.3%，结果与 IFR 版本相同：CSS=1.0=0 边，所有 pairwise Jaccard≈0。关键发现：(1)\\n    ACDC 在 Qwen 上退化为 node-level scoring（与 IFR block-voting 同一问题），(2) 相同 binarization\\n    比例（0.3%），GPT-2(32k边) Jaccard=0.09-0.69 vs Qwen(179k边) Jaccard=0.00-0.04，差一个数量级，(3)\\n    单方法 faithfulness 也极低（EP CPR=0.055）。结论：CSS 跨模型 scaling 失败是结构性的，不可通过换方法修复。当前真实成绩：IOI\\n    GPT-2 明确 PASS，其余全部 FAIL 或 inconclusive。原 paper framing（CSS 作为正向方法贡献）不再可行。\\n  related_experiments:\\n  - exp_id: phase2_qwen05b_ioi_acdc_k3\\n    role: primary\\n    result: CSS=1.0=0 edges, all Jaccard≈0, FAIL\\n  - exp_id: phase2_qwen05b_ioi_k3\\n    role: context\\n    result: IFR version also 0 CSS=1.0 edges\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: contrast\\n    result: GPT-2 IOI PASS, same methods work at 32k scale\\n  depends_on:\\n  - D029\\n  - D025\\n- id: D035\\n  date: 2026-05-13 09:21 UTC\\n  summary: 'D035: Reframe 为分析论文 Route A — \\\"When Does Cross-Method Consensus Fail in\\n    Circuit Discovery?\\\" 目标 EMNLP Findings'\\n  rationale: Dream 三档结果（best 2/6 Reject, median/worst 3/6 Weak Reject）+ 实际实验结果（1/5\\n    PASS，Qwen scaling 根本性失败）共同表明：(1) 正向方法贡献论文不可行——即使 best case 也被 reject，(2) CSS =\\n    feature selection stability index，原框架有致命新颖性问题。Route A 将叙事从\\\"提出 CSS 方法\\\"转为\\\"系统性分析\\n    cross-method consensus 的失败模式\\\"：ACDC binarization pathology（三档一致最强贡献）、component-level\\n    scoring scaling failure、method correlation diagnostics。目标降为 EMNLP Findings。paper_framing.md\\n    和 experiment_plan.yaml 已更新。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: lone positive\\n    result: CSS PASS, but size confound pending\\n  - exp_id: phase2_qwen05b_ioi_acdc_k3\\n    role: scaling failure\\n    result: zero CSS=1.0 edges, node-level degeneration\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: task-dependent failure\\n    result: high Jaccard → CSS degenerates\\n  depends_on:\\n  - D034\\n  - D033\\n  - D029\\n\", \"total_chars\": 22880, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c27b6d6-d1b9-4a87-ae56-a3eeb2093b11",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "54772b1a-3109-4ec5-8a63-ae5782991e6b",
  "sourceToolAssistantUUID": "0c27b6d6-d1b9-4a87-ae56-a3eeb2093b11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-13T09:56:33.632Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DNtRJjqVPFzcBqrT8Qu9HN`</summary>

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
  "parentUuid": "54772b1a-3109-4ec5-8a63-ae5782991e6b",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNKBD6gsUgkABZ9TRFF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84b7b0bd-8e01-4cf3-bb2e-37e1e0c54b54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQMGGHR8yzxv8umkTSbsK6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3904,
      "cache_read_input_tokens": 18598,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3904
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 18598,
          "cache_creation_input_tokens": 3904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3904,
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

_source line 21 · 2026-05-13T09:56:33.640Z_

<details><summary>↩ Tool result · `toolu_01DNtRJjqVPFzcBqrT8Qu9HN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/ROADMAP.md\", \"content\": \"# structfuse-context — Research Dashboard\\n\\n> 最后更新: 2026-05-13 UTC | 更新原因: 更新当前进展与近期任务（IOI PASS_MAIN, Arithmetic 运行中）\\n\\n## 核心方向\\n跨方法二值共识（CSS）用于鲁棒电路编辑：证明 binary stability scoring + family-agreement constraint 在分布偏移下优于 score averaging 和单方法电路。\\n\\n## 当前进展\\n- **阶段**: MVP 验证 — IOI 已 PASS_MAIN（off-diagonal 13.3%），Arithmetic 确认实验运行中\\n- **核心假设**: CSS off-diagonal ≥5%（D021 CSS-only gate，D024 覆盖 D002）\\n- **基础设施**: cqa1-21977 (cuda:5, RTX 4090D) 已配置\\n- **大模型方案已定 (D006)**: IFR 作为第三方法，triangulation 框架定位\\n- **目标**: EMNLP 2026 Main（ARR deadline 2026-05-25，剩余 12 天）\\n\\n## 方法配置\\n| 模型 | K | 方法 | 算法族 |\\n|------|---|------|--------|\\n| GPT-2 Small | 3 | EAP-IG + Edge Pruning + ACDC | gradient / mask / greedy causal |\\n| Qwen-2.5 0.5B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |\\n| Gemma-2 2B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |\\n| Llama-3.1 8B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |\\n\\n论文需披露：GPT-2 Small CSS = 3 因果方法共识；大模型 CSS = 2 因果 + 1 相似度方法共识（triangulation）。\\n\\n## MVP Gate 规则（D001-D003）\\n| off-diagonal % | 决策 |\\n|---|---|\\n| ≥10% | → Main track |\\n| 5-10% | → Findings + 追加 Arithmetic 验证 |\\n| 2-5% | → Findings 确认 |\\n| <2% (两组) + ΔF 无差异 | → Kill |\\n\\n## 阶段规划\\n\\n### Phase 1: MVP pilot（当前）\\n- GPT-2 Small / IOI，K=3（3 因果族），~2h → off-diagonal 判定\\n\\n### Phase 2: K=3 checkpoint + 全量 CSS（MVP 后 ~3天）\\n- Qwen-2.5 0.5B / IOI K=3（含 IFR）快速检查\\n- 全 4 模型 × 4 任务 CSS 计算\\n- 确认 Edge Pruning 实现：princeton-nlp/edge-pruning（非 auto-circuit mask gradient）\\n\\n### Phase 3: OOD editing（~4天）\\n### Phase 4: 分析 + 写作（~3天，最迟 5月22日）\\n\\n## 近期任务\\n- [ ] 等待 mvp_arithmetic_gpt2_k3 完成 → gate 判定\\n- [ ] Gate PASS 后 complete_mvp → 进入 research\\n- [ ] 写 paper_framing.md + experiment_plan.yaml\\n- [ ] 部署 IFR + Phase 2 实验脚本到服务器\\n- [ ] 下载目标模型（Qwen-2.5 0.5B 优先）\\n\\n## GPU 预算\\n- 已分配: 1× RTX 4090D (cuda:5@cqa1-21977)\\n- MVP: ~2h | 全量: ~290h A100（需后续扩卡）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D035 | 2026-05-13 | D035: Reframe 为分析论文 Route A — \\\"When Does Cross-Met | mvp_pilot_gpt2_ioi_v3, phase2_qwen05b_ioi_acdc_k3, mvp_arithmetic_gpt2_k3 |\\n| D034 | 2026-05-13 | D034: Qwen ACDC 确认 CSS 跨模型 scaling 根本性失败——问题不在方法选择 | phase2_qwen05b_ioi_acdc_k3, phase2_qwen05b_ioi_k3, mvp_pilot_gpt2_ioi_v3 |\\n| D033 | 2026-05-13 | D033: SVA 判定降级为 inconclusive——单 seed Δ=0.013 不具鲁棒性 | mvp_sva_gpt2_k3_topk, mvp_sva_gpt2_k3 |\\n| D032 | 2026-05-13 | D032: 条件④评估指标修正——必须用 css_1.00 而非 css_0.67 | mvp_sva_gpt2_k3_topk, mvp_sva_gpt2_k3 |\\n| D031 | 2026-05-13 | 统一 D025 条件④标准：zero PASS 或 mean Δ≥0.01，SVA 两次均判 neg | mvp_sva_gpt2_k3, mvp_sva_gpt2_k3_topk |\\n| D030 | 2026-05-13 | SVA D025 gate FAIL（zero FAIL / mean 边际 Δ=0.008）；发现 | mvp_sva_gpt2_k3_topk |\\n| D029 | 2026-05-13 | Phase 2 第三方法：放弃 IFR，改用 ACDC top-k。IFR 跨族分歧作为 Discu | phase2_qwen05b_ioi_k3 |\\n| D028 | 2026-05-13 | Phase 2 IFR 零重叠问题：暂停 Qwen/Gemma 新实验，先修 IFR per-hea | phase2_qwen05b_ioi_k3 |\\n| D027 | 2026-05-13 | MVP 最终判定：CSS faithfulness 优势 task-dependent（IOI PA | mvp_arithmetic_gpt2_k3, mvp_pilot_gpt2_ioi_v3 |\\n| D026 | 2026-05-13 | Arithmetic D025 gate FAIL（条件④），暂不判 MVP 结果，先做 ACDC  | mvp_arithmetic_gpt2_k3 |\\n\\n\", \"total_chars\": 3059, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84b7b0bd-8e01-4cf3-bb2e-37e1e0c54b54",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "15372fb0-e62e-4de1-a51b-f617ea2c02b7",
  "sourceToolAssistantUUID": "84b7b0bd-8e01-4cf3-bb2e-37e1e0c54b54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-13T09:56:38.245Z_

Now let me look at the actual paper artifacts and any LaTeX files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15372fb0-e62e-4de1-a51b-f617ea2c02b7",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNKXuo5HxreqDJvSV4s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "021e8dcb-dafb-45c5-80db-557c03500624",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cwZFP1FEiQdxcCeZYeNoK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15372,
      "cache_read_input_tokens": 22502,
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

_source line 23 · 2026-05-13T09:56:40.132Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0163cH9su1MmvxeRzWJAgE44`</summary>

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
  "parentUuid": "021e8dcb-dafb-45c5-80db-557c03500624",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNKXuo5HxreqDJvSV4s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25be3cd6-9344-482e-8e8e-5ab7204d6bb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cwZFP1FEiQdxcCeZYeNoK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15372,
      "cache_read_input_tokens": 22502,
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

_source line 24 · 2026-05-13T09:56:40.163Z_

<details><summary>↩ Tool result · `toolu_0163cH9su1MmvxeRzWJAgE44`</summary>

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
  "parentUuid": "25be3cd6-9344-482e-8e8e-5ab7204d6bb3",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "8515a228-2130-4cb3-a659-cba2988d1c35",
  "sourceToolAssistantUUID": "25be3cd6-9344-482e-8e8e-5ab7204d6bb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T09:56:40.776Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019cp1aXxBd5grcT9b3ZRSr4`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8515a228-2130-4cb3-a659-cba2988d1c35",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNKXuo5HxreqDJvSV4s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "472226e4-8d36-42a5-babe-fbaa4b80b765",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cwZFP1FEiQdxcCeZYeNoK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15372,
      "cache_read_input_tokens": 22502,
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

_source line 26 · 2026-05-13T09:56:40.787Z_

<details><summary>↩ Tool result · `toolu_019cp1aXxBd5grcT9b3ZRSr4`</summary>

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
  "parentUuid": "472226e4-8d36-42a5-babe-fbaa4b80b765",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "56533718-48e3-494b-b0ca-e435484f8184",
  "sourceToolAssistantUUID": "472226e4-8d36-42a5-babe-fbaa4b80b765",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T09:56:41.128Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01K4iukQi9xmgWMctEffq4Np`</summary>

```json
{
  "pattern": "**/artifacts/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56533718-48e3-494b-b0ca-e435484f8184",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNKXuo5HxreqDJvSV4s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd61662a-1e90-4057-92f2-bf8b1f581063",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cwZFP1FEiQdxcCeZYeNoK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15372,
      "cache_read_input_tokens": 22502,
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

_source line 28 · 2026-05-13T09:56:41.166Z_

<details><summary>↩ Tool result · `toolu_01K4iukQi9xmgWMctEffq4Np`</summary>

```text
artifacts/structfuse-mvp/API_SURVEY.md
artifacts/structfuse-mvp/circus.py
artifacts/structfuse-mvp/evaluation.py
artifacts/structfuse-mvp/__pycache__/circus.cpython-314.pyc
artifacts/_project/intermediate/run_mvp.py
artifacts/structfuse-mvp/cross_tabulate.py
artifacts/structfuse-mvp/run_mvp.py
artifacts/structfuse-mvp/__pycache__/cross_tabulate.cpython-314.pyc
artifacts/_project/report/LARGE_MODEL_THIRD_METHOD.md
artifacts/structfuse-mvp/LARGE_MODEL_THIRD_METHOD.md
artifacts/_project/intermediate/ifr_discovery.py
artifacts/structfuse-mvp/ifr_discovery.py
artifacts/structfuse-mvp/css.py
artifacts/structfuse-mvp/config.py
artifacts/structfuse-mvp/__pycache__/ifr_discovery.cpython-314.pyc
artifacts/structfuse-mvp/__pycache__/config.cpython-314.pyc
artifacts/structfuse-mvp/__pycache__/css.cpython-314.pyc
artifacts/_project/intermediate/edge_pruning_l0.py
artifacts/structfuse-mvp/edge_pruning_l0.py
artifacts/structfuse-mvp/circuit_discovery.py
artifacts/structfuse-mvp/__pycache__/edge_pruning_l0.cpython-314.pyc
artifacts/mvp_status_report_20260512.md
artifacts/_project/intermediate/ifr_scoring.py
artifacts/ifr_scoring.py
artifacts/__pycache__/ifr_scoring.cpython-314.pyc
artifacts/_project/intermediate/test_ifr_scoring.py
artifacts/test_ifr_scoring.py
artifacts/_project/intermediate/model_adapter.py
artifacts/model_adapter.py
artifacts/_project/intermediate/run_circus.py
artifacts/_project/intermediate/css.py
artifacts/_project/intermediate/test_css.py
artifacts/_project/intermediate/edge_pruning_scoring.py
artifacts/_project/intermediate/test_edge_pruning_scoring.py
artifacts/_project/intermediate/eap_ig_scoring.py
artifacts/eap_ig_scoring.py
artifacts/_project/intermediate/test_eap_ig_scoring.py
artifacts/test_eap_ig_scoring.py
artifacts/_project/intermediate/edge_pruning_scoring_457920.py
artifacts/edge_pruning_scoring.py
artifacts/_project/intermediate/test_edge_pruning_scoring_3089a7.py
artifacts/test_edge_pruning_scoring.py
artifacts/test_run_circus_fixes.py
artifacts/deploy_phase2.sh
artifacts/_project/intermediate/deploy_phase2.sh
artifacts/_project/intermediate/analyze_mvp_results.py
artifacts/_project/data/run_phase2_experiment.py
artifacts/analyze_mvp_results.py
artifacts/analysis/analysis_results.json
artifacts/_project/data/phase2_configs.yaml
artifacts/_project/report/related_work_notes.md
artifacts/run_phase2_experiment.py
artifacts/phase2_configs.yaml
artifacts/_project/report/related_work_notes_114feb.md
artifacts/related_work_notes.md
artifacts/css.py
artifacts/run_circus.py
artifacts/test_css.py
artifacts/__pycache__/css.cpython-314.pyc
artifacts/__pycache__/run_circus.cpython-314.pyc
artifacts/literature_map.yaml
artifacts/_project/intermediate/analysis_fix_v3_meta.txt
artifacts/literature_jaccard_overlap.md
artifacts/_project/report/literature_jaccard_overlap.md
artifacts/D020_acdc_edge_selection.md
artifacts/mvp_pilot_gpt2_ioi_v3/report/D020_acdc_edge_selection.md
artifacts/literature_survey_related_work.md
artifacts/_project/report/edge_pruning_precheck_report.md
artifacts/edge_pruning_precheck_report.md
artifacts/_project/report/literature_survey_related_work.md
artifacts/_project/report/ifr_code_survey.md
artifacts/ifr_code_survey.md
artifacts/mvp_arithmetic_gpt2_k3/report/mvp_gate_checklist_d025.md
artifacts/mvp_gate_checklist_d025.md
artifacts/mvp_arithmetic_gpt2_k3/report/acdc_topk_sweep_results.md
artifacts/mean_ablation_results.json
artifacts/mvp_arithmetic_gpt2_k3/report/mean_ablation_results.json
artifacts/eval_topk_faithfulness.py
artifacts/mvp_arithmetic_gpt2_k3/report/topk_faithfulness_final.md
artifacts/dream_reports/dream_20260513T044816/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260513T044816/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260513T044816/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260513T044816/logs/orchestrator.log
artifacts/dream_reports/dream_20260513T044816/logs/phase2_median_attempt1.log
artifacts/dream_reports/dream_20260513T044816/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260513T054654/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260513T054654/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260513T054654/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260513T054654/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260513T054654/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T054654/best/experiment_data.json
artifacts/dream_reports/dream_20260513T054654/best/paper_framing.md
artifacts/dream_reports/dream_20260513T054654/best/paper.tex
artifacts/dream_reports/dream_20260513T054654/best/paper.aux
artifacts/dream_reports/dream_20260513T054654/best/paper.out
artifacts/dream_reports/dream_20260513T054654/best/paper.pdf
artifacts/dream_reports/dream_20260513T054654/best/paper.log
artifacts/dream_reports/dream_20260513T054654/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260513T054654/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T054654/median/experiment_data.json
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd61662a-1e90-4057-92f2-bf8b1f581063",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "cf441cc1-ea82-409d-9bcc-b2698d8fd48e",
  "sourceToolAssistantUUID": "bd61662a-1e90-4057-92f2-bf8b1f581063",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-13T09:56:45.301Z_

Let me read the most recent dream report paper (the best case, which represents the most polished version of the paper).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf441cc1-ea82-409d-9bcc-b2698d8fd48e",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNL7YrzoLX9zuCfSFgC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76f15285-74e4-4080-be5a-817ce3e05112",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BADFZZMK4x9q3G1Qc35LTq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2438,
      "cache_read_input_tokens": 37874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2438,
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

_source line 30 · 2026-05-13T09:56:47.004Z_

<details open><summary>🔧 Tool call — Read · `toolu_013piD8N4mMcygGwSo1NHV1M`</summary>

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
  "parentUuid": "76f15285-74e4-4080-be5a-817ce3e05112",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNL7YrzoLX9zuCfSFgC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0aa6de77-bcf4-4778-a279-a9a6121d964d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BADFZZMK4x9q3G1Qc35LTq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2438,
      "cache_read_input_tokens": 37874,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2438
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 37874,
          "cache_creation_input_tokens": 2438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2438,
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

_source line 31 · 2026-05-13T09:56:47.345Z_

<details><summary>↩ Tool result · `toolu_013piD8N4mMcygGwSo1NHV1M`</summary>

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
  "parentUuid": "0aa6de77-bcf4-4778-a279-a9a6121d964d",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "09fac9af-b6f7-415c-b18a-d78b225da533",
  "sourceToolAssistantUUID": "0aa6de77-bcf4-4778-a279-a9a6121d964d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-13T09:56:50.351Z_

Now let me also read the related work notes and literature survey that the authors prepared.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09fac9af-b6f7-415c-b18a-d78b225da533",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNLY7E4MbwoZTUiWbSq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4df35ed4-9d78-4700-9807-035230ed900e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122DNwdthBA6h8ScP66eHCH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11585,
      "cache_read_input_tokens": 40312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11585,
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

_source line 33 · 2026-05-13T09:56:52.278Z_

<details open><summary>🔧 Tool call — Read · `toolu_014MdAPf15DpKsmYPUWUY5NX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4df35ed4-9d78-4700-9807-035230ed900e",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNLY7E4MbwoZTUiWbSq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27b82595-7db8-43ac-9ff6-84228cf78acd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122DNwdthBA6h8ScP66eHCH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11585,
      "cache_read_input_tokens": 40312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11585,
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

_source line 34 · 2026-05-13T09:56:52.286Z_

<details><summary>↩ Tool result · `toolu_014MdAPf15DpKsmYPUWUY5NX`</summary>

````text
1	# Circuit Discovery Related Work Notes (2024-2026)
2	
3	> 调研日期：2026-05-12 | 项目：structfuse-context
4	> 核心问题：CSS（Cross-method Stability Scoring）的 novelty 是否站得住？
5	
6	---
7	
8	## 1. 方法一致性比较（Novelty 关键）
9	
10	**结论：没有论文以"跨方法一致性分析"为核心贡献。** 多篇论文在评估新方法时附带比较了不同方法的表现，但比较维度是各方法 vs ground-truth 的 faithfulness/AUC，而非方法之间的 pairwise agreement。
11	
12	### 直接比较多方法的论文
13	
14	| 论文 | 方法比较 | 比较维度 | 是否测量方法间一致性 |
15	|------|----------|----------|---------------------|
16	| Conmy et al. "Towards Automated Circuit Discovery" (NeurIPS 2023) | ACDC vs SP vs HISP | ROC AUC vs ground-truth | ❌ 不测方法间 overlap |
17	| Syed et al. "Attribution Patching Outperforms Automated Circuit Discovery" (BlackboxNLP 2024) | EAP vs ACDC vs SP vs HISP | AUC vs ground-truth | ❌ |
18	| Bhaskar et al. "Finding Transformer Circuits with Edge Pruning" (NeurIPS 2024 Spotlight) | Edge Pruning vs ACDC vs EAP | Faithfulness at various sparsities | ❌ 但隐含表明方法差异大：EP 找到的边不到 ACDC/EAP 的一半 |
19	| Hsu et al. "CD-T" (ICLR 2025) | CD-T vs ACDC vs EAP | ROC AUC vs ground-truth | ❌ |
20	| Edin et al. "GIM" (2025, arXiv) | GIM vs EActP vs EAP vs EAP-IG vs NAP vs IFR vs UGS | Faithfulness metrics | ❌ |
21	| InterpBench (NeurIPS 2024 D&B) | ACDC vs EAP vs SP on 86 semi-synthetic models | Ground-truth recovery | ❌ 但发现 ACDC 与 EAP-IG 统计上不可区分 |
22	
23	### 最接近"一致性分析"的论文
24	
25	**Hanna et al. "Have Faith in Faithfulness: Going Beyond Circuit Overlap" (2024, arXiv 2403.17806)**
26	- 比较 EAP vs EAP-IG 的 **node overlap**，发现两者 overlap 很高但 faithfulness 差异大
27	- 核心结论：overlap ≠ faithfulness，高 overlap 不代表电路功能等价
28	- **与 CSS 的关系**：这是对 overlap-based 评估的警告，但不是跨方法一致性的系统研究
29	
30	**Méloux et al. "Mechanistic Interpretability as Statistical Estimation: A Variance Analysis" (2025, arXiv 2510.00845)**
31	- 对 EAP-IG 做 bootstrap resampling，发现 **单方法内** Jaccard 仅 0.561
32	- 超参数变化导致 Jaccard 从 0.086 到 1.0 不等
33	- **与 CSS 的关系**：揭示了电路不稳定性问题（motivates CSS），但仅限单方法内变异，未跨方法
34	
35	**总结：无人系统测量不同方法间的 pairwise Jaccard / agreement matrix。这正是 CSS 要填补的空白。**
36	
37	---
38	
39	## 2. Circuit Aggregation / Ensemble（Novelty 威胁）
40	
41	### 🔴 最高威胁：CIRCUS
42	
43	**CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles**
44	- 作者：Swapnil Parekh
45	- 时间：2026年3月, arXiv 2603.00523
46	- 方法：对单一归因方法，在多组剪枝阈值配置下运行，计算每条边的 inclusion frequency → stability score s(e) ∈ [0,1]，提取 consensus circuit（所有配置下都存在的边），分为 core/contingent/noise
47	- **与 CSS 的区别**：CIRCUS 变化的是**单方法内的超参数**（剪枝阈值），不是跨不同算法族。它不运行 ACDC + EAP + SP 然后求交集
48	- **与 CSS 的相似度**：数学框架高度相似（per-edge stability scoring, consensus extraction, core/contingent taxonomy）
49	- **威胁评级**：🔴 HIGH — 概念上最接近，但维度不同（intra-method vs cross-method）
50	
51	### 🟡 中等威胁：Mondorf et al. Ensemble
52	
53	**Mondorf et al. "Exploring Ensemble Strategies for Circuit Localization Methods" (BlackboxNLP 2025, arXiv 2510.06811)**
54	- 方法：组合 EAP, EAP-IG-inputs, EAP-IG-activations, Edge Pruning 的输出
55	  - Max = union（任一方法选中）
56	  - Min = intersection（所有方法选中）
57	  - Mean = 连续分数平均
58	  - Hybrid = 并行+串行组合
59	- 结果：Mean > union/intersection，Hybrid 最佳 (CMD 0.03, CPR 1.83)
60	- **与 CSS 的区别**：聚合的是**连续归因分数**（mean/min/max），不是二值 edge-in/edge-out；方法主要是 EAP 变体，不是真正不同的算法族；workshop 短文非完整方法贡献
61	- **与 CSS 的相似度**：确实跨方法组合（attribution + pruning），实现了 union/intersection 操作
62	- **威胁评级**：🟡 MODERATE — 最接近跨方法聚合，但 framing 为 shared task 工程方案非方法论贡献
63	
64	### 🟢 低威胁
65	
66	| 论文 | 方法 | 与 CSS 区别 | 威胁 |
67	|------|------|------------|------|
68	| Nikankin et al. "Improving Circuit Faithfulness via Better Edge Selection" (BlackboxNLP 2025) | Bootstrap EAP-IG scores across data resamples | 单方法 + 数据重采样，非跨方法 | 🟢 LOW |
69	| Anani et al. "Certified Circuits: Stability Guarantees" (2026, arXiv 2602.22968) | 随机化数据子采样 + 删除平滑认证 | 单方法 wrapper，不聚合多方法 | 🟢 LOW |
70	| Miller et al. "Transformer Circuit Faithfulness Metrics are not Robust" (CoLM 2024) | 分析 faithfulness 指标敏感性 | 纯诊断，不提出聚合 | 🟢 LOW |
71	
72	**总结：没有论文提出 CSS 的精确方案——运行 N 种根本不同的算法族（ACDC, EAP, SP, EP），对每种输出做二值化，然后计算跨方法 binary consensus。CIRCUS 最接近但维度不同（intra-method threshold variation vs cross-method）。Mondorf et al. 确实跨方法但用连续分数聚合且为 workshop 工程方案。**
73	
74	---
75	
76	## 3. 2024-2026 新方法
77	
78	| 方法 | 论文 | 年份 | 会议 | 算法族 | 备注 |
79	|------|------|------|------|--------|------|
80	| CD-T | Hsu et al. "Efficient Automated Circuit Discovery using Contextual Decomposition" | 2024 | ICLR 2025 | 分解 (decomposition) | 无需 activation patching，秒级发现，97% AUC |
81	| DiscoGP | Yu et al. "Functional Faithfulness in the Wild" | 2024 | ICML 2024 | 可微剪枝 | 联合权重+边剪枝，端到端学习二值 mask |
82	| Transcoders | Dunefsky et al. "Transcoders Find Interpretable LLM Feature Circuits" | 2024 | NeurIPS 2024 | 稀疏替换模型 | 用稀疏 MLP 替换原 MLP，实现 weights-based 电路分析 |
83	| Sparse Feature Circuits | Marks et al. "Discovering and Editing Interpretable Causal Graphs" | 2024 | ICLR 2025 (Oral) | 归因 + SAE 特征 | 在 SAE 特征级别发现电路，支持 SHIFT 编辑 |
84	| Circuit Tracing | Ameisen, Olah et al. (Anthropic) "Attribution Graphs" | 2025 | Tech Report | 稀疏替换 + 归因 | Cross-layer transcoders → per-prompt DAG，应用于 Claude 3.5 |
85	| GIM | Edin et al. "Improved Interpretability for LLMs" | 2025 | arXiv | 梯度修正 | 修正 softmax/LayerNorm 反传，MIB 排行榜第一 |
86	| HAP | Gu et al. "Hybrid Attribution and Pruning Framework" | 2025 | arXiv | 混合 (EAP → EP) | 先 EAP 粗筛再 EP 精修，比 EP 快 46% |
87	| ModCirc | He et al. "Modular Circuits of LLMs" | 2025 | ICML 2025 | 模块化分解 | 发现跨任务共享的模块化电路词表 |
88	| Stream | Rosser et al. "Scaling up MI to Long Context" | 2025 | arXiv | 层次化剪枝 | O(T log T) 稀疏注意力 mask，支持 100K+ token |
89	| Weight-Sparse Circuits | Gao et al. (OpenAI) | 2025 | arXiv | 稀疏训练 | 极端权重稀疏 (~1/1000) → 天然可解释电路 |
90	| Formal MI | Hadad et al. "Automated Circuit Discovery with Provable Guarantees" | 2026 | ICLR 2026 | 验证 (verification) | 首个可证明保证的电路发现（鲁棒性 + 最小性） |
91	| SVD Directional Masking | Ahmad et al. "Beyond Components" | 2025 | arXiv | SVD + 可微 mask | 揭示单头内叠加子功能 |
92	
93	---
94	
95	## 4. 顶会论文列表
96	
97	### ICLR 2024
98	| 论文 | 主要贡献 |
99	|------|----------|
100	| Sparse Autoencoders Find Highly Interpretable Features in LMs | SAE 发现单语义特征，解决 superposition |
101	| Towards Best Practices of Activation Patching in LMs | 系统分析 patching 方法选择对电路发现的影响 |
102	| Circuit Component Reuse Across Tasks | IOI 电路 ~78% 被 Colored Objects 复用 |
103	| Successor Heads: Recurring Interpretable Attention Heads | 发现跨架构的 successor heads（递增操作） |
104	
105	### ICLR 2025
106	| 论文 | 主要贡献 |
107	|------|----------|
108	| Sparse Feature Circuits (Oral) | SAE 特征级电路发现 + SHIFT 编辑 |
109	| Scaling and Evaluating Sparse Autoencoders (Oral) | k-sparse SAE 扩展到 GPT-4，16M latents |
110	| CD-T: Contextual Decomposition for Circuit Discovery | 秒级电路发现，97% AUC |
111	| Computational Complexity of Circuit Discovery (Spotlight) | 证明多数电路发现查询 NP-hard |
112	| Everything Everywhere All at Once: Is MI Identifiable? | 电路非唯一性：多电路可复现同一行为 |
113	| SAEs Do Not Find Canonical Units of Analysis | SAE stitching 证明特征非原子/非完备 |
114	| Unifying and Verifying Mechanistic Interpretations | 统一群运算网络的机制解释并形式化证明 |
115	
116	### NeurIPS 2024
117	| 论文 | 主要贡献 |
118	|------|----------|
119	| Finding Transformer Circuits with Edge Pruning (Spotlight) | EP 方法，更忠实且更稀疏，扩展到 13B |
120	| Transcoders Find Interpretable LLM Feature Circuits | 稀疏 MLP 替换实现 weights-based 电路分析 |
121	| LLM Circuit Analyses Are Consistent Across Training and Scale | 电路在训练过程和模型规模间一致出现 |
122	| Compact Proofs of Model Performance via MI | MI → 可证明的准确率下界 |
123	| Hypothesis Testing the Circuit Hypothesis | 形式化电路假设的假设检验 |
124	| InterpBench: Semi-Synthetic Transformers for Evaluating MI | 86 个有 ground-truth 的半合成模型评估基准 |
125	
126	### ICML 2025
127	| 论文 | 主要贡献 |
128	|------|----------|
129	| MIB: A Mechanistic Interpretability Benchmark | 标准化电路定位基准，归因+mask 优化方法领先 |
130	| ModCirc: Modular Circuits of LLMs | 跨任务模块化电路词表 |
131	| Towards Understanding Fine-Tuning via Circuit Analysis | 追踪微调中电路变化，提出 circuit-aware LoRA |
132	
133	---
134	
135	## 5. Novelty 评估
136	
137	### CSS 的 novelty 站得住吗？**站得住，但需要精确定位差异化。**
138	
139	#### ✅ Novelty 成立的理由
140	
141	1. **无人做跨算法族的 binary consensus**：所有现有工作要么是单方法内变异分析（CIRCUS, Méloux），要么是连续分数聚合（Mondorf），要么只是各方法 vs ground-truth 的性能比较。CSS 提出跨 N 种根本不同的算法族做二值共识，这个精确配方是新的。
142	
143	2. **方法间差异的系统分析是空白**：没有论文报告过不同方法的 pairwise Jaccard matrix / agreement heatmap。大量论文隐含表明方法差异很大（EP 边数不到 ACDC 一半），但无人将此作为研究问题。
144	
145	3. **core/contingent 分类的跨方法版本未被探索**：CIRCUS 做了类似的 core/contingent/noise taxonomy，但基于 intra-method threshold variation。CSS 基于 cross-method agreement 做分类，维度不同且信息更丰富。
146	
147	#### ⚠️ 需要小心的 Novelty 威胁
148	
149	1. **CIRCUS (2603.00523)** 是最大威胁。虽然维度不同，但 reviewer 可能认为 conceptual overlap 太大。**建议**：论文中必须明确讨论 CIRCUS，强调区别（intra-method hyperparameter variation vs cross-method algorithmic diversity），并论证为何跨方法维度更有意义（不同方法有不同 inductive bias，而阈值变化只探索同一方法的 Rashomon set）。
150	
151	2. **Mondorf et al.** 已经实现了 union/intersection 操作并发现 mean 优于两者。CSS 需要论证 binary consensus 相比连续分数平均的优势（如可解释性、对阈值选择的鲁棒性）。
152	
153	3. **Méloux et al. 的 intra-method instability 问题**：如果单方法内 Jaccard 仅 0.56，跨方法 consensus 可能更低。需要实验证明 CSS-core 的 faithfulness 确实优于单方法，否则 consensus 可能只是噪声的交集。
154	
155	4. **非唯一性问题 (ICLR 2025 "Everything Everywhere All at Once")**：如果电路本身就非唯一，跨方法共识的理论基础需要更强的论证。
156	
157	#### 🎯 差异化建议
158	
159	- **vs CIRCUS**：CSS 跨算法族（不同 inductive bias），CIRCUS 跨阈值（同一方法的 Rashomon set）。论证：不同方法捕获不同类型的因果关系，其交集比单方法阈值交集更有意义。
160	- **vs Mondorf et al.**：CSS 是二值共识（edge in/out），Mondorf 是连续分数平均。论证：二值化消除了方法间分数不可比的问题，且产出可直接解释的 agreement matrix。
161	- **vs MIB benchmark**：MIB 评估单方法表现，CSS 分析方法间关系。互补而非竞争。
162	
163	---
164	
165	## 1b. CIRCUS 深度分析
166	
167	> 论文：CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles (arXiv 2603.00523, 2026.02.28)
168	> 作者：Swapnil Parekh
169	> 代码：未公开（GitHub: SwapnilDreams100，未找到 CIRCUS 仓库）
170	
171	### 方法细节
172	
173	**Stability 测量机制：变化剪枝阈值，不变种子/数据。**
174	
175	CIRCUS 对**单一 attribution graph**（由 cross-layer transcoders 生成的归因图）施加 B 组不同的剪枝配置 {π₁, ..., πB}，每组配置指定不同的 node threshold 和 edge threshold（cumulative-influence cutoffs）。**不涉及**随机种子变化或数据子集变化。
176	
177	**Config-bagging 参数：**
178	- B=25（5×5 grid）用于 stability 分析
179	- B=9（non-nested configurations）用于主实验评估
180	- B=3 用于嵌套配置消融实验
181	- **关键设计约束——non-nesting**：配置必须在不同维度上交叉变化（如 (0.6, 0.99) 保留少 node 多 edge，(0.9, 0.95) 相反），避免 E(1)⊆E(2)⊆...⊆E(B) 导致 consensus 退化为最严格单配置
182	
183	**Consensus 公式：**
184	
185	stability score（per-edge inclusion frequency）：
186	```
187	s(e) = (1/B) × Σ_{b=1}^{B} 𝟙[e ∈ E(b)]
188	```
189	
190	consensus circuit 提取：
191	```
192	C_τ = {e : s(e) ≥ τ}
193	```
194	
195	主实验使用 **strict consensus τ=1**（边必须在所有配置中存在）。τ<1 可用于探索性分析。
196	
197	**Core/Contingent/Noise 分类：**
198	| 类别 | 定义 | 含义 |
199	|------|------|------|
200	| Core | s(e) = 1 | 所有配置都保留，鲁棒结构 |
201	| Contingent | 0.5 ≤ s(e) < 1 | 多数配置保留，替代路径 |
202	| Noise | s(e) < 0.5 | 少数配置保留，阈值敏感伪影 |
203	
204	类比 Bayesian variable selection 中的 posterior model-inclusion indicators。
205	
206	### 实验设置
207	
208	**模型：**
209	- Gemma-2-2B
210	- Llama-3.2-1B
211	
212	**任务：**
213	- Short factoid completions：capitals, arithmetic, trivia
214	- 数据规模：50 prompts (Gemma), 20 prompts (Llama)
215	- 论文明确承认局限："generalization to more complex behaviors (reasoning, in-context learning) remains open"
216	
217	**使用的 circuit discovery 方法：仅一种。**
218	- 底层方法：cross-layer transcoders (CLTs) 生成的 attribution graphs（引用 Ameisen et al. 2025, Hanna et al. 2025）
219	- 节点 = learned features（CLT 特征），边 = features 间的直接因果效应，权重 W ∈ ℝ^{|E|}
220	- **不使用** EAP, ACDC, Edge Pruning 或其他传统 circuit discovery 方法
221	- **不跨方法比较**
222	
223	### Faithfulness 评估
224	
225	**Metrics：**
226	
227	1. **Influence Retained (IR)**：IR(S) = Φ(S)/Φ(E)，其中 Φ(S) = Σ|w_e| 为子图绝对边权之和。衡量通过子图 S 的总归因影响比例。
228	
229	2. **KL Divergence（per-logit）**：D_KL(p_E || p_S)，consensus 达到 0.0010±0.0008 vs union-pruned 0.40±1.74（20 prompts, 17/20 wins）。
230	
231	3. **Activation Patching（因果验证）**：
232	   - Patch C₁ 节点激活从 source prompt → target prompt
233	   - Recovery: consensus 19.4 vs random 6.8 vs matched controls 1.6
234	   - p=0.0004 (Wilcoxon signed-rank)
235	   - Consensus = oracle 的 57%，random = 20%
236	
237	4. **Win-rate**：
238	   - vs union-pruned: 47/50 (Gemma), 19/20 (Llama) with B=9
239	   - vs random: 37/50 (Gemma), 20/20 (Llama)
240	
241	**关键结论：** strict consensus circuit ~40× smaller than union，但保持 comparable influence-flow 解释力。overhead 仅 5.5%（<1ms consensus 构建）。
242	
243	### 跨方法比较
244	
245	**CIRCUS 没有做跨方法比较。** 这是确认的事实：
246	- 仅使用 CLT attribution graphs 一种 pipeline
247	- 变化的是该 pipeline 内的剪枝阈值配置
248	- 不涉及 EAP, ACDC, Edge Pruning, SP 等任何其他 circuit discovery 算法
249	- **这是 CSS 的核心差异点**
250	
251	### CSS vs CIRCUS 精确差异表
252	
253	| 维度 | CIRCUS | CSS (ours) |
254	|------|--------|-----------|
255	| **变化什么** | 单方法内的剪枝阈值 (node/edge cutoffs) | 算法族 (gradient/mask/causal 等不同范式) |
256	| **底层方法数** | 1 种 (CLT attribution graphs) | K=3+ 种根本不同的算法 (如 EAP, ACDC, EP) |
257	| **稳定性来源** | Intra-method: 阈值鲁棒性 (Rashomon set) | Cross-method: 算法族间一致性 (不同 inductive bias) |
258	| **聚合方式** | 连续 stability score s(e)∈[0,1] + strict consensus τ=1 | 二值投票 (K 方法中 ≥ threshold 方法包含 edge) |
259	| **输入** | 单次 attribution run 的一张归因图 | 每种方法独立运行产出的 K 张电路图 |
260	| **计算开销** | 极低 (5.5% overhead, 不需重新计算归因) | 需要运行 K 种不同算法 (各自完整 pipeline) |
261	| **模型规模** | Gemma-2-2B, Llama-3.2-1B | 待定 |
262	| **任务类型** | Short factoid completions | 待定 |
263	| **core claim** | 阈值变化下的鲁棒核心 vs 阈值敏感伪影 | 跨算法族共识比单方法更鲁棒、更可信 |
264	| **方法间差异分析** | ❌ 不分析 | ✅ Pairwise Jaccard matrix / agreement heatmap |
265	| **taxonomy 基础** | 同方法不同参数的 inclusion frequency | 不同方法的 agreement count |
266	
267	### 关键论点：为何 cross-method > intra-method
268	
269	1. **不同 inductive bias**：EAP 基于梯度归因，ACDC 基于 activation patching（因果干预），EP 基于可微剪枝。它们从根本不同的角度逼近"重要边"。阈值变化只探索同一视角的灵敏度。
270	2. **信息正交性**：跨方法共识的边同时被梯度信号、因果干预和优化剪枝确认，信息量远大于同方法不同阈值。
271	3. **实用价值**：如果研究者只有一种方法，CIRCUS 有用；如果研究者想知道"哪些结构是方法无关的"，CSS 回答的是不同的问题。
272	4. **Méloux et al. 的启示**：单方法内 Jaccard 仅 0.561，说明 intra-method 变异已经很大。跨方法共识可能提供更稳定的 core（或发现更大的分歧——这本身也是重要发现）。
273	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27b82595-7db8-43ac-9ff6-84228cf78acd",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "a2e8282a-e2e1-4f1d-9508-5b06b0a6f363",
  "sourceToolAssistantUUID": "27b82595-7db8-43ac-9ff6-84228cf78acd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-13T09:56:53.072Z_

<details open><summary>🔧 Tool call — Read · `toolu_0113JqKnpfDdsBoDqSHfhMi7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/literature_survey_related_work.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2e8282a-e2e1-4f1d-9508-5b06b0a6f363",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNLY7E4MbwoZTUiWbSq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da770f92-3650-4b8c-9e4a-af5b836f0f19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122DNwdthBA6h8ScP66eHCH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11585,
      "cache_read_input_tokens": 40312,
      "output_tokens": 181,
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
          "output_tokens": 181,
          "cache_read_input_tokens": 40312,
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

_source line 36 · 2026-05-13T09:56:53.079Z_

<details><summary>↩ Tool result · `toolu_0113JqKnpfDdsBoDqSHfhMi7`</summary>

```text
1	# Related Work Literature Survey for CSS (Cross-method Structural Consensus)
2	
3	> Generated: 2026-05-13 | Target: EMNLP 2026 Main (ARR deadline 2026-05-25)
4	
5	---
6	
7	## Direction 1: Cross-method Consensus / Ensemble in Mechanistic Interpretability
8	
9	### 1.1 CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles
10	- **Authors:** Swapnil Parekh
11	- **Year:** 2026 (arXiv: 2603.00523)
12	- **Venue:** arXiv preprint (Feb 2026)
13	- **Core findings:** Reframes circuit discovery as an uncertainty-quantification problem. Constructs an ensemble of attribution graphs by pruning a *single* raw attribution run under multiple threshold configurations, assigns each edge a stability score (fraction of configs retaining it), and extracts a strict-consensus circuit (edges appearing in all views). On Gemma-2-2B and Llama-3.2-1B, strict consensus circuits are ~40× smaller than the union while retaining comparable explanatory power. Consensus-identified nodes beat matched non-consensus controls in causal relevance (p=0.0004).
14	- **Relation to CSS:** **直接竞争 (Primary competitor)**. CIRCUS varies pruning thresholds on a single attribution method to build consensus; CSS uses multiple independent discovery methods (EAP-IG, EP, ACDC/IFR). Key differentiators: (1) CSS captures cross-method agreement (different algorithms with different inductive biases), not just threshold robustness within one method; (2) CSS uses binary agreement rather than fractional stability scores; (3) CSS explicitly tests distribution-shift robustness. Must position CSS as complementary/stronger: method diversity > threshold diversity.
15	
16	### 1.2 Certified Circuits: Stability Guarantees for Mechanistic Circuits
17	- **Authors:** Alaa Anani, Tobias Lorenz, Bernt Schiele, et al.
18	- **Year:** 2026 (arXiv: 2602.22968)
19	- **Venue:** arXiv preprint (Feb 2026)
20	- **Core findings:** Wraps any black-box discovery algorithm with randomized data subsampling to certify that circuit component inclusion decisions are invariant to bounded edit-distance perturbations of the concept dataset. On ImageNet with ResNet-101, certified circuits achieved 96% accuracy vs 86% baseline using half the neurons. Addresses dataset-to-circuit instability.
21	- **Relation to CSS:** **互补 (Complementary)**. Certified Circuits focuses on data perturbation stability for vision models with formal guarantees; CSS focuses on method-agreement stability for language model circuits. Both address instability but from orthogonal angles. Could cite as motivation for why stability matters.
22	
23	### 1.3 Open Problems in Mechanistic Interpretability
24	- **Authors:** Lee Sharkey, Bilal Chughtai, Joshua Batson, et al. (29 authors, 18 organizations)
25	- **Year:** 2025 (arXiv: 2501.16496)
26	- **Venue:** arXiv preprint (Jan 2025), commissioned by Schmidt Sciences
27	- **Core findings:** Landmark collaborative paper establishing the field's consensus open problems. Highlights systematic non-identifiability: multiple circuits, features, and algorithm mappings can yield the same behavioral fidelity. Advocates reporting explanation ensembles and clarifying pragmatic vs. unicity criteria.
28	- **Relation to CSS:** **支持 (Supports CSS)**. Directly motivates multi-method consensus: if circuits are non-unique, reporting ensembles and agreement is essential. CSS operationalizes this recommendation.
29	
30	### 1.4 Circuit Tracing: Revealing Computational Graphs in Language Models
31	- **Authors:** Anthropic (Dario Amodei team)
32	- **Year:** 2025
33	- **Venue:** Anthropic Technical Report (March 2025)
34	- **Core findings:** Uses cross-layer transcoders to build attribution graphs—graphical representations of computational steps where nodes are features and edges are causal interactions. Open-sourced circuit tracing tools supporting Gemma-2-2B, Llama-3.1-1B, Qwen3-4B.
35	- **Relation to CSS:** **互补 (Complementary)**. Provides a different paradigm (feature-level circuits via transcoders vs. component-level circuits). CSS methods operate at edge/component level; circuit tracing works at feature level. Represents a parallel direction worth acknowledging.
36	
37	---
38	
39	## Direction 2: Circuit Faithfulness Evaluation
40	
41	### 2.1 Transformer Circuit Faithfulness Metrics Are Not Robust
42	- **Authors:** Joseph Miller, Bilal Chughtai, William Saunders
43	- **Year:** 2024
44	- **Venue:** COLM 2024
45	- **Core findings:** Faithfulness scores are highly sensitive to seemingly insignificant ablation methodology choices. Edge-level vs node-level ablation, resample vs mean ablation, and other methodological variations yield substantially different faithfulness percentages. Existing circuit faithfulness scores reflect researcher methodology as much as actual circuit quality.
46	- **Relation to CSS:** **强支持 (Strongly supports CSS)**. Core motivation for CSS: if single-method faithfulness metrics are unreliable, cross-method agreement provides a more robust signal. Directly supports the claim that binary consensus is more stable than score-dependent evaluation.
47	
48	### 2.2 Have Faith in Faithfulness: Going Beyond Circuit Overlap When Finding Model Mechanisms
49	- **Authors:** Michael Hanna, Sandro Pezzelle, Yonatan Belinkov
50	- **Year:** 2024
51	- **Venue:** COLM 2024 (also ICML 2024 MI Workshop Spotlight)
52	- **Core findings:** Introduces EAP-IG (EAP with integrated gradients) which finds more faithful circuits than EAP. Key finding: high node overlap ≠ high faithfulness. When comparing circuits, measuring overlap is no substitute for measuring faithfulness.
53	- **Relation to CSS:** **支持+基础方法 (Supports + foundational method)**. EAP-IG is one of CSS's three discovery methods. The finding that overlap ≠ faithfulness motivates CSS's use of faithfulness-based evaluation rather than simple circuit overlap metrics.
54	
55	### 2.3 MIB: A Mechanistic Interpretability Benchmark
56	- **Authors:** Yoav Goldberg, Yonatan Belinkov, et al.
57	- **Year:** 2025–2026 (arXiv: 2504.13151)
58	- **Venue:** ICML 2025 / ICLR 2026
59	- **Core findings:** Establishes two evaluation tracks—circuit localization and causal variable localization—across diverse tasks and models. Attribution and mask optimization methods perform best on circuit localization. Supervised DAS significantly outperforms unsupervised SAE features for causal variable localization.
60	- **Relation to CSS:** **互补 (Complementary)**. Provides standardized evaluation framework. CSS could adopt MIB tasks/metrics for evaluation; MIB results contextualize method performance differences.
61	
62	### 2.4 Functional Faithfulness in the Wild: Circuit Discovery with Differentiable Computation Graph Pruning
63	- **Authors:** Lei Yu, Jingcheng Niu, Zining Zhu, et al.
64	- **Year:** 2024 (arXiv: 2407.03779)
65	- **Venue:** arXiv preprint (July 2024)
66	- **Core findings:** Introduces DiscoGP—differentiable masking that prunes both weights and edges. Extracts sheaves preserving 93–100% model performance using only 1–7% of original weights/connections. Identifies that activation-patching-based circuits tend to be neither functionally faithful nor complete.
67	- **Relation to CSS:** **互补 (Complementary)**. Shows that weight+edge pruning yields more faithful circuits than edge-only approaches, further highlighting that methodology choices dramatically affect circuit quality—supporting CSS's cross-method approach.
68	
69	---
70	
71	## Direction 3: Binary vs Continuous Scoring in Circuit Discovery
72	
73	### 3.1 Finding Transformer Circuits with Edge Pruning
74	- **Authors:** Adithya Bhaskar, Alexander Wettig, Dan Friedman, et al.
75	- **Year:** 2024
76	- **Venue:** NeurIPS 2024
77	- **Core findings:** Frames circuit discovery as gradient-based optimization with binary masks over edges. EP is considerably more faithful on IOI and Greater-Than than both ACDC and EAP, especially at higher sparsities. Scales effectively to 100K examples where it is fastest and most faithful.
78	- **Relation to CSS:** **基础方法+支持 (Foundational method + supports)**. EP is one of CSS's discovery methods. Uses binary masks (0/1) for edge inclusion—directly relevant to CSS's binary consensus. Shows binary edge selection can be highly faithful.
79	
80	### 3.2 Attribution Patching Outperforms Automated Circuit Discovery
81	- **Authors:** Aaquib Syed, Can Rager, Arthur Conmy
82	- **Year:** 2024
83	- **Venue:** BlackboxNLP 2024 (NeurIPS Workshop)
84	- **Core findings:** A simple method based on attribution patching outperforms ACDC while requiring just two forward passes + one backward pass. However, EAP's first-order approximations show lower faithfulness to the full model than EP.
85	- **Relation to CSS:** **支持 (Supports)**. Documents that different methods (ACDC, EAP, EP) yield different circuits with different faithfulness levels—core motivation for cross-method consensus. Methods that are fast (EAP) and methods that are faithful (EP) produce systematically different results.
86	
87	### 3.3 Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework (HAP)
88	- **Authors:** Adithya Bhaskar, Alexander Wettig, et al.
89	- **Year:** 2025 (arXiv: 2510.03282)
90	- **Venue:** NeurIPS 2025
91	- **Core findings:** Two-stage pipeline: EAP filters unimportant edges (continuous scores → top-k), then EP refines with binary masks. HAP is ≥46% faster than EP while maintaining high faithfulness. Preserves cooperative circuit components (e.g., S-inhibition heads) that EAP alone prunes at high sparsity.
92	- **Relation to CSS:** **互补 (Complementary)**. Shows that combining methods sequentially (EAP→EP) improves over either alone. CSS takes a different combination approach: run methods independently, then take binary consensus. Complementary philosophies of method combination.
93	
94	### 3.4 Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models
95	- **Authors:** Samuel Marks, Can Rager, Eric Michaud, Yonatan Belinkov, David Bau, Aaron Mueller
96	- **Year:** 2025
97	- **Venue:** ICLR 2025 (Oral)
98	- **Core findings:** Uses SAEs to identify features, then discovers feature-level causal circuits. Small feature circuits (<100 nodes) explain a large proportion of model performance on subject-verb agreement. Introduces SHIFT for improving classifier generalization by ablating task-irrelevant features.
99	- **Relation to CSS:** **互补 (Complementary)**. Operates at feature level (SAE features) vs. CSS's component level (attention heads, MLPs). Shows that sparse/binary feature selection is powerful for circuit analysis. CSS could potentially extend to feature-level consensus in future work.
100	
101	### 3.5 Transcoders Find Interpretable LLM Feature Circuits
102	- **Authors:** Jacob Dunefsky, Philippe Morel, et al.
103	- **Year:** 2024
104	- **Venue:** NeurIPS 2024
105	- **Core findings:** Transcoders approximate dense MLP layers with wider, sparsely-activating layers. On par with SAEs in sparsity, faithfulness, and interpretability. Applied to reverse-engineer circuits in GPT-2-small including novel insights on the greater-than circuit.
106	- **Relation to CSS:** **互补 (Complementary)**. Offers alternative circuit representation (feature-level via transcoders). Relevant as a potential additional discovery method for CSS.
107	
108	---
109	
110	## Direction 4: Instability / Unreliability of Single-method Circuit Discovery
111	
112	### 4.1 Mechanistic Interpretability as Statistical Estimation: A Variance Analysis
113	- **Authors:** Maxime Méloux et al.
114	- **Year:** 2025–2026 (arXiv: 2510.00845, revised Feb 2026)
115	- **Venue:** arXiv preprint
116	- **Core findings:** Frames circuit discovery as a statistical estimation problem. Uncovers fundamental instability: single-input CMA scores exhibit high intrinsic variance—causal effects are volatile random variables, not fixed properties. Small perturbations in input data or hyperparameters yield vastly different circuits. Focuses on EAP and EAP-IG, systematically decomposing variance sources.
117	- **Relation to CSS:** **强支持 (Strongly supports CSS)**. Provides quantitative evidence that single-method circuits are unstable. Directly motivates CSS: if individual methods have high variance, cross-method consensus filters out method-specific noise.
118	
119	### 4.2 Circuit Stability Characterizes Language Model Generalization
120	- **Authors:** Alan Sun
121	- **Year:** 2025
122	- **Venue:** ACL 2025
123	- **Core findings:** Mathematically formalizes circuit stability—a model's ability to apply a consistent reasoning process (circuit) across inputs. Through three case studies, shows circuit stability predicts different aspects of generalization. Models that lack circuit stability fail to generalize.
124	- **Relation to CSS:** **支持 (Supports)**. Establishes that circuit stability is a valuable property. CSS targets a complementary notion of stability: consistency across methods rather than across inputs.
125	
126	### 4.3 Finding Highly Interpretable Prompt-Specific Circuits in Language Models
127	- **Authors:** Gabriel Franco, Lucas M. Tassis, Azalea Rohr, Mark Crovella
128	- **Year:** 2026 (arXiv: 2602.13483)
129	- **Venue:** arXiv preprint (Feb 2026)
130	- **Core findings:** Circuits are prompt-specific even within a fixed task. Applying ACC++ to IOI in GPT-2, Pythia, and Gemma 2: no single circuit for IOI in any model—different prompt templates induce systematically different mechanisms.
131	- **Relation to CSS:** **支持+挑战 (Supports + challenges)**. Supports CSS by showing single circuits are insufficient; challenges CSS to demonstrate that consensus circuits are more stable across prompts. CSS should test prompt-level robustness.
132	
133	### 4.4 Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees
134	- **Authors:** Itamar Hadad, Guy Katz, Shahaf Bassan
135	- **Year:** 2026
136	- **Venue:** ICLR 2026
137	- **Core findings:** Leverages neural network verification to yield circuits with provable guarantees: input domain robustness, robust patching, and minimality. Prior methods depend on heuristics without guarantees over continuous input domains. Applied to vision models.
138	- **Relation to CSS:** **互补 (Complementary)**. Takes a formal verification approach to robustness; CSS takes an empirical consensus approach. Both address circuit reliability but through fundamentally different mechanisms. Currently limited to vision models.
139	
140	### 4.5 Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition (CD-T)
141	- **Authors:** Adelaide Hsu et al.
142	- **Year:** 2025
143	- **Venue:** ICLR 2025
144	- **Core findings:** Uses mathematical decomposition (no approximations) for circuit discovery. Reduces runtime from hours to seconds vs ACDC. Achieves 97% ROC AUC on IOI, Greater-Than, and Docstring tasks. Compatible with all transformer types, no training required.
145	- **Relation to CSS:** **互补 (Complementary)**. Provides yet another discovery method with different inductive biases than EAP-IG/EP/ACDC—could be a candidate additional method for CSS's ensemble.
146	
147	### 4.6 Towards Automated Circuit Discovery for Mechanistic Interpretability (ACDC)
148	- **Authors:** Arthur Conmy, Augustine N. Mavor-Parker, Aaquib Lynch, Stefan Heimersheim, Adrià Garriga-Alonso
149	- **Year:** 2023
150	- **Venue:** NeurIPS 2023
151	- **Core findings:** Foundational automated circuit discovery method using iterative activation patching. Effective but slow (runtime scales linearly with edges). Recovers IOI, Greater-Than, Docstring circuits. Establishes benchmark tasks for circuit discovery evaluation.
152	- **Relation to CSS:** **基础方法 (Foundational method)**. ACDC is one of CSS's three discovery methods for GPT-2 Small. Its different algorithmic approach (iterative patching vs. gradient-based) provides genuine method diversity in CSS's ensemble.
153	
154	---
155	
156	## Additional Relevant Work
157	
158	### RelP: Faithful and Efficient Circuit Discovery via Relevance Patching
159	- **Authors:** Farnoush Rezaei Jafari et al.
160	- **Year:** 2025
161	- **Venue:** NeurIPS 2025 MechInterp Workshop (Spotlight)
162	- **Core findings:** Replaces gradients in attribution patching with LRP propagation coefficients. For MLP outputs in GPT-2 Large, attribution patching achieves Pearson correlation 0.006 vs. RelP's 0.956 with activation patching ground truth. Faithfulness comparable to IG at lower cost.
163	- **Relation to CSS:** **互补 (Complementary)**. Another discovery method with different inductive bias. Documents dramatic differences between methods on the same components—supports CSS's premise.
164	
165	---
166	
167	## Key Takeaways for CSS Positioning
168	
169	### 1. CSS fills a specific gap in the literature
170	The field has established that (a) circuit discovery methods disagree (Syed et al. 2024; Méloux et al. 2025), (b) faithfulness metrics are unreliable (Miller et al. 2024), and (c) circuits are sensitive to analyst choices (CIRCUS, Certified Circuits). CSS is the first to exploit **cross-method binary consensus** as a robustness mechanism, using method diversity rather than threshold/data perturbation diversity.
171	
172	### 2. CIRCUS is the primary competitor — positioning is critical
173	CIRCUS (Parekh, 2026) is the closest work. Key differentiation:
174	- **CIRCUS:** varies pruning thresholds within one attribution method → threshold robustness
175	- **CSS:** uses multiple independent discovery methods → method robustness
176	- CSS argument: method diversity captures a broader space of inductive biases than threshold variation. A threshold ensemble still inherits the blind spots of its single underlying attribution method (e.g., EAP's first-order approximation errors). CSS's methods have structurally different failure modes (gradient-based vs. iterative patching vs. similarity-based).
177	
178	### 3. The "instability problem" is well-documented — CSS offers a practical solution
179	Multiple papers (Méloux et al., Franco et al., Miller et al.) document that circuits are unstable across data, prompts, and methodology. The Open Problems paper (Sharkey et al. 2025) explicitly calls for reporting ensembles. CSS directly operationalizes this recommendation with a concrete, lightweight algorithm.
180	
181	### 4. Binary scoring is underexplored relative to continuous scoring
182	Most methods produce continuous importance scores (EAP, EAP-IG, CD-T) and require threshold selection. Edge Pruning uses binary masks but within a single optimization. CSS's binary consensus (edge included/excluded per method → majority vote) is a distinct aggregation strategy that avoids score calibration issues across methods with incomparable scales.
183	
184	### 5. Distribution-shift robustness is a novel evaluation angle
185	No existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS's off-diagonal evaluation (train on distribution A, test on distribution B) is a distinctive contribution.
186	
187	### 6. Recommended related work structure for the paper
188	1. **Circuit discovery methods** (ACDC, EAP-IG, EP, CD-T, HAP) — establish method landscape
189	2. **Faithfulness evaluation** (Miller et al. 2024, Hanna et al. 2024) — motivate robustness concerns
190	3. **Circuit instability** (Méloux et al. 2025, Franco et al. 2026, Sun 2025) — establish the problem CSS solves
191	4. **Consensus/stability approaches** (CIRCUS, Certified Circuits) — position CSS against alternatives
192	5. **Feature-level circuits** (Sparse Feature Circuits, Transcoders, Circuit Tracing) — acknowledge parallel direction, note CSS works at component level
193	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da770f92-3650-4b8c-9e4a-af5b836f0f19",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "33bd13b6-c3bb-4894-b78e-d6f3175a3a9c",
  "sourceToolAssistantUUID": "da770f92-3650-4b8c-9e4a-af5b836f0f19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-13T09:56:55.724Z_

Now let me also look at the dream review reports to understand what simulated reviewers found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33bd13b6-c3bb-4894-b78e-d6f3175a3a9c",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNLxgLSPNVz4Aa2xjiE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc7a5003-ffd4-4c13-8be4-6ba566143cb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUBFfxfGHngTdPBNGBDKrf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13381,
      "cache_read_input_tokens": 51897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13381,
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

_source line 38 · 2026-05-13T09:56:57.993Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01MrGU4VK1QXQZHc1WeAVooL`</summary>

```json
{
  "pattern": "**/dream_reports/dream_20260513T092135/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc7a5003-ffd4-4c13-8be4-6ba566143cb5",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNLxgLSPNVz4Aa2xjiE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e9b7497-2420-4a7b-9b22-fa965ae7db0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUBFfxfGHngTdPBNGBDKrf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13381,
      "cache_read_input_tokens": 51897,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13381
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 51897,
          "cache_creation_input_tokens": 13381,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13381,
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

_source line 39 · 2026-05-13T09:56:58.006Z_

<details><summary>↩ Tool result · `toolu_01MrGU4VK1QXQZHc1WeAVooL`</summary>

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
artifacts/dream_reports/dream_20260513T092135/logs/review_best.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e9b7497-2420-4a7b-9b22-fa965ae7db0a",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "2923dd2c-26b6-41d9-bbd3-af28d09f2717",
  "sourceToolAssistantUUID": "3e9b7497-2420-4a7b-9b22-fa965ae7db0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-13T09:57:01.020Z_

<details open><summary>🔧 Tool call — Read · `toolu_015m46nhqQnxn16KUqnFEkTi`</summary>

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
  "parentUuid": "2923dd2c-26b6-41d9-bbd3-af28d09f2717",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNMKtYGUdkTbbqaQLCA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c01f49d2-aaed-4ba4-92f9-e7f7ab196313",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013kRVkLoQzaVb9Z1dEwcnrh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 917,
      "cache_read_input_tokens": 65278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 917,
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

_source line 41 · 2026-05-13T09:57:01.026Z_

<details><summary>↩ Tool result · `toolu_015m46nhqQnxn16KUqnFEkTi`</summary>

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
  "parentUuid": "c01f49d2-aaed-4ba4-92f9-e7f7ab196313",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "32c64b09-2874-4511-98f9-8e762e4f5473",
  "sourceToolAssistantUUID": "c01f49d2-aaed-4ba4-92f9-e7f7ab196313",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-13T09:57:01.507Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ja52QEiQsXeTtP8hmwHCwd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T092135/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32c64b09-2874-4511-98f9-8e762e4f5473",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNMKtYGUdkTbbqaQLCA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed84718a-3c67-45c9-a340-a636b17dde57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013kRVkLoQzaVb9Z1dEwcnrh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 917,
      "cache_read_input_tokens": 65278,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 917
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 65278,
          "cache_creation_input_tokens": 917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 917,
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

_source line 43 · 2026-05-13T09:57:01.515Z_

<details><summary>↩ Tool result · `toolu_01Ja52QEiQsXeTtP8hmwHCwd`</summary>

```text
1	# Paper Framing — structfuse-context
2	
3	> 最后更新: 2026-05-13 | 更新原因: D034 后 reframe 为分析论文（Route A）
4	
5	## Target Venue
6	EMNLP 2026 Findings (ARR deadline 2026-05-25)
7	
8	## Core Insight
9	Cross-method binary consensus in circuit discovery fails more often than it succeeds. Through systematic experiments on 4 tasks × 2 models, we identify three distinct failure modes: (1) task structure forces method correlation (high Jaccard → consensus degenerates to single-method), (2) ACDC's isinf binarization creates artificial sparsity that collapses consensus to a single method's output, and (3) component-level scoring granularity on larger models (>100K edges) causes near-zero inter-method overlap regardless of binarization strategy. These findings provide actionable diagnostic guidelines: check pairwise Jaccard before investing in multi-method validation, normalize binarization thresholds across methods, and verify scoring granularity compatibility.
10	
11	## Narrative Arc
12	1. Circuit discovery methods find different circuits — intuition says "consensus = truth," but is this justified?
13	2. We test this intuition systematically with CSS (binary consensus) across K=3 methods on multiple tasks and models
14	3. CSS succeeds in only 1 of 5+ configurations (IOI on GPT-2) — consensus mostly fails
15	4. We identify three mechanistic failure modes with distinct signatures
16	5. Negative results + failure mode taxonomy = actionable practitioner guidelines
17	
18	## Core Claims
19	
20	### Claim 1: ACDC isinf binarization pathology (METHODOLOGICAL — strongest)
21	- **Evidence**: CSS=1.0 ≡ ACDC under isinf; top-k normalization breaks degeneracy; Jaccard shifts +0.16 to +0.25 across tasks
22	- **Status**: Fully demonstrated on IOI + Arithmetic + SVA (3 tasks)
23	- **Strength**: ★★★★★ — concrete, reproducible, actionable
24	
25	### Claim 2: CSS fails on majority of task×model configurations (EMPIRICAL)
26	- **Evidence**: 1/5+ configurations show CSS=1.0 CPR advantage; failures include task-dependent (Arithmetic, SVA) and model-scaling (Qwen×2)
27	- **Status**: IOI PASS, Arithmetic FAIL, SVA inconclusive (D033), Qwen IFR FAIL, Qwen ACDC FAIL, Factual Recall pending
28	- **Strength**: ★★★★ — honest negative finding with systematic coverage
29	
30	### Claim 3: Component-level scoring causes scaling failure (MECHANISTIC)
31	- **Evidence**: On Qwen-0.5B (179K edges), both IFR and ACDC degenerate to node-level scoring; top-0.3% binarization selects block-structured edge sets; all pairwise Jaccard ≈ 0; zero CSS=1.0 edges
32	- **Status**: Demonstrated with two independent methods (IFR D028, ACDC D034)
33	- **Strength**: ★★★★ — root cause identified, not fixable by method substitution
34	
35	### Claim 4: Jaccard as necessary-condition diagnostic (PRACTICAL)
36	- **Evidence**: max Jaccard > 0.5 → CSS never helps (3/3 cases); max Jaccard < 0.35 → CSS helps (1/1 case, IOI); gap zone 0.35-0.50 inconclusive
37	- **Status**: Directionally supported but n too small for statistical significance. Framed as "motivated conjecture + practical heuristic," NOT as proven correlation
38	- **Strength**: ★★★ — honest about limitations, still useful as guideline
39	
40	### Claim 5: CIRCUS (within-method threshold diversity) fails completely (COMPARATIVE)
41	- **Evidence**: CIRCUS produces negative CPR on all tested tasks; cross-method consensus is necessary but not sufficient
42	- **Status**: D021 documented 3× failure
43	- **Strength**: ★★★ — negative ablation, depends on implementation correctness caveat
44	
45	## Anticipated Reviewer Concerns
46	
47	### R1: "This is just a negative result, what's the contribution?"
48	- **Response**: Three concrete contributions: (a) binarization pathology + fix, (b) scaling failure root cause (component-level scoring), (c) diagnostic guidelines. Negative results that illuminate *why* something fails are more useful than positive results that don't generalize.
49	
50	### R2: "CSS is just the feature selection stability index (Nogueira & Brown 2016)"
51	- **Response**: Acknowledged explicitly in Related Work. Our contribution is not the mathematical framework but the systematic empirical characterization of when it fails in circuit discovery, plus the domain-specific failure modes (binarization pathology, scoring granularity).
52	
53	### R3: "IOI positive result could be size effect"
54	- **Response**: Size-controlled baseline analysis (pending) directly addresses this. If confirmed as artifact, strengthens the negative finding narrative.
55	
56	### R4: "Only GPT-2 Small + Qwen 0.5B, limited model coverage"
57	- **Response**: Two models at different scales (32K vs 179K edges) already reveal the scaling failure. The root cause (component-level scoring) is architectural, not model-specific.
58	
59	### R5: "EAP-IG and EP are gradient-adjacent, K=3 is effectively K≈2"
60	- **Response**: This is part of our finding, not a limitation — even theoretically diverse methods (IFR, ACDC) fail to provide independent evidence at scale. Method correlation is structural, not accidental.
61	
62	### R6: "No confidence intervals on CPR differences"
63	- **Response**: Must add bootstrap CIs. IOI advantage of +0.08 needs statistical validation.
64	
65	## Competitors
66	- **CIRCUS** (Parekh 2026): Within-method threshold diversity; our negative ablation
67	- **Mondorf et al.** (2510.06811): Cross-method score averaging; must acknowledge continuous averaging may outperform binary consensus
68	- **PIE** (2604.16889): Iterative pruning ensemble; single paradigm
69	- **Nogueira & Brown** (JMLR 2016): Feature selection stability; CSS is domain application, must cite
70	- **Kuncheva & Whitaker** (2003): Ensemble diversity theory; theoretical foundation for our failure mode analysis
71	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed84718a-3c67-45c9-a340-a636b17dde57",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "40f171ef-0ebc-4118-9031-7e5566eb7430",
  "sourceToolAssistantUUID": "ed84718a-3c67-45c9-a340-a636b17dde57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-13T09:57:07.673Z_

Now I have a thorough understanding of the paper, its experimental results, related work landscape, and internal project history. Let me also check the ACDC binarization pathology claim more carefully, since the paper's framing evolved significantly and the original "Claim 1" (ACDC isinf pathology) seems to have been somewhat subsumed into the final paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40f171ef-0ebc-4118-9031-7e5566eb7430",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNMaimNuTDWmF9ys2vZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8d5971c-d712-4666-b2ef-7f7a47acff3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WymXV2tEr6622QMnJkGCYe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13702,
      "cache_read_input_tokens": 66195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13702,
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

_source line 45 · 2026-05-13T09:57:10.123Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CptW9sbBDDy1fs6DaqnSEJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T092135/median/paper.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8d5971c-d712-4666-b2ef-7f7a47acff3a",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNMaimNuTDWmF9ys2vZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f70ed941-270f-4e54-8b93-d33b6293984e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WymXV2tEr6622QMnJkGCYe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13702,
      "cache_read_input_tokens": 66195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13702,
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

_source line 46 · 2026-05-13T09:57:10.135Z_

<details><summary>↩ Tool result · `toolu_01CptW9sbBDDy1fs6DaqnSEJ`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f70ed941-270f-4e54-8b93-d33b6293984e",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "eaf7f9b6-71e4-4933-8a60-2a6402e66dd8",
  "sourceToolAssistantUUID": "f70ed941-270f-4e54-8b93-d33b6293984e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-13T09:57:13.424Z_

I now have comprehensive understanding of the paper, its development history, and the related work landscape. Let me now produce the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eaf7f9b6-71e4-4933-8a60-2a6402e66dd8",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNNELwgxR8dTrBLnLSy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "113113dd-0afa-497e-b337-46060c504780",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJDPTjf9wf2p5ZEXr94UeY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1469,
      "cache_read_input_tokens": 79897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1469,
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

_source line 48 · 2026-05-13T09:57:14.507Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EzCDXHvCZFAftXV995q7Lg`</summary>

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
  "parentUuid": "113113dd-0afa-497e-b337-46060c504780",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNNELwgxR8dTrBLnLSy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea3c390f-fb91-4c20-9fb8-17b3c52035c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJDPTjf9wf2p5ZEXr94UeY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1469,
      "cache_read_input_tokens": 79897,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1469
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 116,
          "cache_read_input_tokens": 79897,
          "cache_creation_input_tokens": 1469,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1469,
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

_source line 49 · 2026-05-13T09:57:14.510Z_

<details><summary>↩ Tool result · `toolu_01EzCDXHvCZFAftXV995q7Lg`</summary>

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
  "parentUuid": "ea3c390f-fb91-4c20-9fb8-17b3c52035c2",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "28841871-1624-4f00-a84c-f80e3baed46d",
  "sourceToolAssistantUUID": "ea3c390f-fb91-4c20-9fb8-17b3c52035c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-13T09:58:49.211Z_



Now I have all the information needed to write a thorough R2 review focused on Novelty and Related Work. Let me compile the review.

## R2 Review: Novelty & Related Work

### Summary (2-3 sentences)

This paper formalizes cross-method binary consensus in circuit discovery as the Circuit Selection Score (CSS), tests it across 4 tasks and 2 models (6 configurations), and finds that consensus succeeds in only 1/6 cases (IOI on GPT-2). The paper identifies three failure modes -- task-induced method correlation, component-level scoring degeneration at scale, and a Jaccard-based diagnostic predictor -- and reframes itself as a systematic negative-result analysis with practitioner guidelines.

### Strengths

- **S1: The negative result is genuinely informative.** The consensus hypothesis ("multi-method agreement = better circuits") is widely held but untested. Demonstrating systematic failure across 5/6 configurations, with mechanistic explanations for each failure mode, is a legitimate contribution. The field benefits from knowing when intuitive strategies break down, and the failure mode taxonomy (task-induced correlation vs. scoring degeneration vs. Jaccard-predictable failure) provides actionable structure.

- **S2: Clear differentiation from CIRCUS.** The paper correctly positions itself against its primary competitor (Parekh et al. 2026). CIRCUS varies pruning thresholds within a single attribution method (intra-method threshold diversity), while this paper varies across fundamentally different algorithmic paradigms (gradient vs. iterative patching vs. similarity). This distinction is real and well-articulated: method diversity captures a broader space of inductive biases than threshold variation. The paper also includes CIRCUS as a negative ablation (Claim 5 in the framing), which strengthens the positioning.

- **S3: Honest scoping and statistical reporting.** The paper commendably frames the Jaccard diagnostic as an "empirically supported heuristic" rather than a proven law, reports bootstrap CIs for all CPR comparisons, includes a size-controlled baseline for the sole positive result (retaining 76% of advantage), and acknowledges that n=6 is underpowered. This epistemic honesty is refreshing and appropriate for a Findings submission.

- **S4: The component-level scoring degeneration finding (Failure Mode 2) is novel and practically important.** Documenting that IFR degenerates to layer-level scoring due to GQA KV sharing and ACDC degenerates to node-level scoring at 179K edges -- making edge-level consensus semantically meaningless -- is a useful architectural insight that transcends this specific paper's framework.

### Weaknesses

- **W1: CSS is not a novel method; it is a direct application of the feature selection stability index (Nogueira & Brown 2016) and majority voting.** The paper acknowledges this ("Our contribution is not the mathematical framework"), but the acknowledgment does not fully resolve the novelty concern. CSS = (1/K) * sum(m_k(e)) is literally the Kuncheva-Nogueira stability index applied to binary edge masks. The entire "method" section (Section 3) could be replaced by a single sentence: "We apply the feature selection stability index to circuit discovery edge masks." The novelty must therefore rest entirely on the empirical findings and failure mode analysis -- which are interesting but thin at n=6.

- **W2: Insufficient engagement with Mondorf et al. (2025).** This is the most directly comparable work: they run EAP, EAP-IG, EP across the same tasks and compare union, intersection, mean, and hybrid aggregation strategies. Their finding that continuous score averaging (Mean) outperforms binary intersection (Min) directly undermines the CSS approach. The paper dismisses Mondorf et al. as a "workshop short paper" in the internal notes but the published paper cites it without engaging with its central finding. Key questions left unanswered: (a) Does continuous averaging succeed where binary consensus fails? (b) Is the binary vs. continuous distinction the real driver of failure, rather than the failure modes proposed here? (c) Mondorf et al. found Hybrid (EAP->EP pipeline) outperforms both -- how does this relate to the failure modes identified?

- **W3: The reference list is sparse for an EMNLP paper (14 references).** Several important works are missing:
  - **Bhaskar et al. (NeurIPS 2024 Spotlight)** -- the Edge Pruning paper itself is not cited, only the method is used. This is the foundational reference for one of the three methods.
  - **Meloux et al. (2025)** on intra-method instability (bootstrap Jaccard = 0.561 for EAP-IG) -- directly motivates why cross-method consensus might help and contextualizes the Jaccard values reported.
  - **Hanna et al. (2024, COLM)** -- "Have Faith in Faithfulness" introduces EAP-IG and shows overlap != faithfulness, which is directly relevant to the CSS premise.
  - **Miller et al. (2024, COLM)** -- faithfulness metrics are not robust, supporting the motivation for consensus.
  - **Franco et al. (2026)** -- prompt-specific circuits challenge the CSS framework's assumption of a single task-level circuit.
  - **Sharkey et al. (2025)** -- "Open Problems in MI" explicitly recommends reporting explanation ensembles, which CSS operationalizes.
  - **InterpBench (NeurIPS 2024 D&B)** -- semi-synthetic evaluation finding ACDC and EAP-IG statistically indistinguishable.
  - **Sun (2025, ACL)** -- circuit stability predicts generalization, complementary stability notion.
  - **Marks et al. (ICLR 2025 Oral)** -- sparse feature circuits at SAE level, parallel circuit abstraction.
  - **Nikankin et al. (BlackboxNLP 2025)** -- bootstrap EAP-IG for stability, closely related single-method stability approach.
  A typical EMNLP paper in this area would cite 30-40 references. 14 is well below the expected bar and signals incomplete awareness of the rapidly evolving field.

- **W4: The three methods used (EAP-IG, EP, ACDC) do not span three independent algorithmic families as claimed.** EAP-IG and EP are both gradient-based: EAP-IG computes integrated gradients of the attribution-patching objective, EP uses gradient-based optimization of binary edge masks. The paper claims "gradient / mask / greedy causal" as three families, but EP's mask optimization is gradient-driven. This means K=3 is effectively K~2 for the gradient dimension. The paper's own internal notes (D008, memory.md) acknowledge this: "EAP-IG + mask_gradient 同属 gradient." On GPT-2, the EAP-IG x EP Jaccard (0.307) is indeed the highest pairwise value in IOI, consistent with method adjacency. This weakens the claim that "consensus across three independent methods" was tested.

- **W5: n=6 configurations with 1 positive result is underpowered for the claims made.** The Jaccard diagnostic (Failure Mode 3) is presented with 5/6 accuracy and rho=-0.90 (p=0.037 excluding the outlier), but excluding the outlier to achieve significance is methodologically questionable -- the outlier is a legitimate data point representing a real failure mode. On all 6 points, rho=-0.714 with p=0.111 (not significant). The 0.35 and 0.50 Jaccard thresholds are derived from exactly 1 data point below 0.35 and 4 above 0.50, with zero points in between. These thresholds have no statistical grounding.

- **W6: The paper does not adequately engage with the broader XAI ensemble literature.** Multi-method comparison and agreement analysis is well-studied in explainable AI more broadly (e.g., comparing saliency maps across methods in computer vision). The circuit discovery framing is domain-specific, but the underlying question -- "when does multi-method agreement improve explanation quality?" -- has been explored in feature attribution, saliency mapping, and feature importance contexts. The paper treats this as if it is a novel question specific to mechanistic interpretability.

### Questions for Authors

- **Q1:** Mondorf et al. (2025) found that continuous score averaging outperforms both union and intersection. Have you tested whether continuous averaging succeeds in the configurations where binary CSS fails? If not, the failure modes you identify may be specific to binary consensus rather than cross-method agreement in general, which would significantly narrow the paper's contribution.

- **Q2:** The Jaccard diagnostic excludes the Qwen-ACDC outlier to achieve statistical significance (p=0.037 vs. p=0.111 on all 6 points). How do you justify this exclusion? The outlier represents a real, documented failure mode (component-level scoring degeneration). If the diagnostic requires knowing the failure mode a priori to exclude certain configurations, its practical utility as a "pre-check" is diminished -- practitioners would need to diagnose the failure mode before they can apply the diagnostic that is supposed to predict failure.

- **Q3:** The paper claims EAP-IG, EP, and ACDC represent three distinct algorithmic families ("gradient / mask / greedy causal"). Given that EP uses gradient-based optimization of masks, in what precise sense is it not gradient-based? The EAP-IG x EP Jaccard values consistently being the highest pairwise values across configurations suggests these methods share significant inductive biases.

- **Q4:** The sole positive result (IOI on GPT-2) is the most heavily studied circuit in the literature, with a well-characterized ground truth (Wang et al. 2023). Could the CSS success here simply reflect that IOI is an "easy" circuit where any reasonable method converges on the correct answer, rather than demonstrating a genuine advantage of consensus? The 12-edge ground truth circuit may be small enough that all methods reliably find it, making consensus trivially correct.

### Minor Issues

- The Kramar et al. citation (ref [4]) is labeled as "AtP*" but the paper actually uses Edge Pruning (Bhaskar et al. 2024), which is uncited. The Kramar reference appears to be for a different method than what is actually used in experiments.
- Table 1 reports "---" for SVA and Arithmetic CSS CPR values without explanation. If CSS=1.0 edges exist but are not reported, this should be clarified; if they do not exist, this should be stated explicitly.
- The paper_framing.md mentions "ACDC isinf binarization pathology" as the "strongest" claim, but the final paper (best tier) uses top-n binarization throughout, making the isinf pathology a methodological note rather than a core finding. The relationship between the paper's development history (where isinf was a major issue) and the final presentation is confusing.
- Section 2 paragraph on "Ensemble approaches" compresses 5 citations into 4 sentences. Each deserves more substantive engagement -- particularly CIRCUS, which receives one clause.
- The CIRCUS citation is incomplete (no author list beyond "Parekh et al.", no venue, placeholder format).
- PIE citation is "Anonymous" with an arXiv ID -- if it has an arXiv ID, the authors are presumably known.

### Scores

- **Soundness: 3.0/5** -- The experimental methodology is reasonable and the size-controlled baseline is well-designed, but the n=6 sample is insufficient for the Jaccard diagnostic claims, the exclusion of the outlier for significance is questionable, and the gradient-adjacency of EAP-IG/EP undermines the "three independent methods" framing. The core negative finding (consensus usually fails) is adequately supported.

- **Excitement: 2.5/5** -- The negative result is useful but not surprising: anyone familiar with ensemble methods would expect that binary intersection of correlated selectors underperforms the best individual selector. The failure mode taxonomy adds value, but the component-level scoring finding (FM2) is the only one that provides genuinely new insight. FM1 (high correlation -> consensus redundant) and FM3 (Jaccard predicts outcome) are largely restatements of the same observation.

- **Overall: 2.5/5** -- Borderline Findings. The paper addresses a real question and provides an honest negative answer, but the novelty is thin (CSS is a known stability index, the failure modes largely reduce to "correlated methods don't benefit from voting"), the related work coverage is inadequate for the venue, and the empirical scope (n=6, 2 models, K effectively ~2) limits the generalizability of the conclusions. With expanded related work, engagement with continuous aggregation alternatives, and 2-3 additional configurations to ground the Jaccard diagnostic, this could be a solid Findings paper.

- **Reproducibility: 4.0/5** -- Methods are well-specified (top-n binarization, bootstrap parameters, evaluation protocol). Code is not mentioned but the experimental setup is straightforward to replicate. The specific edge counts, Jaccard values, and CPR numbers are reported precisely.

- **Confidence: 4/5** -- I am quite familiar with the circuit discovery literature, feature selection stability theory, and ensemble methods. I have verified the key related work claims (CIRCUS, Mondorf et al., Nogueira & Brown) and am confident in the assessment of novelty gaps and missing citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28841871-1624-4f00-a84c-f80e3baed46d",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNNYUrf2j7JpMLcqLyF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5239543a-27bc-48f8-b638-d236a52b0331",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KAywpAbHNYzzwrzp3SJMMj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 81366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 694,
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

_source line 51 · 2026-05-13T09:59:15.774Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01M8HRx6rm5tT87558Smrzq4`</summary>

```json
{
  "report": "## R2 Review: Novelty & Related Work\n\n### Summary (2-3 sentences)\n\nThis paper formalizes cross-method binary consensus in circuit discovery as the Circuit Selection Score (CSS), tests it across 4 tasks and 2 models (6 configurations), and finds that consensus succeeds in only 1/6 cases (IOI on GPT-2). The paper identifies three failure modes -- task-induced method correlation, component-level scoring degeneration at scale, and a Jaccard-based diagnostic predictor -- and reframes itself as a systematic negative-result analysis with practitioner guidelines.\n\n### Strengths\n\n- **S1: The negative result is genuinely informative.** The consensus hypothesis (\"multi-method agreement = better circuits\") is widely held but untested. Demonstrating systematic failure across 5/6 configurations, with mechanistic explanations for each failure mode, is a legitimate contribution. The field benefits from knowing when intuitive strategies break down, and the failure mode taxonomy (task-induced correlation vs. scoring degeneration vs. Jaccard-predictable failure) provides actionable structure.\n\n- **S2: Clear differentiation from CIRCUS.** The paper correctly positions itself against its primary competitor (Parekh et al. 2026). CIRCUS varies pruning thresholds within a single attribution method (intra-method threshold diversity), while this paper varies across fundamentally different algorithmic paradigms (gradient vs. iterative patching vs. similarity). This distinction is real and well-articulated: method diversity captures a broader space of inductive biases than threshold variation. The paper also includes CIRCUS as a negative ablation (Claim 5 in the framing), which strengthens the positioning.\n\n- **S3: Honest scoping and statistical reporting.** The paper commendably frames the Jaccard diagnostic as an \"empirically supported heuristic\" rather than a proven law, reports bootstrap CIs for all CPR comparisons, includes a size-controlled baseline for the sole positive result (retaining 76% of advantage), and acknowledges that n=6 is underpowered. This epistemic honesty is refreshing and appropriate for a Findings submission.\n\n- **S4: The component-level scoring degeneration finding (Failure Mode 2) is novel and practically important.** Documenting that IFR degenerates to layer-level scoring due to GQA KV sharing and ACDC degenerates to node-level scoring at 179K edges -- making edge-level consensus semantically meaningless -- is a useful architectural insight that transcends this specific paper's framework.\n\n### Weaknesses\n\n- **W1: CSS is not a novel method; it is a direct application of the feature selection stability index (Nogueira & Brown 2016) and majority voting.** The paper acknowledges this (\"Our contribution is not the mathematical framework\"), but the acknowledgment does not fully resolve the novelty concern. CSS = (1/K) * sum(m_k(e)) is literally the Kuncheva-Nogueira stability index applied to binary edge masks. The entire \"method\" section (Section 3) could be replaced by a single sentence: \"We apply the feature selection stability index to circuit discovery edge masks.\" The novelty must therefore rest entirely on the empirical findings and failure mode analysis -- which are interesting but thin at n=6.\n\n- **W2: Insufficient engagement with Mondorf et al. (2025).** This is the most directly comparable work: they run EAP, EAP-IG, EP across the same tasks and compare union, intersection, mean, and hybrid aggregation strategies. Their finding that continuous score averaging (Mean) outperforms binary intersection (Min) directly undermines the CSS approach. The paper dismisses Mondorf et al. as a \"workshop short paper\" in the internal notes but the published paper cites it without engaging with its central finding. Key questions left unanswered: (a) Does continuous averaging succeed where binary consensus fails? (b) Is the binary vs. continuous distinction the real driver of failure, rather than the failure modes proposed here? (c) Mondorf et al. found Hybrid (EAP->EP pipeline) outperforms both -- how does this relate to the failure modes identified?\n\n- **W3: The reference list is sparse for an EMNLP paper (14 references).** Several important works are missing:\n  - **Bhaskar et al. (NeurIPS 2024 Spotlight)** -- the Edge Pruning paper itself is not cited, only the method is used. This is the foundational reference for one of the three methods.\n  - **Meloux et al. (2025)** on intra-method instability (bootstrap Jaccard = 0.561 for EAP-IG) -- directly motivates why cross-method consensus might help and contextualizes the Jaccard values reported.\n  - **Hanna et al. (2024, COLM)** -- \"Have Faith in Faithfulness\" introduces EAP-IG and shows overlap != faithfulness, which is directly relevant to the CSS premise.\n  - **Miller et al. (2024, COLM)** -- faithfulness metrics are not robust, supporting the motivation for consensus.\n  - **Franco et al. (2026)** -- prompt-specific circuits challenge the CSS framework's assumption of a single task-level circuit.\n  - **Sharkey et al. (2025)** -- \"Open Problems in MI\" explicitly recommends reporting explanation ensembles, which CSS operationalizes.\n  - **InterpBench (NeurIPS 2024 D&B)** -- semi-synthetic evaluation finding ACDC and EAP-IG statistically indistinguishable.\n  - **Sun (2025, ACL)** -- circuit stability predicts generalization, complementary stability notion.\n  - **Marks et al. (ICLR 2025 Oral)** -- sparse feature circuits at SAE level, parallel circuit abstraction.\n  - **Nikankin et al. (BlackboxNLP 2025)** -- bootstrap EAP-IG for stability, closely related single-method stability approach.\n  A typical EMNLP paper in this area would cite 30-40 references. 14 is well below the expected bar and signals incomplete awareness of the rapidly evolving field.\n\n- **W4: The three methods used (EAP-IG, EP, ACDC) do not span three independent algorithmic families as claimed.** EAP-IG and EP are both gradient-based: EAP-IG computes integrated gradients of the attribution-patching objective, EP uses gradient-based optimization of binary edge masks. The paper claims \"gradient / mask / greedy causal\" as three families, but EP's mask optimization is gradient-driven. This means K=3 is effectively K~2 for the gradient dimension. The paper's own experimental data supports this: EAP-IG x EP Jaccard (0.307 on IOI) is consistently the highest pairwise value across configurations. This weakens the claim that \"consensus across three independent methods\" was tested.\n\n- **W5: n=6 configurations with 1 positive result is underpowered for the claims made.** The Jaccard diagnostic (Failure Mode 3) is presented with 5/6 accuracy and rho=-0.90 (p=0.037 excluding the outlier), but excluding the outlier to achieve significance is methodologically questionable -- the outlier is a legitimate data point representing a real failure mode. On all 6 points, rho=-0.714 with p=0.111 (not significant). The 0.35 and 0.50 Jaccard thresholds are derived from exactly 1 data point below 0.35 and 4 above 0.50, with zero points in between. These thresholds have no statistical grounding.\n\n- **W6: The paper does not adequately engage with the broader XAI ensemble literature.** Multi-method comparison and agreement analysis is well-studied in explainable AI more broadly (e.g., comparing saliency maps across methods in computer vision). The circuit discovery framing is domain-specific, but the underlying question -- \"when does multi-method agreement improve explanation quality?\" -- has been explored in feature attribution, saliency mapping, and feature importance contexts. The paper treats this as if it is a novel question specific to mechanistic interpretability.\n\n### Questions for Authors\n\n- **Q1:** Mondorf et al. (2025) found that continuous score averaging outperforms both union and intersection. Have you tested whether continuous averaging succeeds in the configurations where binary CSS fails? If not, the failure modes you identify may be specific to binary consensus rather than cross-method agreement in general, which would significantly narrow the paper's contribution.\n\n- **Q2:** The Jaccard diagnostic excludes the Qwen-ACDC outlier to achieve statistical significance (p=0.037 vs. p=0.111 on all 6 points). How do you justify this exclusion? The outlier represents a real, documented failure mode (component-level scoring degeneration). If the diagnostic requires knowing the failure mode a priori to exclude certain configurations, its practical utility as a \"pre-check\" is diminished -- practitioners would need to diagnose the failure mode before they can apply the diagnostic that is supposed to predict failure.\n\n- **Q3:** The paper claims EAP-IG, EP, and ACDC represent three distinct algorithmic families (\"gradient / mask / greedy causal\"). Given that EP uses gradient-based optimization of masks, in what precise sense is it not gradient-based? The EAP-IG x EP Jaccard values consistently being the highest pairwise values across configurations suggests these methods share significant inductive biases.\n\n- **Q4:** The sole positive result (IOI on GPT-2) is the most heavily studied circuit in the literature, with a well-characterized ground truth (Wang et al. 2023). Could the CSS success here simply reflect that IOI is an \"easy\" circuit where any reasonable method converges on the correct answer, rather than demonstrating a genuine advantage of consensus? The 12-edge ground truth circuit may be small enough that all methods reliably find it, making consensus trivially correct.\n\n### Minor Issues\n\n- The Kramar et al. citation (ref [4]) is labeled as \"AtP*\" but the paper actually uses Edge Pruning (Bhaskar et al. 2024), which is uncited. The Kramar reference appears to be for a different method than what is actually used in experiments.\n- Table 1 reports \"---\" for SVA and Arithmetic CSS CPR values without explanation. If CSS=1.0 edges exist but are not reported, this should be clarified; if they do not exist, this should be stated explicitly.\n- The paper_framing.md mentions \"ACDC isinf binarization pathology\" as the \"strongest\" claim, but the final paper (best tier) uses top-n binarization throughout, making the isinf pathology a methodological note rather than a core finding. The relationship between the paper's development history and the final presentation is unclear.\n- Section 2 paragraph on \"Ensemble approaches\" compresses 5 citations into 4 sentences. Each deserves more substantive engagement -- particularly CIRCUS, which receives one clause.\n- The CIRCUS citation is incomplete (no author list beyond \"Parekh et al.\", no venue, placeholder format).\n- PIE citation is \"Anonymous\" with an arXiv ID -- if it has an arXiv ID, the authors are presumably known.\n\n### Scores\n\n- **Soundness: 3.0/5** -- The experimental methodology is reasonable and the size-controlled baseline is well-designed, but the n=6 sample is insufficient for the Jaccard diagnostic claims, the exclusion of the outlier for significance is questionable, and the gradient-adjacency of EAP-IG/EP undermines the \"three independent methods\" framing. The core negative finding (consensus usually fails) is adequately supported.\n\n- **Excitement: 2.5/5** -- The negative result is useful but not surprising: anyone familiar with ensemble methods would expect that binary intersection of correlated selectors underperforms the best individual selector. The failure mode taxonomy adds value, but the component-level scoring finding (FM2) is the only one that provides genuinely new insight. FM1 (high correlation -> consensus redundant) and FM3 (Jaccard predicts outcome) are largely restatements of the same observation.\n\n- **Overall: 2.5/5** -- Borderline Findings. The paper addresses a real question and provides an honest negative answer, but the novelty is thin (CSS is a known stability index, the failure modes largely reduce to \"correlated methods don't benefit from voting\"), the related work coverage is inadequate for the venue, and the empirical scope (n=6, 2 models, K effectively ~2) limits the generalizability of the conclusions. With expanded related work, engagement with continuous aggregation alternatives, and 2-3 additional configurations to ground the Jaccard diagnostic, this could be a solid Findings paper.\n\n- **Reproducibility: 4.0/5** -- Methods are well-specified (top-n binarization, bootstrap parameters, evaluation protocol). Code is not mentioned but the experimental setup is straightforward to replicate. The specific edge counts, Jaccard values, and CPR numbers are reported precisely.\n\n- **Confidence: 4/5** -- I am quite familiar with the circuit discovery literature, feature selection stability theory, and ensemble methods. I have verified the key related work claims (CIRCUS, Mondorf et al., Nogueira & Brown) and am confident in the assessment of novelty gaps and missing citations.",
  "project": "structfuse-context",
  "tier": "best",
  "dream_id": "dream_20260513T092135",
  "overall_score": "Borderline Findings (2.5/5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5239543a-27bc-48f8-b638-d236a52b0331",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNNYUrf2j7JpMLcqLyF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "700485c1-d27a-4903-82d3-bc8e333590e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KAywpAbHNYzzwrzp3SJMMj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 81366,
      "output_tokens": 6475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 694
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6475,
          "cache_read_input_tokens": 81366,
          "cache_creation_input_tokens": 694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 694,
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

_source line 52 · 2026-05-13T09:59:19.113Z_

<details><summary>↩ Tool result · `toolu_01M8HRx6rm5tT87558Smrzq4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T092135/best/review_report.md\", \"dream_id\": \"dream_20260513T092135\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "700485c1-d27a-4903-82d3-bc8e333590e0",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a801083aee3377eeb",
  "type": "user",
  "uuid": "c8864278-f3a3-4264-baf8-b7a13e611ba6",
  "sourceToolAssistantUUID": "700485c1-d27a-4903-82d3-bc8e333590e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-13T09:59:38.668Z_

Review submitted. Here is a summary of the key findings:

**Overall Assessment: Borderline Findings (2.5/5)**

The review identifies six weaknesses and four strengths, with the central tension being:

**Core novelty problem:** CSS is a direct application of the feature selection stability index (Nogueira & Brown 2016). The paper acknowledges this but does not fully resolve it -- the entire methodological contribution reduces to applying a known formula to circuit edge masks.

**Most critical weaknesses:**
1. **Insufficient engagement with Mondorf et al. (2025)** -- they tested continuous score averaging across the same methods and found it outperforms binary intersection, directly undermining CSS. The paper does not test whether continuous alternatives succeed where binary consensus fails.
2. **Only 14 references** for an EMNLP paper, missing ~10 important works including the Edge Pruning paper itself (Bhaskar et al. 2024), Meloux et al. on intra-method instability, Hanna et al. on EAP-IG, Miller et al. on faithfulness metric robustness, and the Open Problems paper (Sharkey et al. 2025).
3. **EAP-IG and EP are gradient-adjacent** (K=3 is effectively K~2), which the paper's own Jaccard data confirms.
4. **n=6 is underpowered** for the Jaccard diagnostic claims; excluding the outlier to achieve significance (p=0.037 vs p=0.111) is methodologically questionable.

**Key strengths:** The negative result is genuinely informative (S1), the CIRCUS differentiation is clear (S2), statistical reporting is honest (S3), and the component-level scoring degeneration finding is novel and practically important (S4).

The review was saved to `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T092135/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8864278-f3a3-4264-baf8-b7a13e611ba6",
  "isSidechain": true,
  "agentId": "a801083aee3377eeb",
  "requestId": "req_011CazNXj4bYgiTCta6ZTQ1y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b60440d5-a27f-481d-83c0-689f65ca65d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WsBDx1DpDBsjxcfWAdxBDQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6604,
      "cache_read_input_tokens": 82060,
      "output_tokens": 473,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6604
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 473,
          "cache_read_input_tokens": 82060,
          "cache_creation_input_tokens": 6604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6604,
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
