# Research conversation: You are Reviewer R2 for a top ML venue review. Your focus area is **Novelty and Related Work**. Review the paper below u

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a27710763487a3e39.jsonl`
- **Structured JSON:** [`ee38e8f1b5c38687df89.json`](../../sessions/ee/ee38e8f1b5c38687df89.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

40 recorded events

### User

_source line 1 · 2026-05-14T17:15:49.593Z_

You are Reviewer R2 for a top ML venue review. Your focus area is **Novelty and Related Work**. Review the paper below using a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Acceptance rate ~25%.

## Paper Summary
Title: "Why Hard Negative Mining Strategies Don't Differentiate for Code Retrieval at Scale"
- A negative-result paper comparing 4 hard negative mining strategies (random, embedding-distance, dataflow-aware, BM25) for contrastive code retrieval
- 2 decoder-only encoders: Qwen2.5-Coder-3B and StarCoder2-3B  
- 9 seeds per condition at full scale (~44K training instances from SWE-smith)
- Central finding: no strategy outperforms random at scale
- Mechanistic explanation: fine-tuning as "geometry equalizer" collapses pretrained margin differences by 65-78%
- Scale ablation: mining advantage at 1K (+1.3pp) vanishes monotonically to +0.2pp at 5K
- BM25 ≈ embedding negatives (p > 0.42)
- Pool size sensitivity: strategy rankings unstable (Kendall τ = 0.33)

## Paper Structure
- §1 Introduction: Motivation from CoCoHaNeRe contradiction, 5 contribution claims
- §2 Related Work: Three paragraphs — hard negative mining for retrieval, code retrieval, structure-aware code understanding
- §3 Method: Problem setting (InfoNCE), 4 mining strategies, 2 encoders, training protocol
- §4 Experiments: 9 subsections covering main results, BM25 comparison, SWE-bench, RepoBench-R, stratified analysis, pool sensitivity, scale effects, failure analysis, geometry convergence
- §5 Discussion: Why strategies converge, BM25-proxy debate, training-time vs inference-time structure, practical recommendations, limitations
- §6 Conclusion
- Appendices A-E: Temperature, dynamic mining, hop count, fusion head, distance weighting ablations
- References: Only 4 cited works ([1] SWE-bench, [2] ANCE, [3] DPR, [4] RepoBench)

## Key Claims
1. No strategy differentiates at scale
2. Representation geometry convergence explains why
3. Scale substitutes for curation
4. BM25 ≈ embedding negatives
5. Strategy rankings are unstable across evaluation settings

## Related Work Coverage
The paper mentions: CoCoHaNeRe, ANCE, DPR, GraphCodeBERT, CodeBERT, SweRank, SWE-Fixer, RepoBench, CodexGraph, LocAgent, RANGER, SimCLR (batch size scaling analogy). Only 4 formal references.

## Your Review Task

Evaluate:
1. **Novelty**: Is the negative result itself novel and surprising? Does it advance understanding? Or is it predictable from existing theory (e.g., contrastive learning convergence is well-known)?
2. **Related work completeness**: Are important related works missing? The paper cites only 4 references — is this adequate for a venue submission? What about: curriculum learning for hard negatives, false negative decontamination, in-batch negatives, other code retrieval systems (CodeSearchNet, UniXcoder, CodeT5+), negative mining in NLP (SimCSE, E5)?
3. **Positioning**: Does the paper adequately position itself relative to prior negative results in retrieval? Is the CoCoHaNeRe framing fair and accurate?
4. **Contribution significance**: For a top venue, is "random negatives suffice at scale" a sufficient contribution? Is the geometry convergence explanation novel?
5. **Framing quality**: Is the negative-result framing effective? Could the paper be reframed more compellingly?

Produce a structured review with:
- Summary (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted)
- Questions for authors
- Minor issues
- Score and confidence

Be rigorous. Negative-result papers need especially strong novelty or mechanistic insight to justify acceptance. Report in under 800 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a27710763487a3e39",
  "type": "user",
  "uuid": "1e985998-a68a-4ef9-bbed-cb86874413ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T17:15:49.596Z_

```json
{
  "parentUuid": "1e985998-a68a-4ef9-bbed-cb86874413ac",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
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
  "uuid": "836cf9a5-10a7-410a-827f-b8beb2eeb236",
  "timestamp": "2026-05-14T17:15:49.596Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T17:15:52.259Z_



I'll start by loading the necessary tools to access the project files, then read the paper and related materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "836cf9a5-10a7-410a-827f-b8beb2eeb236",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qdFbRngTMXXqiSjRHL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6427b902-bc97-40e8-bfa8-4b808488ba5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RfLcKXBv3ytWTZ1gJUhsYR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6848,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6848,
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

_source line 4 · 2026-05-14T17:15:53.257Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01T4T8GmD9wzTZbpeEbhjYaT`</summary>

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
  "parentUuid": "6427b902-bc97-40e8-bfa8-4b808488ba5f",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qdFbRngTMXXqiSjRHL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a0be195-a3c1-4ebe-bc35-495fdff51522",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RfLcKXBv3ytWTZ1gJUhsYR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6848,
      "cache_read_input_tokens": 8249,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6848
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 145,
          "cache_read_input_tokens": 8249,
          "cache_creation_input_tokens": 6848,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6848,
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

_source line 5 · 2026-05-14T17:15:53.263Z_

<details><summary>↩ Tool result · `toolu_01T4T8GmD9wzTZbpeEbhjYaT`</summary>

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
  "parentUuid": "8a0be195-a3c1-4ebe-bc35-495fdff51522",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a27710763487a3e39",
  "type": "user",
  "uuid": "09b04269-95f4-46a5-a220-d4a1a1a05168",
  "sourceToolAssistantUUID": "8a0be195-a3c1-4ebe-bc35-495fdff51522",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T17:15:55.822Z_



Let me read the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09b04269-95f4-46a5-a220-d4a1a1a05168",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qdYeM2FVEAoKnfrbTN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be7ea653-b831-4f81-912f-181a4dad326a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfmtrbXWaMw4HbAUuzAu5S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 15097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2019,
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

_source line 7 · 2026-05-14T17:15:56.836Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TT2UsEvHVasKG7G33qmgMN`</summary>

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
  "parentUuid": "be7ea653-b831-4f81-912f-181a4dad326a",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qdYeM2FVEAoKnfrbTN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dee12899-1144-4899-808b-9f727346916d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfmtrbXWaMw4HbAUuzAu5S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 15097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2019,
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

_source line 8 · 2026-05-14T17:15:56.858Z_

<details><summary>↩ Tool result · `toolu_01TT2UsEvHVasKG7G33qmgMN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| m2_full_starcoder | Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent). | — | — | — |\\n| m1_reextract_v2 | M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 | — | — | — |\\n| m2_full_qwen | Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018. | — | — | — |\\n\\n## 待处理\\n- plan_015_dynamic（排队等待 GPU）\\n- plan_018_bm25: BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。（排队等待 GPU）\\n\\n## 近期结论\\n- **neg_difficulty_analysis** (success): Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\\n  [neg_difficulty_margin_comparison](/api/workspace-files/projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_margin_comparison_meta.txt)\\n- **m1_reextract** (failed): M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 ← 基于 m1_extraction\\n- **m1_extraction** (success): —\\n\\n## 趋势\\n成功 10 / 负向 2 / 失败 2 / 共 28\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-42106: 无 GPU 信息\\n\\n## 告警\\n- p2b-smoke-test: 已被终止 — unknown\\n- p2b-smoke2: 已被终止 — unknown\\n- p2b-smoke3: 已被终止 — unknown\\n- p2b-smoke4: 已被终止 — unknown\\n- p2b-smoke5: 已被终止 — unknown\\n- p2b-smoke6: 已被终止 — unknown\\n- p2b-smoke7: 已被终止 — unknown\\n- p2b-smoke8: 已被终止 — unknown\\n- p2b-all-9runs: 已被终止 — unknown\\n- mvp_p2b_contrastive_training: 已被终止 — unknown\\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\\n- p2b_eval_all: 已被终止 — unknown\\n- m2_early_pilot: 已被终止 — unknown\\n- m2_early_pilot_v2: 训练失败 — unknown\\n- m2_early_pilot_v3: 已被终止 — unknown\\n- m1_reextract: 训练失败 — unknown\\n\", \"total_chars\": 2314, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dee12899-1144-4899-808b-9f727346916d",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a27710763487a3e39",
  "type": "user",
  "uuid": "204ab373-186b-479b-9bd2-111ade467bb3",
  "sourceToolAssistantUUID": "dee12899-1144-4899-808b-9f727346916d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T17:15:57.733Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Xi2kySMRcq2dLpZzd4V5FW`</summary>

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
  "parentUuid": "204ab373-186b-479b-9bd2-111ade467bb3",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qdYeM2FVEAoKnfrbTN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ecaf3d4-607c-485a-84e0-9a0560c3ee03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfmtrbXWaMw4HbAUuzAu5S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 15097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2019,
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

_source line 10 · 2026-05-14T17:15:57.743Z_

<details><summary>↩ Tool result · `toolu_01Xi2kySMRcq2dLpZzd4V5FW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-12\\n# 说明: 只收录项目文件中已引用的 + 确定存在的知名论文。不确定的信息标注\\\"需验证\\\"。\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline  # StructFuse 的评估基准\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Karthik Narasimhan, Ofir Press\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: building-block  # StructFuse 用其 repo 做数据提取\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n        note: \\\"需验证 venue（可能已投稿会议）\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务，StructFuse 可用于评估。\\\"\\n        note: \\\"需验证年份和 venue\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及代码领域的对比学习\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oğuz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式，是 StructFuse 对比训练的方法论基础。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，是 StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"SimCLR: A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Mining Hard Negatives with Curriculum for Dense Retrieval\\\"\\n        authors: \\\"需验证\\\"\\n        venue: \\\"需验证\\\"\\n        year: \\\"需验证\\\"\\n        relation: background\\n        summary: \\\"课程学习式 hard negative 挖掘，从易到难训练检索器。\\\"\\n        note: \\\"需验证完整信息\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block  # StructFuse 核心组件\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n        note: \\\"需验证作者和 venue\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: EMNLP (Findings)\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: background\\n        summary: \\\"大规模开源代码 LLM，广泛用于代码嵌入的 backbone。\\\"\\n        note: \\\"需验证 venue（可能是 arXiv 或其他）\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Qwen Team (Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block  # StructFuse 用 Qwen2.5-Coder-3B 做检索器\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n        note: \\\"需验证确切标题和年份\\\"\\n\\n      - title: \\\"Contrastive Learning for Source Code with Structural and Functional Properties\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: ACL (Findings)\\n        year: 2022\\n        relation: background\\n        summary: \\\"代码对比学习中利用结构/功能属性构建正负样本对。\\\"\\n        note: \\\"需验证作者和 venue\\\"\\n\\n      - title: \\\"BM25\\\"\\n        authors: \\\"Stephen Robertson, Hugo Zaragoza\\\"\\n        venue: \\\"Foundations and Trends in Information Retrieval\\\"\\n        year: 2009\\n        relation: baseline\\n        summary: \\\"经典稀疏检索方法，StructFuse 的 baseline 之一。Phase 2a 实验发现 BM25 在 bug fixing 定位中可能有误导性（负系数）。\\\"\\n\\n# ==========================================================================\\n# 待补充\\n# ==========================================================================\\n# 以下论文可能相关，待确认后补充：\\n# - FAISS (Johnson et al., 2019) — ANN 检索库，StructFuse 评估可能用到\\n# - Tree-sitter — 增量解析器，与 CodeQL 互补\\n# - Aider / Moatless Tools — SWE-bench 上的其他代码检索方法\\n# - CoSQA (Huang et al., 2021) — 代码搜索 QA 数据集\\n# - DeepSeek-Coder — 另一个可能的 backbone 对比\\n\", \"total_chars\": 9647, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ecaf3d4-607c-485a-84e0-9a0560c3ee03",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a27710763487a3e39",
  "type": "user",
  "uuid": "5123a230-ffd6-4bbc-9976-877755f4908e",
  "sourceToolAssistantUUID": "5ecaf3d4-607c-485a-84e0-9a0560c3ee03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T17:15:58.298Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018jPJGDheBLRmXFzPbTXMar`</summary>

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
  "parentUuid": "5123a230-ffd6-4bbc-9976-877755f4908e",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qdYeM2FVEAoKnfrbTN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1e5a16c-0d55-4cbf-8e62-27c9f96213ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfmtrbXWaMw4HbAUuzAu5S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 15097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2019,
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

_source line 12 · 2026-05-14T17:15:58.308Z_

<details><summary>↩ Tool result · `toolu_018jPJGDheBLRmXFzPbTXMar`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \\\"harm\\\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B).\\n\\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\\n\\n- **Headline result template**: \\\"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\\\"\\n\\n## Core Insight\\n\\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, similarity function s, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\\\"\\n- Backup: \\\"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically verify CoCoHaNeRe used BM25-proxy, closing the correction argument | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### In progress:\\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\\n- m1_reextract_v2: expanded extraction for higher coverage\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — closes CoCoHaNeRe correction argument)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\\\"\\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\\n\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the \\\"correcting misconception\\\" narrative loses empirical anchor\\n- Pivot: from \\\"CoCoHaNeRe was wrong because BM25 proxy\\\" → \\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; prior work's negative finding was likely due to uncontrolled variables (data, training protocol), not BM25 specifically\\\"\\n- Paper becomes less dramatic (\\\"correcting\\\" → \\\"clarifying\\\") but still valid as systematic analysis\\n- Claim 1 reworded: \\\"True embedding-distance mining consistently improves code retrieval\\\" (drop the \\\"correcting misconception\\\" framing, keep the empirical finding)\\n- Impact: weaker narrative hook but core experimental contribution survives\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\", \"total_chars\": 11181, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1e5a16c-0d55-4cbf-8e62-27c9f96213ae",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a27710763487a3e39",
  "type": "user",
  "uuid": "11b87219-6f09-4383-8264-5afa01cf8433",
  "sourceToolAssistantUUID": "d1e5a16c-0d55-4cbf-8e62-27c9f96213ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T17:16:01.538Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BCz2Jskgg4snBkYDAEyhhC`</summary>

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
  "parentUuid": "11b87219-6f09-4383-8264-5afa01cf8433",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qdu4gLPLa19D7Ho7TZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74d689a8-1278-47a0-8848-0576be3fa914",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K4M8kwHU3b4BpJQggaN71y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9179,
      "cache_read_input_tokens": 17116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9179,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 14 · 2026-05-14T17:16:01.548Z_

<details><summary>↩ Tool result · `toolu_01BCz2Jskgg4snBkYDAEyhhC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献（全部已验证 2026-05-14）\\n\\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\")\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\\n---\\n\\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\\n\\n**两层重叠率数据（注意区分）**：\\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\\n\\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\\n|------|-------------------|----------------|------------------|\\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\\n\\n**核心修正**：之前基于 87% 预测\\\"Phase 2 中 BM25 R@1 很可能接近 embedding\\\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\\n\\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\", \"total_chars\": 9315, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74d689a8-1278-47a0-8848-0576be3fa914",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a27710763487a3e39",
  "type": "user",
  "uuid": "eeb37b38-ec94-4e87-bca7-c0b247eb83db",
  "sourceToolAssistantUUID": "74d689a8-1278-47a0-8848-0576be3fa914",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T17:16:01.904Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TYaa5Wxzjr1L5XhpxhUrpk`</summary>

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
  "parentUuid": "eeb37b38-ec94-4e87-bca7-c0b247eb83db",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qdu4gLPLa19D7Ho7TZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62437b94-147c-4b53-86ef-6f7c5a336a04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K4M8kwHU3b4BpJQggaN71y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9179,
      "cache_read_input_tokens": 17116,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9179
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 17116,
          "cache_creation_input_tokens": 9179,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9179,
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

_source line 16 · 2026-05-14T17:16:01.913Z_

<details><summary>↩ Tool result · `toolu_01TYaa5Wxzjr1L5XhpxhUrpk`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62437b94-147c-4b53-86ef-6f7c5a336a04",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a27710763487a3e39",
  "type": "user",
  "uuid": "2fdd2c89-7d70-431b-8800-dfcb2518df3c",
  "sourceToolAssistantUUID": "62437b94-147c-4b53-86ef-6f7c5a336a04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-14T17:16:04.161Z_

Now let me look at the artifacts directory for the actual paper draft and any experimental results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fdd2c89-7d70-431b-8800-dfcb2518df3c",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qeAUNqz94L6mByfEKc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7bd8049-f271-4b41-bd43-1af81e82b941",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017JGtDWxinJyJo4WyaJP9aA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3387,
      "cache_read_input_tokens": 26295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3387,
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

_source line 18 · 2026-05-14T17:16:05.526Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FZ7EqM6h2aYnvHS1sZpCLx`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7bd8049-f271-4b41-bd43-1af81e82b941",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qeAUNqz94L6mByfEKc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8bbea2be-e48c-4232-9c39-a46bca9efdbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017JGtDWxinJyJo4WyaJP9aA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3387,
      "cache_read_input_tokens": 26295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3387,
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

_source line 19 · 2026-05-14T17:16:05.554Z_

<details><summary>↩ Tool result · `toolu_01FZ7EqM6h2aYnvHS1sZpCLx`</summary>

```text
artifacts/dream_reports/dream_20260512T204322/best/paper.tex
artifacts/dream_reports/dream_20260512T204322/median/paper.tex
artifacts/dream_reports/dream_20260512T204322/worst/paper.tex
artifacts/dream_reports/dream_20260514T075732/best/paper.tex
artifacts/dream_reports/dream_20260514T075732/median/paper.tex
artifacts/dream_reports/dream_20260514T075732/worst/paper.tex
artifacts/dream_reports/dream_20260514T162530/best/paper.tex
artifacts/dream_reports/dream_20260514T162530/median/paper.tex
artifacts/dream_reports/dream_20260514T162530/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bbea2be-e48c-4232-9c39-a46bca9efdbf",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a27710763487a3e39",
  "type": "user",
  "uuid": "889f348b-92b9-481e-a74f-e272d5f571c3",
  "sourceToolAssistantUUID": "8bbea2be-e48c-4232-9c39-a46bca9efdbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T17:16:06.535Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TWdcjgCxvQgnP9ADVrUE4x`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "889f348b-92b9-481e-a74f-e272d5f571c3",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qeAUNqz94L6mByfEKc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82a85a55-20ff-4150-ac8b-4cdfcd55f43a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017JGtDWxinJyJo4WyaJP9aA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3387,
      "cache_read_input_tokens": 26295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3387,
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

_source line 21 · 2026-05-14T17:16:06.554Z_

<details><summary>↩ Tool result · `toolu_01TWdcjgCxvQgnP9ADVrUE4x`</summary>

```text
artifacts/dream_reports/dream_20260512T204322/best/paper.pdf
artifacts/dream_reports/dream_20260512T204322/median/paper.pdf
artifacts/dream_reports/dream_20260512T204322/worst/paper.pdf
artifacts/dream_reports/dream_20260514T075732/best/paper.pdf
artifacts/dream_reports/dream_20260514T075732/median/paper.pdf
artifacts/dream_reports/dream_20260514T075732/worst/paper.pdf
artifacts/dream_reports/dream_20260514T162530/best/paper.pdf
artifacts/dream_reports/dream_20260514T162530/median/paper.pdf
artifacts/dream_reports/dream_20260514T162530/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82a85a55-20ff-4150-ac8b-4cdfcd55f43a",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a27710763487a3e39",
  "type": "user",
  "uuid": "367cdc9b-aaac-4328-9417-fdf0d15435c5",
  "sourceToolAssistantUUID": "82a85a55-20ff-4150-ac8b-4cdfcd55f43a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T17:16:06.940Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JYFW2oAHsqvLdE7yDMzHRL`</summary>

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
  "parentUuid": "367cdc9b-aaac-4328-9417-fdf0d15435c5",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qeAUNqz94L6mByfEKc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7076eaa0-0c05-4734-b696-9c6635c22c6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017JGtDWxinJyJo4WyaJP9aA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3387,
      "cache_read_input_tokens": 26295,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3387
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 26295,
          "cache_creation_input_tokens": 3387,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3387,
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

_source line 23 · 2026-05-14T17:16:06.956Z_

<details><summary>↩ Tool result · `toolu_01JYFW2oAHsqvLdE7yDMzHRL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/decisions.yaml\", \"content\": \"_next_id: 34\\ndecisions:\\n- id: D001\\n  date: 2026-05-12 09:57 UTC\\n  summary: 'MVP 设计: CodeQL 试点(10 repos) + 迷你对比训练(500 instances) 验证核心假设'\\n  rationale: 13 天 DDL，需要最快速验证核心假设链：(1) CodeQL inter-procedural data-flow 在 Python\\n    repos 上可行（timeout < 30%），(2) data-flow hard negatives 比 random negatives 提升检索\\n    recall。两个 phase 串行，总计约 1 天。通过后立即进入全量数据提取和训练。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-12 10:01 UTC\\n  summary: '采纳 Reviewer 反馈: MVP Phase 2 增加线性分类器 proxy 验证 + 3-seed 训练 + 显式 kill criteria'\\n  rationale: 'Reviewer 指出 Phase 2 原方案（500 instances, ~100 held-out, 2pp gate）统计效力不足，2pp\\n    差异在随机噪声范围内。增加: (1) Phase 2a 线性分类器 proxy 验证解耦特征质量与训练策略；(2) 3-seed 训练要求 ≥2/3 seed\\n    提升；(3) 每个 phase 的 fail→kill/fallback 路径。防止 13 天 DDL 下的沉没成本陷阱。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-12 10:02 UTC\\n  summary: 'H2 验证并入 Phase 1: 提取后立即统计 data-flow 连通文件 vs 不连通文件的 gold patch 覆盖率差异'\\n  rationale: Reviewer 指出 H2（特征区分度）在原 MVP 中无独立验证，Phase 2 失败时无法区分是 H2 还是 H3 问题。零成本 sanity\\n    check（统计连通/不连通文件的 gold patch 覆盖率）可在 Phase 1 提取完后立即执行，不需要训练。这比 Phase 2a 的线性分类器更早给出诊断信号。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-12 11:21 UTC\\n  summary: 'Phase 1 gate PASS: timeout 0%, H2 Fisher p=1.54e-7, 75% instance recall.\\n    进入 Phase 2。'\\n  rationale: 10 repos 中 8 个成功提取（2 个 skip 因 buggy file 路径不存在，非 CodeQL 限制）。timeout rate\\n    0% 远低于 30% 阈值。H2 sanity check：连通文件 gold 覆盖 1.44% vs 不连通 0.00%，Fisher p=1.54e-7。75%\\n    instance recall（6/8 gold file 在连通集）。数据质量问题（路径匹配、skip rate、registry 注册）并行修复，不阻塞\\n    Phase 2。\\n  related_experiments: []\\n  depends_on: []\\n- id: D005\\n  date: 2026-05-12 11:35 UTC\\n  summary: 'CRITICAL: GPU 越界 PID 59170 跑在 GPU 5 而非分配的 cuda:4，立即 kill + 全脚本修复 CUDA_VISIBLE_DEVICES'\\n  rationale: Reviewer 核实 nvidia-smi 发现 run_mvp.py 在 GPU 5 上运行 9.3GB，而项目分配的 cuda:4\\n    完全空闲。违反 L1 红线（GPU 资源边界）。要求 Agent 立即 kill 进程、修复所有脚本强制 CUDA_VISIBLE_DEVICES=4、排查\\n    dry-run 是否也越界。\\n  related_experiments: []\\n  depends_on: []\\n- id: D006\\n  date: 2026-05-12 17:24 UTC\\n  summary: P2b pass criteria 调整：recall@5→recall@1，pool_size 26→50+，阈值 ≥2pp 不变\\n  rationale: Eval v2 (pool_size=26) 显示 random recall@5 已达 98.4-99.2%，原标准\\\"dataflow\\n    recall@5 > random ≥2pp\\\"数学上几乎不可能达标（天花板仅 0.8-1.6pp 空间）。recall@1 有更大区分度（random mean\\n    93.97%），且是更严格的排序指标。同时扩大 pool_size 至 50+ 使 recall@5/10 也获得有效梯度。新标准：dataflow_aware\\n    recall@1 > random recall@1 ≥2pp in ≥2/3 seeds，pool_size=50。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: random recall@1 mean=0.940, emb_dist recall@1=0.669 at pool=26; recall@5\\n      ceiling\\n  depends_on:\\n  - D002\\n- id: D007\\n  date: 2026-05-12 19:52 UTC\\n  summary: MVP P2b dataflow 策略不可验证：connected⊆gold 导致数据相同。决定：50-repo 规模验证 + Scheme\\n    B 备份\\n  rationale: 修复 build_p2b_data.py 后重新生成数据，train_dataflow.jsonl 仍与 train_embedding.jsonl\\n    完全相同。根因：8 个 MVP repos 中 dataflow 连接文件全部是 gold 文件的子集（connected-but-not-gold = 0），non_pos\\n    过滤无差异。这不是方法缺陷而是规模问题——小 repo 紧耦合，2-hop 连接集≈gold 集。P1（Fisher p=1.54e-7）和 P2a（AUC=0.78）仍有效，说明\\n    dataflow connectivity 有信号，只是 MVP 规模不足以分离 connected-but-not-gold 子集。决策：(1) 立即跑\\n    50-repo 样本的 overlap 统计（CPU, ~2-4h），确认大规模下 connected⊃gold；(2) 并行准备 Scheme B（distance-weighted\\n    negatives）作为 pivot 备选；(3) overlap>20% 实例有 connected≠gold → 进入全量 M1 提取；overlap≈100%\\n    → pivot to Scheme B。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: dataflow≡embedding 因 connected⊆gold\\n  depends_on:\\n  - D006\\n  - D004\\n- id: D008\\n  date: 2026-05-12 20:38 UTC\\n  summary: MVP 条件性通过：P1+P2a PASS，P2b dataflow 在 MVP 规模不可测但 50-repo 规模验证确认方法可行（Z=40.8%）。进入\\n    research 阶段。\\n  rationale: MVP 三阶段结果：P1 PASS（timeout 0%, Fisher p=1.54e-7, 75% instance recall）；P2a\\n    PASS（AUC 0.78, BM25 系数为负）；P2b 部分有效——random>>embedding（-27pp recall@1 at pool=26,\\n    -3.7pp at pool=50）确认 naive hard negatives 有害，但 dataflow vs random 因 connected⊆gold\\n    无法在 8 repos 上区分。50-repo 规模验证 Z=40.8%（中型 repo 55.7%），timeout 4%，确认方法在全量数据上可行。Kill\\n    criteria 均未触发。P2b dataflow 对比将在 M2 全量训练中完成。\\n  related_experiments:\\n  - exp_id: mvp_p1_codeql_feasibility\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2a_linear_proxy\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: evidence\\n    result: partial - random>>emb confirmed, dataflow untestable at MVP scale\\n  depends_on:\\n  - D007\\n  - D006\\n  - D004\\n- id: D009\\n  date: 2026-05-12 22:04 UTC\\n  summary: Dream 审稿完成：best=Weak Accept, median=Weak Reject, worst=Reject。批准 P0 启动，但\\n    plan 需增补 5 个 dream-derived 实验\\n  rationale: 三档共识问题：(1) 单编码器无法支撑 generality claim，需加 StarCoder/CodeBERT；(2) static\\n    vs dynamic embedding mining 是潜在 confound；(3) τ=0.05 可能 regime-specific；(4) SWE-bench\\n    +2pp 需 bootstrap CI；(5) abstract \\\"complementary\\\" 需降调。关键风险变量是 M1 的 Z%：≥35% best\\n    framing 成立，20-35% pivot 到 Claim 2 headline，<20% 需重大调整。已在 experiment_plan.yaml\\n    增加 plan_013-017（+35h GPU），paper_framing.md 增加 contingency framing。P0 实验（M1 已在跑）可继续，不需\\n    re-dream。\\n  related_experiments:\\n  - exp_id: dream_20260512T204322\\n    role: dream_simulate\\n    result: best=WA, median=WR, worst=R\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-12 22:09 UTC\\n  summary: plan_013 (second encoder) 从 P1 升级至 P0，headline template 降调修复\\n  rationale: Reviewer 指出 single encoder 是 best→accept 的关键区分因素，在 best-R1-W1 和 median-R2-W5\\n    两档都出现。P1 排期可能导致论文缺少 generality 证据而被 WR。升级后 M2 完成即可并行启动 plan_013。同时修复 headline\\n    template \\\"cannot recover\\\" → \\\"complementary signal not captured by\\\"。\\n  related_experiments:\\n  - exp_id: plan_013\\n    role: priority_upgrade\\n    result: P1→P0\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-13 01:38 UTC\\n  summary: Z%=74.0% 确认 Best Framing — Claim 1 为 headline，批准 M2 早期训练\\n  rationale: M1 部分数据（24/222 repos, 5128 instances）Z%=74.0%，远超 ≥35% 阈值。对比 D007 的 40.8%（50\\n    SWE-bench repos），SWE-Smith 数据集跨文件依赖密度更高。Best framing 成立：Claim 1 (\\\"structure-grounded\\n    negatives outperform\\\") 为 headline。批准在当前 5K instances 上做 M2 早期训练 pilot（3 strategies\\n    × 1 seed），利用 cuda:4 空闲期获取早期信号，不等全量 M1（还需 ~46h）。磁盘已清理至 61GB free (64%)，足够训练。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: Z%=74.0% at 24/222 repos\\n  - exp_id: d007_50repo_overlap\\n    role: baseline\\n    result: Z%=40.8% on SWE-bench 50 repos\\n  depends_on:\\n  - D009\\n  - D010\\n- id: D012\\n  date: 2026-05-13 02:11 UTC\\n  summary: Kill m2_early_pilot_v3 (PID 897752) — 第二次 GPU 越界 (cuda:0)\\n  rationale: Reviewer 发现 m2_early_pilot_v3 在 cuda:0 运行（PID 897752, 17100 MiB），项目仅分配\\n    cuda:4。这是第二次 GPU 越界（第一次 D005 在 GPU 5）。立即 kill 并标记 killed。同时 m2_early_pilot_v2\\n    因 wandb API key error 已崩溃标记 FAILED。当前唯一合法训练为 PID 795791 (m2_early_pilot, cuda:4)。要求\\n    Agent 排查越界原因并确保后续脚本强制 CUDA_VISIBLE_DEVICES=4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot_v3\\n    role: violated\\n    result: killed - GPU 越界 cuda:0\\n  - exp_id: m2_early_pilot_v2\\n    role: failed\\n    result: wandb API key error\\n  - exp_id: m2_early_pilot\\n    role: active\\n    result: PID 795791 on cuda:4, running\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-13 02:50 UTC\\n  summary: 服务器迁移：cqa1-21977 cuda:4 → bjb1-42106 cuda:0/1 (RTX PRO 6000 96GB×2)\\n  rationale: Manager 分配独立服务器 bjb1-42106（2x RTX PRO 6000 96GB）。迁移策略：(1) M1 提取继续在 cqa1-21977\\n    CPU 上完成（不中断），(2) 新服务器立即搭建环境+同步代码+下载模型，(3) M2 early pilot 在 cqa1-21977 cuda:4 跑完后所有\\n    GPU 工作转到新服务器，(4) 通知 Manager 释放 cuda:4。RTX PRO 6000 96GB 彻底解决 M3a VRAM 问题（Qwen3.6-27B\\n    不再需要 fallback），2 卡可并行 M2 全量 + plan_013。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: in_progress\\n    result: finishing on cqa1-21977 cuda:4\\n  - exp_id: m1_extraction\\n    role: in_progress\\n    result: CPU only, stays on cqa1-21977\\n  depends_on:\\n  - D011\\n- id: D014\\n  date: 2026-05-13 04:44 UTC\\n  summary: Kill m2_early_pilot (PID 795791) — 过拟合+卡死，bjb1 m2_embed_verify 取代\\n  rationale: m2_early_pilot 在 cqa1 cuda:4 上仅完成 random 策略（best val_loss=0.5879 at step\\n    1500，之后持续过拟合到 0.728）。进程在 step 4000 卡死 45+ min。OOM 干扰（另一进程在同 GPU 启动）。embedding_distance\\n    和 dataflow_aware 策略未启动。bjb1 上的 m2_embed_verify 使用 true embedding mining + 更大参数（negatives=7,\\n    seq_len=2048, batch=8）+ eval bug fix，将完全取代此 pilot。通知 Manager 释放 cqa1 cuda:4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: killed\\n    result: random best val_loss=0.5879, overfitting after step 1500\\n  - exp_id: m2_embed_verify\\n    role: replacement\\n    result: preparing on bjb1 cuda:1\\n  depends_on:\\n  - D011\\n  - D013\\n- id: D015\\n  date: 2026-05-13 11:43 UTC\\n  summary: 全量 Z%=78.0%（条件）确认 Best Framing；Coverage 34.3% 需论文讨论\\n  rationale: 全量 M1（123/131 repos, 44,173 instances）统计：15,153 instances 有结构数据（34.3%），其中\\n    11,825 有 connected-but-not-gold 文件（条件 Z%=78.0%，高于 pilot 72.5%）。条件 Z% 远超 35% 阈值，Best\\n    Framing（Claim 1 as headline）完全成立。但 Coverage 仅 34.3%——65.7% instances CodeQL/Beniget\\n    未产出结构连接，论文需讨论此局限性并限定 claim 范围为\\\"有结构数据的 instances\\\"。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: 123/131 repos, 44173 instances, 15897 structural\\n  - exp_id: plan_006_scalability\\n    role: prior_pilot\\n    result: pilot Z%=72.5% on 29 repos\\n  depends_on:\\n  - D011\\n- id: D016\\n  date: 2026-05-13 15:24 UTC\\n  summary: 'Reviewer Critical: m2_embed_verify 和 plan_013_starcoder 实际已完成全部 3 策略，registry\\n    错误标记为 failed'\\n  rationale: Reviewer 直接从服务器日志验证：两个实验的 dataflow 策略均已完成（\\\"All 3 strategies completed\\\"），EXIT_CODE\\n    异常发生在训练完成之后（wrapper 脚本问题）。关键数据：(1) Qwen dataflow peak R@1=0.5584 (+2.27pp vs random)，支撑\\n    Claim 1；(2) StarCoder dataflow R@1=0.4869 < random 0.4922，encoder-agnostic claim\\n    受挑战；(3) 两个编码器的 dataflow 策略均严重过拟合（train loss→0）。已派 Agent 紧急修正 registry + 收集完整 metrics\\n    + 验证 StarCoder random 数据来源。方向决策待 Agent 汇报验证数据后确定。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 实际完成（3 strategies all done），Qwen dataflow peak R@1=0.5584\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 实际完成（3 strategies all done），StarCoder dataflow R@1=0.4869 < random 0.4922\\n  depends_on: []\\n- id: D017\\n  date: 2026-05-13 16:03 UTC\\n  summary: Pilot 结果验证完成：embedding > random 跨编码器一致；dataflow 需按两种 checkpoint 标准报告；Claim\\n    2 需修订\\n  rationale: 'Reviewer 验证 18 个指标全部精确匹配。核心发现：(1) embedding > random 在 Qwen (+2.0pp)\\n    和 StarCoder (+1.6pp) 上一致，是最稳健结论；(2) dataflow 排名取决于 checkpoint 选择——按 val_loss:\\n    embedding > dataflow > random (Qwen)，按 peak R@1: dataflow > embedding > random\\n    (Qwen)；(3) StarCoder dataflow final eval 追平 embedding (0.5078=0.5078)，\\\"embedding\\n    consistently beats dataflow\\\" 不成立；(4) Claim 2 (\\\"embedding harms\\\") 在 true embedding\\n    mining 下不复现，仅在 MVP BM25 proxy 下成立。全量 M2 训练需报告两种 checkpoint 标准下的结果，避免 cherry-picking\\n    质疑。Paper framing 修订延后至全量 M2 结果出来后。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 'Qwen: embedding(0.5557) > dataflow(0.5436) > random(0.5357) by val_loss;\\n      dataflow peak(0.5584) > embedding(0.5557) by R@1'\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 'StarCoder: embedding(0.5078) > random(0.4922) > dataflow(0.4869) by val_loss;\\n      dataflow final(0.5078) = embedding'\\n  depends_on:\\n  - D016\\n- id: D018\\n  date: 2026-05-13 16:04 UTC\\n  summary: 不做预判性 framing pivot，full M2 (18 runs) 是 go/no-go 唯一判据；双 checkpoint 标准；准备\\n    B/C 两条后备路线\\n  rationale: Pilot 仅 24 repos / 1 seed，<2pp delta 统计功效不足以支持强 claim 或否决原假设。Full M2\\n    (131 repos × 3 strategies × 3 seeds × 2 encoders = 18 runs) 提供 3-seed 统计功效，是唯一可信判据。不选\\n    Agent 提议的 A/B/C 任何一个——过早锁定叙事会限制后续解读空间。数据构建已在进行，不浪费时间在 framing 讨论上。Full M2 结果出来后根据实际数据\\n    pattern 决定：(a) dataflow 跨编码器一致 > random → 原 framing 修正后可用；(b) dataflow 不一致但 embedding\\n    一致 → 方案 B 或 C；(c) 所有差异不显著 → 需要更大规模实验或 pivot。同时要求 dual checkpoint (best-val-loss\\n    + best-R@1) 和 3-seed CI 确保结果可信。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-13 18:08 UTC\\n  summary: D018 补充：Full M2 go/no-go 量化阈值 + 统计检验方案\\n  rationale: 'Reviewer 指出 D018 缺量化阈值，go/no-go 判据需在结果出来前明确，避免事后 rationalization。\\n\\n\\n    **统计方法**：每个 encoder 3 seeds 的 R@1 (best-by-val-loss checkpoint) 做 paired difference，bootstrap\\n    95% CI + paired t-test (p<0.05)。同时报告 best-by-R@1 checkpoint 结果作为透明度补充。\\n\\n\\n    **Go/No-Go 阈值**：\\n\\n    (A) Go — 原 framing 可用：dataflow > random 的 95% CI 在两个 encoder 上均 > 0\\n\\n    (B) Conditional Go — 修正 framing：dataflow > random 在至少一个 encoder 上 CI > 0，另一个 CI\\n    含 0（差异不显著）\\n\\n    (C) No-Go for Claim 1：dataflow ≤ random 在两个 encoder 上 CI 均含 0 或为负 → Claim 1 失效，pivot\\n    到 \\\"mining strategy × architecture\\\" 分析论文\\n\\n\\n    **Claim 2 判据**：若 full M2 显示 embedding > random 且 CI > 0 → 原 Claim 2 (\\\"embedding\\n    harms\\\") 被否定。新 Claim 2 候选：\\\"true embedding mining helps, but BM25 proxy harms\\\" 或\\n    \\\"hard negative mining method matters more than hard negative source\\\"\\n\\n\\n    **跨 encoder 一致性规则**：\\n\\n    - 同方向同显著 → 强泛化 claim\\n\\n    - 同方向不同显著 → 条件 claim + architecture discussion\\n\\n    - 反方向 → Claim 1 原形式被拒，需 conditional reframe\\n\\n\\n    阈值在 full M2 结果出来前锁定，不允许事后修改。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING - random_s42 in progress\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING - data build phase\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-13 18:10 UTC\\n  summary: D019 补充：Claim 2 完整判定矩阵 + n=3 功效限制声明\\n  rationale: 'Reviewer 指出 D019 的 Claim 2 阈值不完整 + n=3 统计功效天然受限。补充如下：\\n\\n\\n    **Claim 2 完整判定矩阵**（3 seeds, paired bootstrap 95% CI）：\\n\\n    (i) random > embedding CI>0 → Claim 2 confirmed（embedding harms，与 MVP 一致）\\n\\n    (ii) embedding > random CI>0 → Claim 2 falsified（true embedding mining helps，需\\n    reframe）\\n\\n    (iii) CI 含 0 → inconclusive（效应存在但检测不到或确实无差异，论文报告为 \\\"no significant difference\\\"\\n    + 报告 effect size）\\n\\n\\n    **n=3 功效限制**（显式承认，不修改阈值）：\\n\\n    - df=2 时 t 临界值 4.303，pilot 级别差异（<2pp）极难达到 p<0.05\\n\\n    - Bootstrap n=3 仅 27 种重采样，CI 估计粗糙\\n\\n    - 阈值框架偏向 No-Go（Type II error 高）\\n\\n    - 若结果落入 (C) No-Go，论文 Discussion 必须讨论功效限制，不能简单声明 \\\"dataflow 无效\\\"\\n\\n    - 这是算力约束下的合理选择，不改阈值，但明确风险\\n\\n\\n    **plan_014 排期**：Full M2 完成后优先启动 plan_014（temperature ablation, ~10h）——无论 Claim\\n    2 reframe 成哪个方向，temperature regime-specificity 都需要回答。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING\\n  depends_on:\\n  - D019\\n- id: D021\\n  date: 2026-05-13 19:10 UTC\\n  summary: Negative difficulty 分析揭示 encoder capacity 差异是 dataflow 效果不一致的根因\\n  rationale: '预训练模型 cosine similarity 分析显示：Qwen pretrained embeddings 分辨力弱（random\\n    cosine sim 0.899），StarCoder 分辨力强（random cosine sim 0.553）。Dataflow negatives 在两个模型上都比\\n    random 更难（higher sim），说明方法设计正确。但 StarCoder 已经\\\"懂\\\"结构差异（所有策略 sim 都低），额外训练信号边际收益小。这解释了\\n    pilot 中 StarCoder dataflow < random 的现象：不是方法问题，是 encoder 已有足够 capacity。\\n\\n\\n    论文价值：(1) 从 negative result 中提取 mechanistic explanation；(2) 定义 method applicability\\n    condition：\\\"structure-grounded negatives benefit most when pretrained encoder has\\n    limited structural separability\\\"；(3) 产出论文级图表（Figure: Negative Difficulty Distributions）；(4)\\n    无论 full M2 落入 A/B/C，这个分析都增加论文深度。不修改 go/no-go 阈值，但丰富解读框架。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: context\\n    result: 'Qwen: dataflow > random (+0.8~2.3pp)'\\n  - exp_id: plan_013_starcoder\\n    role: context\\n    result: 'StarCoder: dataflow < random (-0.5pp), explained by high pretrained separability'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D022\\n  date: 2026-05-13 19:25 UTC\\n  summary: M1 28K instances 可恢复（运行时故障非数据问题）；当前 M2 继续，并行后台重跑 M1 提取\\n  rationale: 'Fuzzy match 抽查 10/10 发现 buggy_file 全部存在——28,276 个 \\\"error\\\" 是 CodeQL 并行提取时的运行时故障（磁盘/存储瞬态），不是\\n    SWE-smith 数据质量问题。训练数据潜在从 15,897 → ~44,173（2.8x）。\\n\\n\\n    决策：不中断当前 M2 训练 + 并行后台重跑 M1 提取。理由：\\n\\n    (1) 当前 M2 已在双卡运行，中断重来延期 3-7 天超出 DDL\\n\\n    (2) M1 重提取是 CPU 工作，可在 bjb1-42106 后台运行不影响 GPU 训练\\n\\n    (3) 如果当前 M2 结果落入 (C) No-Go 或 effect size 太小，扩展数据集是 natural next step\\n\\n    (4) 2.8x 数据量可能显著缓解 dataflow 过拟合问题（D021 中的核心风险）\\n\\n\\n    Claim 3 叙事需修正：\\\"64% failure 是上游数据问题\\\" → \\\"64% 是运行时提取故障，CodeQL 本身在有效输入上 100% 成功，可通过重跑恢复\\\"。这是\\n    engineering limitation with clear fix，不是方法局限。'\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: primary\\n    result: 28,276 instances recoverable - runtime failure, not data quality\\n  - exp_id: plan_006_scalability\\n    role: affected\\n    result: 'error classification needs correction: buggy_file_not_found was misattributed'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D023\\n  date: 2026-05-13 19:43 UTC\\n  summary: Kill M1 重提取：bjb1 CodeQL 查询 100% 失败，D022 前提不成立需诊断后重新评估\\n  rationale: Reviewer CRITICAL 发现 bjb1-42106 上 CodeQL call_graph.ql 查询全部 exit status\\n    2，317/325 行失败，零有效结构数据产出。原 M1 在 cqa1-21977 成功，迁移后 CodeQL 版本/QL pack 可能不兼容。立即 kill\\n    进程释放 CPU/RAM，诊断 CodeQL 配置后决定修复或换服务器。\\n  related_experiments:\\n  - exp_id: m1_reextract\\n    role: subject\\n    result: killed - CodeQL incompatible on bjb1\\n  depends_on:\\n  - D022\\n- id: D024\\n  date: 2026-05-14 00:49 UTC\\n  summary: 'Major paper framing rewrite: drop falsified \\\"embedding harms\\\" claim, pivot\\n    to \\\"systematic analysis + mechanistic insight\\\" narrative'\\n  rationale: 'Reviewer deep assessment confirmed Claim 2 (\\\"embedding actively harms\\\",\\n    -27pp) was built on BM25-proxy mislabeled as embedding-distance in MVP. D017 proved\\n    true embedding mining helps (+1.6-2.0pp). New framing: (1) embedding universally\\n    helps (corrects misconception), (2) dataflow conditionally helps (mediated by\\n    representation saturation), (3) CodeQL scalable. This is a stronger, more honest\\n    paper type for EMNLP — empirical analysis with mechanistic depth rather than false\\n    \\\"our method beats all\\\" claim.'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: embedding > random confirmed for both encoders\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: dataflow helps Qwen only, not StarCoder — conditional benefit\\n  - exp_id: neg_difficulty_analysis\\n    role: evidence\\n    result: pos_sim saturation explains strategy-encoder interaction\\n  depends_on: []\\n- id: D025\\n  date: 2026-05-14 01:01 UTC\\n  summary: Plan_014 temperature ablation 缩减为 2 strategies × 3τ × 2 epochs = 6 runs\\n    (~70h)，deadline 可达\\n  rationale: 原方案 9 runs × 3 epochs = 157h GPU，超出 May 25 ARR 截稿。缩减理由：(1) 回答 Dream reviewer\\n    的 regime-specificity concern 只需证明 embedding vs random 的相对优势跨 τ 一致，不需要 3 策略全跑；(2)\\n    M2 和 pilot 均显示 epoch 3 过拟合无收益，2 epochs 足够；(3) τ=0.07 已由 M2 覆盖，只需 {0.05, 0.1, 0.2}。6\\n    runs × ~11.7h = ~70h → 双卡并行 35h wall time，M2 完成后 ~1.5 天可跑完。Dataflow strategy 的\\n    τ ablation 降为 P2，时间充裕再补。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: step 1000 best, epoch 3 overfitting → 2 epochs sufficient\\n  - exp_id: plan_014\\n    role: target\\n    result: budget revised from 10h to 70h, scope from 9 to 6 runs\\n  depends_on:\\n  - D024\\n- id: D026\\n  date: 2026-05-14 02:56 UTC\\n  summary: Qwen eval@2000 确认过拟合，后续 M2 runs 从 3 epochs 减至 2 epochs\\n  rationale: 'eval@2000: val_loss=0.5162, R@1=0.5228（与 @1500 持平，未恢复）。Best 锁定 step\\n    1000 (epoch 1 中段)。train_loss=0.04 vs val_loss=0.52，gap 持续扩大。模式与 pilot 一致（best\\n    at ~25% training）。当前 s42 保留 3 epochs 完整跑完（提供 full overfitting curve 数据），后续 8 runs/encoder\\n    设 max_epochs=2。节省 ~48h/GPU，M2 完成时间从 ~May 20-21 提前到 ~May 18-19。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: eval@2000 R@1=0.5228 flat, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: pending\\n    result: eval@1000 still improving, apply 2-epoch precaution for subsequent seeds\\n  depends_on:\\n  - D025\\n- id: D027\\n  date: 2026-05-14 08:13 UTC\\n  summary: M2 剩余 runs 加 early stopping (patience=2 evals)，加速关键路径\\n  rationale: Reviewer 计算 M2 全 18 runs 需 ~5.5 天（StarCoder 瓶颈 ~133h）。两个编码器 best checkpoint\\n    均在 step 1000，之后 val_loss 持续上升。加 early stopping（patience=2，即连续 2 次 eval@500 无改善即停）预计在\\n    step 2000 左右停止（vs 2828 full 2-epoch），节省 ~30% 时间（~1.5 天），M2 从 May 19.5 提前到 ~May\\n    18。关键路径 May 25 ARR 余量从 5 天增至 7 天。风险低：仅影响未启动的 runs，不改已跑数据。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  depends_on:\\n  - D026\\n- id: D028\\n  date: 2026-05-14 11:09 UTC\\n  summary: Claim 2 降级待定：M2 full 结果决定 \\\"conditional benefit\\\" 是独立 claim 还是降为 observation\\n  rationale: Reviewer 覆盖率审查指出 Claim 2 最薄弱：n=2 encoders 交互效应无统计功效，neg_difficulty 是描述性非实验性证据。建议降为\\n    \\\"observation + mechanistic hypothesis\\\"。决策延迟到 M2 full 18 runs 完成后：若 Qwen dataflow>random\\n    p<0.05 则保持 conditional claim；否则降级为 observation。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: Qwen pilot positive\\n    result: dataflow > random +0.8pp val_loss\\n  - exp_id: plan_013_starcoder\\n    role: StarCoder pilot negative\\n    result: dataflow < random -0.5pp\\n  - exp_id: m2_full_qwen\\n    role: go/no-go for claim strength\\n    result: RUNNING\\n  - exp_id: m2_full_starcoder\\n    role: encoder generality test\\n    result: RUNNING\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D029\\n  date: 2026-05-14 16:23 UTC\\n  summary: Dream full review 完成：7 条三档一致结构性问题确认，BM25 baseline 升为 P0，pool size sensitivity\\n    新增 plan_019\\n  rationale: 'dream_20260514T075732 (full review mode) 三档评分: Best 4/6 WA, Median 3/6\\n    WR, Worst 3/6 WR。跨三档一致的结构性问题 7 条：(1) 缺 BM25 baseline 是 #1 共识——论文核心叙事（纠正 CoCoHaNeRe）无实证支撑，已加\\n    plan_018 P0；(2) N=2 编码器限制——保持 honest framing，无法加更多编码器；(3) StarCoder 误标为 encoder-decoder——已修正为\\n    decoder-only；(4) RepoBench-R 无 CIs——plan_004 已标注多 seed 要求；(5) Pool=50 太小——新增 plan_019\\n    P1；(6) 34% structural coverage 未分层——plan_005 已扩展；(7) Checkpoint selection criterion\\n    未指定——写作时明确。观察项：effect sizes 太小（等 M2 真实数据）、overfitting 分析（提取现有训练 log）。忽略项：broken\\n    bibliography（dream artifact）、0 figures（dream artifact）。评分顺序正常（best≥median=worst）。下一步：派\\n    Agent 准备 BM25 mining（CPU），M2 完成后立即执行 plan_018 training phase。'\\n  related_experiments:\\n  - exp_id: plan_018\\n    role: new P0 experiment added\\n    result: planned\\n  - exp_id: plan_019\\n    role: new P1 experiment added\\n    result: planned\\n  - exp_id: plan_004\\n    role: updated with multi-seed CI requirement\\n    result: planned\\n  - exp_id: plan_005\\n    role: extended with structural coverage stratification\\n    result: planned\\n  depends_on:\\n  - D024\\n  - D028\\n- id: D030\\n  date: 2026-05-14 16:23 UTC\\n  summary: Dream dream_20260514T075732 分析完成：7 项确认行动 + 5 项观察项 + re-dream 后批准新 P0\\n  rationale: 'Dream full review (2 Reviewers roundtable) 三档评分: Best=4/6(WA), Median=3/6(WR),\\n    Worst=3/6(WR)。Median 未达 borderline，需修复结构性问题后 re-dream。\\n\\n\\n    **三档一致的结构性问题（7 项确认行动）：**\\n\\n    1. [EXP] 缺 BM25 negative baseline — 论文核心 narrative (correcting CoCoHaNeRe) 无实证。加\\n    plan_018, P0, Phase1 CPU 立即启动\\n\\n    2. [EXP] RepoBench-R 缺 CIs — plan_004 增加多 seed 评估\\n\\n    3. [EXP] Pool size 50 过小 — 加 plan_019 sensitivity analysis\\n\\n    4. [EXP] 34% structural coverage 未分层 — 扩展 plan_005 加 structural-available vs fallback\\n    stratum + neg_difficulty quartile\\n\\n    5. [FRAMING] N=2 encoders → 降级为 \\\"observation + hypothesis\\\"，非 validated mechanism\\n\\n    6. [FRAMING] StarCoder 架构 → 修正为 \\\"decoder-only\\\"（已改）\\n\\n    7. [FRAMING] Claim 3 (CodeQL pipeline) → 降为 supporting methodology（已改）\\n\\n\\n    **观察项（等真实数据）：**\\n\\n    1. Effect sizes marginal [M][W] — 等 M2 full 统计结果\\n\\n    2. Dataflow claim strength [M][W] — D028 已 plan\\n\\n    3. \\\"Scaling law\\\" [W] → 用 \\\"trend\\\" + CIs\\n\\n    4. Temperature ablation contradiction [W] — plan_014 结果决定\\n\\n    5. Zero method contribution [M][W] — framing 强度决定\\n\\n\\n    **Re-dream 要求：** framing + plan 修改完成后需 re-dream，best ≥ WA 且 median ≥ borderline\\n    后才批准新 P0 实验。已在跑的实验继续。'\\n  related_experiments:\\n  - exp_id: dream_20260514T075732\\n    role: trigger\\n    result: best=4/6 WA, median=3/6 WR, worst=3/6 WR\\n  - exp_id: plan_018\\n    role: new_from_dream\\n    result: planned — BM25 baseline\\n  - exp_id: plan_019\\n    role: new_from_dream\\n    result: planned — pool size sensitivity\\n  depends_on:\\n  - D028\\n  - D024\\n- id: D031\\n  date: 2026-05-14 17:02 UTC\\n  summary: 'BM25 Phase 1 完成: 87% overlap with embedding_distance，预示论文叙事可能从 \\\"纠正误标\\\"\\n    转向 \\\"受控对比证明 hard negatives 普遍有效\\\"'\\n  rationale: 'plan_018 Phase 1 (CPU) 完成。3 seeds BM25 negatives 已生成，与 embedding_distance\\n    negatives 重叠率高达 87.1%。小 repo 候选池 ≤50 导致所有策略完全重合，BM25 differentiation 主要在大 repo\\n    上体现。\\n\\n\\n    Phase 2 训练结果预期 3 种可能：\\n\\n    A) BM25 harm (BM25 << random) → 原叙事成立（\\\"BM25 proxy 导致 CoCoHaNeRe 错误结论\\\"）\\n\\n    B) BM25 ≈ random → contingency per D030（叙事降为 \\\"systematic comparison\\\"）\\n\\n    C) BM25 ≈ embedding_distance (87% overlap 强烈预示) → 叙事升级为\\\"BM25 和 embedding mining\\n    高度重叠，两者在受控环境下都优于 random；CoCoHaNeRe 的负面结论源于实验控制不足而非 BM25-proxy 本身\\\"\\n\\n\\n    Scenario C 实际上比 A 更强——我们提供的不只是标签纠正，而是受控对比 + 叙事升级。\\n\\n\\n    附带决策：plan_015 暂缓至 camera-ready（44h 超预算 + DDL 紧），Limitations 中承认 static vs dynamic\\n    confound。'\\n  related_experiments:\\n  - exp_id: plan_018\\n    role: phase1_complete\\n    result: BM25 data ready, 87% overlap with embedding_distance\\n  - exp_id: plan_015\\n    role: deferred\\n    result: design complete, execution deferred to camera-ready\\n  depends_on:\\n  - D030\\n- id: D032\\n  date: 2026-05-14 17:02 UTC\\n  summary: plan_015 缩减为 1 seed × dynamic_ep (~11h)；BM25 overlap 87% 需分层验证\\n  rationale: 'plan_015 原设计 3 variants × 多 seeds = 44h，DDL May 25 前 GPU 时间不够。缩减为 dynamic_ep\\n    × 1 seed (Qwen s42) ~11h，足以排除 static vs dynamic confound。预期 dynamic ≈ static（<1pp），在\\n    Limitation 段写实验证据。\\n\\n\\n    BM25 Phase 1 完成：BM25 vs embedding overlap 87.1%。但 Agent 指出小 repo (pool ≤50) 导致所有策略\\n    negatives 重合——overlap 被拉高。已派补充分析按 repo 大小分层统计真实差异化程度。Phase 2 训练结果将决定 CoCoHaNeRe\\n    narrative 是否需要 pivot（contingency 已在 paper_framing.md）。'\\n  related_experiments:\\n  - exp_id: plan_015\\n    role: scope_reduction\\n    result: 44h→11h, 1 seed × dynamic_ep only\\n  - exp_id: plan_018\\n    role: phase1_complete\\n    result: BM25 vs embedding overlap 87.1%, 3 seeds done\\n  depends_on:\\n  - D030\\n- id: D033\\n  date: 2026-05-14 17:10 UTC\\n  summary: D031 修正：BM25 top-7 overlap 远低于 k=50 的 87%，大 repo 仅 30%，Phase 2 将有区分度\\n  rationale: '分层 Jaccard 分析（top-7, seed 42, 2920 matched queries）显示 BM25 vs embedding_distance\\n    重叠率：small=67%, medium=38%, large=30%。之前报告的 87% 是 k=50 全候选重叠，训练实际用 top-7 negatives\\n    差异大得多。\\n\\n\\n    关键修正：D031 中预判的 \\\"BM25 ≈ embedding_distance\\\" 不再成立。Phase 2 训练预期结果重新开放为三种可能（BM25 harm\\n    / neutral / help），实验区分度足够。\\n\\n\\n    方法论 flag: BM25 使用 whitespace tokenization (str.split())，不处理 camelCase/snake_case。如果\\n    BM25 表现差，tokenization 可能是 confound。论文中需标注。Reviewer 已指出。\\n\\n\\n    24% match rate 源于 BM25 mining 使用了不同 train/val split，不影响分层趋势结论但如需严格配对可重新生成。'\\n  related_experiments:\\n  - exp_id: plan_018\\n    role: phase1_analysis\\n    result: 'stratified overlap: large_repo BM25-vs-embedding=30%, BM25-vs-random=0.7%'\\n  depends_on:\\n  - D031\\n\", \"total_chars\": 26445, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7076eaa0-0c05-4734-b696-9c6635c22c6e",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a27710763487a3e39",
  "type": "user",
  "uuid": "bc43869d-7c08-441e-92f9-845874a19d9a",
  "sourceToolAssistantUUID": "7076eaa0-0c05-4734-b696-9c6635c22c6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-14T17:16:09.187Z_

Now let me read the latest dream paper (the one being reviewed) to understand the exact content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc43869d-7c08-441e-92f9-845874a19d9a",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qeY2AxBF1av4Gza2wk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8c8b021-1cc9-493f-a230-03f1172a00fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017a7LFTsw22HENbKxmtN4BZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15083,
      "cache_read_input_tokens": 29682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15083,
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

_source line 25 · 2026-05-14T17:16:11.597Z_

<details open><summary>🔧 Tool call — Read · `toolu_015ht4w93WdP6YFFibRT7paP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8c8b021-1cc9-493f-a230-03f1172a00fe",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qeY2AxBF1av4Gza2wk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4efe8273-b47c-431d-af2c-aafbb415a31f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017a7LFTsw22HENbKxmtN4BZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15083,
      "cache_read_input_tokens": 29682,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15083
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 29682,
          "cache_creation_input_tokens": 15083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15083,
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

_source line 26 · 2026-05-14T17:16:11.603Z_

<details><summary>↩ Tool result · `toolu_015ht4w93WdP6YFFibRT7paP`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{xcolor}
9	\usepackage[margin=1in]{geometry}
10	\usepackage{natbib}
11	\usepackage{hyperref}
12	\usepackage{caption}
13	\usepackage{subcaption}
14	\usepackage{array}
15	
16	\newcommand{\pp}{\,\text{pp}}
17	\newcommand{\sysname}{StructFuse}
18	
19	\title{What Makes Hard Negatives Work for Code Retrieval?\\A Systematic Study of Mining Strategies and Representation Geometry}
20	
21	\author{Anonymous}
22	\date{}
23	
24	\begin{document}
25	\maketitle
26	
27	%----------------------------------------------------------------------
28	\begin{abstract}
29	Hard negative mining is widely used to improve contrastive retrievers, yet the code retrieval community lacks systematic understanding of what mining strategies work and why.
30	We present a controlled study comparing four hard negative strategies---random, BM25-proxy, embedding-distance, and dataflow-disconnected---for training file-level code retrievers on SWE-smith data, evaluated across two decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B), multiple seeds, two retrieval benchmarks, and a downstream SWE-bench Lite agent pipeline.
31	Our main findings are: (1)~true embedding-distance mining \emph{tends to} improve retrieval over random baselines ($+$0.5--1.0\pp{} R@1 across conditions), while BM25-proxy negatives trend toward harm, suggesting that prior reports of embedding-negative harm (CoCoHaNeRe) were confounded by proxy conflation---though our BM25 effect size is modest and not statistically significant ($p > 0.05$); (2)~dataflow-grounded negatives interact with encoder architecture, showing marginal benefit on Qwen but neutral-to-negative effects on StarCoder, with confidence intervals including zero in most conditions; (3)~stratified analysis reveals that mining benefit concentrates in specific strata (small repos, hard negatives, medium query-positive similarity) but is diluted in the overall population.
32	We release our analysis framework and discuss implications for practitioners choosing negative mining strategies.
33	\end{abstract}
34	
35	%----------------------------------------------------------------------
36	\section{Introduction}
37	\label{sec:intro}
38	
39	Repository-level code repair requires retrieving relevant files from large codebases given a bug report or issue description.
40	Contrastive learning with hard negative mining is a standard recipe for training dense retrievers~\citep{karpukhin2020dense,xiong2021approximate}, and recent code retrieval systems such as SweRank adopt this paradigm.
41	However, the field has not systematically studied \emph{what makes hard negatives effective specifically for code}.
42	
43	A key confusion concerns the source of hard negatives.
44	CoCoHaNeRe reported that embedding-distance negatives \emph{harm} code search by $-27\pp{}$ R@1, leading practitioners to avoid them.
45	We hypothesize that this finding conflated BM25-proxy negatives (lexical top-$k$) with true embedding-distance negatives, and that the reported harm was an artifact of this proxy conflation combined with other uncontrolled factors.
46	
47	Beyond text-based mining, code repositories contain rich structural information---call graphs, dataflow dependencies, import chains---that could inform negative selection.
48	Several recent systems (CodexGraph, LocAgent, RANGER) exploit such structure at \emph{inference time}, but no prior work uses structural signals for \emph{training-time} negative mining.
49	
50	We present a systematic empirical study with the following contributions:
51	\begin{enumerate}
52	    \item A controlled four-strategy comparison (random, BM25, embedding, dataflow) across two encoders, three seeds, and two benchmarks, with full bootstrap confidence intervals.
53	    \item Evidence that true embedding-distance mining tends to help while BM25-proxy negatives trend toward harm, providing a partial correction to the CoCoHaNeRe finding---though with effect sizes smaller than originally reported and statistical significance not achieved on the BM25 comparison.
54	    \item A stratified analysis revealing where and why mining strategies differ, including a representation geometry explanation for encoder--strategy interaction.
55	    \item Introduction of structure-grounded (dataflow) negatives via inter-procedural CodeQL analysis as an exploratory direction, with characterization of the conditions under which they provide marginal benefit.
56	\end{enumerate}
57	
58	We position this work as an analysis paper: our goal is understanding, not proposing a new state-of-the-art method.
59	The effect sizes we observe are modest (typically $<$2\pp{}), and we report them with full uncertainty quantification to enable informed future work.
60	
61	%----------------------------------------------------------------------
62	\section{Related Work}
63	\label{sec:related}
64	
65	\paragraph{Hard Negative Mining for Dense Retrieval.}
66	DPR~\citep{karpukhin2020dense} uses BM25 top-$k$ as hard negatives for open-domain QA.
67	ANCE~\citep{xiong2021approximate} dynamically re-mines negatives from the current model checkpoint.
68	Curriculum-based approaches gradually increase negative difficulty during training.
69	In code retrieval, CoCoHaNeRe studied hard negatives for code search and reported that embedding-distance negatives harm performance by $-27\pp{}$ R@1.
70	We revisit this finding with controlled comparisons separating BM25-proxy from true embedding-distance negatives.
71	
72	\paragraph{Code Retrieval for Software Engineering.}
73	SweRank trains contrastive retrievers on SWE-smith data for file-level bug localization.
74	SWE-Fixer and related systems use BM25 or embedding retrieval as the first stage of a repair pipeline.
75	These systems use standard text-based retrieval without structural awareness at training time.
76	
77	\paragraph{Structure-Aware Code Intelligence.}
78	GraphCodeBERT incorporates dataflow into pretraining objectives.
79	CodexGraph, LocAgent, and RANGER use repository-level graphs (AST, call graph, dependency graph) at inference time for code navigation and localization.
80	ARISE uses intra-procedural dataflow for tool-augmented retrieval.
81	Our work differs by using inter-procedural dataflow for \emph{training-time} negative selection rather than inference-time navigation, making the two approaches complementary.
82	
83	%----------------------------------------------------------------------
84	\section{Method}
85	\label{sec:method}
86	
87	\subsection{Problem Setup}
88	
89	Given a repository $\mathcal{R}$ with files $\{f_1, \ldots, f_n\}$ and a query (bug report) $q$, the retriever must rank files by relevance.
90	We train a contrastive retriever using InfoNCE loss with temperature $\tau$:
91	\begin{equation}
92	    \mathcal{L} = -\log \frac{\exp(s(q, f^+) / \tau)}{\exp(s(q, f^+) / \tau) + \sum_{i=1}^{K} \exp(s(q, f_i^-) / \tau)}
93	\end{equation}
94	where $s(\cdot, \cdot)$ is cosine similarity, $f^+$ is the gold file, and $\{f_i^-\}_{i=1}^K$ are hard negatives.
95	The negative selection strategy---how $\{f_i^-\}$ are chosen---is the focus of this study.
96	
97	\subsection{Negative Mining Strategies}
98	
99	We compare four strategies, all mining from the same candidate pool within each repository:
100	
101	\paragraph{Random.} Uniformly sample $K$ non-gold files from the repository.
102	
103	\paragraph{BM25-Proxy.} Select the top-$K$ files by BM25 score against the query, excluding the gold file. This approximates the ``embedding-distance'' negatives used in prior work (CoCoHaNeRe) that actually relied on lexical retrieval as a proxy.
104	
105	\paragraph{Embedding-Distance.} Compute dense embeddings of all files using a pretrained encoder, then select the $K$ non-gold files closest to the query in embedding space. This is \emph{true} embedding-distance mining: negatives are the files the current model finds hardest to distinguish from the gold.
106	
107	\paragraph{Dataflow-Disconnected.} Using inter-procedural dataflow analysis (CodeQL), identify files that are \emph{not} reachable from the query context within a bounded call graph (default: 2-hop). Among these structurally disconnected files, select the $K$ with highest embedding similarity to the query. When structural data is unavailable (66\% of instances), fall back to random sampling.
108	
109	\subsection{Structural Analysis Pipeline}
110	
111	We extract inter-procedural dataflow graphs using CodeQL with scope-bounded analysis (2-hop default in the call graph).
112	The pipeline processes 123/131 target repositories with 0\% timeout rate and 78\% connected-not-gold rate, indicating that the structural signal captures meaningful code dependencies.
113	Structural data is available for 34\% of training instances; the remainder falls back to random negative selection under the dataflow strategy.
114	
115	\subsection{Training Configuration}
116	
117	We fine-tune two decoder-only encoders---Qwen2.5-Coder-3B and StarCoder2-3B---using LoRA on SWE-smith training data (5K instances, pool size 50 at training time).
118	Each strategy $\times$ encoder combination is trained with 3 seeds.
119	We use $\tau = 0.05$ as the default temperature (with ablation over $\{0.05, 0.1, 0.2\}$) and evaluate at steps \{200, 500, 1000, 1500, 2000\} to select the best checkpoint.
120	
121	%----------------------------------------------------------------------
122	\section{Experiments}
123	\label{sec:experiments}
124	
125	\subsection{Primary Results: SWE-smith Retrieval}
126	\label{sec:primary}
127	
128	Table~\ref{tab:four-strategy} reports R@1 for all four strategies across both encoders on SWE-smith validation (pool=50).
129	Embedding mining consistently ranks first, with $+$1.0\pp{} over random on Qwen and $+$0.7\pp{} on StarCoder.
130	BM25 negatives rank last, trending toward harm ($-$0.9\pp{} Qwen, $-$0.7\pp{} StarCoder) though neither comparison reaches significance ($p = 0.12$ and $p = 0.18$ respectively).
131	Dataflow shows a small positive delta on Qwen ($+$0.2\pp{}) but negative on StarCoder ($-$0.6\pp{}), consistent with an encoder--strategy interaction.
132	
133	\begin{table}[t]
134	\centering
135	\caption{R@1 on SWE-smith validation (pool=50) by strategy. Embedding mining ranks first across both encoders; BM25-proxy negatives trend toward harm but do not reach significance.}
136	\label{tab:four-strategy}
137	\begin{tabular}{lcccc}
138	\toprule
139	Strategy & Qwen R@1 & StarCoder R@1 & Qwen $\Delta$ vs Rand & StarCoder $\Delta$ vs Rand \\
140	\midrule
141	Random    & 0.530 & 0.443 & ---   & --- \\
142	Embedding & 0.540 & 0.450 & $+$1.0\pp{} & $+$0.7\pp{} \\
143	Dataflow  & 0.532 & 0.437 & $+$0.2\pp{} & $-$0.6\pp{} \\
144	BM25      & 0.521 & 0.436 & $-$0.9\pp{} & $-$0.7\pp{} \\
145	\bottomrule
146	\end{tabular}
147	\end{table}
148	
149	\paragraph{BM25 vs.\ Embedding: Partial CoCoHaNeRe Correction.}
150	Table~\ref{tab:bm25-gap} compares the BM25--embedding gap in our setup with the $-27\pp{}$ reported by CoCoHaNeRe.
151	We observe the same \emph{direction} (BM25 worse than embedding) but a much smaller magnitude ($-1.9\pp{}$ Qwen, $-1.4\pp{}$ StarCoder), and the BM25-vs-random comparison does not reach significance ($p = 0.12$, $p = 0.18$).
152	We interpret this as directional support for the hypothesis that CoCoHaNeRe's reported harm was amplified by proxy conflation and other uncontrolled factors (different mining protocol, pool size, pipeline robustness), but the evidence is insufficient to fully rule out alternative explanations.
153	
154	\begin{table}[t]
155	\centering
156	\caption{The BM25--embedding gap in our controlled setup vs.\ CoCoHaNeRe's reported values. Direction is consistent but magnitude is far smaller.}
157	\label{tab:bm25-gap}
158	\begin{tabular}{lcccc}
159	\toprule
160	Encoder & BM25 R@1 & Emb R@1 & Our $\Delta$ (pp) & CoCoHaNeRe $\Delta$ \\
161	\midrule
162	Qwen     & 0.521 & 0.540 & $-$1.9 & $-$27 \\
163	StarCoder & 0.436 & 0.450 & $-$1.4 & n/a \\
164	\bottomrule
165	\end{tabular}
166	\end{table}
167	
168	\subsection{Cross-Benchmark Validation: RepoBench-R}
169	\label{sec:repobench}
170	
171	To assess generalization, we evaluate on RepoBench-R (cross-file code completion retrieval) with both easy (pool$\sim$6) and hard (pool$\sim$18) splits.
172	Table~\ref{tab:repobench} shows directional consistency: embedding mining outperforms random on all conditions, and dataflow shows the same encoder interaction (positive on Qwen, negative on StarCoder).
173	However, all confidence intervals for the embedding--random delta include or border zero, and effect sizes are small (0.5--1.0\pp{}).
174	
175	\begin{table}[t]
176	\centering
177	\caption{RepoBench-R R@1 (\%) by strategy, encoder, and difficulty. Values are mean $\pm$ std across 3 seeds. CI width is 2--4\pp{} for all deltas.}
178	\label{tab:repobench}
179	\begin{tabular}{llccccc}
180	\toprule
181	Encoder & Split & Random & Embedding & Dataflow & Emb $\Delta$ & DF $\Delta$ \\
182	\midrule
183	Qwen     & easy & 68.2$\pm$0.7 & 68.8$\pm$0.8 & 68.5$\pm$0.9 & $+$0.6 & $+$0.3 \\
184	Qwen     & hard & 39.4$\pm$1.0 & 40.4$\pm$1.1 & 39.8$\pm$1.2 & $+$1.0 & $+$0.4 \\
185	StarCoder & easy & 62.1$\pm$0.6 & 62.6$\pm$0.7 & 61.8$\pm$0.8 & $+$0.5 & $-$0.3 \\
186	StarCoder & hard & 33.8$\pm$0.9 & 34.6$\pm$1.0 & 33.3$\pm$1.1 & $+$0.8 & $-$0.5 \\
187	\bottomrule
188	\end{tabular}
189	\end{table}
190	
191	\subsection{Downstream Evaluation: SWE-bench Lite}
192	\label{sec:swebench}
193	
194	We evaluate end-to-end on 300 SWE-bench Lite instances using a Qwen3.6-27B agent with each retrieval strategy (best Qwen checkpoint).
195	Table~\ref{tab:swebench} reports resolve rates and Table~\ref{tab:swebench-ci} reports bootstrap confidence intervals ($n=10{,}000$ resamples).
196	
197	\begin{table}[t]
198	\centering
199	\caption{SWE-bench Lite resolve rate by retrieval strategy. Differences are $<$1\pp{} and not significant.}
200	\label{tab:swebench}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4efe8273-b47c-431d-af2c-aafbb415a31f",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a27710763487a3e39",
  "type": "user",
  "uuid": "5cd67674-886f-4a22-b1b8-8bdb691efa00",
  "sourceToolAssistantUUID": "4efe8273-b47c-431d-af2c-aafbb415a31f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T17:16:15.493Z_

<details open><summary>🔧 Tool call — Read · `toolu_013HN1vkK5m6gcopDDXZG8UP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/paper.tex",
  "offset": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cd67674-886f-4a22-b1b8-8bdb691efa00",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qesvzPVbehNdM78Som",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e77aa43f-99d0-40cf-8c16-6395f40ee2c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YbtEwJq4u8yYZRXqDur2mQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4640,
      "cache_read_input_tokens": 44765,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4640
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 117,
          "cache_read_input_tokens": 44765,
          "cache_creation_input_tokens": 4640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4640,
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

_source line 28 · 2026-05-14T17:16:15.498Z_

<details><summary>↩ Tool result · `toolu_013HN1vkK5m6gcopDDXZG8UP`</summary>

```text
200	\label{tab:swebench}
201	\begin{tabular}{lccccc}
202	\toprule
203	Strategy & Resolved & Total & Rate (\%) & $\Delta$ vs Random (pp) & R@1 \\
204	\midrule
205	Random    & 69 & 300 & 23.0 & --- & 0.41 \\
206	Embedding & 71 & 300 & 23.7 & $+$0.7 & 0.42 \\
207	Dataflow  & 70 & 300 & 23.3 & $+$0.3 & 0.41 \\
208	\bottomrule
209	\end{tabular}
210	\end{table}
211	
212	\begin{table}[t]
213	\centering
214	\caption{Bootstrap 95\% CIs for SWE-bench strategy comparisons ($n=10{,}000$). No comparison is significant.}
215	\label{tab:swebench-ci}
216	\begin{tabular}{lccc}
217	\toprule
218	Comparison & $\Delta$ (pp) & 95\% CI & $p$-value \\
219	\midrule
220	Emb $-$ Random & $+$0.7 & [$-$3.2, $+$4.5] & 0.62 \\
221	DF $-$ Random  & $+$0.3 & [$-$3.8, $+$4.4] & 0.78 \\
222	Emb $-$ DF     & $+$0.3 & [$-$3.5, $+$4.2] & 0.73 \\
223	\bottomrule
224	\end{tabular}
225	\end{table}
226	
227	The SWE-bench evaluation confirms that no strategy \emph{harms} downstream performance, but the benchmark is underpowered to detect the retrieval-stage deltas we observe.
228	With $N=300$ binary outcomes and per-strategy standard error $\approx 2.4\pp{}$, detecting a $0.7\pp{}$ delta would require $N > 15{,}000$.
229	We treat this as a sanity check rather than primary evidence.
230	
231	\subsection{Stratified Analysis}
232	\label{sec:stratified}
233	
234	To understand where mining strategies differ, we stratify the SWE-smith validation set along five dimensions.
235	
236	\paragraph{Repository Size.}
237	Table~\ref{tab:strat-repo} shows embedding mining benefit decreases with repository size: $+$1.8\pp{} for small repos ($<$50 files) vs.\ $+$0.4\pp{} for very large repos ($>$500 files).
238	Small repos have less diverse candidate pools, making embedding-distance mining more effective at identifying meaningful hard negatives.
239	
240	\begin{table}[t]
241	\centering
242	\caption{Embedding $\Delta$ vs.\ random by repository size stratum (Qwen encoder).}
243	\label{tab:strat-repo}
244	\begin{tabular}{lrcccc}
245	\toprule
246	Stratum & $N$ & Random R@1 & Emb R@1 & $\Delta$ (pp) & 95\% CI \\
247	\midrule
248	Small ($<$50)      &   500 & 0.571 & 0.589 & $+$1.8 & [$-$0.5, 4.1] \\
249	Medium (50--200)   & 4{,}096 & 0.542 & 0.554 & $+$1.2 & [0.0, 2.4] \\
250	Large (200--500)   & 13{,}628 & 0.531 & 0.537 & $+$0.6 & [$-$0.3, 1.5] \\
251	XLarge (500$+$)    & 25{,}949 & 0.524 & 0.528 & $+$0.4 & [$-$0.5, 1.3] \\
252	\bottomrule
253	\end{tabular}
254	\end{table}
255	
256	\paragraph{Structural Data Availability.}
257	Table~\ref{tab:strat-structural} separates instances with dataflow data (34\%) from those without (66\%, where dataflow falls back to random).
258	The dataflow advantage ($+$0.6\pp{}) is entirely concentrated in the 34\% with structural coverage; on fallback instances, dataflow $\approx$ random ($+$0.1\pp{}).
259	This confirms that the dataflow strategy's overall diluted effect is due to limited structural coverage.
260	
261	\begin{table}[t]
262	\centering
263	\caption{Strategy deltas by structural data availability (Qwen encoder).}
264	\label{tab:strat-structural}
265	\begin{tabular}{lccccc}
266	\toprule
267	Stratum & $N$ & Random R@1 & Emb R@1 & DF R@1 & Emb $\Delta$ / DF $\Delta$ \\
268	\midrule
269	With dataflow (34\%) & $\sim$15K & 0.538 & 0.548 & 0.544 & $+$1.0 / $+$0.6 \\
270	Fallback (66\%)      & $\sim$29K & 0.526 & 0.536 & 0.527 & $+$1.0 / $+$0.1 \\
271	\bottomrule
272	\end{tabular}
273	\end{table}
274	
275	\paragraph{Negative Difficulty Quartile.}
276	Table~\ref{tab:strat-negdiff} stratifies by the difficulty of mined negatives (margin between positive and hardest negative).
277	Both strategies benefit most from hard negatives (Q4: emb $+$1.6\pp{}, df $+$1.2\pp{}) and least from easy ones (Q1: emb $+$0.3\pp{}, df $-$0.2\pp{}).
278	This supports a representation geometry explanation: when negatives are sufficiently hard, mining provides gradient signal that random sampling misses.
279	
280	\begin{table}[t]
281	\centering
282	\caption{Strategy delta by negative difficulty quartile (Qwen). Q4 = hardest negatives (margin $<$ 0.02).}
283	\label{tab:strat-negdiff}
284	\begin{tabular}{lccc}
285	\toprule
286	Quartile & Margin range & Emb $\Delta$ (pp) & DF $\Delta$ (pp) \\
287	\midrule
288	Q1 (easiest) & $> 0.15$      & $+$0.3 & $-$0.2 \\
289	Q2           & 0.08--0.15    & $+$0.8 & $+$0.1 \\
290	Q3           & 0.02--0.08    & $+$1.4 & $+$0.5 \\
291	Q4 (hardest) & $< 0.02$      & $+$1.6 & $+$1.2 \\
292	\bottomrule
293	\end{tabular}
294	\end{table}
295	
296	\subsection{Pool Size Sensitivity}
297	\label{sec:poolsize}
298	
299	Real-world repositories have pool sizes ranging from tens to thousands of files.
300	Table~\ref{tab:pool-qwen} and Table~\ref{tab:pool-starcoder} evaluate strategy rankings at pool $\in \{50, 100, 200, 500\}$ on SWE-smith validation.
301	
302	\begin{table}[t]
303	\centering
304	\caption{R@1 by pool size (Qwen). Embedding advantage is consistent but diminishes at larger pools.}
305	\label{tab:pool-qwen}
306	\begin{tabular}{rccccc}
307	\toprule
308	Pool & Random & Embedding & Dataflow & Emb $\Delta$ (pp) & Ranking stable? \\
309	\midrule
310	50  & 0.530 & 0.540 & 0.532 & $+$1.0 & \checkmark \\
311	100 & 0.412 & 0.421 & 0.413 & $+$0.9 & \checkmark \\
312	200 & 0.328 & 0.335 & 0.330 & $+$0.7 & \checkmark \\
313	500 & 0.241 & 0.246 & 0.244 & $+$0.5 & \checkmark \\
314	\bottomrule
315	\end{tabular}
316	\end{table}
317	
318	\begin{table}[t]
319	\centering
320	\caption{R@1 by pool size (StarCoder). At pool $\geq 200$, strategy differences converge.}
321	\label{tab:pool-starcoder}
322	\begin{tabular}{rccccc}
323	\toprule
324	Pool & Random & Embedding & Dataflow & Emb $\Delta$ (pp) & Stable? \\
325	\midrule
326	50  & 0.443 & 0.450 & 0.437 & $+$0.7 & \checkmark \\
327	100 & 0.339 & 0.345 & 0.334 & $+$0.6 & \checkmark \\
328	200 & 0.268 & 0.272 & 0.271 & $+$0.4 & $\sim$ \\
329	500 & 0.194 & 0.196 & 0.197 & $+$0.2 & $\times$ \\
330	\bottomrule
331	\end{tabular}
332	\end{table}
333	
334	Embedding mining maintains its advantage across all pool sizes for Qwen, but the delta shrinks from $+$1.0\pp{} (pool=50) to $+$0.5\pp{} (pool=500).
335	On StarCoder, rankings become unstable at pool $\geq 200$.
336	This suggests that at realistic pool sizes (200--1000+), the practical benefit of mining strategy choice is further reduced.
337	
338	\subsection{Ablation Studies}
339	\label{sec:ablations}
340	
341	\paragraph{Temperature.}
342	Table~\ref{tab:temp-qwen} shows R@1 across $\tau \in \{0.05, 0.1, 0.2\}$.
343	Strategy ranking (embedding $>$ random $\geq$ dataflow) is preserved across all temperatures, confirming robustness.
344	However, at the optimal $\tau = 0.1$, the embedding delta is smaller ($+$0.8\pp{}) than at $\tau = 0.05$ ($+$1.0\pp{}), because smoother gradients also smooth the hard-negative advantage.
345	
346	\begin{table}[t]
347	\centering
348	\caption{R@1 by temperature (Qwen). Strategy ranking is preserved; delta shrinks at higher $\tau$.}
349	\label{tab:temp-qwen}
350	\begin{tabular}{ccccc}
351	\toprule
352	$\tau$ & Random & Embedding & Dataflow & Emb $\Delta$ (pp) \\
353	\midrule
354	0.05 & 0.530 & 0.540 & 0.532 & $+$1.0 \\
355	0.10 & 0.537 & 0.545 & 0.537 & $+$0.8 \\
356	0.20 & 0.521 & 0.526 & 0.520 & $+$0.5 \\
357	\bottomrule
358	\end{tabular}
359	\end{table}
360	
361	\begin{table}[t]
362	\centering
363	\caption{R@1 by temperature (StarCoder). Same pattern: ranking preserved, delta shrinks.}
364	\label{tab:temp-starcoder}
365	\begin{tabular}{ccccc}
366	\toprule
367	$\tau$ & Random & Embedding & Dataflow & Emb $\Delta$ (pp) \\
368	\midrule
369	0.05 & 0.443 & 0.450 & 0.437 & $+$0.7 \\
370	0.10 & 0.451 & 0.457 & 0.446 & $+$0.6 \\
371	0.20 & 0.435 & 0.438 & 0.430 & $+$0.3 \\
372	\bottomrule
373	\end{tabular}
374	\end{table}
375	
376	\paragraph{Training Data Size.}
377	Table~\ref{tab:datasize} shows R@1 at 1K, 3K, and 5K training instances (Qwen).
378	Embedding mining benefit scales with data size ($+$0.3\pp{} at 1K, $+$1.0\pp{} at 5K), indicating the advantage is not an overfitting artifact.
379	However, scaling is sub-linear, suggesting that pretrained representation quality is the bottleneck.
380	
381	\begin{table}[t]
382	\centering
383	\caption{R@1 by training data size (Qwen). Embedding advantage grows with data, sub-linearly.}
384	\label{tab:datasize}
385	\begin{tabular}{lcccc}
386	\toprule
387	Size & Random & Embedding & Dataflow & Emb $\Delta$ (pp) \\
388	\midrule
389	1K       & 0.498 & 0.501 & 0.495 & $+$0.3 \\
390	3K       & 0.519 & 0.528 & 0.521 & $+$0.9 \\
391	5K (full)& 0.530 & 0.540 & 0.532 & $+$1.0 \\
392	\bottomrule
393	\end{tabular}
394	\end{table}
395	
396	\paragraph{Fusion Head.}
397	Table~\ref{tab:fusion} ablates inference-time scoring: embedding-only vs.\ structural-features-only vs.\ combined.
398	The combined head adds only $+$0.2\pp{} over embedding-only, confirming that the value of structural information lies in \emph{training-time negative selection}, not inference-time feature fusion.
399	
400	\begin{table}[t]
401	\centering
402	\caption{Fusion head ablation. Structural features alone are weak; combining with embeddings adds marginal value.}
403	\label{tab:fusion}
404	\begin{tabular}{lcccc}
405	\toprule
406	Encoder & Emb-only & Struct-only & Combined & Combined$-$Emb (pp) \\
407	\midrule
408	Qwen     & 0.539 & 0.412 & 0.541 & $+$0.2 \\
409	StarCoder & 0.449 & 0.378 & 0.451 & $+$0.2 \\
410	\bottomrule
411	\end{tabular}
412	\end{table}
413	
414	\paragraph{Call-Graph Hop Count.}
415	Table~\ref{tab:hopcnt} ablates the dataflow bounding at 1, 2, and 3 hops.
416	Differences are $<$0.5\pp{}, with 2-hop slightly optimal.
417	The more informative finding is the high fallback rate at 1-hop (42\%), confirming limited structural coverage.
418	
419	\begin{table}[t]
420	\centering
421	\caption{Dataflow R@1 by hop count and negative pool statistics.}
422	\label{tab:hopcnt}
423	\begin{tabular}{lcccccc}
424	\toprule
425	 & \multicolumn{2}{c}{R@1} & & \multicolumn{2}{c}{Pool statistics} \\
426	\cmidrule{2-3} \cmidrule{5-6}
427	Hops & Qwen & StarCoder & & Mean neg/query & Fallback \% \\
428	\midrule
429	1 & 0.530 & 0.434 & & 3.2 & 42\% \\
430	2 & 0.532 & 0.437 & & 8.7 & 28\% \\
431	3 & 0.529 & 0.436 & & 14.1 & 18\% \\
432	\bottomrule
433	\end{tabular}
434	\end{table}
435	
436	\paragraph{Dynamic vs.\ Static Mining.}
437	We tested dynamic re-mining (per-epoch) and found no significant improvement over static mining ($\Delta = +0.4\pp{}$, CI: [$-$0.8, 1.6], $p = 0.38$) despite 2.3$\times$ training time.
438	This is expected: over 2--3 epochs the encoder changes minimally, so re-mined negatives overlap $>$80\% with static ones.
439	
440	\begin{table}[t]
441	\centering
442	\caption{Static vs.\ dynamic embedding mining (Qwen). Dynamic adds negligible benefit at 2.3$\times$ cost.}
443	\label{tab:dynamic}
444	\begin{tabular}{lcccc}
445	\toprule
446	Mining & R@1 & $\Delta$ vs static (pp) & Train time (h) & 95\% CI \\
447	\midrule
448	Static  & 0.540 & --- & 7.5 & --- \\
449	Dynamic & 0.544 & $+$0.4 & 17.3 & [$-$0.8, 1.6] \\
450	\bottomrule
451	\end{tabular}
452	\end{table}
453	
454	\paragraph{Weighted vs.\ Binary Dataflow Negatives.}
455	Distance-weighted sampling by dataflow distance provides no significant improvement over binary connected/disconnected selection ($+$0.3\pp{}, CI: [$-$0.8, 1.4]).
456	Binary selection is simpler and preferred.
457	
458	\begin{table}[t]
459	\centering
460	\caption{Binary vs.\ weighted dataflow negatives. No significant difference.}
461	\label{tab:weighted}
462	\begin{tabular}{lccc}
463	\toprule
464	Encoder & Binary DF R@1 & Weighted DF R@1 & $\Delta$ (pp) \\
465	\midrule
466	Qwen     & 0.532 & 0.535 & $+$0.3 \\
467	StarCoder & 0.437 & 0.439 & $+$0.2 \\
468	\bottomrule
469	\end{tabular}
470	\end{table}
471	
472	\subsection{Failure Analysis and Case Studies}
473	\label{sec:failure}
474	
475	\paragraph{Failure Categorization.}
476	We manually analyzed 50 retrieval failures from SWE-bench (Table~\ref{tab:failure}).
477	The largest category is lexical gap (36\%), where query wording differs entirely from target file content---neither mining strategy addresses this.
478	Structural gap cases (28\%) are where dataflow helps most (57\% of such cases), but this ceiling limits overall impact.
479	
480	\begin{table}[t]
481	\centering
482	\caption{Failure categories from 50 SWE-bench retrieval failures, with per-strategy help rates.}
483	\label{tab:failure}
484	\begin{tabular}{lcccc}
485	\toprule
486	Category & Count (\%) & DF helps & Emb helps \\
487	\midrule
488	Structural gap      & 14 (28\%) & 8 (57\%) & 5 (36\%) \\
489	Lexical gap         & 18 (36\%) & 3 (17\%) & 6 (33\%) \\
490	Multi-file dep.     &  8 (16\%) & 4 (50\%) & 5 (63\%) \\
491	Other               & 10 (20\%) & 1 (10\%) & 2 (20\%) \\
492	\bottomrule
493	\end{tabular}
494	\end{table}
495	
496	\paragraph{Illustrative Case Studies.}
497	Table~\ref{tab:cases} presents 7 selected cases where strategies changed retrieval outcome.
498	These are chosen to illustrate the mechanism, not as representative evidence---overall effect sizes are modest (Tables~\ref{tab:four-strategy}--\ref{tab:repobench}).
499	Dataflow uniquely helps in cases involving cross-module callees, config propagation, and dependency cycles, where structural connectivity provides signal orthogonal to text similarity.
500	
501	\begin{table}[t]
502	\centering
503	\caption{Selected qualitative cases. Ranks are within the candidate pool. Cases are illustrative, not representative.}
504	\label{tab:cases}
505	\begin{tabular}{clcccl}
506	\toprule
507	\# & Issue type & Rand & Emb & DF & Key observation \\
508	\midrule
509	1 & Missing import     & 12 & 8 & 2 & DF finds cross-module callee \\
510	2 & API mismatch       &  9 & 3 & 4 & Emb finds similar naming \\
511	3 & Config propagation & 15 & 11 & 1 & DF traces config flow \\
512	4 & Type error         &  6 & 2 & 3 & Both find related types \\
513	5 & Null pointer       & 11 & 7 & 3 & DF finds data source \\
514	6 & Method override    &  4 & 1 & 5 & Emb captures signature sim \\
515	7 & Circular dep       & 14 & 10 & 2 & DF traces dependency cycle \\
516	\bottomrule
517	\end{tabular}
518	\end{table}
519	
520	\subsection{Comparison with Inference-Time Graph Methods}
521	\label{sec:inference-comparison}
522	
523	Table~\ref{tab:inference-methods} positions our approach relative to inference-time graph methods.
524	The key distinction is that these methods navigate structure at inference time, while we use structure for training-time data curation.
525	The two approaches are in principle complementary---a retriever trained with structure-grounded negatives could serve as the backbone for an inference-time graph navigator---but we have not experimentally verified this complementarity.
526	
527	\begin{table}[t]
528	\centering
529	\caption{Comparison with inference-time graph methods. StructFuse operates at training time, making it complementary.}
530	\label{tab:inference-methods}
531	\begin{tabular}{llll}
532	\toprule
533	Method & Graph type & When used & Complementary? \\
534	\midrule
535	CodexGraph & Repository graph & Inference & Yes \\
536	LocAgent   & Code structure   & Inference & Yes \\
537	RANGER     & AST + deps       & Inference & Yes \\
538	\sysname{} (ours) & Dataflow  & Training  & --- \\
539	\bottomrule
540	\end{tabular}
541	\end{table}
542	
543	%----------------------------------------------------------------------
544	\section{Discussion}
545	\label{sec:discussion}
546	
547	\paragraph{Summary of Findings.}
548	True embedding-distance mining tends to improve contrastive code retrieval over random baselines, with consistent direction across two encoders, two benchmarks, multiple seeds, and a range of hyperparameters.
549	However, effect sizes are modest (0.5--1.0\pp{} R@1 in most conditions, up to 1.8\pp{} in favorable strata), and multi-seed confidence intervals are wide (2--4\pp{}), with some seed-level deltas $< 0.5\pp$.
550	BM25-proxy negatives trend toward harm, consistent with the hypothesis that CoCoHaNeRe's reported $-27\pp{}$ was amplified by proxy conflation, but our BM25 effect is not statistically significant ($p > 0.05$).
551	
552	\paragraph{Dataflow as Exploratory Observation.}
553	Dataflow-grounded negatives show an encoder--strategy interaction: marginal positive effect on Qwen (CI includes 0) and negative effect on StarCoder.
554	This is consistent with a representation saturation hypothesis---when the encoder's pretrained space has high positive similarity (Qwen: $\text{pos\_sim} = 0.99$), structural negatives may provide an orthogonal signal dimension.
555	However, the evidence is insufficient for an independent claim, and we present this as an exploratory observation that merits further investigation with more encoders.
556	
557	\paragraph{Where Mining Matters.}
558	Stratified analysis reveals that mining benefit concentrates in specific conditions: small repositories, hard negative difficulty quartiles, and medium query-positive similarity ranges.
559	These are precisely the conditions where the encoder's ability to discriminate is most challenged.
560	However, these favorable conditions represent a minority of real-world instances, diluting the overall effect.
561	
562	\paragraph{Practical Implications.}
563	For practitioners choosing a negative mining strategy for code retrieval:
564	(1)~embedding-distance mining is a reasonable default that tends to help and is unlikely to harm;
565	(2)~avoid using BM25 top-$k$ as a proxy for embedding-distance negatives;
566	(3)~structural negatives via dataflow are not recommended as a general-purpose strategy given limited coverage (34\%), encoder-dependent effects, and modest overall benefit.
567	
568	\paragraph{Limitations.}
569	\begin{itemize}
570	    \item \textbf{Two encoders}: Our interaction finding rests on $n=2$ encoders. Generalization requires broader evaluation.
571	    \item \textbf{Pool size}: Training uses pool=50; at realistic pool sizes (200--1000+), strategy advantages shrink further (Table~\ref{tab:pool-qwen}).
572	    \item \textbf{Structural coverage}: Dataflow data is available for only 34\% of instances, diluting any structural benefit.
573	    \item \textbf{SWE-bench power}: With $N=300$ binary outcomes, SWE-bench is underpowered to detect retrieval-stage deltas $< 2\pp{}$.
574	    \item \textbf{Single training domain}: All training uses SWE-smith; domain shift to other retrieval tasks may alter findings.
575	    \item \textbf{Effect magnitude}: All observed deltas are $\leq 2\pp{}$, which may be within the noise floor for practical deployment decisions.
576	\end{itemize}
577	
578	%----------------------------------------------------------------------
579	\section{Conclusion}
580	\label{sec:conclusion}
581	
582	We presented a systematic study of hard negative mining strategies for contrastive code retrieval, comparing random, BM25-proxy, embedding-distance, and dataflow-disconnected negatives across two encoders, two benchmarks, and extensive ablations.
583	Our results suggest that true embedding-distance mining tends to help and that prior reports of harm were likely confounded by BM25-proxy conflation, though the evidence for the latter is directional rather than conclusive.
584	Structure-grounded negatives show an intriguing encoder-dependent interaction but do not provide consistent benefit and remain an exploratory observation.
585	Stratified analysis reveals that mining benefit concentrates in specific conditions, providing a representation geometry explanation for the heterogeneous findings in the literature.
586	We hope this systematic analysis helps the community make more informed choices about negative mining strategies and motivates further investigation into the interaction between encoder properties and training data curation.
587	
588	%----------------------------------------------------------------------
589	\bibliographystyle{plainnat}
590	\begin{thebibliography}{10}
591	
592	\bibitem[Karpukhin et~al.(2020)]{karpukhin2020dense}
593	V.~Karpukhin, B.~Oguz, S.~Min, P.~Lewis, L.~Wu, S.~Edunov, D.~Chen, and W.~Yih.
594	\newblock Dense passage retrieval for open-domain question answering.
595	\newblock In \emph{EMNLP}, 2020.
596	
597	\bibitem[Xiong et~al.(2021)]{xiong2021approximate}
598	L.~Xiong, C.~Xiong, Y.~Li, K.-F.~Tang, J.~Liu, P.~Bennett, J.~Ahmed, and A.~Overwijk.
599	\newblock Approximate nearest neighbor negative contrastive learning for dense text retrieval.
600	\newblock In \emph{ICLR}, 2021.
601	
602	\end{thebibliography}
603	
604	\end{document}
605	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e77aa43f-99d0-40cf-8c16-6395f40ee2c0",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a27710763487a3e39",
  "type": "user",
  "uuid": "c8137652-21cb-4e34-a6a5-5f68feca77d2",
  "sourceToolAssistantUUID": "e77aa43f-99d0-40cf-8c16-6395f40ee2c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-14T17:16:22.003Z_

Now I have a thorough understanding of the paper. Let me also check the paper summary from the user's prompt against the actual paper content -- the user's summary describes a **different version** of the paper (the "negative result" framing where "no strategy outperforms random at scale") while the actual latest paper shows a "median" tier dream with modest positive results for embedding mining. The review task describes a specific paper version with specific claims. Let me review that version as described in the prompt.

Let me check if there's a specific paper version matching the user's description (the one with "geometry equalizer" and scale ablation).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8137652-21cb-4e34-a6a5-5f68feca77d2",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qfAbMLK7mfHmsVSgoJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da8a0f0c-f7b3-49c9-8472-f4056b304d4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GpM4HMjLWDJJUMznifYbQF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7867,
      "cache_read_input_tokens": 49405,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7867,
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

_source line 30 · 2026-05-14T17:16:24.018Z_

<details open><summary>🔧 Tool call — Grep · `toolu_012GUcyEfnwmLEBbKvyirZn5`</summary>

```json
{
  "pattern": "geometry equalizer|scale ablation|monotonically|Kendall",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da8a0f0c-f7b3-49c9-8472-f4056b304d4d",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qfAbMLK7mfHmsVSgoJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b4ceb02-6675-47b9-a291-c37df698207a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GpM4HMjLWDJJUMznifYbQF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7867,
      "cache_read_input_tokens": 49405,
      "output_tokens": 269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7867
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 269,
          "cache_read_input_tokens": 49405,
          "cache_creation_input_tokens": 7867,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7867,
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

_source line 31 · 2026-05-14T17:16:24.094Z_

<details><summary>↩ Tool result · `toolu_012GUcyEfnwmLEBbKvyirZn5`</summary>

```text
Found 22 files
artifacts/dream_reports/dream_20260514T162530/logs/review_worst.log
artifacts/dream_reports/dream_20260514T162530/worst/review_context.yaml
artifacts/dream_reports/dream_20260514T162530/logs/review_median.log
artifacts/dream_reports/dream_20260514T162530/logs/review_best.log
artifacts/dream_reports/dream_20260514T162530/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260514T162530/worst/paper.aux
artifacts/dream_reports/dream_20260514T162530/worst/paper.tex
artifacts/dream_reports/dream_20260514T162530/worst/experiment_data.json
artifacts/dream_reports/dream_20260514T162530/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T162530/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260514T162530/best/paper.tex
artifacts/dream_reports/dream_20260514T162530/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260514T075732/logs/review_worst.log
artifacts/dream_reports/dream_20260514T075732/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260514T075732/worst/paper.tex
artifacts/dream_reports/dream_20260512T204322/meta.yaml
artifacts/dream_reports/dream_20260512T204322/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260512T204322/worst/paper.tex
artifacts/dream_reports/dream_20260512T204322/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260512T204322/median/paper.tex
artifacts/dream_reports/dream_20260512T204322/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T204322/logs/phase2_median_attempt0.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b4ceb02-6675-47b9-a291-c37df698207a",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a27710763487a3e39",
  "type": "user",
  "uuid": "130d13ee-76f0-4266-aff2-7aa9352aafee",
  "sourceToolAssistantUUID": "4b4ceb02-6675-47b9-a291-c37df698207a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-14T17:16:26.304Z_

The user's description matches the "worst" tier paper. Let me read it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "130d13ee-76f0-4266-aff2-7aa9352aafee",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qfo9HiS25CaS72mZsA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f839f340-e29e-43a5-b8c6-1870d8e9aae3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiTmGFK5ktBQsjtgtKteH1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 796,
      "cache_read_input_tokens": 57272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 796,
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

_source line 33 · 2026-05-14T17:16:26.707Z_

<details open><summary>🔧 Tool call — Read · `toolu_011qdcb7DGBcD8wUHtU2pdZf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper.tex",
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f839f340-e29e-43a5-b8c6-1870d8e9aae3",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qfo9HiS25CaS72mZsA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0214daba-ae8d-4473-bdd5-787875e0e83c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiTmGFK5ktBQsjtgtKteH1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 796,
      "cache_read_input_tokens": 57272,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 796
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 57272,
          "cache_creation_input_tokens": 796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 796,
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

_source line 34 · 2026-05-14T17:16:26.714Z_

<details><summary>↩ Tool result · `toolu_011qdcb7DGBcD8wUHtU2pdZf`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{graphicx}
5	\usepackage{booktabs}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{multirow}
9	\usepackage{xcolor}
10	\usepackage{hyperref}
11	
12	\title{Why Hard Negative Mining Strategies Don't Differentiate\\for Code Retrieval at Scale}
13	
14	\author{Anonymous}
15	
16	\begin{document}
17	\maketitle
18	
19	%==============================================================================
20	\begin{abstract}
21	%==============================================================================
22	Hard negative mining is widely believed to be critical for training contrastive code retrievers, yet the field lacks controlled comparisons isolating the effect of mining strategy from confounding factors such as training scale, encoder choice, and evaluation protocol.
23	We present a systematic study of four negative mining strategies---random, embedding-distance, dataflow-aware, and BM25---across two decoder-only code encoders (Qwen2.5-Coder-3B and StarCoder2-3B) with 9 random seeds per condition.
24	Our central finding is \emph{negative}: at full training scale ($\sim$44K instances), no mining strategy reliably outperforms random baselines.
25	The largest observed effect is $+0.20$ percentage points (pp) for embedding mining on Qwen ($p=0.58$), with 95\% confidence intervals spanning zero for all comparisons.
26	Strategy rankings are unstable across pool sizes (Kendall $\tau=0.33$ between pool 50 and 500), and downstream SWE-bench Lite evaluation shows no differentiation ($\Delta < 0.67$pp, bootstrap CI width $\sim$5pp).
27	We provide a mechanistic explanation: fine-tuning acts as a \emph{geometry equalizer}, collapsing pretrained margin differences across strategies by 65--78\%.
28	A data-scaling ablation reveals that mining advantages observed at pilot scale ($+1.3$pp at 1K instances) vanish monotonically with training set size, suggesting that scale substitutes for curation in contrastive code retrieval.
29	We additionally show that BM25 negatives perform indistinguishably from embedding negatives ($p > 0.42$), preventing closure of the argument that prior work's reported harm from hard negatives was caused by BM25-proxy methodology.
30	Our results caution against over-investing in mining strategy optimization and redirect attention toward training scale and inference-time structural methods.
31	\end{abstract}
32	
33	%==============================================================================
34	\section{Introduction}
35	\label{sec:intro}
36	%==============================================================================
37	
38	Repository-level code retrieval---selecting the relevant source files from a large codebase given a bug report or issue description---is a critical bottleneck in automated software repair pipelines \cite{jimenez2024swebench}.
39	Contrastive learning has emerged as the dominant paradigm for training dense code retrievers, where the choice of \emph{hard negatives} is believed to strongly influence retrieval quality.
40	
41	Prior work offers conflicting guidance on hard negative mining for code.
42	CoCoHaNeRe reports that embedding-distance negatives \emph{harm} code search by up to 27 percentage points in R@1, advocating instead for keyword-based retrieval of negatives.
43	However, this finding was obtained using BM25 as a proxy for embedding distance, raising the question of whether the reported harm reflects true embedding mining or confounds introduced by the proxy.
44	Meanwhile, the contrastive learning literature in NLP and vision consistently finds that harder negatives improve representation quality, at least up to a difficulty threshold beyond which false negatives degrade training.
45	
46	We set out to resolve this contradiction through a controlled study comparing four negative mining strategies for code retrieval: (1) random sampling, (2) true embedding-distance mining, (3) structure-grounded (dataflow-aware) mining using inter-procedural call-graph analysis, and (4) BM25-based mining.
47	We train with each strategy on two decoder-only code encoders with distinct pretrained representation geometries---Qwen2.5-Coder-3B (saturated, $\text{pos\_sim}=0.986$) and StarCoder2-3B (healthy, $\text{pos\_sim}=0.798$)---using 9 random seeds per condition to obtain reliable confidence intervals.
48	
49	Our findings are predominantly negative, which we argue is itself a contribution:
50	
51	\begin{enumerate}
52	    \item \textbf{No strategy differentiates at scale.} At full training scale ($\sim$44K instances), all mining strategies produce statistically indistinguishable R@1 on both encoders. The largest effect ($+0.20$pp) has $p=0.58$.
53	    \item \textbf{Representation geometry convergence.} Fine-tuning collapses pretrained margin differences by 65--78\%, explaining why strategies that produce different negative difficulties in the pretrained space converge after training.
54	    \item \textbf{Scale substitutes for curation.} Mining advantages observed at 1K instances ($+1.3$pp) vanish monotonically as training data grows, reaching $+0.2$pp at 5K instances.
55	    \item \textbf{BM25 $\approx$ embedding negatives.} BM25 and embedding-distance negatives are statistically indistinguishable ($p > 0.42$), preventing attribution of prior work's reported harm to the BM25-proxy methodology.
56	    \item \textbf{Unstable strategy rankings.} Rankings flip across pool sizes (stability $= 25\%$), temperatures, and encoders, indicating that reported differences in prior work may be evaluation artifacts.
57	\end{enumerate}
58	
59	These results caution practitioners against investing GPU time in sophisticated mining pipelines when simple random sampling suffices at scale, and redirect attention toward training data volume and inference-time structural navigation methods.
60	
61	%==============================================================================
62	\section{Related Work}
63	\label{sec:related}
64	%==============================================================================
65	
66	\paragraph{Hard Negative Mining for Retrieval.}
67	Hard negative mining has a long history in metric learning and dense retrieval.
68	ANCE~\cite{xiong2021approximate} periodically refreshes negatives using the current encoder, DPR~\cite{karpukhin2020dense} uses BM25 negatives for open-domain QA, and curriculum-based approaches gradually increase negative difficulty during training.
69	For code, CoCoHaNeRe reports that embedding-distance negatives harm code search, but uses BM25 as a proxy rather than true embedding distance.
70	Our work directly tests this claim with proper controls.
71	
72	\paragraph{Code Retrieval.}
73	Dense retrieval for code has been explored with encoder-only models (GraphCodeBERT, CodeBERT) and more recently with decoder-only models fine-tuned for retrieval (SweRank, SWE-Fixer).
74	These systems typically use random or in-batch negatives without systematic comparison of mining strategies.
75	RepoBench~\cite{liu2023repobench} provides a cross-file retrieval benchmark that we use for external validation.
76	
77	\paragraph{Structure-Aware Code Understanding.}
78	Graph-based approaches to code operate at either training time or inference time.
79	Training-time methods (GraphCodeBERT) encode structural features into the model.
80	Inference-time methods (CodexGraph, LocAgent, RANGER) navigate code structure during retrieval using the query context.
81	Our dataflow-aware mining falls in the training-time category; our null result suggests inference-time approaches may be more effective for leveraging structure.
82	
83	%==============================================================================
84	\section{Method}
85	\label{sec:method}
86	%==============================================================================
87	
88	\subsection{Problem Setting}
89	
90	Given a repository $\mathcal{R}$ with source files $\{f_1, \ldots, f_n\}$ and a query $q$ (e.g., a bug report), the retrieval task is to rank files by relevance.
91	We train a contrastive encoder $E_\theta$ using InfoNCE loss with temperature $\tau$:
92	\begin{equation}
93	\mathcal{L} = -\log \frac{\exp(\text{sim}(q, f^+)/\tau)}{\exp(\text{sim}(q, f^+)/\tau) + \sum_{i=1}^{K} \exp(\text{sim}(q, f_i^-)/\tau)}
94	\end{equation}
95	where $f^+$ is the gold file and $\{f_i^-\}_{i=1}^K$ are negatives selected by the mining strategy.
96	
97	\subsection{Negative Mining Strategies}
98	
99	We compare four strategies that differ only in how $\{f_i^-\}$ are selected:
100	
101	\paragraph{Random.} Sample $K$ negatives uniformly from non-gold files in the repository.
102	
103	\paragraph{Embedding-distance.} Using the pretrained encoder, compute cosine similarity between the query and all non-gold files. Select the top-$K$ most similar as hard negatives.
104	
105	\paragraph{Dataflow-aware.} Using inter-procedural call-graph analysis via CodeQL, identify files that are \emph{not} reachable from the gold file within 2 hops. Among these structurally disconnected files, select the top-$K$ by embedding similarity. This produces negatives that are semantically similar but structurally unrelated---the intuition being that structural disconnection is a stronger signal of irrelevance than embedding distance alone. Structural data is available for 34\% of training instances; the remaining 66\% fall back to embedding-distance mining.
106	
107	\paragraph{BM25.} Tokenize query and files, compute BM25 scores, select top-$K$ non-gold files. This replicates the methodology attributed to ``embedding negatives'' in prior work.
108	
109	\subsection{Encoders}
110	
111	We fine-tune two 3B-parameter decoder-only code models using LoRA:
112	
113	\begin{itemize}
114	    \item \textbf{Qwen2.5-Coder-3B}: Pretrained with Fill-in-the-Middle. Exhibits saturated representation geometry ($\text{pos\_sim}=0.986$, margin $= 0.074$ for random negatives).
115	    \item \textbf{StarCoder2-3B}: Pretrained with Fill-in-the-Middle on a different corpus. Healthier geometry ($\text{pos\_sim}=0.798$, margin $= 0.194$ for random negatives).
116	\end{itemize}
117	
118	\subsection{Training Protocol}
119	
120	All models are trained on $\sim$44K instances from SWE-smith with $K=3$ negatives, $\tau=0.05$, LoRA rank 16, for 3 epochs.
121	Each strategy $\times$ encoder combination is trained with 9 random seeds.
122	Evaluation uses R@1 at pool size 50 on a held-out validation set unless otherwise noted.
123	
124	%==============================================================================
125	\section{Experiments}
126	\label{sec:experiments}
127	%==============================================================================
128	
129	\subsection{Main Result: No Strategy Differentiates at Full Scale}
130	\label{sec:main_result}
131	
132	Table~\ref{tab:main} presents the central result.
133	On Qwen, embedding mining achieves $+0.20$pp over random ($p=0.58$); on StarCoder, it achieves $-0.35$pp ($p=0.47$).
134	Neither difference is statistically significant, and the signs are inconsistent across encoders---a signature of noise, not signal.
135	Dataflow-aware mining shows slight harm on both encoders ($-0.45$pp Qwen, $-1.50$pp StarCoder), with the StarCoder result reaching $p=0.015$ before multiple-testing correction but not surviving Bonferroni adjustment across the study's comparisons.
136	
137	\begin{table}[t]
138	\centering
139	\caption{Full-scale R@1 by strategy and encoder (9 seeds, pool=50). No strategy significantly outperforms random.}
140	\label{tab:main}
141	\small
142	\begin{tabular}{llcccc}
143	\toprule
144	\textbf{Encoder} & \textbf{Strategy} & \textbf{Mean R@1} & \textbf{Std} & \textbf{95\% CI} & \textbf{$\Delta$ vs Rand} \\
145	\midrule
146	\multirow{3}{*}{Qwen} & Random & 0.529 & 0.009 & [.522, .536] & --- \\
147	 & Embedding & 0.531 & 0.009 & [.524, .538] & +0.20pp \\
148	 & Dataflow & 0.525 & 0.011 & [.516, .533] & $-$0.45pp \\
149	\midrule
150	\multirow{3}{*}{StarCoder} & Random & 0.443 & 0.011 & [.435, .451] & --- \\
151	 & Embedding & 0.440 & 0.012 & [.430, .449] & $-$0.35pp \\
152	 & Dataflow & 0.428 & 0.014 & [.418, .438] & $-$1.50pp \\
153	\bottomrule
154	\end{tabular}
155	\end{table}
156	
157	Seed-to-seed variance ($\sigma \approx 0.009$--$0.014$) exceeds the strategy effects in all cases.
158	The confidence intervals for all pairwise strategy comparisons include zero:
159	embedding $-$ random on Qwen: $[-0.62, +1.02]$pp;
160	embedding $-$ random on StarCoder: $[-1.4, +0.7]$pp;
161	dataflow $-$ random on StarCoder: $[-3.1, +0.1]$pp.
162	
163	\subsection{BM25 Negatives Match Embedding Negatives}
164	\label{sec:bm25}
165	
166	Table~\ref{tab:bm25} adds BM25 as a fourth strategy.
167	BM25 negatives are statistically indistinguishable from embedding negatives on both encoders (Qwen: $-0.35$pp, $p=0.42$; StarCoder: $-0.25$pp, $p=0.55$).
168	This prevents closing the argument that prior work's reported harm from hard negatives was caused by the BM25-proxy methodology specifically.
169	The high overlap ($\sim$60\%) between BM25 and embedding top-$K$ negatives at full scale explains this convergence.
170	
171	\begin{table}[t]
172	\centering
173	\caption{Four-strategy comparison including BM25 baseline. BM25 and embedding negatives are indistinguishable.}
174	\label{tab:bm25}
175	\small
176	\begin{tabular}{lccccc}
177	\toprule
178	\textbf{Encoder} & \textbf{Random} & \textbf{Embedding} & \textbf{Dataflow} & \textbf{BM25} & \textbf{BM25$-$Emb} \\
179	\midrule
180	Qwen & 0.529 & 0.531 & 0.525 & 0.528 & $-$0.35pp \\
181	StarCoder & 0.443 & 0.440 & 0.428 & 0.437 & $-$0.25pp \\
182	\bottomrule
183	\end{tabular}
184	\end{table}
185	
186	We observe that CoCoHaNeRe's reported $-27$pp harm was not reproduced in our controlled setup with either BM25 or embedding negatives, suggesting the effect is attributable to other experimental differences (scale, encoder, evaluation protocol) rather than the BM25-vs-embedding distinction.
187	
188	\subsection{No Downstream Signal on SWE-bench Lite}
189	\label{sec:swebench}
190	
191	Table~\ref{tab:swebench} reports end-to-end resolve rates on SWE-bench Lite (300 instances) using a Qwen3.6-27B agent.
192	The largest gap across all conditions is 3.0pp (Qwen-embedding 25.0\% vs StarCoder-dataflow 22.0\%), well within the $\pm$5pp binomial confidence interval.
193	Bootstrap resampling (10,000 iterations) confirms all pairwise comparisons are non-significant ($p > 0.80$).
194	
195	\begin{table}[t]
196	\centering
197	\caption{SWE-bench Lite resolve rates. No mining strategy produces detectable downstream improvement.}
198	\label{tab:swebench}
199	\small
200	\begin{tabular}{llccc}
201	\toprule
202	\textbf{Encoder} & \textbf{Strategy} & \textbf{Resolve \%} & \textbf{$\Delta$ vs Rand} & \textbf{95\% Boot.\ CI} \\
203	\midrule
204	\multirow{3}{*}{Qwen} & Random & 24.67 & --- & [19.9, 29.4] \\
205	 & Embedding & 25.00 & +0.33pp & [20.2, 29.8] \\
206	 & Dataflow & 24.33 & $-$0.33pp & [19.6, 29.1] \\
207	\midrule
208	\multirow{3}{*}{StarCoder} & Random & 22.67 & --- & [18.0, 27.3] \\
209	 & Embedding & 22.33 & $-$0.34pp & [17.7, 27.0] \\
210	 & Dataflow & 22.00 & $-$0.67pp & [17.3, 26.7] \\
211	\bottomrule
212	\end{tabular}
213	\end{table}
214	
215	With 300 binary outcomes at a base rate of $\sim$25\%, the binomial standard error is $\sqrt{0.25 \times 0.75 / 300} \approx 0.025$, yielding a CI half-width of $\sim$5pp.
216	Detecting a 0.5pp retrieval difference would require $N \approx 60{,}000$ instances.
217	This is not a power problem we can fix---it is a fundamental limitation of downstream evaluation for detecting sub-1pp retrieval differences.
218	
219	\subsection{External Validation: RepoBench-R}
220	\label{sec:repobench}
221	
222	Table~\ref{tab:repobench} reports R@1 on RepoBench-R (easy and hard splits, $\sim$8K instances each).
223	All confidence intervals overlap across strategies.
224	The inconsistent sign pattern across encoders (positive for Qwen, negative for StarCoder) replicates the main result: strategy differences are noise.
225	
226	\begin{table}[t]
227	\centering
228	\caption{RepoBench-R R@1 (\%) by strategy, encoder, and split. $\pm$ indicates 95\% bootstrap CI half-width.}
229	\label{tab:repobench}
230	\small
231	\begin{tabular}{llcccc}
232	\toprule
233	\textbf{Split} & \textbf{Encoder} & \textbf{Random} & \textbf{Embedding} & \textbf{Dataflow} & \textbf{$\Delta$ E$-$R} \\
234	\midrule
235	\multirow{2}{*}{Easy} & Qwen & 71.2$\pm$1.4 & 71.5$\pm$1.5 & 70.9$\pm$1.6 & +0.3pp \\
236	 & StarCoder & 68.5$\pm$1.6 & 68.1$\pm$1.7 & 67.8$\pm$1.8 & $-$0.4pp \\
237	\midrule
238	\multirow{2}{*}{Hard} & Qwen & 43.1$\pm$2.0 & 43.4$\pm$2.1 & 42.7$\pm$2.2 & +0.3pp \\
239	 & StarCoder & 39.8$\pm$2.2 & 39.3$\pm$2.4 & 38.9$\pm$2.5 & $-$0.5pp \\
240	\bottomrule
241	\end{tabular}
242	\end{table}
243	
244	\subsection{Stratified Analysis}
245	\label{sec:stratified}
246	
247	Table~\ref{tab:stratified} breaks down the embedding-minus-random delta across five strata on Qwen.
248	No stratum produces a significant effect after Bonferroni correction (10 comparisons, $\alpha_{\text{adj}}=0.005$).
249	The most informative finding: the 34\% of instances with structural data show a tiny positive dataflow signal ($+0.40$pp), completely washed out by the 66\% fallback instances.
250	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0214daba-ae8d-4473-bdd5-787875e0e83c",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a27710763487a3e39",
  "type": "user",
  "uuid": "4ce0b0b3-fe6b-48ba-8a61-16947c1cd2e5",
  "sourceToolAssistantUUID": "0214daba-ae8d-4473-bdd5-787875e0e83c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T17:16:30.807Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R1SSWmkvpXoSz4FQvbxt7D`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/paper.tex",
  "offset": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ce0b0b3-fe6b-48ba-8a61-16947c1cd2e5",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qfzVR2erseZxgDEq6n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4f865a1-c2ca-4c79-93dc-c0ddeb4796f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BpVvQeVhFt8oqzU23pwAc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5765,
      "cache_read_input_tokens": 58068,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5765,
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

_source line 36 · 2026-05-14T17:16:30.814Z_

<details><summary>↩ Tool result · `toolu_01R1SSWmkvpXoSz4FQvbxt7D`</summary>

```text
250	
251	\begin{table}[t]
252	\centering
253	\caption{Per-stratum $\Delta$(embedding $-$ random) R@1 on Qwen. None significant after correction.}
254	\label{tab:stratified}
255	\small
256	\begin{tabular}{lccc}
257	\toprule
258	\textbf{Stratum} & \textbf{$N$} & \textbf{$\Delta$ R@1 (pp)} & \textbf{95\% CI} \\
259	\midrule
260	Repo small ($<$200 files) & 4,596 & +0.80 & [$-$1.5, +3.1] \\
261	Repo large ($\geq$200 files) & 39,577 & $-$0.15 & [$-$0.9, +0.6] \\
262	Pool small ($<$30) & 12,044 & +0.35 & [$-$1.2, +1.9] \\
263	Pool large ($\geq$30) & 32,129 & $-$0.20 & [$-$1.0, +0.6] \\
264	High query-pos sim ($>$0.95) & 28,800 & $-$0.10 & [$-$0.8, +0.6] \\
265	Low query-pos sim ($\leq$0.95) & 15,373 & +0.55 & [$-$0.9, +2.0] \\
266	Struct.\ available (34\%) & 15,133 & +0.15 & [$-$1.2, +1.5] \\
267	Struct.\ fallback (66\%) & 29,040 & +0.25 & [$-$0.5, +1.0] \\
268	Neg.\ diff.\ Q1 (easiest) & 11,043 & +0.60 & [$-$1.5, +2.7] \\
269	Neg.\ diff.\ Q4 (hardest) & 11,043 & $-$0.30 & [$-$2.3, +1.7] \\
270	\bottomrule
271	\end{tabular}
272	\end{table}
273	
274	\subsection{Pool Size Sensitivity}
275	\label{sec:pool}
276	
277	Table~\ref{tab:pool} evaluates strategy rankings at pool sizes $\{50, 100, 200, 500\}$.
278	Strategy rankings are highly unstable: the best strategy changes 3 times across 4 pool sizes (stability $= 25\%$), and Kendall's $\tau$ between pool-50 and pool-500 rankings is only 0.33.
279	This instability holds for both encoders.
280	
281	\begin{table}[t]
282	\centering
283	\caption{Strategy ranking stability across pool sizes (Qwen).}
284	\label{tab:pool}
285	\small
286	\begin{tabular}{lcccc}
287	\toprule
288	\textbf{Pool} & \textbf{Rand R@1} & \textbf{Emb R@1} & \textbf{DF R@1} & \textbf{Best} \\
289	\midrule
290	50 & 0.529 & 0.531 & 0.525 & Emb \\
291	100 & 0.412 & 0.409 & 0.405 & Rand \\
292	200 & 0.324 & 0.327 & 0.325 & Emb \\
293	500 & 0.231 & 0.229 & 0.230 & Rand \\
294	\bottomrule
295	\end{tabular}
296	\end{table}
297	
298	\begin{table}[t]
299	\centering
300	\caption{Strategy ranking stability across pool sizes (StarCoder).}
301	\label{tab:pool_sc}
302	\small
303	\begin{tabular}{lcccc}
304	\toprule
305	\textbf{Pool} & \textbf{Rand R@1} & \textbf{Emb R@1} & \textbf{DF R@1} & \textbf{Best} \\
306	\midrule
307	50 & 0.443 & 0.440 & 0.428 & Rand \\
308	100 & 0.341 & 0.338 & 0.331 & Rand \\
309	200 & 0.262 & 0.264 & 0.259 & Emb \\
310	500 & 0.178 & 0.175 & 0.177 & Rand \\
311	\bottomrule
312	\end{tabular}
313	\end{table}
314	
315	\subsection{Scale-Dependent Strategy Effects}
316	\label{sec:scale}
317	
318	Table~\ref{tab:scale} reveals the paper's most explanatory result.
319	At 1K training instances, embedding mining shows $+1.3$pp---consistent with pilot-scale findings.
320	This advantage decreases monotonically to $+0.6$pp at 3K and $+0.2$pp at 5K (full scale).
321	Dataflow mining follows the same pattern, dropping from $+0.7$pp to $-0.45$pp.
322	
323	\begin{table}[t]
324	\centering
325	\caption{Strategy effects decrease monotonically with training scale (Qwen, 1 seed).}
326	\label{tab:scale}
327	\small
328	\begin{tabular}{lcccc}
329	\toprule
330	\textbf{Train size} & \textbf{Rand R@1} & \textbf{Emb R@1} & \textbf{$\Delta$ (pp)} & \textbf{DF $\Delta$ (pp)} \\
331	\midrule
332	1K & 0.505 & 0.518 & +1.30 & +0.70 \\
333	3K & 0.520 & 0.526 & +0.60 & +0.10 \\
334	5K (full) & 0.529 & 0.531 & +0.20 & $-$0.45 \\
335	\bottomrule
336	\end{tabular}
337	\end{table}
338	
339	The mechanism is straightforward: with more training data, random negatives sample a wider region of the embedding space, effectively approximating the coverage that curated negatives provide by design.
340	At small scale, curated negatives concentrate training signal on the decision boundary; at large scale, random sampling covers the boundary through sheer volume.
341	This phenomenon parallels batch-size scaling effects observed in visual contrastive learning.
342	
343	\subsection{Failure Analysis}
344	\label{sec:failure}
345	
346	Manual categorization of 50 retrieval failures (cases where all strategies fail) reveals a ceiling on the potential benefit of any mining strategy (Table~\ref{tab:failure}).
347	The dominant failure mode (36\%) is that the gold file is lexically dissimilar to the query, requiring fundamentally different approaches (e.g., multi-modal queries with error traces).
348	Only 10\% of failures involve cases where structural connectivity could plausibly help.
349	
350	\begin{table}[t]
351	\centering
352	\caption{Failure category breakdown ($n=50$). Structure can address only $\sim$10\% of failures.}
353	\label{tab:failure}
354	\small
355	\begin{tabular}{lcc}
356	\toprule
357	\textbf{Category} & \textbf{Count} & \textbf{\%} \\
358	\midrule
359	Gold file lexically dissimilar & 18 & 36 \\
360	Config / test / non-code files & 12 & 24 \\
361	Large repo dilution ($>$500 files) & 8 & 16 \\
362	Cross-language dependency & 4 & 8 \\
363	Structural connectivity helps & 5 & 10 \\
364	Ambiguous & 3 & 6 \\
365	\bottomrule
366	\end{tabular}
367	\end{table}
368	
369	\subsection{Representation Geometry Convergence}
370	\label{sec:geometry}
371	
372	Table~\ref{tab:geometry} presents the mechanistic core of our analysis.
373	Before fine-tuning, mining strategies produce markedly different negative difficulties: on Qwen, random negatives have margin 0.074 while embedding negatives have margin 0.017 (ratio 4.35$\times$).
374	After fine-tuning, this ratio collapses to 1.29$\times$ (margins 0.067 vs.\ 0.052).
375	Fine-tuning erases 78\% of the pretrained margin difference on Qwen and 65\% on StarCoder.
376	
377	\begin{table}[t]
378	\centering
379	\caption{Representation geometry pre- vs.\ post-fine-tuning. Fine-tuning collapses margin differences across strategies.}
380	\label{tab:geometry}
381	\small
382	\begin{tabular}{llcccc}
383	\toprule
384	\textbf{Encoder} & \textbf{Phase} & \textbf{Rand.\ margin} & \textbf{Emb.\ margin} & \textbf{DF margin} & \textbf{Ratio (R/E)} \\
385	\midrule
386	\multirow{2}{*}{Qwen} & Pretrained & 0.074 & 0.017 & 0.029 & 4.35 \\
387	 & Fine-tuned & 0.067 & 0.052 & 0.059 & 1.29 \\
388	\midrule
389	\multirow{2}{*}{StarCoder} & Pretrained & 0.194 & 0.067 & 0.119 & 2.90 \\
390	 & Fine-tuned & 0.073 & 0.057 & 0.065 & 1.28 \\
391	\bottomrule
392	\end{tabular}
393	\end{table}
394	
395	The contrastive objective drives all strategies toward the same representation geometry regardless of the specific negatives used.
396	Pretrained geometry---which determines initial negative difficulty---is a transient condition that gets erased during training.
397	This explains why pilot-scale results showed strategy effects (insufficient training to erase geometry) while full-scale results do not (sufficient training to converge).
398	
399	%==============================================================================
400	\section{Discussion}
401	\label{sec:discussion}
402	%==============================================================================
403	
404	\paragraph{Why strategies converge.}
405	The representation geometry analysis (\S\ref{sec:geometry}) provides a unified explanation.
406	The contrastive loss optimizes for a target geometry (margins that minimize loss), and LoRA fine-tuning has sufficient capacity to reach this target from any starting point defined by the mining strategy.
407	Different strategies change the \emph{path} through representation space but converge to the same \emph{destination}.
408	At small scale (\S\ref{sec:scale}), training is insufficient to complete this convergence, so initial differences persist and strategy choice matters.
409	At full scale, convergence is complete and strategy choice is irrelevant.
410	
411	\paragraph{Implications for the BM25-proxy debate.}
412	Our finding that BM25 and embedding negatives are indistinguishable (\S\ref{sec:bm25}) means that prior work's reported harm cannot be attributed to the BM25-vs-embedding distinction.
413	We observe that CoCoHaNeRe's $-27$pp effect was not reproduced in our setup with either method, suggesting other experimental factors (training scale, encoder architecture, evaluation protocol) are responsible.
414	We frame this as an \emph{observation} rather than a correction, as we cannot fully disentangle the confounds.
415	
416	\paragraph{Training-time vs.\ inference-time structure.}
417	Our null result for dataflow-aware training-time mining contrasts with reported gains from inference-time graph navigation methods (LocAgent: $+8$--$12$pp on SWE-bench; CodexGraph: $+5$pp).
418	The key difference: training-time mining fixes structural signal at corpus construction time, but the relevant structure changes per query.
419	Inference-time methods adapt structural navigation to the specific query context.
420	This reframes our contribution: structure matters for code retrieval, but the mechanism for incorporating it should be inference-time navigation, not training-time negative curation.
421	
422	\paragraph{Practical recommendations.}
423	\begin{enumerate}
424	    \item If your training set exceeds $\sim$5K instances, random negative sampling is sufficient. Save the GPU time that would be spent on mining.
425	    \item If your training set is small ($<$2K), embedding-distance mining provides a modest benefit ($+1.3$pp) worth the overhead.
426	    \item Do not optimize mining strategy based on a single pool size---rankings are unstable (Kendall $\tau = 0.33$).
427	    \item For leveraging code structure in retrieval, invest in inference-time graph navigation rather than training-time negative mining.
428	    \item If structural negative mining is attempted, invest in extraction coverage first: at 34\% coverage, the structural signal is too diluted to surface.
429	\end{enumerate}
430	
431	\paragraph{Limitations.}
432	Our study uses two 3B-parameter encoders; larger models may exhibit different convergence behavior.
433	All training uses LoRA; full fine-tuning might preserve more strategy-specific signal.
434	The dataflow extraction covers only 34\% of instances; higher coverage might change the dataflow result, though the stratified analysis (\S\ref{sec:stratified}) suggests the effect would remain small.
435	SWE-bench Lite's 300 instances provide limited statistical power for downstream evaluation.
436	
437	%==============================================================================
438	\section{Conclusion}
439	\label{sec:conclusion}
440	%==============================================================================
441	
442	We presented a controlled study of hard negative mining strategies for contrastive code retrieval, finding that no strategy---embedding-distance, dataflow-aware, or BM25---reliably outperforms random baselines at full training scale.
443	The representation geometry convergence analysis reveals the mechanism: fine-tuning acts as a geometry equalizer, collapsing pretrained margin differences by 65--78\% and rendering the initial negative difficulty distribution irrelevant.
444	Data-scaling ablations show that mining advantages observed at pilot scale vanish monotonically with training set size, consistent with scale substituting for curation.
445	
446	Our negative results carry actionable implications: practitioners should prioritize training data volume over mining sophistication, use random negatives at scale, and leverage code structure through inference-time navigation rather than training-time negative selection.
447	We hope this work encourages the community to report and value negative results in retrieval research, where publication bias toward positive findings can mislead practitioners into over-investing in techniques that do not survive rigorous evaluation.
448	
449	%==============================================================================
450	\appendix
451	\section{Temperature Ablation}
452	\label{app:temperature}
453	%==============================================================================
454	
455	Table~\ref{tab:temp} shows that the null result holds across temperatures $\tau \in \{0.05, 0.10, 0.20\}$.
456	Strategy rankings are unstable across temperatures (embedding leads at $\tau=0.10$ but trails at $\tau=0.20$), confirming the absence of a robust strategy effect.
457	Higher temperatures degrade all strategies uniformly by $\sim$2.5pp at $\tau=0.20$.
458	
459	\begin{table}[h]
460	\centering
461	\caption{Temperature $\times$ strategy interaction (R@1, Qwen).}
462	\label{tab:temp}
463	\small
464	\begin{tabular}{lcccc}
465	\toprule
466	$\tau$ & \textbf{Random} & \textbf{Embedding} & $\Delta$ \textbf{E$-$R} & $\Delta$ \textbf{DF$-$R} \\
467	\midrule
468	0.05 & 0.529 & 0.531 & +0.20pp & $-$0.45pp \\
469	0.10 & 0.522 & 0.525 & +0.35pp & $-$0.15pp \\
470	0.20 & 0.504 & 0.503 & $-$0.10pp & $-$0.25pp \\
471	\bottomrule
472	\end{tabular}
473	\end{table}
474	
475	%==============================================================================
476	\section{Dynamic Mining Ablation}
477	\label{app:dynamic}
478	%==============================================================================
479	
480	Re-mining embedding negatives per epoch (dynamic) vs.\ once from the pretrained encoder (static) yields negligible improvement (Table~\ref{tab:dynamic}): $+0.05$pp on both encoders at $3.4\times$ time overhead.
481	The encoder changes minimally during LoRA fine-tuning (cosine similarity between epoch-0 and epoch-3 embeddings $>0.995$), so dynamic and static negatives are nearly identical.
482	
483	\begin{table}[h]
484	\centering
485	\caption{Static vs.\ dynamic embedding mining.}
486	\label{tab:dynamic}
487	\small
488	\begin{tabular}{lcccc}
489	\toprule
490	\textbf{Encoder} & \textbf{Static R@1} & \textbf{Dynamic R@1} & $\Delta$ \textbf{(pp)} & \textbf{Time $\times$} \\
491	\midrule
492	Qwen & 0.531 & 0.532 & +0.05 & 3.4$\times$ \\
493	StarCoder & 0.440 & 0.440 & +0.05 & 3.4$\times$ \\
494	\bottomrule
495	\end{tabular}
496	\end{table}
497	
498	%==============================================================================
499	\section{Hop Count Ablation}
500	\label{app:hop}
501	%==============================================================================
502	
503	Expanding call-graph scope from 1-hop to 3-hop does not rescue the dataflow strategy (Table~\ref{tab:hop}).
504	All hop counts produce R@1 within noise of random (0.529).
505	3-hop slightly worsens performance by over-expanding the connected set, reducing the pool of available structural negatives.
506	
507	\begin{table}[h]
508	\centering
509	\caption{Hop count ablation (Qwen, dataflow strategy, 1 seed).}
510	\label{tab:hop}
511	\small
512	\begin{tabular}{lcccc}
513	\toprule
514	\textbf{Hops} & \textbf{Connected/query} & \textbf{Neg.\ available} & \textbf{R@1} & $\Delta$ \textbf{vs Rand} \\
515	\midrule
516	1 & 2.1 & 47.9 & 0.523 & $-$0.60pp \\
517	2 & 4.8 & 45.2 & 0.525 & $-$0.45pp \\
518	3 & 11.3 & 38.7 & 0.521 & $-$0.80pp \\
519	\bottomrule
520	\end{tabular}
521	\end{table}
522	
523	%==============================================================================
524	\section{Fusion Head Ablation}
525	\label{app:fusion}
526	%==============================================================================
527	
528	Adding structural features at inference time via a combined scoring head does not improve over embedding-only retrieval (Table~\ref{tab:fusion}).
529	The structural-only head performs poorly (R@1 $= 0.312$), and the combined head slightly underperforms embedding-only ($-0.25$pp), suggesting the model learns to partially ignore the noisy structural channel.
530	
531	\begin{table}[h]
532	\centering
533	\caption{Fusion head ablation (Qwen, best checkpoint).}
534	\label{tab:fusion}
535	\small
536	\begin{tabular}{lccc}
537	\toprule
538	\textbf{Head} & \textbf{R@1} & \textbf{R@5} & $\Delta$ \textbf{vs Emb} \\
539	\midrule
540	Embedding only & 0.531 & 0.960 & --- \\
541	Structural only & 0.312 & 0.620 & $-$21.9pp \\
542	Combined & 0.529 & 0.955 & $-$0.25pp \\
543	\bottomrule
544	\end{tabular}
545	\end{table}
546	
547	%==============================================================================
548	\section{Distance Weighting Ablation}
549	\label{app:distance}
550	%==============================================================================
551	
552	Using dataflow-distance-weighted negative selection instead of binary connected/disconnected yields a marginal $+0.10$pp over binary, still underperforming random by $0.35$pp (Table~\ref{tab:dist_weight}).
553	
554	\begin{table}[h]
555	\centering
556	\caption{Distance weighting ablation (Qwen, 1 seed).}
557	\label{tab:dist_weight}
558	\small
559	\begin{tabular}{lccc}
560	\toprule
561	\textbf{Selection} & \textbf{R@1} & $\Delta$ \textbf{vs Rand} & $\Delta$ \textbf{vs Binary} \\
562	\midrule
563	Random & 0.529 & --- & --- \\
564	Binary disconnect & 0.525 & $-$0.45pp & --- \\
565	Distance weighted & 0.526 & $-$0.35pp & +0.10pp \\
566	\bottomrule
567	\end{tabular}
568	\end{table}
569	
570	\begin{thebibliography}{9}
571	
572	\bibitem{jimenez2024swebench}
573	Carlos~E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan.
574	\newblock {SWE-bench}: Can language models resolve real-world {GitHub} issues?
575	\newblock In \emph{Proc.\ ICLR}, 2024.
576	
577	\bibitem{xiong2021approximate}
578	Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, and Arnold Overwijk.
579	\newblock Approximate nearest neighbor negative contrastive learning for dense text retrieval.
580	\newblock In \emph{Proc.\ ICLR}, 2021.
581	
582	\bibitem{karpukhin2020dense}
583	Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, and Wen-tau Yih.
584	\newblock Dense passage retrieval for open-domain question answering.
585	\newblock In \emph{Proc.\ EMNLP}, 2020.
586	
587	\bibitem{liu2023repobench}
588	Tianyang Liu, Canwen Xu, and Julian McAuley.
589	\newblock {RepoBench}: Benchmarking repository-level code auto-completion systems.
590	\newblock In \emph{Proc.\ ICLR}, 2024.
591	
592	\end{thebibliography}
593	
594	\end{document}
595	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4f865a1-c2ca-4c79-93dc-c0ddeb4796f4",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a27710763487a3e39",
  "type": "user",
  "uuid": "b3e298a9-6b75-44f0-8c64-80d69c8e5343",
  "sourceToolAssistantUUID": "f4f865a1-c2ca-4c79-93dc-c0ddeb4796f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-14T17:16:33.868Z_

Now I have the complete paper. Let me also check if there are review reports from prior dreams that I should be aware of for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3e298a9-6b75-44f0-8c64-80d69c8e5343",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qgJQg4mom8xhLBQSy2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0bd0db87-c578-45d6-9ea4-21c6044fd221",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YHh7iYEhuJupJUMLHjxeEN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6452,
      "cache_read_input_tokens": 63833,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6452,
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

_source line 38 · 2026-05-14T17:16:36.518Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Cz7zrQbBbvDuvXTEjBQzf5`</summary>

```json
{
  "pattern": "**/dream_20260514T162530/**/review_report.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bd0db87-c578-45d6-9ea4-21c6044fd221",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qgJQg4mom8xhLBQSy2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "732c4c15-ce9b-4d33-a24d-80f076618f69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YHh7iYEhuJupJUMLHjxeEN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6452,
      "cache_read_input_tokens": 63833,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6452,
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

_source line 39 · 2026-05-14T17:16:36.536Z_

<details><summary>↩ Tool result · `toolu_01Cz7zrQbBbvDuvXTEjBQzf5`</summary>

```text
artifacts/dream_reports/dream_20260514T162530/best/review_report.md
artifacts/dream_reports/dream_20260514T162530/median/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "732c4c15-ce9b-4d33-a24d-80f076618f69",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a27710763487a3e39",
  "type": "user",
  "uuid": "cbfba2a1-631b-46f8-8f85-da30b50e9b98",
  "sourceToolAssistantUUID": "732c4c15-ce9b-4d33-a24d-80f076618f69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-14T17:17:32.674Z_

I now have a thorough understanding of the paper, its history, and the project context. Here is my review.

---

## Reviewer R2: Novelty and Related Work

**Focus: Novelty, Related Work Completeness, Positioning, Contribution Significance, Framing**

### Summary

This paper compares four hard negative mining strategies (random, embedding-distance, dataflow-aware, BM25) for contrastive code retrieval, finding that no strategy outperforms random at full training scale (~44K instances). The authors propose "geometry equalization" as a mechanistic explanation: fine-tuning collapses pretrained margin differences by 65-78%, rendering mining strategy choice irrelevant. A scale ablation shows mining advantages at 1K instances vanish by 5K. The paper positions itself as a negative-result contribution.

### Strengths

- **Thorough experimental design.** 9 seeds per condition, two encoders with distinct representation geometries, multiple benchmarks, bootstrap CIs, and extensive ablations (temperature, dynamic mining, hop count, fusion head, distance weighting). This is substantially more rigorous than most positive-result papers.
- **Geometry convergence analysis is the paper's strongest contribution.** The pre- vs. post-fine-tuning margin analysis (Table 8) and the monotonic scale ablation (Table 7) provide a concrete, testable mechanism for why strategies converge. This is more explanatory than simply reporting null results.
- **Honest uncertainty quantification.** The paper consistently reports p-values, CIs, and acknowledges power limitations (e.g., SWE-bench N=300 is underpowered). This contrasts favorably with the field norm of reporting point estimates without uncertainty.
- **Pool size instability finding is novel and practically useful.** Kendall tau = 0.33 across pool sizes is an important caution against evaluation-dependent conclusions in retrieval research.

### Weaknesses

- **The negative result is not sufficiently surprising to justify acceptance at a top venue.** That contrastive learning converges to similar representations regardless of negative sampling strategy is a well-known phenomenon. SimCLR (Chen et al., 2020) demonstrated that batch size (i.e., more random negatives) substitutes for negative curation. The "scale substitutes for curation" finding restates this insight in the code domain without adding new theoretical understanding. The paper's geometry convergence analysis is descriptive rather than predictive -- it documents convergence after the fact but does not predict the convergence rate or identify the critical scale threshold.
- **Related work is critically underdeveloped.** The paper cites only 4 references. For a venue submission, this is unacceptable. Major omissions include:
  - **False negative decontamination** (e.g., Qu et al., 2021): Hard negatives that are actually positives degrade training. The paper never discusses whether its strategies suffer from false negatives.
  - **SimCSE** (Gao et al., 2021): Demonstrated that dropout-based augmentation can match hard negative mining for sentence embeddings -- directly relevant to the "mining doesn't matter" conclusion.
  - **E5** (Wang et al., 2022): Large-scale text embedding with sophisticated negative mining that shows clear improvements at scale, potentially contradicting this paper's conclusion.
  - **CodeSearchNet** (Husain et al., 2019), **UniXcoder** (Guo et al., 2022), **CodeT5+** (Wang et al., 2023): Major code retrieval baselines completely absent.
  - **Curriculum learning for negatives** (Bengio et al., 2009 framework; specific retrieval instantiations): Mentioned in passing but no citations.
  - **In-batch negatives** literature: The interaction between mined negatives and in-batch negatives is never discussed.
  - **GraphCodeBERT** (Guo et al., 2021), **CodeBERT** (Feng et al., 2020): Named but not cited.
  - The CoCoHaNeRe work is central to the paper's framing but has no formal citation and no verified publication details.
- **CoCoHaNeRe framing is problematic.** The paper builds its narrative around "correcting" or "contextualizing" CoCoHaNeRe's -27pp finding, but (a) CoCoHaNeRe is not formally cited, making verification impossible; (b) the paper's own BM25 result (p > 0.42) fails to demonstrate that BM25 negatives are harmful, undermining the proxy-conflation hypothesis; (c) the paper ultimately acknowledges it "cannot fully disentangle the confounds." This leaves the CoCoHaNeRe framing as a narrative device rather than a scientific contribution.
- **5K instances is not "at scale."** The title claims strategies "don't differentiate at scale," but 5K training instances is small by modern standards. DPR uses ~60K, ANCE uses >100K, and large-scale retrieval training routinely uses millions of examples. The geometry convergence mechanism might not hold at 100K+ instances where longer training could differentiate strategies again. The paper's "scale" claim would be more accurately stated as "at moderate scale."
- **Training with K=3 negatives is unusually low.** Most contrastive retrieval work uses K=7-15 hard negatives per query. With K=3, the discrimination signal from mining is inherently weak, potentially biasing toward the null result. This confound is not discussed.
- **LoRA-specific limitation is underexplored.** The paper acknowledges "full fine-tuning might preserve more strategy-specific signal" but treats this as a minor limitation. Given that LoRA constrains the update space, the geometry convergence may be an artifact of limited model capacity for differentiation rather than a general property of contrastive fine-tuning.

### Questions for Authors

1. Have you verified that CoCoHaNeRe is a published, peer-reviewed work? The absence of a formal citation raises concerns about whether the paper's central framing target is a strawman.
2. What happens with K=7 or K=15 negatives? The unusually low K=3 could be driving the null result by limiting the gradient signal from any mining strategy.
3. The scale ablation uses only 1 seed (Table 7 caption). How robust is the monotonic trend across seeds?
4. Have you measured the false negative rate for each mining strategy? Embedding-distance mining at high recall may select actual positives as negatives, which would mask its benefit.
5. Why not include encoder-only models (e.g., CodeBERT, GraphCodeBERT) as additional encoders? Two decoder-only models with similar architectures limit the generality of the geometry convergence claim.

### Minor Issues

- Table 7 uses 1 seed, contradicting the 9-seed rigor of the main result. This key ablation should use all 9 seeds.
- The SimCLR batch-size analogy is made without citation.
- "Decoder-only encoders" is a confusing term -- clarify as "decoder-only models used as encoders."
- Section 5 practical recommendation #1 ("if your training set exceeds ~5K") is stated too confidently given the study's narrow scope (2 encoders, 1 domain, LoRA only).
- The bibliography format is inconsistent (some entries have "Proc." prefix, others do not).

### Score and Confidence

**Score: 3 (Weak Reject)**

**Confidence: 4/5 (High)**

**Justification:** The paper is well-executed experimentally but falls short on novelty and related work -- the two criteria most critical for my review focus. The negative result that "random negatives suffice at scale" is predictable from existing contrastive learning theory and has been observed (though less systematically) in NLP retrieval. The geometry convergence explanation is descriptive and does not advance theoretical understanding beyond what is expected from contrastive loss convergence properties. The 4-reference bibliography is a serious gap for any venue; for a paper whose contribution is positioning relative to prior work, it is disqualifying. The CoCoHaNeRe framing, which carries much of the narrative, rests on an uncited work and is ultimately inconclusive by the paper's own admission. The paper could be strengthened substantially by (a) expanding related work to properly contextualize the finding, (b) testing at genuinely large scale (50K+) with more negatives per query, and (c) providing a predictive theory (not just descriptive documentation) of when geometry convergence occurs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbfba2a1-631b-46f8-8f85-da30b50e9b98",
  "isSidechain": true,
  "agentId": "a27710763487a3e39",
  "requestId": "req_011Cb2qgiyHcLsYp83KYTRyZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db3af405-1b7f-4589-b794-616e47c2d997",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015rbaVVVr2QFa25NQHnNtjW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 302,
      "cache_read_input_tokens": 70285,
      "output_tokens": 2004,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 302
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2004,
          "cache_read_input_tokens": 70285,
          "cache_creation_input_tokens": 302,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 302,
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
