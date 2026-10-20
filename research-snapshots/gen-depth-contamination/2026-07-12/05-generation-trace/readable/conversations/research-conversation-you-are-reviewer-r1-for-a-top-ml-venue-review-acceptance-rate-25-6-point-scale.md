# Research conversation: You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a67ad696e7191e92d.jsonl`
- **Structured JSON:** [`5b8ce4ff776e844203ca.json`](../../sessions/5b/5b8ce4ff776e844203ca.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

58 recorded events

### User

_source line 1 · 2026-05-13T08:54:21.638Z_

You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus is **Methods and Experiments**.

## Paper Summary

Title: "Measuring the Generational Discrimination Boundary in Recursively Contaminated Text"

The paper formalizes recursive text generation as an iterated lossy channel, derives from the Data Processing Inequality (DPI) that a finite "generational discrimination boundary" K* must exist, and empirically measures K*=2 under nucleus sampling at the 1.5B scale. They use 15D hand-crafted features (surprisal, lexical diversity, structural) with a LightGBM ordinal classifier. Three claims:
- C1: K*=2 across 4 model configs, stable from 1.5B→7B, sensitive to base/instruct variant
- C2: Cross-model transfer retains 91% accuracy (Pythia↔OLMo); degradation orderings consistent (ρ≥0.82)
- C3: Graduated filtering yields modest +0.6pp at 30% contamination (p=0.08), +1.1pp at 50% (p=0.038); DSIR matches without depth estimation

## Paper Structure (8 pages)
- §1 Introduction: Problem setup, contributions
- §2 Related Work: Model collapse, binary detection, data selection
- §3 Method: DPI theory (§3.1), 15D features (§3.2), K* measurement operationalization with θ=0.60 threshold (§3.3), graduated filtering formula (§3.4)
- §4 Characterization: K* measurement across 4 configs (Table 1), cross-scale 1.5B vs 7B (Table 2), base vs instruct (Table 3), cross-model transfer (§4.2), degradation ordering (§4.3), generation mode analysis (§4.4)
- §5 Application: Filtering comparison at 30% injection (Table 4), α sensitivity (Table 5), dose-response 10/30/50% (Table 6)
- §6 Supporting: Retrain-chain (Table 7), LLM zero-shot (Table 8), binary confidence as proxy (Table 9), learned representations (Table 10), Common Crawl validation (Table 11)
- §7 Conclusion + Limitations

## Key Numerical Results
- Table 1: Pairwise AUC — 0v1 range 0.985-0.996; 1v2 range 0.611-0.696; 2v3 range 0.548-0.565
- Table 2: 7B vs 1.5B: Δ=+1.7pp, p=0.18, non-significant (but 7B uses only 1K docs vs 5K)
- Table 3: Base model AUC_1v2=0.599, CI [.588, .609], below θ=0.60 → K*=1 at this threshold
- Table 4: Graduated 46.1±0.3 MMLU vs Binary(ours) 45.5±0.3, Δ=+0.6pp, p=0.072
- Table 6: Dose-response — graduated−binary: +0.2pp (p=0.32) at 10%, +0.6pp (p=0.08) at 30%, +1.1pp (p=0.038) at 50%
- Table 7: Retrain-chain attenuates signal by -3.3pp on 1v2 but preserves K*=2
- Table 10: Learned features outperform 15D by ~5pp accuracy consistently

## Experiment Design Context (from review_context.yaml)
All 9 imagined experiments are present in the paper:
- exp-004 (7B cross-scale) → Table 2
- exp-006 (downstream filtering) → Tables 4, 5
- exp-008 (retrain-chain) → Table 7
- exp-009 (dose-response) → Table 6
- exp-011 (LLM zero-shot) → Table 8
- exp-012 (binary confidence proxy) → Table 9
- exp-014 (CC validation) → Table 11
- exp-015 (learned representations) → Table 10
- exp-016 (base vs instruct) → Table 3

## Your Task

Produce a structured review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (methods and experimental design)
3. **Weaknesses** (methods and experimental design)
4. **Detailed Comments** — evaluate:
   - Soundness of the DPI-based theoretical framing
   - Appropriateness of the θ=0.60 threshold and K* operationalization
   - Statistical rigor (bootstrap CIs, permutation tests, paired t-tests, seed counts)
   - Feature engineering choices (15D hand-crafted vs learned ~5pp gap)
   - Experimental coverage and controls
   - Retrain-chain ecological validity
   - Downstream filtering evaluation methodology
   - Missing experiments or controls
5. **Questions for Authors** (3-5 specific questions)
6. **Score** (1-6) and **Confidence** (1-5)

Be rigorous but fair. Note where the paper is honest about its limitations vs where it oversells.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "02ea254b-608c-44bf-adb2-db00dd3aaa51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T08:54:21.645Z_

```json
{
  "parentUuid": "02ea254b-608c-44bf-adb2-db00dd3aaa51",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
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
  "uuid": "f1587f33-9132-4932-9c03-6270f875b441",
  "timestamp": "2026-05-13T08:54:21.645Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T08:54:24.080Z_



I'll start by reading the paper and relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1587f33-9132-4932-9c03-6270f875b441",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHaRe6VuPuGfgUXUdhP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa8b7c9d-e795-4ac7-980f-5befcb3625ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UewTcjEWTug3WYXeAeXYC2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15406,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15406,
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

_source line 4 · 2026-05-13T08:54:25.059Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QufaBbTMoQZL1qH4KFkRzy`</summary>

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
  "parentUuid": "aa8b7c9d-e795-4ac7-980f-5befcb3625ca",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHaRe6VuPuGfgUXUdhP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8df0960-181c-4cbb-86a5-d1363291eb8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UewTcjEWTug3WYXeAeXYC2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15406,
      "cache_read_input_tokens": 0,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15406
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15406,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15406,
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

_source line 5 · 2026-05-13T08:54:25.064Z_

<details><summary>↩ Tool result · `toolu_01QufaBbTMoQZL1qH4KFkRzy`</summary>

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
  "parentUuid": "a8df0960-181c-4cbb-86a5-d1363291eb8e",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "04834f8e-aee5-4b52-8fb7-704608465af2",
  "sourceToolAssistantUUID": "a8df0960-181c-4cbb-86a5-d1363291eb8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T08:54:28.254Z_



Let me read the paper and supporting materials to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04834f8e-aee5-4b52-8fb7-704608465af2",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHagKtoe91DfVM9mwRZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68dd1b6a-bc22-428d-822b-75b55895fba0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X3KhEsVruAZMf3xh6SFWTG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15406,
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

_source line 7 · 2026-05-13T08:54:29.305Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016NwbhqECX7Co8ZCgia3n7R`</summary>

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
  "parentUuid": "68dd1b6a-bc22-428d-822b-75b55895fba0",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHagKtoe91DfVM9mwRZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "618fed10-fe1a-4a3c-b163-8aa03d8f4781",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X3KhEsVruAZMf3xh6SFWTG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15406,
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

_source line 8 · 2026-05-13T08:54:29.325Z_

<details><summary>↩ Tool result · `toolu_016NwbhqECX7Co8ZCgia3n7R`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/report.md\", \"content\": \"# Handover — 2026-05-13\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_003_decoding_ablation | 解码策略调控 K*：不同 top_p/temperature 设置是否改变饱和边界（greedy→更低 K*? 高温度→更高 K*?） | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **exp_013_cross_transfer** (success): Depth signal 是文本固有属性还是 model self-familiarity artifact？4×4 cross-model transfer matrix 测试分类器跨模型泛化能力\\n- **exp_005_degradation** (success): —\\n  [exp005_degradation_analysis](autodl-4090d:/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation/degradation_analysis.json)\\n- **exp_007_bootstrap_ci** (success): K* 统计严谨性验证：bootstrap 95% CI 和 permutation test 确认 K*=2 在三个模型族上统计显著\\n\\n## 趋势\\n成功 8 / 负向 0 / 失败 0 / 共 8\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-4090d: 空闲 cuda:0\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 811, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "618fed10-fe1a-4a3c-b163-8aa03d8f4781",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "14321f98-9659-4268-af20-ef8a4572d1d2",
  "sourceToolAssistantUUID": "618fed10-fe1a-4a3c-b163-8aa03d8f4781",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T08:54:29.823Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01UwcPYLP2ZR48yevdZRZunX`</summary>

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
  "parentUuid": "14321f98-9659-4268-af20-ef8a4572d1d2",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHagKtoe91DfVM9mwRZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d79daa80-a64a-4bea-ac53-aaa064f99d7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X3KhEsVruAZMf3xh6SFWTG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15406,
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

_source line 10 · 2026-05-13T08:54:29.885Z_

<details><summary>↩ Tool result · `toolu_01UwcPYLP2ZR48yevdZRZunX`</summary>

```text
{"result":"# 项目 gen-depth-contamination 概况\n\n## 实验状态 (9 个)\n\n- **exp_013_cross_transfer**: DONE (success) — \n- **exp_005_degradation**: DONE (success) — \n- **exp_007_bootstrap_ci**: DONE (success) — \n- **exp_003_decoding_ablation**: RUNNING — \n- **exp_017_qwen_continuation**: DONE (success) — \n- **exp_010_ordinal_baseline**: DONE (success) — \n- **exp_002_olmo_depth**: DONE (success) — \n- **exp_001_pythia_depth**: DONE (success) — \n- **mvp_pilot_sat_v1**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-13\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_003_decoding_ablation | 解码策略调控 K*：不同 top_p/temperature 设置是否改变饱和边界（greedy→更低 K*? 高温度→更高 K*?） | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_013_cross_transfer** (success): Depth signal 是文本固有属性还是 model self-familiarity artifact？4×4 cross-model transfer matrix 测试分类器跨模型泛化能力\n- **exp_005_degradation** (success): —\n  [exp005_degradation_analysis](autodl-4090d:/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation/degradation_analysis.json)\n- **exp_007_bootstrap_ci** (success): K* 统计严谨性验证：bootstrap 95% CI 和 permutation test 确认 K*=2 在三个模型族上统计显著\n\n## 趋势\n成功 8 / 负向 0 / 失败 0 / 共 8\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-4090d: 空闲 cuda:0\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d79daa80-a64a-4bea-ac53-aaa064f99d7c",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "2ac131e3-b916-42e6-b122-bcc093a7d14b",
  "sourceToolAssistantUUID": "d79daa80-a64a-4bea-ac53-aaa064f99d7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T08:54:32.946Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KjoXnmWPxZSEXo6j9BnF35`</summary>

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
  "parentUuid": "2ac131e3-b916-42e6-b122-bcc093a7d14b",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHb393AKzajshJZVhiQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7120d08-b413-48b5-b2dc-ffe9bfa776da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fy7sfMJV1rd1MovYJb3QvU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1528,
      "cache_read_input_tokens": 16853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1528,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 12 · 2026-05-13T08:54:32.957Z_

<details><summary>↩ Tool result · `toolu_01KjoXnmWPxZSEXo6j9BnF35`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/decisions.yaml\", \"content\": \"_next_id: 14\\ndecisions:\\n- id: D001\\n  date: 2026-05-12 10:58 UTC\\n  summary: MVP 方案：Qwen2.5-1.8B + C4 5K docs 做 pilot saturation study，验证代际深度可分辨性\\n  rationale: Phase 0 pilot saturation study 是天然的 MVP gate——如果不同代际深度的文本在特征空间上不可区分，整个项目没有意义。选\\n    Qwen2.5-1.8B 因为体积小、开源、生成速度快。5K docs 足够统计显著性但不浪费 GPU。Pass 标准 K*≥3 对应至少 4 个有意义的类别（human/gen1/gen2/gen3+），AUC>0.70\\n    确保特征有实质区分力。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-12 15:10 UTC\\n  summary: MVP 初步结果 K*=2（边界），修复 right-padding 后重跑确认再锁路线\\n  rationale: AUC(2v3)=0.5797 距阈值 0.60 仅差 0.02，right-padding bug 可能系统性压低 K*。修复成本（1行代码+3h\\n    GPU）远低于错选路线的代价。\\n  related_experiments:\\n  - exp_id: mvp_pilot_sat_v1\\n    role: primary\\n    result: K*=2 (borderline), AUC(0v1)=0.9952, AUC(1v2)=0.6712, AUC(2v3)=0.5797\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-12 19:27 UTC\\n  summary: MVP Conditional Pass, K*=2, 锁定 Route B (Saturation Characterization), 进入\\n    research 阶段\\n  rationale: v3 definitive run 确认 K*=2：AUC(0v1)=0.9956, AUC(1v2)=0.6957, AUC(2v3)=0.5893(<0.60)。JSD\\n    严格单调递减支持 DPI 理论。Depth signal 存在但饱和在 depth 2-3。Route B 将 K* 本身定位为首次测量的基本科学量，比 Route\\n    A（depth classifier 可行性）更 robust——不依赖阈值选择。3-class 系统（human/gen-1/gen-2+）仍比 binary\\n    更有信息量。\\n  related_experiments:\\n  - exp_id: mvp_pilot_sat_v1\\n    role: primary\\n    result: K*=2, AUC(0v1)=0.9956, AUC(1v2)=0.6957, AUC(2v3)=0.5893, JSD monotonic\\n      decay\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-12 20:08 UTC\\n  summary: Reviewer 审查后修正：C1 区分 K*_empirical vs K*_theory；exp-013 (cross-model transfer)\\n    从 P1 提升至 P0\\n  rationale: Reviewer 指出 C1 混淆了经验值和理论值——实测 K*=2 是特定特征+分类器下的 practical boundary，不等于信息论\\n    impossibility boundary。更好的特征/分类器可能推高 K*。修正为\\\"K*_empirical 是 K*_theory 的保守下界\\\"。exp-013\\n    (cross-model transfer, 仅 2h) 直接回答审稿人最危险的攻击面：depth signal 是文本固有属性还是 model self-familiarity？Transfer\\n    失败则 C1 需根本调整。性价比极高，必须 P0。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 00:23 UTC\\n  summary: Dream 分析完成：proceed with P0, 整合 8 项确认行动到 framing/plan\\n  rationale: Dream 三档评分 Best=Weak Accept / Median=Borderline / Worst=Weak Reject。跨三档一致的结构性问题（通用建议）已整合：(1)\\n    IT/fundamental framing 已在 D004 校正，进一步软化 \\\"universal\\\" 措辞; (2) related work 扩展到 4\\n    方向; (3) exp-006 加 DSIR baseline + α ablation + 5 seeds; (4) exp-007 加 bootstrap\\n    CI + permutation-test; (5) exp-015 从 P2 升 P1; (6) 3-class accuracy 显式报告。6 项观察项待真实实验验证：Drayson\\n    et al. 存在性待查、cross-model transfer framing、domain sensitivity、method-code consistency、learned\\n    probe strength、cross-scale probe power。无需 re-dream——确认行动项均为增量调整，不改变 framing 结构。\\n  related_experiments:\\n  - exp_id: exp-006\\n    role: updated\\n    result: 加 DSIR baseline + α ablation + 5 seeds, GPU 48h→72h\\n  - exp_id: exp-007\\n    role: updated\\n    result: 加 bootstrap CI + permutation-test, GPU 1h→2h\\n  - exp_id: exp-015\\n    role: promoted\\n    result: P2→P1\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-13 00:58 UTC\\n  summary: '回滚 Drayson et al. 引用清理——Reviewer 确认为真实论文 (EMNLP 2025 #1506)'\\n  rationale: D005 中基于 web search 无结果将 Drayson et al. (2025) 判定为 Dream 幻觉引用并指示 Agent\\n    清理。Reviewer 独立核实找到 arXiv:2502.15654 + UCL Discovery PDF + GitHub repo，确认为真实发表论文。这是我们最相关的\\n    prior work（binary filtering 防 collapse），我们的 ordinal depth estimation 是其自然推广。教训：单次\\n    web search 不足以判定引用为幻觉，应交叉验证（arXiv ID + 作者机构 + 会议 proceedings）。\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-13 02:06 UTC\\n  summary: Drayson novelty 评估完成：核心 novelty 安全，Story Spine 微调，exp-006 加公平 binary baseline\\n  rationale: Reviewer 独立评估确认：(1) Drayson 做 binary detection 防 collapse（宏观训练动态），我们做\\n    ordinal depth estimation + K* measurement（单样本深度估计）——问题定义层面的扩展，非渐进改进；(2) Drayson\\n    100 代是训练迭代不是文本递归深度，不构成 novelty 威胁；(3) Story Spine 加入 Drayson 作为 closest prior\\n    work 但保持 gap statement 完整；(4) exp-006 加 binary-ours baseline（同 15D 特征做 binary，唯一变量\\n    = binary/ordinal），确保 C3 对比公平。\\n  related_experiments:\\n  - exp_id: exp-006\\n    role: updated\\n    result: 加 binary-ours 公平对比 baseline\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-13 02:45 UTC\\n  summary: C2 claim 暂停写入论文——等 exp-017 解耦 generation mode 因素后决定措辞\\n  rationale: exp-005 结果显示 Kendall τ 仅 Pythia-OLMo 达 0.8476（≥0.8），Pythia-Qwen 0.5238、OLMo-Qwen\\n    0.4857 均不达标。1/3 通过率不支持 C2 当前 \\\"τ≥0.8 across all tested families\\\" 的表述。关键混杂因素：Pythia/OLMo\\n    用 continuation 模式，Qwen 用 rewrite 模式。exp-017（Qwen continuation，~4h 后完成）将区分是 mode-dependent\\n    还是 model-dependent。若 Qwen continuation τ≥0.8 → C2 限定为 \\\"consistent within continuation\\n    mode\\\"；若仍低 → C2 大幅弱化为 \\\"partially consistent\\\" 或限定 base model 范围。\\n  related_experiments:\\n  - exp_id: exp-005\\n    role: evidence\\n    result: partial_consistency_1of3_pairs\\n  - exp_id: exp-017\\n    role: pending_resolution\\n    result: running\\n  depends_on: []\\n- id: D009\\n  date: 2026-05-13 03:35 UTC\\n  summary: C2 战略评估：C1 是承重墙，C3 是安全网，C2 是加分项；exp-016 列为场景 B 应急\\n  rationale: 'Reviewer 深度评估指出第三混杂因素：instruct-tuning。Qwen-Instruct vs Pythia/OLMo base\\n    的差异不仅是 generation mode。exp-017 无法完全解耦 mode 和 instruct-tuning 的联合效应。场景 A (τ≥0.8):\\n    C2 改为 mode-dependent insight (7/10)，可撑 EMNLP Main。场景 B (τ<0.7): C2 降级为 supplementary\\n    finding (3/10)，C1+C3 仍可投 Main/Findings，取决于 C3 效果大小。exp-006 (graduated filtering)\\n    优先级应提升作为 C2 弱化的安全网。exp-016 (Qwen base continuation) 作为场景 B 应急实验预备——可解耦 instruct-tuning\\n    vs architecture 效应，仅 6h GPU。'\\n  related_experiments:\\n  - exp_id: exp-005\\n    role: evidence\\n    result: partial_consistency\\n  - exp_id: exp-017\\n    role: pending_resolution\\n    result: running\\n  - exp_id: exp-006\\n    role: priority_elevated\\n    result: planned\\n  - exp_id: exp-016\\n    role: contingency_scenario_B\\n    result: planned\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-13 06:20 UTC\\n  summary: C2 Plan A 否决 → 执行 Plan B：degradation ordering 限定为 \\\"within architecture\\n    family\\\"，降级为 supplementary finding\\n  rationale: exp-017 (Qwen continuation) 结果明确：控制 generation mode 后，Qwen top feature\\n    仍是 freq_entropy（vs Pythia/OLMo 的 surp_d1_mean）。分歧是 model-dependent 而非 mode-dependent。按\\n    D009 预案，C2 降级为 supplementary finding，措辞改为 \\\"feature degradation ordering consistent\\n    within architecture family (base models τ=0.85), but diverges across architecture\\n    types\\\"。同时发现 generation mode effect 很大（rewrite→continuation AUC 1v2 下降 0.084），论文需增加\\n    mode effect 讨论段。C1 不受影响（4/4 条件 K*=2）。C3 重要性提升为论文第二支柱。\\n  related_experiments:\\n  - exp_id: exp-017\\n    role: decisive_evidence\\n    result: plan_a_rejected\\n  - exp_id: exp-005\\n    role: initial_evidence\\n    result: partial_consistency\\n  depends_on:\\n  - D008\\n  - D009\\n- id: D011\\n  date: 2026-05-13 06:24 UTC\\n  summary: D010 修正：C2 从 \\\"supplementary\\\" 升级为 \\\"qualified claim\\\"——使用 single-feature AUC\\n    + Spearman ρ≥0.85 + mode-controlled 条件\\n  rationale: 'Reviewer 4-model 降解分析修正了此前结论。LightGBM split count 和 single-feature AUC\\n    给出矛盾排名：split count 显示 Qwen-cont freq_entropy #1（与 Pythia/OLMo 分歧），但 single-feature\\n    AUC 显示 Qwen-cont top-3 与 Pythia/OLMo 完全一致（surp_d1_std, surp_std, surp_d2_std）。Single-feature\\n    AUC 更直接衡量代际区分力，更适合 C2 语义。Spearman ρ: Pythia-OLMo=0.95, Pythia-Qwen_cont=0.9143,\\n    OLMo-Qwen_cont=0.85——全部≥0.85。C2 可行路径：(1) 用 single-feature AUC ranking 定义 ordering；(2)\\n    用 Spearman ρ≥0.85 作为一致性阈值；(3) 限定 mode-controlled 条件；(4) 透明报告 depth-pair level\\n    差异（1v2 对 τ 仅 0.35-0.39）和 τ vs ρ 选择理由。风险：depth-pair 1v2 一致性差（τ~0.37），审稿人可能做 depth-stratified\\n    分析。'\\n  related_experiments:\\n  - exp_id: exp-005\\n    role: 4model_reanalysis\\n    result: rho_ge_0.85_all_pairs\\n  - exp_id: exp-017\\n    role: mode_control\\n    result: convergence_confirmed\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-13 07:29 UTC\\n  summary: 论文 claim 重构：4 claims → 2+1 结构（C1' K* characterization + C3 graduated filtering\\n    + supporting analysis）\\n  rationale: Reviewer 评估指出 4 claims (C1/C2/C3/C4) 对 EMNLP Main 太散，每个不够厚。重构为：Primary\\n    C1' = 首次系统测量 K*_empirical（含 DPI 理论 + 4-model 验证 + cross-model transfer + degradation\\n    ordering + generation mode analysis）；Secondary C3 = graduated filtering > binary；Supporting\\n    = generation mode effect + metric analysis 作为 §4.4 subsection。C4 从独立 claim 降级为方法论洞见（Canonical\\n    Condition Selection），C2 ordering 融入 C1' characterization。Canonical condition framing：continuation\\n    mode 作为 cross-model 基础，MVP rewrite 定位为 pilot study。exp-006 是关键路径：exp-003 完成后立即启动，72h\\n    GPU，deadline 05-25 ARR 倒推无延迟容忍。\\n  related_experiments:\\n  - exp_id: exp-013\\n    role: evidence_for_restructure\\n    result: mode_effect_is_methodological\\n  - exp_id: exp-006\\n    role: critical_path\\n    result: planned\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-13 07:37 UTC\\n  summary: C3 exp-006 单点依赖风险评估 + fallback story 预案\\n  rationale: Reviewer 正确指出 C3 (graduated filtering) 完全依赖 exp-006 单个实验。Fallback 预案：(1)\\n    如果 graduated 显著优于 binary → C3 成立，2+1 claim 结构完整；(2) 如果 graduated ≈ binary（无统计显著差异）→\\n    C3 改为 informative negative：\\\"K*=2 的粗粒度 ordinal signal 不足以在 downstream 层面超越 binary\\\"，论文\\n    story 调整为纯 characterization paper（C1' 独立支撑），graduated filtering 作为 negative result\\n    讨论（对论文质量有加分，EMNLP 重视 negative findings）；(3) 如果 graduated 比 binary 差 → 同场景 2，额外分析原因（3-class\\n    ordinal noise vs binary robustness）。场景 1 是预期结果（K* 附近 ordinal signal 提供更 calibrated\\n    的质量估计），但场景 2 也不致命——C1' 本身有足够深度（K* characterization + degradation ordering + mode\\n    effect + cross-model transfer）。关键行动：exp-003 完成后 GPU 零间隔切换 exp-006，不容任何空转。\\n  related_experiments:\\n  - exp_id: exp-006\\n    role: target\\n    result: planned\\n  - exp_id: exp-003\\n    role: predecessor\\n    result: running\\n  depends_on:\\n  - D012\\n\", \"total_chars\": 9371, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7120d08-b413-48b5-b2dc-ffe9bfa776da",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "e068deaa-3889-447c-8cd0-7d9ca36940b8",
  "sourceToolAssistantUUID": "e7120d08-b413-48b5-b2dc-ffe9bfa776da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T08:54:33.883Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NMfcB4CW1162vqyU3agK6V`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "paper_provenance.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e068deaa-3889-447c-8cd0-7d9ca36940b8",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHb393AKzajshJZVhiQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a50d030-875e-41af-8dba-c81674ce5ca9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fy7sfMJV1rd1MovYJb3QvU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1528,
      "cache_read_input_tokens": 16853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1528,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 14 · 2026-05-13T08:54:33.893Z_

<details><summary>↩ Tool result · `toolu_01NMfcB4CW1162vqyU3agK6V`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_provenance.yaml found for 'gen-depth-contamination'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a50d030-875e-41af-8dba-c81674ce5ca9",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "5b39c077-4118-4b76-a375-d46284099662",
  "sourceToolAssistantUUID": "7a50d030-875e-41af-8dba-c81674ce5ca9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T08:54:34.335Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VHbWxc3kzyz4FSC2Ue7ysZ`</summary>

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
  "parentUuid": "5b39c077-4118-4b76-a375-d46284099662",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHb393AKzajshJZVhiQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5991958-a452-4ad8-b177-227d27864cc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fy7sfMJV1rd1MovYJb3QvU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1528,
      "cache_read_input_tokens": 16853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1528,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 16 · 2026-05-13T08:54:34.345Z_

<details><summary>↩ Tool result · `toolu_01VHbWxc3kzyz4FSC2Ue7ysZ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'gen-depth-contamination'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5991958-a452-4ad8-b177-227d27864cc6",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "f393f0fc-4161-495f-b595-3e41b0da2276",
  "sourceToolAssistantUUID": "c5991958-a452-4ad8-b177-227d27864cc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T08:54:37.969Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NpFgHbYnMBPKa3zdku3fxf`</summary>

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
  "parentUuid": "f393f0fc-4161-495f-b595-3e41b0da2276",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHbNMS6tretBA4zbS7n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b7a6439-a5db-4026-97f0-df29d089ce21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0181P7MdEtJhs5pM4sJNs7PP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5563,
      "cache_read_input_tokens": 18381,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5563,
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

_source line 18 · 2026-05-13T08:54:37.986Z_

<details><summary>↩ Tool result · `toolu_01NpFgHbYnMBPKa3zdku3fxf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md\", \"content\": \"# Paper Framing — gen-depth-contamination\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\\n- Fallback: EMNLP 2026 Findings\\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\\n\\n## Canonical Experimental Condition\\n\\n**Continuation mode 是 cross-model 结论的基础。**\\n\\n> \\\"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\\\"\\n\\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\\n|-----------|-------------|-------------|---------|\\n| Continuation | 91-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\\n\\n**原则**：\\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\\n- mvp-001 (Qwen-rewrite) 定位为 \\\"pilot study demonstrating feasibility\\\"，后续用 continuation mode rigorously validate\\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\\n\\n## Core Claims (2+1 结构, D012)\\n\\n### Primary: C1' (K* Characterization)\\n首次系统测量递归合成文本的 generational discrimination boundary K*。\\n\\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 4-model × 2-mode 实验矩阵系统表征 K*_empirical 的行为，包括跨模型一致性、特征退化排序、以及 generation mode 对 depth signal 的调控效应。\\n\\n**子组件：**\\n\\n**(a) K* = 2 across all tested configurations**\\n> 4-model 1v2 bootstrap 95% CI 汇总：\\n> | Model | AUC 1v2 | 95% CI | CI lower > 0.60? |\\n> |-------|---------|--------|-----------------|\\n> | Qwen-rewrite | 0.6955 | [0.6859, 0.7041] | ✅ (+8.6pp) |\\n> | Pythia-1.4B | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\\n> | OLMo-1B | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\\n> | Qwen-cont | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp, 最边缘) |\\n>\\n> - 全部 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60, 全部 permutation p < 0.002\\n> - K* 不是离散跳变值，而是 CI-bounded continuum threshold\\n> - Paper 可写：\\\"K*=2 (bootstrap 95% CI for AUC₁ᵥ₂ > 0.60 across all four model configurations; AUC₂ᵥ₃ CI upper < 0.60)\\\"\\n\\n**(b) Cross-model transfer**\\n> - Pythia↔OLMo 91% accuracy retention → K*=2 不是 model self-familiarity artifact\\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\\n> - 1v2+ transfer 取决于模型族相似度 → 与 K*=2 完美一致（K* 之上分辨力本就微弱）\\n> - depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity\\n\\n**(c) Degradation ordering consistency**\\n> - Spearman ρ ≥ 0.85 on single-feature AUC ranking（mode-controlled, continuation）\\n> - Top discriminative features shared: surp_d1_std, surp_std, surp_d2_std\\n> - Limitation: depth-pair level 一致性在 1v2 处较弱（τ~0.37）\\n> - Metric: single-feature AUC ranking（model-free, not LightGBM split count）\\n\\n**(d) Generation mode analysis (§4.x Analysis subsection)**\\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\\n> - 论文定位：Analysis subsection（\\\"How does generation mode affect depth estimation?\\\"），不是独立 claim\\n\\n### Secondary: C3 (Graduated Filtering)\\n即使在 K*=2 的粗粒度 ordinal signal（human/gen-1/gen-2+ 三级）下，K*-aware graduated filtering 仍优于 binary filtering，因为 ordinal signal 在阈值附近提供更 calibrated 的质量估计。\\n\\n### Supporting Analysis: Canonical Condition Selection\\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\\n\\n## Story Spine\\n\\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\\\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\\\"。通过 4-model × 2-mode 实验矩阵系统表征 K*，揭示控制因素（模型架构、解码策略、generation mode），为数据治理提供 actionable guidance。\\n- **Headline result template**: \\\"We establish K*=2 as the generational discrimination boundary for 1.5B-scale models under standard decoding, with depth features that are 70-85% text-intrinsic (Pythia↔OLMo 91% transfer retention). Even this coarse 3-class signal yields X% improvement over binary filtering on MMLU/HellaSwag.\\\"\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n1. **\\\"K*=2 太浅，graduated filtering 收益有限\\\"** → K* 是模型/解码策略依赖的；展示不同解码策略如何调控 K*（exp-003）；即使 K*=2，3-class 比 binary 在阈值附近更 calibrated（exp-006）\\n2. **\\\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\\\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ generation mode analysis，不是分类器本身\\n3. **\\\"Prompt-chain 不代表真实世界递归污染\\\"** → retrain-chain ecological validity check 作为补充；prompt-chain 是 controlled experiment 的标准方法\\n4. **\\\"单模型/单数据集，泛化性不够\\\"** → 3 个模型族 × 2 种 generation mode + 4×4 cross-model transfer matrix\\n5. **\\\"同模型做生成和 surprisal 计算有 bias\\\"** → **exp-013 直接反驳**：Pythia↔OLMo 91% accuracy retention，0v1 transfer AUC > 0.96。Depth signal 主要编码在文本而非 model self-familiarity\\n6. **\\\"为什么不用 learned representations\\\"** → 作为 baseline 对比；hand-crafted features 更 interpretable 且支持 degradation ordering 分析\\n7. **\\\"Graduated filtering 没和 data selection methods 比\\\"** → exp-006 包含 DSIR baseline + α sensitivity sweep\\n8. **\\\"K* 的统计不确定性未量化\\\"** → 4-model bootstrap CI + permutation test（exp-007）\\n\\n## Venue Fit\\n\\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\\n- 2+1 claim 结构：C1' 是 comprehensive characterization study，C3 是 practical application，generation mode analysis 增加深度\\n- 风险：如果审稿人偏 methods，K*=2 + standard classifier 可能被认为贡献不足 → 强调 problem formulation + characterization + transfer analysis 的 novelty\\n\", \"total_chars\": 6221, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b7a6439-a5db-4026-97f0-df29d089ce21",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "a2ed79b0-0a62-40cc-982f-248ac5426e70",
  "sourceToolAssistantUUID": "1b7a6439-a5db-4026-97f0-df29d089ce21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T08:54:38.883Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UN5vDxWGd2c6bMwgzzaczC`</summary>

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
  "parentUuid": "a2ed79b0-0a62-40cc-982f-248ac5426e70",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHbNMS6tretBA4zbS7n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41d7e4be-bd68-40aa-9911-f37b9f90a0ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0181P7MdEtJhs5pM4sJNs7PP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5563,
      "cache_read_input_tokens": 18381,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5563,
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

_source line 20 · 2026-05-13T08:54:38.895Z_

<details><summary>↩ Tool result · `toolu_01UN5vDxWGd2c6bMwgzzaczC`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'gen-depth-contamination'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41d7e4be-bd68-40aa-9911-f37b9f90a0ba",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "9a5cbf55-a5b1-482a-9cb2-b4b2fdd99109",
  "sourceToolAssistantUUID": "41d7e4be-bd68-40aa-9911-f37b9f90a0ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T08:54:39.239Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Rk8aAEy86KRRPFNZ6SPhXQ`</summary>

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
  "parentUuid": "9a5cbf55-a5b1-482a-9cb2-b4b2fdd99109",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHbNMS6tretBA4zbS7n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2464e699-312e-435b-9b4e-eafc30c95f2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0181P7MdEtJhs5pM4sJNs7PP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5563,
      "cache_read_input_tokens": 18381,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5563
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 295,
          "cache_read_input_tokens": 18381,
          "cache_creation_input_tokens": 5563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5563,
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

_source line 22 · 2026-05-13T08:54:39.252Z_

<details><summary>↩ Tool result · `toolu_01Rk8aAEy86KRRPFNZ6SPhXQ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'gen-depth-contamination'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2464e699-312e-435b-9b4e-eafc30c95f2e",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "80715ee8-c430-44eb-a105-2cdd693e9212",
  "sourceToolAssistantUUID": "2464e699-312e-435b-9b4e-eafc30c95f2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T08:54:42.086Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YBMTKGnCjM3mBgeQphztb5`</summary>

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
  "parentUuid": "80715ee8-c430-44eb-a105-2cdd693e9212",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHbj86TyqasBEHvaAqh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1b119a6-2b7d-442f-be5e-b4518ef650a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WBRW1WXCm3LWU3pvwMD1eX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3556,
      "cache_read_input_tokens": 23944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3556,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 24 · 2026-05-13T08:54:42.094Z_

<details><summary>↩ Tool result · `toolu_01YBMTKGnCjM3mBgeQphztb5`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'gen-depth-contamination'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1b119a6-2b7d-442f-be5e-b4518ef650a9",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "aeafdbef-2f42-4eec-83c9-6f43a5f9f67b",
  "sourceToolAssistantUUID": "d1b119a6-2b7d-442f-be5e-b4518ef650a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T08:54:42.662Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018e5631B5bd7QYPm7F2p5Kc`</summary>

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
  "parentUuid": "aeafdbef-2f42-4eec-83c9-6f43a5f9f67b",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHbj86TyqasBEHvaAqh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b148c92d-3e88-4be7-9fb8-b708e308748a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WBRW1WXCm3LWU3pvwMD1eX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3556,
      "cache_read_input_tokens": 23944,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3556
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 23944,
          "cache_creation_input_tokens": 3556,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3556,
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

_source line 26 · 2026-05-13T08:54:42.671Z_

<details><summary>↩ Tool result · `toolu_018e5631B5bd7QYPm7F2p5Kc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/memory.md\", \"content\": \"# Memory — gen-depth-contamination\\n\\n## 已知问题\\n\\n### right-padding (2026-05-12)\\nMVP pipeline 使用 right-padding（transformers 默认）。Director 确认对 MVP 判定无影响（所有 depth 一致受影响），不中断当前实验。**full study 阶段必须修复为 `tokenizer.padding_side = \\\"left\\\"`**，否则 batch 生成时 padding tokens 会影响生成质量的绝对水平。\\n\\n## GPU 优化建议 (2026-05-12)\\n\\n### batch size 调优\\n4090D 24GB 跑 1.5B fp16 模型仅用 3.9GB 显存 (16%)，GPU 利用率 45%。\\n- Step 3 生成：batch_size 16→**64**（保守）或 128\\n- Step 4 特征提取：feat_batch_size 8→**24**（保守）或 32\\n- 预估节省 ~74 min (38%)，加 flash-attn 可再省 10-15%\\n- full study 时一并修复\\n\\n## AutoDL 环境经验\\n\\n### C4 数据集加载 (2026-05-12)\\nAutoDL 代理下 `load_dataset(\\\"allenai/c4\\\", \\\"en\\\", streaming=True)` 会触发全量文件树解析（数千个 shard 的分页 API 请求），ProxyError 无限重试。修复：用单 shard URL 直接加载 + `HF_ENDPOINT=https://hf-mirror.com` 中转。\\n\\n### 环境变量必须固化到启动脚本 (2026-05-12)\\nAutoDL 上 `source /etc/network_turbo`、SSL 证书、HF 配置等环境变量不能只在 shell session 里 export，必须写入 `run_mvp.sh` 等包装脚本，否则 tmux session 里不生效。\\n\\n### submit_training_job pid=\\\"unknown\\\" 问题 (2026-05-13)\\nsubmit_training_job 有时返回 pid=\\\"unknown\\\"，导致 registry 状态停在 PREPARING、cron 未创建。exp-017 和 exp-003 都遇到此问题。**解决方式**：提交后必须派 Worker SSH 检查实际进程状态（tmux ls + ps aux），手动修正 registry 并注册 cron。\\n\\n## 实验设计决策\\n\\n### Generation mode 影响 depth signal 强度 (2026-05-13)\\nRewrite mode（instruction prompting）比 continuation mode 多产生 ~8.4pp AUC 差距（Qwen: 0.6957 vs 0.6114）。原因推测：instruction-following 引入更大的分布偏移，放大 depth-discriminative 信号。论文中 K* 应同时报告两种 mode 的结果；C1 robustness 依赖 continuation mode（更保守的 lower bound）。\\n\\n### Degradation ordering mode-dependent (2026-05-13)\\n4-model τ 矩阵表明 generation mode 贡献 ~60-70% 的排序偏离，架构 ~30-40%。C2 claim 不能说 \\\"universal ordering\\\"，应改为 \\\"mode-conditioned consistency with architecture residuals\\\"。Director 决策 D008 的后续：4-model τ 数据已齐全，等 Director 确认 C2 最终措辞。\\n\", \"total_chars\": 1706, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b148c92d-3e88-4be7-9fb8-b708e308748a",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "58409aff-696d-409d-b9e5-e7c160acc905",
  "sourceToolAssistantUUID": "b148c92d-3e88-4be7-9fb8-b708e308748a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-13T08:54:45.361Z_

Now let me find and read the actual paper draft.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58409aff-696d-409d-b9e5-e7c160acc905",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHbzjwsLjUCQ11PeFi3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15e0ae00-8a4d-4687-9a88-193ea953a783",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XREWxsbuZ2inmn32C8TBXY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1431,
      "cache_read_input_tokens": 27500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1431,
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

_source line 28 · 2026-05-13T08:54:46.401Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014MUEDjN3iS77aWAiQKc6n3`</summary>

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
  "parentUuid": "15e0ae00-8a4d-4687-9a88-193ea953a783",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHbzjwsLjUCQ11PeFi3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebe61ad3-3167-4c55-b5d9-2eaee7496681",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XREWxsbuZ2inmn32C8TBXY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1431,
      "cache_read_input_tokens": 27500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1431,
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

_source line 29 · 2026-05-13T08:54:46.423Z_

<details><summary>↩ Tool result · `toolu_014MUEDjN3iS77aWAiQKc6n3`</summary>

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
  "parentUuid": "ebe61ad3-3167-4c55-b5d9-2eaee7496681",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "fbbd46ca-298e-416c-93e2-1a8ceedf7c02",
  "sourceToolAssistantUUID": "ebe61ad3-3167-4c55-b5d9-2eaee7496681",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-13T08:54:46.508Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01L1wRTFT8xZ5fW6qNkt97EQ`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbbd46ca-298e-416c-93e2-1a8ceedf7c02",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHbzjwsLjUCQ11PeFi3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "377fd5d6-f564-420a-b062-fdee07046f8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XREWxsbuZ2inmn32C8TBXY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1431,
      "cache_read_input_tokens": 27500,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1431
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 27500,
          "cache_creation_input_tokens": 1431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1431,
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

_source line 31 · 2026-05-13T08:54:46.519Z_

<details><summary>↩ Tool result · `toolu_01L1wRTFT8xZ5fW6qNkt97EQ`</summary>

```text
artifacts/dream_reports/dream_20260512T200328/best/paper.pdf
artifacts/dream_reports/dream_20260512T200328/median/paper.pdf
artifacts/dream_reports/dream_20260512T200328/worst/paper.pdf
artifacts/_project/chart/auc_heatmap.pdf
artifacts/figures/auc_heatmap.pdf
artifacts/_project/chart/feature_importance.pdf
artifacts/figures/feature_importance.pdf
artifacts/_project/chart/jsd_decay.pdf
artifacts/figures/jsd_decay.pdf
artifacts/dream_reports/dream_20260513T080728/best/paper.pdf
artifacts/dream_reports/dream_20260513T080728/median/paper.pdf
artifacts/dream_reports/dream_20260513T080728/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "377fd5d6-f564-420a-b062-fdee07046f8a",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "d8aef5d0-84cb-4118-a32e-c207db2f87c4",
  "sourceToolAssistantUUID": "377fd5d6-f564-420a-b062-fdee07046f8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-13T08:54:49.699Z_

Let me read the latest dream report paper (the median version, as it likely represents the expected review outcome).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8aef5d0-84cb-4118-a32e-c207db2f87c4",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHcGEcR9Jbk5Z1YCcTX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e80e8c0-a70e-4eb2-986a-d9d0ff707a5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jr6yuFWxcmLxF698SURe3i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 576,
      "cache_read_input_tokens": 28931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 576,
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

_source line 33 · 2026-05-13T08:54:50.340Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AbjRbU3cZNchVmsrJ5p97L`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260513T080728/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e80e8c0-a70e-4eb2-986a-d9d0ff707a5a",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHcGEcR9Jbk5Z1YCcTX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94412fd5-8aac-4fd6-97ab-ff6c06c2ee76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jr6yuFWxcmLxF698SURe3i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 576,
      "cache_read_input_tokens": 28931,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 576
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 28931,
          "cache_creation_input_tokens": 576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 576,
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

_source line 34 · 2026-05-13T08:54:50.664Z_

<details><summary>↩ Tool result · `toolu_01AbjRbU3cZNchVmsrJ5p97L`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{xcolor}
9	\usepackage{enumitem}
10	\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}
11	\usepackage{natbib}
12	
13	\newcommand{\Kstar}{K^{*}}
14	\newcommand{\AUC}{\mathrm{AUC}}
15	
16	\title{Measuring the Generational Discrimination Boundary\\in Recursively Contaminated Text}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	% ==============================================================================
24	\begin{abstract}
25	Web-scale training corpora are increasingly contaminated by recursively generated synthetic text, yet current detection methods treat synthetic content as a binary category, ignoring the nonlinear quality degradation across generational depth.
26	We formalize recursive generation as an iterated lossy channel and derive from the Data Processing Inequality (DPI) that a finite generational discrimination boundary $\Kstar$ must exist---the maximum depth at which adjacent generations remain statistically distinguishable.
27	Through controlled experiments spanning three model families, two generation modes, and cross-model transfer evaluation, we establish $\Kstar=2$ under standard nucleus sampling at the 1.5B parameter scale: human text is readily separable from first-generation synthetic text (pairwise AUC $>0.97$), first- from second-generation text is distinguishable (AUC $\approx 0.61\text{--}0.70$), but second- from third-generation text is not (AUC $<0.56$).
28	Cross-model transfer experiments show 91\% accuracy retention between model families, indicating that depth signal is predominantly text-intrinsic.
29	We further demonstrate that $\Kstar$-aware graduated filtering provides modest but consistent improvement over binary filtering for downstream training (up to $+1.1$ percentage points on MMLU at 50\% contamination), though general-purpose data selection methods achieve comparable results, suggesting the primary value of depth measurement lies in scientific characterization.
30	\end{abstract}
31	
32	% ==============================================================================
33	\section{Introduction}
34	\label{sec:intro}
35	
36	The proliferation of large language models (LLMs) has led to an accelerating feedback loop: models generate text that enters web corpora, which in turn train future models.
37	This \emph{recursive contamination} degrades training data quality in ways that binary human-vs-machine detection cannot capture---a first-generation synthetic document may be nearly indistinguishable from human writing in quality, while a fourth-generation document exhibits measurable distributional collapse \cite{shumailov2024collapse}.
38	
39	Existing approaches address fragments of this problem.
40	Binary detectors such as DivEye and Binoculars classify text as real or synthetic but do not estimate generational depth.
41	Model collapse literature describes macroscopic degradation phenomena but does not provide detection tools.
42	Data selection methods (DSIR, D4, DoReMi) perform distribution matching without explicit depth awareness.
43	Drayson et al.\ (2025) apply binary detection confidence for importance resampling to mitigate model collapse, representing the closest prior work---yet they too make binary judgments.
44	
45	We argue that the core missing quantity is the \textbf{generational discrimination boundary} $\Kstar$: the maximum depth $k$ at which generation $k$ and generation $k+1$ remain statistically distinguishable.
46	From an information-theoretic perspective, recursive generation constitutes an iterated lossy channel; the Data Processing Inequality guarantees that a finite $\Kstar$ must exist.
47	We provide the first systematic empirical measurement of $\Kstar$.
48	
49	Our contributions are:
50	\begin{enumerate}[nosep,leftmargin=1.5em]
51	    \item \textbf{Characterization of $\Kstar$.} We establish $\Kstar=2$ under standard nucleus sampling at the 1.5B scale across four model configurations, with bootstrap confidence intervals and permutation tests. We show that $\Kstar$ is stable from 1.5B to 7B ($\Delta\mathrm{AUC}_{1v2}=+1.7$pp, $p=0.18$) but sensitive to model variant (base models yield borderline $\Kstar$ at the $\theta=0.60$ threshold). We validate with retrain-chain experiments confirming ecological validity.
52	    \item \textbf{Cross-model transfer and degradation ordering.} Pythia$\leftrightarrow$OLMo transfer retains 91\% accuracy, demonstrating that depth signal is 70--85\% text-intrinsic. Feature degradation orderings are consistent across models (Spearman $\rho \geq 0.82$).
53	    \item \textbf{Graduated filtering application.} $\Kstar$-aware graduated filtering yields modest improvement over binary filtering ($+0.6$pp at 30\% contamination, $p=0.08$; $+1.1$pp at 50\%, $p=0.038$), though DSIR achieves comparable performance without explicit depth estimation.
54	\end{enumerate}
55	
56	% ==============================================================================
57	\section{Related Work}
58	\label{sec:related}
59	
60	\paragraph{Model collapse and recursive generation.}
61	Shumailov et al.\ (2024) demonstrate that iteratively training on model-generated data leads to distributional collapse.
62	Alemohammad et al.\ (2024) and Dohmatob et al.\ (2024) provide theoretical analysis of this phenomenon.
63	These works characterize macroscopic effects but do not operationalize detection of generational depth in individual documents.
64	
65	\paragraph{Machine-generated text detection.}
66	Binary detectors---watermarking, statistical tests (DetectGPT, DNA-GPT), and trained classifiers (DivEye, Binoculars)---distinguish human from machine text but conflate all generational depths into a single ``synthetic'' class.
67	Drayson et al.\ (2025) use binary detection confidence for importance resampling to prevent model collapse, the closest work to ours; however, we show that binary confidence is a poor depth proxy (Spearman $\rho \leq 0.22$; Section~\ref{sec:binary-proxy}).
68	
69	\paragraph{Data selection and curation.}
70	DSIR performs importance resampling to match a target distribution; D4 and DoReMi optimize domain weights.
71	These methods implicitly down-weight low-quality content but do not explicitly estimate recursive depth.
72	
73	% ==============================================================================
74	\section{Method}
75	\label{sec:method}
76	
77	\subsection{Recursive Generation as Iterated Lossy Channel}
78	\label{sec:theory}
79	
80	Let $P_0$ denote the human text distribution and $P_k = \mathcal{G}(P_{k-1})$ the distribution after $k$ rounds of generation through a stochastic language model $\mathcal{G}$.
81	Each application of $\mathcal{G}$ constitutes a lossy channel: the generated distribution $P_k$ cannot contain more information about $P_0$ than $P_{k-1}$ does.
82	By the Data Processing Inequality, for any divergence measure $D$:
83	\begin{equation}
84	    D(P_k \| P_{k+1}) \leq D(P_{k-1} \| P_k) \leq \cdots \leq D(P_0 \| P_1).
85	    \label{eq:dpi}
86	\end{equation}
87	
88	Since $D(P_k \| P_{k+1})$ is monotonically non-increasing and bounded below by zero, there exists a finite $\Kstar_{\mathrm{theory}}$ beyond which adjacent generations are information-theoretically indistinguishable.
89	Our empirical $\Kstar_{\mathrm{empirical}}$ provides a conservative lower bound on $\Kstar_{\mathrm{theory}}$, as measurement noise raises the effective indistinguishability floor.
90	
91	\subsection{Depth Estimation via Distributional Features}
92	\label{sec:features}
93	
94	We extract a 15-dimensional hand-crafted feature vector from each document, designed to capture distributional shifts induced by recursive generation:
95	
96	\begin{itemize}[nosep,leftmargin=1.5em]
97	    \item \textbf{Surprisal features} (6D): mean, std, and first/second differences of per-token surprisal under a reference language model, capturing smoothing of the surprisal landscape across generations.
98	    \item \textbf{Lexical diversity features} (5D): type-token ratio, hapax ratio, vocabulary richness, frequency entropy, and frequency kurtosis, capturing vocabulary compression.
99	    \item \textbf{Structural features} (4D): sentence length statistics, discourse markers, and repetition metrics, capturing homogenization of text structure.
100	\end{itemize}
101	
102	We train a LightGBM ordinal classifier on these features, predicting depth class $\hat{k} \in \{0, 1, 2, \ldots\}$.
103	
104	\subsection{Measuring $\Kstar$}
105	\label{sec:kstar-def}
106	
107	We operationalize $\Kstar$ as the largest $k$ for which the pairwise AUC between generations $k$ and $k+1$ exceeds a threshold $\theta$:
108	\begin{equation}
109	    \Kstar = \max\{k : \AUC(k, k+1) > \theta\}.
110	    \label{eq:kstar}
111	\end{equation}
112	
113	We set $\theta = 0.60$ (moderate discriminability above the 0.50 chance level) and report bootstrap 95\% confidence intervals on each pairwise AUC.
114	$\Kstar = k$ requires: (i) the lower bound of the 95\% CI for $\AUC(k-1, k)$ exceeds $\theta$, and (ii) the upper bound of the 95\% CI for $\AUC(k, k+1)$ falls below $\theta$.
115	
116	\subsection{Graduated Filtering}
117	\label{sec:graduated}
118	
119	Given a predicted depth $\hat{k}$ and a mixing parameter $\alpha \in [0,1]$, we assign sample weight:
120	\begin{equation}
121	    w(\hat{k}) = \begin{cases}
122	    1 & \text{if } \hat{k} = 0, \\
123	    (1 - \alpha)^{\hat{k}} & \text{if } \hat{k} \geq 1.
124	    \end{cases}
125	    \label{eq:graduated}
126	\end{equation}
127	
128	This provides a calibrated weighting that retains high-quality first-generation text at reduced weight while aggressively down-weighting deeper generations, in contrast to binary filtering which discards all synthetic text uniformly.
129	
130	% ==============================================================================
131	\section{Characterization Experiments}
132	\label{sec:characterization}
133	
134	All experiments use continuation-mode generation as the canonical condition unless otherwise noted, following our analysis that rewrite (instruction) mode introduces mode-specific style artifacts that inflate depth signal but reduce cross-model transferability (Section~\ref{sec:genmode}).
135	
136	\subsection{$\Kstar$ Measurement}
137	\label{sec:kstar-measurement}
138	
139	\paragraph{Setup.}
140	We measure $\Kstar$ across four model configurations using C4 documents, generating recursive chains to depth 5 with nucleus sampling ($p=0.95$, $T=1.0$).
141	Table~\ref{tab:kstar-main} reports pairwise AUC with bootstrap 95\% CIs.
142	
143	\begin{table}[t]
144	\centering
145	\small
146	\caption{Pairwise AUC across model configurations (continuation mode, $\theta=0.60$). All configurations yield $\Kstar=2$: 1v2 CI lower $> 0.60$, 2v3 CI upper $< 0.60$.}
147	\label{tab:kstar-main}
148	\begin{tabular}{lcccc}
149	\toprule
150	\textbf{Config} & \textbf{0v1} & \textbf{1v2} & \textbf{2v3} & $\Kstar$ \\
151	\midrule
152	Qwen-1.5B (rw) & 0.996 & 0.696 & 0.565 & 2 \\
153	Pythia-1.4B & 0.993 & 0.654 & 0.552 & 2 \\
154	OLMo-1B & 0.985 & 0.615 & 0.548 & 2 \\
155	Qwen-1.5B (cont) & 0.992 & 0.611 & 0.548 & 2 \\
156	\bottomrule
157	\end{tabular}
158	\end{table}
159	
160	Across all four configurations, $\Kstar=2$.
161	The 0v1 boundary is consistently strong (AUC $> 0.98$), while the 1v2 boundary ranges from $0.611$ to $0.696$, with the continuation-mode Qwen configuration being most marginal (CI: $[0.602, 0.621]$).
162	All 2v3 AUCs fall below $0.57$, confirming that depth $\geq 2$ text converges to a distributional fixed point.
163	
164	\paragraph{Cross-scale stability.}
165	Table~\ref{tab:cross-scale} compares Qwen2.5-1.5B and 7B.
166	The 7B model yields $\AUC_{1v2} = 0.629$ versus $0.611$ for 1.5B ($\Delta = +1.7$pp, Welch $t$-test $p = 0.18$), a non-significant difference.
167	
168	\begin{table}[t]
169	\centering
170	\small
171	\caption{Cross-scale comparison: Qwen2.5 1.5B vs 7B (continuation mode, nucleus $p=0.95$). $\Kstar=2$ remains stable; scale does not significantly affect the discrimination boundary.}
172	\label{tab:cross-scale}
173	\begin{tabular}{lccccc}
174	\toprule
175	\textbf{Scale} & \textbf{0v1} & \textbf{1v2} & \textbf{1v2 CI} & \textbf{2v3} & $p$ \\
176	\midrule
177	1.5B & 0.992 & 0.611 & [.602, .621] & 0.548 & --- \\
178	7B & 0.998 & 0.629 & [.606, .651] & 0.558 & 0.18 \\
179	\bottomrule
180	\end{tabular}
181	\end{table}
182	
183	The wider CI for 7B ($\pm 0.023$) reflects the reduced sample size (1K vs 5K documents) necessitated by computational constraints.
184	The degradation ordering between scales is highly consistent (Spearman $\rho = 0.82$), with \texttt{surp\_d1\_std}, \texttt{surp\_std}, and \texttt{freq\_entropy} as the top discriminative features at both scales.
185	
186	\paragraph{Base vs instruct model.}
187	Table~\ref{tab:base-instruct} compares Qwen2.5-1.5B base (no instruction tuning) against the instruct variant.
188	The base model yields $\AUC_{1v2} = 0.599$, with CI lower bound $0.588 < 0.60$---placing $\Kstar$ at the threshold boundary.
189	
190	\begin{table}[t]
191	\centering
192	\small
193	\caption{Base vs instruct model (Qwen2.5-1.5B, continuation mode). The base model's 1v2 AUC CI lower falls below $\theta=0.60$, yielding borderline $\Kstar$.}
194	\label{tab:base-instruct}
195	\begin{tabular}{lcccc}
196	\toprule
197	\textbf{Variant} & \textbf{0v1} & \textbf{1v2} & \textbf{1v2 CI} & $\Kstar$ \\
198	\midrule
199	Instruct & 0.992 & 0.611 & [.602, .621] & 2 \\
200	Base & 0.992 & 0.599 & [.588, .609] & 1\textsuperscript{$\dagger$} \\
201	\bottomrule
202	\end{tabular}
203	\vspace{0.3em}
204	\raggedright\scriptsize\textsuperscript{$\dagger$}At $\theta=0.585$, the base model also achieves $\Kstar=2$; the result is threshold-sensitive.
205	\end{table}
206	
207	Feature degradation orderings remain highly consistent between base and instruct variants (Spearman $\rho = 0.87$), with \texttt{surp\_d1\_std} and \texttt{surp\_std} ranking in the top 3 for both.
208	The key divergence is \texttt{freq\_entropy}, which ranks 1st for the instruct model but 5th for the base model, reflecting instruction tuning's effect on vocabulary concentration.
209	
210	\subsection{Cross-Model Transfer}
211	\label{sec:transfer}
212	
213	Depth features trained on one model's generations and evaluated on another's retain 91\% accuracy (Pythia$\leftrightarrow$OLMo), with 0v1 transfer AUC exceeding 0.96 across all pairs.
214	This demonstrates that depth signal is predominantly text-intrinsic (70--85\%) rather than an artifact of model self-familiarity.
215	Transfer performance for 1v2+ pairs depends on model family similarity, consistent with the weak signal above $\Kstar$.
216	
217	\subsection{Degradation Ordering}
218	\label{sec:degradation}
219	
220	We analyze which features degrade most rapidly across generations.
221	Single-feature AUC rankings are consistent across model configurations (Spearman $\rho \geq 0.82$ for continuation mode).
222	The top three discriminative features---\texttt{surp\_d1\_std} (first-difference surprisal standard deviation), \texttt{surp\_std} (raw surprisal standard deviation), and \texttt{surp\_d2\_std} or \texttt{freq\_entropy}---reflect the smoothing of the surprisal landscape and compression of vocabulary diversity that characterize iterative generation.
223	
224	The retrain-chain experiment (Section~\ref{sec:retrain}) confirms that this ordering transfers to the ecologically valid setting ($\rho = 0.78$, with 2 of 3 top features shared), with \texttt{freq\_kurtosis} gaining importance in the retrain scenario due to LoRA fine-tuning's systematic compression of frequency distribution tails.
225	
226	\subsection{Generation Mode Analysis}
227	\label{sec:genmode}
228	
229	Rewrite (instruction) mode yields substantially higher signal (AUC$_{1v2} = 0.696$ vs $0.611$ for continuation, $\Delta = +8.4$pp) but lower cross-model transferability (61--63\% retention vs 80--92\%).
230	The asymmetry in feature transfer---continuation$\to$rewrite 89\% vs rewrite$\to$continuation 82\%---indicates that continuation features form a universal subset augmented by mode-specific style artifacts in rewrite mode.
231	We therefore adopt continuation mode as the canonical condition for all cross-model claims.
232	
233	% ==============================================================================
234	\section{Application: Graduated Filtering}
235	\label{sec:application}
236	
237	\subsection{Filtering Strategy Comparison}
238	\label{sec:filtering}
239	
240	We evaluate six filtering strategies under continued pretraining of Qwen2.5-1.5B with 30\% synthetic text injection, measuring downstream performance on MMLU and HellaSwag across 5 random seeds.
241	Table~\ref{tab:filtering} reports results.
242	
243	\begin{table}[t]
244	\centering
245	\small
246	\caption{Filtering strategies at 30\% synthetic injection (5 seeds, mean $\pm$ std). Graduated filtering yields modest improvement over binary; DSIR achieves comparable performance without depth estimation.}
247	\label{tab:filtering}
248	\begin{tabular}{lcc}
249	\toprule
250	\textbf{Strategy} & \textbf{MMLU} & \textbf{HellaSwag} \\
251	\midrule
252	Clean baseline & 46.5 $\pm$ 0.3 & 62.0 $\pm$ 0.4 \\
253	\midrule
254	No filter & 44.8 $\pm$ 0.4 & 60.2 $\pm$ 0.5 \\
255	Surprisal-based & 45.0 $\pm$ 0.4 & 60.4 $\pm$ 0.5 \\
256	Binary (Drayson) & 45.3 $\pm$ 0.3 & 60.8 $\pm$ 0.4 \\
257	Binary (ours) & 45.5 $\pm$ 0.3 & 60.9 $\pm$ 0.4 \\
258	DSIR & 45.9 $\pm$ 0.3 & 61.4 $\pm$ 0.4 \\
259	Graduated ($\alpha\!=\!0.5$) & \textbf{46.1} $\pm$ 0.3 & \textbf{61.5} $\pm$ 0.4 \\
260	\bottomrule
261	\end{tabular}
262	\end{table}
263	
264	Graduated filtering recovers most of the clean-data performance ($-0.4$pp on MMLU vs clean, compared to $-1.7$pp for no filtering).
265	However, the advantage over binary filtering is modest: $+0.6$pp on both MMLU and HellaSwag, with paired $t$-test $p$-values of $0.072$ and $0.085$ respectively---borderline significant.
266	DSIR performs comparably to graduated filtering ($-0.2$pp MMLU, $-0.1$pp HellaSwag, neither significant), indicating that importance resampling implicitly achieves a similar quality gradient without explicit depth estimation.
267	
268	\paragraph{Sensitivity to $\alpha$.}
269	Table~\ref{tab:alpha} shows that graduated filtering is robust to the mixing parameter, with a shallow inverted-U peaking at $\alpha = 0.5$.
270	
271	\begin{table}[t]
272	\centering
273	\small
274	\caption{Graduated filtering sensitivity to $\alpha$ (30\% injection).}
275	\label{tab:alpha}
276	\begin{tabular}{lccccc}
277	\toprule
278	$\alpha$ & 0.1 & 0.3 & 0.5 & 0.7 & 0.9 \\
279	\midrule
280	MMLU & 45.7 & 45.9 & \textbf{46.1} & 46.0 & 45.8 \\
281	HellaSwag & 61.0 & 61.3 & \textbf{61.5} & 61.4 & 61.1 \\
282	\bottomrule
283	\end{tabular}
284	\end{table}
285	
286	\subsection{Dose-Response Analysis}
287	\label{sec:dose}
288	
289	The practical value of graduated filtering scales with contamination prevalence.
290	Table~\ref{tab:dose} shows the graduated$-$binary delta across three injection rates.
291	
292	\begin{table}[t]
293	\centering
294	\small
295	\caption{Dose-response: graduated vs binary filtering across contamination levels. Benefit becomes significant only at high contamination (50\%).}
296	\label{tab:dose}
297	\begin{tabular}{lccccc}
298	\toprule
299	\textbf{Dose} & \multicolumn{2}{c}{\textbf{MMLU}} & \multicolumn{2}{c}{\textbf{HellaSwag}} & $p$ \\
300	\cmidrule(lr){2-3}\cmidrule(lr){4-5}
301	 & Binary & Grad. & Binary & Grad. & (MMLU) \\
302	\midrule
303	10\% & 46.2 & 46.4 & 61.7 & 61.9 & 0.32 \\
304	30\% & 45.5 & 46.1 & 60.9 & 61.5 & 0.08 \\
305	50\% & 44.8 & 45.9 & 60.1 & 61.0 & 0.038 \\
306	\bottomrule
307	\end{tabular}
308	\end{table}
309	
310	At 10\% contamination, the difference is negligible ($+0.2$pp, $p=0.32$).
311	At 50\% contamination---a worst-case but increasingly plausible scenario as web synthetic content grows---the benefit reaches $+1.1$pp on MMLU ($p=0.038$).
312	
313	% ==============================================================================
314	\section{Supporting Analyses}
315	\label{sec:supporting}
316	
317	\subsection{Retrain-Chain Ecological Validity}
318	\label{sec:retrain}
319	
320	Prompt-chain generation provides controlled conditions but may overestimate inter-generational differences compared to the recursive fine-tuning that characterizes real-world model collapse.
321	We validate with a retrain-chain experiment: Pythia-1.4B with LoRA (rank=16, $\alpha=32$) iteratively fine-tuned on its own generations (C4, 5K documents, depth 0--4).
322	
323	\begin{table}[t]
324	\centering
325	\small
326	\caption{Prompt-chain vs retrain-chain pairwise AUC (Pythia-1.4B). Retrain-chain confirms $\Kstar=2$ with attenuated but consistent signal.}
327	\label{tab:retrain}
328	\begin{tabular}{lcccc}
329	\toprule
330	\textbf{Method} & \textbf{0v1} & \textbf{1v2} & \textbf{2v3} & \textbf{3v4} \\
331	\midrule
332	Prompt-chain & 0.993 & 0.654 & 0.552 & --- \\
333	Retrain-chain & 0.975 & 0.621 & 0.544 & 0.510 \\
334	$\Delta$ & $-$1.8pp & $-$3.3pp & $-$0.8pp & --- \\
335	\bottomrule
336	\end{tabular}
337	\end{table}
338	
339	The retrain-chain attenuates all pairwise AUCs ($\Delta\AUC_{1v2} = -3.3$pp) but preserves $\Kstar=2$.
340	Feature ranking correlation between prompt- and retrain-chains is $\rho = 0.78$, with 2 of 3 top features shared.
341	The attenuation reflects that LoRA fine-tuning produces more subtle distributional shifts than prompt-based generation, as the model gradually adapts to its own output distribution.
342	
343	\subsection{LLM Zero-Shot Depth Estimation}
344	\label{sec:llm-baseline}
345	
346	We evaluate GPT-4o and Claude 3.5 on zero-shot depth estimation to establish that generational depth is a distributional property not accessible to surface-level analysis.
347	Table~\ref{tab:llm-zeroshot} reports results.
348	
349	\begin{table}[t]
350	\centering
351	\small
352	\caption{LLM zero-shot vs our 15D method on depth estimation. LLMs achieve near-chance on depth classification despite reasonable binary detection.}
353	\label{tab:llm-zeroshot}
354	\begin{tabular}{lccccc}
355	\toprule
356	\textbf{Method} & \textbf{Bin.\ Acc.} & \textbf{3-cl.} & \textbf{6-cl.} & $\rho$ & \textbf{MAE} \\
357	\midrule
358	GPT-4o & 0.72 & 0.38 & 0.20 & 0.18 & 1.85 \\
359	Claude 3.5 & 0.68 & 0.36 & 0.19 & 0.15 & 1.92 \\
360	\midrule
361	Random & --- & 0.33 & 0.17 & --- & --- \\
362	Ours (15D) & --- & 0.63 & 0.42 & 0.55 & --- \\
363	\bottomrule
364	\end{tabular}
365	\end{table}
366	
367	While LLMs achieve moderate binary detection (68--72\%), their 3-class depth accuracy (36--38\%) is near chance (33.3\%), and Spearman $\rho$ with true depth is $\leq 0.18$.
368	Our 15D feature method achieves 63\% 3-class accuracy and $\rho = 0.55$, confirming that depth estimation requires specialized distributional measurement.
369	
370	\subsection{Binary Detector Confidence as Depth Proxy}
371	\label{sec:binary-proxy}
372	
373	A natural question is whether binary detector confidence scores can serve as depth proxies, obviating the need for dedicated depth estimation.
374	Table~\ref{tab:binary-proxy} shows this is not the case.
375	
376	\begin{table}[t]
377	\centering
378	\small
379	\caption{Binary detector confidence as depth proxy. Strong binary detection does not translate to depth estimation.}
380	\label{tab:binary-proxy}
381	\begin{tabular}{lcccc}
382	\toprule
383	\textbf{Detector} & \textbf{Bin.\ AUC} & $\rho_{\mathrm{depth}}$ & \textbf{AUC}$_{1v2}$ & \textbf{AUC}$_{2v3}$ \\
384	\midrule
385	DivEye & 0.882 & 0.215 & 0.548 & 0.512 \\
386	Binoculars & 0.907 & 0.192 & 0.534 & 0.508 \\
387	\midrule
388	Ours (15D) & --- & 0.553 & 0.654 & 0.552 \\
389	\bottomrule
390	\end{tabular}
391	\end{table}
392	
393	Binary confidence correlates weakly with depth ($\rho \leq 0.22$) and yields near-chance pairwise AUC for 1v2 and 2v3 pairs.
394	Notably, Binoculars achieves higher binary AUC (0.907) but \emph{lower} depth correlation ($\rho = 0.192$) than DivEye ($\rho = 0.215$), confirming that better binary detection does not imply better depth estimation---these are fundamentally different tasks.
395	
396	\subsection{Learned Representation Baseline}
397	\label{sec:learned}
398	
399	We compare our hand-crafted 15D features against frozen Qwen2.5-1.5B last-hidden-state embeddings (1536D) with a 2-layer MLP, evaluated across three generator configurations (Table~\ref{tab:learned}).
400	
401	\begin{table}[t]
402	\centering
403	\small
404	\caption{Hand-crafted 15D features vs frozen LM embeddings + MLP. Learned representations outperform by $\sim$5pp but at the cost of interpretability.}
405	\label{tab:learned}
406	\begin{tabular}{llccc}
407	\toprule
408	\textbf{Generator} & \textbf{Method} & \textbf{Acc.} & \textbf{mPW-AUC} & \textbf{AUC}$_{1v2}$ \\
409	\midrule
410	\multirow{2}{*}{Qwen (rw)} & 15D & 0.423 & 0.621 & 0.696 \\
411	 & Learned & 0.479 & 0.682 & 0.734 \\
412	\midrule
413	\multirow{2}{*}{Pythia} & 15D & 0.386 & 0.606 & 0.654 \\
414	 & Learned & 0.436 & 0.650 & 0.697 \\
415	\midrule
416	\multirow{2}{*}{OLMo} & 15D & 0.382 & 0.602 & 0.615 \\
417	 & Learned & 0.431 & 0.643 & 0.658 \\
418	\bottomrule
419	\end{tabular}
420	\end{table}
421	
422	Learned representations outperform hand-crafted features by $\sim$5pp in accuracy and $\sim$4.9pp in mean pairwise AUC, consistently across all configurations.
423	However, the 15D features capture approximately 85\% of the available discriminative signal, indicating that depth information is predominantly encoded in low-dimensional statistical patterns.
424	The interpretability-performance tradeoff is central: learned features are stronger but opaque, while hand-crafted features uniquely support the degradation ordering analysis (Section~\ref{sec:degradation}) and cross-model transfer analysis (Section~\ref{sec:transfer}) that constitute the paper's primary characterization contribution.
425	
426	\subsection{Naturalistic Validation}
427	\label{sec:naturalistic}
428	
429	We apply our depth estimator to a 10K-document sample from Common Crawl (2025 snapshot) to assess ecological plausibility.
430	
431	\begin{table}[t]
432	\centering
433	\small
434	\caption{Predicted depth distribution on Common Crawl 2025 and correlation with independent quality proxies.}
435	\label{tab:naturalistic}
436	\begin{tabular}{lclc}
437	\toprule
438	\textbf{Pred.\ Depth} & \textbf{\%} & \textbf{Proxy} & $\rho$ \\
439	\midrule
440	Gen-0 (human) & 83.2 & AlignScore & $-$0.28 \\
441	Gen-1 & 11.5 & Vocab richness & $-$0.24 \\
442	Gen-2+ & 5.3 & Self-BLEU & +0.19 \\
443	 & & Perplexity (GPT-2) & $-$0.31 \\
444	\bottomrule
445	\end{tabular}
446	\end{table}
447	
448	The predicted distribution (83/12/5\%) is broadly consistent with current estimates of web synthetic content prevalence (10--20\%).
449	Correlations with independent quality proxies are weak but directionally consistent: predicted deeper-generation text exhibits lower factual alignment (AlignScore $\rho = -0.28$), lower vocabulary richness ($\rho = -0.24$), and lower perplexity under GPT-2 ($\rho = -0.31$), the latter reflecting proximity to the LM typical set.
450	We present this as preliminary ecological validation, acknowledging the absence of ground-truth depth labels and the confounding effects of domain, length, and genre variation.
451	
452	% ==============================================================================
453	\section{Conclusion}
454	\label{sec:conclusion}
455	
456	We introduced the generational discrimination boundary $\Kstar$ as a principled quantity for characterizing recursive synthetic text contamination, grounded in the Data Processing Inequality.
457	Through systematic measurement across model families, scales, and generation modes, we established $\Kstar=2$ under standard nucleus sampling at the 1.5B scale---meaning that while human and first-generation synthetic text are readily distinguishable, text beyond the second generation converges to a distributional fixed point.
458	This finding is stable from 1.5B to 7B parameters ($p=0.18$) and across model families (91\% cross-model transfer retention), though base models without instruction tuning show borderline behavior at the threshold.
459	
460	The practical implication is nuanced: $\Kstar$-aware graduated filtering provides modest improvement over binary filtering, scaling with contamination prevalence ($+1.1$pp at 50\% contamination), but general-purpose data selection achieves comparable results.
461	The primary value of $\Kstar$ measurement thus lies in scientific characterization---understanding \emph{how} recursive generation degrades text distributions---rather than direct engineering advantage.
462	
463	\paragraph{Limitations.}
464	Our measurements are limited to 1.5B--7B scale models; larger models may exhibit different $\Kstar$ behavior.
465	The retrain-chain validation uses LoRA (rank=16) rather than full fine-tuning.
466	Naturalistic validation lacks ground-truth depth labels.
467	The $\Kstar=2$ result is specific to nucleus sampling ($p=0.95$); other decoding strategies (e.g., greedy) may yield different boundaries.
468	
469	\end{document}
470	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94412fd5-8aac-4fd6-97ab-ff6c06c2ee76",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "5a91543e-da8c-4e16-b525-4dba72115154",
  "sourceToolAssistantUUID": "94412fd5-8aac-4fd6-97ab-ff6c06c2ee76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-13T08:54:53.747Z_

Now let me also read the review context file and the best/worst dream papers for comparison.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a91543e-da8c-4e16-b525-4dba72115154",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHcZiL1rKn5R8hk2vgo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e566634b-70e6-4c38-b06a-7db77c8384cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jt7TM483NuKfjRYPvzPjp5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10230,
      "cache_read_input_tokens": 29507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10230,
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

_source line 36 · 2026-05-13T08:54:55.644Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01JLJWsZTqYV9X5fPBZeBAGC`</summary>

```json
{
  "pattern": "**/review_context*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e566634b-70e6-4c38-b06a-7db77c8384cc",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHcZiL1rKn5R8hk2vgo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a1a9219-2875-406d-9190-eb582d2aa7b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jt7TM483NuKfjRYPvzPjp5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10230,
      "cache_read_input_tokens": 29507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10230,
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

_source line 37 · 2026-05-13T08:54:55.655Z_

<details><summary>↩ Tool result · `toolu_01JLJWsZTqYV9X5fPBZeBAGC`</summary>

```text
artifacts/dream_reports/dream_20260513T080728/best/review_context.yaml
artifacts/dream_reports/dream_20260513T080728/median/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a1a9219-2875-406d-9190-eb582d2aa7b8",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "971d2068-9950-41fa-b40f-91e5c4a92712",
  "sourceToolAssistantUUID": "8a1a9219-2875-406d-9190-eb582d2aa7b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-13T08:54:55.902Z_

<details open><summary>🔧 Tool call — Glob · `toolu_015X1CuSvRyUc4sbEZk9rMyA`</summary>

```json
{
  "pattern": "**/dream_review*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "971d2068-9950-41fa-b40f-91e5c4a92712",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHcZiL1rKn5R8hk2vgo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f74bb8a-056f-499f-b7c2-5db7214ebf23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jt7TM483NuKfjRYPvzPjp5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10230,
      "cache_read_input_tokens": 29507,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10230
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 29507,
          "cache_creation_input_tokens": 10230,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10230,
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

_source line 39 · 2026-05-13T08:54:55.937Z_

<details><summary>↩ Tool result · `toolu_015X1CuSvRyUc4sbEZk9rMyA`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f74bb8a-056f-499f-b7c2-5db7214ebf23",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "ebc9ef3e-3a20-4fb0-a285-8daed20e8776",
  "sourceToolAssistantUUID": "8f74bb8a-056f-499f-b7c2-5db7214ebf23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-13T08:54:59.129Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JEEDzgcR7Yc7XxWgCmde1Y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260513T080728/median/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebc9ef3e-3a20-4fb0-a285-8daed20e8776",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHcxP6Z5pt3tUxLBo7z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49bb9af3-16b3-432c-87c4-fff0cfb697b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pgc8zeUcjo2gdVwfNe6wpL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 314,
      "cache_read_input_tokens": 39737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 314,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 41 · 2026-05-13T08:54:59.136Z_

<details><summary>↩ Tool result · `toolu_01JEEDzgcR7Yc7XxWgCmde1Y`</summary>

```text
1	narrative_guidance: 'C1'' 仍是核心但需 qualification: "K*=2 under standard nucleus sampling
2	  at 1.5B scale"。 exp-004 显示 7B 未显著改善 K*，exp-016 base model 在阈值边缘（CI lower < 0.60）。
3	  exp-003 (RUNNING) 预期 greedy 配置 K*=1 打破 universal claim，要求限定 scope。 C3 从 "practically
4	  superior" 弱化为 "modest but consistent improvement"： graduated − binary 仅 0.5-1.5pp
5	  且 borderline significant，DSIR 持平进一步削弱应用叙事。 exp-015 learned features 优 ~5pp 需诚实报告但论述
6	  interpretability-performance tradeoff。 论文结构 characterization-heavy: §4 四个子节（K* measurement,
7	  cross-model transfer, degradation ordering, generation mode analysis），§5 缩短为 application
8	  note。 审稿策略: 强调 "first systematic measurement" + DPI 理论框架。目标 EMNLP 2026 Findings
9	  (稳) 或 Main (borderline)。
10	
11	  '
12	imagined_experiments:
13	- name: 'Cross-scale probe: Qwen2.5-7B'
14	  plan_id: exp-004
15	  description: Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth 0-3. 测试 K* 是否随模型规模变化。
16	  expected_results:
17	    k_star: 2
18	    pairwise_auc:
19	      0v1: 0.9983
20	      1v2: 0.6285
21	      2v3: 0.558
22	    pairwise_auc_ci:
23	      1v2_ci_lower: 0.6058
24	      1v2_ci_upper: 0.6512
25	      2v3_ci_lower: 0.5342
26	      2v3_ci_upper: 0.5818
27	    pairwise_jsd:
28	      0v1: 0.2953
29	      1v2: 0.0068
30	      2v3: 0.0042
31	    ordinal_accuracy_3class: 0.52
32	    ordinal_mae_3class: 0.58
33	    scale_comparison:
34	      auc_1v2_7B: 0.6285
35	      auc_1v2_1.5B_cont: 0.6112
36	      delta_pp: 1.73
37	      welch_t_p_value: 0.18
38	      ci_overlap: true
39	    degradation_spearman_rho_vs_1.5B: 0.82
40	    top3_features:
41	    - surp_d1_std
42	    - surp_std
43	    - freq_entropy
44	  result_rationale: '7B 的 1v2 AUC (0.6285) 仅比 1.5B (0.6112) 高 ~1.7pp，Welch t-test
45	    p=0.18 不显著。 原因: (1) K* 由 iterated lossy channel 信息衰减速率决定，depth 2+ 信号已接近 noise
46	    floor， 更大模型不改变此信息论极限；(2) 7B 更高建模能力使 gen-1 更接近 human distribution， 同时也使 gen-2 与
47	    gen-1 差异更难检测——两者部分抵消；(3) 仅 1K docs 导致 CI 较宽 (±0.023)， 进一步模糊潜在小效应。1K docs 而非 5K
48	    是 GPU budget 约束（7B 的 generation 开销是 1.5B 的 ~5x）， CI 宽度本身就是 limitation。degradation
49	    ordering ρ=0.82 说明特征退化模式在 scale 间稳定。
50	
51	    '
52	  tables:
53	  - 'Table: Pairwise AUC across scales (1.5B vs 7B), bootstrap 95% CI, Welch t-test
54	    p-values'
55	  figures_description:
56	  - 'Bar chart: 1v2 AUC with CI error bars — Qwen-1.5B-cont vs Qwen-7B, 显示 CI 重叠'
57	  - 'AUC decay curve (depth pair vs AUC): 7B overlaid on 1.5B, 几乎相同的衰减形状'
58	  analysis: '结论: scale 在 1.5B→7B 范围内不显著改变 K*。论文写法: "K*=2 remains stable from 1.5B
59	    to 7B (Δ AUC₁ᵥ₂ = +1.7pp, p = 0.18), though larger models (>7B) may exhibit different
60	    behavior." 支持 bounded claim 但不能外推。7B 结果作为 §4.1 K* measurement 的子结果呈现。
61	
62	    '
63	- name: Downstream filtering evaluation
64	  plan_id: exp-006
65	  description: 六种过滤策略 (no-filter / binary-ours / binary-Drayson / graduated / surprisal-based
66	    / DSIR) + α sensitivity sweep，5 seeds paired t-test，continued pretraining + lm-eval-harness
67	    (MMLU, HellaSwag)。假设 30% synthetic injection ratio。
68	  expected_results:
69	    clean_baseline:
70	      mmlu:
71	        mean: 46.5
72	        std: 0.3
73	      hellaswag:
74	        mean: 62.0
75	        std: 0.4
76	    no_filter:
77	      mmlu:
78	        mean: 44.8
79	        std: 0.4
80	      hellaswag:
81	        mean: 60.2
82	        std: 0.5
83	    binary_drayson:
84	      mmlu:
85	        mean: 45.3
86	        std: 0.3
87	      hellaswag:
88	        mean: 60.8
89	        std: 0.4
90	    surprisal_based:
91	      mmlu:
92	        mean: 45.0
93	        std: 0.4
94	      hellaswag:
95	        mean: 60.4
96	        std: 0.5
97	    binary_ours:
98	      mmlu:
99	        mean: 45.5
100	        std: 0.3
101	      hellaswag:
102	        mean: 60.9
103	        std: 0.4
104	    graduated_best_alpha:
105	      mmlu:
106	        mean: 46.1
107	        std: 0.3
108	      hellaswag:
109	        mean: 61.5
110	        std: 0.4
111	      optimal_alpha: 0.5
112	    dsir:
113	      mmlu:
114	        mean: 45.9
115	        std: 0.3
116	      hellaswag:
117	        mean: 61.4
118	        std: 0.4
119	    graduated_minus_binary_ours:
120	      mmlu_delta_pp: 0.6
121	      mmlu_paired_t_p: 0.072
122	      hellaswag_delta_pp: 0.6
123	      hellaswag_paired_t_p: 0.085
124	    dsir_minus_graduated:
125	      mmlu_delta_pp: -0.2
126	      hellaswag_delta_pp: -0.1
127	      neither_significant: true
128	    alpha_sweep:
129	      alpha_0.1:
130	        mmlu: 45.7
131	        hellaswag: 61.0
132	      alpha_0.3:
133	        mmlu: 45.9
134	        hellaswag: 61.3
135	      alpha_0.5:
136	        mmlu: 46.1
137	        hellaswag: 61.5
138	      alpha_0.7:
139	        mmlu: 46.0
140	        hellaswag: 61.4
141	      alpha_0.9:
142	        mmlu: 45.8
143	        hellaswag: 61.1
144	  result_rationale: 'graduated − binary = +0.6pp (MMLU/HellaSwag), p ∈ [0.07, 0.09]
145	    borderline significant。 原因: K*=2 意味着仅 3 个有效类别 (human/gen-1/gen-2+)，ordinal signal
146	    很粗糙。 graduated 优势仅体现在 gen-1 vs gen-2 的决策边界——对 gen-1（质量尚可）给予部分权重而非完全丢弃。 处于此决策边界的样本比例有限
147	    (大约 training data 的 8-12%)，整体收益被稀释。 p-value borderline 因为 5 seeds 统计功效有限 (power
148	    ~0.45 for 0.6pp effect size)。 DSIR 持平 graduated 因为 importance resampling 隐式实现类似质量梯度：
149	    低质量文本被下采样，效果等价于 soft ordinal filtering。 α=0.5 最优因为 ordinal signal 有噪声：过强 (α→1)
150	    放大误分类风险，过弱 (α→0) 退化为 binary。 α sweep 呈平缓 inverted-U 形——好消息: 对超参数不敏感。 binary-ours
151	    优于 binary-Drayson (+0.2pp) 因为共享相同 feature space 使比较更公平， Drayson 的 importance resampling
152	    引入额外方差。
153	
154	    '
155	  tables:
156	  - 'Table: 六种策略 MMLU/HellaSwag (mean ± std, 5 seeds), paired t-test p-values for
157	    key comparisons'
158	  - 'Table: α sensitivity sweep — graduated α ∈ {0.1, 0.3, 0.5, 0.7, 0.9} MMLU/HellaSwag'
159	  figures_description:
160	  - 'Grouped bar chart: 六种策略 MMLU/HellaSwag 得分, error bars = 1 std, clean baseline
161	    虚线'
162	  - 'Line plot: α vs MMLU/HellaSwag, 显示平缓 inverted-U (峰值 α≈0.5)'
163	  analysis: 'C3 收益真实但偏弱 (0.6pp, borderline p)，不足以作为独立 selling point。 DSIR 无需 depth
164	    estimation 即达相似效果，进一步削弱应用价值。 论文定位: C3 缩为 §5 short application section，核心论点变为 "even
165	    coarse 3-class ordinal signal provides modest improvement at the decision boundary;
166	    general-purpose data selection methods achieve comparable results without explicit
167	    depth estimation, suggesting that the primary value of depth measurement lies
168	    in scientific characterization rather than direct engineering advantage."
169	
170	    '
171	- name: Retrain-chain ecological validity
172	  plan_id: exp-008
173	  description: Pythia-1.4B LoRA (rank=16, alpha=32), C4 5K docs, depth 0-4. 对比 prompt-chain
174	    和 retrain-chain 的 K* 和特征分布。
175	  expected_results:
176	    k_star: 2
177	    pairwise_auc:
178	      0v1: 0.9754
179	      1v2: 0.6205
180	      2v3: 0.5438
181	      3v4: 0.5095
182	    pairwise_auc_ci:
183	      0v1_ci:
184	      - 0.9712
185	      - 0.9796
186	      1v2_ci:
187	      - 0.6098
188	      - 0.6312
189	      2v3_ci:
190	      - 0.5331
191	      - 0.5545
192	      3v4_ci:
193	      - 0.4982
194	      - 0.5208
195	    pairwise_jsd:
196	      0v1: 0.1547
197	      1v2: 0.0098
198	      2v3: 0.0038
199	      3v4: 0.0025
200	    ordinal_accuracy: 0.372
201	    ordinal_mae: 1.168
202	    prompt_vs_retrain_comparison:
203	      prompt_chain_ref_auc_0v1: 0.9932
204	      prompt_chain_ref_auc_1v2: 0.6539
205	      retrain_chain_auc_0v1_delta: -0.0178
206	      retrain_chain_auc_1v2_delta: -0.0334
207	      retrain_chain_auc_2v3_delta: -0.0077
208	      feature_ranking_spearman_rho: 0.78
209	      top3_feature_overlap: 2 of 3 shared (surp_d1_std, surp_std)
210	    top3_features:
211	    - surp_d1_std
212	    - surp_std
213	    - freq_kurtosis
214	  result_rationale: 'retrain-chain 0v1 AUC (0.975) 低于 prompt-chain (0.993) —— LoRA
215	    rank=16 对模型的改变 比逐步 prompt generation 更 subtle，首代 retrain 文本与原模型偏移较小。 1v2 AUC (0.620)
216	    比 prompt-chain (0.654) 低 ~3.3pp：retrain 使模型逐渐"适应" 自身生成分布，减缓代际间信息损失速率（模型在自己的输出上变得更
217	    calibrated）， 但不改变 K*=2 的基本事实——到 depth 3 信号仍收敛到 noise floor。 特征排序 ρ=0.78 (vs prompt-chain)
218	    反映退化机制高度相关但不完全相同： retrain-chain 中 freq_kurtosis 排名上升因为 LoRA 微调系统性压缩词频分布尾部。 JSD
219	    全面低于 prompt-chain (0v1: 0.154 vs 0.214) 反映 retrain 后模型输出分布更接近训练分布。
220	
221	    '
222	  tables:
223	  - 'Table: Prompt-chain vs Retrain-chain pairwise AUC 对比, bootstrap CI'
224	  figures_description:
225	  - 'Parallel AUC decay curves: prompt-chain vs retrain-chain, same K*=2 但 offset
226	    lower'
227	  - 'Feature importance heatmap: side-by-side prompt vs retrain, highlighting freq_kurtosis
228	    上升'
229	  analysis: 'retrain-chain 确认 K*=2 在更接近真实 model collapse 场景下成立，增强 ecological validity。
230	    prompt-chain 高估代际差异（特别是 0v1），论文需写: "Prompt-chain provides a controlled upper bound;
231	    retrain-chain ecological validation confirms K*=2 with attenuated but consistent
232	    signal (Δ AUC₁ᵥ₂ = −3.3pp)." LoRA rank=16 是实际限制——完整微调可能不同，列为 limitation。
233	
234	    '
235	- name: Contamination dose-response
236	  plan_id: exp-009
237	  description: 10%/30%/50% synthetic injection 下 graduated vs binary filtering 收益差异。
238	  expected_results:
239	    dose_10pct:
240	      no_filter:
241	        mmlu: 46.1
242	        hellaswag: 61.6
243	      binary_ours:
244	        mmlu: 46.2
245	        hellaswag: 61.7
246	      graduated:
247	        mmlu: 46.4
248	        hellaswag: 61.9
249	      graduated_minus_binary_pp: 0.2
250	      paired_t_p: 0.32
251	    dose_30pct:
252	      no_filter:
253	        mmlu: 44.8
254	        hellaswag: 60.2
255	      binary_ours:
256	        mmlu: 45.5
257	        hellaswag: 60.9
258	      graduated:
259	        mmlu: 46.1
260	        hellaswag: 61.5
261	      graduated_minus_binary_pp: 0.6
262	      paired_t_p: 0.08
263	    dose_50pct:
264	      no_filter:
265	        mmlu: 43.5
266	        hellaswag: 58.8
267	      binary_ours:
268	        mmlu: 44.8
269	        hellaswag: 60.1
270	      graduated:
271	        mmlu: 45.9
272	        hellaswag: 61.0
273	      graduated_minus_binary_pp: 1.1
274	      paired_t_p: 0.038
275	    dose_response_trend: monotonically increasing graduated−binary delta with contamination
276	      dose
277	  result_rationale: 'graduated vs binary 收益随 dose 单调递增 (0.2→0.6→1.1pp)。 10% 时差异可忽略
278	    (p=0.32)：contaminated 样本占比小，binary 已能移除大部分， graduated 的边际价值被 clean data 主导的 signal
279	    淹没。 30% 时 borderline (p=0.08)：binary 误杀 gen-1（质量可接受）的代价开始显现， graduated 保留部分 gen-1
280	    内容。 50% 时 significant (p=0.038)：高比例 contamination 下 gen-1 样本数量庞大， binary 丢弃它们的损失显著，graduated
281	    的 calibrated weighting 优势放大。 实际 web data synthetic 比例目前估计 10-30%， 所以 graduated
282	    filtering 的真实收益大概率在 0.2-0.6pp 的 borderline 范围。
283	
284	    '
285	  tables:
286	  - 'Table: Dose-response matrix — MMLU/HellaSwag × {10%, 30%, 50%} × {no-filter,
287	    binary, graduated}'
288	  figures_description:
289	  - 'Line plot: contamination dose (x) vs graduated−binary delta (y), 显示近线性增长'
290	  - 'Stacked area chart: dose × 策略, 显示 graduated 在高 dose 下优势扩大'
291	  analysis: 'dose-response 为 C3 提供 nuanced framing: "practical value scales with contamination
292	    prevalence: at moderate levels (30%) benefit is borderline (0.6pp, p=0.08); at
293	    high contamination (50%) it becomes significant (1.1pp, p<0.04)." 比 flat "graduated
294	    is better" 更 honest 也更有学术价值。 50% 是 worst-case，但 web contamination trend 持续上升——graduated
295	    filtering 的价值可能随时间增长。
296	
297	    '
298	- name: LLM zero-shot depth estimation baseline
299	  plan_id: exp-011
300	  description: GPT-4o / Claude 3.5 对 depth 0-4 文本做 zero-shot depth 判断。API cost only,
301	    no GPU。
302	  expected_results:
303	    gpt4o:
304	      binary_accuracy_0v1: 0.72
305	      accuracy_3class: 0.38
306	      accuracy_6class: 0.2
307	      depth_spearman_rho: 0.18
308	      mae: 1.85
309	    claude_3_5:
310	      binary_accuracy_0v1: 0.68
311	      accuracy_3class: 0.36
312	      accuracy_6class: 0.19
313	      depth_spearman_rho: 0.15
314	      mae: 1.92
315	    random_baselines:
316	      accuracy_6class_chance: 0.167
317	      accuracy_3class_chance: 0.333
318	    our_method_reference:
319	      accuracy_6class: 0.42
320	      accuracy_3class: 0.63
321	      depth_spearman_rho: 0.55
322	  result_rationale: 'LLM 在 binary detection (0v1) 有一定能力 (~70%)：人类与合成文本在流畅度、重复性、 generic
323	    phrasing 等维度有 perceptible 差异。但 depth estimation 接近 chance: 代际间差异是 subtle statistical
324	    patterns (surprisal 分布高阶矩、频率分布尾部行为)， 非 LLM prompt 可捕捉的显式质量指标。 3-class accuracy
325	    ~37% ≈ chance (33.3%)，说明即使简化为 3 级任务 LLM 仍无能为力。 Spearman ρ ≈ 0.15-0.18 仅有极弱单调关系。GPT-4o
326	    略优于 Claude (72% vs 68% on 0v1) 可能因训练数据中包含更多 synthetic text artifact 讨论，但差异不显著且与
327	    depth 无关。
328	
329	    '
330	  tables:
331	  - 'Table: LLM zero-shot vs our 15D method — accuracy (6/3-class), MAE, Spearman
332	    ρ'
333	  figures_description:
334	  - 'Confusion matrix heatmaps: GPT-4o / Claude 3.5 zero-shot predictions vs true
335	    depth — 仅 gen-0 row 有对角集中，其余近均匀'
336	  analysis: '强化 C1'' novelty: "State-of-the-art LLMs achieve near-chance on depth
337	    estimation (3-class accuracy 36-38% vs chance 33%), confirming generational depth
338	    is a distributional property requiring specialized measurement, not a surface
339	    quality attribute." 这个 baseline 直接回应 "为什么需要专门方法" 的潜在质疑。
340	
341	    '
342	- name: Binary detector confidence as depth proxy
343	  plan_id: exp-012
344	  description: DivEye / Binoculars confidence score 与 true depth 的 Spearman correlation，验证
345	    binary confidence ≠ depth。
346	  expected_results:
347	    diveye:
348	      binary_auc_0v1: 0.882
349	      spearman_rho_confidence_vs_depth: 0.215
350	      auc_1v2_from_confidence: 0.548
351	      auc_2v3_from_confidence: 0.512
352	    binoculars:
353	      binary_auc_0v1: 0.907
354	      spearman_rho_confidence_vs_depth: 0.192
355	      auc_1v2_from_confidence: 0.534
356	      auc_2v3_from_confidence: 0.508
357	    our_method_reference:
358	      spearman_rho_vs_depth: 0.553
359	      auc_1v2: 0.654
360	      auc_2v3: 0.552
361	  result_rationale: 'Binary detectors 的 confidence 与 depth 有弱正相关 (ρ≈0.19-0.22)： 更深代际文本更"像合成"，confidence
362	    缓慢上升。但远弱于我们的方法 (ρ=0.55)， 因为 binary confidence 主要捕捉 0v1 的大跳变，对 1v2+ 微小差异不敏感—— 这些
363	    detectors 的 decision boundary 在 real/synthetic 边界，不在 gen-1/gen-2 边界。 Binoculars
364	    binary AUC (0.907) > DivEye (0.882) 但 depth ρ 反而更低 (0.192 vs 0.215)—— 更好的 binary
365	    detector 不自动成为更好的 depth estimator，证明二者是不同任务。 1v2 AUC from confidence (0.534-0.548)
366	    远低于我们的 15D features (0.654)。
367	
368	    '
369	  tables:
370	  - 'Table: Binary detector confidence as depth proxy — Spearman ρ, per-pair AUC,
371	    vs 15D method'
372	  figures_description:
373	  - 'Scatter plot: Binoculars confidence vs true depth — gen-0/gen-1 分离明显，gen-1+ 基本平坦'
374	  - 'AUC decay comparison: 15D method vs DivEye/Binoculars confidence 的 per-pair AUC'
375	  analysis: '直接回答审稿人 "为什么不直接用 binary confidence 做 graduated filtering"。 论文写法: "Binary
376	    detection confidence provides a poor depth proxy (ρ ≤ 0.22 vs 0.55), confirming
377	    that depth estimation requires features capturing distributional shifts beyond
378	    the real/synthetic boundary."
379	
380	    '
381	- name: Naturalistic validation on Common Crawl
382	  plan_id: exp-014
383	  description: CC 2025/2026 snapshot 样本 (10K docs) 做 depth 预测，与 AlignScore、vocabulary
384	    richness、self-BLEU、perplexity 做 correlation。
385	  expected_results:
386	    depth_distribution_cc2025:
387	      predicted_gen0_pct: 83.2
388	      predicted_gen1_pct: 11.5
389	      predicted_gen2plus_pct: 5.3
390	    correlation_with_proxies:
391	      spearman_rho_align_score: -0.28
392	      spearman_rho_vocab_richness_ttr: -0.24
393	      spearman_rho_self_bleu: 0.19
394	      spearman_rho_perplexity_gpt2: -0.31
395	    confidence_calibration:
396	      mean_confidence_gen0: 0.78
397	      mean_confidence_gen1: 0.52
398	      mean_confidence_gen2plus: 0.41
399	  result_rationale: 'CC 上 depth 预测分布 (83/12/5) 与当前 web synthetic content 比例估计 (10-20%)
400	    粗略一致。 AlignScore 负相关 (ρ=-0.28)：预测为更深代际的文本事实一致性更差，符合 model collapse 理论。 但相关性偏弱因为:
401	    (1) 无 ground truth depth labels，只能做 proxy correlation； (2) CC "合成文本" 来自多种 LLM/pipeline，与单模型受控实验分布不同；
402	    (3) domain/length/genre 是强混淆变量。 perplexity 相关性稍高 (ρ=-0.31) 因为 synthetic 文本在 GPT-2
403	    下 perplexity 更低 （更接近 LM 的 typical set）。confidence 校准显示模型对 gen-2+ 不确定性更高 (0.41
404	    vs 0.78)， 符合 K*=2 预期——gen-2+ 之间确实难以区分。
405	
406	    '
407	  tables:
408	  - 'Table: Predicted depth distribution on CC 2025 (10K sample)'
409	  - 'Table: Spearman ρ between predicted depth and four independent quality proxies'
410	  figures_description:
411	  - 'Histogram: CC 2025 predicted depth distribution'
412	  - 'Scatter + trend line: predicted depth vs AlignScore, 弱负相关'
413	  analysis: '提供 directional evidence 但非 conclusive proof。定位为 "preliminary ecological
414	    validation"， 承认没有 ground truth。ρ≈0.24-0.31 弱相关在 web data confounders 下是合理的。 主要回应
415	    reviewer concern #3 (ecological validity)，strength 有限——作为 supplementary analysis。
416	
417	    '
418	- name: Learned representation baseline
419	  plan_id: exp-015
420	  description: Frozen Qwen2.5-1.5B last-hidden-state (1536d) + 2-layer MLP vs hand-crafted
421	    15D features。验证 interpretable features 的价值上限。
422	  expected_results:
423	    learned_frozen_mlp:
424	      qwen_rewrite:
425	        accuracy: 0.4785
426	        mae: 0.8512
427	        tau_b: 0.6195
428	        mean_pw_auc: 0.6823
429	        auc_1v2: 0.7342
430	      pythia:
431	        accuracy: 0.4358
432	        mae: 0.9624
433	        tau_b: 0.5412
434	        mean_pw_auc: 0.6498
435	        auc_1v2: 0.6973
436	      olmo:
437	        accuracy: 0.431
438	        mae: 0.9787
439	        tau_b: 0.5318
440	        mean_pw_auc: 0.6425
441	        auc_1v2: 0.6582
442	    handcrafted_15d_reference:
443	      qwen_rewrite:
444	        accuracy: 0.4229
445	        mean_pw_auc: 0.6214
446	        auc_1v2: 0.6955
447	      pythia:
448	        accuracy: 0.3856
449	        mean_pw_auc: 0.6055
450	        auc_1v2: 0.6539
451	      olmo:
452	        accuracy: 0.3822
453	        mean_pw_auc: 0.6015
454	        auc_1v2: 0.6145
455	    delta_accuracy_pp:
456	      qwen_rewrite: 5.56
457	      pythia: 5.02
458	      olmo: 4.88
459	      mean: 5.15
460	    delta_mean_pw_auc_pp:
461	      qwen_rewrite: 6.09
462	      pythia: 4.43
463	      olmo: 4.1
464	      mean: 4.87
465	  result_rationale: 'frozen embedding + MLP 优于 15D hand-crafted ~5pp accuracy / ~4.9pp
466	    mean_pw_auc。 原因: (1) 1536d frozen embeddings 包含 surprisal/diversity/frequency
467	    等 hand-crafted  features 捕捉的信息以及高阶交互和 contextual patterns；(2) MLP 学习非线性组合， 而 LightGBM
468	    虽也非线性但受限于 15d 输入；(3) LM 内部表征隐式编码 generation process artifacts。 但差距是 ~5pp 而非 overwhelming：hand-crafted
469	    features 已捕捉大部分 discriminative signal （~85% of available performance），剩余 ~5pp
470	    来自 high-dimensional interaction effects。 这说明 depth signal 主要是 low-dimensional
471	    统计模式，learned features 的优势在于 residual pattern 捕捉，而非发现全新 signal source。 跨模型一致的 ~5pp
472	    gap 说明这个差距是 structural 的，不是 dataset-specific。
473	
474	    '
475	  tables:
476	  - 'Table: Hand-crafted 15D vs Frozen-LM+MLP — accuracy, MAE, τ_b, mean_pw_auc, AUC₁ᵥ₂
477	    across 3 configs'
478	  figures_description:
479	  - 'Grouped bar chart: accuracy 15D vs learned, per config, 显示一致 ~5pp gap'
480	  - 't-SNE: learned embeddings colored by depth — gen-0/gen-1 boundary 清晰, gen-2+
481	    混合'
482	  analysis: 'median tier 最 uncomfortable 的结果。论文必须诚实报告，但论述: (1) "15D features capture
483	    ~85% of available signal — the gap confirms our features  target the right distributional
484	    properties." (2) "Hand-crafted features remain uniquely valuable for degradation
485	    ordering analysis (§4.3)  and cross-model transfer analysis (§4.2), which require
486	    per-feature interpretability." (3) "This interpretability-performance tradeoff
487	    is central: learned features are stronger  but opaque; hand-crafted features support
488	    the characterization that is the paper''s  primary contribution." 审稿人必问 "why not
489	    learned features" — 回答是贡献在 characterization 不是 SOTA classifier。
490	
491	    '
492	- name: Base vs Instruct model comparison
493	  plan_id: exp-016
494	  description: Qwen2.5-1.5B base (无 instruction tuning) vs Instruct 的 K* 和特征分布差异，continuation
495	    mode, C4 5K docs, depth 0-5。
496	  expected_results:
497	    base_model:
498	      k_star: 1
499	      k_star_note: 'at θ=0.60: CI lower=0.5878 < 0.60 → K*=1; at θ=0.585: K*=2 — threshold-sensitive'
500	      pairwise_auc:
501	        0v1: 0.9923
502	        1v2: 0.5985
503	        2v3: 0.5482
504	        3v4: 0.5265
505	        4v5: 0.5098
506	      pairwise_auc_ci:
507	        1v2_ci_lower: 0.5878
508	        1v2_ci_upper: 0.6092
509	      pairwise_jsd:
510	        0v1: 0.2415
511	        1v2: 0.0042
512	        2v3: 0.0031
513	        3v4: 0.0028
514	        4v5: 0.0024
515	      ordinal_accuracy: 0.362
516	      ordinal_mae: 1.225
517	      top3_features:
518	      - surp_d1_std
519	      - surp_std
520	      - surp_d2_std
521	    instruct_reference:
522	      k_star: 2
523	      auc_1v2: 0.6112
524	      auc_1v2_ci_lower: 0.6015
525	    instruct_minus_base:
526	      auc_1v2_delta_pp: 1.27
527	      auc_0v1_delta_pp: 0.49
528	    feature_ranking_comparison:
529	      spearman_rho_base_vs_instruct: 0.87
530	      shared_top3: true
531	      key_divergence: 'freq_entropy: instruct top-1 → base rank-5'
532	  result_rationale: 'Base model 1v2 AUC (0.5985) 比 Instruct (0.6112) 低 ~1.3pp，CI lower
533	    (0.5878)  在 θ=0.60 下方 → K*=1。 原因: instruction tuning 使模型输出更结构化、更遵循特定 pattern，
534	    这些 pattern 在递归生成中的退化更 systematic 因而更 detectable。 Base model 的 continuation 输出更
535	    diverse/stochastic，代际间 distributional shift  更 diffuse 更难检测。 但差异很小 (1.3pp)：depth
536	    signal 主要来自 iterated generation 的信息损失， 不是 instruction-following artifact。 特征排序高度一致
537	    (ρ=0.87)：surprisal 特征在两种模型中都最 discriminative。 关键差异在 freq_entropy：instruct model
538	    中 rank 1 但 base 中 rank 5， 因为 instruction tuning 使词频更集中（模板化用词），这个 entropy signal
539	    在递归中退化更明显。
540	
541	    '
542	  tables:
543	  - 'Table: Base vs Instruct pairwise AUC 对比, bootstrap CI'
544	  - 'Table: Feature importance ranking comparison (Spearman ρ = 0.87), highlighting
545	    freq_entropy divergence'
546	  figures_description:
547	  - 'AUC decay curve: base vs instruct 并列, 平行衰减但 instruct ~1pp higher'
548	  - 'Feature importance bar chart: base vs instruct side-by-side, freq_entropy 箭头标注'
549	  analysis: 'base model borderline K* 增加 important qualification。论文写法: "K*=2 holds
550	    for instruction-tuned models; base models show marginally weaker signal  (AUC₁ᵥ₂
551	    = 0.60 vs 0.61), with the 0.60 threshold falling within the bootstrap CI. Feature
552	    degradation orderings are highly consistent across variants (ρ = 0.87),  indicating
553	    shared underlying mechanisms." 这个结果实际上 strengthen "systematic characterization"
554	    叙事： 展示 K* 对 model variant 的 sensitivity，证明 fine-grained measurement 的必要性。 作为 §4.1
555	    的子分析呈现。'
556	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49bb9af3-16b3-432c-87c4-fff0cfb697b7",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "1e2feaff-7d7c-40e2-a422-deab1efd4f0a",
  "sourceToolAssistantUUID": "49bb9af3-16b3-432c-87c4-fff0cfb697b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-13T08:54:59.541Z_

<details open><summary>🔧 Tool call — Read · `toolu_013GQe2SVjR41qrnZ7cFecRK`</summary>

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
  "parentUuid": "1e2feaff-7d7c-40e2-a422-deab1efd4f0a",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHcxP6Z5pt3tUxLBo7z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51b70db5-1ea2-4ea9-ab56-35514fe214dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pgc8zeUcjo2gdVwfNe6wpL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 314,
      "cache_read_input_tokens": 39737,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 314
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 39737,
          "cache_creation_input_tokens": 314,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 314,
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

_source line 43 · 2026-05-13T08:55:00.082Z_

<details><summary>↩ Tool result · `toolu_013GQe2SVjR41qrnZ7cFecRK`</summary>

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
  "parentUuid": "51b70db5-1ea2-4ea9-ab56-35514fe214dd",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "1c33c7db-a906-4d71-9a6b-e7c49d08abdd",
  "sourceToolAssistantUUID": "51b70db5-1ea2-4ea9-ab56-35514fe214dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-13T08:55:04.189Z_

Now let me also check the literature map and any other relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c33c7db-a906-4d71-9a6b-e7c49d08abdd",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHdG1F5nwaSApv4CbAV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0da9e8b4-c2f1-4341-9ced-b5dc3d9564ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LH5vZyA2qxuMutqEJdK2DT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29384,
      "cache_read_input_tokens": 40051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29384,
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

_source line 45 · 2026-05-13T08:55:05.180Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NibW25kSjmXwZXQRXE36F5`</summary>

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
  "parentUuid": "0da9e8b4-c2f1-4341-9ced-b5dc3d9564ba",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHdG1F5nwaSApv4CbAV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe13407d-277d-4d9e-a171-417aa16b82b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LH5vZyA2qxuMutqEJdK2DT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29384,
      "cache_read_input_tokens": 40051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29384,
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

_source line 46 · 2026-05-13T08:55:05.198Z_

<details><summary>↩ Tool result · `toolu_01NibW25kSjmXwZXQRXE36F5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/literature_map.yaml\", \"content\": \"papers:\\n  # === Must-Cite ===\\n\\n  - id: drayson2025\\n    title: \\\"Machine-generated text detection prevents language model collapse\\\"\\n    authors: \\\"Drayson, Yilmaz, Lampos\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2502.15654\\\"\\n    code: \\\"https://github.com/GeorgeDrayson/model_collapse\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Binary MGT detection + importance resampling for collapse prevention; our depth estimator generalizes their binary detector to ordinal depth\\\"\\n    cited: false\\n    methodology: >\\n      Binary MGT detector (encoder-only transformer + classification head; best: ModernBERT-150M, AUC .986 in-dist, .943 OOD).\\n      Fine-tuned 5 epochs with label smoothing α=0.1 + temperature scaling.\\n      Sampling Importance Resampling (SIR): w_j = (1-q(x_j))^b / Σ(1-q(x_l))^b, where q(x) = P(machine-generated), b≥1 bias term.\\n      Resample at k=1.5 (50% upsampling). Evaluated on GPT-2 and SmolLM2 (124M–1.7B).\\n    key_findings:\\n      - \\\"SIR filtering not only prevents collapse but improves over human-only training (perplexity -0.85% to -25.65%, diversity +3.44% to +14.62%, MAUVE +8.46% to +20.92%)\\\"\\n      - \\\"ModernBERT achieves best detection (AUC .986 in-dist); optimal threshold 0.8674 on imbalanced data (29% human)\\\"\\n      - \\\"Curated synthetic data has positive value — outperforms oracle (perfect filter) in equal-ratio settings\\\"\\n      - \\\"Only evaluates fine-tuning (not pretraining), models ≤2B, open-ended generation only\\\"\\n    positioning_notes: >\\n      Closest prior work. Their SIR is a special case of our graduated filtering when K*=1 (binary: human vs all synthetic).\\n      We generalize binary→ordinal: estimate depth d∈{0,1,...,K*} and apply depth-graduated weights.\\n      K* tells when ordinal signal adds value over binary. They never discuss ordinal depth or multi-class estimation.\\n      Our C3 claim directly extends their framework: \\\"even coarse 3-class signal yields better calibration at decision boundaries.\\\"\\n\\n  - id: schaeffer2025position\\n    title: \\\"Position: Model Collapse Does Not Mean What You Think\\\"\\n    authors: \\\"Schaeffer, Kazdan, Arulandu, Koyejo\\\"\\n    venue: \\\"ICML 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2503.03150\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"framing-critical\\\"\\n    relevance: \\\"Identifies 8 definitions of model collapse across 3 families; forces us to position K* as discriminability saturation (distribution deformation), not test-loss collapse\\\"\\n    cited: false\\n    methodology: >\\n      Position paper. Surveys model collapse literature and identifies 8 distinct definitions organized in 3 families.\\n      Evaluates each definition against realistic deployment conditions. No experiments—purely analytical/argumentative.\\n    key_findings:\\n      - \\\"8 definitions in 3 families: (A) Population risk degrading [D1: catastrophic increase, D2: any increase, D3: asymptotic divergence]; (B) Distributions deforming [D4: collapsing variance, D5: scaling law change, D6: mode disappearance/entanglement, D7: tail data loss]; (C) Spurious generation [D8: hallucinated data]\\\"\\n      - \\\"Under realistic conditions (data accumulation, growing compute), catastrophic risk divergence (D1-D3) is avoidable\\\"\\n      - \\\"Real harms—tail data loss (D7) and mode entanglement (D6)—have received disproportionately less attention\\\"\\n      - \\\"Recommends researchers explicitly state which definition they study\\\"\\n    positioning_notes: >\\n      K* belongs to Family B (distributions deforming), specifically D4 (collapsing variance) + D6 (mode entanglement).\\n      K* measures when distribution deformation renders generations indistinguishable in feature space.\\n      K* is NOT about population risk (Family A). This distinction is critical for framing:\\n      we contribute a diagnostic for exactly the harms Schaeffer et al. identify as underexplored.\\n      Adopt their taxonomy explicitly in Related Work to anchor K* precisely.\\n\\n  - id: kazdan2025collapse\\n    title: \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\"\\n    authors: \\\"Kazdan, Schaeffer, Dey, Gerstgrasser, Rafailov, Donoho, Koyejo\\\"\\n    venue: \\\"ICML 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2410.16713\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Accumulate vs replace regimes affect contamination dynamics; in accumulate regime K* may shift upward\\\"\\n    cited: false\\n    methodology: >\\n      Formal comparison of 3 data regimes: Replace (train on latest synthetic only; Σ→0 a.s.),\\n      Accumulate (train on all historical data; real fraction→0 but stability holds),\\n      Accumulate-subsample (fixed budget from accumulated pool; intermediate degradation).\\n      Theory: Gaussian setting with closed-form limits. Experiments: multivariate Gaussian, KDE, LLM SFT (Gemma2-2B on HelpSteer2/TinyStories).\\n    key_findings:\\n      - \\\"Replace: covariance collapses to 0 (a.s.), W2 diverges. Collapse inevitable within 5-10 iterations\\\"\\n      - \\\"Accumulate: covariance stabilizes at σ₀²·sin(π/√n)/(π/√n). No collapse even as real data fraction→0\\\"\\n      - \\\"Accumulate-subsample: degradation plateaus rather than diverges\\\"\\n      - \\\"Cardinality of real data matters more than proportion (R²=0.59 vs 0.34)\\\"\\n    positioning_notes: >\\n      Our prompt-chain = replace regime (harshest setting). K*=2 measured under replace conditions.\\n      This makes K*=2 a conservative lower bound: under accumulate regime (more realistic), K* would shift upward.\\n      Strengthens our result: if depth estimation adds value at K*=2 under replace, it adds more under accumulate.\\n      Cite to justify experimental design and contextualize K* as regime-dependent.\\n\\n  - id: shi2025generalization\\n    title: \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\"\\n    authors: \\\"Shi, Wu, Zhang, Zhang, Tao, Qu\\\"\\n    venue: \\\"NeurIPS 2025 Spotlight\\\"\\n    url: \\\"https://arxiv.org/abs/2509.16499\\\"\\n    code: \\\"https://shilianghe007.github.io/model-collapse/\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Generalization-to-memorization transition in iterative retraining parallels our feature-space convergence; entropy decrease over iterations aligns with our depth-discriminative features\\\"\\n    cited: false\\n    methodology: >\\n      Study iterative retraining of diffusion models (DDPM) on CIFAR-10 subsets (1K–32K images).\\n      Generalization Score (GS): avg distance between generated and nearest training image.\\n      Entropy: Kozachenko-Leonenko estimator. Strong correlation: Pearson r=0.91 between entropy and log(GS).\\n      Mitigation: entropy-based data selection (greedy max-NN-distance + threshold-decay filter).\\n    key_findings:\\n      - \\\"GS drops approximately exponentially across iterations; collapse within 5-10 iterations for large datasets\\\"\\n      - \\\"Training data entropy is a direct predictor of generalization capability (r=0.91)\\\"\\n      - \\\"Entropy-based data selection mitigates memorization transition\\\"\\n      - \\\"Diffusion models only; no LLM experiments. No theoretical analysis of WHY entropy collapses\\\"\\n      - \\\"Generated images form tight local clusters while overall variance remains relatively stable\\\"\\n    positioning_notes: >\\n      Parallel phenomenon across modalities: their entropy decline ↔ our JSD decrease (0.27→0.004).\\n      Their \\\"GS drops exponentially\\\" ↔ our feature-space divergence vanishes rapidly → K*=2.\\n      Key distinction: they measure output-distribution entropy; we measure discriminability in feature space.\\n      K* complements their entropy metric: operationalizes \\\"at what depth does entropy decline = indistinguishability?\\\"\\n      Their clustering-while-variance-stable parallels our depth features converging before global statistics.\\n      Cite for cross-modal validation of convergence phenomenon.\\n\\n  # === Should-Cite ===\\n\\n  - id: basani2026diveye\\n    title: \\\"DivEye: Diversity Boosts AI-Generated Text Detection\\\"\\n    authors: \\\"Basani, Chen\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2509.18880\\\"\\n    code: \\\"https://github.com/IBM/diveye\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Surprisal diversity features as potential baseline for depth estimation; zero-shot detector outperforms prior work by 33.2%\\\"\\n    cited: false\\n\\n  - id: amin2025escaping\\n    title: \\\"Escaping Collapse: The Strength of Weak Data for Large Language Model Training\\\"\\n    authors: \\\"Amin et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2502.08924\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Boosting-inspired framework showing weak signal suffices for iterative training; motivates practical utility of imperfect depth estimators\\\"\\n    cited: false\\n\\n  - id: zawalski2026codec\\n    title: \\\"CoDeC: Detecting Data Contamination in LLMs via In-Context Learning\\\"\\n    authors: \\\"Zawalski et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2510.27055\\\"\\n    category: \\\"contamination\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Binary contamination detection via ICL confidence shifts; complementary to our finer-grained depth estimation approach\\\"\\n    cited: false\\n\\n  - id: gambetta2025surplexity\\n    title: \\\"Learning by Surprise: Surplexity for Mitigating Model Collapse\\\"\\n    authors: \\\"Gambetta et al.\\\"\\n    venue: \\\"arXiv preprint 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2410.12341\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Surprise-based collapse metric; surplexity scores as potential feature for depth estimation pipeline and baseline comparison\\\"\\n    cited: false\\n\\n  - id: zhang2024minkpp\\n    title: \\\"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\\\"\\n    authors: \\\"Zhang, Zheng, Gao, Miao\\\"\\n    venue: \\\"EMNLP 2024\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Binary detection baseline; does not distinguish generational depth\\\"\\n    cited: false\\n\\n  - id: shumailov2024collapse\\n    title: \\\"AI models collapse when trained on recursively generated data\\\"\\n    authors: \\\"Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal\\\"\\n    venue: \\\"Nature 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Seminal model collapse result; describes macro phenomenon but provides no detection tool for depth\\\"\\n    cited: false\\n\\n  - id: alemohammad2024selfconsuming\\n    title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n    authors: \\\"Alemohammad, Casco-Rodriguez, Luber, Babaei, Letizia, Bastani, Baraniuk\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Theoretical and empirical analysis of iterative generative training; complements Shumailov with formal convergence analysis\\\"\\n    cited: false\\n\\n  - id: dohmatob2024model\\n    title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n    authors: \\\"Dohmatob, Feng, Yang, Charton, Kempe\\\"\\n    venue: \\\"ICML 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Scaling law perspective on collapse; tail distribution loss aligns with our observed feature convergence\\\"\\n    cited: false\\n\\n  - id: xie2023dsir\\n    title: \\\"Data Selection with Importance Resampling\\\"\\n    authors: \\\"Xie, Santurkar, Ma, Liang\\\"\\n    venue: \\\"ICML 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Distribution-matching data selection baseline; does not estimate recursive depth\\\"\\n    cited: false\\n\\n  - id: tirumala2024d4\\n    title: \\\"D4: Improving LLM Pretraining via Document De-Duplication and Diversification\\\"\\n    authors: \\\"Tirumala, Markosyan, Zettlemoyer, Aghajanyan\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Deduplication + diversification baseline for data curation; orthogonal to depth-based filtering\\\"\\n    cited: false\\n\\n  - id: xie2024doremi\\n    title: \\\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\\\"\\n    authors: \\\"Xie, Pham, Dong, Du, Liu, Lu, Liang, Le, Ma, Yu\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Domain reweighting for pretraining; does not consider generational depth dimension\\\"\\n    cited: false\\n\\n  - id: kirchenbauer2023watermark\\n    title: \\\"A Watermark for Large Language Models\\\"\\n    authors: \\\"Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein\\\"\\n    venue: \\\"ICML 2023\\\"\\n    category: \\\"watermarking\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Provenance tracking via watermarking; complementary approach to depth estimation when watermarks are available\\\"\\n    cited: false\\n\\n  - id: zellers2019grover\\n    title: \\\"Defending Against Neural Fake News\\\"\\n    authors: \\\"Zellers, Holtzman, Rashkin, Bisk, Farhadi, Roesner, Choi\\\"\\n    venue: \\\"NeurIPS 2019\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Early neural text detection; binary classification paradigm that our ordinal approach generalizes\\\"\\n    cited: false\\n\\n  - id: ippolito2020detection\\n    title: \\\"Automatic Detection of Generated Text is Easiest when Humans are Fooled\\\"\\n    authors: \\\"Ippolito, Duckworth, Callison-Burch, Eck\\\"\\n    venue: \\\"ACL 2020\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Binary detection difficulty analysis; does not consider multi-generational depth\\\"\\n    cited: false\\n\", \"total_chars\": 13194, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe13407d-277d-4d9e-a171-417aa16b82b0",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "7175af8a-e271-4351-aea7-dfc6aa8b2786",
  "sourceToolAssistantUUID": "fe13407d-277d-4d9e-a171-417aa16b82b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-13T08:55:05.739Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HdaFrwXWMn6ZgQ3fEEBf8d`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7175af8a-e271-4351-aea7-dfc6aa8b2786",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHdG1F5nwaSApv4CbAV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1654fc69-7737-4d60-983f-47ce984777dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LH5vZyA2qxuMutqEJdK2DT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29384,
      "cache_read_input_tokens": 40051,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 29384
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 216,
          "cache_read_input_tokens": 40051,
          "cache_creation_input_tokens": 29384,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 29384,
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

_source line 48 · 2026-05-13T08:55:05.747Z_

<details><summary>↩ Tool result · `toolu_01HdaFrwXWMn6ZgQ3fEEBf8d`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ROADMAP.md\", \"content\": \"# gen-depth-contamination — Research Dashboard\\n\\n> 最后更新: 2026-05-13 07:50 UTC | 更新原因: exp-006 估算 ~21h（非 72h），deadline 倒排修订，timeline 宽裕\\n\\n## 核心方向\\n递归合成文本的代际深度估计：测量 K*（饱和边界）+ graduated filtering 应用。Route B framing（K* 作为 operational quantity）。Drayson et al. (EMNLP 2025) = closest prior work (binary filtering)，我们是 ordinal 推广。2+1 claim 结构（D012）：C1'(K* characterization) + C3(graduated filtering) + supporting analysis。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（P0 实验收尾）+ 审稿通道已开\\n- **实验**: 8 DONE / 1 RUNNING / 9 planned (18 total)\\n- **K*=2**: 4/4 model configs 确认，bootstrap 95% CI 全 > 0.60\\n- **C1' 子组件**: (a) K*=2 ✅ (b) cross-transfer ✅ (c) degradation ordering ✅ (d) mode analysis ✅\\n- **C3**: exp-006 脚本就绪，等 GPU（D013 fallback 预案已建立）\\n- **paper_framing.md**: D012 重构完成（2+1 结构）\\n- **关键路径**: exp-003 (~8h) → exp-006 (~21h) → analysis + writing → 05-25 ARR\\n\\n## 近期任务\\n- [ ] exp-003 decoding ablation 完成 + 结果收集（RUNNING，~8h 剩余）\\n- [ ] exp-006 启动（exp-003 完成后 GPU **零间隔**切换，~21h，C3 核心证据）\\n- [ ] exp-003 bootstrap CI for 4 decoding configs（CPU，exp-003 完成后）\\n- [ ] exp-005 registry Spearman ρ 补全（Agent CPU 任务，进行中）\\n- [ ] exp-004 cross-scale probe Qwen-7B（P0, 8h budget，exp-006 后或并行）\\n- [ ] 论文写作启动（exp-006 结果后）\\n- [x] exp-006 脚本 + dry-run 就绪（6 策略 × 5 seeds × α sweep）\\n- [x] D012 paper_framing.md 重构完成（2+1 结构）\\n- [x] K*=2 四模型 bootstrap CI (exp-007)\\n- [x] Cross-model transfer 4×4 matrix (exp-013)\\n- [x] C2 qualified claim (D011)\\n- [x] Generation mode effect (exp-017)\\n\\n## GPU 预算\\n- 分配：1×RTX 4090D (cuda:0) on autodl-4090d\\n- 已消耗（实际）：~20h（actual/budget ratio ≈ 40%）\\n- 剩余关键：exp-006 ~21h + exp-004 ~3h (估)\\n- DDL: 05-25 ARR（12 天）\\n\\n## Deadline 倒排（修订）\\n| 日期 | 里程碑 |\\n|------|--------|\\n| ~05-14 | exp-003 完成，exp-006 立即启动 |\\n| ~05-15 | exp-006 完成（~21h 估算） |\\n| ~05-16 | exp-006 分析 + exp-004 (optional) |\\n| ~05-17 | 论文写作启动（Paper Agent） |\\n| ~05-22 | 初稿完成，提交审稿 |\\n| ~05-24 | 修订定稿 |\\n| 05-25 | ARR 提交 |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D013 | 2026-05-13 | C3 exp-006 单点依赖风险评估 + fallback story 预案 | exp-006, exp-003 |\\n| D012 | 2026-05-13 | 论文 claim 重构：4 claims → 2+1 结构（C1' K* characterizat | exp-013, exp-006 |\\n| D011 | 2026-05-13 | D010 修正：C2 从 \\\"supplementary\\\" 升级为 \\\"qualified claim\\\" | exp-005, exp-017 |\\n| D010 | 2026-05-13 | C2 Plan A 否决 → 执行 Plan B：degradation ordering 限定为  | exp-017, exp-005 |\\n| D009 | 2026-05-13 | C2 战略评估：C1 是承重墙，C3 是安全网，C2 是加分项；exp-016 列为场景 B 应急 | exp-005, exp-017, exp-006, exp-016 |\\n| D008 | 2026-05-13 | C2 claim 暂停写入论文——等 exp-017 解耦 generation mode 因素后决 | exp-005, exp-017 |\\n| D007 | 2026-05-13 | Drayson novelty 评估完成：核心 novelty 安全，Story Spine 微调， | exp-006 |\\n| D006 | 2026-05-13 | 回滚 Drayson et al. 引用清理——Reviewer 确认为真实论文 (EMNLP 20 | — |\\n| D005 | 2026-05-13 | Dream 分析完成：proceed with P0, 整合 8 项确认行动到 framing/pl | exp-006, exp-007, exp-015 |\\n| D004 | 2026-05-12 | Reviewer 审查后修正：C1 区分 K*_empirical vs K*_theory；exp | — |\\n\\n\\n\\n\", \"total_chars\": 2847, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1654fc69-7737-4d60-983f-47ce984777dc",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "0667e5b5-c6f9-4f8a-b067-d939934fc4f6",
  "sourceToolAssistantUUID": "1654fc69-7737-4d60-983f-47ce984777dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-13T08:55:10.364Z_

Now I have a comprehensive understanding of the paper, the experimental pipeline, the design decisions, and the internal deliberations. Let me also check the discrepancy between the best and median dream reports on key experiments, particularly exp-015 (learned representations) where the two versions diverge dramatically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0667e5b5-c6f9-4f8a-b067-d939934fc4f6",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHdgSB8obcxNEGt5Xrn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4796ca0f-a68e-42b7-98bb-38239c30b4ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DkVuZaGUG2y9mdd2RruiNb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6870,
      "cache_read_input_tokens": 69435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6870,
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

_source line 50 · 2026-05-13T08:55:11.357Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HV3A7ENG7rkhnD7PFqU6aR`</summary>

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
  "parentUuid": "4796ca0f-a68e-42b7-98bb-38239c30b4ca",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHdgSB8obcxNEGt5Xrn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25cfa71f-95e2-4fab-b15b-71e4cfe12bdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DkVuZaGUG2y9mdd2RruiNb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6870,
      "cache_read_input_tokens": 69435,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6870
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 69435,
          "cache_creation_input_tokens": 6870,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6870,
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

_source line 51 · 2026-05-13T08:55:11.630Z_

<details><summary>↩ Tool result · `toolu_01HV3A7ENG7rkhnD7PFqU6aR`</summary>

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
  "parentUuid": "25cfa71f-95e2-4fab-b15b-71e4cfe12bdd",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "5bdc7265-d4fb-4a82-873d-2a971b4c471b",
  "sourceToolAssistantUUID": "25cfa71f-95e2-4fab-b15b-71e4cfe12bdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-13T08:55:15.842Z_

Now I have a thorough understanding of both dream papers (best and median scenarios), the project's internal decision history, and all experimental context. Let me now load the submission tool and write the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bdc7265-d4fb-4a82-873d-2a971b4c471b",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHe7M81zSvce2UqdwtS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "089ff7fe-a7f3-4a91-b1b0-91b14264561a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWzwhYDHaQooMTMyfSUVNp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11052,
      "cache_read_input_tokens": 76305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11052,
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

_source line 53 · 2026-05-13T08:55:16.872Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CFhZAMoAtk9JL4cghp7uLk`</summary>

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
  "parentUuid": "089ff7fe-a7f3-4a91-b1b0-91b14264561a",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHe7M81zSvce2UqdwtS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ff3a699-3704-4580-b0b6-e40bc6b08e92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWzwhYDHaQooMTMyfSUVNp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11052,
      "cache_read_input_tokens": 76305,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11052
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 76305,
          "cache_creation_input_tokens": 11052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11052,
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

_source line 54 · 2026-05-13T08:55:16.876Z_

<details><summary>↩ Tool result · `toolu_01CFhZAMoAtk9JL4cghp7uLk`</summary>

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
  "parentUuid": "3ff3a699-3704-4580-b0b6-e40bc6b08e92",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "ab623cf8-8d73-4517-81c0-39f46b8faf73",
  "sourceToolAssistantUUID": "3ff3a699-3704-4580-b0b6-e40bc6b08e92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-13T08:55:20.811Z_



Now I have all the information needed. Let me construct the review. I'm reviewing the **median** tier paper, which represents the most likely outcome scenario.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab623cf8-8d73-4517-81c0-39f46b8faf73",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHeWLysy6EPHVck2YdT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2ce184e-f83e-4c31-bd42-d052e47aafc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GGhp4nNNnFr5RfbcZu79UG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 87357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 709,
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

_source line 56 · 2026-05-13T08:57:17.756Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01SDMVGyccXxEiLjygKvfQ1G`</summary>

```json
{
  "project": "gen-depth-contamination",
  "tier": "median",
  "dream_id": "dream_20260513T080728",
  "overall_score": "Weak Reject (3)",
  "report": "# Review Report — R1 (Methods and Experiments)\n\n**Paper:** \"Measuring the Generational Discrimination Boundary in Recursively Contaminated Text\"\n\n---\n\n## 1. Summary\n\nThis paper formalizes recursive text generation as an iterated lossy channel, invokes the Data Processing Inequality to argue that a finite \"generational discrimination boundary\" K* must exist, and empirically measures K*=2 at the 1.5B parameter scale under nucleus sampling. A 15D hand-crafted feature set with a LightGBM ordinal classifier is used across three model families and two generation modes. The paper also demonstrates that K*-aware graduated filtering yields modest improvements over binary filtering on downstream benchmarks, though general-purpose data selection (DSIR) achieves comparable results.\n\n---\n\n## 2. Strengths\n\n**S1. Well-defined problem formulation.** The concept of K* as an operational quantity — the deepest generation at which adjacent depths remain distinguishable — is clean, intuitive, and novel. Framing recursive generation as an iterated lossy channel and invoking DPI to guarantee convergence is elegant and provides theoretical grounding that is rare in empirical detection work.\n\n**S2. Comprehensive characterization matrix.** The paper covers an impressive experimental matrix: 4 model configurations, cross-scale (1.5B vs 7B), base vs instruct, cross-model transfer (Pythia/OLMo), and generation mode analysis. This breadth is above average for a characterization paper and addresses many obvious confounds preemptively.\n\n**S3. Honest reporting of weak and negative results.** The paper does not oversell. The graduated filtering advantage is reported as \"modest\" (+0.6pp at 30%, p=0.08), DSIR is acknowledged as achieving comparable performance without depth estimation, and the base model's borderline K* is transparently reported with its threshold sensitivity. This intellectual honesty is commendable and increases trust in the results.\n\n**S4. Useful supporting analyses.** The binary-confidence-as-depth-proxy analysis (Table 9) and the LLM zero-shot baseline (Table 8) effectively establish that depth estimation is a genuinely different task from binary detection and cannot be solved trivially. These analyses strengthen the paper's motivation.\n\n**S5. Retrain-chain ecological validity.** Including a retrain-chain experiment (Table 7), even with its limitations, demonstrates awareness of the gap between controlled prompt-chains and real-world recursive contamination. The K*=2 preservation with attenuated signal is a reassuring result.\n\n---\n\n## 3. Weaknesses\n\n**W1. The DPI theoretical framing is invoked but never truly leveraged (Major).** The paper applies DPI to the sequence of distributions P_0, P_1, ..., P_k, concluding that D(P_k || P_{k+1}) is monotonically non-increasing and therefore a finite K* exists. This is correct but nearly trivial — it is a direct restatement of the data processing inequality for Markov chains and provides no quantitative prediction about K*. The theory does not predict K*=2, does not predict how K* depends on model scale or decoding parameters, and does not constrain the rate of convergence. Any positive empirical finding would be \"consistent with DPI.\" The theoretical contribution is therefore a framing device rather than a substantive result, yet it is positioned as a core contribution. The paper should be more explicit that the theory provides existence only, not characterization.\n\n**W2. The theta=0.60 threshold is arbitrary and load-bearing (Major).** K* is defined as the largest k where AUC(k, k+1) > theta with theta=0.60. This threshold is the single most consequential design choice in the paper — it determines K*=2 vs K*=1 for the base model (Table 3: AUC=0.599, CI [.588, .609]), and it renders K* a binary output of a continuous quantity (pairwise AUC). Yet the choice receives only a parenthetical justification (\"moderate discriminability above the 0.50 chance level\"). No sensitivity analysis over theta is provided. At theta=0.585, the base model also achieves K*=2 (as the paper's own footnote admits). At theta=0.62, several instruct configurations might yield K*=1. The headline finding \"K*=2 across all configurations\" is entirely an artifact of where this line is drawn. The paper should either (a) report K* as a function of theta, (b) provide principled justification for theta=0.60 (e.g., statistical power analysis, or connection to downstream utility), or (c) abandon the discretized K* framing and report continuous pairwise AUC curves as the primary result.\n\n**W3. Learned features outperform 15D by ~5pp consistently, undermining the feature engineering narrative (Major).** Table 10 shows frozen LM embeddings + MLP outperform hand-crafted features by approximately 5pp in accuracy and 4.9pp in mean pairwise AUC across all three generator configurations. The paper argues this is acceptable because hand-crafted features support interpretability and degradation ordering analysis. However, the ~5pp gap is substantial — it represents roughly 15% of the available discriminative signal that is systematically missed. More critically, the gap raises the question of whether K*=2 is a property of recursive text or a ceiling of the 15D feature set. With learned features achieving AUC_1v2 = 0.734 for Qwen-rewrite (vs 0.696 for 15D), would a better feature set push K* to 3? The paper acknowledges this possibility in passing (K*_empirical <= K*_theory) but does not report K* under learned features, which is a significant omission. If K*=3 under learned features, the paper's headline finding changes fundamentally.\n\n**W4. Graduated filtering results are borderline and DSIR matches without depth estimation (Major).** The downstream evaluation (Table 4) is the paper's practical contribution, but the results undermine the practical narrative:\n- Graduated vs binary: +0.6pp MMLU (p=0.072), +0.6pp HellaSwag (p=0.085) — neither reaches p<0.05.\n- DSIR matches graduated filtering within 0.2pp on both benchmarks, without any depth estimation.\n- Only at the extreme 50% contamination level does graduated filtering become significant (+1.1pp, p=0.038).\nThe paper is honest about this, but the conclusion — that \"the primary value of K* measurement lies in scientific characterization rather than direct engineering advantage\" — effectively concedes that the application contribution (C3) is null. A characterization paper can be valuable, but the paper still allocates substantial real estate (Section 5) to an application that does not work convincingly.\n\n**W5. Statistical power is concerning throughout (Moderate).** Five random seeds yield 4 degrees of freedom for paired t-tests. For the observed effect sizes (0.6pp with std ~0.3), the statistical power is approximately 0.45 — meaning there is a >50% chance of failing to detect a true effect of this magnitude. The 7B cross-scale experiment uses only 1K documents (vs 5K for 1.5B), producing wide CIs (±0.023 on 1v2 AUC) that render the p=0.18 non-significance largely uninformative — the experiment is simply underpowered. The paper should report power analyses or acknowledge that several null results may reflect insufficient sample size rather than true absence of effect.\n\n**W6. Ecological validity of the retrain-chain is limited (Moderate).** The retrain-chain uses LoRA rank=16, which modifies <0.2% of model parameters per iteration. Real-world model collapse involves full pretraining on mixed corpora accumulated over time, a fundamentally different regime. LoRA fine-tuning produces conservative distributional shifts by construction (low-rank constraint preserves most of the original model). The paper acknowledges this as a limitation but still titles the section \"Ecological Validity\" — the experiment validates prompt-chain as a proxy for LoRA-retrain-chain, but neither is ecologically valid for the real-world phenomenon described in the introduction.\n\n**W7. Single corpus, single domain (Moderate).** All experiments use C4 documents. The paper does not evaluate domain sensitivity — whether K* varies across news, scientific text, code, or dialogue. The Common Crawl validation (Table 11) uses the same classifier without adaptation and provides only weak correlations (|rho| < 0.35) with quality proxies. Given the paper's claim that K*=2 is a general property, the single-domain evaluation is a significant gap.\n\n---\n\n## 4. Detailed Comments\n\n### 4.1 Soundness of the DPI-Based Theoretical Framing\n\nThe application of DPI (Eq. 1) to the Markov chain P_0 -> P_1 -> ... -> P_k is mathematically correct. However, several issues arise:\n\n(a) The paper states D(P_k || P_{k+1}) is \"monotonically non-increasing\" — this holds for D(P_0 || P_k) or for I(X; Y_k), but it does NOT automatically hold for D(P_k || P_{k+1}) as written. The divergence between adjacent distributions in a Markov chain is not guaranteed to be monotonically decreasing by DPI alone. Consider: if the channel has a periodic component, D(P_k || P_{k+1}) could oscillate even as the overall information decays. The claim requires the additional assumption that the channel is homogeneous (same G applied at each step) AND that the Markov chain converges to a unique stationary distribution. The paper should state these assumptions explicitly.\n\n(b) The convergence of D(P_k || P_{k+1}) to zero does not imply the existence of a finite K* in the empirical sense. It implies an asymptotic limit. K* as operationalized is a thresholded version of a continuously decaying quantity — DPI guarantees the decay but not the specific rate or where it crosses theta=0.60.\n\n(c) The relationship K*_empirical <= K*_theory is stated but not exploited. How tight is this bound? If K*_theory = 10 but K*_empirical = 2, the practical implications differ vastly from K*_theory = 3 and K*_empirical = 2.\n\n### 4.2 Appropriateness of theta=0.60 and K* Operationalization\n\nThe threshold theta=0.60 is the most consequential arbitrary choice in the paper. It determines:\n- Whether K*=1 or K*=2 for the base model (AUC=0.599)\n- Whether the Qwen-cont configuration is \"clearly\" K*=2 (CI lower = 0.602, margin of 0.002)\n\nThe CI-based operationalization (requiring CI lower > theta for k-1,k and CI upper < theta for k,k+1) is reasonable as a statistical procedure. However, the results are extremely sensitive to theta:\n- At theta=0.58: all configurations yield K*=2 (including base model)\n- At theta=0.60: base model yields K*=1, Qwen-cont is borderline\n- At theta=0.62: potentially multiple configurations yield K*=1\n\nReporting K* as a function of theta (even in an appendix) would substantially increase the paper's robustness.\n\n### 4.3 Statistical Rigor\n\nPositives:\n- Bootstrap 95% CIs with 10K resamples on pairwise AUC — appropriate\n- Permutation tests for K* significance (p < 0.002 reported)\n- Paired t-tests for downstream comparisons (5 seeds)\n\nConcerns:\n- 5 seeds is the bare minimum for paired t-tests (4 df). The paper's key claim (graduated vs binary) has p=0.072 and p=0.085 — both fail conventional significance thresholds. With 10 seeds, these might become significant (or not). The current result is simply inconclusive.\n- The 7B experiment's 1K documents (vs 5K) is acknowledged but not addressed with a power analysis. The p=0.18 non-significance should not be interpreted as \"K* is stable across scales\" — it is equally consistent with K* increasing at 7B but the experiment being underpowered to detect it.\n- No correction for multiple comparisons across the many pairwise AUC tests, CI boundaries, and hypothesis tests. Given the number of tests, some false positives are expected.\n\n### 4.4 Feature Engineering Choices\n\nThe 15D feature set (surprisal statistics, lexical diversity, structural) is well-motivated and covers the expected dimensions of recursive degradation. The degradation ordering analysis (Section 4.3) identifying surp_d1_std as the top discriminative feature is a genuine insight.\n\nHowever, the ~5pp gap to learned features (Table 10) is not merely an interpretability tradeoff — it suggests the 15D features miss systematic patterns. The paper claims \"15D features capture approximately 85% of the available discriminative signal.\" This framing is optimistic: 85% of what metric? If measured by accuracy, 0.423/0.479 = 88%. If by AUC_1v2, 0.696/0.734 = 95%. If by the gap above chance (AUC=0.5), then (0.696-0.5)/(0.734-0.5) = 84%. The \"85%\" claim depends on the denominator.\n\nMore importantly, reporting K* under learned features is essential. If learned features push 2v3 AUC above 0.60, K*=3 and the paper's headline changes.\n\n### 4.5 Experimental Coverage and Controls\n\nStrong coverage:\n- 4 model configs (Qwen-rewrite, Qwen-cont, Pythia, OLMo)\n- Cross-model transfer matrix\n- Base vs instruct comparison\n- Retrain-chain validation\n- LLM zero-shot and binary detector baselines\n\nMissing controls:\n- No domain sensitivity analysis (C4 only)\n- No analysis of document length effects on K* (longer documents should be more discriminable)\n- No human evaluation or calibration against human depth perception\n- Decoding ablation is mentioned in the paper structure description but Table 1 shows only 4 model configs with fixed nucleus p=0.95, T=1.0 — the decoding ablation appears absent from the median paper\n- No analysis of the classifier's calibration (does predicted depth=1 actually correspond to gen-1 text?)\n\n### 4.6 Retrain-Chain Ecological Validity\n\nThe LoRA retrain-chain (Table 7) preserves K*=2 with 3.3pp attenuation on AUC_1v2. The feature ranking correlation (rho=0.78) with 2/3 top features shared is reassuring. However:\n- LoRA rank=16 is extremely conservative. Real-world model collapse involves full pretraining.\n- Only one model (Pythia-1.4B) is tested in retrain mode.\n- The \"retrain\" involves fine-tuning on 5K generated documents — far from realistic pre-training scale.\n\n### 4.7 Downstream Filtering Evaluation Methodology\n\nThe filtering evaluation is well-designed in principle (6 strategies, 5 seeds, paired comparison), but:\n- The evaluation uses continued pretraining, not pretraining from scratch. The contamination is therefore layered on top of an already-trained model, which may understate or overstate the real effect.\n- MMLU and HellaSwag are the only downstream benchmarks. More diverse evaluation (coding, reasoning, factuality) would strengthen the claim.\n- The alpha sensitivity sweep (Table 5) is done only at 30% contamination. The optimal alpha likely varies with contamination level.\n- The \"clean baseline\" is 46.5 MMLU — graduated filtering recovers to 46.1 (-0.4pp), which is close but not tested for statistical significance against clean.\n\n---\n\n## 5. Questions for Authors\n\n**Q1.** What is K* when measured using learned features (Table 10) instead of the 15D hand-crafted set? Specifically, does AUC_2v3 under learned features exceed 0.60 for any configuration? If so, the paper's headline K*=2 result is an artifact of feature choice, not a property of recursive text.\n\n**Q2.** Can you provide K* as a function of theta for at least 3-4 threshold values (e.g., 0.55, 0.58, 0.60, 0.62, 0.65)? The current results are extremely sensitive to the threshold, and the base model's K* flips between 1 and 2 at the exact chosen value.\n\n**Q3.** The DPI derivation claims D(P_k || P_{k+1}) is monotonically non-increasing (Eq. 1). This requires the Markov chain to converge and the channel to be applied homogeneously. Can you clarify the assumptions under which this holds? In practice, each generation may use slightly different prompts or contexts, breaking strict homogeneity.\n\n**Q4.** The graduated filtering advantage at 30% contamination (the most realistic scenario) is +0.6pp with p=0.072 — not significant at conventional levels. Have you considered increasing to 10+ seeds to resolve whether this effect is real? A power analysis would clarify whether 5 seeds can detect a 0.6pp effect with the observed variance.\n\n**Q5.** Why is the decoding strategy ablation (which appears in the best-case version of the paper with greedy K*=1 and T=1.2 K*=3) absent from the main characterization? This experiment, if it exists, would substantially strengthen the paper by showing K* is a controllable property of the channel rather than a fixed artifact.\n\n---\n\n## 6. Score and Confidence\n\n**Score: 3 (Weak Reject)**\n\n**Confidence: 4 (High)**\n\n**Justification:** The paper introduces a clean and novel concept (K*) with solid theoretical motivation and a thorough experimental matrix. The honesty in reporting weak results is appreciated. However, several issues prevent acceptance at a top venue:\n\n(1) The headline K*=2 finding is sensitive to an arbitrary threshold (W2) and may be an artifact of the feature set rather than the data (W3 — learned features consistently outperform by ~5pp, and K* under learned features is not reported).\n\n(2) The practical contribution (graduated filtering, C3) fails to reach statistical significance at realistic contamination levels (W4), and DSIR matches it without depth estimation.\n\n(3) The theoretical contribution (DPI) is correct but provides only a trivial existence result that does not constrain or predict the empirical findings (W1).\n\n(4) Statistical power is insufficient for several key claims — the 7B comparison and the graduated filtering advantage are both underpowered (W5).\n\nThe paper would benefit from: (a) reporting K* under learned features, (b) providing theta sensitivity analysis, (c) including the decoding ablation if available, and (d) either increasing seeds for the filtering experiment or explicitly acknowledging the result as inconclusive. In its current form, the characterization contribution (C1) is borderline sufficient for a Findings paper, but the application contribution (C3) does not add meaningfully, and the theoretical contribution (DPI) is too thin. With the suggested revisions, the paper could reach Weak Accept territory.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2ce184e-f83e-4c31-bd42-d052e47aafc4",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHeWLysy6EPHVck2YdT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a2cd741-fffc-4d95-92db-1a1f9d525711",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GGhp4nNNnFr5RfbcZu79UG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 87357,
      "output_tokens": 4807,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 709
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4807,
          "cache_read_input_tokens": 87357,
          "cache_creation_input_tokens": 709,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 709,
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

_source line 57 · 2026-05-13T08:57:21.094Z_

<details><summary>↩ Tool result · `toolu_01SDMVGyccXxEiLjygKvfQ1G`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260513T080728/median/review_report.md\", \"dream_id\": \"dream_20260513T080728\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a2cd741-fffc-4d95-92db-1a1f9d525711",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a67ad696e7191e92d",
  "type": "user",
  "uuid": "70f42057-f8e6-4145-8aae-d6c8f27ea02d",
  "sourceToolAssistantUUID": "3a2cd741-fffc-4d95-92db-1a1f9d525711",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-13T08:57:32.694Z_

Review submitted. Here is a summary of the key findings:

**Score: 3 (Weak Reject) | Confidence: 4 (High)**

The review identifies four major weaknesses and three moderate ones:

**Major issues:**
1. **DPI theory is a framing device, not a substantive contribution** -- it provides existence of K* but no quantitative predictions. Any positive result would be "consistent with DPI."
2. **The theta=0.60 threshold is arbitrary and load-bearing** -- the base model's K* flips between 1 and 2 at exactly this value (AUC=0.599), and Qwen-cont's CI lower is only 0.002 above threshold. No sensitivity analysis over theta is provided.
3. **Learned features outperform 15D by ~5pp consistently** -- K* under learned features is never reported. If learned features push AUC_2v3 above 0.60, the headline K*=2 is an artifact of the feature set, not a property of recursive text.
4. **Graduated filtering fails significance at realistic contamination** -- +0.6pp at 30% with p=0.072; DSIR matches without depth estimation. The application claim (C3) is effectively null.

**Moderate issues:** Low statistical power (5 seeds, 1K docs for 7B), limited ecological validity of LoRA retrain-chain, single-domain evaluation (C4 only).

**Strengths acknowledged:** Novel problem formulation, comprehensive experimental matrix, commendable honesty in reporting weak results, useful supporting analyses (binary-confidence proxy, LLM zero-shot baseline).

**Critical questions:** (1) What is K* under learned features? (2) K* as a function of theta? (3) DPI assumptions on channel homogeneity? (4) Power analysis for the filtering experiment? (5) Where is the decoding ablation that appears in the best-case paper?

The review is saved at `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260513T080728/median/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70f42057-f8e6-4145-8aae-d6c8f27ea02d",
  "isSidechain": true,
  "agentId": "a67ad696e7191e92d",
  "requestId": "req_011CazHoeuRxW8878yRoaorv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1553e93d-fbc3-403e-8ecd-286d36f01584",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DLDMNZYKsEj9JsUVyhPGzv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4937,
      "cache_read_input_tokens": 88066,
      "output_tokens": 509,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4937
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 509,
          "cache_read_input_tokens": 88066,
          "cache_creation_input_tokens": 4937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4937,
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
