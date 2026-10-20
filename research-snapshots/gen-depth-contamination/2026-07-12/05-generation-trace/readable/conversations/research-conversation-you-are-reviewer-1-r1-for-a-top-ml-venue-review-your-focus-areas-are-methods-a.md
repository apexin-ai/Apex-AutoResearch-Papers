# Research conversation: You are Reviewer 1 (R1) for a top ML venue review. Your focus areas are **methods** and **experiments**. Use a 6-point s

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a326a0799fe55d2d5.jsonl`
- **Structured JSON:** [`c3ef10e9f5d41efd7f6d.json`](../../sessions/c3/c3ef10e9f5d41efd7f6d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-13T08:47:59.721Z_

You are Reviewer 1 (R1) for a top ML venue review. Your focus areas are **methods** and **experiments**. Use a 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept. Target venue acceptance rate ~25%.

## Paper Summary

**Title:** "Generational Depth Contamination: Measuring and Exploiting the Discrimination Boundary of Recursive Synthetic Text"

**Core idea:** Web training data is contaminated by recursively regenerated synthetic text. Existing detectors are binary (human vs machine). This paper formalizes recursive generation as an iterated lossy channel, invokes DPI to prove a finite "generational discrimination boundary" K* — the deepest generation at which pairwise depth discrimination remains statistically reliable. They then exploit the ordinal depth signal for "graduated filtering" that outperforms binary filtering.

**Claims:**
- C1 (K* Characterization): K*=2 for 1.5B models under standard decoding; K*≥3 at 7B scale and T=1.2. Greedy→K*=1 creates a controllable gradient.
- C3 (Graduated Filtering): K*-aware graduated filtering (human/gen-1/gen-2+ with α weighting) significantly outperforms binary filtering: +2.48pp MMLU, +2.70pp HellaSwag (p<0.01, 5 seeds). Gains scale monotonically with contamination rate.

**Method:**
- 15D hand-crafted features (vocabulary diversity, surprisal stats, tail distribution, structural) + LightGBM ordinal classifier
- Graduated filtering: w(x) = 1 if predicted human, α if predicted gen-1, 0 if predicted gen-2+
- θ=0.60 AUC threshold for K* definition

**Models:** Qwen2.5-1.5B-Instruct, Qwen2.5-1.5B (base), Qwen2.5-7B, Pythia-1.4B
**Data:** C4, 5K docs (1K for 7B)
**Generation:** Continuation mode, depth 0-5

**Key experimental results (from the paper's 15 tables):**

Table 1 – Decoding ablation (Qwen2.5-1.5B-Instruct):
- greedy: K*=1, AUC_1v2=0.5862
- nucleus p=0.9 T=1.0: K*=2, AUC_1v2=0.6278
- p=0.95 T=0.7: K*=2, AUC_1v2=0.6241
- baseline p=0.95 T=1.0: K*=2, AUC_1v2=0.6114
- p=0.95 T=1.2: K*=3, AUC_1v2=0.6823, AUC_2v3=0.6218

Table 2 – Feature ordering Spearman ρ ≥ 0.878 across configs

Table 3 – 7B vs 1.5B: 7B has AUC_1v2=0.6948, AUC_2v3=0.6175 → K*≥3
Table 4 – 7B bootstrap CI: 2v3 CI lower=0.6015 (barely above θ=0.60)

Table 5 – Base vs Instruct: both K*=2, base AUC_1v2=0.6382 vs instruct 0.6114

Table 6 – Retrain vs prompt chain (Pythia): K* identical, AUC diff < 2pp, cross-method transfer 91.5%
Table 7 – Feature JSD between methods: 0.0018–0.0378

Table 8 – 6 filtering strategies (5 seeds): graduated(α=0.5) = 29.41 MMLU / 47.08 HellaSwag, best by clear margin
Table 9 – Significance: graduated vs binary-ours p=0.0043 (MMLU), p=0.0067 (HellaSwag)
Table 10 – α sweep: inverted U, peak at α=0.5
Table 11 – Dose-response: Δ scales monotonically 0.72→2.48→3.82 (MMLU) with injection 10%→30%→50%

Table 12 – LLM zero-shot: GPT-4o acc=0.218, Claude=0.234 vs our classifier=0.423
Table 13 – Binary detectors: DivEye/Binoculars AUC_1v2 ≤ 0.528 vs our 0.634
Table 14 – 15D vs frozen embeddings: 15D wins (AUC_1v2 0.611 vs 0.598), 85% vs 62% cross-model transfer
Table 15 – Common Crawl: pred depth correlates with AlignScore (ρ=-0.288) and vocab richness (ρ=-0.342)

**Experiment coverage note:** The review_context.yaml lists these imagined experiments: exp-003 (decoding ablation), exp-004 (7B), exp-006 (graduated filtering), exp-008 (retrain-chain), exp-009 (dose-response), exp-011 (LLM zero-shot), exp-012 (binary detectors), exp-014 (Common Crawl), exp-015 (learned vs handcrafted), exp-016 (base vs instruct). The paper appears to cover ALL of these experiments.

## Your Task (R1: Methods + Experiments)

Produce a structured review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (bullet points, focus on methodological rigor, experimental design, statistical validity)
3. **Weaknesses** (bullet points, focus on methodological gaps, experimental limitations, statistical concerns)
4. **Detailed Comments** — address at minimum:
   - Is the DPI framing sound? Is the gap between DPI theory and the empirical K* definition well-handled?
   - Is θ=0.60 well-justified or arbitrary?
   - Are the sample sizes adequate (5K docs, 1K for 7B, 5 seeds)?
   - Statistical rigor: are CIs and p-values used appropriately? 7B 2v3 CI lower=0.6015 is barely above 0.60.
   - Is the graduated filtering evaluation convincing? (benchmarks, baselines, seeds)
   - Retrain-chain ecological validity: is LoRA rank=16 realistic?
   - Common Crawl validation: how strong is the evidence without ground truth?
   - Are there missing experiments or controls?
   - Feature design: is the 15D set well-motivated? Any concern about data leakage?
5. **Questions for Authors** (3-5 specific questions)
6. **Score** (1-6) with one-line justification
7. **Confidence** (1-5: 1=low, 5=expert)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "164300f2-6f9a-44c6-9734-333f563109ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T08:47:59.727Z_

```json
{
  "parentUuid": "164300f2-6f9a-44c6-9734-333f563109ac",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
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
  "uuid": "84ed726a-6047-4d5f-a566-60a2953030fc",
  "timestamp": "2026-05-13T08:47:59.727Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T08:48:03.360Z_



I'll start by reading the paper and all available project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84ed726a-6047-4d5f-a566-60a2953030fc",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH6Go1T837YhLsweeBz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82dc01c3-8de7-4480-b285-03534df9725c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BHYJMcdPXsf6UmrdJfFGBQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15841,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15841,
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

_source line 4 · 2026-05-13T08:48:04.493Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AKAPQbre2gGZe6eRnCmCHx`</summary>

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
  "parentUuid": "82dc01c3-8de7-4480-b285-03534df9725c",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH6Go1T837YhLsweeBz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a32edff-9b87-46a5-a934-13a628375dcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BHYJMcdPXsf6UmrdJfFGBQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15841,
      "cache_read_input_tokens": 0,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15841
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 142,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15841,
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

_source line 5 · 2026-05-13T08:48:04.501Z_

<details><summary>↩ Tool result · `toolu_01AKAPQbre2gGZe6eRnCmCHx`</summary>

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
  "parentUuid": "6a32edff-9b87-46a5-a934-13a628375dcb",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "cde1d31c-380d-4468-93c7-ae809b1a4b89",
  "sourceToolAssistantUUID": "6a32edff-9b87-46a5-a934-13a628375dcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T08:48:07.615Z_



Let me read the paper and project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cde1d31c-380d-4468-93c7-ae809b1a4b89",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH6dMWxJo8SdZth4nL5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1516f36-bef3-44fd-9918-f06f8e533b38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9BvwWVGg279wxuzBof9Qd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 15841,
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

_source line 7 · 2026-05-13T08:48:08.084Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01SC5HXNocCJBBGjMijZggUt`</summary>

```json
{
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1516f36-bef3-44fd-9918-f06f8e533b38",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH6dMWxJo8SdZth4nL5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd111f64-a6fb-44ea-b00f-9f7dc7763413",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9BvwWVGg279wxuzBof9Qd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 15841,
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

_source line 8 · 2026-05-13T08:48:08.146Z_

<details><summary>↩ Tool result · `toolu_01SC5HXNocCJBBGjMijZggUt`</summary>

```text
{"result":"# 项目 gen-depth-contamination 概况\n\n## 实验状态 (9 个)\n\n- **exp_013_cross_transfer**: DONE (success) — \n- **exp_005_degradation**: DONE (success) — \n- **exp_007_bootstrap_ci**: DONE (success) — \n- **exp_003_decoding_ablation**: RUNNING — \n- **exp_017_qwen_continuation**: DONE (success) — \n- **exp_010_ordinal_baseline**: DONE (success) — \n- **exp_002_olmo_depth**: DONE (success) — \n- **exp_001_pythia_depth**: DONE (success) — \n- **mvp_pilot_sat_v1**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-13\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_003_decoding_ablation | 解码策略调控 K*：不同 top_p/temperature 设置是否改变饱和边界（greedy→更低 K*? 高温度→更高 K*?） | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_013_cross_transfer** (success): Depth signal 是文本固有属性还是 model self-familiarity artifact？4×4 cross-model transfer matrix 测试分类器跨模型泛化能力\n- **exp_005_degradation** (success): —\n  [exp005_degradation_analysis](autodl-4090d:/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation/degradation_analysis.json)\n- **exp_007_bootstrap_ci** (success): K* 统计严谨性验证：bootstrap 95% CI 和 permutation test 确认 K*=2 在三个模型族上统计显著\n\n## 趋势\n成功 8 / 负向 0 / 失败 0 / 共 8\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-4090d: 空闲 cuda:0\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd111f64-a6fb-44ea-b00f-9f7dc7763413",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "518e9ce5-42cd-4ace-b8cb-3519cdda742c",
  "sourceToolAssistantUUID": "fd111f64-a6fb-44ea-b00f-9f7dc7763413",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T08:48:08.680Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0199ChHFTebistcquLmmxD75`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "518e9ce5-42cd-4ace-b8cb-3519cdda742c",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH6dMWxJo8SdZth4nL5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8629983-2bfc-4f99-b2b4-b52aae429e88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9BvwWVGg279wxuzBof9Qd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 15841,
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

_source line 10 · 2026-05-13T08:48:08.694Z_

<details><summary>↩ Tool result · `toolu_0199ChHFTebistcquLmmxD75`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/report.md\", \"content\": \"# Handover — 2026-05-13\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_003_decoding_ablation | 解码策略调控 K*：不同 top_p/temperature 设置是否改变饱和边界（greedy→更低 K*? 高温度→更高 K*?） | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **exp_013_cross_transfer** (success): Depth signal 是文本固有属性还是 model self-familiarity artifact？4×4 cross-model transfer matrix 测试分类器跨模型泛化能力\\n- **exp_005_degradation** (success): —\\n  [exp005_degradation_analysis](autodl-4090d:/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation/degradation_analysis.json)\\n- **exp_007_bootstrap_ci** (success): K* 统计严谨性验证：bootstrap 95% CI 和 permutation test 确认 K*=2 在三个模型族上统计显著\\n\\n## 趋势\\n成功 8 / 负向 0 / 失败 0 / 共 8\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-4090d: 空闲 cuda:0\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 811, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8629983-2bfc-4f99-b2b4-b52aae429e88",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "20483e6d-b8e8-4903-b2f0-e781e2b3a9bc",
  "sourceToolAssistantUUID": "a8629983-2bfc-4f99-b2b4-b52aae429e88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T08:48:11.655Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RnjvgwR4PysSq4mmH4tijK`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20483e6d-b8e8-4903-b2f0-e781e2b3a9bc",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH6wKWaV8GVxGoTcEQD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eae468d7-54b9-41a5-9e2b-eaf324eb3c3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxFVm1JuZwDwoX6fTmtw7s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1528,
      "cache_read_input_tokens": 17856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1528,
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

_source line 12 · 2026-05-13T08:48:11.664Z_

<details><summary>↩ Tool result · `toolu_01RnjvgwR4PysSq4mmH4tijK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md\", \"content\": \"# Paper Framing — gen-depth-contamination\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\\n- Fallback: EMNLP 2026 Findings\\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\\n\\n## Canonical Experimental Condition\\n\\n**Continuation mode 是 cross-model 结论的基础。**\\n\\n> \\\"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\\\"\\n\\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\\n|-----------|-------------|-------------|---------|\\n| Continuation | 91-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\\n\\n**原则**：\\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\\n- mvp-001 (Qwen-rewrite) 定位为 \\\"pilot study demonstrating feasibility\\\"，后续用 continuation mode rigorously validate\\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\\n\\n## Core Claims (2+1 结构, D012)\\n\\n### Primary: C1' (K* Characterization)\\n首次系统测量递归合成文本的 generational discrimination boundary K*。\\n\\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 4-model × 2-mode 实验矩阵系统表征 K*_empirical 的行为，包括跨模型一致性、特征退化排序、以及 generation mode 对 depth signal 的调控效应。\\n\\n**子组件：**\\n\\n**(a) K* = 2 across all tested configurations**\\n> 4-model 1v2 bootstrap 95% CI 汇总：\\n> | Model | AUC 1v2 | 95% CI | CI lower > 0.60? |\\n> |-------|---------|--------|-----------------|\\n> | Qwen-rewrite | 0.6955 | [0.6859, 0.7041] | ✅ (+8.6pp) |\\n> | Pythia-1.4B | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\\n> | OLMo-1B | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\\n> | Qwen-cont | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp, 最边缘) |\\n>\\n> - 全部 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60, 全部 permutation p < 0.002\\n> - K* 不是离散跳变值，而是 CI-bounded continuum threshold\\n> - Paper 可写：\\\"K*=2 (bootstrap 95% CI for AUC₁ᵥ₂ > 0.60 across all four model configurations; AUC₂ᵥ₃ CI upper < 0.60)\\\"\\n\\n**(b) Cross-model transfer**\\n> - Pythia↔OLMo 91% accuracy retention → K*=2 不是 model self-familiarity artifact\\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\\n> - 1v2+ transfer 取决于模型族相似度 → 与 K*=2 完美一致（K* 之上分辨力本就微弱）\\n> - depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity\\n\\n**(c) Degradation ordering consistency**\\n> - Spearman ρ ≥ 0.85 on single-feature AUC ranking（mode-controlled, continuation）\\n> - Top discriminative features shared: surp_d1_std, surp_std, surp_d2_std\\n> - Limitation: depth-pair level 一致性在 1v2 处较弱（τ~0.37）\\n> - Metric: single-feature AUC ranking（model-free, not LightGBM split count）\\n\\n**(d) Generation mode analysis (§4.x Analysis subsection)**\\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\\n> - 论文定位：Analysis subsection（\\\"How does generation mode affect depth estimation?\\\"），不是独立 claim\\n\\n### Secondary: C3 (Graduated Filtering)\\n即使在 K*=2 的粗粒度 ordinal signal（human/gen-1/gen-2+ 三级）下，K*-aware graduated filtering 仍优于 binary filtering，因为 ordinal signal 在阈值附近提供更 calibrated 的质量估计。\\n\\n### Supporting Analysis: Canonical Condition Selection\\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\\n\\n## Story Spine\\n\\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\\\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\\\"。通过 4-model × 2-mode 实验矩阵系统表征 K*，揭示控制因素（模型架构、解码策略、generation mode），为数据治理提供 actionable guidance。\\n- **Headline result template**: \\\"We establish K*=2 as the generational discrimination boundary for 1.5B-scale models under standard decoding, with depth features that are 70-85% text-intrinsic (Pythia↔OLMo 91% transfer retention). Even this coarse 3-class signal yields X% improvement over binary filtering on MMLU/HellaSwag.\\\"\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n1. **\\\"K*=2 太浅，graduated filtering 收益有限\\\"** → K* 是模型/解码策略依赖的；展示不同解码策略如何调控 K*（exp-003）；即使 K*=2，3-class 比 binary 在阈值附近更 calibrated（exp-006）\\n2. **\\\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\\\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ generation mode analysis，不是分类器本身\\n3. **\\\"Prompt-chain 不代表真实世界递归污染\\\"** → retrain-chain ecological validity check 作为补充；prompt-chain 是 controlled experiment 的标准方法\\n4. **\\\"单模型/单数据集，泛化性不够\\\"** → 3 个模型族 × 2 种 generation mode + 4×4 cross-model transfer matrix\\n5. **\\\"同模型做生成和 surprisal 计算有 bias\\\"** → **exp-013 直接反驳**：Pythia↔OLMo 91% accuracy retention，0v1 transfer AUC > 0.96。Depth signal 主要编码在文本而非 model self-familiarity\\n6. **\\\"为什么不用 learned representations\\\"** → 作为 baseline 对比；hand-crafted features 更 interpretable 且支持 degradation ordering 分析\\n7. **\\\"Graduated filtering 没和 data selection methods 比\\\"** → exp-006 包含 DSIR baseline + α sensitivity sweep\\n8. **\\\"K* 的统计不确定性未量化\\\"** → 4-model bootstrap CI + permutation test（exp-007）\\n\\n## Venue Fit\\n\\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\\n- 2+1 claim 结构：C1' 是 comprehensive characterization study，C3 是 practical application，generation mode analysis 增加深度\\n- 风险：如果审稿人偏 methods，K*=2 + standard classifier 可能被认为贡献不足 → 强调 problem formulation + characterization + transfer analysis 的 novelty\\n\", \"total_chars\": 6221, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eae468d7-54b9-41a5-9e2b-eaf324eb3c3a",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "b15be7f0-3153-4e9d-81dd-1823eff5d50b",
  "sourceToolAssistantUUID": "eae468d7-54b9-41a5-9e2b-eaf324eb3c3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T08:48:12.584Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019EKVQk4w5c6oyBeKcvAtaj`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b15be7f0-3153-4e9d-81dd-1823eff5d50b",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH6wKWaV8GVxGoTcEQD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da74a8cc-c889-4ada-b2d5-b42b35b0069b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxFVm1JuZwDwoX6fTmtw7s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1528,
      "cache_read_input_tokens": 17856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1528,
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

_source line 14 · 2026-05-13T08:48:12.595Z_

<details><summary>↩ Tool result · `toolu_019EKVQk4w5c6oyBeKcvAtaj`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'gen-depth-contamination'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da74a8cc-c889-4ada-b2d5-b42b35b0069b",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "7087ac3d-e72b-4739-bb04-58b7734f366d",
  "sourceToolAssistantUUID": "da74a8cc-c889-4ada-b2d5-b42b35b0069b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T08:48:13.083Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Pzeyc6TBhsRfYHucuR28Zg`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "ARCHITECTURE.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7087ac3d-e72b-4739-bb04-58b7734f366d",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH6wKWaV8GVxGoTcEQD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17a9b158-8aab-4f1a-b438-eed981713c13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxFVm1JuZwDwoX6fTmtw7s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1528,
      "cache_read_input_tokens": 17856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1528,
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

_source line 16 · 2026-05-13T08:48:13.096Z_

<details><summary>↩ Tool result · `toolu_01Pzeyc6TBhsRfYHucuR28Zg`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ARCHITECTURE.md found for 'gen-depth-contamination'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17a9b158-8aab-4f1a-b438-eed981713c13",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "0f5b7249-5592-46b4-988e-f0b17f05bc24",
  "sourceToolAssistantUUID": "17a9b158-8aab-4f1a-b438-eed981713c13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T08:48:13.630Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JDj6LMth5QK3HCvcCpjYCF`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f5b7249-5592-46b4-988e-f0b17f05bc24",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH6wKWaV8GVxGoTcEQD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18e90990-419a-4905-9a56-703c928548cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxFVm1JuZwDwoX6fTmtw7s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1528,
      "cache_read_input_tokens": 17856,
      "output_tokens": 382,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1528
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 382,
          "cache_read_input_tokens": 17856,
          "cache_creation_input_tokens": 1528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1528,
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

_source line 18 · 2026-05-13T08:48:13.651Z_

<details><summary>↩ Tool result · `toolu_01JDj6LMth5QK3HCvcCpjYCF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/decisions.yaml\", \"content\": \"_next_id: 14\\ndecisions:\\n- id: D001\\n  date: 2026-05-12 10:58 UTC\\n  summary: MVP 方案：Qwen2.5-1.8B + C4 5K docs 做 pilot saturation study，验证代际深度可分辨性\\n  rationale: Phase 0 pilot saturation study 是天然的 MVP gate——如果不同代际深度的文本在特征空间上不可区分，整个项目没有意义。选\\n    Qwen2.5-1.8B 因为体积小、开源、生成速度快。5K docs 足够统计显著性但不浪费 GPU。Pass 标准 K*≥3 对应至少 4 个有意义的类别（human/gen1/gen2/gen3+），AUC>0.70\\n    确保特征有实质区分力。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-12 15:10 UTC\\n  summary: MVP 初步结果 K*=2（边界），修复 right-padding 后重跑确认再锁路线\\n  rationale: AUC(2v3)=0.5797 距阈值 0.60 仅差 0.02，right-padding bug 可能系统性压低 K*。修复成本（1行代码+3h\\n    GPU）远低于错选路线的代价。\\n  related_experiments:\\n  - exp_id: mvp_pilot_sat_v1\\n    role: primary\\n    result: K*=2 (borderline), AUC(0v1)=0.9952, AUC(1v2)=0.6712, AUC(2v3)=0.5797\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-12 19:27 UTC\\n  summary: MVP Conditional Pass, K*=2, 锁定 Route B (Saturation Characterization), 进入\\n    research 阶段\\n  rationale: v3 definitive run 确认 K*=2：AUC(0v1)=0.9956, AUC(1v2)=0.6957, AUC(2v3)=0.5893(<0.60)。JSD\\n    严格单调递减支持 DPI 理论。Depth signal 存在但饱和在 depth 2-3。Route B 将 K* 本身定位为首次测量的基本科学量，比 Route\\n    A（depth classifier 可行性）更 robust——不依赖阈值选择。3-class 系统（human/gen-1/gen-2+）仍比 binary\\n    更有信息量。\\n  related_experiments:\\n  - exp_id: mvp_pilot_sat_v1\\n    role: primary\\n    result: K*=2, AUC(0v1)=0.9956, AUC(1v2)=0.6957, AUC(2v3)=0.5893, JSD monotonic\\n      decay\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-12 20:08 UTC\\n  summary: Reviewer 审查后修正：C1 区分 K*_empirical vs K*_theory；exp-013 (cross-model transfer)\\n    从 P1 提升至 P0\\n  rationale: Reviewer 指出 C1 混淆了经验值和理论值——实测 K*=2 是特定特征+分类器下的 practical boundary，不等于信息论\\n    impossibility boundary。更好的特征/分类器可能推高 K*。修正为\\\"K*_empirical 是 K*_theory 的保守下界\\\"。exp-013\\n    (cross-model transfer, 仅 2h) 直接回答审稿人最危险的攻击面：depth signal 是文本固有属性还是 model self-familiarity？Transfer\\n    失败则 C1 需根本调整。性价比极高，必须 P0。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 00:23 UTC\\n  summary: Dream 分析完成：proceed with P0, 整合 8 项确认行动到 framing/plan\\n  rationale: Dream 三档评分 Best=Weak Accept / Median=Borderline / Worst=Weak Reject。跨三档一致的结构性问题（通用建议）已整合：(1)\\n    IT/fundamental framing 已在 D004 校正，进一步软化 \\\"universal\\\" 措辞; (2) related work 扩展到 4\\n    方向; (3) exp-006 加 DSIR baseline + α ablation + 5 seeds; (4) exp-007 加 bootstrap\\n    CI + permutation-test; (5) exp-015 从 P2 升 P1; (6) 3-class accuracy 显式报告。6 项观察项待真实实验验证：Drayson\\n    et al. 存在性待查、cross-model transfer framing、domain sensitivity、method-code consistency、learned\\n    probe strength、cross-scale probe power。无需 re-dream——确认行动项均为增量调整，不改变 framing 结构。\\n  related_experiments:\\n  - exp_id: exp-006\\n    role: updated\\n    result: 加 DSIR baseline + α ablation + 5 seeds, GPU 48h→72h\\n  - exp_id: exp-007\\n    role: updated\\n    result: 加 bootstrap CI + permutation-test, GPU 1h→2h\\n  - exp_id: exp-015\\n    role: promoted\\n    result: P2→P1\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-13 00:58 UTC\\n  summary: '回滚 Drayson et al. 引用清理——Reviewer 确认为真实论文 (EMNLP 2025 #1506)'\\n  rationale: D005 中基于 web search 无结果将 Drayson et al. (2025) 判定为 Dream 幻觉引用并指示 Agent\\n    清理。Reviewer 独立核实找到 arXiv:2502.15654 + UCL Discovery PDF + GitHub repo，确认为真实发表论文。这是我们最相关的\\n    prior work（binary filtering 防 collapse），我们的 ordinal depth estimation 是其自然推广。教训：单次\\n    web search 不足以判定引用为幻觉，应交叉验证（arXiv ID + 作者机构 + 会议 proceedings）。\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-13 02:06 UTC\\n  summary: Drayson novelty 评估完成：核心 novelty 安全，Story Spine 微调，exp-006 加公平 binary baseline\\n  rationale: Reviewer 独立评估确认：(1) Drayson 做 binary detection 防 collapse（宏观训练动态），我们做\\n    ordinal depth estimation + K* measurement（单样本深度估计）——问题定义层面的扩展，非渐进改进；(2) Drayson\\n    100 代是训练迭代不是文本递归深度，不构成 novelty 威胁；(3) Story Spine 加入 Drayson 作为 closest prior\\n    work 但保持 gap statement 完整；(4) exp-006 加 binary-ours baseline（同 15D 特征做 binary，唯一变量\\n    = binary/ordinal），确保 C3 对比公平。\\n  related_experiments:\\n  - exp_id: exp-006\\n    role: updated\\n    result: 加 binary-ours 公平对比 baseline\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-13 02:45 UTC\\n  summary: C2 claim 暂停写入论文——等 exp-017 解耦 generation mode 因素后决定措辞\\n  rationale: exp-005 结果显示 Kendall τ 仅 Pythia-OLMo 达 0.8476（≥0.8），Pythia-Qwen 0.5238、OLMo-Qwen\\n    0.4857 均不达标。1/3 通过率不支持 C2 当前 \\\"τ≥0.8 across all tested families\\\" 的表述。关键混杂因素：Pythia/OLMo\\n    用 continuation 模式，Qwen 用 rewrite 模式。exp-017（Qwen continuation，~4h 后完成）将区分是 mode-dependent\\n    还是 model-dependent。若 Qwen continuation τ≥0.8 → C2 限定为 \\\"consistent within continuation\\n    mode\\\"；若仍低 → C2 大幅弱化为 \\\"partially consistent\\\" 或限定 base model 范围。\\n  related_experiments:\\n  - exp_id: exp-005\\n    role: evidence\\n    result: partial_consistency_1of3_pairs\\n  - exp_id: exp-017\\n    role: pending_resolution\\n    result: running\\n  depends_on: []\\n- id: D009\\n  date: 2026-05-13 03:35 UTC\\n  summary: C2 战略评估：C1 是承重墙，C3 是安全网，C2 是加分项；exp-016 列为场景 B 应急\\n  rationale: 'Reviewer 深度评估指出第三混杂因素：instruct-tuning。Qwen-Instruct vs Pythia/OLMo base\\n    的差异不仅是 generation mode。exp-017 无法完全解耦 mode 和 instruct-tuning 的联合效应。场景 A (τ≥0.8):\\n    C2 改为 mode-dependent insight (7/10)，可撑 EMNLP Main。场景 B (τ<0.7): C2 降级为 supplementary\\n    finding (3/10)，C1+C3 仍可投 Main/Findings，取决于 C3 效果大小。exp-006 (graduated filtering)\\n    优先级应提升作为 C2 弱化的安全网。exp-016 (Qwen base continuation) 作为场景 B 应急实验预备——可解耦 instruct-tuning\\n    vs architecture 效应，仅 6h GPU。'\\n  related_experiments:\\n  - exp_id: exp-005\\n    role: evidence\\n    result: partial_consistency\\n  - exp_id: exp-017\\n    role: pending_resolution\\n    result: running\\n  - exp_id: exp-006\\n    role: priority_elevated\\n    result: planned\\n  - exp_id: exp-016\\n    role: contingency_scenario_B\\n    result: planned\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-13 06:20 UTC\\n  summary: C2 Plan A 否决 → 执行 Plan B：degradation ordering 限定为 \\\"within architecture\\n    family\\\"，降级为 supplementary finding\\n  rationale: exp-017 (Qwen continuation) 结果明确：控制 generation mode 后，Qwen top feature\\n    仍是 freq_entropy（vs Pythia/OLMo 的 surp_d1_mean）。分歧是 model-dependent 而非 mode-dependent。按\\n    D009 预案，C2 降级为 supplementary finding，措辞改为 \\\"feature degradation ordering consistent\\n    within architecture family (base models τ=0.85), but diverges across architecture\\n    types\\\"。同时发现 generation mode effect 很大（rewrite→continuation AUC 1v2 下降 0.084），论文需增加\\n    mode effect 讨论段。C1 不受影响（4/4 条件 K*=2）。C3 重要性提升为论文第二支柱。\\n  related_experiments:\\n  - exp_id: exp-017\\n    role: decisive_evidence\\n    result: plan_a_rejected\\n  - exp_id: exp-005\\n    role: initial_evidence\\n    result: partial_consistency\\n  depends_on:\\n  - D008\\n  - D009\\n- id: D011\\n  date: 2026-05-13 06:24 UTC\\n  summary: D010 修正：C2 从 \\\"supplementary\\\" 升级为 \\\"qualified claim\\\"——使用 single-feature AUC\\n    + Spearman ρ≥0.85 + mode-controlled 条件\\n  rationale: 'Reviewer 4-model 降解分析修正了此前结论。LightGBM split count 和 single-feature AUC\\n    给出矛盾排名：split count 显示 Qwen-cont freq_entropy #1（与 Pythia/OLMo 分歧），但 single-feature\\n    AUC 显示 Qwen-cont top-3 与 Pythia/OLMo 完全一致（surp_d1_std, surp_std, surp_d2_std）。Single-feature\\n    AUC 更直接衡量代际区分力，更适合 C2 语义。Spearman ρ: Pythia-OLMo=0.95, Pythia-Qwen_cont=0.9143,\\n    OLMo-Qwen_cont=0.85——全部≥0.85。C2 可行路径：(1) 用 single-feature AUC ranking 定义 ordering；(2)\\n    用 Spearman ρ≥0.85 作为一致性阈值；(3) 限定 mode-controlled 条件；(4) 透明报告 depth-pair level\\n    差异（1v2 对 τ 仅 0.35-0.39）和 τ vs ρ 选择理由。风险：depth-pair 1v2 一致性差（τ~0.37），审稿人可能做 depth-stratified\\n    分析。'\\n  related_experiments:\\n  - exp_id: exp-005\\n    role: 4model_reanalysis\\n    result: rho_ge_0.85_all_pairs\\n  - exp_id: exp-017\\n    role: mode_control\\n    result: convergence_confirmed\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-13 07:29 UTC\\n  summary: 论文 claim 重构：4 claims → 2+1 结构（C1' K* characterization + C3 graduated filtering\\n    + supporting analysis）\\n  rationale: Reviewer 评估指出 4 claims (C1/C2/C3/C4) 对 EMNLP Main 太散，每个不够厚。重构为：Primary\\n    C1' = 首次系统测量 K*_empirical（含 DPI 理论 + 4-model 验证 + cross-model transfer + degradation\\n    ordering + generation mode analysis）；Secondary C3 = graduated filtering > binary；Supporting\\n    = generation mode effect + metric analysis 作为 §4.4 subsection。C4 从独立 claim 降级为方法论洞见（Canonical\\n    Condition Selection），C2 ordering 融入 C1' characterization。Canonical condition framing：continuation\\n    mode 作为 cross-model 基础，MVP rewrite 定位为 pilot study。exp-006 是关键路径：exp-003 完成后立即启动，72h\\n    GPU，deadline 05-25 ARR 倒推无延迟容忍。\\n  related_experiments:\\n  - exp_id: exp-013\\n    role: evidence_for_restructure\\n    result: mode_effect_is_methodological\\n  - exp_id: exp-006\\n    role: critical_path\\n    result: planned\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-13 07:37 UTC\\n  summary: C3 exp-006 单点依赖风险评估 + fallback story 预案\\n  rationale: Reviewer 正确指出 C3 (graduated filtering) 完全依赖 exp-006 单个实验。Fallback 预案：(1)\\n    如果 graduated 显著优于 binary → C3 成立，2+1 claim 结构完整；(2) 如果 graduated ≈ binary（无统计显著差异）→\\n    C3 改为 informative negative：\\\"K*=2 的粗粒度 ordinal signal 不足以在 downstream 层面超越 binary\\\"，论文\\n    story 调整为纯 characterization paper（C1' 独立支撑），graduated filtering 作为 negative result\\n    讨论（对论文质量有加分，EMNLP 重视 negative findings）；(3) 如果 graduated 比 binary 差 → 同场景 2，额外分析原因（3-class\\n    ordinal noise vs binary robustness）。场景 1 是预期结果（K* 附近 ordinal signal 提供更 calibrated\\n    的质量估计），但场景 2 也不致命——C1' 本身有足够深度（K* characterization + degradation ordering + mode\\n    effect + cross-model transfer）。关键行动：exp-003 完成后 GPU 零间隔切换 exp-006，不容任何空转。\\n  related_experiments:\\n  - exp_id: exp-006\\n    role: target\\n    result: planned\\n  - exp_id: exp-003\\n    role: predecessor\\n    result: running\\n  depends_on:\\n  - D012\\n\", \"total_chars\": 9371, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18e90990-419a-4905-9a56-703c928548cc",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "9a41cac8-e30d-4476-b9bc-7b17aeb2e722",
  "sourceToolAssistantUUID": "18e90990-419a-4905-9a56-703c928548cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T08:48:17.492Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RuRkc7vF3r5jBM6zCGUDtA`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a41cac8-e30d-4476-b9bc-7b17aeb2e722",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH7JUjwxXSAJngEKHSF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3507e72-47aa-45ad-a070-cd910caed644",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V7hYnUkKHQ4sTt5YyMSRoH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8735,
      "cache_read_input_tokens": 19384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8735,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 20 · 2026-05-13T08:48:17.503Z_

<details><summary>↩ Tool result · `toolu_01RuRkc7vF3r5jBM6zCGUDtA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/memory.md\", \"content\": \"# Memory — gen-depth-contamination\\n\\n## 已知问题\\n\\n### right-padding (2026-05-12)\\nMVP pipeline 使用 right-padding（transformers 默认）。Director 确认对 MVP 判定无影响（所有 depth 一致受影响），不中断当前实验。**full study 阶段必须修复为 `tokenizer.padding_side = \\\"left\\\"`**，否则 batch 生成时 padding tokens 会影响生成质量的绝对水平。\\n\\n## GPU 优化建议 (2026-05-12)\\n\\n### batch size 调优\\n4090D 24GB 跑 1.5B fp16 模型仅用 3.9GB 显存 (16%)，GPU 利用率 45%。\\n- Step 3 生成：batch_size 16→**64**（保守）或 128\\n- Step 4 特征提取：feat_batch_size 8→**24**（保守）或 32\\n- 预估节省 ~74 min (38%)，加 flash-attn 可再省 10-15%\\n- full study 时一并修复\\n\\n## AutoDL 环境经验\\n\\n### C4 数据集加载 (2026-05-12)\\nAutoDL 代理下 `load_dataset(\\\"allenai/c4\\\", \\\"en\\\", streaming=True)` 会触发全量文件树解析（数千个 shard 的分页 API 请求），ProxyError 无限重试。修复：用单 shard URL 直接加载 + `HF_ENDPOINT=https://hf-mirror.com` 中转。\\n\\n### 环境变量必须固化到启动脚本 (2026-05-12)\\nAutoDL 上 `source /etc/network_turbo`、SSL 证书、HF 配置等环境变量不能只在 shell session 里 export，必须写入 `run_mvp.sh` 等包装脚本，否则 tmux session 里不生效。\\n\\n### submit_training_job pid=\\\"unknown\\\" 问题 (2026-05-13)\\nsubmit_training_job 有时返回 pid=\\\"unknown\\\"，导致 registry 状态停在 PREPARING、cron 未创建。exp-017 和 exp-003 都遇到此问题。**解决方式**：提交后必须派 Worker SSH 检查实际进程状态（tmux ls + ps aux），手动修正 registry 并注册 cron。\\n\\n## 实验设计决策\\n\\n### Generation mode 影响 depth signal 强度 (2026-05-13)\\nRewrite mode（instruction prompting）比 continuation mode 多产生 ~8.4pp AUC 差距（Qwen: 0.6957 vs 0.6114）。原因推测：instruction-following 引入更大的分布偏移，放大 depth-discriminative 信号。论文中 K* 应同时报告两种 mode 的结果；C1 robustness 依赖 continuation mode（更保守的 lower bound）。\\n\\n### Degradation ordering mode-dependent (2026-05-13)\\n4-model τ 矩阵表明 generation mode 贡献 ~60-70% 的排序偏离，架构 ~30-40%。C2 claim 不能说 \\\"universal ordering\\\"，应改为 \\\"mode-conditioned consistency with architecture residuals\\\"。Director 决策 D008 的后续：4-model τ 数据已齐全，等 Director 确认 C2 最终措辞。\\n\", \"total_chars\": 1706, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3507e72-47aa-45ad-a070-cd910caed644",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "1e82cfbc-b213-414e-b1e6-5fee241dfd82",
  "sourceToolAssistantUUID": "f3507e72-47aa-45ad-a070-cd910caed644",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T08:48:18.041Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0153bTpac4BaRjaHRrNXje1r`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e82cfbc-b213-414e-b1e6-5fee241dfd82",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH7JUjwxXSAJngEKHSF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "298ccc32-7b26-4700-b5c0-e4f36a25b859",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V7hYnUkKHQ4sTt5YyMSRoH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8735,
      "cache_read_input_tokens": 19384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8735,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 22 · 2026-05-13T08:48:18.050Z_

<details><summary>↩ Tool result · `toolu_0153bTpac4BaRjaHRrNXje1r`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/literature_map.yaml\", \"content\": \"papers:\\n  # === Must-Cite ===\\n\\n  - id: drayson2025\\n    title: \\\"Machine-generated text detection prevents language model collapse\\\"\\n    authors: \\\"Drayson, Yilmaz, Lampos\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2502.15654\\\"\\n    code: \\\"https://github.com/GeorgeDrayson/model_collapse\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Binary MGT detection + importance resampling for collapse prevention; our depth estimator generalizes their binary detector to ordinal depth\\\"\\n    cited: false\\n    methodology: >\\n      Binary MGT detector (encoder-only transformer + classification head; best: ModernBERT-150M, AUC .986 in-dist, .943 OOD).\\n      Fine-tuned 5 epochs with label smoothing α=0.1 + temperature scaling.\\n      Sampling Importance Resampling (SIR): w_j = (1-q(x_j))^b / Σ(1-q(x_l))^b, where q(x) = P(machine-generated), b≥1 bias term.\\n      Resample at k=1.5 (50% upsampling). Evaluated on GPT-2 and SmolLM2 (124M–1.7B).\\n    key_findings:\\n      - \\\"SIR filtering not only prevents collapse but improves over human-only training (perplexity -0.85% to -25.65%, diversity +3.44% to +14.62%, MAUVE +8.46% to +20.92%)\\\"\\n      - \\\"ModernBERT achieves best detection (AUC .986 in-dist); optimal threshold 0.8674 on imbalanced data (29% human)\\\"\\n      - \\\"Curated synthetic data has positive value — outperforms oracle (perfect filter) in equal-ratio settings\\\"\\n      - \\\"Only evaluates fine-tuning (not pretraining), models ≤2B, open-ended generation only\\\"\\n    positioning_notes: >\\n      Closest prior work. Their SIR is a special case of our graduated filtering when K*=1 (binary: human vs all synthetic).\\n      We generalize binary→ordinal: estimate depth d∈{0,1,...,K*} and apply depth-graduated weights.\\n      K* tells when ordinal signal adds value over binary. They never discuss ordinal depth or multi-class estimation.\\n      Our C3 claim directly extends their framework: \\\"even coarse 3-class signal yields better calibration at decision boundaries.\\\"\\n\\n  - id: schaeffer2025position\\n    title: \\\"Position: Model Collapse Does Not Mean What You Think\\\"\\n    authors: \\\"Schaeffer, Kazdan, Arulandu, Koyejo\\\"\\n    venue: \\\"ICML 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2503.03150\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"framing-critical\\\"\\n    relevance: \\\"Identifies 8 definitions of model collapse across 3 families; forces us to position K* as discriminability saturation (distribution deformation), not test-loss collapse\\\"\\n    cited: false\\n    methodology: >\\n      Position paper. Surveys model collapse literature and identifies 8 distinct definitions organized in 3 families.\\n      Evaluates each definition against realistic deployment conditions. No experiments—purely analytical/argumentative.\\n    key_findings:\\n      - \\\"8 definitions in 3 families: (A) Population risk degrading [D1: catastrophic increase, D2: any increase, D3: asymptotic divergence]; (B) Distributions deforming [D4: collapsing variance, D5: scaling law change, D6: mode disappearance/entanglement, D7: tail data loss]; (C) Spurious generation [D8: hallucinated data]\\\"\\n      - \\\"Under realistic conditions (data accumulation, growing compute), catastrophic risk divergence (D1-D3) is avoidable\\\"\\n      - \\\"Real harms—tail data loss (D7) and mode entanglement (D6)—have received disproportionately less attention\\\"\\n      - \\\"Recommends researchers explicitly state which definition they study\\\"\\n    positioning_notes: >\\n      K* belongs to Family B (distributions deforming), specifically D4 (collapsing variance) + D6 (mode entanglement).\\n      K* measures when distribution deformation renders generations indistinguishable in feature space.\\n      K* is NOT about population risk (Family A). This distinction is critical for framing:\\n      we contribute a diagnostic for exactly the harms Schaeffer et al. identify as underexplored.\\n      Adopt their taxonomy explicitly in Related Work to anchor K* precisely.\\n\\n  - id: kazdan2025collapse\\n    title: \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\"\\n    authors: \\\"Kazdan, Schaeffer, Dey, Gerstgrasser, Rafailov, Donoho, Koyejo\\\"\\n    venue: \\\"ICML 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2410.16713\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Accumulate vs replace regimes affect contamination dynamics; in accumulate regime K* may shift upward\\\"\\n    cited: false\\n    methodology: >\\n      Formal comparison of 3 data regimes: Replace (train on latest synthetic only; Σ→0 a.s.),\\n      Accumulate (train on all historical data; real fraction→0 but stability holds),\\n      Accumulate-subsample (fixed budget from accumulated pool; intermediate degradation).\\n      Theory: Gaussian setting with closed-form limits. Experiments: multivariate Gaussian, KDE, LLM SFT (Gemma2-2B on HelpSteer2/TinyStories).\\n    key_findings:\\n      - \\\"Replace: covariance collapses to 0 (a.s.), W2 diverges. Collapse inevitable within 5-10 iterations\\\"\\n      - \\\"Accumulate: covariance stabilizes at σ₀²·sin(π/√n)/(π/√n). No collapse even as real data fraction→0\\\"\\n      - \\\"Accumulate-subsample: degradation plateaus rather than diverges\\\"\\n      - \\\"Cardinality of real data matters more than proportion (R²=0.59 vs 0.34)\\\"\\n    positioning_notes: >\\n      Our prompt-chain = replace regime (harshest setting). K*=2 measured under replace conditions.\\n      This makes K*=2 a conservative lower bound: under accumulate regime (more realistic), K* would shift upward.\\n      Strengthens our result: if depth estimation adds value at K*=2 under replace, it adds more under accumulate.\\n      Cite to justify experimental design and contextualize K* as regime-dependent.\\n\\n  - id: shi2025generalization\\n    title: \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\"\\n    authors: \\\"Shi, Wu, Zhang, Zhang, Tao, Qu\\\"\\n    venue: \\\"NeurIPS 2025 Spotlight\\\"\\n    url: \\\"https://arxiv.org/abs/2509.16499\\\"\\n    code: \\\"https://shilianghe007.github.io/model-collapse/\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Generalization-to-memorization transition in iterative retraining parallels our feature-space convergence; entropy decrease over iterations aligns with our depth-discriminative features\\\"\\n    cited: false\\n    methodology: >\\n      Study iterative retraining of diffusion models (DDPM) on CIFAR-10 subsets (1K–32K images).\\n      Generalization Score (GS): avg distance between generated and nearest training image.\\n      Entropy: Kozachenko-Leonenko estimator. Strong correlation: Pearson r=0.91 between entropy and log(GS).\\n      Mitigation: entropy-based data selection (greedy max-NN-distance + threshold-decay filter).\\n    key_findings:\\n      - \\\"GS drops approximately exponentially across iterations; collapse within 5-10 iterations for large datasets\\\"\\n      - \\\"Training data entropy is a direct predictor of generalization capability (r=0.91)\\\"\\n      - \\\"Entropy-based data selection mitigates memorization transition\\\"\\n      - \\\"Diffusion models only; no LLM experiments. No theoretical analysis of WHY entropy collapses\\\"\\n      - \\\"Generated images form tight local clusters while overall variance remains relatively stable\\\"\\n    positioning_notes: >\\n      Parallel phenomenon across modalities: their entropy decline ↔ our JSD decrease (0.27→0.004).\\n      Their \\\"GS drops exponentially\\\" ↔ our feature-space divergence vanishes rapidly → K*=2.\\n      Key distinction: they measure output-distribution entropy; we measure discriminability in feature space.\\n      K* complements their entropy metric: operationalizes \\\"at what depth does entropy decline = indistinguishability?\\\"\\n      Their clustering-while-variance-stable parallels our depth features converging before global statistics.\\n      Cite for cross-modal validation of convergence phenomenon.\\n\\n  # === Should-Cite ===\\n\\n  - id: basani2026diveye\\n    title: \\\"DivEye: Diversity Boosts AI-Generated Text Detection\\\"\\n    authors: \\\"Basani, Chen\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2509.18880\\\"\\n    code: \\\"https://github.com/IBM/diveye\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Surprisal diversity features as potential baseline for depth estimation; zero-shot detector outperforms prior work by 33.2%\\\"\\n    cited: false\\n\\n  - id: amin2025escaping\\n    title: \\\"Escaping Collapse: The Strength of Weak Data for Large Language Model Training\\\"\\n    authors: \\\"Amin et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2502.08924\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Boosting-inspired framework showing weak signal suffices for iterative training; motivates practical utility of imperfect depth estimators\\\"\\n    cited: false\\n\\n  - id: zawalski2026codec\\n    title: \\\"CoDeC: Detecting Data Contamination in LLMs via In-Context Learning\\\"\\n    authors: \\\"Zawalski et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2510.27055\\\"\\n    category: \\\"contamination\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Binary contamination detection via ICL confidence shifts; complementary to our finer-grained depth estimation approach\\\"\\n    cited: false\\n\\n  - id: gambetta2025surplexity\\n    title: \\\"Learning by Surprise: Surplexity for Mitigating Model Collapse\\\"\\n    authors: \\\"Gambetta et al.\\\"\\n    venue: \\\"arXiv preprint 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2410.12341\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Surprise-based collapse metric; surplexity scores as potential feature for depth estimation pipeline and baseline comparison\\\"\\n    cited: false\\n\\n  - id: zhang2024minkpp\\n    title: \\\"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\\\"\\n    authors: \\\"Zhang, Zheng, Gao, Miao\\\"\\n    venue: \\\"EMNLP 2024\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Binary detection baseline; does not distinguish generational depth\\\"\\n    cited: false\\n\\n  - id: shumailov2024collapse\\n    title: \\\"AI models collapse when trained on recursively generated data\\\"\\n    authors: \\\"Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal\\\"\\n    venue: \\\"Nature 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Seminal model collapse result; describes macro phenomenon but provides no detection tool for depth\\\"\\n    cited: false\\n\\n  - id: alemohammad2024selfconsuming\\n    title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n    authors: \\\"Alemohammad, Casco-Rodriguez, Luber, Babaei, Letizia, Bastani, Baraniuk\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Theoretical and empirical analysis of iterative generative training; complements Shumailov with formal convergence analysis\\\"\\n    cited: false\\n\\n  - id: dohmatob2024model\\n    title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n    authors: \\\"Dohmatob, Feng, Yang, Charton, Kempe\\\"\\n    venue: \\\"ICML 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Scaling law perspective on collapse; tail distribution loss aligns with our observed feature convergence\\\"\\n    cited: false\\n\\n  - id: xie2023dsir\\n    title: \\\"Data Selection with Importance Resampling\\\"\\n    authors: \\\"Xie, Santurkar, Ma, Liang\\\"\\n    venue: \\\"ICML 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Distribution-matching data selection baseline; does not estimate recursive depth\\\"\\n    cited: false\\n\\n  - id: tirumala2024d4\\n    title: \\\"D4: Improving LLM Pretraining via Document De-Duplication and Diversification\\\"\\n    authors: \\\"Tirumala, Markosyan, Zettlemoyer, Aghajanyan\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Deduplication + diversification baseline for data curation; orthogonal to depth-based filtering\\\"\\n    cited: false\\n\\n  - id: xie2024doremi\\n    title: \\\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\\\"\\n    authors: \\\"Xie, Pham, Dong, Du, Liu, Lu, Liang, Le, Ma, Yu\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Domain reweighting for pretraining; does not consider generational depth dimension\\\"\\n    cited: false\\n\\n  - id: kirchenbauer2023watermark\\n    title: \\\"A Watermark for Large Language Models\\\"\\n    authors: \\\"Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein\\\"\\n    venue: \\\"ICML 2023\\\"\\n    category: \\\"watermarking\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Provenance tracking via watermarking; complementary approach to depth estimation when watermarks are available\\\"\\n    cited: false\\n\\n  - id: zellers2019grover\\n    title: \\\"Defending Against Neural Fake News\\\"\\n    authors: \\\"Zellers, Holtzman, Rashkin, Bisk, Farhadi, Roesner, Choi\\\"\\n    venue: \\\"NeurIPS 2019\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Early neural text detection; binary classification paradigm that our ordinal approach generalizes\\\"\\n    cited: false\\n\\n  - id: ippolito2020detection\\n    title: \\\"Automatic Detection of Generated Text is Easiest when Humans are Fooled\\\"\\n    authors: \\\"Ippolito, Duckworth, Callison-Burch, Eck\\\"\\n    venue: \\\"ACL 2020\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Binary detection difficulty analysis; does not consider multi-generational depth\\\"\\n    cited: false\\n\", \"total_chars\": 13194, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "298ccc32-7b26-4700-b5c0-e4f36a25b859",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "cdd731ac-128b-4533-b826-f4639b206168",
  "sourceToolAssistantUUID": "298ccc32-7b26-4700-b5c0-e4f36a25b859",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T08:48:18.645Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XrYHyaKRqef58Q2CWvjADc`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdd731ac-128b-4533-b826-f4639b206168",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH7JUjwxXSAJngEKHSF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f73de72-077d-46af-a8b3-5065794c641c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V7hYnUkKHQ4sTt5YyMSRoH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8735,
      "cache_read_input_tokens": 19384,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8735
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 19384,
          "cache_creation_input_tokens": 8735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8735,
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

_source line 24 · 2026-05-13T08:48:18.654Z_

<details><summary>↩ Tool result · `toolu_01XrYHyaKRqef58Q2CWvjADc`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'gen-depth-contamination'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f73de72-077d-46af-a8b3-5065794c641c",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "e1ad896b-763b-4bc1-be04-c10deb2a3c20",
  "sourceToolAssistantUUID": "7f73de72-077d-46af-a8b3-5065794c641c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T08:48:22.280Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Khg5Avr5ztbKFJRUxjj5Dt`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1ad896b-763b-4bc1-be04-c10deb2a3c20",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH7fv5wuWYrG6wRTKSc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4fac53fd-0e9e-490a-b664-51837a9f5a5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LL8oXR4v7RQ3qhjKQpc81t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6427,
      "cache_read_input_tokens": 28119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6427,
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

_source line 26 · 2026-05-13T08:48:22.294Z_

<details><summary>↩ Tool result · `toolu_01Khg5Avr5ztbKFJRUxjj5Dt`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'gen-depth-contamination'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fac53fd-0e9e-490a-b664-51837a9f5a5a",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "36a58c36-f079-4990-8031-0fc66f8ad757",
  "sourceToolAssistantUUID": "4fac53fd-0e9e-490a-b664-51837a9f5a5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T08:48:22.768Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WWo2vAb7SZ641WKi9xAXW5`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36a58c36-f079-4990-8031-0fc66f8ad757",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH7fv5wuWYrG6wRTKSc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "061e3de6-3bdc-4168-98dc-25427b29e747",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LL8oXR4v7RQ3qhjKQpc81t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6427,
      "cache_read_input_tokens": 28119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6427,
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

_source line 28 · 2026-05-13T08:48:22.779Z_

<details><summary>↩ Tool result · `toolu_01WWo2vAb7SZ641WKi9xAXW5`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'gen-depth-contamination'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "061e3de6-3bdc-4168-98dc-25427b29e747",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "0f8378c2-ceef-49e7-af16-6d6eec01d476",
  "sourceToolAssistantUUID": "061e3de6-3bdc-4168-98dc-25427b29e747",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-13T08:48:25.880Z_

Now let me look at the actual paper artifacts and experimental code/results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f8378c2-ceef-49e7-af16-6d6eec01d476",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH7yq6wHa7SZPPSCAnF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4379ddc-d0dd-4a30-a2ca-877ca75a0876",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTfmocqZFyqbaXe4jpfAaw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 374,
      "cache_read_input_tokens": 34546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 374,
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

_source line 30 · 2026-05-13T08:48:27.429Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01RUBtoBufJUb74L8cwYPZyw`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4379ddc-d0dd-4a30-a2ca-877ca75a0876",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH7yq6wHa7SZPPSCAnF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b9f6057-c6f2-4882-986f-deab62289b06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTfmocqZFyqbaXe4jpfAaw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 374,
      "cache_read_input_tokens": 34546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 374,
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

_source line 31 · 2026-05-13T08:48:27.445Z_

<details><summary>↩ Tool result · `toolu_01RUBtoBufJUb74L8cwYPZyw`</summary>

```text
artifacts/dream_reports/dream_20260512T200328/best/paper.tex
artifacts/dream_reports/dream_20260512T200328/median/paper.tex
artifacts/dream_reports/dream_20260512T200328/worst/paper.tex
artifacts/dream_reports/dream_20260513T080728/best/paper.tex
artifacts/dream_reports/dream_20260513T080728/median/paper.tex
artifacts/dream_reports/dream_20260513T080728/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b9f6057-c6f2-4882-986f-deab62289b06",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "1c7c99f2-152b-4a29-847d-1d8e10338db3",
  "sourceToolAssistantUUID": "2b9f6057-c6f2-4882-986f-deab62289b06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-13T08:48:27.755Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019ovZnNEZStfw63YPwkAGg9`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c7c99f2-152b-4a29-847d-1d8e10338db3",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH7yq6wHa7SZPPSCAnF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23d31e91-65c7-4645-bbc4-674a4b38509c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTfmocqZFyqbaXe4jpfAaw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 374,
      "cache_read_input_tokens": 34546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 374,
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

_source line 33 · 2026-05-13T08:48:27.768Z_

<details><summary>↩ Tool result · `toolu_019ovZnNEZStfw63YPwkAGg9`</summary>

```text
scripts/run_pipeline.py
scripts/run_cross_transfer.py
scripts/run_exp013_cross_transfer.py
artifacts/exp006_filtering_strategies.py
artifacts/exp006_continued_pretraining.py
artifacts/exp006_evaluate.py
artifacts/exp006_analyze.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23d31e91-65c7-4645-bbc4-674a4b38509c",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "0821a878-601c-40bc-88f6-e9243cdcf209",
  "sourceToolAssistantUUID": "23d31e91-65c7-4645-bbc4-674a4b38509c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-13T08:48:28.306Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QNwysgNbRK19LQT3AsKrQN`</summary>

```json
{
  "pattern": "artifacts/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0821a878-601c-40bc-88f6-e9243cdcf209",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH7yq6wHa7SZPPSCAnF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dcaaaf34-ed1b-49bb-b232-75fefa81d07b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTfmocqZFyqbaXe4jpfAaw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 374,
      "cache_read_input_tokens": 34546,
      "output_tokens": 275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 374
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 275,
          "cache_read_input_tokens": 34546,
          "cache_creation_input_tokens": 374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 374,
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

_source line 35 · 2026-05-13T08:48:28.321Z_

<details><summary>↩ Tool result · `toolu_01QNwysgNbRK19LQT3AsKrQN`</summary>

```text
artifacts/_project/report/related_work_structure.md
artifacts/_project/report/gpu_optimization_report.txt
artifacts/gpu_optimization_report.txt
artifacts/_project/report/claim_routes.md
artifacts/_project/report/theory_framework.md
artifacts/_project/report/full_study_plan.md
artifacts/_project/report/methodology_draft.md
artifacts/_project/report/figure_plan.md
artifacts/dream_reports/dream_20260512T200328/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260512T200328/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260512T200328/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260512T200328/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260512T200328/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T200328/best/experiment_data.json
artifacts/dream_reports/dream_20260512T200328/best/paper.tex
artifacts/dream_reports/dream_20260512T200328/best/paper.aux
artifacts/dream_reports/dream_20260512T200328/best/paper.out
artifacts/dream_reports/dream_20260512T200328/best/paper.pdf
artifacts/dream_reports/dream_20260512T200328/best/paper.log
artifacts/dream_reports/dream_20260512T200328/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260512T200328/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T200328/median/experiment_data.json
artifacts/dream_reports/dream_20260512T200328/median/paper.tex
artifacts/dream_reports/dream_20260512T200328/median/paper.aux
artifacts/dream_reports/dream_20260512T200328/median/paper.out
artifacts/dream_reports/dream_20260512T200328/median/paper.pdf
artifacts/dream_reports/dream_20260512T200328/median/paper.log
artifacts/dream_reports/dream_20260512T200328/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260512T200328/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T200328/worst/experiment_data.json
artifacts/dream_reports/dream_20260512T200328/worst/paper.tex
artifacts/dream_reports/dream_20260512T200328/worst/paper.aux
artifacts/dream_reports/dream_20260512T200328/worst/paper.out
artifacts/dream_reports/dream_20260512T200328/worst/paper.pdf
artifacts/dream_reports/dream_20260512T200328/worst/paper.log
artifacts/dream_reports/dream_20260512T200328/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260512T200328/logs/orchestrator.log
artifacts/dream_reports/dream_20260512T200328/best/review_report.md
artifacts/dream_reports/dream_20260512T200328/logs/review_best.log
artifacts/dream_reports/dream_20260512T200328/median/review_report.md
artifacts/dream_reports/dream_20260512T200328/logs/review_median.log
artifacts/dream_reports/dream_20260512T200328/worst/review_report.md
artifacts/dream_reports/dream_20260512T200328/logs/review_worst.log
artifacts/dream_reports/dream_20260512T200328/meta.yaml
artifacts/_project/report/literature_scan_2025_2026.md
artifacts/literature_scan_2025_2026.md
artifacts/_project/report/literature_positioning_notes.md
artifacts/_project/report/literature_positioning_notes_d23bf4.md
artifacts/literature_positioning_notes.md
artifacts/_project/chart/auc_heatmap.pdf
artifacts/figures/auc_heatmap.pdf
artifacts/_project/chart/feature_importance.pdf
artifacts/figures/feature_importance.pdf
artifacts/_project/chart/jsd_decay.pdf
artifacts/figures/jsd_decay.pdf
artifacts/exp005_4model_tau_matrix.json
artifacts/exp-005/data/exp005_4model_tau_matrix.json
artifacts/bootstrap_ci_4model.json
artifacts/exp-013/data/cross_transfer_matrix.csv
artifacts/exp-013/data/cross_transfer_matrix.json
artifacts/manifest.yaml
artifacts/exp006_filtering_strategies.py
artifacts/exp006_continued_pretraining.py
artifacts/exp006_evaluate.py
artifacts/run_exp006.sh
artifacts/exp006_analyze.py
artifacts/dream_reports/dream_20260513T080728/logs/orchestrator.log
artifacts/dream_reports/dream_20260513T080728/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260513T080728/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260513T080728/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260513T080728/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260513T080728/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T080728/best/experiment_data.json
artifacts/dream_reports/dream_20260513T080728/best/paper_framing.md
artifacts/dream_reports/dream_20260513T080728/best/paper.tex
artifacts/dream_reports/dream_20260513T080728/best/paper.aux
artifacts/dream_reports/dream_20260513T080728/best/paper.out
artifacts/dream_reports/dream_20260513T080728/best/paper.pdf
artifacts/dream_reports/dream_20260513T080728/best/paper.log
artifacts/dream_reports/dream_20260513T080728/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260513T080728/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T080728/median/experiment_data.json
artifacts/dream_reports/dream_20260513T080728/median/paper_framing.md
artifacts/dream_reports/dream_20260513T080728/median/paper.tex
artifacts/dream_reports/dream_20260513T080728/median/paper.aux
artifacts/dream_reports/dream_20260513T080728/median/paper.out
artifacts/dream_reports/dream_20260513T080728/median/paper.pdf
artifacts/dream_reports/dream_20260513T080728/median/paper.log
artifacts/dream_reports/dream_20260513T080728/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260513T080728/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T080728/worst/experiment_data.json
artifacts/dream_reports/dream_20260513T080728/worst/paper_framing.md
artifacts/dream_reports/dream_20260513T080728/worst/paper.tex
artifacts/dream_reports/dream_20260513T080728/worst/paper.aux
artifacts/dream_reports/dream_20260513T080728/worst/paper.out
artifacts/dream_reports/dream_20260513T080728/worst/paper.pdf
artifacts/dream_reports/dream_20260513T080728/worst/paper.log
artifacts/dream_reports/dream_20260513T080728/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260513T080728/best/review_context.yaml
artifacts/dream_reports/dream_20260513T080728/logs/review_best.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dcaaaf34-ed1b-49bb-b232-75fefa81d07b",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "7b1286f8-be79-4851-a4c4-073f60156ddc",
  "sourceToolAssistantUUID": "dcaaaf34-ed1b-49bb-b232-75fefa81d07b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-13T08:48:30.963Z_

<details open><summary>🔧 Tool call — Read · `toolu_014bwwFpTgi6mKQREnmUJSVY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260513T080728/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b1286f8-be79-4851-a4c4-073f60156ddc",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH8PB3NBe92QhcNTMNH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9734c7b1-e486-4739-8442-5a2313e16e28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wh8Qj7KLqDeZqQCmmd9Lfp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2532,
      "cache_read_input_tokens": 34920,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2532
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 101,
          "cache_read_input_tokens": 34920,
          "cache_creation_input_tokens": 2532,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2532,
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

_source line 37 · 2026-05-13T08:48:31.296Z_

<details><summary>↩ Tool result · `toolu_014bwwFpTgi6mKQREnmUJSVY`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{graphicx}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{xcolor}
10	\usepackage{hyperref}
11	
12	\title{Generational Depth Contamination: Measuring and Exploiting the Discrimination Boundary of Recursive Synthetic Text}
13	
14	\author{Anonymous}
15	
16	\begin{document}
17	\maketitle
18	
19	% ============================================================
20	\begin{abstract}
21	Web-scale training corpora are increasingly contaminated by machine-generated text that has been recursively regenerated across multiple generations.
22	Existing detectors treat synthetic text as a binary category (human vs.\ machine), ignoring the progressive quality degradation across generational depth.
23	We formalize recursive generation as an iterated lossy channel and invoke the Data Processing Inequality (DPI) to prove the existence of a finite generational discrimination boundary $K^*$---the deepest generation at which pairwise depth discrimination remains statistically reliable.
24	
25	Through controlled experiments spanning three model families (Qwen-2.5, Pythia, OLMo), two model scales (1.5B, 7B), multiple decoding strategies, and both base and instruction-tuned variants, we establish $K^*=2$ as the empirical boundary for 1.5B-scale models under standard nucleus decoding, rising to $K^*\geq 3$ under high-temperature decoding ($T=1.2$) and at 7B scale.
26	Decoding temperature creates a controllable gradient from $K^*=1$ (greedy) to $K^*=3$ (high temperature), demonstrating that $K^*$ captures genuine information-theoretic properties of the recursive channel rather than classifier artifacts.
27	
28	We show that even this coarse three-class ordinal signal (human / gen-1 / gen-2+) enables \emph{graduated filtering} that significantly outperforms binary filtering on downstream benchmarks: $+2.48$ pp on MMLU and $+2.70$ pp on HellaSwag ($p<0.01$, 5 seeds), with gains scaling monotonically with contamination severity.
29	Our 15-dimensional hand-crafted feature set matches frozen-embedding baselines while providing 85\% cross-model transfer retention versus 62\% for learned representations, supporting interpretable, model-agnostic deployment.
30	\end{abstract}
31	
32	% ============================================================
33	\section{Introduction}
34	
35	The proliferation of large language models (LLMs) has created a feedback loop in web-scale data: model outputs enter training corpora, and subsequent models train on---and regenerate---these outputs, producing \emph{recursive synthetic text} of increasing generational depth \cite{shumailov2024model}.
36	While binary synthetic text detectors have achieved strong performance at distinguishing human from machine text \cite{mitchell2023detectgpt,hans2024binoculars}, they do not estimate \emph{how many rounds of recursive generation} a text has undergone.
37	This distinction matters: first-generation synthetic text retains approximately 85\% of the information structure of its human source, while deeper generations undergo progressive quality collapse that binary detectors cannot resolve.
38	
39	We introduce the concept of the \textbf{generational discrimination boundary} $K^*$, defined as the maximum depth $k$ at which a pairwise classifier can reliably distinguish generation $k$ from generation $k+1$.
40	Our information-theoretic framing models recursive generation as an iterated lossy channel.
41	By the Data Processing Inequality (DPI), the mutual information $I(X; Y_k)$ between the original text $X$ and its $k$-th generation output $Y_k$ decreases monotonically, guaranteeing convergence and thus a finite $K^*$.
42	
43	Our contributions are:
44	\begin{enumerate}
45	\item \textbf{$K^*$ Characterization (C1):} We provide the first systematic measurement of $K^*$ across four model configurations, establishing $K^*=2$ for 1.5B-scale models under standard decoding.
46	    We show that $K^*$ is not a ceiling but a controllable operating point that rises with model scale ($K^*\geq 3$ at 7B) and decoding entropy ($K^*=3$ at $T=1.2$), forming a gradient from $K^*=1$ (greedy) through $K^*=2$ (standard) to $K^*=3$ (high temperature/larger model).
47	\item \textbf{Graduated Filtering (C3):} We demonstrate that $K^*$-aware graduated filtering, which assigns fractional weights based on ordinal depth estimates, significantly outperforms binary filtering on MMLU ($+2.48$ pp) and HellaSwag ($+2.70$ pp), with gains that scale monotonically with contamination rate.
48	\item \textbf{Supporting analyses:} We validate ecological validity via retrain-chain experiments, demonstrate 85\% cross-model feature transfer, show that frontier LLMs and binary detectors cannot estimate depth, and provide proof-of-concept Common Crawl validation.
49	\end{enumerate}
50	
51	% ============================================================
52	\section{Related Work}
53	
54	\paragraph{Model Collapse and Recursive Generation.}
55	Shumailov et al.\ (2024) demonstrate that iterative training on model outputs leads to ``model collapse,'' where tail distributions vanish over generations.
56	Alemohammad et al.\ (2024) and Dohmatob et al.\ (2024) provide theoretical analyses of this phenomenon.
57	These works characterize the \emph{macroscopic} phenomenon but do not provide tools for detecting or measuring generational depth in individual texts.
58	
59	\paragraph{Binary Synthetic Text Detection.}
60	DetectGPT \cite{mitchell2023detectgpt}, Binoculars \cite{hans2024binoculars}, and DivEye leverage statistical properties of model outputs for binary (human vs.\ machine) classification.
61	While effective at the human/synthetic boundary (AUC $> 0.91$), we show these methods achieve near-chance performance at distinguishing adjacent generational depths ($\text{AUC}_{1v2} \leq 0.53$).
62	
63	\paragraph{Data Selection and Curation.}
64	DSIR \cite{xie2023dsir} and related methods perform distribution matching for data selection but do not estimate recursive depth.
65	Drayson et al.\ (2025) apply binary detection scores for importance resampling to prevent model collapse---the closest prior work.
66	Our graduated filtering extends this by exploiting ordinal depth structure beyond binary decisions.
67	
68	% ============================================================
69	\section{Method}
70	
71	\subsection{Information-Theoretic Framework}
72	
73	We model recursive text generation as an iterated lossy channel.
74	Let $X$ denote the original human-written text and let $\mathcal{G}$ be the generation function of an LLM with decoding strategy $\delta$.
75	The $k$-th generation is $Y_k = \mathcal{G}(Y_{k-1})$ with $Y_0 = X$.
76	
77	By the \textbf{Data Processing Inequality (DPI)}, for any Markov chain $X \to Y_1 \to Y_2 \to \cdots$:
78	\begin{equation}
79	I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq I(X; Y_k) \geq 0
80	\end{equation}
81	Since $I(X; Y_k)$ is monotonically non-increasing and bounded below, it converges.
82	This guarantees the existence of a finite \textbf{theoretical discrimination boundary} $K^*_{\text{theory}}$: the depth beyond which pairwise discrimination is information-theoretically impossible.
83	
84	\subsection{Empirical Discrimination Boundary $K^*$}
85	
86	We define the \textbf{empirical discrimination boundary} $K^*_{\text{emp}}$ operationally:
87	\begin{equation}
88	K^* = \max\{k : \text{AUC}_{k \text{v} (k+1)} > \theta\}
89	\end{equation}
90	where $\text{AUC}_{k\text{v}(k+1)}$ is the area under the ROC curve for a binary classifier distinguishing generation $k$ from $k+1$, and $\theta = 0.60$ is a discrimination threshold.
91	$K^*_{\text{emp}} \leq K^*_{\text{theory}}$ provides a conservative lower bound.
92	
93	\subsection{Feature Design}
94	
95	We extract a 15-dimensional feature vector for each text document, organized into four groups:
96	
97	\begin{itemize}
98	\item \textbf{Vocabulary diversity} (4 features): type-token ratio, hapax legomena ratio, frequency-rank entropy, Yule's K.
99	\item \textbf{Surprisal statistics} (5 features): mean and standard deviation of token surprisal, first- and second-order surprisal differences (surp\_d1\_std, surp\_d2\_std), and max surprisal.
100	\item \textbf{Tail distribution} (3 features): fraction of tokens with surprisal $> 2\sigma$, tail weight ratio, kurtosis of surprisal distribution.
101	\item \textbf{Structural} (3 features): sentence length variance, repetition rate (3-gram), and discourse coherence score.
102	\end{itemize}
103	
104	We train LightGBM ordinal classifiers with these features for depth estimation.
105	
106	\subsection{Graduated Filtering}
107	
108	Given a contaminated corpus $\mathcal{D}$ with unknown mixture of human and multi-generation synthetic text, our graduated filtering assigns weights:
109	\begin{equation}
110	w(x) = \begin{cases}
111	1 & \text{if } \hat{d}(x) = 0 \text{ (predicted human)} \\
112	\alpha & \text{if } \hat{d}(x) = 1 \text{ (predicted gen-1)} \\
113	0 & \text{if } \hat{d}(x) \geq 2 \text{ (predicted gen-2+)}
114	\end{cases}
115	\end{equation}
116	where $\hat{d}(x)$ is the predicted depth and $\alpha \in [0, 1]$ is a discount factor for first-generation text, which retains substantial information value despite being synthetic.
117	
118	% ============================================================
119	\section{Experiments}
120	
121	\subsection{Experimental Setup}
122	
123	\paragraph{Models.} We use Qwen2.5-1.5B-Instruct, Qwen2.5-1.5B (base), Qwen2.5-7B, and Pythia-1.4B.
124	\paragraph{Data.} C4 corpus, 5K documents (1K for 7B due to compute constraints).
125	\paragraph{Generation.} Continuation mode (the model continues from a prefix) is the canonical condition. Depth chains span generations 0--5 (0--3 for 7B, 0--4 for Pythia).
126	\paragraph{Decoding.} Default: nucleus sampling $p=0.95$, $T=1.0$. Ablation covers greedy, $p=0.9/T=1.0$, $p=0.95/T=0.7$, and $p=0.95/T=1.2$.
127	\paragraph{Metrics.} Pairwise AUC, pairwise JSD, $K^*$ (AUC threshold $\theta=0.60$), ordinal accuracy, MAE, bootstrap 95\% CI (10K resamples).
128	
129	% ============================================================
130	\subsection{$K^*$ Characterization}
131	\label{sec:kstar}
132	
133	\paragraph{Decoding Strategy Ablation.}
134	We evaluate four decoding configurations on Qwen2.5-1.5B-Instruct (Table~\ref{tab:decoding}).
135	The results establish a controllable $K^*$ gradient: greedy decoding yields $K^*=1$, standard nucleus configurations ($p=0.9/T=1.0$, $p=0.95/T=0.7$, baseline $p=0.95/T=1.0$) consistently yield $K^*=2$, and high-temperature decoding ($T=1.2$) yields $K^*=3$.
136	
137	The high-temperature condition achieves $\text{AUC}_{2v3} = 0.6218$, crossing the $\theta=0.60$ threshold that all standard-temperature configurations fail to reach.
138	This gradient demonstrates that $K^*$ captures genuine information-theoretic properties of the recursive channel: higher decoding entropy preserves more distributional structure per generation, requiring additional iterations before the signal saturates.
139	
140	Feature degradation ordering remains highly consistent across all configurations, with Spearman $\rho \geq 0.878$ relative to the baseline (Table~\ref{tab:feature_ordering}).
141	This indicates that decoding strategy modulates signal \emph{strength} but not which features degrade first.
142	
143	\begin{table}[t]
144	\centering
145	\small
146	\caption{Decoding strategy ablation on Qwen2.5-1.5B-Instruct. $K^*$ forms a controllable gradient from greedy ($K^*=1$) through standard ($K^*=2$) to high-temperature ($K^*=3$).}
147	\label{tab:decoding}
148	\begin{tabular}{lccccc}
149	\toprule
150	\textbf{Config} & \textbf{$K^*$} & \textbf{AUC$_{0v1}$} & \textbf{AUC$_{1v2}$} & \textbf{AUC$_{2v3}$} & \textbf{JSD$_{0v1}$} \\
151	\midrule
152	greedy & 1 & .9965 & .5862 & .5481 & .2753 \\
153	nucleus $p$=0.9 $T$=1.0 & 2 & .9968 & .6278 & .5582 & .2814 \\
154	$p$=0.95 $T$=0.7 & 2 & .9963 & .6241 & .5558 & .2685 \\
155	baseline $p$=0.95 $T$=1.0 & 2 & .9972 & .6114 & .5609 & .2863 \\
156	$p$=0.95 $T$=1.2 & \textbf{3} & .9981 & .6823 & .6218 & .3082 \\
157	\bottomrule
158	\end{tabular}
159	\end{table}
160	
161	\begin{table}[t]
162	\centering
163	\small
164	\caption{Feature degradation ordering consistency (Spearman $\rho$ vs.\ baseline configuration).}
165	\label{tab:feature_ordering}
166	\begin{tabular}{lc}
167	\toprule
168	\textbf{Config} & \textbf{Spearman $\rho$} \\
169	\midrule
170	greedy & 0.886 \\
171	$p$=0.9 & 0.921 \\
172	$T$=0.7 & 0.914 \\
173	$T$=1.2 & 0.878 \\
174	\bottomrule
175	\end{tabular}
176	\end{table}
177	
178	\paragraph{Cross-Scale Probing (7B).}
179	Scaling from 1.5B to 7B parameters yields $K^* \geq 3$ (Table~\ref{tab:7b}), with $\text{AUC}_{1v2} = 0.6948$ ($+8.34$ pp vs.\ 1.5B) and $\text{AUC}_{2v3} = 0.6175$ (bootstrap 95\% CI: $[0.6015, 0.6338]$, lower bound above $\theta$).
180	
181	The 7B model preserves richer distributional structure per generation---rare n-grams, long-range discourse patterns, and low-frequency vocabulary---requiring more recursive iterations before the depth signal saturates.
182	Combined with the decoding ablation, two independent causal pathways elevate $K^*$ beyond 2: model scale and decoding entropy.
183	
184	\begin{table}[t]
185	\centering
186	\small
187	\caption{Qwen2.5-7B vs.\ 1.5B pairwise discrimination. 7B achieves $K^* \geq 3$.}
188	\label{tab:7b}
189	\begin{tabular}{lcccc}
190	\toprule
191	\textbf{Pair} & \textbf{7B AUC} & \textbf{7B JSD} & \textbf{1.5B AUC} & \textbf{1.5B JSD} \\
192	\midrule
193	0v1 & .9984 & .3415 & .9972 & .2863 \\
194	1v2 & .6948 & .0285 & .6114 & .0051 \\
195	2v3 & .6175 & .0112 & .5609 & .0036 \\
196	\bottomrule
197	\end{tabular}
198	\end{table}
199	
200	\begin{table}[t]
201	\centering
202	\small
203	\caption{7B bootstrap 95\% confidence intervals (10K resamples).}
204	\label{tab:7b_ci}
205	\begin{tabular}{lcccc}
206	\toprule
207	\textbf{Pair} & \textbf{AUC} & \textbf{CI lower} & \textbf{CI upper} & \textbf{CI lower $> 0.60$?} \\
208	\midrule
209	1v2 & .6948 & .6782 & .7108 & \checkmark~(+7.8 pp) \\
210	2v3 & .6175 & .6015 & .6338 & \checkmark~(+0.15 pp) \\
211	\bottomrule
212	\end{tabular}
213	\end{table}
214	
215	\paragraph{Base vs.\ Instruction-Tuned Models.}
216	Table~\ref{tab:base_instruct} compares Qwen2.5-1.5B base and instruct variants.
217	Both yield $K^*=2$, but the base model exhibits stronger pairwise signals ($\text{AUC}_{1v2} = 0.6382$ vs.\ $0.6114$, $\Delta = +2.68$ pp).
218	RLHF alignment compresses inter-generational variance by pulling outputs toward a preferred mode, reducing quantitative signal strength without altering the qualitative convergence behavior.
219	This is practically important: since wild synthetic text originates from both base and instruction-tuned models, the consistency of $K^*=2$ across variants supports the generality of our framework.
220	
221	\begin{table}[t]
222	\centering
223	\small
224	\caption{Base vs.\ Instruct comparison (Qwen2.5-1.5B, continuation mode). Both yield $K^*=2$; base signals are stronger by 2.68 pp at the 1v2 boundary.}
225	\label{tab:base_instruct}
226	\begin{tabular}{lcccccc}
227	\toprule
228	\textbf{Variant} & \textbf{$K^*$} & \textbf{AUC$_{0v1}$} & \textbf{AUC$_{1v2}$} & \textbf{AUC$_{2v3}$} & \textbf{JSD$_{0v1}$} & \textbf{Ord.\ Acc.} \\
229	\midrule
230	base & 2 & .9958 & .6382 & .5685 & .2952 & .3948 \\
231	instruct & 2 & .9972 & .6114 & .5609 & .2863 & .3819 \\
232	$\Delta$ & 0 & $-.0014$ & $+.0268$ & $+.0076$ & $+.0089$ & $+.0129$ \\
233	\bottomrule
234	\end{tabular}
235	\end{table}
236	
237	% ============================================================
238	\subsection{Ecological Validity: Retrain-Chain}
239	\label{sec:retrain}
240	
241	A natural concern is whether prompt-based generation chains reflect realistic recursive contamination, where models are actually \emph{retrained} on their own outputs.
242	We evaluate this using Pythia-1.4B with LoRA (rank=16, $\alpha=32$) retrain chains and compare against prompt chains on the same model (Table~\ref{tab:retrain}).
243	
244	$K^*$ is identical across methods ($K^*=2$) with AUC differences $< 2$ pp at all depth pairs.
245	A classifier trained on prompt-chain data retains 91.5\% accuracy when evaluated on retrain-chain data.
246	Feature distribution divergence (JSD) between methods increases with depth but remains small ($< 0.04$), confirming that inter-generational degradation dominates over method-specific artifacts.
247	
248	\begin{table}[t]
249	\centering
250	\small
251	\caption{Retrain-chain vs.\ prompt-chain (Pythia-1.4B). $K^*$ and AUC are consistent across generation methods.}
252	\label{tab:retrain}
253	\begin{tabular}{lccc}
254	\toprule
255	\textbf{Pair} & \textbf{Retrain AUC} & \textbf{Prompt AUC} & \textbf{$\Delta$} \\
256	\midrule
257	0v1 & .9895 & .9932 & $-.0037$ \\
258	1v2 & .6362 & .6539 & $-.0177$ \\
259	2v3 & .5448 & .5515 & $-.0067$ \\
260	3v4 & .5128 & .5153 & $-.0025$ \\
261	\bottomrule
262	\end{tabular}
263	\end{table}
264	
265	\begin{table}[t]
266	\centering
267	\small
268	\caption{Feature distribution divergence between retrain and prompt chains (JSD by depth).}
269	\label{tab:retrain_jsd}
270	\begin{tabular}{lc}
271	\toprule
272	\textbf{Depth} & \textbf{JSD} \\
273	\midrule
274	0 & 0.0018 \\
275	1 & 0.0162 \\
276	2 & 0.0285 \\
277	3 & 0.0378 \\
278	\bottomrule
279	\end{tabular}
280	\end{table}
281	
282	% ============================================================
283	\subsection{Downstream Graduated Filtering}
284	\label{sec:filtering}
285	
286	\paragraph{Main Comparison.}
287	We compare six filtering strategies applied to continued pretraining of Qwen2.5-1.5B on contaminated data (30\% synthetic injection), evaluated on MMLU and HellaSwag with 5 random seeds (Table~\ref{tab:downstream}).
288	
289	Graduated filtering ($\alpha=0.5$) achieves 29.41\% on MMLU and 47.08\% on HellaSwag, significantly outperforming all baselines.
290	The critical comparison is graduated vs.\ binary-ours ($+2.48$ pp MMLU, $p=0.0043$; $+2.70$ pp HellaSwag, $p=0.0067$), where the \emph{only} variable changed is the binary vs.\ ordinal decision boundary.
291	Graduated filtering also outperforms DSIR ($+2.09$ pp MMLU, $p=0.013$) and binary-Drayson ($+2.20$ pp MMLU, $p=0.008$), demonstrating that the advantage derives from depth-aware curation rather than better filtering in general (Table~\ref{tab:significance}).
292	
293	\begin{table}[t]
294	\centering
295	\small
296	\caption{Downstream evaluation: 6 filtering strategies (5-seed mean $\pm$ std). Graduated filtering significantly outperforms all baselines.}
297	\label{tab:downstream}
298	\begin{tabular}{lcccc}
299	\toprule
300	\textbf{Strategy} & \textbf{MMLU} & \textbf{$\pm$} & \textbf{HellaSwag} & \textbf{$\pm$} \\
301	\midrule
302	no-filter & 25.82 & 0.21 & 43.24 & 0.18 \\
303	binary-ours & 26.93 & 0.28 & 44.38 & 0.23 \\
304	binary-Drayson & 27.21 & 0.32 & 44.65 & 0.27 \\
305	DSIR & 27.32 & 0.30 & 44.81 & 0.25 \\
306	surprisal-based & 28.15 & 0.33 & 45.92 & 0.28 \\
307	\textbf{graduated ($\alpha$=0.5)} & \textbf{29.41} & 0.25 & \textbf{47.08} & 0.20 \\
308	\bottomrule
309	\end{tabular}
310	\end{table}
311	
312	\begin{table}[t]
313	\centering
314	\small
315	\caption{Statistical significance of graduated filtering advantages (paired $t$-test, 5 seeds).}
316	\label{tab:significance}
317	\begin{tabular}{lcccc}
318	\toprule
319	\textbf{Comparison} & \textbf{$\Delta$MMLU} & \textbf{$p$} & \textbf{$\Delta$HS} & \textbf{$p$} \\
320	\midrule
321	vs.\ binary-ours & +2.48 & .0043 & +2.70 & .0067 \\
322	vs.\ binary-Drayson & +2.20 & .0082 & +2.43 & .0054 \\
323	vs.\ DSIR & +2.09 & .0125 & +2.27 & .0098 \\
324	vs.\ surprisal-based & +1.26 & .0318 & +1.16 & .0425 \\
325	\bottomrule
326	\end{tabular}
327	\end{table}
328	
329	\paragraph{Mixing Weight Sensitivity.}
330	Table~\ref{tab:alpha} shows the sensitivity of graduated filtering to the discount factor $\alpha$.
331	Performance peaks at $\alpha=0.5$, forming an inverted-U shape: $\alpha \to 0$ converges to binary removal (discarding useful gen-1 data), while $\alpha \to 1$ converges to no filtering (retaining gen-2+ noise).
332	The optimum at $\alpha=0.5$ aligns with the intuition that gen-1 text retains approximately half the quality-relevant information of human text.
333	
334	\begin{table}[t]
335	\centering
336	\small
337	\caption{Graduated filtering sensitivity to $\alpha$ (gen-1 weight).}
338	\label{tab:alpha}
339	\begin{tabular}{lcc}
340	\toprule
341	\textbf{$\alpha$} & \textbf{MMLU} & \textbf{HellaSwag} \\
342	\midrule
343	0.1 & 27.45 & 44.85 \\
344	0.3 & 28.72 & 46.28 \\
345	\textbf{0.5} & \textbf{29.41} & \textbf{47.08} \\
346	0.7 & 29.08 & 46.72 \\
347	0.9 & 28.14 & 45.65 \\
348	\bottomrule
349	\end{tabular}
350	\end{table}
351	
352	\paragraph{Dose-Response.}
353	To assess practical relevance, we vary the synthetic injection rate from 10\% to 50\% (Table~\ref{tab:dose}).
354	The graduated--binary advantage scales monotonically: $+0.72$ pp MMLU at 10\% injection (non-significant), $+2.48$ pp at 30\% ($p=0.004$), and $+3.82$ pp at 50\% ($p<0.001$).
355	Current estimates of synthetic text in web corpora range from 15--30\%, precisely the regime where graduated filtering transitions from marginal to strongly significant.
356	As synthetic contamination grows, so does the value of depth-aware curation.
357	
358	\begin{table}[t]
359	\centering
360	\small
361	\caption{Dose-response: graduated vs.\ binary filtering advantage by contamination rate. Gains are monotonically increasing.}
362	\label{tab:dose}
363	\begin{tabular}{lcccc}
364	\toprule
365	\textbf{Injection} & \textbf{$\Delta$MMLU} & \textbf{$p$} & \textbf{$\Delta$HS} & \textbf{$p$} \\
366	\midrule
367	10\% & +0.72 & .142 & +0.51 & .218 \\
368	30\% & +2.48 & .004 & +2.70 & .007 \\
369	50\% & +3.82 & $<$.001 & +3.48 & .001 \\
370	\bottomrule
371	\end{tabular}
372	\end{table}
373	
374	% ============================================================
375	\subsection{Analysis}
376	
377	\paragraph{Frontier LLMs Cannot Estimate Depth.}
378	We evaluate GPT-4o and Claude 3.5 Sonnet on zero-shot depth classification (5-class, 200 samples per depth; Table~\ref{tab:llm_baseline}).
379	Both achieve near-chance accuracy (21.8\% and 23.4\% vs.\ 20\% random), with Kendall $\tau$ correlations of 0.082 and 0.118 respectively.
380	Our ordinal classifier more than doubles this performance (42.3\% accuracy, $\tau=0.552$).
381	The failure of frontier LLMs reflects a structural limitation: depth estimation requires distributional comparison across a reference population, whereas LLMs process individual texts and lack the concept of recursive generational depth in their training signal.
382	Both LLMs exhibit a systematic bias toward predicting depth 0 or 1, consistent with the finding that high-level fluency---the cue LLMs rely on---is the last feature to degrade.
383	
384	\begin{table}[t]
385	\centering
386	\small
387	\caption{Zero-shot depth estimation: frontier LLMs vs.\ our ordinal classifier.}
388	\label{tab:llm_baseline}
389	\begin{tabular}{lccc}
390	\toprule
391	\textbf{Method} & \textbf{Accuracy} & \textbf{MAE} & \textbf{Kendall $\tau$} \\
392	\midrule
393	GPT-4o (zero-shot) & .218 & 1.742 & .082 \\
394	Claude 3.5 Sonnet (zero-shot) & .234 & 1.668 & .118 \\
395	Random baseline & .200 & 2.000 & .000 \\
396	Our ordinal classifier (15D) & \textbf{.423} & \textbf{0.984} & \textbf{.552} \\
397	\bottomrule
398	\end{tabular}
399	\end{table}
400	
401	\paragraph{Binary Detectors as Depth Proxies.}
402	We evaluate whether existing binary detector confidence scores can serve as depth proxies (Table~\ref{tab:binary_proxy}).
403	DivEye and Binoculars achieve strong human-vs-synthetic separation ($\text{AUC}_{0v1} = 0.935$ and $0.912$) but near-chance adjacent-depth discrimination ($\text{AUC}_{1v2} \leq 0.528$).
404	Their Spearman correlation with true depth ($\rho = 0.223$ and $0.184$) is statistically significant but driven entirely by the depth-0 vs.\ depth-$\geq$1 discontinuity.
405	Within the synthetic regime (depth $\geq 1$), confidence scores plateau---all synthetic text clusters in a narrow band regardless of depth.
406	Our 15D features achieve $+10$ pp higher $\text{AUC}_{1v2}$, confirming that binary detection and depth estimation are fundamentally different tasks.
407	
408	\begin{table}[t]
409	\centering
410	\small
411	\caption{Binary detector scores as depth proxies. Existing detectors plateau at depth $\geq 1$.}
412	\label{tab:binary_proxy}
413	\begin{tabular}{lccccc}
414	\toprule
415	\textbf{Detector} & \textbf{$\rho$} & \textbf{$p$} & \textbf{AUC$_{0v1}$} & \textbf{AUC$_{1v2}$} & \textbf{AUC$_{2v3}$} \\
416	\midrule
417	DivEye & .223 & .001 & .935 & .528 & .508 \\
418	Binoculars & .184 & .003 & .912 & .521 & .505 \\
419	Our 15D & --- & --- & .995 & .634 & .551 \\
420	\bottomrule
421	\end{tabular}
422	\end{table}
423	
424	\paragraph{Learned vs.\ Hand-Crafted Features.}
425	Table~\ref{tab:learned} compares frozen Qwen2.5-1.5B embeddings (1536-dim) with a 2-layer MLP against our 15D hand-crafted features with LightGBM.
426	The performance gap is small: $\text{AUC}_{1v2}$ difference of 1.3 pp in favor of hand-crafted features, with 102$\times$ fewer dimensions and 32.5$\times$ faster training.
427	
428	The decisive argument is cross-model transfer: when trained on Qwen data and tested on Pythia, hand-crafted features retain 85\% of accuracy versus 62\% for frozen embeddings.
429	Learned representations overfit to model-specific embedding spaces, while statistical features capture model-agnostic properties of recursive degradation.
430	This supports our design choice as a \emph{structural advantage}, not a methodological compromise.
431	
432	\begin{table}[t]
433	\centering
434	\small
435	\caption{Learned vs.\ hand-crafted features. 15D features match or exceed frozen embeddings with 102$\times$ fewer dimensions and 85\% cross-model transfer.}
436	\label{tab:learned}
437	\begin{tabular}{lcccccc}
438	\toprule
439	\textbf{Method} & \textbf{AUC$_{1v2}$} & \textbf{Ord.\ Acc.} & \textbf{MAE} & \textbf{Dim} & \textbf{GPU-h} & \textbf{Transfer} \\
440	\midrule
441	frozen emb.\ + MLP & .598 & .371 & 1.195 & 1536 & 2.6 & 62\% \\
442	15D + LightGBM & .611 & .388 & 1.155 & 15 & 0.08 & 85\% \\
443	\bottomrule
444	\end{tabular}
445	\end{table}
446	
447	\paragraph{Common Crawl Validation.}
448	As a proof-of-concept, we apply our classifier to 10K documents from Common Crawl 2025/2026 snapshots (Table~\ref{tab:commoncrawl}).
449	Predicted depth correlates negatively with AlignScore (factual consistency, $\rho=-0.288$) and vocabulary richness ($\rho=-0.342$), both $p<0.001$.
450	The predicted distribution---82.5\% depth-0, 10.7\% depth-1, 4.7\% depth-2, 2.1\% depth-3+---is consistent with external estimates of 15--25\% synthetic content in web data.
451	While lacking ground truth, these directionally correct correlations support the external validity of our depth estimation framework.
452	
453	\begin{table}[t]
454	\centering
455	\small
456	\caption{Common Crawl proof-of-concept validation ($n=10$K).}
457	\label{tab:commoncrawl}
458	\begin{tabular}{lc}
459	\toprule
460	\textbf{Metric} & \textbf{Value} \\
461	\midrule
462	Spearman(pred.\ depth, AlignScore) & $-0.288$ \\
463	Spearman(pred.\ depth, vocab richness) & $-0.342$ \\
464	\% predicted depth $\geq 1$ & 17.5\% \\
465	\% predicted depth $\geq 2$ & 6.8\% \\
466	\% predicted depth $\geq 3$ & 2.1\% \\
467	\bottomrule
468	\end{tabular}
469	\end{table}
470	
471	% ============================================================
472	\section{Discussion}
473	
474	\paragraph{$K^*$ is Not a Ceiling.}
475	A primary contribution of this work is demonstrating that $K^*=2$, established as the empirical boundary for 1.5B-scale models under standard decoding, is not a fundamental limit but a controllable operating point.
476	Two independent causal pathways push $K^*$ beyond 2: increasing model scale (7B yields $K^* \geq 3$) and increasing decoding entropy ($T=1.2$ yields $K^*=3$).
477	The greedy endpoint ($K^*=1$) completes the gradient, confirming that $K^*$ captures information-theoretic channel properties rather than classifier artifacts.
478	
479	\paragraph{Practical Implications.}
480	Current estimates place synthetic text at 15--30\% of web data, with this fraction growing.
481	Our dose-response analysis shows graduated filtering transitions from marginal to strongly significant at $\sim$20\% contamination, precisely the current operating regime.
482	The monotonically increasing benefit curve means the value of depth-aware curation will grow with the problem.
483	
484	\paragraph{Limitations.}
485	Our experiments are conducted at 1.5B and 7B scale; behavior at larger scales (70B+) remains an open question, though the scale$\to K^*$ trend suggests $K^*$ will continue to rise.
486	The Common Crawl validation lacks ground truth and provides only correlational evidence.
487	Our $\alpha$ sensitivity sweep is limited to a single contamination rate (30\%); the optimal $\alpha$ may vary with injection level.
488	
489	% ============================================================
490	\section{Conclusion}
491	
492	We introduced the generational discrimination boundary $K^*$---the first systematic measurement of how deeply recursive synthetic text can be resolved.
493	Through experiments spanning three model families, two scales, multiple decoding strategies, and both base and instruction-tuned variants, we established $K^*=2$ as the empirical boundary for 1.5B models under standard decoding, with $K^*\geq 3$ achievable via increased scale or decoding entropy.
494	
495	Even this coarse ordinal signal enables graduated filtering that significantly outperforms binary approaches on MMLU ($+2.48$ pp) and HellaSwag ($+2.70$ pp), with benefits scaling monotonically with contamination severity.
496	Our 15-dimensional interpretable feature set provides 85\% cross-model transfer retention, supporting practical deployment for data curation at scale.
497	As the fraction of synthetic text in web corpora continues to grow, depth-aware data governance will become increasingly essential.
498	
499	\bibliography{custom}
500	
501	\end{document}
502	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9734c7b1-e486-4739-8442-5a2313e16e28",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "494e612a-699c-4f9e-b30d-ad7c97b1c843",
  "sourceToolAssistantUUID": "9734c7b1-e486-4739-8442-5a2313e16e28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-13T08:48:34.261Z_

Now let me also read the experiment data and review context to get the full picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "494e612a-699c-4f9e-b30d-ad7c97b1c843",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH8bnpNyWLiPNAXL6Pr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "273d1b72-284a-4399-9b45-d3cfff5b4e8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GorzS3gVAV4xgH9oHoPR6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10991,
      "cache_read_input_tokens": 37452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10991,
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

_source line 39 · 2026-05-13T08:48:36.695Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VrX5vjwv5cRkYtqtbz4cue`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260513T080728/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "273d1b72-284a-4399-9b45-d3cfff5b4e8f",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH8bnpNyWLiPNAXL6Pr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "efc1f891-1aac-4ad0-9680-a7405d21b733",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GorzS3gVAV4xgH9oHoPR6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10991,
      "cache_read_input_tokens": 37452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10991,
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

_source line 40 · 2026-05-13T08:48:37.038Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GTMBwxwQRkWDSpqdVySyww`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260513T080728/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efc1f891-1aac-4ad0-9680-a7405d21b733",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH8bnpNyWLiPNAXL6Pr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f610f2f-212e-4373-ac5c-fd0249557c1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GorzS3gVAV4xgH9oHoPR6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10991,
      "cache_read_input_tokens": 37452,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10991
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 37452,
          "cache_creation_input_tokens": 10991,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10991,
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

_source line 41 · 2026-05-13T08:48:37.047Z_

<details><summary>↩ Tool result · `toolu_01VrX5vjwv5cRkYtqtbz4cue`</summary>

```text
1	narrative_guidance: 'C1'' 全面成立 + C3 downstream 收益显著。exp-003 解码消融建立 K* 可调控梯度（greedy
2	  K*=1 → standard K*=2 → high-temp K*=3）， 直接消解 "K*=2 太浅" 审稿人顾虑。exp-004 7B 确认 scale
3	  → K* 因果链（K*≥3），与 exp-003 形成两条独立路径推高 K*。 exp-006 graduated filtering 在 MMLU/HellaSwag
4	  上均显著优于 binary（Δ≥2pp, p<0.01），exp-009 dose-response 单调递增。 exp-015 15D hand-crafted
5	  features 与 frozen embeddings 差距 <1.5pp，支撑 interpretable features 叙事。 Qwen-cont 的
6	  0.0015 margin 脆弱性被 exp-003 新 configs 的一致 K*=2 所补偿——多条件汇聚证据远强于单点 CI。 所有完成实验的实际数据与
7	  best 档预测高度一致，原始 2+1 claim 结构可直接支撑 EMNLP 2026 Main，reviewer score 预期 3.5-4.0。
8	
9	  '
10	imagined_experiments:
11	- name: Qwen2.5-1.5B 解码策略消融
12	  plan_id: exp-003
13	  description: 'Qwen2.5-1.5B-Instruct continuation mode, C4 5K docs, depth 0-5, 4
14	    解码配置: greedy / nucleus p=0.9 T=1.0 / nucleus p=0.95 T=0.7 / nucleus p=0.95 T=1.2。
15	    Baseline 为 exp-017 (nucleus p=0.95, T=1.0, continuation): 1v2 AUC=0.6114, K*=2。
16	
17	    '
18	  expected_results:
19	    greedy:
20	      k_star: 1
21	      pairwise_auc:
22	        0v1: 0.9965
23	        1v2: 0.5862
24	        2v3: 0.5481
25	        3v4: 0.5225
26	        4v5: 0.5108
27	      pairwise_jsd:
28	        0v1: 0.2753
29	        1v2: 0.0038
30	        2v3: 0.0029
31	        3v4: 0.0022
32	        4v5: 0.0019
33	      ordinal_accuracy: 0.3412
34	    nucleus_p0.9_T1.0:
35	      k_star: 2
36	      pairwise_auc:
37	        0v1: 0.9968
38	        1v2: 0.6278
39	        2v3: 0.5582
40	        3v4: 0.5312
41	        4v5: 0.5124
42	      pairwise_jsd:
43	        0v1: 0.2814
44	        1v2: 0.0057
45	        2v3: 0.0035
46	        3v4: 0.0028
47	        4v5: 0.0024
48	      ordinal_accuracy: 0.3685
49	    T0.7_p0.95:
50	      k_star: 2
51	      pairwise_auc:
52	        0v1: 0.9963
53	        1v2: 0.6241
54	        2v3: 0.5558
55	        3v4: 0.5286
56	        4v5: 0.5115
57	      pairwise_jsd:
58	        0v1: 0.2685
59	        1v2: 0.0052
60	        2v3: 0.0033
61	        3v4: 0.0026
62	        4v5: 0.0022
63	      ordinal_accuracy: 0.3648
64	    T1.2_p0.95:
65	      k_star: 3
66	      pairwise_auc:
67	        0v1: 0.9981
68	        1v2: 0.6823
69	        2v3: 0.6218
70	        3v4: 0.5614
71	        4v5: 0.5305
72	      pairwise_jsd:
73	        0v1: 0.3082
74	        1v2: 0.0118
75	        2v3: 0.0056
76	        3v4: 0.0035
77	        4v5: 0.0027
78	      ordinal_accuracy: 0.3975
79	    cross_config_spearman_rho_feature_ordering:
80	      greedy_vs_baseline: 0.886
81	      p0.9_vs_baseline: 0.921
82	      T0.7_vs_baseline: 0.914
83	      T1.2_vs_baseline: 0.878
84	    k_star_summary: K*=2 in 3/4 configs (p=0.9, T=0.7, T=1.2≥2); K*=1 for greedy;
85	      K*=3 for T=1.2
86	  result_rationale: '解码策略通过控制 token 采样的有效熵，直接调控递归信道的信息保持率。 Greedy 解码（argmax）将输出钉死在条件分布的
87	    mode 上：gen-1 已高度确定性，gen-2 对 gen-1 施加相同的 argmax 压缩后几乎无新增信息损失可测—— 因此 1v2 AUC=0.586
88	    低于 θ=0.60 阈值，K*=1。这不是检测失败，而是 greedy 信道本身在首代就完成了绝大部分信息丢弃。 p=0.9（vs baseline p=0.95）仅移除尾部
89	    5% 概率质量的差异，效应量小——1v2 AUC 从 0.611 降到 0.628，仍稳定在 K*=2。 T=0.7 压缩 softmax 温度使分布更 peaked，效应与收窄
90	    nucleus 类似，1v2=0.624 保持 K*=2。 T=1.2 是关键条件：高温度展平分布→每代输出保留更多"非主流" token 选择→这些 tail
91	    tokens 携带的分布结构需要更多代际才能被递归"洗掉"。 信息论机制：T=1.2 抬高了初始互信息 I(X;Y₁)，DPI 保证 I(X;Yₖ) 单调递减，但更高起点意味着
92	    2v3 AUC=0.622 仍高于 0.60→K*=3。 Feature ordering 一致性（ρ≥0.878）表明解码策略改变信号强度但不改变哪些特征最先饱和——退化顺序是信息论结构性规律。
93	
94	    '
95	  tables:
96	  - caption: '解码策略消融: K* 与关键 pairwise AUC'
97	    columns:
98	    - decoding_config
99	    - K*
100	    - AUC_0v1
101	    - AUC_1v2
102	    - AUC_2v3
103	    - AUC_3v4
104	    - JSD_0v1
105	    rows:
106	    - - greedy
107	      - 1
108	      - 0.9965
109	      - 0.5862
110	      - 0.5481
111	      - 0.5225
112	      - 0.2753
113	    - - nucleus p=0.9 T=1.0
114	      - 2
115	      - 0.9968
116	      - 0.6278
117	      - 0.5582
118	      - 0.5312
119	      - 0.2814
120	    - - p=0.95 T=0.7
121	      - 2
122	      - 0.9963
123	      - 0.6241
124	      - 0.5558
125	      - 0.5286
126	      - 0.2685
127	    - - p=0.95 T=1.2
128	      - 3
129	      - 0.9981
130	      - 0.6823
131	      - 0.6218
132	      - 0.5614
133	      - 0.3082
134	    - - baseline (p=0.95 T=1.0)
135	      - 2
136	      - 0.9972
137	      - 0.6114
138	      - 0.5609
139	      - 0.5408
140	      - 0.2863
141	  - caption: Feature degradation ordering 一致性 (Spearman ρ vs baseline)
142	    columns:
143	    - config
144	    - spearman_rho
145	    rows:
146	    - - greedy
147	      - 0.886
148	    - - p=0.9
149	      - 0.921
150	    - - T=0.7
151	      - 0.914
152	    - - T=1.2
153	      - 0.878
154	  figures_description:
155	  - 'K* vs 解码有效熵散点图: x轴为各解码配置的实际 token 分布熵估计，y轴为 K*。Greedy 在最左 K*=1，standard configs
156	    居中 K*=2，T=1.2 在最右 K*=3，形成清晰阶跃。'
157	  - '五配置 JSD decay 曲线族谱图: T=1.2 曲线在 depth=3 才穿过 θ=0.60 对应的 JSD 阈值线，greedy 在 depth=1
158	    就穿过，其余在 depth=2。'
159	  - 'Bootstrap CI 对比图: 各配置的 1v2 AUC 95% CI 与 θ=0.60 阈值线的关系，视觉化 K* 判定。'
160	  analysis: 'T=1.2 → K*=3 + greedy → K*=1 建立了完整的 K* 可调控梯度，这是论文最有力的发现之一。 审稿人无法再说 "K*=2
161	    is a ceiling"——它是 standard 解码下的 operating point，可被解码熵上下调控。 3/4 configs K*≥2 表明
162	    K*=2 在合理解码空间内高度稳健；greedy 的 K*=1 不是弱点而是优势： 它证明 K* 捕捉的是信道的真实信息论性质，而非分类器的统计 artifact。
163	    Feature ordering ρ≥0.878 跨所有配置，扩展了 exp-005 的 degradation ordering 一致性结论到新解码条件。
164	
165	    '
166	- name: Qwen2.5-7B 跨规模探测
167	  plan_id: exp-004
168	  description: 'Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth 0-3。 测试模型规模是否是
169	    K* 的杠杆。1K docs（vs 5K）引入更大方差但降低 GPU 成本。
170	
171	    '
172	  expected_results:
173	    pairwise_auc:
174	      0v1: 0.9984
175	      1v2: 0.6948
176	      2v3: 0.6175
177	    pairwise_auc_std:
178	      0v1: 0.0004
179	      1v2: 0.0092
180	      2v3: 0.0108
181	    pairwise_jsd:
182	      0v1: 0.3415
183	      1v2: 0.0285
184	      2v3: 0.0112
185	    k_star: 3
186	    ordinal_accuracy_4class: 0.4752
187	    ordinal_mae: 0.724
188	    bootstrap_ci_1v2:
189	    - 0.6782
190	    - 0.7108
191	    bootstrap_ci_2v3:
192	    - 0.6015
193	    - 0.6338
194	    top3_features:
195	    - surp_d1_std
196	    - surp_std
197	    - freq_entropy
198	    comparison_vs_1.5B:
199	      delta_auc_1v2: '+0.0834'
200	      delta_auc_2v3: '+0.0566'
201	      delta_jsd_0v1: '+0.0552'
202	  result_rationale: '7B 模型的参数空间是 1.5B 的 ~4.7 倍，编码了更丰富的语言分布。递归生成时，每代输出保留更多原始分布的细微结构：
203	    rare n-grams、长距离 discourse patterns、低频词汇的上下文相关用法。这些信息在 1.5B 级模型中首代就大部分丢失， 但在 7B
204	    中至少保持到第二代——因此 2v3 AUC=0.618 仍高于 θ=0.60，K*≥3。 具体机制：7B 的 next-token 分布有更长的"有意义尾巴"（tail
205	    tokens 仍携带语义区分力）， 递归第二代保留了这些 tail 的部分结构特征，到第三代才显著丢失。 1v2 AUC=0.695 较 1.5B 的 0.611
206	    提升 8.3pp，JSD_0v1=0.342 较 1.5B 的 0.286 提升 19%—— 更大模型的输出在特征空间中占据更大体积，递归压缩的"距离"更长。
207	    1K docs 的样本量约束使 CI 较宽（±0.015 vs 5K docs 的 ±0.010），但 2v3 CI lower=0.602 仍 comfortably
208	    高于 0.60。 Ordinal accuracy 4-class=0.475（chance=0.25），MAE=0.724，均显著优于 1.5B 的 6-class
209	    表现， 确认更多参数→更多可利用的代际特征梯度。
210	
211	    '
212	  tables:
213	  - caption: Qwen2.5-7B vs 1.5B pairwise discrimination 对比
214	    columns:
215	    - depth_pair
216	    - 7B_AUC
217	    - 7B_JSD
218	    - 1.5B_AUC_cont
219	    - 1.5B_JSD_cont
220	    rows:
221	    - - 0v1
222	      - 0.9984
223	      - 0.3415
224	      - 0.9972
225	      - 0.2863
226	    - - 1v2
227	      - 0.6948
228	      - 0.0285
229	      - 0.6114
230	      - 0.0051
231	    - - 2v3
232	      - 0.6175
233	      - 0.0112
234	      - 0.5609
235	      - 0.0036
236	  - caption: 7B bootstrap 95% CI
237	    columns:
238	    - depth_pair
239	    - AUC
240	    - CI_lower
241	    - CI_upper
242	    - CI_lower > 0.60?
243	    rows:
244	    - - 1v2
245	      - 0.6948
246	      - 0.6782
247	      - 0.7108
248	      - ✅ +7.8pp
249	    - - 2v3
250	      - 0.6175
251	      - 0.6015
252	      - 0.6338
253	      - ✅ +0.15pp
254	  figures_description:
255	  - 'Scale-K* 关系图: x轴为模型参数量（log scale: 1B, 1.4B, 1.5B, 7B），y轴为 K*。1B-1.5B 区间 K*=2
256	    稳定，7B 跳到 K*=3。虚线外推暗示更大模型 K*≥4。'
257	  - '7B vs 1.5B JSD decay 对比: 7B 曲线整体上移且右移，穿过 θ 阈值的 depth 更深，视觉化 scale → K* 效应。'
258	  analysis: '7B K*≥3 确认模型规模是 K* 的因果杠杆，与 exp-003 T=1.2 → K*=3 形成两条独立路径。 结合两者可写: "K*=2
259	    is not a ceiling but a floor that rises with model scale (7B) and decoding entropy
260	    (T=1.2)." 2v3 CI lower=0.602 虽然 margin 较小（受 1K docs 限制），但方向明确且与 1v2 的强信号一致。 如需更强统计力度，可考虑增至
261	    2K docs（额外 4 GPU-hours），但当前结果已足以支撑 claim。 对 ordinal_accuracy_best_model 的贡献: 7B
262	    4-class=0.475 落入 best 档范围 [0.42, 0.48]。
263	
264	    '
265	- name: Downstream graduated filtering 评估
266	  plan_id: exp-006
267	  description: 'Qwen2.5-1.5B depth chain (continuation mode), 比较 6 种过滤策略: no-filter
268	    / binary-ours (15D binary) / binary-Drayson (importance resampling) / graduated
269	    (3-class ordinal) / surprisal-based (单特征) / DSIR (分布匹配)。Continued pretraining
270	    + lm-eval-harness (MMLU, HellaSwag)。 5 seeds, paired t-test。graduated 加 α sensitivity
271	    sweep (α ∈ {0.1, 0.3, 0.5, 0.7, 0.9})。
272	
273	    '
274	  expected_results:
275	    mmlu_accuracy_pp:
276	      no_filter: 25.82
277	      binary_ours: 26.93
278	      binary_drayson: 27.21
279	      graduated_best_alpha: 29.41
280	      surprisal_based: 28.15
281	      dsir: 27.32
282	    hellaswag_accuracy_pp:
283	      no_filter: 43.24
284	      binary_ours: 44.38
285	      binary_drayson: 44.65
286	      graduated_best_alpha: 47.08
287	      surprisal_based: 45.92
288	      dsir: 44.81
289	    mmlu_std_5seeds:
290	      no_filter: 0.21
291	      binary_ours: 0.28
292	      binary_drayson: 0.32
293	      graduated: 0.25
294	      surprisal_based: 0.33
295	      dsir: 0.3
296	    hellaswag_std_5seeds:
297	      no_filter: 0.18
298	      binary_ours: 0.23
299	      binary_drayson: 0.27
300	      graduated: 0.2
301	      surprisal_based: 0.28
302	      dsir: 0.25
303	    key_deltas:
304	      graduated_minus_binary_ours_mmlu_pp: 2.48
305	      graduated_minus_binary_ours_hellaswag_pp: 2.7
306	      graduated_minus_dsir_mmlu_pp: 2.09
307	      graduated_minus_dsir_hellaswag_pp: 2.27
308	    paired_ttest_pvalues:
309	      graduated_vs_binary_ours_mmlu: 0.0043
310	      graduated_vs_binary_ours_hellaswag: 0.0067
311	      graduated_vs_dsir_mmlu: 0.0125
312	      graduated_vs_dsir_hellaswag: 0.0098
313	    alpha_sensitivity_mmlu:
314	      alpha_0.1: 27.45
315	      alpha_0.3: 28.72
316	      alpha_0.5: 29.41
317	      alpha_0.7: 29.08
318	      alpha_0.9: 28.14
319	    alpha_sensitivity_hellaswag:
320	      alpha_0.1: 44.85
321	      alpha_0.3: 46.28
322	      alpha_0.5: 47.08
323	      alpha_0.7: 46.72
324	      alpha_0.9: 45.65
325	    optimal_alpha: 0.5
326	  result_rationale: 'Binary filtering 的核心困境: gen-1 文本保留了原始文本 ~85% 的信息（0v1 AUC>0.99
327	    说明 gen-1 与 human 可区分， 但 1v2 AUC~0.61 说明 gen-1 仍保留了大部分质量）。Binary 策略要么丢掉这些高质量 gen-1（过严→训练数据量骤降），
328	    要么连 gen-2+ 一起保留（过松→引入已过 K* 的噪声数据）。 Graduated filtering 通过 3-class ordinal signal
329	    精确解耦: 对 gen-1 施加 α 衰减权重（降低但不移除）， 对 gen-2+ 完全移除。最优 α=0.5 意味着 gen-1 以半权重参与训练——保留了其信息价值同时抑制了合成偏差。
330	    MMLU 收益（+2.48pp）高于 HellaSwag，因为 MMLU 对知识密度更敏感：graduated 保留的 gen-1 中知识保真度高， binary
331	    移除后的知识缺口比常识推理缺口更难弥补。 Binary-Drayson 的 importance resampling 略优于 binary-ours（soft
332	    vs hard 决策边界），但仍做二值判断→无法利用 ordinal signal。 DSIR 做分布匹配但不估计 depth→对 depth-specific
333	    污染效果有限。 Surprisal-based 策略用单一特征（surprisal mean）做 proxy filtering，优于 binary 但不及
334	    graduated 的多维 ordinal signal。 α sensitivity 呈倒 U 形: α 太小（0.1）几乎等于 binary 移除，α
335	    太大（0.9）几乎等于 no-filter。 5 seeds paired t-test p<0.01 确认 graduated vs binary-ours
336	    的差异非采样噪声。
337	
338	    '
339	  tables:
340	  - caption: 6 策略 downstream 评估 (5 seeds mean ± std)
341	    columns:
342	    - strategy
343	    - MMLU_pp
344	    - MMLU_std
345	    - HellaSwag_pp
346	    - HS_std
347	    rows:
348	    - - no-filter
349	      - 25.82
350	      - 0.21
351	      - 43.24
352	      - 0.18
353	    - - binary-ours
354	      - 26.93
355	      - 0.28
356	      - 44.38
357	      - 0.23
358	    - - binary-Drayson
359	      - 27.21
360	      - 0.32
361	      - 44.65
362	      - 0.27
363	    - - graduated (α=0.5)
364	      - 29.41
365	      - 0.25
366	      - 47.08
367	      - 0.2
368	    - - surprisal-based
369	      - 28.15
370	      - 0.33
371	      - 45.92
372	      - 0.28
373	    - - DSIR
374	      - 27.32
375	      - 0.3
376	      - 44.81
377	      - 0.25
378	  - caption: 关键对比统计显著性 (paired t-test, 5 seeds)
379	    columns:
380	    - comparison
381	    - Δ_MMLU_pp
382	    - p_MMLU
383	    - Δ_HellaSwag_pp
384	    - p_HellaSwag
385	    rows:
386	    - - graduated vs binary-ours
387	      - 2.48
388	      - 0.0043
389	      - 2.7
390	      - 0.0067
391	    - - graduated vs DSIR
392	      - 2.09
393	      - 0.0125
394	      - 2.27
395	      - 0.0098
396	    - - graduated vs binary-Drayson
397	      - 2.2
398	      - 0.0082
399	      - 2.43
400	      - 0.0054
401	    - - graduated vs surprisal-based
402	      - 1.26
403	      - 0.0318
404	      - 1.16
405	      - 0.0425
406	  - caption: α sensitivity sweep (graduated, MMLU)
407	    columns:
408	    - α
409	    - MMLU_pp
410	    - HellaSwag_pp
411	    rows:
412	    - - 0.1
413	      - 27.45
414	      - 44.85
415	    - - 0.3
416	      - 28.72
417	      - 46.28
418	    - - 0.5
419	      - 29.41
420	      - 47.08
421	    - - 0.7
422	      - 29.08
423	      - 46.72
424	    - - 0.9
425	      - 28.14
426	      - 45.65
427	  figures_description:
428	  - '6 策略 benchmark bar chart (error bars = 1 std over 5 seeds): graduated 最高，与 binary-ours
429	    之间有清晰 gap。'
430	  - 'α sensitivity curve (倒 U 形): 最优 α=0.5，α→0 趋向 binary 性能，α→1 趋向 no-filter 性能。'
431	  - 'Filtering precision-recall 在 gen-1 附近: graduated 的 calibrated soft boundary vs
432	    binary 的 hard step function，视觉化 ordinal signal 的阈值优势。'
433	  analysis: 'graduated vs binary-ours Δ≥2.48pp (MMLU) 和 2.70pp (HellaSwag) 均落入 best
434	    档 [2.0, 4.0] 且 p<0.01。 C3 成立: 即使 K*=2 的粗粒度 3-class ordinal signal 也能在 downstream
435	    产生显著收益。 Binary-ours vs graduated 的唯一变量是 binary/ordinal decision→公平验证了 ordinal
436	    structure 的价值。 DSIR 和 binary-Drayson 的存在证明 graduated 的优势不仅来自"更好的 filtering"而是来自
437	    depth-aware 决策。 α=0.5 的最优性直观: gen-1 质量约为 human 的 ~85%（基于 1v2 AUC），半权重大致反映这个质量折扣。
438	
439	    '
440	- name: Retrain-chain 生态效度验证
441	  plan_id: exp-008
442	  description: 'Pythia-1.4B LoRA (rank=16, alpha=32) retrain-chain vs prompt-chain,
443	    C4 5K docs, depth 0-4。验证 prompt-chain 是否是 retrain-chain 的合理实验代理。
444	
445	    '
446	  expected_results:
447	    retrain_chain:
448	      k_star: 2
449	      pairwise_auc:
450	        0v1: 0.9895
451	        1v2: 0.6362
452	        2v3: 0.5448
453	        3v4: 0.5128
454	      pairwise_jsd:
455	        0v1: 0.2058
456	        1v2: 0.0118
457	        2v3: 0.0044
458	        3v4: 0.0029
459	    prompt_chain_actual:
460	      k_star: 2
461	      pairwise_auc:
462	        0v1: 0.9932
463	        1v2: 0.6539
464	        2v3: 0.5515
465	        3v4: 0.5153
466	    kstar_diff: 0
467	    auc_1v2_diff: -0.0177
468	    feature_distribution_jsd_retrain_vs_prompt:
469	      depth_0: 0.0018
470	      depth_1: 0.0162
471	      depth_2: 0.0285
472	      depth_3: 0.0378
473	    cross_method_transfer_retention: 0.915
474	  result_rationale: 'LoRA rank=16 (alpha=32) 只修改了参数空间中一个 16 维的低秩子空间， 实际参数变化量 < 模型总参数的
475	    0.2%——这意味着 retrain-chain 的每代"模型"与原始 Pythia-1.4B 高度相似。 因此 retrain-chain 的行为应近似于
476	    prompt-chain：两者都是同一个（或近似相同的）模型对自身输出的迭代。 K* diff=0：DPI 约束是拓扑性的——只要信道是有损的（LoRA 微调后仍是有损信道），收敛行为保持。
477	    AUC 差异 -0.018：retrain-chain 略低，因为 LoRA 微调在每代引入微小但累积的分布偏移， 这些偏移模糊了"纯递归"的代际边界——相当于在递归信道上叠加了一层
478	    adaptation noise。 Feature distribution JSD 随 depth 递增是预期行为：更深代际累积了更多 retrain 偏移。
479	    但 JSD < 0.04 在所有 depth，远低于代际间的 JSD（~0.01-0.21）， 确认 prompt-chain 的代际差异主导了 retrain
480	    偏移效应。 Cross-method transfer retention 91.5%: prompt-chain 上训练的 classifier 在 retrain-chain
481	    上保持高性能。
482	
483	    '
484	  tables:
485	  - caption: Retrain-chain vs prompt-chain 对比 (Pythia-1.4B)
486	    columns:
487	    - depth_pair
488	    - retrain_AUC
489	    - prompt_AUC
490	    - Δ_AUC
491	    rows:
492	    - - 0v1
493	      - 0.9895
494	      - 0.9932
495	      - -0.0037
496	    - - 1v2
497	      - 0.6362
498	      - 0.6539
499	      - -0.0177
500	    - - 2v3
501	      - 0.5448
502	      - 0.5515
503	      - -0.0067
504	    - - 3v4
505	      - 0.5128
506	      - 0.5153
507	      - -0.0025
508	  - caption: Feature 分布偏移 (retrain vs prompt JSD by depth)
509	    columns:
510	    - depth
511	    - JSD
512	    rows:
513	    - - 0
514	      - 0.0018
515	    - - 1
516	      - 0.0162
517	    - - 2
518	      - 0.0285
519	    - - 3
520	      - 0.0378
521	  figures_description:
522	  - 'Retrain vs prompt JSD decay 对比: 两条曲线近乎重叠，附 bootstrap 95% CI shading。'
523	  - 'Feature space t-SNE: retrain 和 prompt 在同一 depth 的点高度混合，depth 之间有清晰分离。不同颜色区分 method，不同标记区分
524	    depth。'
525	  analysis: 'K* diff=0 且 AUC 差异 < 2pp，直接回应 "prompt-chain 不代表真实递归污染" 的审稿人顾虑。 Prompt-chain
526	    作为 controlled proxy 的生态效度得到确认。 Feature JSD 随 depth 缓慢递增的模式可作为 supplementary 报告:
527	    它表明 retrain adaptation 的效应虽然累积但始终被代际退化信号所主导。 Cross-method transfer 91.5% 与 exp-013
528	    的 Pythia↔OLMo 91-92% 一致—— 换言之，prompt vs retrain 的差异与同族不同模型的差异量级相当。
529	
530	    '
531	- name: Contamination dose-response
532	  plan_id: exp-009
533	  description: '10%/30%/50% synthetic injection 比例下 graduated vs binary filtering
534	    的收益差异。 基于 exp-006 的实验框架，仅变化 injection 比例。5 seeds, MMLU+HellaSwag。
535	
536	    '
537	  expected_results:
538	    graduated_vs_binary_delta_mmlu_pp:
539	      injection_10pct: 0.72
540	      injection_30pct: 2.48
541	      injection_50pct: 3.82
542	    graduated_vs_binary_delta_hellaswag_pp:
543	      injection_10pct: 0.51
544	      injection_30pct: 2.7
545	      injection_50pct: 3.48
546	    graduated_vs_binary_pvalue_mmlu:
547	      injection_10pct: 0.142
548	      injection_30pct: 0.0043
549	      injection_50pct: 0.0008
550	    graduated_vs_binary_pvalue_hellaswag:
551	      injection_10pct: 0.218
552	      injection_30pct: 0.0067
553	      injection_50pct: 0.0012
554	    trend: monotonically increasing with injection rate
555	    significance_threshold_pct: ~20% injection for p<0.05
556	  result_rationale: '10% injection 时，训练数据中仅 10% 是合成文本（其中 gen-1 约 5%，gen-2+ 约 5%），
557	    binary 策略移除全部 10% 的信息损失较小，错分 gen-1 的代价也小（因为总量少）→graduated 的边际收益有限（<1pp, p>0.05）。
558	    30% 对应 exp-006 主实验条件，graduated 优势 ~2.5pp。 50% injection 是 graduated 价值最大化的条件:
559	    半数数据是合成的，其中 gen-1 占 ~25% 的全部训练数据。 Binary 面临极端权衡——移除全部 50% 导致训练数据减半（catastrophic
560	    data loss）， 保留则引入 ~25% gen-2+ 噪声。Graduated 精确解耦: gen-1 以 α=0.5 权重保留→等效保留 12.5%
561	    高质量数据， gen-2+ 移除→等效移除 25% 噪声。净效果: graduated 比 binary 多保留 12.5% 有用数据同时多移除等量噪声。
562	    单调递增趋势是 C3 的核心叙事: "The value of depth-aware curation scales with contamination
563	    severity."
564	
565	    '
566	  tables:
567	  - caption: 'Dose-response: graduated vs binary Δ by contamination rate'
568	    columns:
569	    - injection_rate
570	    - Δ_MMLU_pp
571	    - p_MMLU
572	    - Δ_HellaSwag_pp
573	    - p_HellaSwag
574	    rows:
575	    - - 10%
576	      - 0.72
577	      - 0.142
578	      - 0.51
579	      - 0.218
580	    - - 30%
581	      - 2.48
582	      - 0.0043
583	      - 2.7
584	      - 0.0067
585	    - - 50%
586	      - 3.82
587	      - 0.0008
588	      - 3.48
589	      - 0.0012
590	  figures_description:
591	  - 'Dose-response curve: x轴 injection rate, y轴 graduated−binary Δ (pp)。MMLU/HellaSwag
592	    两条线均单调递增。横虚线标注 2pp 和 p=0.05 阈值。'
593	  - 'Stacked bar: 各 injection rate 下 no-filter/binary/graduated 绝对性能对比。随着 injection
594	    rate 升高，no-filter 下降最快，graduated 最稳健。'
595	  analysis: '单调递增的 dose-response 关系是 graduated filtering 实际部署价值的最直接证据。 10% injection
596	    下 p>0.05 是预期中的——低污染率下任何 filtering 策略都足够好，无需精细化。 50% injection 下 Δ=3.82pp (MMLU)
597	    落入 best 档上限附近 [2.0, 4.0]。 这为 practical impact 叙事提供核心论据: 当前 web 数据合成文本比例估计 15-30%（且在增长），
598	    graduated filtering 在这个区间恰好开始产生统计显著收益，随比例增长价值越大。
599	
600	    '
601	- name: LLM zero-shot depth estimation baseline
602	  plan_id: exp-011
603	  description: 'GPT-4o / Claude 3.5 Sonnet 对 depth 0-4 文本做 zero-shot depth 判断。 200
604	    samples per depth (共 1000 样本), 5-class classification。 验证 depth estimation 不能被
605	    frontier LLM 的通用能力"免费"解决。
606	
607	    '
608	  expected_results:
609	    gpt4o:
610	      accuracy: 0.218
611	      mae: 1.742
612	      kendall_tau_with_true_depth: 0.082
613	      confusion_matrix_diagonal_pct: 0.218
614	    claude_3_5_sonnet:
615	      accuracy: 0.234
616	      mae: 1.668
617	      kendall_tau_with_true_depth: 0.118
618	      confusion_matrix_diagonal_pct: 0.234
619	    our_ordinal_classifier:
620	      accuracy: 0.423
621	      mae: 0.984
622	      kendall_tau_with_true_depth: 0.552
623	    random_baseline:
624	      accuracy: 0.2
625	      mae: 2.0
626	    llm_common_failure_mode: LLM 倾向将所有文本判为 depth 0 或 1，几乎不预测 depth≥3
627	  result_rationale: 'LLM zero-shot depth estimation 近乎随机，三个结构性原因: (1) Depth signal
628	    是统计性的——需要同一 domain 的多样本分布对比，单文本缺乏参照系。 LLM 每次只看一篇文本，无法感知"这篇相对于同源文本的 vocabulary
629	    diversity 降低了多少"。 (2) LLM 的"质量判断"偏向 fluency/coherence/factuality，而这些高层语义特征恰恰是最后才饱和的（与
630	    C2 degradation ordering 一致）。 即使 gen-3 的 vocabulary diversity 已严重退化，LLM 仍判定其"写得不错"因为它仍然
631	    fluent。 (3) Depth 是一个 training-data 中从未出现过的概念——LLM 没有被训练理解"递归生成导致的信息损失梯度"， 其世界模型中不存在"第
632	    N 代合成文本"这个 schema。 Claude 略优于 GPT-4o（差异在 noise range 内）可能反映 Claude 对文本微妙模式的 slightly
633	    better sensitivity。 两者均远低于 15D ordinal classifier（accuracy 0.42 vs 0.22），倍率 ~1.9x。
634	
635	    '
636	  tables:
637	  - caption: 'Zero-shot depth estimation: frontier LLM vs ordinal classifier'
638	    columns:
639	    - method
640	    - accuracy
641	    - MAE
642	    - Kendall_τ
643	    rows:
644	    - - GPT-4o (zero-shot)
645	      - 0.218
646	      - 1.742
647	      - 0.082
648	    - - Claude 3.5 Sonnet (zero-shot)
649	      - 0.234
650	      - 1.668
651	      - 0.118
652	    - - Random baseline
653	      - 0.2
654	      - 2.0
655	      - 0.0
656	    - - Our ordinal classifier (15D)
657	      - 0.423
658	      - 0.984
659	      - 0.552
660	  figures_description:
661	  - 'Confusion matrix 三面板: LLM 预测分布近乎 uniform（微偏向 depth 0-1），ordinal classifier 对角线主导。'
662	  - 'Per-depth accuracy breakdown: LLM 在 depth=0 的 accuracy 最高（~0.35）但仍低于 classifier（~0.70），depth≥2
663	    完全随机。'
664	  analysis: 'LLM zero-shot 仅比 random chance 高 1.8-3.4pp，而 ordinal classifier 高出 22.3pp。
665	    这确立了 depth estimation 作为需要专门方法的 task——不能被 frontier LLM 的 general intelligence
666	    "免费"解决。 这是论文 problem formulation 的关键支撑: 我们定义的问题是 genuinely novel 且有技术门槛的。 LLM
667	    偏向预测 depth=0/1 的 failure mode 与 C2 一致——高层语义质量在前几代保持， 导致 LLM "认为大部分文本都是 human-written
668	    或 first-generation"。
669	
670	    '
671	- name: Binary detector confidence 作为 depth proxy
672	  plan_id: exp-012
673	  description: 'DivEye / Binoculars score 与 true depth 的 Spearman correlation, 在 exp-001
674	    (Pythia) 和 exp-002 (OLMo) depth chain 上评估。
675	
676	    '
677	  expected_results:
678	    diveye:
679	      spearman_rho_with_depth: 0.223
680	      spearman_p_value: 0.001
681	      auc_0v1: 0.935
682	      auc_1v2: 0.528
683	      auc_2v3: 0.508
684	    binoculars:
685	      spearman_rho_with_depth: 0.184
686	      spearman_p_value: 0.003
687	      auc_0v1: 0.912
688	      auc_1v2: 0.521
689	      auc_2v3: 0.505
690	    our_15d_features:
691	      auc_0v1: 0.995
692	      auc_1v2: 0.634
693	      auc_2v3: 0.5505
694	    binary_score_depth_correlation_interpretation: 'Binary scores 在 depth=0→1 处有大跳跃然后
695	      plateau—— 所有 depth≥1 的合成文本在 binary score 空间中挤在一个窄 band 内。
696	
697	      '
698	  result_rationale: 'Binary detectors 的训练目标是最大化 real/synthetic 决策边界，不是估计 "how synthetic"。
699	    其 confidence score 在 depth=0→1 跳跃后迅速饱和，原因: (1) DivEye 和 Binoculars 使用的 summary
700	    statistics（如 min-k% perplexity、cross-entropy ratio） 在 gen-1 就已经偏离 human 文本的分布，之后
701	    gen-2→gen-5 的偏移量极小（增量 < noise）。 (2) 这些 detectors 被优化为在 human/synthetic 边界处有最大
702	    separability—— 边界远处（depth≥2）的分辨力从未被训练目标所选择。 Spearman ρ 显著但极弱（0.18-0.22），因为 depth=0
703	    vs depth≥1 的 rank 差异贡献了大部分 correlation， depth≥1 内部几乎无 rank 信息。 DivEye 略优于 Binoculars
704	    因为其 vocabulary diversity 相关特征恰好也编码了少量 depth 信息。 关键对比: 我们的 15D features 在 1v2 AUC
705	    上高出 binary detectors ~10pp， 证明 binary confidence ≠ depth，depth estimation 需要专用特征。
706	
707	    '
708	  tables:
709	  - caption: Binary detector scores 作为 depth proxy
710	    columns:
711	    - detector
712	    - Spearman_ρ
713	    - p_value
714	    - AUC_0v1
715	    - AUC_1v2
716	    - AUC_2v3
717	    rows:
718	    - - DivEye
719	      - 0.223
720	      - 0.001
721	      - 0.935
722	      - 0.528
723	      - 0.508
724	    - - Binoculars
725	      - 0.184
726	      - 0.003
727	      - 0.912
728	      - 0.521
729	      - 0.505
730	    - - Our 15D features
731	      - —
732	      - —
733	      - 0.995
734	      - 0.634
735	      - 0.551
736	  figures_description:
737	  - 'Binary score vs true depth scatter: score 在 depth=0→1 有大跳跃，depth≥1 几乎平坦 (ceiling
738	    effect)。附 LOESS smooth line。'
739	  - 'Pairwise AUC decay 对比: binary detectors 在 1v2 处即降至 chance level，我们的 features
740	    保持到 depth=2。'
741	  analysis: 'Binary detectors 在 0v1 处强劲（AUC 0.91-0.94）但 1v2 处近乎 chance level（0.52-0.53），
742	    直接证明 "binary detection ≠ depth estimation"。 这是论文 related work positioning 的关键数据:
743	    existing methods solve a different (easier) problem。 Spearman ρ 的统计显著性反映的是 binary
744	    信号本身（depth=0 vs all），而非 ordinal depth estimation 能力。
745	
746	    '
747	- name: Common Crawl 自然验证
748	  plan_id: exp-014
749	  description: '对 Common Crawl 2025/2026 snapshot 10K 样本做 depth 预测， 与 AlignScore (事实一致性)
750	    和 vocabulary richness 指标做 correlation。 无 ground truth，仅间接验证。
751	
752	    '
753	  expected_results:
754	    spearman_predicted_depth_vs_alignscore: -0.288
755	    spearman_predicted_depth_vs_vocab_richness: -0.342
756	    spearman_p_values:
757	      alignscore: <0.001
758	      vocab_richness: <0.001
759	    pct_samples_predicted_depth_geq_1: 17.5
760	    pct_samples_predicted_depth_geq_2: 6.8
761	    pct_samples_predicted_depth_geq_3: 2.1
762	    predicted_depth_distribution:
763	      depth_0: 82.5
764	      depth_1: 10.7
765	      depth_2: 4.7
766	      depth_3_plus: 2.1
767	  result_rationale: 'Common Crawl 中的真实合成文本比例和代际深度无 ground truth，只能通过与外部质量指标的 correlation
768	    间接验证。 Predicted depth 与 AlignScore 呈负相关（ρ≈-0.29），因为更深代际的文本在递归"电话游戏"中积累了更多事实偏差。
769	    与 vocabulary richness 的负相关更强（ρ≈-0.34），与 C2 degradation ordering 一致: vocabulary
770	    diversity 是最先退化的特征组，predicted depth 高的文本确实词汇更贫乏。 ~17.5% 样本被预测为 depth≥1 与 2025-2026
771	    时期 web 合成文本比例的外部估计（15-25%）一致。 Depth≥2 仅 6.8%——大部分合成文本是"首代"（直接由模型生成），多代递归仍是小众现象。
772	    相关性不高（|ρ|<0.35）是预期中的: wild data 的噪声（domain 多样性、unknown model 族、未知解码策略） 稀释了在 controlled
773	    实验中观察到的信号。这些结果属于 "proof of concept" 级别。
774	
775	    '
776	  tables:
777	  - caption: Common Crawl 自然验证
778	    columns:
779	    - metric
780	    - value
781	    rows:
782	    - - Spearman(pred depth, AlignScore)
783	      - -0.288
784	    - - Spearman(pred depth, vocab richness)
785	      - -0.342
786	    - - '% pred depth ≥ 1'
787	      - 17.5%
788	    - - '% pred depth ≥ 2'
789	      - 6.8%
790	    - - '% pred depth ≥ 3'
791	      - 2.1%
792	  figures_description:
793	  - 'Predicted depth 分布直方图: depth=0 占 82.5%，depth=1 占 10.7%，depth=2+ 占 6.8%。'
794	  - 'Predicted depth vs AlignScore scatter (LOESS smooth): 清晰下降趋势但散点稀疏。'
795	  - 'Predicted depth vs vocabulary richness scatter: 负相关趋势更清晰。'
796	  analysis: '自然验证提供 "proof of concept" 级别的 wild-data 证据。 相关性方向正确且显著，足以支持 appendix
797	    或 discussion section 的 generalizability 论述。 不足以作为 main claim 的证据但有效回应 "只在 controlled
798	    设置下验证" 的审稿人顾虑。 Predicted depth 分布与 web 合成文本比例估计的一致性增加了 classifier 的可信度。
799	
800	    '
801	- name: Learned representation baseline
802	  plan_id: exp-015
803	  description: 'Frozen Qwen2.5-1.5B embeddings (last hidden state, 1536-dim) + 2-layer
804	    MLP vs hand-crafted 15D features + LightGBM。在 Qwen continuation depth chain 上评估。
805	
806	    '
807	  expected_results:
808	    frozen_embeddings_mlp:
809	      auc_1v2: 0.5982
810	      mean_pw_auc: 0.5865
811	      ordinal_accuracy: 0.3708
812	      mae: 1.195
813	      training_time_gpu_hours: 2.6
814	      feature_dim: 1536
815	    handcrafted_15d:
816	      auc_1v2: 0.6112
817	      mean_pw_auc: 0.6048
818	      ordinal_accuracy: 0.3875
819	      mae: 1.155
820	      training_time_gpu_hours: 0.08
821	      feature_dim: 15
822	    gap_auc_1v2_pp: 1.3
823	    gap_mean_pw_auc_pp: 1.83
824	    gap_ordinal_accuracy_pp: 1.67
825	    cross_model_transfer_frozen:
826	      frozen_on_qwen_test_pythia_retention: 0.62
827	      handcrafted_on_qwen_test_pythia_retention: 0.85
828	  result_rationale: 'Frozen embeddings 包含丰富的语义信息但存在三个结构性劣势: (1) 1536 维中绝大部分编码内容语义（topic,
829	    entity, style），而非递归退化信号—— MLP 需要从高维空间中"挖掘"少数相关维度。在 5K 训练样本下，这个搜索问题容易过拟合。 (2) Frozen
830	    embeddings 来自同一模型（Qwen2.5-1.5B），引入自我参照偏差: 模型对自己生成的文本有系统性 embedding 偏向，但这种偏向在 cross-model
831	    设置下不 transfer—— 因此 frozen 的 cross-model retention 仅 62%，远低于 15D 的 85%。 (3) Embedding
832	    空间中的 depth signal 不是线性可分的，2-layer MLP 的容量有限。 Hand-crafted 15D 的优势: 每个特征都直接编码与递归退化相关的统计量（diversity/surprisal/tail
833	    weight）， 人类先验弥补了维度不足。AUC gap 1.30pp < 3pp (best 档要求 < 3pp)。 更关键的是 interpretability
834	    优势: 15D 支持 degradation ordering 分析（exp-005/C2）和 feature group ablation， 这是 frozen
835	    embeddings 无法提供的。论文叙事需要 interpretable features 来讲述 "which linguistic properties
836	    degrade first" 的故事。
837	
838	    '
839	  tables:
840	  - caption: Learned vs hand-crafted features 对比
841	    columns:
842	    - method
843	    - AUC_1v2
844	    - mean_pw_AUC
845	    - ordinal_acc
846	    - MAE
847	    - dim
848	    - GPU_hours
849	    rows:
850	    - - frozen embeddings + MLP
851	      - 0.5982
852	      - 0.5865
853	      - 0.3708
854	      - 1.195
855	      - 1536
856	      - 2.6
857	    - - hand-crafted 15D
858	      - 0.6112
859	      - 0.6048
860	      - 0.3875
861	      - 1.155
862	      - 15
863	      - 0.08
864	  - caption: Cross-model transfer 对比 (train Qwen → test Pythia)
865	    columns:
866	    - method
867	    - in_domain_acc
868	    - cross_model_acc
869	    - retention_pct
870	    rows:
871	    - - frozen embeddings
872	      - 0.3708
873	      - 0.2299
874	      - 62%
875	    - - hand-crafted 15D
876	      - 0.3875
877	      - 0.3294
878	      - 85%
879	  figures_description:
880	  - 'Performance vs interpretability 双轴图: 15D 在 Pareto 前沿（低维高性能），frozen 在高维略低性能区。'
881	  - 'Cross-model transfer retention bar chart: frozen 62% vs 15D 85%，视觉化 interpretable
882	    features 的 generalization 优势。'
883	  analysis: 'AUC gap 1.30pp < 3pp 满足 best 档假设。15D hand-crafted 在所有指标上优于或持平 frozen
884	    embeddings， 且维度低 102 倍、训练快 32.5 倍。 Cross-model transfer 的巨大差距（85% vs 62%）是 decisive
885	    argument: frozen embeddings 过拟合 model-specific embedding space，而 15D 统计特征是 model-agnostic
886	    的。 这验证了论文 "选择 interpretable features 不是方法论妥协而是设计优势" 的叙事， 同时回应审稿人 "为什么不用 learned
887	    representations" 的问题。
888	
889	    '
890	- name: Base vs Instruct 模型对比
891	  plan_id: exp-016
892	  description: 'Qwen2.5-1.5B base model (非 instruct 微调版) continuation mode, C4 5K
893	    docs, depth 0-5。 与 exp-017 (Qwen2.5-1.5B-Instruct continuation) 对比，分离 RLHF/instruction-tuning
894	    对 K* 的影响。
895	
896	    '
897	  expected_results:
898	    base:
899	      k_star: 2
900	      pairwise_auc:
901	        0v1: 0.9958
902	        1v2: 0.6382
903	        2v3: 0.5685
904	        3v4: 0.5358
905	        4v5: 0.5148
906	      pairwise_jsd:
907	        0v1: 0.2952
908	        1v2: 0.0068
909	        2v3: 0.0042
910	        3v4: 0.0032
911	        4v5: 0.0028
912	      ordinal_accuracy: 0.3948
913	      top3_features:
914	      - surp_d1_std
915	      - surp_std
916	      - freq_entropy
917	    instruct_actual:
918	      k_star: 2
919	      pairwise_auc:
920	        0v1: 0.9972
921	        1v2: 0.6114
922	        2v3: 0.5609
923	        3v4: 0.5408
924	        4v5: 0.5139
925	    base_vs_instruct_diff:
926	      delta_auc_1v2: '+0.0268'
927	      delta_auc_2v3: '+0.0076'
928	      delta_jsd_0v1: '+0.0089'
929	    feature_shift:
930	      surprisal_mean_base_vs_instruct: -0.14 std units
931	      vocab_diversity_base_vs_instruct: +0.06 std units
932	  result_rationale: 'RLHF/instruction-tuning 将模型输出拉向 "人类偏好的模式"——更规范的句式、更安全的措辞、更集中的
933	    vocabulary 选择。 这种 alignment 相当于对输出分布施加了额外的低熵约束，使得即使 gen-0→gen-1 的转换也已经部分"标准化"了。
934	    结果: instruct 模型的递归代际间差异更小，因为每代输出都被拉向同一个 "preferred mode"。 Base model 没有这个约束，输出更接近预训练数据的原始分布→递归代际间保留更多分布结构→1v2
935	    AUC 高 2.7pp。 但 K* 仍为 2: alignment 的影响是 quantitative（减弱信号 2.7pp）而非 qualitative（改变收敛行为）。
936	    DPI 的信息论约束在有无 RLHF 的情况下都成立——只要模型是有限容量的 lossy channel。 Surprisal mean 偏移为负（instruct
937	    更"可预测"，反映 RLHF 倾向于生成预期输出）; vocabulary diversity 偏移为正（instruct 词汇稍更多样，反映 RLHF 鼓励的表达丰富性）。
938	    两种偏移方向一致且量级小（< 0.15 std），为 discussion 段落提供数据。
939	
940	    '
941	  tables:
942	  - caption: Base vs Instruct 对比 (Qwen2.5-1.5B, continuation mode)
943	    columns:
944	    - variant
945	    - K*
946	    - AUC_0v1
947	    - AUC_1v2
948	    - AUC_2v3
949	    - JSD_0v1
950	    - ordinal_acc
951	    rows:
952	    - - base
953	      - 2
954	      - 0.9958
955	      - 0.6382
956	      - 0.5685
957	      - 0.2952
958	      - 0.3948
959	    - - instruct (exp-017)
960	      - 2
961	      - 0.9972
962	      - 0.6114
963	      - 0.5609
964	      - 0.2863
965	      - 0.3819
966	    - - Δ (base − instruct)
967	      - 0
968	      - '-0.0014'
969	      - '+0.0268'
970	      - '+0.0076'
971	      - '+0.0089'
972	      - '+0.0129'
973	  figures_description:
974	  - 'Base vs instruct JSD decay 对比: base 曲线在 depth 1-2 段系统性高于 instruct，差距在 depth≥3
975	    后消失。'
976	  - 'Feature distribution violin plots: base vs instruct 在 depth=1 的 surprisal mean
977	    和 vocab diversity 分布差异。'
978	  analysis: 'Base 信号更强但 K* 不变——RLHF alignment 压缩了代际差异但未改变信息论收敛行为。 这对实际应用有关键意义: 野外合成文本可能来自
979	    base 或 instruct 模型， K*=2 在两种设置下一致意味着 graduated filtering 框架对两者都适用。 Base model
980	    1v2 AUC=0.638 的 CI 预期 lower bound ~0.628（远高于 0.60）， 为 Qwen-cont instruct 的 0.0015
981	    margin 脆弱性提供了安全网: 即使 instruct 模型在重复实验中偶尔 CI lower 落到 0.599，base model 的稳健 K*=2
982	    仍支撑 claim。'
983	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efc1f891-1aac-4ad0-9680-a7405d21b733",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "23a6b292-1b1b-40ee-8e79-f641840749ab",
  "sourceToolAssistantUUID": "efc1f891-1aac-4ad0-9680-a7405d21b733",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-13T08:48:37.377Z_

<details><summary>↩ Tool result · `toolu_01GTMBwxwQRkWDSpqdVySyww`</summary>

```text
1	tier: best
2	narrative_guidance: 'C1'' 全面成立 + C3 downstream 收益显著。exp-003 解码消融建立 K* 可调控梯度（greedy
3	  K*=1 → standard K*=2 → high-temp K*=3）， 直接消解 "K*=2 太浅" 审稿人顾虑。exp-004 7B 确认 scale
4	  → K* 因果链（K*≥3），与 exp-003 形成两条独立路径推高 K*。 exp-006 graduated filtering 在 MMLU/HellaSwag
5	  上均显著优于 binary（Δ≥2pp, p<0.01），exp-009 dose-response 单调递增。 exp-015 15D hand-crafted
6	  features 与 frozen embeddings 差距 <1.5pp，支撑 interpretable features 叙事。 Qwen-cont 的
7	  0.0015 margin 脆弱性被 exp-003 新 configs 的一致 K*=2 所补偿——多条件汇聚证据远强于单点 CI。 所有完成实验的实际数据与
8	  best 档预测高度一致，原始 2+1 claim 结构可直接支撑 EMNLP 2026 Main，reviewer score 预期 3.5-4.0。
9	
10	  '
11	imagined_experiments:
12	- name: Qwen2.5-1.5B 解码策略消融
13	  plan_id: exp-003
14	  description: 'Qwen2.5-1.5B-Instruct continuation mode, C4 5K docs, depth 0-5, 4
15	    解码配置: greedy / nucleus p=0.9 T=1.0 / nucleus p=0.95 T=0.7 / nucleus p=0.95 T=1.2。
16	    Baseline 为 exp-017 (nucleus p=0.95, T=1.0, continuation): 1v2 AUC=0.6114, K*=2。
17	
18	    '
19	  expected_results:
20	    greedy:
21	      k_star: 1
22	      pairwise_auc:
23	        0v1: 0.9965
24	        1v2: 0.5862
25	        2v3: 0.5481
26	        3v4: 0.5225
27	        4v5: 0.5108
28	      pairwise_jsd:
29	        0v1: 0.2753
30	        1v2: 0.0038
31	        2v3: 0.0029
32	        3v4: 0.0022
33	        4v5: 0.0019
34	      ordinal_accuracy: 0.3412
35	    nucleus_p0.9_T1.0:
36	      k_star: 2
37	      pairwise_auc:
38	        0v1: 0.9968
39	        1v2: 0.6278
40	        2v3: 0.5582
41	        3v4: 0.5312
42	        4v5: 0.5124
43	      pairwise_jsd:
44	        0v1: 0.2814
45	        1v2: 0.0057
46	        2v3: 0.0035
47	        3v4: 0.0028
48	        4v5: 0.0024
49	      ordinal_accuracy: 0.3685
50	    T0.7_p0.95:
51	      k_star: 2
52	      pairwise_auc:
53	        0v1: 0.9963
54	        1v2: 0.6241
55	        2v3: 0.5558
56	        3v4: 0.5286
57	        4v5: 0.5115
58	      pairwise_jsd:
59	        0v1: 0.2685
60	        1v2: 0.0052
61	        2v3: 0.0033
62	        3v4: 0.0026
63	        4v5: 0.0022
64	      ordinal_accuracy: 0.3648
65	    T1.2_p0.95:
66	      k_star: 3
67	      pairwise_auc:
68	        0v1: 0.9981
69	        1v2: 0.6823
70	        2v3: 0.6218
71	        3v4: 0.5614
72	        4v5: 0.5305
73	      pairwise_jsd:
74	        0v1: 0.3082
75	        1v2: 0.0118
76	        2v3: 0.0056
77	        3v4: 0.0035
78	        4v5: 0.0027
79	      ordinal_accuracy: 0.3975
80	    cross_config_spearman_rho_feature_ordering:
81	      greedy_vs_baseline: 0.886
82	      p0.9_vs_baseline: 0.921
83	      T0.7_vs_baseline: 0.914
84	      T1.2_vs_baseline: 0.878
85	    k_star_summary: K*=2 in 3/4 configs (p=0.9, T=0.7, T=1.2≥2); K*=1 for greedy;
86	      K*=3 for T=1.2
87	  result_rationale: '解码策略通过控制 token 采样的有效熵，直接调控递归信道的信息保持率。 Greedy 解码（argmax）将输出钉死在条件分布的
88	    mode 上：gen-1 已高度确定性，gen-2 对 gen-1 施加相同的 argmax 压缩后几乎无新增信息损失可测—— 因此 1v2 AUC=0.586
89	    低于 θ=0.60 阈值，K*=1。这不是检测失败，而是 greedy 信道本身在首代就完成了绝大部分信息丢弃。 p=0.9（vs baseline p=0.95）仅移除尾部
90	    5% 概率质量的差异，效应量小——1v2 AUC 从 0.611 降到 0.628，仍稳定在 K*=2。 T=0.7 压缩 softmax 温度使分布更 peaked，效应与收窄
91	    nucleus 类似，1v2=0.624 保持 K*=2。 T=1.2 是关键条件：高温度展平分布→每代输出保留更多"非主流" token 选择→这些 tail
92	    tokens 携带的分布结构需要更多代际才能被递归"洗掉"。 信息论机制：T=1.2 抬高了初始互信息 I(X;Y₁)，DPI 保证 I(X;Yₖ) 单调递减，但更高起点意味着
93	    2v3 AUC=0.622 仍高于 0.60→K*=3。 Feature ordering 一致性（ρ≥0.878）表明解码策略改变信号强度但不改变哪些特征最先饱和——退化顺序是信息论结构性规律。
94	
95	    '
96	  tables:
97	  - caption: '解码策略消融: K* 与关键 pairwise AUC'
98	    columns:
99	    - decoding_config
100	    - K*
101	    - AUC_0v1
102	    - AUC_1v2
103	    - AUC_2v3
104	    - AUC_3v4
105	    - JSD_0v1
106	    rows:
107	    - - greedy
108	      - 1
109	      - 0.9965
110	      - 0.5862
111	      - 0.5481
112	      - 0.5225
113	      - 0.2753
114	    - - nucleus p=0.9 T=1.0
115	      - 2
116	      - 0.9968
117	      - 0.6278
118	      - 0.5582
119	      - 0.5312
120	      - 0.2814
121	    - - p=0.95 T=0.7
122	      - 2
123	      - 0.9963
124	      - 0.6241
125	      - 0.5558
126	      - 0.5286
127	      - 0.2685
128	    - - p=0.95 T=1.2
129	      - 3
130	      - 0.9981
131	      - 0.6823
132	      - 0.6218
133	      - 0.5614
134	      - 0.3082
135	    - - baseline (p=0.95 T=1.0)
136	      - 2
137	      - 0.9972
138	      - 0.6114
139	      - 0.5609
140	      - 0.5408
141	      - 0.2863
142	  - caption: Feature degradation ordering 一致性 (Spearman ρ vs baseline)
143	    columns:
144	    - config
145	    - spearman_rho
146	    rows:
147	    - - greedy
148	      - 0.886
149	    - - p=0.9
150	      - 0.921
151	    - - T=0.7
152	      - 0.914
153	    - - T=1.2
154	      - 0.878
155	  figures_description:
156	  - 'K* vs 解码有效熵散点图: x轴为各解码配置的实际 token 分布熵估计，y轴为 K*。Greedy 在最左 K*=1，standard configs
157	    居中 K*=2，T=1.2 在最右 K*=3，形成清晰阶跃。'
158	  - '五配置 JSD decay 曲线族谱图: T=1.2 曲线在 depth=3 才穿过 θ=0.60 对应的 JSD 阈值线，greedy 在 depth=1
159	    就穿过，其余在 depth=2。'
160	  - 'Bootstrap CI 对比图: 各配置的 1v2 AUC 95% CI 与 θ=0.60 阈值线的关系，视觉化 K* 判定。'
161	  analysis: 'T=1.2 → K*=3 + greedy → K*=1 建立了完整的 K* 可调控梯度，这是论文最有力的发现之一。 审稿人无法再说 "K*=2
162	    is a ceiling"——它是 standard 解码下的 operating point，可被解码熵上下调控。 3/4 configs K*≥2 表明
163	    K*=2 在合理解码空间内高度稳健；greedy 的 K*=1 不是弱点而是优势： 它证明 K* 捕捉的是信道的真实信息论性质，而非分类器的统计 artifact。
164	    Feature ordering ρ≥0.878 跨所有配置，扩展了 exp-005 的 degradation ordering 一致性结论到新解码条件。
165	
166	    '
167	- name: Qwen2.5-7B 跨规模探测
168	  plan_id: exp-004
169	  description: 'Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth 0-3。 测试模型规模是否是
170	    K* 的杠杆。1K docs（vs 5K）引入更大方差但降低 GPU 成本。
171	
172	    '
173	  expected_results:
174	    pairwise_auc:
175	      0v1: 0.9984
176	      1v2: 0.6948
177	      2v3: 0.6175
178	    pairwise_auc_std:
179	      0v1: 0.0004
180	      1v2: 0.0092
181	      2v3: 0.0108
182	    pairwise_jsd:
183	      0v1: 0.3415
184	      1v2: 0.0285
185	      2v3: 0.0112
186	    k_star: 3
187	    ordinal_accuracy_4class: 0.4752
188	    ordinal_mae: 0.724
189	    bootstrap_ci_1v2:
190	    - 0.6782
191	    - 0.7108
192	    bootstrap_ci_2v3:
193	    - 0.6015
194	    - 0.6338
195	    top3_features:
196	    - surp_d1_std
197	    - surp_std
198	    - freq_entropy
199	    comparison_vs_1.5B:
200	      delta_auc_1v2: '+0.0834'
201	      delta_auc_2v3: '+0.0566'
202	      delta_jsd_0v1: '+0.0552'
203	  result_rationale: '7B 模型的参数空间是 1.5B 的 ~4.7 倍，编码了更丰富的语言分布。递归生成时，每代输出保留更多原始分布的细微结构：
204	    rare n-grams、长距离 discourse patterns、低频词汇的上下文相关用法。这些信息在 1.5B 级模型中首代就大部分丢失， 但在 7B
205	    中至少保持到第二代——因此 2v3 AUC=0.618 仍高于 θ=0.60，K*≥3。 具体机制：7B 的 next-token 分布有更长的"有意义尾巴"（tail
206	    tokens 仍携带语义区分力）， 递归第二代保留了这些 tail 的部分结构特征，到第三代才显著丢失。 1v2 AUC=0.695 较 1.5B 的 0.611
207	    提升 8.3pp，JSD_0v1=0.342 较 1.5B 的 0.286 提升 19%—— 更大模型的输出在特征空间中占据更大体积，递归压缩的"距离"更长。
208	    1K docs 的样本量约束使 CI 较宽（±0.015 vs 5K docs 的 ±0.010），但 2v3 CI lower=0.602 仍 comfortably
209	    高于 0.60。 Ordinal accuracy 4-class=0.475（chance=0.25），MAE=0.724，均显著优于 1.5B 的 6-class
210	    表现， 确认更多参数→更多可利用的代际特征梯度。
211	
212	    '
213	  tables:
214	  - caption: Qwen2.5-7B vs 1.5B pairwise discrimination 对比
215	    columns:
216	    - depth_pair
217	    - 7B_AUC
218	    - 7B_JSD
219	    - 1.5B_AUC_cont
220	    - 1.5B_JSD_cont
221	    rows:
222	    - - 0v1
223	      - 0.9984
224	      - 0.3415
225	      - 0.9972
226	      - 0.2863
227	    - - 1v2
228	      - 0.6948
229	      - 0.0285
230	      - 0.6114
231	      - 0.0051
232	    - - 2v3
233	      - 0.6175
234	      - 0.0112
235	      - 0.5609
236	      - 0.0036
237	  - caption: 7B bootstrap 95% CI
238	    columns:
239	    - depth_pair
240	    - AUC
241	    - CI_lower
242	    - CI_upper
243	    - CI_lower > 0.60?
244	    rows:
245	    - - 1v2
246	      - 0.6948
247	      - 0.6782
248	      - 0.7108
249	      - ✅ +7.8pp
250	    - - 2v3
251	      - 0.6175
252	      - 0.6015
253	      - 0.6338
254	      - ✅ +0.15pp
255	  figures_description:
256	  - 'Scale-K* 关系图: x轴为模型参数量（log scale: 1B, 1.4B, 1.5B, 7B），y轴为 K*。1B-1.5B 区间 K*=2
257	    稳定，7B 跳到 K*=3。虚线外推暗示更大模型 K*≥4。'
258	  - '7B vs 1.5B JSD decay 对比: 7B 曲线整体上移且右移，穿过 θ 阈值的 depth 更深，视觉化 scale → K* 效应。'
259	  analysis: '7B K*≥3 确认模型规模是 K* 的因果杠杆，与 exp-003 T=1.2 → K*=3 形成两条独立路径。 结合两者可写: "K*=2
260	    is not a ceiling but a floor that rises with model scale (7B) and decoding entropy
261	    (T=1.2)." 2v3 CI lower=0.602 虽然 margin 较小（受 1K docs 限制），但方向明确且与 1v2 的强信号一致。 如需更强统计力度，可考虑增至
262	    2K docs（额外 4 GPU-hours），但当前结果已足以支撑 claim。 对 ordinal_accuracy_best_model 的贡献: 7B
263	    4-class=0.475 落入 best 档范围 [0.42, 0.48]。
264	
265	    '
266	- name: Downstream graduated filtering 评估
267	  plan_id: exp-006
268	  description: 'Qwen2.5-1.5B depth chain (continuation mode), 比较 6 种过滤策略: no-filter
269	    / binary-ours (15D binary) / binary-Drayson (importance resampling) / graduated
270	    (3-class ordinal) / surprisal-based (单特征) / DSIR (分布匹配)。Continued pretraining
271	    + lm-eval-harness (MMLU, HellaSwag)。 5 seeds, paired t-test。graduated 加 α sensitivity
272	    sweep (α ∈ {0.1, 0.3, 0.5, 0.7, 0.9})。
273	
274	    '
275	  expected_results:
276	    mmlu_accuracy_pp:
277	      no_filter: 25.82
278	      binary_ours: 26.93
279	      binary_drayson: 27.21
280	      graduated_best_alpha: 29.41
281	      surprisal_based: 28.15
282	      dsir: 27.32
283	    hellaswag_accuracy_pp:
284	      no_filter: 43.24
285	      binary_ours: 44.38
286	      binary_drayson: 44.65
287	      graduated_best_alpha: 47.08
288	      surprisal_based: 45.92
289	      dsir: 44.81
290	    mmlu_std_5seeds:
291	      no_filter: 0.21
292	      binary_ours: 0.28
293	      binary_drayson: 0.32
294	      graduated: 0.25
295	      surprisal_based: 0.33
296	      dsir: 0.3
297	    hellaswag_std_5seeds:
298	      no_filter: 0.18
299	      binary_ours: 0.23
300	      binary_drayson: 0.27
301	      graduated: 0.2
302	      surprisal_based: 0.28
303	      dsir: 0.25
304	    key_deltas:
305	      graduated_minus_binary_ours_mmlu_pp: 2.48
306	      graduated_minus_binary_ours_hellaswag_pp: 2.7
307	      graduated_minus_dsir_mmlu_pp: 2.09
308	      graduated_minus_dsir_hellaswag_pp: 2.27
309	    paired_ttest_pvalues:
310	      graduated_vs_binary_ours_mmlu: 0.0043
311	      graduated_vs_binary_ours_hellaswag: 0.0067
312	      graduated_vs_dsir_mmlu: 0.0125
313	      graduated_vs_dsir_hellaswag: 0.0098
314	    alpha_sensitivity_mmlu:
315	      alpha_0.1: 27.45
316	      alpha_0.3: 28.72
317	      alpha_0.5: 29.41
318	      alpha_0.7: 29.08
319	      alpha_0.9: 28.14
320	    alpha_sensitivity_hellaswag:
321	      alpha_0.1: 44.85
322	      alpha_0.3: 46.28
323	      alpha_0.5: 47.08
324	      alpha_0.7: 46.72
325	      alpha_0.9: 45.65
326	    optimal_alpha: 0.5
327	  result_rationale: 'Binary filtering 的核心困境: gen-1 文本保留了原始文本 ~85% 的信息（0v1 AUC>0.99
328	    说明 gen-1 与 human 可区分， 但 1v2 AUC~0.61 说明 gen-1 仍保留了大部分质量）。Binary 策略要么丢掉这些高质量 gen-1（过严→训练数据量骤降），
329	    要么连 gen-2+ 一起保留（过松→引入已过 K* 的噪声数据）。 Graduated filtering 通过 3-class ordinal signal
330	    精确解耦: 对 gen-1 施加 α 衰减权重（降低但不移除）， 对 gen-2+ 完全移除。最优 α=0.5 意味着 gen-1 以半权重参与训练——保留了其信息价值同时抑制了合成偏差。
331	    MMLU 收益（+2.48pp）高于 HellaSwag，因为 MMLU 对知识密度更敏感：graduated 保留的 gen-1 中知识保真度高， binary
332	    移除后的知识缺口比常识推理缺口更难弥补。 Binary-Drayson 的 importance resampling 略优于 binary-ours（soft
333	    vs hard 决策边界），但仍做二值判断→无法利用 ordinal signal。 DSIR 做分布匹配但不估计 depth→对 depth-specific
334	    污染效果有限。 Surprisal-based 策略用单一特征（surprisal mean）做 proxy filtering，优于 binary 但不及
335	    graduated 的多维 ordinal signal。 α sensitivity 呈倒 U 形: α 太小（0.1）几乎等于 binary 移除，α
336	    太大（0.9）几乎等于 no-filter。 5 seeds paired t-test p<0.01 确认 graduated vs binary-ours
337	    的差异非采样噪声。
338	
339	    '
340	  tables:
341	  - caption: 6 策略 downstream 评估 (5 seeds mean ± std)
342	    columns:
343	    - strategy
344	    - MMLU_pp
345	    - MMLU_std
346	    - HellaSwag_pp
347	    - HS_std
348	    rows:
349	    - - no-filter
350	      - 25.82
351	      - 0.21
352	      - 43.24
353	      - 0.18
354	    - - binary-ours
355	      - 26.93
356	      - 0.28
357	      - 44.38
358	      - 0.23
359	    - - binary-Drayson
360	      - 27.21
361	      - 0.32
362	      - 44.65
363	      - 0.27
364	    - - graduated (α=0.5)
365	      - 29.41
366	      - 0.25
367	      - 47.08
368	      - 0.2
369	    - - surprisal-based
370	      - 28.15
371	      - 0.33
372	      - 45.92
373	      - 0.28
374	    - - DSIR
375	      - 27.32
376	      - 0.3
377	      - 44.81
378	      - 0.25
379	  - caption: 关键对比统计显著性 (paired t-test, 5 seeds)
380	    columns:
381	    - comparison
382	    - Δ_MMLU_pp
383	    - p_MMLU
384	    - Δ_HellaSwag_pp
385	    - p_HellaSwag
386	    rows:
387	    - - graduated vs binary-ours
388	      - 2.48
389	      - 0.0043
390	      - 2.7
391	      - 0.0067
392	    - - graduated vs DSIR
393	      - 2.09
394	      - 0.0125
395	      - 2.27
396	      - 0.0098
397	    - - graduated vs binary-Drayson
398	      - 2.2
399	      - 0.0082
400	      - 2.43
401	      - 0.0054
402	    - - graduated vs surprisal-based
403	      - 1.26
404	      - 0.0318
405	      - 1.16
406	      - 0.0425
407	  - caption: α sensitivity sweep (graduated, MMLU)
408	    columns:
409	    - α
410	    - MMLU_pp
411	    - HellaSwag_pp
412	    rows:
413	    - - 0.1
414	      - 27.45
415	      - 44.85
416	    - - 0.3
417	      - 28.72
418	      - 46.28
419	    - - 0.5
420	      - 29.41
421	      - 47.08
422	    - - 0.7
423	      - 29.08
424	      - 46.72
425	    - - 0.9
426	      - 28.14
427	      - 45.65
428	  figures_description:
429	  - '6 策略 benchmark bar chart (error bars = 1 std over 5 seeds): graduated 最高，与 binary-ours
430	    之间有清晰 gap。'
431	  - 'α sensitivity curve (倒 U 形): 最优 α=0.5，α→0 趋向 binary 性能，α→1 趋向 no-filter 性能。'
432	  - 'Filtering precision-recall 在 gen-1 附近: graduated 的 calibrated soft boundary vs
433	    binary 的 hard step function，视觉化 ordinal signal 的阈值优势。'
434	  analysis: 'graduated vs binary-ours Δ≥2.48pp (MMLU) 和 2.70pp (HellaSwag) 均落入 best
435	    档 [2.0, 4.0] 且 p<0.01。 C3 成立: 即使 K*=2 的粗粒度 3-class ordinal signal 也能在 downstream
436	    产生显著收益。 Binary-ours vs graduated 的唯一变量是 binary/ordinal decision→公平验证了 ordinal
437	    structure 的价值。 DSIR 和 binary-Drayson 的存在证明 graduated 的优势不仅来自"更好的 filtering"而是来自
438	    depth-aware 决策。 α=0.5 的最优性直观: gen-1 质量约为 human 的 ~85%（基于 1v2 AUC），半权重大致反映这个质量折扣。
439	
440	    '
441	- name: Retrain-chain 生态效度验证
442	  plan_id: exp-008
443	  description: 'Pythia-1.4B LoRA (rank=16, alpha=32) retrain-chain vs prompt-chain,
444	    C4 5K docs, depth 0-4。验证 prompt-chain 是否是 retrain-chain 的合理实验代理。
445	
446	    '
447	  expected_results:
448	    retrain_chain:
449	      k_star: 2
450	      pairwise_auc:
451	        0v1: 0.9895
452	        1v2: 0.6362
453	        2v3: 0.5448
454	        3v4: 0.5128
455	      pairwise_jsd:
456	        0v1: 0.2058
457	        1v2: 0.0118
458	        2v3: 0.0044
459	        3v4: 0.0029
460	    prompt_chain_actual:
461	      k_star: 2
462	      pairwise_auc:
463	        0v1: 0.9932
464	        1v2: 0.6539
465	        2v3: 0.5515
466	        3v4: 0.5153
467	    kstar_diff: 0
468	    auc_1v2_diff: -0.0177
469	    feature_distribution_jsd_retrain_vs_prompt:
470	      depth_0: 0.0018
471	      depth_1: 0.0162
472	      depth_2: 0.0285
473	      depth_3: 0.0378
474	    cross_method_transfer_retention: 0.915
475	  result_rationale: 'LoRA rank=16 (alpha=32) 只修改了参数空间中一个 16 维的低秩子空间， 实际参数变化量 < 模型总参数的
476	    0.2%——这意味着 retrain-chain 的每代"模型"与原始 Pythia-1.4B 高度相似。 因此 retrain-chain 的行为应近似于
477	    prompt-chain：两者都是同一个（或近似相同的）模型对自身输出的迭代。 K* diff=0：DPI 约束是拓扑性的——只要信道是有损的（LoRA 微调后仍是有损信道），收敛行为保持。
478	    AUC 差异 -0.018：retrain-chain 略低，因为 LoRA 微调在每代引入微小但累积的分布偏移， 这些偏移模糊了"纯递归"的代际边界——相当于在递归信道上叠加了一层
479	    adaptation noise。 Feature distribution JSD 随 depth 递增是预期行为：更深代际累积了更多 retrain 偏移。
480	    但 JSD < 0.04 在所有 depth，远低于代际间的 JSD（~0.01-0.21）， 确认 prompt-chain 的代际差异主导了 retrain
481	    偏移效应。 Cross-method transfer retention 91.5%: prompt-chain 上训练的 classifier 在 retrain-chain
482	    上保持高性能。
483	
484	    '
485	  tables:
486	  - caption: Retrain-chain vs prompt-chain 对比 (Pythia-1.4B)
487	    columns:
488	    - depth_pair
489	    - retrain_AUC
490	    - prompt_AUC
491	    - Δ_AUC
492	    rows:
493	    - - 0v1
494	      - 0.9895
495	      - 0.9932
496	      - -0.0037
497	    - - 1v2
498	      - 0.6362
499	      - 0.6539
500	      - -0.0177
501	    - - 2v3
502	      - 0.5448
503	      - 0.5515
504	      - -0.0067
505	    - - 3v4
506	      - 0.5128
507	      - 0.5153
508	      - -0.0025
509	  - caption: Feature 分布偏移 (retrain vs prompt JSD by depth)
510	    columns:
511	    - depth
512	    - JSD
513	    rows:
514	    - - 0
515	      - 0.0018
516	    - - 1
517	      - 0.0162
518	    - - 2
519	      - 0.0285
520	    - - 3
521	      - 0.0378
522	  figures_description:
523	  - 'Retrain vs prompt JSD decay 对比: 两条曲线近乎重叠，附 bootstrap 95% CI shading。'
524	  - 'Feature space t-SNE: retrain 和 prompt 在同一 depth 的点高度混合，depth 之间有清晰分离。不同颜色区分 method，不同标记区分
525	    depth。'
526	  analysis: 'K* diff=0 且 AUC 差异 < 2pp，直接回应 "prompt-chain 不代表真实递归污染" 的审稿人顾虑。 Prompt-chain
527	    作为 controlled proxy 的生态效度得到确认。 Feature JSD 随 depth 缓慢递增的模式可作为 supplementary 报告:
528	    它表明 retrain adaptation 的效应虽然累积但始终被代际退化信号所主导。 Cross-method transfer 91.5% 与 exp-013
529	    的 Pythia↔OLMo 91-92% 一致—— 换言之，prompt vs retrain 的差异与同族不同模型的差异量级相当。
530	
531	    '
532	- name: Contamination dose-response
533	  plan_id: exp-009
534	  description: '10%/30%/50% synthetic injection 比例下 graduated vs binary filtering
535	    的收益差异。 基于 exp-006 的实验框架，仅变化 injection 比例。5 seeds, MMLU+HellaSwag。
536	
537	    '
538	  expected_results:
539	    graduated_vs_binary_delta_mmlu_pp:
540	      injection_10pct: 0.72
541	      injection_30pct: 2.48
542	      injection_50pct: 3.82
543	    graduated_vs_binary_delta_hellaswag_pp:
544	      injection_10pct: 0.51
545	      injection_30pct: 2.7
546	      injection_50pct: 3.48
547	    graduated_vs_binary_pvalue_mmlu:
548	      injection_10pct: 0.142
549	      injection_30pct: 0.0043
550	      injection_50pct: 0.0008
551	    graduated_vs_binary_pvalue_hellaswag:
552	      injection_10pct: 0.218
553	      injection_30pct: 0.0067
554	      injection_50pct: 0.0012
555	    trend: monotonically increasing with injection rate
556	    significance_threshold_pct: ~20% injection for p<0.05
557	  result_rationale: '10% injection 时，训练数据中仅 10% 是合成文本（其中 gen-1 约 5%，gen-2+ 约 5%），
558	    binary 策略移除全部 10% 的信息损失较小，错分 gen-1 的代价也小（因为总量少）→graduated 的边际收益有限（<1pp, p>0.05）。
559	    30% 对应 exp-006 主实验条件，graduated 优势 ~2.5pp。 50% injection 是 graduated 价值最大化的条件:
560	    半数数据是合成的，其中 gen-1 占 ~25% 的全部训练数据。 Binary 面临极端权衡——移除全部 50% 导致训练数据减半（catastrophic
561	    data loss）， 保留则引入 ~25% gen-2+ 噪声。Graduated 精确解耦: gen-1 以 α=0.5 权重保留→等效保留 12.5%
562	    高质量数据， gen-2+ 移除→等效移除 25% 噪声。净效果: graduated 比 binary 多保留 12.5% 有用数据同时多移除等量噪声。
563	    单调递增趋势是 C3 的核心叙事: "The value of depth-aware curation scales with contamination
564	    severity."
565	
566	    '
567	  tables:
568	  - caption: 'Dose-response: graduated vs binary Δ by contamination rate'
569	    columns:
570	    - injection_rate
571	    - Δ_MMLU_pp
572	    - p_MMLU
573	    - Δ_HellaSwag_pp
574	    - p_HellaSwag
575	    rows:
576	    - - 10%
577	      - 0.72
578	      - 0.142
579	      - 0.51
580	      - 0.218
581	    - - 30%
582	      - 2.48
583	      - 0.0043
584	      - 2.7
585	      - 0.0067
586	    - - 50%
587	      - 3.82
588	      - 0.0008
589	      - 3.48
590	      - 0.0012
591	  figures_description:
592	  - 'Dose-response curve: x轴 injection rate, y轴 graduated−binary Δ (pp)。MMLU/HellaSwag
593	    两条线均单调递增。横虚线标注 2pp 和 p=0.05 阈值。'
594	  - 'Stacked bar: 各 injection rate 下 no-filter/binary/graduated 绝对性能对比。随着 injection
595	    rate 升高，no-filter 下降最快，graduated 最稳健。'
596	  analysis: '单调递增的 dose-response 关系是 graduated filtering 实际部署价值的最直接证据。 10% injection
597	    下 p>0.05 是预期中的——低污染率下任何 filtering 策略都足够好，无需精细化。 50% injection 下 Δ=3.82pp (MMLU)
598	    落入 best 档上限附近 [2.0, 4.0]。 这为 practical impact 叙事提供核心论据: 当前 web 数据合成文本比例估计 15-30%（且在增长），
599	    graduated filtering 在这个区间恰好开始产生统计显著收益，随比例增长价值越大。
600	
601	    '
602	- name: LLM zero-shot depth estimation baseline
603	  plan_id: exp-011
604	  description: 'GPT-4o / Claude 3.5 Sonnet 对 depth 0-4 文本做 zero-shot depth 判断。 200
605	    samples per depth (共 1000 样本), 5-class classification。 验证 depth estimation 不能被
606	    frontier LLM 的通用能力"免费"解决。
607	
608	    '
609	  expected_results:
610	    gpt4o:
611	      accuracy: 0.218
612	      mae: 1.742
613	      kendall_tau_with_true_depth: 0.082
614	      confusion_matrix_diagonal_pct: 0.218
615	    claude_3_5_sonnet:
616	      accuracy: 0.234
617	      mae: 1.668
618	      kendall_tau_with_true_depth: 0.118
619	      confusion_matrix_diagonal_pct: 0.234
620	    our_ordinal_classifier:
621	      accuracy: 0.423
622	      mae: 0.984
623	      kendall_tau_with_true_depth: 0.552
624	    random_baseline:
625	      accuracy: 0.2
626	      mae: 2.0
627	    llm_common_failure_mode: LLM 倾向将所有文本判为 depth 0 或 1，几乎不预测 depth≥3
628	  result_rationale: 'LLM zero-shot depth estimation 近乎随机，三个结构性原因: (1) Depth signal
629	    是统计性的——需要同一 domain 的多样本分布对比，单文本缺乏参照系。 LLM 每次只看一篇文本，无法感知"这篇相对于同源文本的 vocabulary
630	    diversity 降低了多少"。 (2) LLM 的"质量判断"偏向 fluency/coherence/factuality，而这些高层语义特征恰恰是最后才饱和的（与
631	    C2 degradation ordering 一致）。 即使 gen-3 的 vocabulary diversity 已严重退化，LLM 仍判定其"写得不错"因为它仍然
632	    fluent。 (3) Depth 是一个 training-data 中从未出现过的概念——LLM 没有被训练理解"递归生成导致的信息损失梯度"， 其世界模型中不存在"第
633	    N 代合成文本"这个 schema。 Claude 略优于 GPT-4o（差异在 noise range 内）可能反映 Claude 对文本微妙模式的 slightly
634	    better sensitivity。 两者均远低于 15D ordinal classifier（accuracy 0.42 vs 0.22），倍率 ~1.9x。
635	
636	    '
637	  tables:
638	  - caption: 'Zero-shot depth estimation: frontier LLM vs ordinal classifier'
639	    columns:
640	    - method
641	    - accuracy
642	    - MAE
643	    - Kendall_τ
644	    rows:
645	    - - GPT-4o (zero-shot)
646	      - 0.218
647	      - 1.742
648	      - 0.082
649	    - - Claude 3.5 Sonnet (zero-shot)
650	      - 0.234
651	      - 1.668
652	      - 0.118
653	    - - Random baseline
654	      - 0.2
655	      - 2.0
656	      - 0.0
657	    - - Our ordinal classifier (15D)
658	      - 0.423
659	      - 0.984
660	      - 0.552
661	  figures_description:
662	  - 'Confusion matrix 三面板: LLM 预测分布近乎 uniform（微偏向 depth 0-1），ordinal classifier 对角线主导。'
663	  - 'Per-depth accuracy breakdown: LLM 在 depth=0 的 accuracy 最高（~0.35）但仍低于 classifier（~0.70），depth≥2
664	    完全随机。'
665	  analysis: 'LLM zero-shot 仅比 random chance 高 1.8-3.4pp，而 ordinal classifier 高出 22.3pp。
666	    这确立了 depth estimation 作为需要专门方法的 task——不能被 frontier LLM 的 general intelligence
667	    "免费"解决。 这是论文 problem formulation 的关键支撑: 我们定义的问题是 genuinely novel 且有技术门槛的。 LLM
668	    偏向预测 depth=0/1 的 failure mode 与 C2 一致——高层语义质量在前几代保持， 导致 LLM "认为大部分文本都是 human-written
669	    或 first-generation"。
670	
671	    '
672	- name: Binary detector confidence 作为 depth proxy
673	  plan_id: exp-012
674	  description: 'DivEye / Binoculars score 与 true depth 的 Spearman correlation, 在 exp-001
675	    (Pythia) 和 exp-002 (OLMo) depth chain 上评估。
676	
677	    '
678	  expected_results:
679	    diveye:
680	      spearman_rho_with_depth: 0.223
681	      spearman_p_value: 0.001
682	      auc_0v1: 0.935
683	      auc_1v2: 0.528
684	      auc_2v3: 0.508
685	    binoculars:
686	      spearman_rho_with_depth: 0.184
687	      spearman_p_value: 0.003
688	      auc_0v1: 0.912
689	      auc_1v2: 0.521
690	      auc_2v3: 0.505
691	    our_15d_features:
692	      auc_0v1: 0.995
693	      auc_1v2: 0.634
694	      auc_2v3: 0.5505
695	    binary_score_depth_correlation_interpretation: 'Binary scores 在 depth=0→1 处有大跳跃然后
696	      plateau—— 所有 depth≥1 的合成文本在 binary score 空间中挤在一个窄 band 内。
697	
698	      '
699	  result_rationale: 'Binary detectors 的训练目标是最大化 real/synthetic 决策边界，不是估计 "how synthetic"。
700	    其 confidence score 在 depth=0→1 跳跃后迅速饱和，原因: (1) DivEye 和 Binoculars 使用的 summary
701	    statistics（如 min-k% perplexity、cross-entropy ratio） 在 gen-1 就已经偏离 human 文本的分布，之后
702	    gen-2→gen-5 的偏移量极小（增量 < noise）。 (2) 这些 detectors 被优化为在 human/synthetic 边界处有最大
703	    separability—— 边界远处（depth≥2）的分辨力从未被训练目标所选择。 Spearman ρ 显著但极弱（0.18-0.22），因为 depth=0
704	    vs depth≥1 的 rank 差异贡献了大部分 correlation， depth≥1 内部几乎无 rank 信息。 DivEye 略优于 Binoculars
705	    因为其 vocabulary diversity 相关特征恰好也编码了少量 depth 信息。 关键对比: 我们的 15D features 在 1v2 AUC
706	    上高出 binary detectors ~10pp， 证明 binary confidence ≠ depth，depth estimation 需要专用特征。
707	
708	    '
709	  tables:
710	  - caption: Binary detector scores 作为 depth proxy
711	    columns:
712	    - detector
713	    - Spearman_ρ
714	    - p_value
715	    - AUC_0v1
716	    - AUC_1v2
717	    - AUC_2v3
718	    rows:
719	    - - DivEye
720	      - 0.223
721	      - 0.001
722	      - 0.935
723	      - 0.528
724	      - 0.508
725	    - - Binoculars
726	      - 0.184
727	      - 0.003
728	      - 0.912
729	      - 0.521
730	      - 0.505
731	    - - Our 15D features
732	      - —
733	      - —
734	      - 0.995
735	      - 0.634
736	      - 0.551
737	  figures_description:
738	  - 'Binary score vs true depth scatter: score 在 depth=0→1 有大跳跃，depth≥1 几乎平坦 (ceiling
739	    effect)。附 LOESS smooth line。'
740	  - 'Pairwise AUC decay 对比: binary detectors 在 1v2 处即降至 chance level，我们的 features
741	    保持到 depth=2。'
742	  analysis: 'Binary detectors 在 0v1 处强劲（AUC 0.91-0.94）但 1v2 处近乎 chance level（0.52-0.53），
743	    直接证明 "binary detection ≠ depth estimation"。 这是论文 related work positioning 的关键数据:
744	    existing methods solve a different (easier) problem。 Spearman ρ 的统计显著性反映的是 binary
745	    信号本身（depth=0 vs all），而非 ordinal depth estimation 能力。
746	
747	    '
748	- name: Common Crawl 自然验证
749	  plan_id: exp-014
750	  description: '对 Common Crawl 2025/2026 snapshot 10K 样本做 depth 预测， 与 AlignScore (事实一致性)
751	    和 vocabulary richness 指标做 correlation。 无 ground truth，仅间接验证。
752	
753	    '
754	  expected_results:
755	    spearman_predicted_depth_vs_alignscore: -0.288
756	    spearman_predicted_depth_vs_vocab_richness: -0.342
757	    spearman_p_values:
758	      alignscore: <0.001
759	      vocab_richness: <0.001
760	    pct_samples_predicted_depth_geq_1: 17.5
761	    pct_samples_predicted_depth_geq_2: 6.8
762	    pct_samples_predicted_depth_geq_3: 2.1
763	    predicted_depth_distribution:
764	      depth_0: 82.5
765	      depth_1: 10.7
766	      depth_2: 4.7
767	      depth_3_plus: 2.1
768	  result_rationale: 'Common Crawl 中的真实合成文本比例和代际深度无 ground truth，只能通过与外部质量指标的 correlation
769	    间接验证。 Predicted depth 与 AlignScore 呈负相关（ρ≈-0.29），因为更深代际的文本在递归"电话游戏"中积累了更多事实偏差。
770	    与 vocabulary richness 的负相关更强（ρ≈-0.34），与 C2 degradation ordering 一致: vocabulary
771	    diversity 是最先退化的特征组，predicted depth 高的文本确实词汇更贫乏。 ~17.5% 样本被预测为 depth≥1 与 2025-2026
772	    时期 web 合成文本比例的外部估计（15-25%）一致。 Depth≥2 仅 6.8%——大部分合成文本是"首代"（直接由模型生成），多代递归仍是小众现象。
773	    相关性不高（|ρ|<0.35）是预期中的: wild data 的噪声（domain 多样性、unknown model 族、未知解码策略） 稀释了在 controlled
774	    实验中观察到的信号。这些结果属于 "proof of concept" 级别。
775	
776	    '
777	  tables:
778	  - caption: Common Crawl 自然验证
779	    columns:
780	    - metric
781	    - value
782	    rows:
783	    - - Spearman(pred depth, AlignScore)
784	      - -0.288
785	    - - Spearman(pred depth, vocab richness)
786	      - -0.342
787	    - - '% pred depth ≥ 1'
788	      - 17.5%
789	    - - '% pred depth ≥ 2'
790	      - 6.8%
791	    - - '% pred depth ≥ 3'
792	      - 2.1%
793	  figures_description:
794	  - 'Predicted depth 分布直方图: depth=0 占 82.5%，depth=1 占 10.7%，depth=2+ 占 6.8%。'
795	  - 'Predicted depth vs AlignScore scatter (LOESS smooth): 清晰下降趋势但散点稀疏。'
796	  - 'Predicted depth vs vocabulary richness scatter: 负相关趋势更清晰。'
797	  analysis: '自然验证提供 "proof of concept" 级别的 wild-data 证据。 相关性方向正确且显著，足以支持 appendix
798	    或 discussion section 的 generalizability 论述。 不足以作为 main claim 的证据但有效回应 "只在 controlled
799	    设置下验证" 的审稿人顾虑。 Predicted depth 分布与 web 合成文本比例估计的一致性增加了 classifier 的可信度。
800	
801	    '
802	- name: Learned representation baseline
803	  plan_id: exp-015
804	  description: 'Frozen Qwen2.5-1.5B embeddings (last hidden state, 1536-dim) + 2-layer
805	    MLP vs hand-crafted 15D features + LightGBM。在 Qwen continuation depth chain 上评估。
806	
807	    '
808	  expected_results:
809	    frozen_embeddings_mlp:
810	      auc_1v2: 0.5982
811	      mean_pw_auc: 0.5865
812	      ordinal_accuracy: 0.3708
813	      mae: 1.195
814	      training_time_gpu_hours: 2.6
815	      feature_dim: 1536
816	    handcrafted_15d:
817	      auc_1v2: 0.6112
818	      mean_pw_auc: 0.6048
819	      ordinal_accuracy: 0.3875
820	      mae: 1.155
821	      training_time_gpu_hours: 0.08
822	      feature_dim: 15
823	    gap_auc_1v2_pp: 1.3
824	    gap_mean_pw_auc_pp: 1.83
825	    gap_ordinal_accuracy_pp: 1.67
826	    cross_model_transfer_frozen:
827	      frozen_on_qwen_test_pythia_retention: 0.62
828	      handcrafted_on_qwen_test_pythia_retention: 0.85
829	  result_rationale: 'Frozen embeddings 包含丰富的语义信息但存在三个结构性劣势: (1) 1536 维中绝大部分编码内容语义（topic,
830	    entity, style），而非递归退化信号—— MLP 需要从高维空间中"挖掘"少数相关维度。在 5K 训练样本下，这个搜索问题容易过拟合。 (2) Frozen
831	    embeddings 来自同一模型（Qwen2.5-1.5B），引入自我参照偏差: 模型对自己生成的文本有系统性 embedding 偏向，但这种偏向在 cross-model
832	    设置下不 transfer—— 因此 frozen 的 cross-model retention 仅 62%，远低于 15D 的 85%。 (3) Embedding
833	    空间中的 depth signal 不是线性可分的，2-layer MLP 的容量有限。 Hand-crafted 15D 的优势: 每个特征都直接编码与递归退化相关的统计量（diversity/surprisal/tail
834	    weight）， 人类先验弥补了维度不足。AUC gap 1.30pp < 3pp (best 档要求 < 3pp)。 更关键的是 interpretability
835	    优势: 15D 支持 degradation ordering 分析（exp-005/C2）和 feature group ablation， 这是 frozen
836	    embeddings 无法提供的。论文叙事需要 interpretable features 来讲述 "which linguistic properties
837	    degrade first" 的故事。
838	
839	    '
840	  tables:
841	  - caption: Learned vs hand-crafted features 对比
842	    columns:
843	    - method
844	    - AUC_1v2
845	    - mean_pw_AUC
846	    - ordinal_acc
847	    - MAE
848	    - dim
849	    - GPU_hours
850	    rows:
851	    - - frozen embeddings + MLP
852	      - 0.5982
853	      - 0.5865
854	      - 0.3708
855	      - 1.195
856	      - 1536
857	      - 2.6
858	    - - hand-crafted 15D
859	      - 0.6112
860	      - 0.6048
861	      - 0.3875
862	      - 1.155
863	      - 15
864	      - 0.08
865	  - caption: Cross-model transfer 对比 (train Qwen → test Pythia)
866	    columns:
867	    - method
868	    - in_domain_acc
869	    - cross_model_acc
870	    - retention_pct
871	    rows:
872	    - - frozen embeddings
873	      - 0.3708
874	      - 0.2299
875	      - 62%
876	    - - hand-crafted 15D
877	      - 0.3875
878	      - 0.3294
879	      - 85%
880	  figures_description:
881	  - 'Performance vs interpretability 双轴图: 15D 在 Pareto 前沿（低维高性能），frozen 在高维略低性能区。'
882	  - 'Cross-model transfer retention bar chart: frozen 62% vs 15D 85%，视觉化 interpretable
883	    features 的 generalization 优势。'
884	  analysis: 'AUC gap 1.30pp < 3pp 满足 best 档假设。15D hand-crafted 在所有指标上优于或持平 frozen
885	    embeddings， 且维度低 102 倍、训练快 32.5 倍。 Cross-model transfer 的巨大差距（85% vs 62%）是 decisive
886	    argument: frozen embeddings 过拟合 model-specific embedding space，而 15D 统计特征是 model-agnostic
887	    的。 这验证了论文 "选择 interpretable features 不是方法论妥协而是设计优势" 的叙事， 同时回应审稿人 "为什么不用 learned
888	    representations" 的问题。
889	
890	    '
891	- name: Base vs Instruct 模型对比
892	  plan_id: exp-016
893	  description: 'Qwen2.5-1.5B base model (非 instruct 微调版) continuation mode, C4 5K
894	    docs, depth 0-5。 与 exp-017 (Qwen2.5-1.5B-Instruct continuation) 对比，分离 RLHF/instruction-tuning
895	    对 K* 的影响。
896	
897	    '
898	  expected_results:
899	    base:
900	      k_star: 2
901	      pairwise_auc:
902	        0v1: 0.9958
903	        1v2: 0.6382
904	        2v3: 0.5685
905	        3v4: 0.5358
906	        4v5: 0.5148
907	      pairwise_jsd:
908	        0v1: 0.2952
909	        1v2: 0.0068
910	        2v3: 0.0042
911	        3v4: 0.0032
912	        4v5: 0.0028
913	      ordinal_accuracy: 0.3948
914	      top3_features:
915	      - surp_d1_std
916	      - surp_std
917	      - freq_entropy
918	    instruct_actual:
919	      k_star: 2
920	      pairwise_auc:
921	        0v1: 0.9972
922	        1v2: 0.6114
923	        2v3: 0.5609
924	        3v4: 0.5408
925	        4v5: 0.5139
926	    base_vs_instruct_diff:
927	      delta_auc_1v2: '+0.0268'
928	      delta_auc_2v3: '+0.0076'
929	      delta_jsd_0v1: '+0.0089'
930	    feature_shift:
931	      surprisal_mean_base_vs_instruct: -0.14 std units
932	      vocab_diversity_base_vs_instruct: +0.06 std units
933	  result_rationale: 'RLHF/instruction-tuning 将模型输出拉向 "人类偏好的模式"——更规范的句式、更安全的措辞、更集中的
934	    vocabulary 选择。 这种 alignment 相当于对输出分布施加了额外的低熵约束，使得即使 gen-0→gen-1 的转换也已经部分"标准化"了。
935	    结果: instruct 模型的递归代际间差异更小，因为每代输出都被拉向同一个 "preferred mode"。 Base model 没有这个约束，输出更接近预训练数据的原始分布→递归代际间保留更多分布结构→1v2
936	    AUC 高 2.7pp。 但 K* 仍为 2: alignment 的影响是 quantitative（减弱信号 2.7pp）而非 qualitative（改变收敛行为）。
937	    DPI 的信息论约束在有无 RLHF 的情况下都成立——只要模型是有限容量的 lossy channel。 Surprisal mean 偏移为负（instruct
938	    更"可预测"，反映 RLHF 倾向于生成预期输出）; vocabulary diversity 偏移为正（instruct 词汇稍更多样，反映 RLHF 鼓励的表达丰富性）。
939	    两种偏移方向一致且量级小（< 0.15 std），为 discussion 段落提供数据。
940	
941	    '
942	  tables:
943	  - caption: Base vs Instruct 对比 (Qwen2.5-1.5B, continuation mode)
944	    columns:
945	    - variant
946	    - K*
947	    - AUC_0v1
948	    - AUC_1v2
949	    - AUC_2v3
950	    - JSD_0v1
951	    - ordinal_acc
952	    rows:
953	    - - base
954	      - 2
955	      - 0.9958
956	      - 0.6382
957	      - 0.5685
958	      - 0.2952
959	      - 0.3948
960	    - - instruct (exp-017)
961	      - 2
962	      - 0.9972
963	      - 0.6114
964	      - 0.5609
965	      - 0.2863
966	      - 0.3819
967	    - - Δ (base − instruct)
968	      - 0
969	      - '-0.0014'
970	      - '+0.0268'
971	      - '+0.0076'
972	      - '+0.0089'
973	      - '+0.0129'
974	  figures_description:
975	  - 'Base vs instruct JSD decay 对比: base 曲线在 depth 1-2 段系统性高于 instruct，差距在 depth≥3
976	    后消失。'
977	  - 'Feature distribution violin plots: base vs instruct 在 depth=1 的 surprisal mean
978	    和 vocab diversity 分布差异。'
979	  analysis: 'Base 信号更强但 K* 不变——RLHF alignment 压缩了代际差异但未改变信息论收敛行为。 这对实际应用有关键意义: 野外合成文本可能来自
980	    base 或 instruct 模型， K*=2 在两种设置下一致意味着 graduated filtering 框架对两者都适用。 Base model
981	    1v2 AUC=0.638 的 CI 预期 lower bound ~0.628（远高于 0.60）， 为 Qwen-cont instruct 的 0.0015
982	    margin 脆弱性提供了安全网: 即使 instruct 模型在重复实验中偶尔 CI lower 落到 0.599，base model 的稳健 K*=2
983	    仍支撑 claim。'
984	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f610f2f-212e-4373-ac5c-fd0249557c1a",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "c6a2d46d-f68a-4d08-868b-a02604ee1852",
  "sourceToolAssistantUUID": "5f610f2f-212e-4373-ac5c-fd0249557c1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-13T08:48:40.944Z_

Now let me also read the theory framework and the prior dream review to understand the full picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6a2d46d-f68a-4d08-868b-a02604ee1852",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH93kGfaPFrwRg16GLc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be9c16db-ad41-418e-a9b1-0ce9950f79d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CmaKUYrXsXh3QcRWJbEg8T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37073,
      "cache_read_input_tokens": 48443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37073,
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

_source line 44 · 2026-05-13T08:48:42.877Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AgPYMrm4TjJyegtY8q1Ndk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/report/theory_framework.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be9c16db-ad41-418e-a9b1-0ce9950f79d6",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH93kGfaPFrwRg16GLc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d9f54c3-1282-40ea-ace8-87007f4f7e93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CmaKUYrXsXh3QcRWJbEg8T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37073,
      "cache_read_input_tokens": 48443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37073,
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

_source line 45 · 2026-05-13T08:48:42.889Z_

<details><summary>↩ Tool result · `toolu_01AgPYMrm4TjJyegtY8q1Ndk`</summary>

```text
1	# 信道级联 + DPI 理论框架草案
2	
3	> 将递归生成建模为 iterated lossy channel，用 Data Processing Inequality 约束 depth-discriminability 的 fundamental limit。
4	
5	---
6	
7	## 1. 信道级联模型形式化
8	
9	### 基本设定
10	
11	设 X₀ 为人类撰写的文本（seed text），表示为某概率空间上的随机变量。LLM 的生成过程建模为一个随机信道：
12	
13	$$\mathcal{T}: \mathcal{X} \to \mathcal{X}$$
14	
15	将输入文本映射到输出文本。递归生成形成 Markov chain：
16	
17	$$X_0 \to X_1 \to X_2 \to \cdots \to X_k$$
18	
19	其中 $X_{i+1} = \mathcal{T}(X_i)$，即 depth-$(i+1)$ 的文本由 depth-$i$ 的文本经过一次 LLM 信道产生。
20	
21	**关键假设**：
22	
23	- **(A1) 时不变信道**：同一 LLM + 同一 decoding strategy 在每次迭代中使用相同的信道 $\mathcal{T}$。（prompt-chain 设定下成立；retrain-chain 需放宽为 $\mathcal{T}_i$）
24	- **(A2) Markov 性**：$X_{i+1}$ 仅依赖 $X_i$，不依赖 $X_0, \ldots, X_{i-1}$（prompt-chain 逐段独立生成时成立）
25	- **(A3) 有损信道**：$\mathcal{T}$ 是 non-invertible 的——生成过程丢失关于输入的信息（sampling 引入 noise，decoding 策略截断分布尾部）
26	
27	### 形式化表述
28	
29	$$X_0 \xrightarrow{\mathcal{T}} X_1 \xrightarrow{\mathcal{T}} X_2 \xrightarrow{\mathcal{T}} \cdots \xrightarrow{\mathcal{T}} X_k$$
30	
31	这是一个齐次 Markov chain（在假设 A1 下），其转移核由 LLM 的条件分布 $p_\theta(\cdot | x)$ 决定。
32	
33	---
34	
35	## 2. Data Processing Inequality 约束
36	
37	### DPI 基本形式
38	
39	对于 Markov chain $X_0 \to X_1 \to \cdots \to X_k$，DPI 给出：
40	
41	$$I(X_0; X_k) \leq I(X_0; X_{k-1}) \leq \cdots \leq I(X_0; X_1) \leq H(X_0)$$
42	
43	即 $I(X_0; X_k)$ 关于 $k$ 单调非递增。
44	
45	**直觉**：每经过一次 LLM 信道，关于原始人类文本 $X_0$ 的信息只会减少或不变，绝不增加。递归生成是不可逆的信息丢失过程。
46	
47	### 严格衰减条件
48	
49	当 $\mathcal{T}$ 是 strictly lossy channel（即 $I(X_i; X_{i+1}) < H(X_i)$ for all $i$）时，衰减是严格的：
50	
51	$$I(X_0; X_k) < I(X_0; X_{k-1}) \quad \forall k \geq 1$$
52	
53	这对应于 LLM 生成过程中 sampling noise 不可消除的事实——任何 temperature > 0 或 nucleus/top-k 截断都引入不可逆信息损失。
54	
55	### 与 Depth Discriminability 的联系
56	
57	两个不同深度 $k, k'$ 的文本 $X_k, X_{k'}$ 的可区分性取决于它们的分布差异。定义可区分性度量：
58	
59	$$D(k, k') = d(P_{X_k}, P_{X_{k'}})$$
60	
61	其中 $d$ 是某种分布距离（JSD、MMD、Total Variation 等）。
62	
63	**关键观察**：随着 $k$ 增大，$P_{X_k}$ 趋近于信道 $\mathcal{T}$ 的不动点分布 $P^*$（如果存在），相邻深度的分布差异趋于零：
64	
65	$$D(k, k+1) \to 0 \quad \text{as} \quad k \to \infty$$
66	
67	---
68	
69	## 3. K* 的理论解释
70	
71	### 定义
72	
73	$K^*$ 是 **判别饱和边界（discriminability saturation boundary）**：
74	
75	$$K^* = \max\{k : D(k-1, k) > \epsilon\}$$
76	
77	其中 $\epsilon$ 是 noise floor（对应于有限样本下的统计检验 power limit）。
78	
79	### Information-Theoretic 解释
80	
81	$K^*$ 对应于 $I(X_0; X_k)$ 降至 noise floor 的临界深度：
82	
83	$$K^* \approx \min\{k : I(X_0; X_k) - I(X_0; X_{k+1}) < \delta\}$$
84	
85	其中 $\delta$ 是 MI 增量的可检测下限。
86	
87	**关键 insight**：$K^*$ 不是分类器的能力上限，而是 **information-theoretic impossibility boundary**——任何方法（无论多复杂）都无法区分 depth $> K^*$ 的文本，因为原始人类文本的信息已经被信道噪声完全淹没。
88	
89	### 与 Channel Capacity 的关系
90	
91	信道 $\mathcal{T}$ 的 "contraction rate" $\rho$ 控制 MI 衰减速度：
92	
93	$$I(X_0; X_k) \leq \rho^k \cdot H(X_0) \quad (\text{if exponential decay})$$
94	
95	- $\rho$ 接近 1（低噪声信道，如 greedy decoding）→ 衰减慢，$K^*$ 大
96	- $\rho$ 接近 0（高噪声信道，如 high-temperature sampling）→ 衰减快，$K^*$ 小
97	
98	**但这里有一个反直觉的 nuance**：虽然 high-temperature 使 $\rho$ 更小（信息丢失更快），但它同时保持了更高的 diversity，使相邻深度的分布差异可能更大。因此 $K^*$ 与 decoding strategy 的关系不是简单单调的——这正是需要实验验证的假设。
99	
100	---
101	
102	## 4. Propositions / Theorems 骨架
103	
104	### Proposition 1: MI 单调衰减（DPI 直接推论）
105	
106	**Statement**: 设 $X_0 \to X_1 \to \cdots \to X_k$ 为上述递归生成 Markov chain。则对任意 $k \geq 1$：
107	
108	$$I(X_0; X_k) \leq I(X_0; X_{k-1})$$
109	
110	等号成立当且仅当 $X_{k-1} \to X_k$ 是 sufficient statistic（即信道 $\mathcal{T}$ 是无损的，实际中不成立）。
111	
112	**Proof sketch**:
113	直接由 DPI 定理得出。$X_0 \to X_{k-1} \to X_k$ 构成 Markov chain，DPI 立即给出 $I(X_0; X_k) \leq I(X_0; X_{k-1})$。严格不等号由 $\mathcal{T}$ 的 strictly lossy 性质保证（sampling 引入不可消除的噪声）。$\square$
114	
115	**论文中的作用**：建立理论基础——depth discrimination 必然随深度退化，这不是分类器缺陷，而是信息论必然。
116	
117	---
118	
119	### Proposition 2: 不动点收敛与 K* 有限性
120	
121	**Statement**: 若信道 $\mathcal{T}$ 具有唯一不动点分布 $P^*$（即 $\mathcal{T}(P^*) = P^*$），且 $\mathcal{T}$ 关于某分布度量 $d$ 是 contractive 的（$d(\mathcal{T}(P), \mathcal{T}(Q)) \leq \rho \cdot d(P, Q)$，$0 < \rho < 1$），则：
122	
123	(a) $d(P_{X_k}, P^*) \leq \rho^k \cdot d(P_{X_0}, P^*)$
124	
125	(b) $D(k, k+1) = d(P_{X_k}, P_{X_{k+1}}) \leq (\rho^k + \rho^{k+1}) \cdot d(P_{X_0}, P^*)$
126	
127	(c) 对任意 $\epsilon > 0$，$K^*(\epsilon)$ 有限。
128	
129	**Proof sketch**:
130	(a) 由 contractive mapping theorem 的标准迭代 bound。
131	(b) 三角不等式：$d(P_{X_k}, P_{X_{k+1}}) \leq d(P_{X_k}, P^*) + d(P_{X_{k+1}}, P^*)$，代入 (a) 得结论。
132	(c) $D(k, k+1)$ 以几何速率趋于 0，因此超过 $\epsilon$ 的 $k$ 值数量有限。$\square$
133	
134	**论文中的作用**：证明 $K^*$ 的有限性是理论必然——saturation 不是方法缺陷而是系统属性。同时给出 $K^* = O(\log(d(P_{X_0}, P^*)/\epsilon) / \log(1/\rho))$ 的粗略 scaling。
135	
136	---
137	
138	### Proposition 3: 衰减速率与 Decoding Strategy 的关系（经验驱动假设）
139	
140	**Statement（Conjecture，标注为 empirically motivated）**: 设 $\rho(\tau)$ 为 temperature 为 $\tau$ 时信道 $\mathcal{T}_\tau$ 的 contraction rate。在以下简化假设下（unigram-level，忽略序列结构）：
141	
142	(a) $\rho(\tau)$ 关于 $\tau$ 非单调：存在 $\tau^*$ 使得 $\rho(\tau)$ 在 $\tau < \tau^*$ 时随 $\tau$ 递增，在 $\tau > \tau^*$ 时随 $\tau$ 递减。
143	
144	(b) 直觉：极低 temperature（近 greedy）→ 信道近确定性 → $\rho$ 大但 diversity 低 → MI 本身小。极高 temperature → 信道近均匀随机 → $\rho$ 小 → MI 快速衰减。中间 temperature 平衡两个效应。
145	
146	**Proof sketch**: 此为 conjecture，不提供证明。给出 unigram softmax 信道的显式 contraction rate 计算作为 supporting analysis，实验验证 $K^*(\tau)$ 的非单调性。
147	
148	**论文中的作用**：将 decoding strategy 对 $K^*$ 的影响从 ad hoc 观察提升为 hypothesis-driven 研究。用 AIC/BIC model comparison 区分 exponential vs. polynomial MI 衰减。
149	
150	---
151	
152	## 5. 计算上的 Tractable Proxy
153	
154	### JSD 作为 MI 近似
155	
156	Mutual information 在高维文本空间中不可直接计算。我们采用 Jensen-Shannon Divergence (JSD) 作为 computationally tractable proxy：
157	
158	$$\text{JSD}(P_{X_k} \| P_{X_{k'}}) = \frac{1}{2} D_{\text{KL}}(P_{X_k} \| M) + \frac{1}{2} D_{\text{KL}}(P_{X_{k'}} \| M)$$
159	
160	其中 $M = \frac{1}{2}(P_{X_k} + P_{X_{k'}})$。
161	
162	**在 unigram level 上计算**：将 $P_{X_k}$ 估计为 depth-$k$ 文档集合的 empirical unigram distribution。
163	
164	**局限性（必须在论文中承认）**：
165	- Unigram JSD 忽略序列结构（bigram, trigram, syntactic patterns）
166	- 不等价于真正的 MI——JSD 是 distributional divergence，MI 是 sample-level information quantity
167	- 但 DPI 的定性结论（单调衰减）仍成立，因为 $\text{JSD}(P_{X_k} \| P_{X_0})$ 在 Markov chain 下也满足类似的单调性
168	
169	**补充度量**：
170	- Pairwise classifier AUC 作为 empirical discriminability 的非参数度量
171	- Feature-space Mahalanobis distance 作为多维度的分布距离
172	
173	---
174	
175	## 6. 理论与实验的对接
176	
177	| 理论预测 | 实验验证方法 |
178	|---|---|
179	| $I(X_0; X_k)$ 单调衰减 | JSD$(P_{X_0}, P_{X_k})$ 随 $k$ 递减曲线 |
180	| $K^*$ 有限 | Pairwise AUC 矩阵 + 操作性 K* 定义 |
181	| 衰减速率 $\rho$ 由 decoding strategy 控制 | $K^*(\text{greedy})$ vs. $K^*(p{=}0.95)$ vs. $K^*(T{=}1.2)$ |
182	| Exponential vs. polynomial decay | AIC/BIC model comparison on JSD decay curves |
183	| 不动点 $P^*$ 存在 | 检验 $P_{X_k}$ 对 $k$ 的收敛性（JSD$(P_{X_k}, P_{X_{k+1}}) \to 0$） |
184	
185	---
186	
187	## 7. 与既有理论的关系
188	
189	- **Shumailov et al. (Nature 2024)**：他们的 tail disappearance → diversity loss → mode conflation 三阶段模型对应我们的 $P_{X_k} \to P^*$ 收敛过程中的不同阶段——尾部消失是收敛初期，mode conflation 是收敛后期
190	- **Strong Model Collapse (Dohmatob et al., ICLR 2025)**：他们的 statistical learning theory bound 与我们的 DPI bound 互补——他们关注 retrain-chain 下 generalization error 的增长，我们关注 distributional information 的衰减
191	- **JPEG 重压缩类比**：JPEG 信道也是 contractive mapping（量化步骤不可逆），K* 对应 JPEG recompression detection 的 cycle limit——在图像 forensics 中已被充分研究的问题
192	
193	---
194	
195	## 8. 写作注意事项
196	
197	1. **措辞校准**：Propositions 1-2 是严格的（DPI + contractive mapping 标准结果）；Proposition 3 标注为 "empirically motivated conjecture"，不 overclaim
198	2. **JSD proxy 局限性**：在 Method section 设专段讨论 unigram 近似的局限和 justification
199	3. **信道假设**：A1（时不变）和 A2（Markov）在 prompt-chain 下合理，在 retrain-chain 下需要放宽——在 Discussion 中讨论
200	4. **不做"完整证明"**：论文风格是 proposition + proof sketch + experimental validation，不是纯理论论文的 full proof 风格。重点在 theory-experiment connection
201	5. **Appendix 安排**：完整的 contraction rate 计算、unigram softmax channel 分析放 appendix
202	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d9f54c3-1282-40ea-ace8-87007f4f7e93",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "21eec94e-0748-4186-83d3-cd9ff59b6e29",
  "sourceToolAssistantUUID": "9d9f54c3-1282-40ea-ace8-87007f4f7e93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-13T08:48:43.836Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B3Z7UR9KiLH9fKDLU8s4aR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21eec94e-0748-4186-83d3-cd9ff59b6e29",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH93kGfaPFrwRg16GLc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d44a65df-9248-463c-a90d-fa3017f1a433",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CmaKUYrXsXh3QcRWJbEg8T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37073,
      "cache_read_input_tokens": 48443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37073,
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

_source line 47 · 2026-05-13T08:48:43.845Z_

<details><summary>↩ Tool result · `toolu_01B3Z7UR9KiLH9fKDLU8s4aR`</summary>

```text
1	---
2	dream_id: dream_20260512T200328
3	tier: best
4	overall_score: weak accept
5	timestamp: 2026-05-12T20:15:00Z
6	---
7	
8	# Dream Review Report — best tier
9	
10	**Paper:** K*: Measuring the Generational Discrimination Boundary in Recursive Synthetic Text
11	**Venue:** EMNLP 2026
12	**Headline Assessment:** Weak Accept
13	
14	---
15	
16	## Reviewer 1: Method + Experiments
17	
18	### Strengths
19	
20	1. **Clean problem formulation.** Modeling recursive generation as an iterated lossy channel and grounding K* in the Data Processing Inequality is elegant. The DPI guarantee (Eq. 1) makes the existence of a saturation boundary inevitable, giving the work a principled foundation rather than a purely empirical one.
21	
22	2. **Systematic experimental design.** Three model families (Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B) × multiple decoding strategies × a cross-scale 7B probe. Tables 1–3 build the K* characterization incrementally and convincingly. All three families yield K*=2 under standard decoding with near-identical JSD decay profiles (17–18× drop at 0v1, then 2–3× per subsequent pair).
23	
24	3. **Well-motivated feature design.** The 15D features organized into three complementary groups (vocabulary diversity, surprisal dynamics, tail distribution) are interpretable and grounded in known distributional collapse phenomena. Using the generating model's own surprisal is a smart design choice for a setting where the source model is unknown.
25	
26	4. **Thorough ablation suite.** Classifier architecture (Table 9: CORAL vs ordinal regression vs multinomial), hand-crafted vs learned features (Table 10: 15D outperforms 4096D frozen embeddings while being 270× smaller and 28× faster), LLM zero-shot baseline (Table 11: GPT-4o and Claude 3.5 Sonnet near chance), binary detector comparison (Table 12: DivEye/Binoculars have ρ ≤ 0.23 with depth). Each ablation is well-motivated and answers a specific question.
27	
28	5. **Ecological validity checks.** Retrain-chain vs prompt-chain validation (Table 14: |Δ| ≤ 0.014 across all pairs, both yield K*=2), base vs instruct comparison (both K*=2), and Common Crawl sanity check (predicted depth≥1 proportion of 18.4% aligns with external estimates of 15–25%). These significantly strengthen external validity.
29	
30	6. **Statistical rigor.** 5-fold CV with std reported for discrimination experiments; paired t-test with p-values for downstream evaluation (p=0.008 MMLU, p=0.013 HellaSwag); mean ± std over 3 seeds for continued pretraining.
31	
32	### Weaknesses
33	
34	1. **K* is operationally defined, not information-theoretically fundamental.** Eq. 2 defines K* = max{k : AUC(P_{k-1}, P_k) ≥ θ} with θ=0.60 and a fixed 15D feature set. The paper repeatedly claims K* is "a fundamental, modulable quantity" (Abstract) and "an information-theoretic quantity" (§3.1), but this is overstated. The JSD decay provides circumstantial evidence that an IT boundary exists, but no formal connection is established between θ=0.60 and any information-theoretic threshold. The paper acknowledges this ("While the operational definition...depends on the feature set and threshold θ") but proceeds to make strong IT claims anyway.
35	
36	2. **Seed corpus sensitivity unexamined.** All experiments use 5,000 C4 documents filtered for 128–512 tokens. No analysis is provided on whether K* varies with domain (e.g., scientific text, dialogue, code), length distribution, or corpus size. This is a notable gap given the universality claims.
37	
38	3. **Cross-scale comparison is underpowered.** The 7B probe uses 1,000 documents (vs 5,000 at 1.5B), goes only to depth 3 (vs depth 5), and tests a single model family (Qwen only). The claim K*_7B=3 is plausible but rests on limited evidence.
39	
40	4. **α=0.5 is unjustified.** The gen-1 retention weight in graduated filtering (Eq. 3) is a critical practical parameter but receives no ablation. The downstream results could be sensitive to this choice. A sweep over α ∈ {0.1, 0.3, 0.5, 0.7, 0.9} would be straightforward and highly informative.
41	
42	5. **Absolute classification accuracy is low and partially obscured.** Table 9 reports 0.483 accuracy on 6-class ordinal prediction. The practical 3-class accuracy (human / gen-1 / gen-2+) is never explicitly reported — the reader must infer it from adjacent accuracy (0.821). Since the 3-class signal is the actual practical contribution, this number should be front and center.
43	
44	6. **Cross-model transfer framing is misleading.** Section 5.7 claims "70–79% transfer retention" and "mean transfer retention is 74.6%." But absolute transfer accuracy is 0.35–0.39 (Table 13), with in-domain accuracy only 0.40–0.42. High retention of modest accuracy inflates the practical significance of model-agnostic transfer.
45	
46	7. **Downstream evaluation uses continued pretraining, not training from scratch.** The +2.24 pp MMLU and +2.07 pp HellaSwag improvements (Table 7) are measured on Qwen2.5-1.5B with 30% synthetic injection during continued pretraining. Training from scratch would provide a more definitive test of graduated filtering's value. The dose-response analysis (Table 8) partially compensates by showing monotonic improvement scaling.
47	
48	### Minor Issues
49	- Non-adjacent discrimination (0v2, 0v3) is never reported. These would further validate the ordinal structure.
50	- The choice of exactly 5 features per group appears untested — was this tuned or coincidental?
51	- Confidence intervals for K* itself (across CV folds or bootstrap) would strengthen the main claim.
52	
53	---
54	
55	## Reviewer 2: Novelty + Related Work
56	
57	### Strengths
58	
59	1. **Genuinely novel reframing.** The shift from binary synthetic text detection to ordinal generational depth estimation is a clear conceptual advance. No prior work has systematically asked "how many rounds of recursive generation can we discriminate?" This question is both theoretically natural (given DPI) and practically relevant (for data curation).
60	
61	2. **Elegant theoretical motivation.** The DPI-based argument for K*'s existence is simple and correct: since the recursive generation channel is lossy, mutual information with the human source must decrease monotonically, so at some depth discrimination must fail. This provides a principled upper bound on any depth estimator, not just the proposed one.
62	
63	3. **Effective empirical positioning.** Table 12 concretely demonstrates that DivEye (Spearman ρ=0.23) and Binoculars (ρ=0.19) are poor depth proxies despite excellent 0v1 discrimination (AUC ≥ 0.92). This is the cleanest evidence that binary detection and depth estimation are distinct problems, and it directly motivates the paper's contribution.
64	
65	4. **Actionable concept.** K* provides data curators a concrete answer to "how much depth resolution is useful?" — at current scales, 3 classes suffice. The graduated filtering application (Table 7) demonstrates tangible value, and the dose-response relationship (Table 8) shows the advantage grows with contamination severity.
66	
67	### Weaknesses
68	
69	1. **Related work is thin in several important directions:**
70	   - **Multi-class synthetic text detection:** No discussion of whether any prior work has attempted fine-grained (beyond binary) synthetic text classification.
71	   - **Data selection methods:** DSIR (Xie et al., 2023), D4 (Engstrom et al., 2024), DoReMi (Xie et al., 2024) are relevant baselines for the graduated filtering contribution but are entirely absent. The comparison in Table 7 uses only naive strategies (no filter, binary, surprisal-based).
72	   - **Watermarking-based provenance tracking:** Watermark decay across recursive generations could theoretically track depth. This connection is not discussed.
73	   - **Model collapse literature:** Only Shumailov et al. (2024) and Dohmatob et al. (2024) are cited. Missing key works: Alemohammad et al. (2023) "Self-Consuming Generative Models Go MAD," Bertrand et al. (2024), and Guo et al. (2024) on iterative retraining dynamics.
74	
75	2. **"Fundamental" framing is overclaimed relative to the operational definition.** The paper oscillates between positioning K* as an information-theoretic quantity (§3.1: "we argue it is a fundamental information-theoretic boundary") and acknowledging it is classifier-dependent (§3.1: "the operational definition...depends on the feature set and threshold θ"). A stronger paper would either formally derive θ from the JSD curve or more carefully distinguish the conjectured IT boundary from the measured operational one.
76	
77	3. **Depth estimation vs. depth binning mismatch.** The title and framing promise "Measuring the Generational Discrimination Boundary," but the practical contribution is a coarse 3-class bin (human / gen-1 / gen-2+). K*=2 means fine-grained depth estimation is infeasible beyond depth 2, which is honest but somewhat deflationary given the ambitious framing. The paper would benefit from more explicitly distinguishing the conceptual contribution (K* as a measurable property of the generation channel) from the practical one (3-class filtering suffices).
78	
79	4. **Narrow base for universality claims.** "Universal degradation ordering" (§5.4) is established from three autoregressive transformers trained on English web data with broadly similar architectures (GPT-NeoX family for Pythia, transformer-based for all). Testing across SSMs (Mamba), multilingual models, or significantly different training distributions would strengthen the universality claim. The high Kendall τ=0.84 may partly reflect architectural and data similarity.
80	
81	5. **No adversarial robustness discussion.** If K* informs data curation decisions, adversaries could attempt to produce deeply recursive text that mimics shallow depth signatures. The paper does not discuss this attack surface or potential defenses.
82	
83	### Story Consistency
84	
85	- The abstract's three claims (K*=2 at 1–1.5B, degradation ordering with τ=0.84, +2.24/+2.07 pp downstream gains) are all directly supported by the experimental results.
86	- The three contributions map cleanly to results sections (C1→§5.1–5.3, C2→§5.4, C3→§5.5).
87	- The "best tier" narrative is well-supported: the results are genuinely solid for the claims made.
88	- One minor inconsistency: the conclusion claims "1.5–3.5 pp downstream improvement" but Table 7 shows exactly 2.24 pp (MMLU) and 2.07 pp (HellaSwag) at 30% injection. The 3.5 pp upper bound comes from the 50% injection dose-response (Table 8), which is a different experimental condition. This conflation is slightly misleading in the conclusion.
89	
90	---
91	
92	## Round 2 — Cross-Share Synthesis
93	
94	### R1 on R2's findings:
95	- **Agree on overclaimed IT framing.** The JSD decay profile (Table 1) is consistent with DPI but θ=0.60 is arbitrary relative to any IT quantity. A principled connection — e.g., deriving θ from where JSD drops below a statistical significance threshold — would resolve the tension.
96	- **Missing data selection baselines are a real experimental gap.** DSIR or D4-style distributional matching methods would be a substantially harder baseline for graduated filtering than the naive strategies in Table 7. Without these, the practical contribution is not fully contextualized.
97	- **Narrow model diversity weakens universality.** All three 1–1.5B models are autoregressive transformers trained on similar English web corpora. The high Kendall τ=0.84 may reflect shared architectural inductive biases rather than a universal property of recursive text generation.
98	
99	### R2 on R1's findings:
100	- **Low accuracy is concerning but appropriately contextualized by the 3-class practical contribution.** The paper's actual downstream application uses 3 classes, not 6. However, R1 is correct that explicit 3-class accuracy should be reported — this is a presentation gap that undersells the method's practical utility.
101	- **α ablation is a critical missing experiment.** For graduated filtering to be actionable guidance, practitioners need to know whether the improvement is robust across α values or whether α=0.5 is a lucky choice. This is a simple, low-cost experiment.
102	- **Seed corpus sensitivity and domain transfer are interconnected.** If K* varies across domains, the universality claim weakens, and the practical guidance ("use 3 classes") becomes domain-conditional.
103	
104	---
105	
106	## Round 3 — Convergence
107	
108	Both reviewers converge on **weak accept**. No further rounds needed. Key areas of agreement:
109	
110	- The core contribution (K* concept + systematic measurement) is novel and well-executed
111	- The experimental design is solid within its scope but limited in diversity
112	- The "information-theoretic" framing is overclaimed relative to the operational definition
113	- The practical contribution (graduated filtering) is real but missing key ablations (α) and stronger baselines (data selection methods)
114	- These are addressable revisions, not fatal flaws
115	
116	---
117	
118	## Synthesized Assessment
119	
120	### Headline: Weak Accept
121	
122	### Core Strengths
123	1. **Novel, well-motivated concept.** K* as a saturation boundary for generational depth discrimination is a genuine conceptual contribution that reframes the synthetic text detection problem in a practically useful way.
124	2. **Solid experimental methodology.** Three model families, multiple decoding strategies, cross-scale probe, extensive ablations, ecological validity checks, and appropriate statistical testing.
125	3. **Actionable practical contribution.** Graduated filtering with a coarse 3-class depth signal yields statistically significant downstream improvements, with a dose-response relationship showing increasing value at higher contamination rates.
126	
127	### Core Weaknesses (cross-dimensional)
128	1. **Method × Novelty tension: overclaimed theoretical status.** The paper's strongest narrative claim — that K* is "fundamental" and "information-theoretic" — is not supported by the operational definition (Eq. 2). The concept would stand perfectly well as an empirically measurable, practically useful quantity without the IT overreach. *Severity: moderate — addressable by recalibrating claims.*
129	2. **Experiment × Related Work gap: missing stronger baselines.** The graduated filtering comparison lacks data selection methods (DSIR, D4) that would be natural competitors. Combined with the unjustified α=0.5 choice, the practical contribution's strength is not fully established. *Severity: moderate — requires additional experiments.*
130	3. **Method × Experiments scope limitation: narrow universality basis.** Three architecturally similar English-only transformers at 1–1.5B scale (plus a single 7B probe) are insufficient to support "universal" ordering claims. *Severity: minor-to-moderate — the claims can be softened without damaging the contribution.*
131	
132	### Narrative-Tier Alignment (best tier)
133	The paper is well-positioned for a best-tier dream: the K* concept is clean, the experiments are thorough within scope, and the results support the claims (after the IT framing is recalibrated). The graduated filtering improvement is modest but statistically significant and monotonically increasing with contamination — exactly the kind of result that reviewers find credible. The main risk to acceptance is the combination of overclaimed novelty framing with undertested practical contribution (missing α ablation and data selection baselines).
134	
135	### Recommendations for Revision
136	1. Recalibrate the "information-theoretic" claims — present K* as an operationally defined, empirically robust quantity that is *consistent with* IT bounds, not itself an IT quantity.
137	2. Add α sensitivity ablation for graduated filtering (α ∈ {0.1, 0.3, 0.5, 0.7, 0.9}).
138	3. Include DSIR or D4 as graduated filtering baselines.
139	4. Report explicit 3-class accuracy alongside the 6-class ordinal metrics.
140	5. Soften "universal ordering" language to "consistent ordering across tested architectures."
141	6. Expand related work: add data selection methods, additional model collapse references, and watermarking-based provenance discussion.
142	7. Clarify the conclusion's "1.5–3.5 pp" claim — separate the 30% and 50% injection conditions.
143	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d44a65df-9248-463c-a90d-fa3017f1a433",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "a326a0799fe55d2d5",
  "type": "user",
  "uuid": "75b0936b-ebb3-46ed-a459-39937b9ab263",
  "sourceToolAssistantUUID": "d44a65df-9248-463c-a90d-fa3017f1a433",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-13T08:50:14.776Z_

I now have a comprehensive understanding of the paper, its experimental infrastructure, claims, and the prior review round. Let me now compose the R1 review.

---

## R1 Review: Methods and Experiments

**Paper:** "Generational Depth Contamination: Measuring and Exploiting the Discrimination Boundary of Recursive Synthetic Text"

---

### 1. Summary

This paper formalizes recursive LLM text generation as an iterated lossy channel, invokes DPI to argue for a finite generational discrimination boundary K*, and provides the first systematic empirical measurement of K* across model families, scales, and decoding strategies. The headline finding is K*=2 for 1.5B-scale models under standard nucleus decoding, rising to K*>=3 at 7B scale or high temperature. A secondary contribution shows that even this coarse 3-class ordinal signal enables graduated corpus filtering that significantly outperforms binary approaches on MMLU and HellaSwag.

---

### 2. Strengths

- **Well-structured problem formulation.** The iterated lossy channel model and DPI-based argument for K*'s existence provide a clean conceptual foundation. The distinction between K*_theory and K*_empirical (Section 3.2) is correctly drawn, with the latter positioned as a conservative lower bound.

- **Comprehensive decoding ablation (Table 1).** The greedy-to-high-temperature gradient (K*=1 -> K*=2 -> K*=3) is the paper's most convincing methodological finding. It demonstrates that K* responds to a theoretically motivated control variable (effective decoding entropy), not just to classifier artifacts. The feature ordering consistency (Spearman rho >= 0.878, Table 2) strengthens this by showing that decoding strategy modulates signal strength without altering the degradation structure.

- **Appropriate statistical practice for the K* characterization.** Bootstrap 95% CIs with 10K resamples (Table 4) and permutation tests are used. The paper is transparent that the Qwen-cont instruct CI lower bound is only +0.15pp above theta, which is commendable honesty.

- **Fair graduated filtering design.** The binary-ours baseline (Table 8) isolates the effect of ordinal vs. binary decision boundaries with the same 15D feature set, which is the correct controlled comparison. The inclusion of DSIR and binary-Drayson baselines provides additional context.

- **Ecologically grounded validity checks.** The retrain-chain experiment (Table 6-7), base vs. instruct comparison (Table 5), and cross-model transfer analysis address the most natural objections about experimental generalizability.

- **Hand-crafted features justified empirically, not just narratively.** Table 14 shows 15D features match frozen embeddings on discrimination while achieving 85% vs. 62% cross-model transfer. This makes the feature design a structural advantage rather than a methodological compromise.

---

### 3. Weaknesses

- **The theta=0.60 threshold is not well-justified.** This is the single most consequential design choice in the paper: it directly determines every K* value reported and therefore underlies C1 entirely. The paper provides no principled derivation. An AUC of 0.60 means the classifier correctly ranks a random positive-negative pair only 60% of the time -- barely above chance. A different threshold (e.g., 0.55 or 0.65) would produce different K* values across conditions. The paper should report sensitivity of all K* claims to theta in [0.55, 0.65], which would be straightforward given the existing pairwise AUC data.

- **The gap between DPI theory and empirical K* is wider than acknowledged.** DPI guarantees that I(X; Y_k) is non-increasing, and the theory framework (Proposition 2) shows convergence under contractivity. But the paper's K* is defined via classifier AUC on 15D hand-crafted features, not mutual information. The paper claims K* "captures genuine information-theoretic properties of the recursive channel" (Section 4.1), but this conflates the measured quantity (classifier discriminability on a specific feature set) with the theoretical quantity (information-theoretic impossibility). A stronger approach would be to show that K* is invariant to the choice of feature set (which it likely is not -- the theory framework notes this gap but the paper does not test it beyond the 15D vs. frozen embedding comparison).

- **7B results are statistically fragile.** The K*>=3 claim at 7B rests on a 2v3 CI lower bound of 0.6015 -- exceeding theta=0.60 by 0.15pp. With only 1K documents (vs. 5K for 1.5B), this margin is uncomfortably thin. A single unlucky bootstrap resample could flip the conclusion. The paper should either acknowledge this fragility more prominently or increase sample size. The claim "comfortably above theta" in the narrative guidance does not match the data.

- **Paired t-test with 5 seeds (df=4) for graduated filtering.** The p-values in Table 9 (p=0.0043 MMLU, p=0.0067 HellaSwag) are surprisingly low for a t-test with 4 degrees of freedom, which requires very consistent per-seed differences. With only 5 data points, the t-distribution is heavy-tailed, and the assumption of normally distributed differences is unverifiable. The authors should report individual seed results or consider a non-parametric alternative (Wilcoxon signed-rank, though also limited at n=5). The results would be more convincing with 10+ seeds.

- **Retrain-chain ecological validity is limited by LoRA rank=16.** LoRA rank=16, alpha=32 modifies <0.2% of model parameters per generation -- this is a near-identity perturbation, not full retraining. Real-world recursive contamination involves full pretraining or extensive fine-tuning on web-scraped data, where the model changes substantially between generations. The paper should discuss this limitation: the retrain-chain result validates prompt-chain as a proxy for LoRA-level adaptation, not for full retraining.

- **Common Crawl validation is weak evidence.** Correlations of rho=-0.288 and rho=-0.342 with proxy quality metrics (AlignScore, vocabulary richness) explain <12% of variance. Without ground truth, these correlations could arise from confounds: lower-quality web text (regardless of generational depth) would also correlate with lower AlignScore and vocabulary. The paper correctly labels this as "proof of concept" but still presents it as a main-body result spanning a full table.

- **Domain sensitivity is completely unexamined.** All experiments use C4 (English web text) filtered for 128-512 tokens. K* likely varies across domains (scientific text, dialogue, code, multilingual). No analysis is provided on domain sensitivity, which limits the generalizability of the K*=2 headline result.

- **The 15D feature set was apparently designed with knowledge of the task.** Several features (surprisal statistics, tail distribution measures) are explicitly motivated by known recursive degradation phenomena. While this is reasonable feature engineering, it raises the question: would K* be different with a different feature set? The frozen embedding baseline (Table 14) partially addresses this, but the AUC_1v2 gap is only 1.3pp, suggesting the features matter less than the underlying signal strength. This should be discussed.

---

### 4. Detailed Comments

**DPI framing soundness.** The DPI argument is mathematically correct: for any Markov chain, mutual information is non-increasing under data processing. The application to recursive generation is natural. However, the theory-to-practice gap is substantial. DPI operates on the full joint distribution over text sequences -- an astronomically high-dimensional space. The empirical K* operates on 15D hand-crafted projections of that space. The paper's Proposition 2 (contraction to a fixed point) requires the channel to be contractive in the chosen metric, but contractivity in JSD (or in the 15D feature space) does not follow from DPI alone. The paper should state clearly: "DPI guarantees that *some* K*_theory exists. Our K*_empirical is a lower bound on K*_theory, determined by the discriminative power of our features and threshold."

**Threshold sensitivity (theta=0.60).** Looking at the pairwise AUC data across all tables:
- At theta=0.55: Greedy 1v2 AUC=0.5862 would pass, making K*=2 for greedy. All standard configs would remain K*=2. The T=1.2 condition would likely reach K*=4 (3v4 AUC=0.5614 > 0.55).
- At theta=0.65: Most 1.5B configs would drop to K*=1 (baseline 1v2 AUC=0.6114 still passes, but barely). 7B 2v3=0.6175 barely passes.

This means K* is highly sensitive to theta in the 0.55-0.65 range. A 5pp shift in threshold changes nearly every claim. The paper should present a "K* as a function of theta" figure.

**Sample sizes.** 5K documents for 1.5B is adequate for pairwise AUC estimation (standard errors ~0.01 for AUC at these effect sizes). 1K for 7B introduces substantially higher variance. The 5 seeds for graduated filtering are the minimum for significance testing and leave essentially no room for distributional assumption violations.

**Graduated filtering evaluation.** The evaluation is reasonably convincing within its scope: continued pretraining on Qwen2.5-1.5B with synthetic injection at 30%, evaluated on MMLU and HellaSwag. The inclusion of multiple baselines (no-filter, binary-ours, binary-Drayson, DSIR, surprisal-based) is good. The alpha sweep (Table 10) showing inverted-U is informative. However, the absolute performance levels are low (29.41% MMLU, 47.08% HellaSwag), which is expected for 1.5B models but limits interpretability of the deltas. The dose-response (Table 11) is the most practically relevant result, showing monotonic scaling.

**Retrain-chain realism.** LoRA rank=16 is standard for parameter-efficient fine-tuning but not for the kind of recursive contamination the paper motivates. In the real-world contamination cycle (model trained on web data -> generates text -> text enters web -> new model trained on contaminated web), each "generation" involves training a new model from scratch or significant continued pretraining. The paper's retrain-chain is better understood as validating prompt-chain vs. LoRA adaptation, not prompt-chain vs. realistic contamination cycles.

**Common Crawl.** This analysis would be strengthened by: (1) stratifying by predicted depth and reporting per-stratum quality metrics; (2) comparing against a classifier calibration analysis (what fraction of predicted-depth-1 texts are actually synthetic, per an independent binary detector?); (3) using a held-out set of known-synthetic web text (e.g., GPT-watermarked content) as partial ground truth.

**Feature design and potential leakage.** The surprisal features (5 of 15 dimensions) are computed using the same model family that generated the text. This creates a self-referential signal: the model's surprisal at its own outputs is systematically lower than at human text, and this gap may be model-specific. The cross-model transfer experiment (85% retention) partially addresses this concern, showing the signal is mostly text-intrinsic. However, the 15% retention loss may reflect exactly this self-referential component. The paper should discuss this.

---

### 5. Questions for Authors

1. **Threshold sensitivity.** What are the K* values for all configurations at theta = {0.55, 0.575, 0.625, 0.65}? Is the qualitative story (greedy < standard < high-temp/7B) preserved, or do rankings change?

2. **Graduated filtering at 10% injection.** The dose-response shows a non-significant advantage at 10% (p=0.142 MMLU). Given current estimates of 15-25% synthetic text, this means graduated filtering may not yet provide significant value at the lower end of estimated contamination. Have you tested intermediate injection rates (e.g., 15%, 20%) to identify the transition point more precisely?

3. **Full retraining chain.** Given that LoRA rank=16 modifies <0.2% of parameters, have you considered a full fine-tuning retrain chain (even at small scale, e.g., Pythia-160M) to assess whether the prompt-chain-to-retrain-chain consistency holds under more realistic conditions?

4. **Feature set robustness.** If you remove all 5 surprisal features (eliminating the potential self-referential signal), what happens to K* and the AUC values? Does K* drop to 1 with only the 10 non-surprisal features?

5. **Alpha optimality.** The alpha sweep uses a single injection rate (30%). Does the optimal alpha shift with injection rate? At 50% injection, where gen-1 text constitutes a larger fraction, would a higher alpha be preferred?

---

### 6. Score: 4 (Weak Accept)

The paper introduces a well-motivated concept (K*), provides systematic empirical characterization across a reasonable range of conditions, and demonstrates a modest but statistically significant practical application. The decoding ablation establishing the K* gradient is the strongest methodological contribution. However, the unjustified theta=0.60 threshold, the fragile 7B statistical margin, the limited ecological validity of the retrain-chain, and the thin 5-seed significance testing collectively create a pattern of results that are just barely over the bar on multiple axes simultaneously. The paper would benefit substantially from a theta sensitivity analysis and more seeds for the downstream evaluation. These are addressable revisions that do not undermine the core contribution.

---

### 7. Confidence: 4 (High)

I have substantial familiarity with synthetic text detection, information-theoretic analysis of generative models, and data curation methodology. I have carefully read the full paper including all 15 tables and the theoretical framework. I am less certain about the absolute calibration of my score relative to the EMNLP 2026 acceptance threshold, but confident in my assessment of the methodological strengths and limitations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75b0936b-ebb3-46ed-a459-39937b9ab263",
  "isSidechain": true,
  "agentId": "a326a0799fe55d2d5",
  "requestId": "req_011CazH9XY75J2X1VM2ErhtV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27e2f4e8-22f9-4a71-8f96-95ef9c727f47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019KeLZbzpTyn9s5Z57fWEi3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9573,
      "cache_read_input_tokens": 85516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9573,
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
