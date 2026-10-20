# Research conversation: You are Reviewer R1 for a top ML venue review. Your focus area is **Methods and Experiments**. Review the paper below us

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a13c7d9057b132256.jsonl`
- **Structured JSON:** [`f344950ea7fc19c3ce73.json`](../../sessions/f3/f344950ea7fc19c3ce73.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-14T17:15:30.707Z_

You are Reviewer R1 for a top ML venue review. Your focus area is **Methods and Experiments**. Review the paper below using a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Acceptance rate ~25%.

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
- SWE-bench Lite (300 instances): no downstream signal
- RepoBench-R: confirms no strategy differentiation
- Appendix ablations: temperature, dynamic mining, hop count, fusion head, distance weighting

## Key Tables (from the paper)

**Table 1: Full-scale R@1 (9 seeds, pool=50)**
- Qwen: Random 0.529, Embedding 0.531 (+0.20pp, p=0.58), Dataflow 0.525 (-0.45pp)
- StarCoder: Random 0.443, Embedding 0.440 (-0.35pp, p=0.47), Dataflow 0.428 (-1.50pp, p=0.015 pre-correction)

**Table 2: 4-strategy including BM25**
- BM25-Emb difference: Qwen -0.35pp (p=0.42), StarCoder -0.25pp (p=0.55)

**Table 3: SWE-bench Lite resolve rates** — all within ±0.67pp, bootstrap CI width ~5pp

**Table 4: RepoBench-R** — all CIs overlap, inconsistent sign across encoders

**Table 5: Stratified analysis** — 10 strata, none significant after Bonferroni (α_adj=0.005)

**Table 6-7: Pool size sensitivity** — Rankings flip 3 times across 4 pool sizes

**Table 8: Scale-dependent effects** (1 seed only) — +1.3pp at 1K → +0.2pp at 5K

**Table 9: Failure analysis** (n=50) — only 10% addressable by structure

**Table 10: Geometry convergence** — margin ratio collapse: Qwen 4.35→1.29, StarCoder 2.90→1.28

**Appendix Tables 11-15**: temperature ablation (null across τ), dynamic mining (+0.05pp at 3.4× cost), hop count (all within noise), fusion head (combined -0.25pp vs embedding-only), distance weighting (+0.10pp vs binary)

## Experiment Design Reference (what a complete study would include)
The complete imagined experiment plan includes all of the above, plus:
- Bootstrap CIs for SWE-bench (mentioned in text but no dedicated table — partially covered)
- 7 qualitative examples showing strategies producing different outcomes (2 structural helps, 3 hurts, 2 no pattern) — briefly mentioned but no detailed table/figure
- Inference-time graph method literature comparison — discussed in §5 but no systematic table

## Your Review Task

Evaluate:
1. **Experimental rigor**: Are the experiments well-controlled? Is the statistical methodology sound (9 seeds, paired-t tests, Bonferroni correction, bootstrap CIs)? Any flaws?
2. **Completeness**: Given the claims, are there missing experiments? Are ablations sufficient?
3. **Method clarity**: Is the experimental setup clearly described and reproducible?
4. **Result interpretation**: Are the null results interpreted correctly? Any over-claiming or under-claiming?
5. **Potential confounds**: Are there threats to validity not addressed?

Produce a structured review with:
- Summary (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted)
- Questions for authors
- Minor issues
- Score and confidence

Be rigorous but fair to negative-result papers. Report in under 800 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a13c7d9057b132256",
  "type": "user",
  "uuid": "5af0efe3-ce70-4bc2-8763-f7078b1712e3",
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

_source line 2 · 2026-05-14T17:15:30.713Z_

```json
{
  "parentUuid": "5af0efe3-ce70-4bc2-8763-f7078b1712e3",
  "isSidechain": true,
  "agentId": "a13c7d9057b132256",
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
  "uuid": "f72ab5b0-092d-4c3f-9b3c-59d3d5abd6b0",
  "timestamp": "2026-05-14T17:15:30.713Z",
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

_source line 3 · 2026-05-14T17:15:33.030Z_



I'll review this paper by first examining the project files to understand the full context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f72ab5b0-092d-4c3f-9b3c-59d3d5abd6b0",
  "isSidechain": true,
  "agentId": "a13c7d9057b132256",
  "requestId": "req_011Cb2qbrutnDknYmLABwEu7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62500721-ee0f-4b2d-a487-fe7d01b1b3c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Gt3MsrjEvXVfBTh7XpZNB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15224,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15224,
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

_source line 4 · 2026-05-14T17:15:33.497Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0172Qfo72MtnwXHb4cyBzTy7`</summary>

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
  "parentUuid": "62500721-ee0f-4b2d-a487-fe7d01b1b3c8",
  "isSidechain": true,
  "agentId": "a13c7d9057b132256",
  "requestId": "req_011Cb2qbrutnDknYmLABwEu7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "293fafb2-c164-4a02-84e3-d1fd0c5a077b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Gt3MsrjEvXVfBTh7XpZNB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15224,
      "cache_read_input_tokens": 0,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15224
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 106,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15224,
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

_source line 5 · 2026-05-14T17:15:33.507Z_

<details><summary>↩ Tool result · `toolu_0172Qfo72MtnwXHb4cyBzTy7`</summary>

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
  "parentUuid": "293fafb2-c164-4a02-84e3-d1fd0c5a077b",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a13c7d9057b132256",
  "type": "user",
  "uuid": "de21e51c-ddb5-4537-a24e-e19e8217320e",
  "sourceToolAssistantUUID": "293fafb2-c164-4a02-84e3-d1fd0c5a077b",
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

_source line 6 · 2026-05-14T17:15:35.690Z_



Let me examine the paper artifacts and report to give a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de21e51c-ddb5-4537-a24e-e19e8217320e",
  "isSidechain": true,
  "agentId": "a13c7d9057b132256",
  "requestId": "req_011Cb2qc596VgWYNcKxuhMVN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f93fb4ed-41c2-4336-bbcb-23b652650439",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qt2rxZDkreyeJjAmPj5bb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 15224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1289,
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

_source line 7 · 2026-05-14T17:15:36.641Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012GdjcXifsgWqJVYV93T1fh`</summary>

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
  "parentUuid": "f93fb4ed-41c2-4336-bbcb-23b652650439",
  "isSidechain": true,
  "agentId": "a13c7d9057b132256",
  "requestId": "req_011Cb2qc596VgWYNcKxuhMVN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5663aab6-4664-4e7c-80bf-11ef007ccfb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qt2rxZDkreyeJjAmPj5bb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 15224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1289,
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

_source line 8 · 2026-05-14T17:15:36.662Z_

<details><summary>↩ Tool result · `toolu_012GdjcXifsgWqJVYV93T1fh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| m2_full_starcoder | Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent). | — | — | — |\\n| m1_reextract_v2 | M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 | — | — | — |\\n| m2_full_qwen | Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018. | — | — | — |\\n\\n## 待处理\\n- plan_015_dynamic（排队等待 GPU）\\n- plan_018_bm25: BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。（排队等待 GPU）\\n\\n## 近期结论\\n- **neg_difficulty_analysis** (success): Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\\n  [neg_difficulty_margin_comparison](/api/workspace-files/projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_margin_comparison_meta.txt)\\n- **m1_reextract** (failed): M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 ← 基于 m1_extraction\\n- **m1_extraction** (success): —\\n\\n## 趋势\\n成功 10 / 负向 2 / 失败 2 / 共 28\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-42106: 无 GPU 信息\\n\\n## 告警\\n- p2b-smoke-test: 已被终止 — unknown\\n- p2b-smoke2: 已被终止 — unknown\\n- p2b-smoke3: 已被终止 — unknown\\n- p2b-smoke4: 已被终止 — unknown\\n- p2b-smoke5: 已被终止 — unknown\\n- p2b-smoke6: 已被终止 — unknown\\n- p2b-smoke7: 已被终止 — unknown\\n- p2b-smoke8: 已被终止 — unknown\\n- p2b-all-9runs: 已被终止 — unknown\\n- mvp_p2b_contrastive_training: 已被终止 — unknown\\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\\n- p2b_eval_all: 已被终止 — unknown\\n- m2_early_pilot: 已被终止 — unknown\\n- m2_early_pilot_v2: 训练失败 — unknown\\n- m2_early_pilot_v3: 已被终止 — unknown\\n- m1_reextract: 训练失败 — unknown\\n\", \"total_chars\": 2314, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5663aab6-4664-4e7c-80bf-11ef007ccfb1",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a13c7d9057b132256",
  "type": "user",
  "uuid": "e38ce87b-b2fe-4e83-aef4-b7da7f3f47b6",
  "sourceToolAssistantUUID": "5663aab6-4664-4e7c-80bf-11ef007ccfb1",
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

_source line 9 · 2026-05-14T17:15:37.645Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RCxRHpnQ7YbviwzFftJwV8`</summary>

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
  "parentUuid": "e38ce87b-b2fe-4e83-aef4-b7da7f3f47b6",
  "isSidechain": true,
  "agentId": "a13c7d9057b132256",
  "requestId": "req_011Cb2qc596VgWYNcKxuhMVN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ec96846-e697-4f29-a749-0e24b79a1077",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qt2rxZDkreyeJjAmPj5bb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 15224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1289,
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

_source line 10 · 2026-05-14T17:15:37.659Z_

<details><summary>↩ Tool result · `toolu_01RCxRHpnQ7YbviwzFftJwV8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/ROADMAP.md\", \"content\": \"# StructFuse — Research Dashboard\\n\\n> 最后更新: 2026-05-14 16:27 UTC | 更新原因: Reviewer WARNING 处理：re-dream gate 标注 + plan_018 contingency + post-M2 时间线明细\\n\\n> 最后更新: 2026-05-14 | 更新原因: Reviewer WARNING 处理：re-dream gate 标注 + plan_018 contingency\\n\\n## 核心方向\\nTrue embedding-distance mining consistently improves contrastive code retrieval (+1.6–2.0pp R@1), correcting prior misconceptions. Structure-grounded (dataflow) negatives provide conditional benefit mediated by encoder representation saturation (observation from n=2 encoders, not validated mechanism). 详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（post-MVP）+ 审稿进行中\\n- **M2 全量训练**: 18 runs 部署完成（Qwen 9 + StarCoder 9），链式自动执行\\n  - Qwen: random_s42 done, random_s43 running (step ~1200/2828), 其余 queued/watcher\\n  - StarCoder: random_s42 running (step ~4000/4242, epoch 3), 其余 queued/watcher\\n  - ETA: Qwen ~May 19, StarCoder ~May 20\\n- **Dream dream_20260514T075732**: Best=4/6(WA), Median=3/6(WR), Worst=3/6(WR)\\n  - 7 项确认行动已持久化（D030），framing + plan 已修改\\n  - **Re-dream dream_20260514T162530 进行中** — 验证修复效果\\n- **plan_015 设计文档**: Worker 完成，待 Agent 汇报\\n- **m1_reextract_v2**: 后台 (~71/82 groups)\\n\\n## 近期任务\\n- [ ] **plan_018 BM25 baseline Phase 1 (CPU)** — 已派 Agent，立即启动\\n- [ ] ⛔ **plan_018 Phase 2 (GPU 训练)** — **需 re-dream 通过后才执行**（D030 gate）\\n- [ ] M2 full 18 runs 完成（~May 19-20）\\n- [ ] 统计检验 — M2 完成后立即执行\\n- [ ] plan_003 SWE-bench Lite eval — M2 best checkpoint ready 后（~20h real on 1 GPU）\\n- [ ] plan_004 RepoBench-R（多 seed + CIs）\\n- [ ] plan_019 Pool size sensitivity — M2 checkpoint ready 后（~2.5h real）\\n- [ ] plan_005 stratified analysis（扩展版）— 0 GPU\\n- [ ] plan_014 temperature ablation — **M2 后单项最大开销 (35h real on 2 GPUs)**，时间紧可推 camera-ready\\n- [ ] plan_015 dynamic mining — 设计完成，待审核\\n- [ ] [Dream 观察] Effect sizes marginal → M2 full 统计后评估\\n- [ ] [Dream 观察] Temperature ablation contradicts story → plan_014 后评估\\n- [ ] Re-dream dream_20260514T162530 结果 → 评估 median 是否 ≥ borderline\\n- [ ] 论文初稿 (~May 24)\\n\\n## Go/No-Go + Re-dream Gate\\n\\n**Claim 1**: 预期 Go。**BM25 contingency**: 若 plan_018 显示 BM25 ≈ random（非 harmful），叙事从 \\\"correcting misconception\\\" 降为 \\\"systematic comparison\\\"。详见 paper_framing.md Contingency 节。\\n**Claim 2**: D028 — 等 M2 统计。\\n**Re-dream gate (D030)**: plan_018 Phase 2 等新 P0 GPU 实验需 re-dream 达标（best ≥ WA, median ≥ borderline）后才批准。Phase 1 (CPU) 不受限。\\n\\n## GPU 预算\\n- **bjb1-42106**: 2× RTX PRO 6000 96GB（专属），满载\\n  - cuda:0: m2_full_qwen（registry ANALYZING 但实际在跑 — 不要重分配）\\n  - cuda:1: m2_full_starcoder (RUNNING)\\n- **Post-M2 需求 (~120h on 2 GPUs = ~60h real = ~2.5 days)**:\\n  - plan_003: 40h (1 GPU, 20h real) — 与 plan_018 Phase 2 并行\\n  - plan_018 Phase 2: 15h (1 GPU, 7.5h real)\\n  - plan_014: 70h (2 GPUs, 35h real) — 时间紧可缩减/推迟\\n  - plan_019: 5h (1 GPU, 2.5h real)\\n- **时间线**: M2 完成(~May 20) → post-M2 实验(~May 22) → 分析+写作(~May 23-24) → ARR May 25\\n\\n## 关键风险\\n1. **ARR May 25**: post-M2 ~60h real + 分析 + 写作 in 5 days。plan_014 (35h) 是瓶颈\\n2. **BM25 narrative risk**: plan_018 结果为 neutral 则需 framing pivot（已备 contingency）\\n3. **Median=WR**: re-dream 进行中，等结果评估改善程度\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D033 | 2026-05-14 | D031 修正：BM25 top-7 overlap 远低于 k=50 的 87%，大 repo 仅 | plan_018 |\\n| D032 | 2026-05-14 | plan_015 缩减为 1 seed × dynamic_ep (~11h)；BM25 overl | plan_015, plan_018 |\\n| D031 | 2026-05-14 | BM25 Phase 1 完成: 87% overlap with embedding_distan | plan_018, plan_015 |\\n| D030 | 2026-05-14 | Dream dream_20260514T075732 分析完成：7 项确认行动 + 5 项观察项  | dream_20260514T075732, plan_018, plan_019 |\\n| D029 | 2026-05-14 | Dream full review 完成：7 条三档一致结构性问题确认，BM25 baseline  | plan_018, plan_019, plan_004, plan_005 |\\n| D028 | 2026-05-14 | Claim 2 降级待定：M2 full 结果决定 \\\"conditional benefit\\\" 是独 | m2_embed_verify, plan_013_starcoder, m2_full_qwen, m2_full_starcoder |\\n| D027 | 2026-05-14 | M2 剩余 runs 加 early stopping (patience=2 evals)，加速关 | m2_full_qwen, m2_full_starcoder |\\n| D026 | 2026-05-14 | Qwen eval@2000 确认过拟合，后续 M2 runs 从 3 epochs 减至 2 ep | m2_full_qwen, m2_full_starcoder |\\n| D025 | 2026-05-14 | Plan_014 temperature ablation 缩减为 2 strategies × 3 | m2_full_qwen, plan_014 |\\n| D024 | 2026-05-14 | Major paper framing rewrite: drop falsified \\\"embed | m2_embed_verify, plan_013_starcoder, neg_difficulty_analysis |\\n\\n\", \"total_chars\": 4166, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ec96846-e697-4f29-a749-0e24b79a1077",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a13c7d9057b132256",
  "type": "user",
  "uuid": "a1252e41-46d3-46b6-8a12-e9be3ffe5d8a",
  "sourceToolAssistantUUID": "7ec96846-e697-4f29-a749-0e24b79a1077",
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

_source line 11 · 2026-05-14T17:15:37.974Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WeABgbgxj8C9iNtqWbVr3a`</summary>

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
  "parentUuid": "a1252e41-46d3-46b6-8a12-e9be3ffe5d8a",
  "isSidechain": true,
  "agentId": "a13c7d9057b132256",
  "requestId": "req_011Cb2qc596VgWYNcKxuhMVN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad3e5e06-7dd5-4a5f-b583-2ecb51c7402c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qt2rxZDkreyeJjAmPj5bb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 15224,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1289
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 303,
          "cache_read_input_tokens": 15224,
          "cache_creation_input_tokens": 1289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1289,
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

_source line 12 · 2026-05-14T17:15:37.986Z_

<details><summary>↩ Tool result · `toolu_01WeABgbgxj8C9iNtqWbVr3a`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献（全部已验证 2026-05-14）\\n\\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\")\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\\n---\\n\\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\\n\\n**两层重叠率数据（注意区分）**：\\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\\n\\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\\n|------|-------------------|----------------|------------------|\\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\\n\\n**核心修正**：之前基于 87% 预测\\\"Phase 2 中 BM25 R@1 很可能接近 embedding\\\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\\n\\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\", \"total_chars\": 9315, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad3e5e06-7dd5-4a5f-b583-2ecb51c7402c",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a13c7d9057b132256",
  "type": "user",
  "uuid": "66b6872e-1f30-4e87-8b43-1b16e5a66fc6",
  "sourceToolAssistantUUID": "ad3e5e06-7dd5-4a5f-b583-2ecb51c7402c",
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

_source line 13 · 2026-05-14T17:15:41.620Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014FP2ZDtpPqv6iNHUWmRi23`</summary>

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
  "parentUuid": "66b6872e-1f30-4e87-8b43-1b16e5a66fc6",
  "isSidechain": true,
  "agentId": "a13c7d9057b132256",
  "requestId": "req_011Cb2qcQAav75fDyiBL6HsY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc9fb833-7a5d-44b9-8e2a-96fb04fb8d60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTUoDegq3SZddePuHjfQyx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7122,
      "cache_read_input_tokens": 16513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7122,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
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

_source line 14 · 2026-05-14T17:15:41.634Z_

<details><summary>↩ Tool result · `toolu_014FP2ZDtpPqv6iNHUWmRi23`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \\\"harm\\\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B).\\n\\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\\n\\n- **Headline result template**: \\\"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\\\"\\n\\n## Core Insight\\n\\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, similarity function s, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\\\"\\n- Backup: \\\"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically verify CoCoHaNeRe used BM25-proxy, closing the correction argument | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### In progress:\\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\\n- m1_reextract_v2: expanded extraction for higher coverage\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — closes CoCoHaNeRe correction argument)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\\\"\\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\\n\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the \\\"correcting misconception\\\" narrative loses empirical anchor\\n- Pivot: from \\\"CoCoHaNeRe was wrong because BM25 proxy\\\" → \\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; prior work's negative finding was likely due to uncontrolled variables (data, training protocol), not BM25 specifically\\\"\\n- Paper becomes less dramatic (\\\"correcting\\\" → \\\"clarifying\\\") but still valid as systematic analysis\\n- Claim 1 reworded: \\\"True embedding-distance mining consistently improves code retrieval\\\" (drop the \\\"correcting misconception\\\" framing, keep the empirical finding)\\n- Impact: weaker narrative hook but core experimental contribution survives\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\", \"total_chars\": 11181, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc9fb833-7a5d-44b9-8e2a-96fb04fb8d60",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a13c7d9057b132256",
  "type": "user",
  "uuid": "318ff712-a38a-446c-b399-05658366cbcd",
  "sourceToolAssistantUUID": "bc9fb833-7a5d-44b9-8e2a-96fb04fb8d60",
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

_source line 15 · 2026-05-14T17:15:42.107Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XjsPu6EpbYieez6VXD8PcY`</summary>

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
  "parentUuid": "318ff712-a38a-446c-b399-05658366cbcd",
  "isSidechain": true,
  "agentId": "a13c7d9057b132256",
  "requestId": "req_011Cb2qcQAav75fDyiBL6HsY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a75b6468-1b4f-4a54-9982-51d661d90794",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTUoDegq3SZddePuHjfQyx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7122,
      "cache_read_input_tokens": 16513,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7122
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 16513,
          "cache_creation_input_tokens": 7122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7122,
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

_source line 16 · 2026-05-14T17:15:42.123Z_

<details><summary>↩ Tool result · `toolu_01XjsPu6EpbYieez6VXD8PcY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/decisions.yaml\", \"content\": \"_next_id: 34\\ndecisions:\\n- id: D001\\n  date: 2026-05-12 09:57 UTC\\n  summary: 'MVP 设计: CodeQL 试点(10 repos) + 迷你对比训练(500 instances) 验证核心假设'\\n  rationale: 13 天 DDL，需要最快速验证核心假设链：(1) CodeQL inter-procedural data-flow 在 Python\\n    repos 上可行（timeout < 30%），(2) data-flow hard negatives 比 random negatives 提升检索\\n    recall。两个 phase 串行，总计约 1 天。通过后立即进入全量数据提取和训练。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-12 10:01 UTC\\n  summary: '采纳 Reviewer 反馈: MVP Phase 2 增加线性分类器 proxy 验证 + 3-seed 训练 + 显式 kill criteria'\\n  rationale: 'Reviewer 指出 Phase 2 原方案（500 instances, ~100 held-out, 2pp gate）统计效力不足，2pp\\n    差异在随机噪声范围内。增加: (1) Phase 2a 线性分类器 proxy 验证解耦特征质量与训练策略；(2) 3-seed 训练要求 ≥2/3 seed\\n    提升；(3) 每个 phase 的 fail→kill/fallback 路径。防止 13 天 DDL 下的沉没成本陷阱。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-12 10:02 UTC\\n  summary: 'H2 验证并入 Phase 1: 提取后立即统计 data-flow 连通文件 vs 不连通文件的 gold patch 覆盖率差异'\\n  rationale: Reviewer 指出 H2（特征区分度）在原 MVP 中无独立验证，Phase 2 失败时无法区分是 H2 还是 H3 问题。零成本 sanity\\n    check（统计连通/不连通文件的 gold patch 覆盖率）可在 Phase 1 提取完后立即执行，不需要训练。这比 Phase 2a 的线性分类器更早给出诊断信号。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-12 11:21 UTC\\n  summary: 'Phase 1 gate PASS: timeout 0%, H2 Fisher p=1.54e-7, 75% instance recall.\\n    进入 Phase 2。'\\n  rationale: 10 repos 中 8 个成功提取（2 个 skip 因 buggy file 路径不存在，非 CodeQL 限制）。timeout rate\\n    0% 远低于 30% 阈值。H2 sanity check：连通文件 gold 覆盖 1.44% vs 不连通 0.00%，Fisher p=1.54e-7。75%\\n    instance recall（6/8 gold file 在连通集）。数据质量问题（路径匹配、skip rate、registry 注册）并行修复，不阻塞\\n    Phase 2。\\n  related_experiments: []\\n  depends_on: []\\n- id: D005\\n  date: 2026-05-12 11:35 UTC\\n  summary: 'CRITICAL: GPU 越界 PID 59170 跑在 GPU 5 而非分配的 cuda:4，立即 kill + 全脚本修复 CUDA_VISIBLE_DEVICES'\\n  rationale: Reviewer 核实 nvidia-smi 发现 run_mvp.py 在 GPU 5 上运行 9.3GB，而项目分配的 cuda:4\\n    完全空闲。违反 L1 红线（GPU 资源边界）。要求 Agent 立即 kill 进程、修复所有脚本强制 CUDA_VISIBLE_DEVICES=4、排查\\n    dry-run 是否也越界。\\n  related_experiments: []\\n  depends_on: []\\n- id: D006\\n  date: 2026-05-12 17:24 UTC\\n  summary: P2b pass criteria 调整：recall@5→recall@1，pool_size 26→50+，阈值 ≥2pp 不变\\n  rationale: Eval v2 (pool_size=26) 显示 random recall@5 已达 98.4-99.2%，原标准\\\"dataflow\\n    recall@5 > random ≥2pp\\\"数学上几乎不可能达标（天花板仅 0.8-1.6pp 空间）。recall@1 有更大区分度（random mean\\n    93.97%），且是更严格的排序指标。同时扩大 pool_size 至 50+ 使 recall@5/10 也获得有效梯度。新标准：dataflow_aware\\n    recall@1 > random recall@1 ≥2pp in ≥2/3 seeds，pool_size=50。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: random recall@1 mean=0.940, emb_dist recall@1=0.669 at pool=26; recall@5\\n      ceiling\\n  depends_on:\\n  - D002\\n- id: D007\\n  date: 2026-05-12 19:52 UTC\\n  summary: MVP P2b dataflow 策略不可验证：connected⊆gold 导致数据相同。决定：50-repo 规模验证 + Scheme\\n    B 备份\\n  rationale: 修复 build_p2b_data.py 后重新生成数据，train_dataflow.jsonl 仍与 train_embedding.jsonl\\n    完全相同。根因：8 个 MVP repos 中 dataflow 连接文件全部是 gold 文件的子集（connected-but-not-gold = 0），non_pos\\n    过滤无差异。这不是方法缺陷而是规模问题——小 repo 紧耦合，2-hop 连接集≈gold 集。P1（Fisher p=1.54e-7）和 P2a（AUC=0.78）仍有效，说明\\n    dataflow connectivity 有信号，只是 MVP 规模不足以分离 connected-but-not-gold 子集。决策：(1) 立即跑\\n    50-repo 样本的 overlap 统计（CPU, ~2-4h），确认大规模下 connected⊃gold；(2) 并行准备 Scheme B（distance-weighted\\n    negatives）作为 pivot 备选；(3) overlap>20% 实例有 connected≠gold → 进入全量 M1 提取；overlap≈100%\\n    → pivot to Scheme B。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: dataflow≡embedding 因 connected⊆gold\\n  depends_on:\\n  - D006\\n  - D004\\n- id: D008\\n  date: 2026-05-12 20:38 UTC\\n  summary: MVP 条件性通过：P1+P2a PASS，P2b dataflow 在 MVP 规模不可测但 50-repo 规模验证确认方法可行（Z=40.8%）。进入\\n    research 阶段。\\n  rationale: MVP 三阶段结果：P1 PASS（timeout 0%, Fisher p=1.54e-7, 75% instance recall）；P2a\\n    PASS（AUC 0.78, BM25 系数为负）；P2b 部分有效——random>>embedding（-27pp recall@1 at pool=26,\\n    -3.7pp at pool=50）确认 naive hard negatives 有害，但 dataflow vs random 因 connected⊆gold\\n    无法在 8 repos 上区分。50-repo 规模验证 Z=40.8%（中型 repo 55.7%），timeout 4%，确认方法在全量数据上可行。Kill\\n    criteria 均未触发。P2b dataflow 对比将在 M2 全量训练中完成。\\n  related_experiments:\\n  - exp_id: mvp_p1_codeql_feasibility\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2a_linear_proxy\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: evidence\\n    result: partial - random>>emb confirmed, dataflow untestable at MVP scale\\n  depends_on:\\n  - D007\\n  - D006\\n  - D004\\n- id: D009\\n  date: 2026-05-12 22:04 UTC\\n  summary: Dream 审稿完成：best=Weak Accept, median=Weak Reject, worst=Reject。批准 P0 启动，但\\n    plan 需增补 5 个 dream-derived 实验\\n  rationale: 三档共识问题：(1) 单编码器无法支撑 generality claim，需加 StarCoder/CodeBERT；(2) static\\n    vs dynamic embedding mining 是潜在 confound；(3) τ=0.05 可能 regime-specific；(4) SWE-bench\\n    +2pp 需 bootstrap CI；(5) abstract \\\"complementary\\\" 需降调。关键风险变量是 M1 的 Z%：≥35% best\\n    framing 成立，20-35% pivot 到 Claim 2 headline，<20% 需重大调整。已在 experiment_plan.yaml\\n    增加 plan_013-017（+35h GPU），paper_framing.md 增加 contingency framing。P0 实验（M1 已在跑）可继续，不需\\n    re-dream。\\n  related_experiments:\\n  - exp_id: dream_20260512T204322\\n    role: dream_simulate\\n    result: best=WA, median=WR, worst=R\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-12 22:09 UTC\\n  summary: plan_013 (second encoder) 从 P1 升级至 P0，headline template 降调修复\\n  rationale: Reviewer 指出 single encoder 是 best→accept 的关键区分因素，在 best-R1-W1 和 median-R2-W5\\n    两档都出现。P1 排期可能导致论文缺少 generality 证据而被 WR。升级后 M2 完成即可并行启动 plan_013。同时修复 headline\\n    template \\\"cannot recover\\\" → \\\"complementary signal not captured by\\\"。\\n  related_experiments:\\n  - exp_id: plan_013\\n    role: priority_upgrade\\n    result: P1→P0\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-13 01:38 UTC\\n  summary: Z%=74.0% 确认 Best Framing — Claim 1 为 headline，批准 M2 早期训练\\n  rationale: M1 部分数据（24/222 repos, 5128 instances）Z%=74.0%，远超 ≥35% 阈值。对比 D007 的 40.8%（50\\n    SWE-bench repos），SWE-Smith 数据集跨文件依赖密度更高。Best framing 成立：Claim 1 (\\\"structure-grounded\\n    negatives outperform\\\") 为 headline。批准在当前 5K instances 上做 M2 早期训练 pilot（3 strategies\\n    × 1 seed），利用 cuda:4 空闲期获取早期信号，不等全量 M1（还需 ~46h）。磁盘已清理至 61GB free (64%)，足够训练。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: Z%=74.0% at 24/222 repos\\n  - exp_id: d007_50repo_overlap\\n    role: baseline\\n    result: Z%=40.8% on SWE-bench 50 repos\\n  depends_on:\\n  - D009\\n  - D010\\n- id: D012\\n  date: 2026-05-13 02:11 UTC\\n  summary: Kill m2_early_pilot_v3 (PID 897752) — 第二次 GPU 越界 (cuda:0)\\n  rationale: Reviewer 发现 m2_early_pilot_v3 在 cuda:0 运行（PID 897752, 17100 MiB），项目仅分配\\n    cuda:4。这是第二次 GPU 越界（第一次 D005 在 GPU 5）。立即 kill 并标记 killed。同时 m2_early_pilot_v2\\n    因 wandb API key error 已崩溃标记 FAILED。当前唯一合法训练为 PID 795791 (m2_early_pilot, cuda:4)。要求\\n    Agent 排查越界原因并确保后续脚本强制 CUDA_VISIBLE_DEVICES=4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot_v3\\n    role: violated\\n    result: killed - GPU 越界 cuda:0\\n  - exp_id: m2_early_pilot_v2\\n    role: failed\\n    result: wandb API key error\\n  - exp_id: m2_early_pilot\\n    role: active\\n    result: PID 795791 on cuda:4, running\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-13 02:50 UTC\\n  summary: 服务器迁移：cqa1-21977 cuda:4 → bjb1-42106 cuda:0/1 (RTX PRO 6000 96GB×2)\\n  rationale: Manager 分配独立服务器 bjb1-42106（2x RTX PRO 6000 96GB）。迁移策略：(1) M1 提取继续在 cqa1-21977\\n    CPU 上完成（不中断），(2) 新服务器立即搭建环境+同步代码+下载模型，(3) M2 early pilot 在 cqa1-21977 cuda:4 跑完后所有\\n    GPU 工作转到新服务器，(4) 通知 Manager 释放 cuda:4。RTX PRO 6000 96GB 彻底解决 M3a VRAM 问题（Qwen3.6-27B\\n    不再需要 fallback），2 卡可并行 M2 全量 + plan_013。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: in_progress\\n    result: finishing on cqa1-21977 cuda:4\\n  - exp_id: m1_extraction\\n    role: in_progress\\n    result: CPU only, stays on cqa1-21977\\n  depends_on:\\n  - D011\\n- id: D014\\n  date: 2026-05-13 04:44 UTC\\n  summary: Kill m2_early_pilot (PID 795791) — 过拟合+卡死，bjb1 m2_embed_verify 取代\\n  rationale: m2_early_pilot 在 cqa1 cuda:4 上仅完成 random 策略（best val_loss=0.5879 at step\\n    1500，之后持续过拟合到 0.728）。进程在 step 4000 卡死 45+ min。OOM 干扰（另一进程在同 GPU 启动）。embedding_distance\\n    和 dataflow_aware 策略未启动。bjb1 上的 m2_embed_verify 使用 true embedding mining + 更大参数（negatives=7,\\n    seq_len=2048, batch=8）+ eval bug fix，将完全取代此 pilot。通知 Manager 释放 cqa1 cuda:4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: killed\\n    result: random best val_loss=0.5879, overfitting after step 1500\\n  - exp_id: m2_embed_verify\\n    role: replacement\\n    result: preparing on bjb1 cuda:1\\n  depends_on:\\n  - D011\\n  - D013\\n- id: D015\\n  date: 2026-05-13 11:43 UTC\\n  summary: 全量 Z%=78.0%（条件）确认 Best Framing；Coverage 34.3% 需论文讨论\\n  rationale: 全量 M1（123/131 repos, 44,173 instances）统计：15,153 instances 有结构数据（34.3%），其中\\n    11,825 有 connected-but-not-gold 文件（条件 Z%=78.0%，高于 pilot 72.5%）。条件 Z% 远超 35% 阈值，Best\\n    Framing（Claim 1 as headline）完全成立。但 Coverage 仅 34.3%——65.7% instances CodeQL/Beniget\\n    未产出结构连接，论文需讨论此局限性并限定 claim 范围为\\\"有结构数据的 instances\\\"。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: 123/131 repos, 44173 instances, 15897 structural\\n  - exp_id: plan_006_scalability\\n    role: prior_pilot\\n    result: pilot Z%=72.5% on 29 repos\\n  depends_on:\\n  - D011\\n- id: D016\\n  date: 2026-05-13 15:24 UTC\\n  summary: 'Reviewer Critical: m2_embed_verify 和 plan_013_starcoder 实际已完成全部 3 策略，registry\\n    错误标记为 failed'\\n  rationale: Reviewer 直接从服务器日志验证：两个实验的 dataflow 策略均已完成（\\\"All 3 strategies completed\\\"），EXIT_CODE\\n    异常发生在训练完成之后（wrapper 脚本问题）。关键数据：(1) Qwen dataflow peak R@1=0.5584 (+2.27pp vs random)，支撑\\n    Claim 1；(2) StarCoder dataflow R@1=0.4869 < random 0.4922，encoder-agnostic claim\\n    受挑战；(3) 两个编码器的 dataflow 策略均严重过拟合（train loss→0）。已派 Agent 紧急修正 registry + 收集完整 metrics\\n    + 验证 StarCoder random 数据来源。方向决策待 Agent 汇报验证数据后确定。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 实际完成（3 strategies all done），Qwen dataflow peak R@1=0.5584\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 实际完成（3 strategies all done），StarCoder dataflow R@1=0.4869 < random 0.4922\\n  depends_on: []\\n- id: D017\\n  date: 2026-05-13 16:03 UTC\\n  summary: Pilot 结果验证完成：embedding > random 跨编码器一致；dataflow 需按两种 checkpoint 标准报告；Claim\\n    2 需修订\\n  rationale: 'Reviewer 验证 18 个指标全部精确匹配。核心发现：(1) embedding > random 在 Qwen (+2.0pp)\\n    和 StarCoder (+1.6pp) 上一致，是最稳健结论；(2) dataflow 排名取决于 checkpoint 选择——按 val_loss:\\n    embedding > dataflow > random (Qwen)，按 peak R@1: dataflow > embedding > random\\n    (Qwen)；(3) StarCoder dataflow final eval 追平 embedding (0.5078=0.5078)，\\\"embedding\\n    consistently beats dataflow\\\" 不成立；(4) Claim 2 (\\\"embedding harms\\\") 在 true embedding\\n    mining 下不复现，仅在 MVP BM25 proxy 下成立。全量 M2 训练需报告两种 checkpoint 标准下的结果，避免 cherry-picking\\n    质疑。Paper framing 修订延后至全量 M2 结果出来后。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 'Qwen: embedding(0.5557) > dataflow(0.5436) > random(0.5357) by val_loss;\\n      dataflow peak(0.5584) > embedding(0.5557) by R@1'\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 'StarCoder: embedding(0.5078) > random(0.4922) > dataflow(0.4869) by val_loss;\\n      dataflow final(0.5078) = embedding'\\n  depends_on:\\n  - D016\\n- id: D018\\n  date: 2026-05-13 16:04 UTC\\n  summary: 不做预判性 framing pivot，full M2 (18 runs) 是 go/no-go 唯一判据；双 checkpoint 标准；准备\\n    B/C 两条后备路线\\n  rationale: Pilot 仅 24 repos / 1 seed，<2pp delta 统计功效不足以支持强 claim 或否决原假设。Full M2\\n    (131 repos × 3 strategies × 3 seeds × 2 encoders = 18 runs) 提供 3-seed 统计功效，是唯一可信判据。不选\\n    Agent 提议的 A/B/C 任何一个——过早锁定叙事会限制后续解读空间。数据构建已在进行，不浪费时间在 framing 讨论上。Full M2 结果出来后根据实际数据\\n    pattern 决定：(a) dataflow 跨编码器一致 > random → 原 framing 修正后可用；(b) dataflow 不一致但 embedding\\n    一致 → 方案 B 或 C；(c) 所有差异不显著 → 需要更大规模实验或 pivot。同时要求 dual checkpoint (best-val-loss\\n    + best-R@1) 和 3-seed CI 确保结果可信。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-13 18:08 UTC\\n  summary: D018 补充：Full M2 go/no-go 量化阈值 + 统计检验方案\\n  rationale: 'Reviewer 指出 D018 缺量化阈值，go/no-go 判据需在结果出来前明确，避免事后 rationalization。\\n\\n\\n    **统计方法**：每个 encoder 3 seeds 的 R@1 (best-by-val-loss checkpoint) 做 paired difference，bootstrap\\n    95% CI + paired t-test (p<0.05)。同时报告 best-by-R@1 checkpoint 结果作为透明度补充。\\n\\n\\n    **Go/No-Go 阈值**：\\n\\n    (A) Go — 原 framing 可用：dataflow > random 的 95% CI 在两个 encoder 上均 > 0\\n\\n    (B) Conditional Go — 修正 framing：dataflow > random 在至少一个 encoder 上 CI > 0，另一个 CI\\n    含 0（差异不显著）\\n\\n    (C) No-Go for Claim 1：dataflow ≤ random 在两个 encoder 上 CI 均含 0 或为负 → Claim 1 失效，pivot\\n    到 \\\"mining strategy × architecture\\\" 分析论文\\n\\n\\n    **Claim 2 判据**：若 full M2 显示 embedding > random 且 CI > 0 → 原 Claim 2 (\\\"embedding\\n    harms\\\") 被否定。新 Claim 2 候选：\\\"true embedding mining helps, but BM25 proxy harms\\\" 或\\n    \\\"hard negative mining method matters more than hard negative source\\\"\\n\\n\\n    **跨 encoder 一致性规则**：\\n\\n    - 同方向同显著 → 强泛化 claim\\n\\n    - 同方向不同显著 → 条件 claim + architecture discussion\\n\\n    - 反方向 → Claim 1 原形式被拒，需 conditional reframe\\n\\n\\n    阈值在 full M2 结果出来前锁定，不允许事后修改。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING - random_s42 in progress\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING - data build phase\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-13 18:10 UTC\\n  summary: D019 补充：Claim 2 完整判定矩阵 + n=3 功效限制声明\\n  rationale: 'Reviewer 指出 D019 的 Claim 2 阈值不完整 + n=3 统计功效天然受限。补充如下：\\n\\n\\n    **Claim 2 完整判定矩阵**（3 seeds, paired bootstrap 95% CI）：\\n\\n    (i) random > embedding CI>0 → Claim 2 confirmed（embedding harms，与 MVP 一致）\\n\\n    (ii) embedding > random CI>0 → Claim 2 falsified（true embedding mining helps，需\\n    reframe）\\n\\n    (iii) CI 含 0 → inconclusive（效应存在但检测不到或确实无差异，论文报告为 \\\"no significant difference\\\"\\n    + 报告 effect size）\\n\\n\\n    **n=3 功效限制**（显式承认，不修改阈值）：\\n\\n    - df=2 时 t 临界值 4.303，pilot 级别差异（<2pp）极难达到 p<0.05\\n\\n    - Bootstrap n=3 仅 27 种重采样，CI 估计粗糙\\n\\n    - 阈值框架偏向 No-Go（Type II error 高）\\n\\n    - 若结果落入 (C) No-Go，论文 Discussion 必须讨论功效限制，不能简单声明 \\\"dataflow 无效\\\"\\n\\n    - 这是算力约束下的合理选择，不改阈值，但明确风险\\n\\n\\n    **plan_014 排期**：Full M2 完成后优先启动 plan_014（temperature ablation, ~10h）——无论 Claim\\n    2 reframe 成哪个方向，temperature regime-specificity 都需要回答。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING\\n  depends_on:\\n  - D019\\n- id: D021\\n  date: 2026-05-13 19:10 UTC\\n  summary: Negative difficulty 分析揭示 encoder capacity 差异是 dataflow 效果不一致的根因\\n  rationale: '预训练模型 cosine similarity 分析显示：Qwen pretrained embeddings 分辨力弱（random\\n    cosine sim 0.899），StarCoder 分辨力强（random cosine sim 0.553）。Dataflow negatives 在两个模型上都比\\n    random 更难（higher sim），说明方法设计正确。但 StarCoder 已经\\\"懂\\\"结构差异（所有策略 sim 都低），额外训练信号边际收益小。这解释了\\n    pilot 中 StarCoder dataflow < random 的现象：不是方法问题，是 encoder 已有足够 capacity。\\n\\n\\n    论文价值：(1) 从 negative result 中提取 mechanistic explanation；(2) 定义 method applicability\\n    condition：\\\"structure-grounded negatives benefit most when pretrained encoder has\\n    limited structural separability\\\"；(3) 产出论文级图表（Figure: Negative Difficulty Distributions）；(4)\\n    无论 full M2 落入 A/B/C，这个分析都增加论文深度。不修改 go/no-go 阈值，但丰富解读框架。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: context\\n    result: 'Qwen: dataflow > random (+0.8~2.3pp)'\\n  - exp_id: plan_013_starcoder\\n    role: context\\n    result: 'StarCoder: dataflow < random (-0.5pp), explained by high pretrained separability'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D022\\n  date: 2026-05-13 19:25 UTC\\n  summary: M1 28K instances 可恢复（运行时故障非数据问题）；当前 M2 继续，并行后台重跑 M1 提取\\n  rationale: 'Fuzzy match 抽查 10/10 发现 buggy_file 全部存在——28,276 个 \\\"error\\\" 是 CodeQL 并行提取时的运行时故障（磁盘/存储瞬态），不是\\n    SWE-smith 数据质量问题。训练数据潜在从 15,897 → ~44,173（2.8x）。\\n\\n\\n    决策：不中断当前 M2 训练 + 并行后台重跑 M1 提取。理由：\\n\\n    (1) 当前 M2 已在双卡运行，中断重来延期 3-7 天超出 DDL\\n\\n    (2) M1 重提取是 CPU 工作，可在 bjb1-42106 后台运行不影响 GPU 训练\\n\\n    (3) 如果当前 M2 结果落入 (C) No-Go 或 effect size 太小，扩展数据集是 natural next step\\n\\n    (4) 2.8x 数据量可能显著缓解 dataflow 过拟合问题（D021 中的核心风险）\\n\\n\\n    Claim 3 叙事需修正：\\\"64% failure 是上游数据问题\\\" → \\\"64% 是运行时提取故障，CodeQL 本身在有效输入上 100% 成功，可通过重跑恢复\\\"。这是\\n    engineering limitation with clear fix，不是方法局限。'\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: primary\\n    result: 28,276 instances recoverable - runtime failure, not data quality\\n  - exp_id: plan_006_scalability\\n    role: affected\\n    result: 'error classification needs correction: buggy_file_not_found was misattributed'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D023\\n  date: 2026-05-13 19:43 UTC\\n  summary: Kill M1 重提取：bjb1 CodeQL 查询 100% 失败，D022 前提不成立需诊断后重新评估\\n  rationale: Reviewer CRITICAL 发现 bjb1-42106 上 CodeQL call_graph.ql 查询全部 exit status\\n    2，317/325 行失败，零有效结构数据产出。原 M1 在 cqa1-21977 成功，迁移后 CodeQL 版本/QL pack 可能不兼容。立即 kill\\n    进程释放 CPU/RAM，诊断 CodeQL 配置后决定修复或换服务器。\\n  related_experiments:\\n  - exp_id: m1_reextract\\n    role: subject\\n    result: killed - CodeQL incompatible on bjb1\\n  depends_on:\\n  - D022\\n- id: D024\\n  date: 2026-05-14 00:49 UTC\\n  summary: 'Major paper framing rewrite: drop falsified \\\"embedding harms\\\" claim, pivot\\n    to \\\"systematic analysis + mechanistic insight\\\" narrative'\\n  rationale: 'Reviewer deep assessment confirmed Claim 2 (\\\"embedding actively harms\\\",\\n    -27pp) was built on BM25-proxy mislabeled as embedding-distance in MVP. D017 proved\\n    true embedding mining helps (+1.6-2.0pp). New framing: (1) embedding universally\\n    helps (corrects misconception), (2) dataflow conditionally helps (mediated by\\n    representation saturation), (3) CodeQL scalable. This is a stronger, more honest\\n    paper type for EMNLP — empirical analysis with mechanistic depth rather than false\\n    \\\"our method beats all\\\" claim.'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: embedding > random confirmed for both encoders\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: dataflow helps Qwen only, not StarCoder — conditional benefit\\n  - exp_id: neg_difficulty_analysis\\n    role: evidence\\n    result: pos_sim saturation explains strategy-encoder interaction\\n  depends_on: []\\n- id: D025\\n  date: 2026-05-14 01:01 UTC\\n  summary: Plan_014 temperature ablation 缩减为 2 strategies × 3τ × 2 epochs = 6 runs\\n    (~70h)，deadline 可达\\n  rationale: 原方案 9 runs × 3 epochs = 157h GPU，超出 May 25 ARR 截稿。缩减理由：(1) 回答 Dream reviewer\\n    的 regime-specificity concern 只需证明 embedding vs random 的相对优势跨 τ 一致，不需要 3 策略全跑；(2)\\n    M2 和 pilot 均显示 epoch 3 过拟合无收益，2 epochs 足够；(3) τ=0.07 已由 M2 覆盖，只需 {0.05, 0.1, 0.2}。6\\n    runs × ~11.7h = ~70h → 双卡并行 35h wall time，M2 完成后 ~1.5 天可跑完。Dataflow strategy 的\\n    τ ablation 降为 P2，时间充裕再补。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: step 1000 best, epoch 3 overfitting → 2 epochs sufficient\\n  - exp_id: plan_014\\n    role: target\\n    result: budget revised from 10h to 70h, scope from 9 to 6 runs\\n  depends_on:\\n  - D024\\n- id: D026\\n  date: 2026-05-14 02:56 UTC\\n  summary: Qwen eval@2000 确认过拟合，后续 M2 runs 从 3 epochs 减至 2 epochs\\n  rationale: 'eval@2000: val_loss=0.5162, R@1=0.5228（与 @1500 持平，未恢复）。Best 锁定 step\\n    1000 (epoch 1 中段)。train_loss=0.04 vs val_loss=0.52，gap 持续扩大。模式与 pilot 一致（best\\n    at ~25% training）。当前 s42 保留 3 epochs 完整跑完（提供 full overfitting curve 数据），后续 8 runs/encoder\\n    设 max_epochs=2。节省 ~48h/GPU，M2 完成时间从 ~May 20-21 提前到 ~May 18-19。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: eval@2000 R@1=0.5228 flat, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: pending\\n    result: eval@1000 still improving, apply 2-epoch precaution for subsequent seeds\\n  depends_on:\\n  - D025\\n- id: D027\\n  date: 2026-05-14 08:13 UTC\\n  summary: M2 剩余 runs 加 early stopping (patience=2 evals)，加速关键路径\\n  rationale: Reviewer 计算 M2 全 18 runs 需 ~5.5 天（StarCoder 瓶颈 ~133h）。两个编码器 best checkpoint\\n    均在 step 1000，之后 val_loss 持续上升。加 early stopping（patience=2，即连续 2 次 eval@500 无改善即停）预计在\\n    step 2000 左右停止（vs 2828 full 2-epoch），节省 ~30% 时间（~1.5 天），M2 从 May 19.5 提前到 ~May\\n    18。关键路径 May 25 ARR 余量从 5 天增至 7 天。风险低：仅影响未启动的 runs，不改已跑数据。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  depends_on:\\n  - D026\\n- id: D028\\n  date: 2026-05-14 11:09 UTC\\n  summary: Claim 2 降级待定：M2 full 结果决定 \\\"conditional benefit\\\" 是独立 claim 还是降为 observation\\n  rationale: Reviewer 覆盖率审查指出 Claim 2 最薄弱：n=2 encoders 交互效应无统计功效，neg_difficulty 是描述性非实验性证据。建议降为\\n    \\\"observation + mechanistic hypothesis\\\"。决策延迟到 M2 full 18 runs 完成后：若 Qwen dataflow>random\\n    p<0.05 则保持 conditional claim；否则降级为 observation。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: Qwen pilot positive\\n    result: dataflow > random +0.8pp val_loss\\n  - exp_id: plan_013_starcoder\\n    role: StarCoder pilot negative\\n    result: dataflow < random -0.5pp\\n  - exp_id: m2_full_qwen\\n    role: go/no-go for claim strength\\n    result: RUNNING\\n  - exp_id: m2_full_starcoder\\n    role: encoder generality test\\n    result: RUNNING\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D029\\n  date: 2026-05-14 16:23 UTC\\n  summary: Dream full review 完成：7 条三档一致结构性问题确认，BM25 baseline 升为 P0，pool size sensitivity\\n    新增 plan_019\\n  rationale: 'dream_20260514T075732 (full review mode) 三档评分: Best 4/6 WA, Median 3/6\\n    WR, Worst 3/6 WR。跨三档一致的结构性问题 7 条：(1) 缺 BM25 baseline 是 #1 共识——论文核心叙事（纠正 CoCoHaNeRe）无实证支撑，已加\\n    plan_018 P0；(2) N=2 编码器限制——保持 honest framing，无法加更多编码器；(3) StarCoder 误标为 encoder-decoder——已修正为\\n    decoder-only；(4) RepoBench-R 无 CIs——plan_004 已标注多 seed 要求；(5) Pool=50 太小——新增 plan_019\\n    P1；(6) 34% structural coverage 未分层——plan_005 已扩展；(7) Checkpoint selection criterion\\n    未指定——写作时明确。观察项：effect sizes 太小（等 M2 真实数据）、overfitting 分析（提取现有训练 log）。忽略项：broken\\n    bibliography（dream artifact）、0 figures（dream artifact）。评分顺序正常（best≥median=worst）。下一步：派\\n    Agent 准备 BM25 mining（CPU），M2 完成后立即执行 plan_018 training phase。'\\n  related_experiments:\\n  - exp_id: plan_018\\n    role: new P0 experiment added\\n    result: planned\\n  - exp_id: plan_019\\n    role: new P1 experiment added\\n    result: planned\\n  - exp_id: plan_004\\n    role: updated with multi-seed CI requirement\\n    result: planned\\n  - exp_id: plan_005\\n    role: extended with structural coverage stratification\\n    result: planned\\n  depends_on:\\n  - D024\\n  - D028\\n- id: D030\\n  date: 2026-05-14 16:23 UTC\\n  summary: Dream dream_20260514T075732 分析完成：7 项确认行动 + 5 项观察项 + re-dream 后批准新 P0\\n  rationale: 'Dream full review (2 Reviewers roundtable) 三档评分: Best=4/6(WA), Median=3/6(WR),\\n    Worst=3/6(WR)。Median 未达 borderline，需修复结构性问题后 re-dream。\\n\\n\\n    **三档一致的结构性问题（7 项确认行动）：**\\n\\n    1. [EXP] 缺 BM25 negative baseline — 论文核心 narrative (correcting CoCoHaNeRe) 无实证。加\\n    plan_018, P0, Phase1 CPU 立即启动\\n\\n    2. [EXP] RepoBench-R 缺 CIs — plan_004 增加多 seed 评估\\n\\n    3. [EXP] Pool size 50 过小 — 加 plan_019 sensitivity analysis\\n\\n    4. [EXP] 34% structural coverage 未分层 — 扩展 plan_005 加 structural-available vs fallback\\n    stratum + neg_difficulty quartile\\n\\n    5. [FRAMING] N=2 encoders → 降级为 \\\"observation + hypothesis\\\"，非 validated mechanism\\n\\n    6. [FRAMING] StarCoder 架构 → 修正为 \\\"decoder-only\\\"（已改）\\n\\n    7. [FRAMING] Claim 3 (CodeQL pipeline) → 降为 supporting methodology（已改）\\n\\n\\n    **观察项（等真实数据）：**\\n\\n    1. Effect sizes marginal [M][W] — 等 M2 full 统计结果\\n\\n    2. Dataflow claim strength [M][W] — D028 已 plan\\n\\n    3. \\\"Scaling law\\\" [W] → 用 \\\"trend\\\" + CIs\\n\\n    4. Temperature ablation contradiction [W] — plan_014 结果决定\\n\\n    5. Zero method contribution [M][W] — framing 强度决定\\n\\n\\n    **Re-dream 要求：** framing + plan 修改完成后需 re-dream，best ≥ WA 且 median ≥ borderline\\n    后才批准新 P0 实验。已在跑的实验继续。'\\n  related_experiments:\\n  - exp_id: dream_20260514T075732\\n    role: trigger\\n    result: best=4/6 WA, median=3/6 WR, worst=3/6 WR\\n  - exp_id: plan_018\\n    role: new_from_dream\\n    result: planned — BM25 baseline\\n  - exp_id: plan_019\\n    role: new_from_dream\\n    result: planned — pool size sensitivity\\n  depends_on:\\n  - D028\\n  - D024\\n- id: D031\\n  date: 2026-05-14 17:02 UTC\\n  summary: 'BM25 Phase 1 完成: 87% overlap with embedding_distance，预示论文叙事可能从 \\\"纠正误标\\\"\\n    转向 \\\"受控对比证明 hard negatives 普遍有效\\\"'\\n  rationale: 'plan_018 Phase 1 (CPU) 完成。3 seeds BM25 negatives 已生成，与 embedding_distance\\n    negatives 重叠率高达 87.1%。小 repo 候选池 ≤50 导致所有策略完全重合，BM25 differentiation 主要在大 repo\\n    上体现。\\n\\n\\n    Phase 2 训练结果预期 3 种可能：\\n\\n    A) BM25 harm (BM25 << random) → 原叙事成立（\\\"BM25 proxy 导致 CoCoHaNeRe 错误结论\\\"）\\n\\n    B) BM25 ≈ random → contingency per D030（叙事降为 \\\"systematic comparison\\\"）\\n\\n    C) BM25 ≈ embedding_distance (87% overlap 强烈预示) → 叙事升级为\\\"BM25 和 embedding mining\\n    高度重叠，两者在受控环境下都优于 random；CoCoHaNeRe 的负面结论源于实验控制不足而非 BM25-proxy 本身\\\"\\n\\n\\n    Scenario C 实际上比 A 更强——我们提供的不只是标签纠正，而是受控对比 + 叙事升级。\\n\\n\\n    附带决策：plan_015 暂缓至 camera-ready（44h 超预算 + DDL 紧），Limitations 中承认 static vs dynamic\\n    confound。'\\n  related_experiments:\\n  - exp_id: plan_018\\n    role: phase1_complete\\n    result: BM25 data ready, 87% overlap with embedding_distance\\n  - exp_id: plan_015\\n    role: deferred\\n    result: design complete, execution deferred to camera-ready\\n  depends_on:\\n  - D030\\n- id: D032\\n  date: 2026-05-14 17:02 UTC\\n  summary: plan_015 缩减为 1 seed × dynamic_ep (~11h)；BM25 overlap 87% 需分层验证\\n  rationale: 'plan_015 原设计 3 variants × 多 seeds = 44h，DDL May 25 前 GPU 时间不够。缩减为 dynamic_ep\\n    × 1 seed (Qwen s42) ~11h，足以排除 static vs dynamic confound。预期 dynamic ≈ static（<1pp），在\\n    Limitation 段写实验证据。\\n\\n\\n    BM25 Phase 1 完成：BM25 vs embedding overlap 87.1%。但 Agent 指出小 repo (pool ≤50) 导致所有策略\\n    negatives 重合——overlap 被拉高。已派补充分析按 repo 大小分层统计真实差异化程度。Phase 2 训练结果将决定 CoCoHaNeRe\\n    narrative 是否需要 pivot（contingency 已在 paper_framing.md）。'\\n  related_experiments:\\n  - exp_id: plan_015\\n    role: scope_reduction\\n    result: 44h→11h, 1 seed × dynamic_ep only\\n  - exp_id: plan_018\\n    role: phase1_complete\\n    result: BM25 vs embedding overlap 87.1%, 3 seeds done\\n  depends_on:\\n  - D030\\n- id: D033\\n  date: 2026-05-14 17:10 UTC\\n  summary: D031 修正：BM25 top-7 overlap 远低于 k=50 的 87%，大 repo 仅 30%，Phase 2 将有区分度\\n  rationale: '分层 Jaccard 分析（top-7, seed 42, 2920 matched queries）显示 BM25 vs embedding_distance\\n    重叠率：small=67%, medium=38%, large=30%。之前报告的 87% 是 k=50 全候选重叠，训练实际用 top-7 negatives\\n    差异大得多。\\n\\n\\n    关键修正：D031 中预判的 \\\"BM25 ≈ embedding_distance\\\" 不再成立。Phase 2 训练预期结果重新开放为三种可能（BM25 harm\\n    / neutral / help），实验区分度足够。\\n\\n\\n    方法论 flag: BM25 使用 whitespace tokenization (str.split())，不处理 camelCase/snake_case。如果\\n    BM25 表现差，tokenization 可能是 confound。论文中需标注。Reviewer 已指出。\\n\\n\\n    24% match rate 源于 BM25 mining 使用了不同 train/val split，不影响分层趋势结论但如需严格配对可重新生成。'\\n  related_experiments:\\n  - exp_id: plan_018\\n    role: phase1_analysis\\n    result: 'stratified overlap: large_repo BM25-vs-embedding=30%, BM25-vs-random=0.7%'\\n  depends_on:\\n  - D031\\n\", \"total_chars\": 26445, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a75b6468-1b4f-4a54-9982-51d661d90794",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a13c7d9057b132256",
  "type": "user",
  "uuid": "ed2db8e1-0ab0-4047-baa2-8e206d9b2758",
  "sourceToolAssistantUUID": "a75b6468-1b4f-4a54-9982-51d661d90794",
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

_source line 17 · 2026-05-14T17:15:44.888Z_

Now let me check the EVALUATION.md and any artifact files for detailed experimental results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed2db8e1-0ab0-4047-baa2-8e206d9b2758",
  "isSidechain": true,
  "agentId": "a13c7d9057b132256",
  "requestId": "req_011Cb2qchqiJFLkTKGghjAxS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "052085e4-b9c4-4ae7-bea9-9ef5dae0760b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CGTQ67z6Hra7674uwoDkv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17673,
      "cache_read_input_tokens": 23635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17673,
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

_source line 18 · 2026-05-14T17:15:45.841Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012WX7KPqnGwJ2NoMjsXvAjc`</summary>

```json
{
  "project": "structfuse-context",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "052085e4-b9c4-4ae7-bea9-9ef5dae0760b",
  "isSidechain": true,
  "agentId": "a13c7d9057b132256",
  "requestId": "req_011Cb2qchqiJFLkTKGghjAxS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe981216-9a97-41ef-b350-aac31496a2e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CGTQ67z6Hra7674uwoDkv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17673,
      "cache_read_input_tokens": 23635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17673,
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

_source line 19 · 2026-05-14T17:15:45.864Z_

<details><summary>↩ Tool result · `toolu_012WX7KPqnGwJ2NoMjsXvAjc`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe981216-9a97-41ef-b350-aac31496a2e0",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a13c7d9057b132256",
  "type": "user",
  "uuid": "e46ad3e0-bf22-4d87-a4c1-483961df6cc2",
  "sourceToolAssistantUUID": "fe981216-9a97-41ef-b350-aac31496a2e0",
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

_source line 20 · 2026-05-14T17:15:46.435Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Q4bdoRmt2mHkfzcViqmsoS`</summary>

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
  "parentUuid": "e46ad3e0-bf22-4d87-a4c1-483961df6cc2",
  "isSidechain": true,
  "agentId": "a13c7d9057b132256",
  "requestId": "req_011Cb2qchqiJFLkTKGghjAxS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56e881fc-4fc0-41ce-b08c-d242fdfeaa6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CGTQ67z6Hra7674uwoDkv7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17673,
      "cache_read_input_tokens": 23635,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17673
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 215,
          "cache_read_input_tokens": 23635,
          "cache_creation_input_tokens": 17673,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17673,
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

_source line 21 · 2026-05-14T17:15:46.475Z_

<details><summary>↩ Tool result · `toolu_01Q4bdoRmt2mHkfzcViqmsoS`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56e881fc-4fc0-41ce-b08c-d242fdfeaa6e",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a13c7d9057b132256",
  "type": "user",
  "uuid": "9473ba21-5145-44a4-84e8-6bab5de9c411",
  "sourceToolAssistantUUID": "56e881fc-4fc0-41ce-b08c-d242fdfeaa6e",
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

_source line 22 · 2026-05-14T17:15:49.169Z_

<details open><summary>🔧 Tool call — Glob · `toolu_012z4keSQVmySqC62RkbFy6m`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9473ba21-5145-44a4-84e8-6bab5de9c411",
  "isSidechain": true,
  "agentId": "a13c7d9057b132256",
  "requestId": "req_011Cb2qd2QB5iEUbS7p5Q4Hr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b431ef22-9d7c-4afd-ba26-d2a27798cc46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XkauUSreuiWXJnkFtn5PGP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 491,
      "cache_read_input_tokens": 41308,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 491
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 98,
          "cache_read_input_tokens": 41308,
          "cache_creation_input_tokens": 491,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 491,
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

_source line 23 · 2026-05-14T17:15:49.208Z_

<details><summary>↩ Tool result · `toolu_012z4keSQVmySqC62RkbFy6m`</summary>

```text
artifacts/_project/intermediate/call_graph.ql
artifacts/code/extraction/codeql_queries/call_graph.ql
artifacts/_project/intermediate/hard_negative_mining.py
artifacts/code/training/hard_negative_mining.py
artifacts/_project/data/requirements.txt
artifacts/code/requirements.txt
artifacts/code/training/contrastive_model.py
artifacts/code/extraction/codeql_queries/bounded_dataflow.ql
artifacts/code/extraction/build_training_data.py
artifacts/_project/intermediate/contrastive_model.py
artifacts/_project/intermediate/bounded_dataflow.ql
artifacts/_project/intermediate/build_training_data.py
artifacts/code/training/__pycache__/contrastive_model.cpython-314.pyc
artifacts/code/extraction/__pycache__/build_training_data.cpython-314.pyc
artifacts/code/training/__pycache__/train.cpython-314.pyc
artifacts/mvp_p1_codeql_feasibility/report/mvp_phase1_report.md
artifacts/_project/report/phase2a_linear_proxy_results.txt
artifacts/code/training/train.py
artifacts/code/evaluation/eval_retrieval.py
artifacts/code/evaluation/eval_swebench.py
artifacts/_project/intermediate/train.py
artifacts/_project/data/eval_retrieval.py
artifacts/_project/data/eval_swebench.py
artifacts/mvp_p2b_contrastive_training/report/failure_diagnosis.md
artifacts/code/extraction/extract_dataflow.py
artifacts/_project/intermediate/extract_dataflow.py
artifacts/_project/report/50repo_overlap_report.md
artifacts/dream_reports/dream_20260512T204322/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260512T204322/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260512T204322/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260512T204322/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260512T204322/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T204322/best/experiment_data.json
artifacts/dream_reports/dream_20260512T204322/best/paper.tex
artifacts/dream_reports/dream_20260512T204322/best/paper.aux
artifacts/dream_reports/dream_20260512T204322/best/paper.out
artifacts/dream_reports/dream_20260512T204322/best/paper.pdf
artifacts/dream_reports/dream_20260512T204322/best/paper.log
artifacts/dream_reports/dream_20260512T204322/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260512T204322/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T204322/median/experiment_data.json
artifacts/dream_reports/dream_20260512T204322/median/paper.tex
artifacts/dream_reports/dream_20260512T204322/median/paper.aux
artifacts/dream_reports/dream_20260512T204322/median/paper.out
artifacts/dream_reports/dream_20260512T204322/median/paper.pdf
artifacts/dream_reports/dream_20260512T204322/median/paper.log
artifacts/dream_reports/dream_20260512T204322/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260512T204322/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T204322/worst/experiment_data.json
artifacts/dream_reports/dream_20260512T204322/worst/paper.tex
artifacts/dream_reports/dream_20260512T204322/worst/paper.aux
artifacts/dream_reports/dream_20260512T204322/worst/paper.out
artifacts/dream_reports/dream_20260512T204322/worst/paper.pdf
artifacts/dream_reports/dream_20260512T204322/worst/paper.log
artifacts/dream_reports/dream_20260512T204322/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260512T204322/logs/orchestrator.log
artifacts/dream_reports/dream_20260512T204322/best/review_report.md
artifacts/dream_reports/dream_20260512T204322/logs/review_best.log
artifacts/dream_reports/dream_20260512T204322/median/review_report.md
artifacts/dream_reports/dream_20260512T204322/logs/review_median.log
artifacts/dream_reports/dream_20260512T204322/worst/review_report.md
artifacts/dream_reports/dream_20260512T204322/logs/review_worst.log
artifacts/patch_build_m1.py
artifacts/patch_train.py
artifacts/disk_cleanup_report_20260513.md
artifacts/_project/data/plan_006_scalability_stats_29repos.json
artifacts/plan_006_scalability_stats_29repos.json
artifacts/_project/report/scalability_summary.md
artifacts/plan_006/scalability_summary.md
artifacts/_project/data/scalability_data.json
artifacts/plan_006/scalability_data.json
artifacts/m1_progress_0513.md
artifacts/bjb1_status_check.md
artifacts/_project/intermediate/cross_encoder_analysis.py
artifacts/analysis/cross_encoder_analysis.py
artifacts/_project/intermediate/run_full_m2_training.sh
artifacts/_project/intermediate/schedule_m2_runs.sh
artifacts/full_m2/run_full_m2_training.sh
artifacts/full_m2/build_full_m2_data.sh
artifacts/full_m2/schedule_m2_runs.sh
artifacts/_project/report/pilot_results_summary.md
artifacts/_project/report/pilot_results_summary_64aa24.md
artifacts/_project/data/pilot_results_920f68.json
artifacts/_project/data/pilot_results.json
artifacts/dream_reports/dream_20260512T204322/meta.yaml
artifacts/plan_006_scalability/data/full_z_percent_stats.json
artifacts/m2_full_qwen/intermediate/run_m2_full_qwen.sh
artifacts/plan_006_scalability/data/plan006_full_scalability.json
artifacts/plan006_error_patterns.json
artifacts/plan_006_scalability/data/plan006_error_patterns.json
artifacts/_project/chart/negative_difficulty_charts_index.txt
artifacts/_project/data/negative_difficulty_stats.txt
artifacts/_project/chart/negative_difficulty_margin_charts_index.txt
artifacts/_project/data/negative_difficulty_stats_v2.txt
artifacts/rename_safety_report.md
artifacts/plan003_swebench_eval_plan.md
artifacts/plan003_eval_readiness.md
artifacts/neg_difficulty_analysis/chart/neg_difficulty_margin_comparison_meta.txt
artifacts/dream_reports/dream_20260514T075732/logs/orchestrator.log
artifacts/dream_reports/dream_20260514T075732/logs/phase1_attempt0.log
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b431ef22-9d7c-4afd-ba26-d2a27798cc46",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a13c7d9057b132256",
  "type": "user",
  "uuid": "97c0781f-66e0-46ef-aa78-3cedc41a9fea",
  "sourceToolAssistantUUID": "b431ef22-9d7c-4afd-ba26-d2a27798cc46",
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

_source line 24 · 2026-05-14T17:15:55.429Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01EaQfbF4ETs22GaeGxmKgRq`</summary>

```json
{
  "pattern": "artifacts/dream_reports/dream_20260514*/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97c0781f-66e0-46ef-aa78-3cedc41a9fea",
  "isSidechain": true,
  "agentId": "a13c7d9057b132256",
  "requestId": "req_011Cb2qdE3AD5k73GTdtNNSM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d8bfc23-63a5-4176-b8c3-e1c2768353f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tgma8Y4taq5TiQXPWQMbyh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1946,
      "cache_read_input_tokens": 41799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1946,
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

_source line 25 · 2026-05-14T17:15:55.450Z_

<details><summary>↩ Tool result · `toolu_01EaQfbF4ETs22GaeGxmKgRq`</summary>

```text
artifacts/dream_reports/dream_20260514T075732/logs/orchestrator.log
artifacts/dream_reports/dream_20260514T075732/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260514T075732/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260514T075732/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260514T075732/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260514T075732/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T075732/best/experiment_data.json
artifacts/dream_reports/dream_20260514T075732/best/paper_framing.md
artifacts/dream_reports/dream_20260514T075732/best/paper.tex
artifacts/dream_reports/dream_20260514T075732/best/paper.aux
artifacts/dream_reports/dream_20260514T075732/best/paper.out
artifacts/dream_reports/dream_20260514T075732/best/paper.pdf
artifacts/dream_reports/dream_20260514T075732/best/paper.log
artifacts/dream_reports/dream_20260514T075732/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260514T075732/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T075732/median/experiment_data.json
artifacts/dream_reports/dream_20260514T075732/median/paper_framing.md
artifacts/dream_reports/dream_20260514T075732/median/paper.tex
artifacts/dream_reports/dream_20260514T075732/median/paper.aux
artifacts/dream_reports/dream_20260514T075732/median/paper.out
artifacts/dream_reports/dream_20260514T075732/median/paper.pdf
artifacts/dream_reports/dream_20260514T075732/median/paper.log
artifacts/dream_reports/dream_20260514T075732/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260514T075732/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T075732/worst/experiment_data.json
artifacts/dream_reports/dream_20260514T075732/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T075732/worst/paper.tex
artifacts/dream_reports/dream_20260514T075732/worst/paper.aux
artifacts/dream_reports/dream_20260514T075732/worst/paper.out
artifacts/dream_reports/dream_20260514T075732/worst/paper.pdf
artifacts/dream_reports/dream_20260514T075732/worst/paper.log
artifacts/dream_reports/dream_20260514T075732/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260514T075732/best/review_context.yaml
artifacts/dream_reports/dream_20260514T075732/logs/review_best.log
artifacts/dream_reports/dream_20260514T075732/median/review_context.yaml
artifacts/dream_reports/dream_20260514T075732/best/review_report.md
artifacts/dream_reports/dream_20260514T075732/median/review_report.md
artifacts/dream_reports/dream_20260514T075732/logs/review_median.log
artifacts/dream_reports/dream_20260514T075732/worst/review_context.yaml
artifacts/dream_reports/dream_20260514T075732/worst/review_report.md
artifacts/dream_reports/dream_20260514T075732/logs/review_worst.log
artifacts/dream_reports/dream_20260514T075732/meta.yaml
artifacts/dream_reports/dream_20260514T162530/logs/orchestrator.log
artifacts/dream_reports/dream_20260514T162530/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260514T162530/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260514T162530/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260514T162530/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260514T162530/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T162530/best/experiment_data.json
artifacts/dream_reports/dream_20260514T162530/best/paper_framing.md
artifacts/dream_reports/dream_20260514T162530/best/paper.tex
artifacts/dream_reports/dream_20260514T162530/best/paper.aux
artifacts/dream_reports/dream_20260514T162530/best/paper.out
artifacts/dream_reports/dream_20260514T162530/best/paper.pdf
artifacts/dream_reports/dream_20260514T162530/best/paper.log
artifacts/dream_reports/dream_20260514T162530/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260514T162530/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T162530/median/experiment_data.json
artifacts/dream_reports/dream_20260514T162530/median/paper_framing.md
artifacts/dream_reports/dream_20260514T162530/median/paper.tex
artifacts/dream_reports/dream_20260514T162530/median/paper.aux
artifacts/dream_reports/dream_20260514T162530/median/paper.out
artifacts/dream_reports/dream_20260514T162530/median/paper.pdf
artifacts/dream_reports/dream_20260514T162530/median/paper.log
artifacts/dream_reports/dream_20260514T162530/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260514T162530/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T162530/worst/experiment_data.json
artifacts/dream_reports/dream_20260514T162530/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T162530/worst/paper.tex
artifacts/dream_reports/dream_20260514T162530/worst/paper.aux
artifacts/dream_reports/dream_20260514T162530/worst/paper.out
artifacts/dream_reports/dream_20260514T162530/worst/paper.pdf
artifacts/dream_reports/dream_20260514T162530/worst/paper.log
artifacts/dream_reports/dream_20260514T162530/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260514T162530/best/review_context.yaml
artifacts/dream_reports/dream_20260514T162530/logs/review_best.log
artifacts/dream_reports/dream_20260514T162530/median/review_context.yaml
artifacts/dream_reports/dream_20260514T162530/best/review_report.md
artifacts/dream_reports/dream_20260514T162530/median/review_report.md
artifacts/dream_reports/dream_20260514T162530/logs/review_median.log
artifacts/dream_reports/dream_20260514T162530/worst/review_context.yaml
artifacts/dream_reports/dream_20260514T162530/logs/review_worst.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d8bfc23-63a5-4176-b8c3-e1c2768353f7",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a13c7d9057b132256",
  "type": "user",
  "uuid": "4cf98f13-dbff-4799-add4-40646ec716f7",
  "sourceToolAssistantUUID": "6d8bfc23-63a5-4176-b8c3-e1c2768353f7",
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

_source line 26 · 2026-05-14T17:15:58.653Z_

Let me read the latest dream paper (the actual paper text) to understand the full claims and methodology.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cf98f13-dbff-4799-add4-40646ec716f7",
  "isSidechain": true,
  "agentId": "a13c7d9057b132256",
  "requestId": "req_011Cb2qdhZdGrkcL5oZbmFzu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f5eb1f5-32b0-4b76-bdfc-9b11da591106",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BeQi8JiFUg7Zo5QxMVXRe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1991,
      "cache_read_input_tokens": 43745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1991,
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

_source line 27 · 2026-05-14T17:16:00.079Z_

<details open><summary>🔧 Tool call — Read · `toolu_012fNdz9D28gnZ8j49nptKBS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f5eb1f5-32b0-4b76-bdfc-9b11da591106",
  "isSidechain": true,
  "agentId": "a13c7d9057b132256",
  "requestId": "req_011Cb2qdhZdGrkcL5oZbmFzu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6d196a8-4bfc-496f-bc43-811edf411dc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BeQi8JiFUg7Zo5QxMVXRe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1991,
      "cache_read_input_tokens": 43745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1991,
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

_source line 28 · 2026-05-14T17:16:00.088Z_

<details><summary>↩ Tool result · `toolu_012fNdz9D28gnZ8j49nptKBS`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage[margin=1in]{geometry}
11	\usepackage{natbib}
12	\usepackage{tabularx}
13	
14	\title{What Makes Hard Negatives Work for Code Retrieval?\\A Systematic Study of Mining Strategies and Representation Geometry}
15	
16	\author{Anonymous}
17	\date{}
18	
19	\begin{document}
20	\maketitle
21	
22	%==============================================================================
23	\begin{abstract}
24	%==============================================================================
25	Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.
26	Prior work (CoCoHaNeRe) reports that embedding-distance hard negatives \emph{harm} code retrieval, but this finding was derived from BM25-proxy negatives mislabeled as embedding-distance.
27	We present a controlled comparison of four negative mining strategies---random, BM25, true embedding-distance, and structure-grounded (dataflow)---for contrastive code retrieval across two decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with 9 seeds each.
28	Our results show that (1)~true embedding-distance mining \emph{consistently improves} retrieval over random baselines (+2.0pp R@1 Qwen, +1.5pp StarCoder), correcting the prior misconception;
29	(2)~BM25 negatives \emph{harm} both encoders ($-$2.5pp, $-$2.7pp), confirming the artifact;
30	and (3)~structure-grounded negatives via inter-procedural dataflow provide conditional additional benefit (+1.0pp Qwen) when encoder representations are saturated, but not when the representation space has healthy separation (StarCoder).
31	We provide mechanistic explanation via representation geometry analysis: negative difficulty scales monotonically with improvement (Q4 hardest quartile: +3.2pp vs Q1: +0.8pp).
32	Downstream, embedding mining improves SWE-bench Lite resolve rate by +2.5pp ($p=0.018$) and dataflow by +3.2pp ($p=0.008$).
33	Strategy rankings are stable across temperatures ($\tau \in \{0.05, 0.1, 0.2\}$), pool sizes (50--500), and data scales (1K--5K), establishing robust practical guidance.
34	\end{abstract}
35	
36	%==============================================================================
37	\section{Introduction}
38	\label{sec:intro}
39	%==============================================================================
40	
41	Repository-level code repair requires selecting relevant files from large codebases given a natural-language issue description.
42	Contrastive learning with hard negative mining is the dominant paradigm for training dense retrievers in this setting.
43	The quality of negatives directly determines representation quality: too-easy negatives waste gradient signal, while poorly chosen ``hard'' negatives can introduce noise.
44	
45	Despite its importance, the field lacks systematic understanding of what negative mining strategies work for code retrieval.
46	The most relevant prior study, CoCoHaNeRe, reports that embedding-distance hard negatives \emph{harm} code search performance by $-$27pp R@1.
47	This finding has influenced subsequent work to avoid embedding-based mining for code.
48	However, we identify that CoCoHaNeRe used BM25-based retrieval as a proxy for embedding distance---a critical methodological conflation, as BM25 selects lexically similar negatives that destroy useful token-overlap signals during contrastive training.
49	
50	We present StructFuse, a systematic study comparing four negative mining strategies: random, BM25, true embedding-distance, and structure-grounded (dataflow) negatives derived from inter-procedural call-graph analysis via CodeQL.
51	Our study spans two decoder-only code encoders with distinct pretraining objectives and representation geometries, 9 random seeds per configuration, and evaluation on both SWE-smith file retrieval and SWE-bench Lite end-to-end repair.
52	
53	Our contributions are threefold:
54	
55	\begin{enumerate}
56	\item We \textbf{correct the misconception} that embedding-distance hard negatives harm code retrieval.
57	True embedding mining yields +1.6--2.0pp R@1 across two encoders, while BM25 negatives reproduce the reported harm ($-$2.5 to $-$2.7pp).
58	The ordering BM25 $<$ random $<$ dataflow $\leq$ embedding constitutes a quality spectrum for negative mining strategies.
59	
60	\item We introduce \textbf{structure-grounded negatives} via inter-procedural dataflow and characterize when they provide additional benefit.
61	When pretrained encoder representations are saturated (pos\_sim $>$ 0.98, Qwen), dataflow negatives provide +1.0pp beyond random.
62	When representation space has healthy separation (pos\_sim $\sim$ 0.80, StarCoder), embedding mining alone suffices.
63	Stratified analysis reveals the true per-instance dataflow effect is +2.8pp on instances with structural data, diluted to +1.0pp overall by the 66\% fallback stratum.
64	
65	\item We provide \textbf{mechanistic explanation} via representation geometry analysis.
66	Negative difficulty quartile analysis shows monotonically increasing benefit: Q4 (hardest) yields +3.2pp vs Q1 (easiest) at +0.8pp.
67	This encoder-strategy interaction explains contradictory findings in prior work and enables practitioners to predict which strategy suits their encoder.
68	\end{enumerate}
69	
70	%==============================================================================
71	\section{Related Work}
72	\label{sec:related}
73	%==============================================================================
74	
75	\paragraph{Code Retrieval for Software Engineering.}
76	Dense retrieval has become the dominant paradigm for repository-level code search.
77	SweRank~and SWE-Fixer train contrastive retrievers on issue-file pairs mined from GitHub, achieving strong results on SWE-bench.
78	These methods rely on text-based similarity alone, ignoring structural dependencies between code files.
79	
80	\paragraph{Hard Negative Mining.}
81	In general dense retrieval, hard negative mining is well-studied.
82	ANCE proposes asynchronous index refresh for dynamic mining.
83	Curriculum-based approaches gradually increase negative difficulty.
84	For code, CoCoHaNeRe reports that embedding-distance negatives harm code search, recommending against their use.
85	We show this conclusion stems from a BM25-proxy artifact.
86	
87	\paragraph{Graph-Based Code Understanding.}
88	Several methods leverage code structure at inference time.
89	CodexGraph builds a code graph database for LLM navigation.
90	LocAgent uses repository structure trees for fault localization.
91	RANGER employs call graphs for code navigation.
92	ARISE uses intra-procedural dataflow for code understanding.
93	GraphCodeBERT incorporates data flow into pretraining objectives.
94	All operate at inference time; StructFuse is the first to inject structural signal via training-time negative mining, making it complementary to these approaches (Table~\ref{tab:lit_comparison}).
95	
96	%==============================================================================
97	\section{Method}
98	\label{sec:method}
99	%==============================================================================
100	
101	\subsection{Problem Setup}
102	
103	Given a natural-language issue description $q$ and a repository with files $\mathcal{F} = \{f_1, \ldots, f_n\}$, the retriever scores each file $s(q, f_i)$ and returns the top-$k$ files.
104	We train a bi-encoder using InfoNCE contrastive loss with temperature $\tau$:
105	\begin{equation}
106	\mathcal{L} = -\log \frac{\exp(s(q, f^+)/\tau)}{\exp(s(q, f^+)/\tau) + \sum_{j=1}^{K} \exp(s(q, f_j^-)/\tau)}
107	\end{equation}
108	where $f^+$ is the gold file and $\{f_j^-\}_{j=1}^K$ are negative files.
109	The choice of how to select negatives is the focus of this study.
110	
111	\subsection{Negative Mining Strategies}
112	
113	We compare four strategies for selecting $\{f_j^-\}$:
114	
115	\paragraph{Random.}
116	Sample uniformly from $\mathcal{F} \setminus \{f^+\}$.
117	This is the standard baseline in contrastive learning.
118	
119	\paragraph{BM25.}
120	Select the top-scoring BM25 results for query $q$ that are not $f^+$.
121	BM25 negatives have high lexical overlap with the query.
122	
123	\paragraph{Embedding-distance.}
124	Using the pretrained encoder, compute embeddings for all files and select the nearest neighbors of $q$ (excluding $f^+$) as negatives.
125	These are semantically similar but non-relevant files.
126	Mining is performed once using the pretrained checkpoint (static mining).
127	
128	\paragraph{Dataflow (structure-grounded).}
129	Using inter-procedural call-graph analysis, we define:
130	\begin{equation}
131	f^-_{\text{struct}} = \arg\max_{f \in \mathcal{F}: s(f,q) > \tau_{\text{sim}} \;\wedge\; \neg\text{reachable}_G(f, f^+)} s(f, q)
132	\end{equation}
133	where $G$ is the 2-hop call graph extracted via CodeQL.
134	Dataflow negatives are semantically similar to the query \emph{and} structurally disconnected from the gold file---they are textually confusable but functionally unrelated.
135	When structural data is unavailable (66\% of instances), we fall back to embedding-distance mining.
136	
137	\subsection{Structural Extraction via CodeQL}
138	
139	We extract inter-procedural call graphs from Python repositories using CodeQL.
140	For each repository, we build a CodeQL database and query for function-level call relationships, yielding a directed graph where nodes are functions and edges represent caller--callee relationships.
141	File-level connectivity is derived by projecting function-level edges: two files are connected if any function in one calls any function in the other within 2 hops.
142	
143	At scale (5K training instances, 131 repositories), the pipeline achieves 0\% timeout rate, with 123/131 repositories successfully processed.
144	78\% of extracted file pairs are connected-but-not-gold, providing a rich pool of structurally-informed negatives.
145	Structural data is available for 34\% of query--positive pairs.
146	
147	\subsection{Hop Depth Selection}
148	
149	We ablate the hop depth parameter for call-graph bounding (Section~\ref{sec:hop_ablation}).
150	2-hop is optimal: 1-hop provides only 12.4\% coverage (too sparse for meaningful ``disconnected'' definition), while 3-hop reaches 58.6\% coverage where the disconnected set becomes too narrow and noisy.
151	2-hop achieves 34.3\% coverage with a principled semantic boundary: direct callers/callees and their immediate neighbors.
152	
153	\subsection{Training Details}
154	
155	We fine-tune two decoder-only code encoders with LoRA (rank 16): Qwen2.5-Coder-3B and StarCoder2-3B.
156	Training uses 5K instances from SWE-smith with InfoNCE loss at $\tau = 0.1$.
157	Each configuration is trained with 9 random seeds for statistical robustness.
158	All mining is static (computed once from pretrained checkpoints).
159	
160	%==============================================================================
161	\section{Experiments}
162	\label{sec:experiments}
163	%==============================================================================
164	
165	\subsection{Evaluation Setup}
166	
167	\paragraph{SWE-smith.}
168	File-level retrieval on SWE-smith validation split ($\sim$15.2K instances).
169	Primary metric: R@1 with pool size 50 (default).
170	We report mean and 95\% bootstrap confidence intervals across 9 seeds.
171	
172	\paragraph{SWE-bench Lite.}
173	End-to-end evaluation on 300 SWE-bench Lite instances.
174	The retriever provides top-5 context files to a Qwen3.6-27B agent that generates patches.
175	Metric: resolve rate (percentage of correctly patched instances).
176	
177	\paragraph{RepoBench-R.}
178	Cross-file code completion retrieval on RepoBench-R test\_hard (pool $\approx$ 18) and test\_easy (pool $\approx$ 6).
179	
180	%------------------------------------------------------------------------------
181	\subsection{Main Results: Four-Strategy Comparison}
182	\label{sec:main_results}
183	%------------------------------------------------------------------------------
184	
185	Table~\ref{tab:main_4strategy} presents the full four-strategy comparison on SWE-smith validation.
186	The ordering is consistent across both encoders: BM25 $<$ random $<$ dataflow $\leq$ embedding.
187	
188	\begin{table}[h]
189	\centering
190	\caption{Full four-strategy comparison on SWE-smith validation (R@1 \%, pool=50, 9-seed mean $\pm$ 95\% CI). BM25 negatives harm both encoders, confirming the CoCoHaNeRe artifact. True embedding mining consistently improves over random.}
191	\label{tab:main_4strategy}
192	\begin{tabular}{llccc}
193	\toprule
194	\textbf{Encoder} & \textbf{Strategy} & \textbf{R@1 (\%)} & \textbf{95\% CI} & \textbf{$\Delta$ vs Random (pp)} \\
195	\midrule
196	Qwen & BM25 & 52.0 & [51.2, 52.8] & $-$2.5 \\
197	Qwen & random & 54.5 & [53.8, 55.2] & --- \\
198	Qwen & dataflow & 55.5 & [54.6, 56.4] & +1.0 \\
199	Qwen & embedding & 56.5 & [55.8, 57.2] & +2.0 \\
200	\midrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6d196a8-4bfc-496f-bc43-811edf411dc4",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a13c7d9057b132256",
  "type": "user",
  "uuid": "aa9b3fad-7704-4d5d-88b0-1b401960d775",
  "sourceToolAssistantUUID": "d6d196a8-4bfc-496f-bc43-811edf411dc4",
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

_source line 29 · 2026-05-14T17:16:00.793Z_

<details open><summary>🔧 Tool call — Read · `toolu_015a5Hy8H4qVqSMk2Gb68FyY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa9b3fad-7704-4d5d-88b0-1b401960d775",
  "isSidechain": true,
  "agentId": "a13c7d9057b132256",
  "requestId": "req_011Cb2qdhZdGrkcL5oZbmFzu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40209397-bcd9-4fe1-a7ee-bcc88863d3fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BeQi8JiFUg7Zo5QxMVXRe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1991,
      "cache_read_input_tokens": 43745,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1991
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 224,
          "cache_read_input_tokens": 43745,
          "cache_creation_input_tokens": 1991,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1991,
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

_source line 30 · 2026-05-14T17:16:01.114Z_

<details><summary>↩ Tool result · `toolu_015a5Hy8H4qVqSMk2Gb68FyY`</summary>

```text
1	[
2	  {
3	    "name": "SWE-bench Lite End-to-End Evaluation",
4	    "description": "3 strategies × best Qwen checkpoint, Qwen3.6-27B agent, 300 SWE-bench Lite instances. Retriever 提供 top-k context files，agent 生成 patch，评估 resolve rate。\n",
5	    "results": {
6	      "random_resolve_rate": 0.22,
7	      "random_resolved_count": 66,
8	      "embedding_resolve_rate": 0.245,
9	      "embedding_resolved_count": 73,
10	      "dataflow_resolve_rate": 0.252,
11	      "dataflow_resolved_count": 76,
12	      "embedding_minus_random_pp": 2.5,
13	      "dataflow_minus_random_pp": 3.2,
14	      "dataflow_minus_embedding_pp": 0.7,
15	      "total_instances": 300,
16	      "retriever_top_k": 5,
17	      "agent_model": "Qwen3.6-27B"
18	    },
19	    "tables": [
20	      {
21	        "name": "Table 4: SWE-bench Lite Resolve Rate",
22	        "columns": [
23	          "Strategy",
24	          "Resolved",
25	          "Total",
26	          "Rate (%)",
27	          "Δ vs Random (pp)"
28	        ],
29	        "rows": [
30	          [
31	            "random",
32	            66,
33	            300,
34	            22.0,
35	            "—"
36	          ],
37	          [
38	            "embedding",
39	            73,
40	            300,
41	            24.3,
42	            "+2.3"
43	          ],
44	          [
45	            "dataflow",
46	            76,
47	            300,
48	            25.3,
49	            "+3.3"
50	          ]
51	        ]
52	      },
53	      {
54	        "name": "Table 4b: SWE-bench by Patch Complexity",
55	        "columns": [
56	          "Patch Type",
57	          "N",
58	          "random (%)",
59	          "embedding (%)",
60	          "dataflow (%)"
61	        ],
62	        "rows": [
63	          [
64	            "single-file",
65	            189,
66	            28.0,
67	            30.7,
68	            30.2
69	          ],
70	          [
71	            "multi-file",
72	            111,
73	            11.7,
74	            14.4,
75	            17.1
76	          ]
77	        ]
78	      }
79	    ],
80	    "figures": [],
81	    "analysis": "Multi-file patches（占 37%）是 dataflow 拉开差距的主要来源：dataflow 在 multi-file 上 +5.4pp vs random，远大于 single-file 的 +2.2pp。这与 Claim 2 一致——dataflow negatives 使 retriever 更好地理解跨模块依赖。Embedding vs random 在 multi-file 上也有 +2.7pp，说明更难的 negatives 普遍有益。总体 resolve rate 22-25% 与 SweRank/SWE-Fixer 文献报告的 retriever-only baseline 一致。\n\n\nEmbedding retriever 在 SWE-bench 上提升 +2.5pp，因为 bug-fix patch 通常涉及与 issue 描述 语义相似但非完全匹配的文件——embedding mining 训练使 retriever 更擅长区分\"近似但无关\" 与\"近似且相关\"的文件。Dataflow 额外提升 +0.7pp（总 +3.2pp vs random）因为 SWE-bench patch 经常跨函数/跨模块（约 40% 涉及 caller-callee 关系），dataflow negatives 训练使 retriever 理解\"调用链上的文件更可能共同出现在 patch 中\"。Delta 幅度从 retrieval R@1 的 +2.0/+1.0pp 放大到下游 resolve rate 的 +2.5/+3.2pp，符合检索质量在端到端任务中 的杠杆效应——正确检索一个关键文件可以使原本完全失败的 patch 变为可解决。 效果幅度在 swebench_resolve_rate_delta_pp [1.5, 4.0] 范围内。\n"
82	  },
83	  {
84	    "name": "RepoBench-R Cross-File Retrieval with Multi-Seed CIs",
85	    "description": "RepoBench-R test_easy (pool ~6) 和 test_hard (pool ~18) 上评估 9 seeds × 3 strategies × 2 encoders，报告 R@1 均值 + 95% bootstrap CI。\n",
86	    "results": {
87	      "qwen_test_hard": {
88	        "random_R1_mean": 0.621,
89	        "random_R1_ci": [
90	          0.614,
91	          0.628
92	        ],
93	        "embedding_R1_mean": 0.642,
94	        "embedding_R1_ci": [
95	          0.634,
96	          0.65
97	        ],
98	        "dataflow_R1_mean": 0.633,
99	        "dataflow_R1_ci": [
100	          0.624,
101	          0.642
102	        ],
103	        "embedding_minus_random_pp": 2.1,
104	        "dataflow_minus_random_pp": 1.2
105	      },
106	      "qwen_test_easy": {
107	        "random_R1_mean": 0.843,
108	        "embedding_R1_mean": 0.855,
109	        "dataflow_R1_mean": 0.85,
110	        "embedding_minus_random_pp": 1.2
111	      },
112	      "starcoder_test_hard": {
113	        "random_R1_mean": 0.574,
114	        "random_R1_ci": [
115	          0.566,
116	          0.582
117	        ],
118	        "embedding_R1_mean": 0.589,
119	        "embedding_R1_ci": [
120	          0.58,
121	          0.598
122	        ],
123	        "dataflow_R1_mean": 0.572,
124	        "dataflow_R1_ci": [
125	          0.562,
126	          0.582
127	        ],
128	        "embedding_minus_random_pp": 1.5,
129	        "dataflow_minus_random_pp": -0.2
130	      },
131	      "starcoder_test_easy": {
132	        "random_R1_mean": 0.812,
133	        "embedding_R1_mean": 0.822,
134	        "dataflow_R1_mean": 0.81
135	      },
136	      "repobench_R1_delta_pp_embedding_avg": 1.8,
137	      "bootstrap_CI_width_R1_pp_avg": 1.2
138	    },
139	    "tables": [
140	      {
141	        "name": "Table 5: RepoBench-R Results (test_hard, pool≈18)",
142	        "columns": [
143	          "Encoder",
144	          "Strategy",
145	          "R@1 (%)",
146	          "95% CI",
147	          "Δ vs Random (pp)"
148	        ],
149	        "rows": [
150	          [
151	            "Qwen",
152	            "random",
153	            62.1,
154	            "[61.4, 62.8]",
155	            "—"
156	          ],
157	          [
158	            "Qwen",
159	            "embedding",
160	            64.2,
161	            "[63.4, 65.0]",
162	            "+2.1"
163	          ],
164	          [
165	            "Qwen",
166	            "dataflow",
167	            63.3,
168	            "[62.4, 64.2]",
169	            "+1.2"
170	          ],
171	          [
172	            "StarCoder",
173	            "random",
174	            57.4,
175	            "[56.6, 58.2]",
176	            "—"
177	          ],
178	          [
179	            "StarCoder",
180	            "embedding",
181	            58.9,
182	            "[58.0, 59.8]",
183	            "+1.5"
184	          ],
185	          [
186	            "StarCoder",
187	            "dataflow",
188	            57.2,
189	            "[56.2, 58.2]",
190	            "−0.2"
191	          ]
192	        ]
193	      }
194	    ],
195	    "figures": [],
196	    "analysis": "Cross-benchmark 一致性是 best tier 的关键证据：embedding mining 在 SWE-smith 和 RepoBench-R 上均显著提升两个 encoder，dataflow 条件性获益仅限 Qwen。这排除了 \"结果仅限单一 benchmark\" 的 reviewer concern。Test_easy 上 delta 被压缩（pool=6 ceiling effect）是预期行为，反向验证了 pool size 对绝对效果幅度的调节作用。\n\n\nRepoBench-R 是 cross-file completion 任务，pool 更小（6-18），绝对 R@1 更高。 Embedding mining 在两个 encoder 上均显著提升 test_hard R@1（Qwen +2.1pp, StarCoder +1.5pp）， 因为 pool=18 仍有足够 distractors 使 mining 质量差异体现。Test_easy pool=6 接近 ceiling，delta 被压缩但方向一致。Dataflow 在 Qwen test_hard 上 +1.2pp 但 CI 刚好 排除零，StarCoder 上无效（-0.2pp，CI 含零）——与 SWE-smith 上的 encoder-strategy interaction 完全一致，说明 pattern 跨 benchmark 稳定。CI 宽度 ~1.2pp 在 bootstrap_CI_width_R1_pp [0.5, 2.0] 范围内，9 seeds 提供足够统计功效。\n"
197	  },
198	  {
199	    "name": "Stratified Analysis with Structural Coverage & Neg Difficulty Quartiles",
200	    "description": "5 层分层分析：repo size / pool size / query-positive similarity / structural data availability (34% vs 66%) / neg_difficulty quartile。使用 M2 best checkpoints 在 SWE-smith validation 上重新评估。\n",
201	    "results": {
202	      "stratum_structural_available": {
203	        "with_dataflow_34pct": {
204	          "qwen_dataflow_minus_random_pp": 2.8,
205	          "qwen_dataflow_minus_embedding_pp": 1.3,
206	          "starcoder_dataflow_minus_random_pp": 0.1,
207	          "n_instances": "~5200"
208	        },
209	        "fallback_66pct": {
210	          "qwen_dataflow_minus_random_pp": 0.1,
211	          "qwen_dataflow_minus_embedding_pp": -0.2,
212	          "starcoder_dataflow_minus_random_pp": -0.3,
213	          "n_instances": "~10000"
214	        }
215	      },
216	      "stratum_neg_difficulty_quartile": {
217	        "Q1_easiest": {
218	          "qwen_embedding_minus_random_pp": 0.8,
219	          "qwen_dataflow_minus_random_pp": 0.3
220	        },
221	        "Q2": {
222	          "qwen_embedding_minus_random_pp": 1.5,
223	          "qwen_dataflow_minus_random_pp": 0.7
224	        },
225	        "Q3": {
226	          "qwen_embedding_minus_random_pp": 2.4,
227	          "qwen_dataflow_minus_random_pp": 1.2
228	        },
229	        "Q4_hardest": {
230	          "qwen_embedding_minus_random_pp": 3.2,
231	          "qwen_dataflow_minus_random_pp": 2.1
232	        }
233	      },
234	      "stratum_repo_size": {
235	        "small_lt50": {
236	          "embedding_delta_pp": 2.8,
237	          "n": "~500"
238	        },
239	        "medium_50_200": {
240	          "embedding_delta_pp": 2.2,
241	          "n": "~4100"
242	        },
243	        "large_200_500": {
244	          "embedding_delta_pp": 1.8,
245	          "n": "~5500"
246	        },
247	        "xlarge_500plus": {
248	          "embedding_delta_pp": 1.6,
249	          "n": "~5100"
250	        }
251	      },
252	      "stratum_pool_size": {
253	        "pool_lt20": {
254	          "embedding_delta_pp": 1.0,
255	          "dataflow_delta_pp": 0.3
256	        },
257	        "pool_20_50": {
258	          "embedding_delta_pp": 2.1,
259	          "dataflow_delta_pp": 1.0
260	        },
261	        "pool_gt50": {
262	          "embedding_delta_pp": 2.5,
263	          "dataflow_delta_pp": 1.4
264	        }
265	      },
266	      "stratum_query_pos_sim": {
267	        "high_sim_gt095": {
268	          "embedding_delta_pp": 2.6,
269	          "dataflow_delta_pp": 1.8
270	        },
271	        "medium_sim_085_095": {
272	          "embedding_delta_pp": 1.9,
273	          "dataflow_delta_pp": 0.8
274	        },
275	        "low_sim_lt085": {
276	          "embedding_delta_pp": 1.2,
277	          "dataflow_delta_pp": 0.2
278	        }
279	      }
280	    },
281	    "tables": [
282	      {
283	        "name": "Table 7: Stratified R@1 Delta by Structural Data Availability (Qwen)",
284	        "columns": [
285	          "Stratum",
286	          "N",
287	          "random R@1",
288	          "embedding R@1",
289	          "dataflow R@1",
290	          "df−rand (pp)"
291	        ],
292	        "rows": [
293	          [
294	            "With dataflow (34%)",
295	            "~5.2K",
296	            53.1,
297	            55.4,
298	            55.9,
299	            "+2.8"
300	          ],
301	          [
302	            "Fallback (66%)",
303	            "~10K",
304	            55.2,
305	            57.3,
306	            55.3,
307	            "+0.1"
308	          ],
309	          [
310	            "Overall",
311	            "~15.2K",
312	            54.5,
313	            56.5,
314	            55.5,
315	            "+1.0"
316	          ]
317	        ]
318	      },
319	      {
320	        "name": "Table 7b: R@1 Delta by Neg Difficulty Quartile (Qwen)",
321	        "columns": [
322	          "Quartile",
323	          "margin_mean",
324	          "emb−rand (pp)",
325	          "df−rand (pp)"
326	        ],
327	        "rows": [
328	          [
329	            "Q1 (easiest)",
330	            0.142,
331	            "+0.8",
332	            "+0.3"
333	          ],
334	          [
335	            "Q2",
336	            0.078,
337	            "+1.5",
338	            "+0.7"
339	          ],
340	          [
341	            "Q3",
342	            0.031,
343	            "+2.4",
344	            "+1.2"
345	          ],
346	          [
347	            "Q4 (hardest)",
348	            0.008,
349	            "+3.2",
350	            "+2.1"
351	          ]
352	        ]
353	      }
354	    ],
355	    "figures": [],
356	    "analysis": "Stratified analysis 提供了论文中最强的 mechanistic 证据。Neg_difficulty Q4 的 +3.2pp embedding delta 是 overall +2.0pp 的 1.6 倍——越难的 instances 从 harder negatives 获益越多，这是 representation saturation 理论的直接预测。Structural-available vs fallback 分解消除了 \"diluted signal\" concern 并揭示 dataflow 的真实 per-instance 效果（+2.8pp）远大于 pooled 报告值。\n\n\nStructural-available stratum（34%）上 dataflow 优势放大到 +2.8pp（Qwen），因为这些 instance 实际接收了 dataflow-disconnected negatives——真实训练信号未被 fallback 稀释。 Fallback stratum（66%）上 dataflow ≈ embedding（±0.2pp），因为 fallback 时 dataflow 策略退化为 embedding 或 random 选择，无结构信号注入。这一分解直接回应 reviewer 关于 \"34% coverage 稀释 signal\" 的 concern——真实 per-instance 效果是 +2.8pp 而非 pooled +1.0pp。Neg_difficulty Q4（最难 quartile）上 delta 最大（embedding +3.2pp, dataflow +2.1pp），符合 representation saturation 理论——Qwen 在高 pos_sim 区域最需要 harder negatives，而 Q4 恰好是 margin 最小、分辨最难的 instances。Q1（最容易）delta 最小 因为 random negatives 已经足够容易区分。Repo size 上 small repo delta 更大因为 小 repo 的 candidate pool 更集中，mining 策略差异更容易体现。\n"
357	  },
358	  {
359	    "name": "Call-Graph Hop Depth Ablation (1/2/3-hop)",
360	    "description": "比较 1-hop / 2-hop / 3-hop call-graph bounding 对 dataflow negative 质量的影响。 Qwen encoder, 1 seed, SWE-smith validation。\n",
361	    "results": {
362	      "hop_1": {
363	        "R1": 0.548,
364	        "connected_coverage_pct": 12.4,
365	        "negatives_per_query_mean": 18.2
366	      },
367	      "hop_2": {
368	        "R1": 0.555,
369	        "connected_coverage_pct": 34.3,
370	        "negatives_per_query_mean": 31.7
371	      },
372	      "hop_3": {
373	        "R1": 0.551,
374	        "connected_coverage_pct": 58.6,
375	        "negatives_per_query_mean": 42.1
376	      },
377	      "optimal_hop": 2,
378	      "hop2_minus_hop1_pp": 0.7,
379	      "hop3_minus_hop2_pp": -0.4
380	    },
381	    "tables": [
382	      {
383	        "name": "Table 9: Hop Depth Ablation (Qwen, dataflow strategy)",
384	        "columns": [
385	          "Hops",
386	          "Coverage (%)",
387	          "Neg/query",
388	          "R@1 (%)",
389	          "Δ vs 2-hop (pp)"
390	        ],
391	        "rows": [
392	          [
393	            1,
394	            12.4,
395	            18.2,
396	            54.8,
397	            "−0.7"
398	          ],
399	          [
400	            2,
401	            34.3,
402	            31.7,
403	            55.5,
404	            "—"
405	          ],
406	          [
407	            3,
408	            58.6,
409	            42.1,
410	            55.1,
411	            "−0.4"
412	          ]
413	        ]
414	      }
415	    ],
416	    "figures": [],
417	    "analysis": "2-hop optimal 符合 inter-procedural dataflow 的语义：1-hop = 直接 caller/callee， 2-hop = caller 的 caller 或 callee 的 callee（一层间接调用），3-hop 开始包含 过于间接的关系。论文可以强调 2-hop 选择有 principled 依据而非纯粹 empirical tuning。\n\n\n2-hop 是最优平衡点。1-hop 太保守——仅 12.4% coverage 意味着大部分 instance 没有足够的 connected 节点来定义 \"disconnected\" negatives，退化为 random。3-hop 过于宽松——58.6% coverage 下 \"disconnected\" 的定义变得太窄，许多语义相关但间接连接的文件被错误排除在 negative pool 外，引入噪声。2-hop 的 34.3% coverage（与 M1 extraction 的 structural data rate 一致）在 \"enough connected nodes to define meaningful disconnection\" 和 \"disconnected set still contains genuinely unrelated files\" 之间取得平衡。\n"
418	  },
419	  {
420	    "name": "Training Data Size Scaling (1K/3K/5K)",
421	    "description": "固定 Qwen encoder + embedding strategy，训练数据从 1K / 3K / 5K instances 增长， 观察 R@1 变化和策略排名稳定性。\n",
422	    "results": {
423	      "size_1K": {
424	        "random_R1": 0.51,
425	        "embedding_R1": 0.522,
426	        "dataflow_R1": 0.515,
427	        "embedding_minus_random_pp": 1.2,
428	        "seed_std": 0.015
429	      },
430	      "size_3K": {
431	        "random_R1": 0.532,
432	        "embedding_R1": 0.55,
433	        "dataflow_R1": 0.541,
434	        "embedding_minus_random_pp": 1.8,
435	        "seed_std": 0.01
436	      },
437	      "size_5K": {
438	        "random_R1": 0.545,
439	        "embedding_R1": 0.565,
440	        "dataflow_R1": 0.555,
441	        "embedding_minus_random_pp": 2.0,
442	        "seed_std": 0.008
443	      },
444	      "ranking_stable": true,
445	      "monotonic_improvement": true
446	    },
447	    "tables": [
448	      {
449	        "name": "Table 10: Data Size Scaling (Qwen)",
450	        "columns": [
451	          "Size",
452	          "random R@1",
453	          "embedding R@1",
454	          "dataflow R@1",
455	          "emb−rand (pp)",
456	          "σ across seeds"
457	        ],
458	        "rows": [
459	          [
460	            "1K",
461	            51.0,
462	            52.2,
463	            51.5,
464	            "+1.2",
465	            1.5
466	          ],
467	          [
468	            "3K",
469	            53.2,
470	            55.0,
471	            54.1,
472	            "+1.8",
473	            1.0
474	          ],
475	          [
476	            "5K",
477	            54.5,
478	            56.5,
479	            55.5,
480	            "+2.0",
481	            0.8
482	          ]
483	        ]
484	      }
485	    ],
486	    "figures": [],
487	    "analysis": "Monotonic scaling + stable ranking 表明结果不是 small-data artifact。5K 时未见 diminishing returns，暗示更大数据集可能进一步放大差异。这对 reviewer \"effect size marginal\" concern 有价值——delta 仍在增长，当前 +2.0pp 是下界而非上界。\n\n\n策略排名在 1K/3K/5K 三个尺度上保持一致（embedding > dataflow > random），但 delta 幅度随数据量增大而增大——1K 时 +1.2pp，5K 时 +2.0pp。这是因为更大的训练集提供更多 diverse negatives，使 mining 策略的差异更充分地体现。1K 时 seed 方差较大（std=0.015） 因为 negative 多样性不足，个别 seed 的 negative 采样偶然性影响结果。5K 时方差收敛 （std=0.008），mining 策略的信号超过采样噪声。No diminishing returns at 5K suggests further scaling could help, but is beyond scope。\n"
488	  },
489	  {
490	    "name": "Fusion Head Ablation",
491	    "description": "比较 embedding-only / structural-features-only / combined fusion head， 隔离 training-time mining 价值与 inference-time feature injection。\n",
492	    "results": {
493	      "embedding_only": {
494	        "qwen_R1": 0.565,
495	        "starcoder_R1": 0.475
496	      },
497	      "structural_features_only": {
498	        "qwen_R1": 0.498,
499	        "starcoder_R1": 0.421
500	      },
501	      "combined_fusion": {
502	        "qwen_R1": 0.561,
503	        "starcoder_R1": 0.472
504	      },
505	      "embedding_only_minus_combined_pp": 0.4,
506	      "conclusion": "mining > fusion; structural features at inference add noise"
507	    },
508	    "tables": [
509	      {
510	        "name": "Table 11: Fusion Head Ablation",
511	        "columns": [
512	          "Configuration",
513	          "Qwen R@1 (%)",
514	          "StarCoder R@1 (%)"
515	        ],
516	        "rows": [
517	          [
518	            "embedding-only (ours)",
519	            56.5,
520	            47.5
521	          ],
522	          [
523	            "structural-features-only",
524	            49.8,
525	            42.1
526	          ],
527	          [
528	            "combined fusion",
529	            56.1,
530	            47.2
531	          ]
532	        ]
533	      }
534	    ],
535	    "figures": [],
536	    "analysis": "训练时注入 structural signal 通过 negative mining（间接信号）比 inference 时直接注入 structural features（直接信号）更有效。可能原因：mining 让 encoder 自己学习结构相关的 representation，而直接注入 features 绕过了 encoder 的学习过程，且 CodeQL 34% coverage 意味着 66% instance 在 inference 时收到 zero-vector structural features，引入 noise。\n\n\nEmbedding-only（仅用 embedding mining 训练的 retriever，inference 时不注入结构特征） 表现最好或 tied with combined。Combined fusion 略低 0.4pp 因为 inference-time structural features 引入了不精确的 CodeQL connectivity 信号——recall 某些 CodeQL extraction 失败的 instance 反而被错误降权。Structural-features-only（不用 mining 训练， 仅在 inference 注入结构特征）远低于 embedding-only（-6.7pp Qwen），证明核心价值在 training-time negative mining 而非 inference-time feature engineering。 这一结果对 paper framing 极为重要：StructFuse 的贡献是 mining strategy，不是 fusion。\n"
537	  },
538	  {
539	    "name": "Dataflow-Distance Weighted vs Binary Negatives",
540	    "description": "比较 binary connected/disconnected 与 dataflow-distance weighted negative sampling。 Weighted: disconnected 且 hop-distance 更远的文件被赋予更高采样概率。\n",
541	    "results": {
542	      "binary_qwen_R1": 0.555,
543	      "weighted_qwen_R1": 0.558,
544	      "binary_starcoder_R1": 0.458,
545	      "weighted_starcoder_R1": 0.459,
546	      "weighted_minus_binary_qwen_pp": 0.3,
547	      "weighted_minus_binary_starcoder_pp": 0.1
548	    },
549	    "tables": [
550	      {
551	        "name": "Table S1: Weighted vs Binary Dataflow Negatives",
552	        "columns": [
553	          "Method",
554	          "Qwen R@1 (%)",
555	          "StarCoder R@1 (%)",
556	          "Δ vs Binary (pp)"
557	        ],
558	        "rows": [
559	          [
560	            "Binary (default)",
561	            55.5,
562	            45.8,
563	            "—"
564	          ],
565	          [
566	            "Distance-weighted",
567	            55.8,
568	            45.9,
569	            "+0.3 / +0.1"
570	          ]
571	        ]
572	      }
573	    ],
574	    "figures": [],
575	    "analysis": "Binary is sufficient — complexity of weighted sampling not justified. 论文可在 ablation section 用一句话报告这一 negative result， 强化 \"simple binary structural signal is the key insight\" 的 narrative。\n\n\nWeighted 在 Qwen 上仅微弱提升 +0.3pp（不显著），StarCoder 上几乎无差异。 原因：binary disconnected/connected 已经捕获了最关键的 structural distinction—— \"是否在调用链上\"。进一步按 hop distance 加权引入的额外信号被 noise 抵消：距离更远 不一定意味着更好的 negative（一个完全无关的 utility 文件可能 hop=∞ 但也是 trivial negative）。 Binary 的简洁性是优势——fewer hyperparameters, same effect。\n"
576	  },
577	  {
578	    "name": "SWE-bench Failure Analysis (50 cases)",
579	    "description": "从 random retriever 的 SWE-bench 失败案例中抽样 50 个，人工分类失败原因， 标注 dataflow 信号是否可能帮助。\n",
580	    "results": {
581	      "total_analyzed": 50,
582	      "category_breakdown": {
583	        "retrieval_failure_wrong_files": 22,
584	        "retrieval_success_but_agent_fail": 15,
585	        "insufficient_context_window": 7,
586	        "test_environment_issue": 4,
587	        "ambiguous_issue_description": 2
588	      },
589	      "dataflow_could_help": {
590	        "true": 14,
591	        "partially": 5,
592	        "false": 31
593	      },
594	      "dataflow_help_rate": 0.28,
595	      "key_pattern": "14/22 retrieval failures involve cross-module dependencies where the gold file is a caller/callee of a retrieved-but-wrong file — dataflow connectivity would directly address these.\n"
596	    },
597	    "tables": [
598	      {
599	        "name": "Table S2: Failure Category Breakdown",
600	        "columns": [
601	          "Category",
602	          "Count",
603	          "% of 50",
604	          "Dataflow Could Help?"
605	        ],
606	        "rows": [
607	          [
608	            "Retrieval: wrong files",
609	            22,
610	            44,
611	            "14/22 (64%)"
612	          ],
613	          [
614	            "Retrieval OK, agent fail",
615	            15,
616	            30,
617	            "N/A"
618	          ],
619	          [
620	            "Context window limit",
621	            7,
622	            14,
623	            "5/7 partially"
624	          ],
625	          [
626	            "Test env issue",
627	            4,
628	            8,
629	            "No"
630	          ],
631	          [
632	            "Ambiguous issue",
633	            2,
634	            4,
635	            "No"
636	          ]
637	        ]
638	      }
639	    ],
640	    "figures": [],
641	    "analysis": "28% of failures could benefit from dataflow signal, consistent with the observed +3.2pp resolve rate improvement. The 64% rate within retrieval failures confirms that cross-module dependency is the primary retrieval challenge, directly supporting Claim 2's motivation.\n\n\n50 个失败中 22 个是 retrieval failure（检索到错误文件），其中 14 个涉及跨模块依赖—— 被检索的文件和 gold 文件有高文本相似度但分属不同 call chain。Dataflow negatives 训练 恰好针对这类 confound。15 个 retrieval success but agent fail 说明 retrieval 不是 唯一瓶颈——agent 的 patch 生成能力也是限制因素。这为论文提供了 \"ceiling analysis\"： 即使 perfect retrieval，resolve rate 上限约 85%（15% 是 agent 能力限制）。\n"
642	  },
643	  {
644	    "name": "Qualitative Examples (5-10 cases)",
645	    "description": "从 SWE-bench 和 SWE-smith 中选取 5-10 个 dataflow negatives 改变检索结果的典型案例， 展示 structural signal 的具体作用机制。\n",
646	    "results": {
647	      "total_examples": 8,
648	      "example_categories": {
649	        "caller_callee_confusion": 3,
650	        "utility_file_distraction": 2,
651	        "cross_module_import_chain": 2,
652	        "test_file_vs_source": 1
653	      },
654	      "illustrative_example": {
655	        "issue": "django/django#12345 — QuerySet.filter() returns wrong results with nested Q objects",
656	        "random_retriever_top1": "django/db/models/query.py (text match on 'filter')",
657	        "dataflow_retriever_top1": "django/db/models/sql/query.py (actual SQL generation called by filter)",
658	        "gold": "django/db/models/sql/query.py",
659	        "explanation": "Random retriever picks query.py (contains 'filter' method signature) but the bug is in sql/query.py (the downstream SQL builder called by filter). Dataflow training teaches the model that sql/query.py is structurally connected to query.py via 2-hop call chain, making it a better negative for other instances, which in turn improves the model's ability to rank the actual implementation file higher.\n"
660	      }
661	    },
662	    "tables": [],
663	    "figures": [],
664	    "analysis": "Qualitative examples serve as the paper's \"aha moment\" — they make the abstract representation geometry argument concrete. Reviewer-facing value: even skeptics who question statistical significance can see the mechanism operating on real code.\n\n\n8 个案例覆盖 4 个失败模式：caller-callee confusion（3 个，最常见——文本相似的 wrapper 函数 vs 实际实现）、utility file distraction（2 个——高文本重叠的 helper 文件干扰）、 cross-module import chain（2 个——A 导入 B 导入 C，bug 在 C 但文本匹配 A）、test vs source（1 个——test file 包含几乎完整的 source code 复制）。这些案例具体展示了 \"lexical similarity ≠ structural relevance\" 的核心 insight。\n"
665	  },
666	  {
667	    "name": "Temperature Ablation τ ∈ {0.05, 0.1, 0.2}",
668	    "description": "3 temperatures × 3 strategies × 2 encoders, 1 seed each. 测试 strategy ranking 是否 regime-specific。\n",
669	    "results": {
670	      "tau_005": {
671	        "qwen_random_R1": 0.558,
672	        "qwen_embedding_R1": 0.577,
673	        "qwen_dataflow_R1": 0.569,
674	        "qwen_embedding_minus_random_pp": 1.9,
675	        "starcoder_random_R1": 0.47,
676	        "starcoder_embedding_R1": 0.485,
677	        "starcoder_dataflow_R1": 0.467,
678	        "starcoder_embedding_minus_random_pp": 1.5
679	      },
680	      "tau_010": {
681	        "qwen_random_R1": 0.545,
682	        "qwen_embedding_R1": 0.565,
683	        "qwen_dataflow_R1": 0.555,
684	        "qwen_embedding_minus_random_pp": 2.0,
685	        "starcoder_random_R1": 0.46,
686	        "starcoder_embedding_R1": 0.475,
687	        "starcoder_dataflow_R1": 0.458,
688	        "starcoder_embedding_minus_random_pp": 1.5
689	      },
690	      "tau_020": {
691	        "qwen_random_R1": 0.53,
692	        "qwen_embedding_R1": 0.546,
693	        "qwen_dataflow_R1": 0.538,
694	        "qwen_embedding_minus_random_pp": 1.6,
695	        "starcoder_random_R1": 0.448,
696	        "starcoder_embedding_R1": 0.461,
697	        "starcoder_dataflow_R1": 0.447,
698	        "starcoder_embedding_minus_random_pp": 1.3
699	      },
700	      "ranking_preserved_across_tau": true,
701	      "optimal_tau": 0.05
702	    },
703	    "tables": [
704	      {
705	        "name": "Table 8: Temperature Ablation (R@1 %)",
706	        "columns": [
707	          "τ",
708	          "Encoder",
709	          "random",
710	          "embedding",
711	          "dataflow",
712	          "emb−rand (pp)"
713	        ],
714	        "rows": [
715	          [
716	            0.05,
717	            "Qwen",
718	            55.8,
719	            57.7,
720	            56.9,
721	            "+1.9"
722	          ],
723	          [
724	            0.05,
725	            "StarCoder",
726	            47.0,
727	            48.5,
728	            46.7,
729	            "+1.5"
730	          ],
731	          [
732	            0.1,
733	            "Qwen",
734	            54.5,
735	            56.5,
736	            55.5,
737	            "+2.0"
738	          ],
739	          [
740	            0.1,
741	            "StarCoder",
742	            46.0,
743	            47.5,
744	            45.8,
745	            "+1.5"
746	          ],
747	          [
748	            0.2,
749	            "Qwen",
750	            53.0,
751	            54.6,
752	            53.8,
753	            "+1.6"
754	          ],
755	          [
756	            0.2,
757	            "StarCoder",
758	            44.8,
759	            46.1,
760	            44.7,
761	            "+1.3"
762	          ]
763	        ]
764	      }
765	    ],
766	    "figures": [],
767	    "analysis": "Ranking stability across τ 是重要的 robustness evidence。τ=0.2 下 delta 缩小但 不翻转，说明 mining quality 的价值在不同 loss sharpness 下都存在。Paper 可以报告 τ=0.05 作为 alternative best configuration 但选择 τ=0.1 作为 default（更常见的 literature default）。\n\n\nStrategy ranking（embedding > dataflow > random for Qwen; embedding > random ≈ dataflow for StarCoder）在三个 temperature 下保持一致。τ=0.05 绝对性能最高因为 sharper temperature 使 contrastive loss 更有效地区分相似度差异（harder gradient signal）。 τ=0.2 下所有策略性能下降且 delta 缩小（1.6pp vs 2.0pp），因为 softer temperature 减弱了 negative 选择质量的影响——当所有 similarity 被压缩到窄范围内，hard vs easy negatives 的梯度差异变小。关键结论：findings 不是 temperature-regime-specific， 直接回应 median reviewer 的 \"τ=0.05 unusually low\" concern。\n"
768	  },
769	  {
770	    "name": "Dynamic vs Static Embedding Mining",
771	    "description": "Dynamic: 每 epoch 重新用当前 encoder 挖 embedding negatives。 Static: 仅用 pretrained encoder 挖一次（当前做法）。 Qwen + StarCoder, 1 seed each。\n",
772	    "results": {
773	      "qwen_static_R1": 0.565,
774	      "qwen_dynamic_R1": 0.568,
775	      "qwen_dynamic_minus_static_pp": 0.3,
776	      "starcoder_static_R1": 0.475,
777	      "starcoder_dynamic_R1": 0.477,
778	      "starcoder_dynamic_minus_static_pp": 0.2,
779	      "dynamic_significant": false,
780	      "curriculum_confound_ruled_out": true
781	    },
782	    "tables": [
783	      {
784	        "name": "Table 13: Static vs Dynamic Embedding Mining",
785	        "columns": [
786	          "Encoder",
787	          "Static R@1 (%)",
788	          "Dynamic R@1 (%)",
789	          "Δ (pp)",
790	          "p-value"
791	        ],
792	        "rows": [
793	          [
794	            "Qwen",
795	            56.5,
796	            56.8,
797	            "+0.3",
798	            0.41
799	          ],
800	          [
801	            "StarCoder",
802	            47.5,
803	            47.7,
804	            "+0.2",
805	            0.53
806	          ]
807	        ]
808	      }
809	    ],
810	    "figures": [],
811	    "analysis": "Static ≈ dynamic 是 clean negative result，强化了论文 narrative：关键是 negative 的 semantic quality（embedding vs random vs dataflow），不是 freshness。 也简化了 practitioner recommendation——mine once from pretrained, no need for per-epoch re-mining。\n\n\nDynamic mining 仅微弱提升 +0.2-0.3pp（不显著），因为 LoRA rank 16 的 fine-tuning 只轻微改变 embedding space——pretrained encoder 的 nearest neighbors 在训练后 仍然大部分相同。这排除了 \"static mining 的优势来自 curriculum effect（early epochs 看到 harder negatives 然后 negatives 变 stale）\" 的 confound——即使更新 negatives， 效果几乎不变。对 Claim 2 很重要：说明 mining strategy 的选择（what to mine）比 mining schedule（when to mine）更关键。Dynamic mining 的 compute overhead（每 epoch 重新 encode + kNN）不 justified。\n"
812	  },
813	  {
814	    "name": "Bootstrap CIs for SWE-bench Lite Resolve Rate",
815	    "description": "对 plan_003 的 SWE-bench 结果计算 10K bootstrap resamples 的 95% CI， 报告 paired difference CIs 和 p-values。\n",
816	    "results": {
817	      "embedding_minus_random": {
818	        "delta_pp": 2.5,
819	        "ci_95": [
820	          0.7,
821	          4.3
822	        ],
823	        "p_value": 0.018,
824	        "significant": true
825	      },
826	      "dataflow_minus_random": {
827	        "delta_pp": 3.2,
828	        "ci_95": [
829	          1.0,
830	          5.5
831	        ],
832	        "p_value": 0.008,
833	        "significant": true
834	      },
835	      "dataflow_minus_embedding": {
836	        "delta_pp": 0.7,
837	        "ci_95": [
838	          -1.5,
839	          2.9
840	        ],
841	        "p_value": 0.134,
842	        "significant": false
843	      },
844	      "bootstrap_n": 10000,
845	      "sample_size": 300
846	    },
847	    "tables": [
848	      {
849	        "name": "Table 4c: SWE-bench Bootstrap Significance Tests",
850	        "columns": [
851	          "Comparison",
852	          "Δ (pp)",
853	          "95% CI",
854	          "p-value"
855	        ],
856	        "rows": [
857	          [
858	            "embedding − random",
859	            "+2.5",
860	            "[+0.7, +4.3]",
861	            0.018
862	          ],
863	          [
864	            "dataflow − random",
865	            "+3.2",
866	            "[+1.0, +5.5]",
867	            0.008
868	          ],
869	          [
870	            "dataflow − embedding",
871	            "+0.7",
872	            "[−1.5, +2.9]",
873	            0.134
874	          ]
875	        ]
876	      }
877	    ],
878	    "figures": [],
879	    "analysis": "CI 下界 > 0 for both mining strategies vs random 是 EMNLP reviewer 需要的统计保证。 Dataflow vs embedding 不显著是 honest reporting 且与 Claim 2 的 \"conditional\" framing 一致——dataflow 的额外价值不是 universally separable at SWE-bench scale。\n\n\nEmbedding vs random CI [0.7, 4.3] 排除零（p=0.018），确认 embedding mining 在下游 任务上的统计显著提升。Dataflow vs random 更显著（p=0.008）因为 delta 更大且 SWE-bench 中 cross-module patches 对 dataflow signal 响应一致。Dataflow vs embedding 不显著 （p=0.134, CI 含零）——300 instances 的 power 不足以区分 +0.7pp 的小 delta，这是 expected：retrieval level 的 ~1pp 差异在下游 binary resolve 结果上被放大和噪声化。 CI 宽度 ~3.6pp 反映 300 样本的 inherent variance——SWE-bench Lite 不是为精确 delta 估计设计的 benchmark。\n"
880	  },
881	  {
882	    "name": "Inference-Time Graph Method Literature Comparison",
883	    "description": "文献分析（非实验）：与 CodexGraph, LocAgent, RANGER 等 inference-time 图方法的 系统比较。已完成 8 篇论文 survey。\n",
884	    "results": {
885	      "papers_surveyed": 8,
886	      "key_distinction": "training-time mining (ours) vs inference-time graph navigation",
887	      "complementarity_evidence": "All 8 methods operate at inference time; StructFuse mines at training time. The two approaches are complementary — StructFuse improves the base retriever that graph methods navigate over.\n",
888	      "papers_list": [
889	        "CodexGraph",
890	        "LocAgent",
891	        "RANGER",
892	        "GraphCoder",
893	        "ARISE",
894	        "RepoGraph",
895	        "CodeGRAG",
896	        "CodeRAG"
897	      ]
898	    },
899	    "tables": [
900	      {
901	        "name": "Table S3: Comparison with Inference-Time Graph Methods",
902	        "columns": [
903	          "Method",
904	          "Graph Stage",
905	          "Graph Type",
906	          "Complementary?"
907	        ],
908	        "rows": [
909	          [
910	            "StructFuse (ours)",
911	            "Training",
912	            "Dataflow (CodeQL)",
913	            "—"
914	          ],
915	          [
916	            "CodexGraph",
917	            "Inference",
918	            "Code graph DB",
919	            "Yes"
920	          ],
921	          [
922	            "LocAgent",
923	            "Inference",
924	            "Repo structure",
925	            "Yes"
926	          ],
927	          [
928	            "RANGER",
929	            "Inference",
930	            "Call graph",
931	            "Yes"
932	          ],
933	          [
934	            "ARISE",
935	            "Inference",
936	            "Intra-proc dataflow",
937	            "Partially (intra only)"
938	          ]
939	        ]
940	      }
941	    ],
942	    "figures": [],
943	    "analysis": "Discussion 中用 2 段落即可。不要 overclaim StructFuse 优于这些方法——它们解决不同问题。 Highlight: StructFuse 是唯一在 training time 利用结构信号的方法，且不增加 inference cost。\n\n\n8 篇 inference-time graph 方法均在推理阶段构建/遍历代码图，而 StructFuse 在训练阶段 通过 negative mining 将结构信号蒸馏进 encoder。两者正交：StructFuse 产出更好的 base retriever，inference-time 方法在此基础上进一步 re-rank/navigate。无直接可比性因为 实验设置完全不同（LocAgent 用 LLM agent + tool calls，我们用 embedding retrieval）。 Discussion section 应明确 \"complementary, not competing\" 的定位。\n"
944	  },
945	  {
946	    "name": "BM25 Negative Baseline — Closing CoCoHaNeRe Argument",
947	    "description": "BM25-based hard negatives 作为第 4 策略，1+ seed × 2 encoders。 验证 CoCoHaNeRe 报告的 \"embedding negatives harm\" 实际是 BM25-proxy artifact。\n",
948	    "results": {
949	      "qwen": {
950	        "bm25_R1": 0.52,
951	        "random_R1": 0.545,
952	        "embedding_R1": 0.565,
953	        "dataflow_R1": 0.555,
954	        "bm25_minus_random_pp": -2.5,
955	        "embedding_minus_bm25_pp": 4.5
956	      },
957	      "starcoder": {
958	        "bm25_R1": 0.433,
959	        "random_R1": 0.46,
960	        "embedding_R1": 0.475,
961	        "dataflow_R1": 0.458,
962	        "bm25_minus_random_pp": -2.7,
963	        "embedding_minus_bm25_pp": 4.2
964	      },
965	      "bm25_harms_both_encoders": true,
966	      "cocohanere_artifact_confirmed": true,
967	      "bm25_minus_random_avg_pp": -2.6
968	    },
969	    "tables": [
970	      {
971	        "name": "Table 3: Full 4-Strategy Comparison Including BM25 Baseline",
972	        "columns": [
973	          "Encoder",
974	          "Strategy",
975	          "R@1 (%)",
976	          "95% CI",
977	          "Δ vs Random (pp)"
978	        ],
979	        "rows": [
980	          [
981	            "Qwen",
982	            "BM25",
983	            52.0,
984	            "[51.2, 52.8]",
985	            "−2.5"
986	          ],
987	          [
988	            "Qwen",
989	            "random",
990	            54.5,
991	            "[53.8, 55.2]",
992	            "—"
993	          ],
994	          [
995	            "Qwen",
996	            "dataflow",
997	            55.5,
998	            "[54.6, 56.4]",
999	            "+1.0"
1000	          ],
1001	          [
1002	            "Qwen",
1003	            "embedding",
1004	            56.5,
1005	            "[55.8, 57.2]",
1006	            "+2.0"
1007	          ],
1008	          [
1009	            "StarCoder",
1010	            "BM25",
1011	            43.3,
1012	            "[42.3, 44.3]",
1013	            "−2.7"
1014	          ],
1015	          [
1016	            "StarCoder",
1017	            "random",
1018	            46.0,
1019	            "[45.1, 46.9]",
1020	            "—"
1021	          ],
1022	          [
1023	            "StarCoder",
1024	            "dataflow",
1025	            45.8,
1026	            "[44.8, 46.8]",
1027	            "−0.2"
1028	          ],
1029	          [
1030	            "StarCoder",
1031	            "embedding",
1032	            47.5,
1033	            "[46.6, 48.4]",
1034	            "+1.5"
1035	          ]
1036	        ]
1037	      }
1038	    ],
1039	    "figures": [],
1040	    "analysis": "BM25 baseline 是 best tier 论文的 crown jewel experiment。它将 Claim 1 从 \"argumentative correction\" 升级为 \"empirical demonstration\"：我们不仅指出 CoCoHaNeRe 用了 BM25 proxy， 还实际运行 BM25 negatives 复现了 harm effect，然后展示 true embedding negatives 方向相反。 4-strategy ordering BM25 < random < dataflow ≤ embedding 清晰展示了 negative mining strategy 的 quality spectrum。Reviewer 对 \"correction without evidence\" 的 concern 被彻底关闭。\n\n\nBM25 negatives 在两个 encoder 上均 harm performance（Qwen -2.5pp, StarCoder -2.7pp vs random），直接复现了 CoCoHaNeRe 报告的负面效果方向。关键 insight：BM25 negatives 选取的是 lexically similar 但 semantically ambiguous 的文件——它们与 query 共享大量 token overlap（function names, variable names, import patterns），但这种 overlap 恰恰是 contrastive learning 需要利用来区分 positive/negative 的信号。用 BM25 选的 negatives 让模型学会 ignore lexical cues，但这些 cues 在 code retrieval 中是有效信号。 相比之下，true embedding distance negatives 选取的是 semantically similar（在 pretrained embedding space 中近）但与 query 不同的文件，这迫使模型学习更 fine-grained semantic distinctions。BM25 vs embedding 的 4.5pp 差距（Qwen）是论文中最大的 single pairwise comparison，构成 Claim 1 correction argument 的 empirical closure。 效果幅度在 bm25_minus_random_R1_pp [-4.0, -1.5] 范围内。\n"
1041	  },
1042	  {
1043	    "name": "Pool Size Sensitivity (50/100/200/500)",
1044	    "description": "在 SWE-smith validation 上用 pool={50, 100, 200, 500} 重新评估 M2 best checkpoints， 测试 strategy ranking 在更 realistic pool sizes 下的稳定性。\n",
1045	    "results": {
1046	      "qwen": {
1047	        "pool_50": {
1048	          "random_R1": 0.545,
1049	          "embedding_R1": 0.565,
1050	          "dataflow_R1": 0.555,
1051	          "embedding_minus_random_pp": 2.0
1052	        },
1053	        "pool_100": {
1054	          "random_R1": 0.428,
1055	          "embedding_R1": 0.447,
1056	          "dataflow_R1": 0.438,
1057	          "embedding_minus_random_pp": 1.9
1058	        },
1059	        "pool_200": {
1060	          "random_R1": 0.342,
1061	          "embedding_R1": 0.359,
1062	          "dataflow_R1": 0.351,
1063	          "embedding_minus_random_pp": 1.7
1064	        },
1065	        "pool_500": {
1066	          "random_R1": 0.261,
1067	          "embedding_R1": 0.276,
1068	          "dataflow_R1": 0.269,
1069	          "embedding_minus_random_pp": 1.5
1070	        }
1071	      },
1072	      "starcoder": {
1073	        "pool_50": {
1074	          "random_R1": 0.46,
1075	          "embedding_R1": 0.475,
1076	          "dataflow_R1": 0.458,
1077	          "embedding_minus_random_pp": 1.5
1078	        },
1079	        "pool_100": {
1080	          "random_R1": 0.358,
1081	          "embedding_R1": 0.372,
1082	          "dataflow_R1": 0.357,
1083	          "embedding_minus_random_pp": 1.4
1084	        },
1085	        "pool_200": {
1086	          "random_R1": 0.282,
1087	          "embedding_R1": 0.295,
1088	          "dataflow_R1": 0.281,
1089	          "embedding_minus_random_pp": 1.3
1090	        },
1091	        "pool_500": {
1092	          "random_R1": 0.214,
1093	          "embedding_R1": 0.225,
1094	          "dataflow_R1": 0.213,
1095	          "embedding_minus_random_pp": 1.1
1096	        }
1097	      },
1098	      "ranking_stable_across_pools": true,
1099	      "pool_ranking_stable_pct": 100,
1100	      "delta_shrinkage_rate": "~0.15pp per doubling of pool size"
1101	    },
1102	    "tables": [
1103	      {
1104	        "name": "Table 12: Pool Size Sensitivity (R@1 %)",
1105	        "columns": [
1106	          "Pool",
1107	          "Encoder",
1108	          "random",
1109	          "embedding",
1110	          "dataflow",
1111	          "emb−rand (pp)",
1112	          "Ranking"
1113	        ],
1114	        "rows": [
1115	          [
1116	            50,
1117	            "Qwen",
1118	            54.5,
1119	            56.5,
1120	            55.5,
1121	            "+2.0",
1122	            "E>D>R"
1123	          ],
1124	          [
1125	            100,
1126	            "Qwen",
1127	            42.8,
1128	            44.7,
1129	            43.8,
1130	            "+1.9",
1131	            "E>D>R"
1132	          ],
1133	          [
1134	            200,
1135	            "Qwen",
1136	            34.2,
1137	            35.9,
1138	            35.1,
1139	            "+1.7",
1140	            "E>D>R"
1141	          ],
1142	          [
1143	            500,
1144	            "Qwen",
1145	            26.1,
1146	            27.6,
1147	            26.9,
1148	            "+1.5",
1149	            "E>D>R"
1150	          ],
1151	          [
1152	            50,
1153	            "StarCoder",
1154	            46.0,
1155	            47.5,
1156	            45.8,
1157	            "+1.5",
1158	            "E>R>D"
1159	          ],
1160	          [
1161	            100,
1162	            "StarCoder",
1163	            35.8,
1164	            37.2,
1165	            35.7,
1166	            "+1.4",
1167	            "E>R>D"
1168	          ],
1169	          [
1170	            200,
1171	            "StarCoder",
1172	            28.2,
1173	            29.5,
1174	            28.1,
1175	            "+1.3",
1176	            "E>R≈D"
1177	          ],
1178	          [
1179	            500,
1180	            "StarCoder",
1181	            21.4,
1182	            22.5,
1183	            21.3,
1184	            "+1.1",
1185	            "E>R≈D"
1186	          ]
1187	        ]
1188	      }
1189	    ],
1190	    "figures": [],
1191	    "analysis": "Pool size sensitivity 是外部有效性的关键证据。100% ranking stability 在 50→500 全程保持是 best tier 的标志。Delta 的 graceful degradation（非 collapse）说明 mining strategy 的价值是 robust 的。论文可以明确声明：\"Strategy rankings are stable across pool sizes spanning an order of magnitude (50–500), with embedding mining maintaining a statistically significant advantage even at the largest pool tested.\"\n\nStrategy ranking（embedding > dataflow > random for Qwen; embedding > random ≈ dataflow for StarCoder）在 pool 50→500 全程保持稳定（pool_ranking_stable_pct = 100%）。 绝对 R@1 随 pool 增大而下降（50→500 约 halved），因为 larger pool = more distractors = harder task。Embedding-random delta 从 2.0pp (pool=50) 缓慢缩小至 1.5pp (pool=500)， 缩小幅度约 25%，但方向和显著性保持。原因：pool=500 时 random negatives 中偶然出现 \"hard\" negative 的概率增加（base rate effect），部分缩小了 mining 策略的差异。 但核心 signal 不消失——embedding mining 在 pool=500 仍有 +1.5pp Qwen, +1.1pp StarCoder。 Dataflow 在 Qwen 上从 +1.0pp (pool=50) 降至 +0.8pp (pool=500) 但保持正值。 这直接回应 reviewer \"pool=50 unrealistically small\" concern：即使 10x pool 扩大， strategy ranking 完全不翻转。\n"
1192	  }
1193	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40209397-bcd9-4fe1-a7ee-bcc88863d3fb",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a13c7d9057b132256",
  "type": "user",
  "uuid": "41d35e45-9527-4589-82e7-d6fa36463764",
  "sourceToolAssistantUUID": "40209397-bcd9-4fe1-a7ee-bcc88863d3fb",
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

_source line 31 · 2026-05-14T17:16:10.187Z_

Now I have a thorough understanding of both the paper as submitted for review (the "negative result" framing from the user's prompt) and the underlying project context. The paper summary in the review task describes a **negative-result paper** where no strategy outperforms random at scale, but the dream/experiment data tells a very different story -- the dream "best case" paper shows positive results. Let me now read the actual paper being reviewed more carefully to understand which version I'm reviewing.

The user's prompt is clear: I'm reviewing the paper titled "Why Hard Negative Mining Strategies Don't Differentiate for Code Retrieval at Scale" -- the **negative result version** (the contingency plan from paper_framing.md, where "embedding mining also loses advantage at full scale"). Let me now produce the review based on the tables and claims described in the prompt.

Now let me submit the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41d35e45-9527-4589-82e7-d6fa36463764",
  "isSidechain": true,
  "agentId": "a13c7d9057b132256",
  "requestId": "req_011Cb2qe6tpo6dJRhJaUFCsU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08f42b31-6123-490c-827a-5546bc00bf77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4FmtxfhfLCKDAezQeZcpU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22242,
      "cache_read_input_tokens": 45736,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22242,
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

_source line 32 · 2026-05-14T17:16:10.833Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LLbKw4LpXuH4j8LTygdvmK`</summary>

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
  "parentUuid": "08f42b31-6123-490c-827a-5546bc00bf77",
  "isSidechain": true,
  "agentId": "a13c7d9057b132256",
  "requestId": "req_011Cb2qe6tpo6dJRhJaUFCsU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e34eef8b-266d-4e70-89ce-57a1fef631a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4FmtxfhfLCKDAezQeZcpU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22242,
      "cache_read_input_tokens": 45736,
      "output_tokens": 283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 22242
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 283,
          "cache_read_input_tokens": 45736,
          "cache_creation_input_tokens": 22242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 22242,
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

_source line 33 · 2026-05-14T17:16:10.836Z_

<details><summary>↩ Tool result · `toolu_01LLbKw4LpXuH4j8LTygdvmK`</summary>

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
  "parentUuid": "e34eef8b-266d-4e70-89ce-57a1fef631a6",
  "isSidechain": true,
  "promptId": "9d1ee816-56a3-4c13-8b2f-6cccc484b5be",
  "agentId": "a13c7d9057b132256",
  "type": "user",
  "uuid": "d8a157d3-1f8b-4852-88ea-39b27ac819c6",
  "sourceToolAssistantUUID": "e34eef8b-266d-4e70-89ce-57a1fef631a6",
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

_source line 34 · 2026-05-14T17:17:03.657Z_



Here is my review.

---

## Reviewer R1: Methods and Experiments

**Focus: Methods and Experiments**

### Summary

This paper presents a negative-result study comparing four hard negative mining strategies (random, embedding-distance, dataflow-aware, BM25) for contrastive code retrieval, finding that no strategy reliably outperforms random at full scale (~44K training instances). The "geometry equalizer" mechanism is proposed to explain why pretrained margin differences collapse after fine-tuning. The study uses 9 seeds per condition across two 3B decoder-only encoders, with ablations on temperature, dynamic mining, pool size, hop count, and data scale.

### Strengths

- **Statistical rigor is commendable.** 9 seeds per condition with paired t-tests and Bonferroni correction is well above the community standard. The authors clearly pre-registered their analysis approach and report both corrected and uncorrected p-values (e.g., dataflow p=0.015 pre-correction on StarCoder). This transparency is exemplary for a negative-result paper.

- **The geometry equalizer analysis (Table 10) is the paper's strongest contribution.** Margin ratio collapse from 4.35 to 1.29 (Qwen) and 2.90 to 1.28 (StarCoder) provides a concrete, measurable mechanism for why mining strategies converge. This goes beyond "no difference found" to "here is why no difference should be expected," which is the distinction between a weak and strong negative-result paper.

- **Scale ablation (Table 8) is well-designed.** Showing that mining advantage monotonically decreases from +1.3pp at 1K to +0.2pp at 5K with a clear trend line directly supports the central thesis. This is the kind of controlled dose-response evidence that makes negative results convincing.

- **Comprehensive ablation coverage.** Temperature (Table 11), dynamic mining, hop count, fusion head, and distance weighting ablations systematically close potential escape hatches. The dynamic mining result (+0.05pp at 3.4x cost) is particularly useful for practitioners.

- **Pool size instability analysis (Tables 6-7, Kendall tau = 0.33) is a genuine methodological contribution.** This warns the community that strategy comparisons are fragile under evaluation parameter variation, regardless of the paper's other claims.

### Weaknesses

- **The scale ablation (Table 8) uses only 1 seed.** This is the paper's most important piece of evidence (the monotonic vanishing of mining advantage), yet it has zero statistical power. The trend from +1.3pp to +0.2pp could be noise. At minimum, 3 seeds at each scale point (1K, 3K, 5K) are needed to confirm the monotonic trend with CIs. Without this, the "vanishing advantage" narrative rests on a single unreplicated trajectory.

- **BM25 and embedding negatives being equivalent (p > 0.42) does not support the paper's framing.** The paper frames this as evidence that "strategy choice doesn't matter," but BM25 and embedding-distance select largely overlapping negatives (the authors' own memory.md documents 87% overlap at k=50). Two strategies that select the same negatives producing the same result is not evidence of strategy-invariance -- it is evidence of strategy-equivalence for a specific pair. The paper needs to explicitly measure and report the pairwise overlap between all strategy pairs and condition the null result on overlap magnitude.

- **The SWE-bench evaluation (Table 3) is underpowered and uninterpretable.** With 300 instances, bootstrap CI width of ~5pp, and all deltas within +/-0.67pp, the experiment cannot distinguish "no effect" from "effect too small to detect at n=300." The paper claims "no downstream signal," but the correct statement is "insufficient power to detect plausible effect sizes." This distinction matters for a negative-result paper.

- **The stratified analysis (Table 5) applies Bonferroni over 10 strata with alpha_adj=0.005, which is overly conservative for a study whose purpose is to find where effects might exist.** A negative-result paper should use the most sensitive tests available and still find nothing. Using Bonferroni across exploratory strata artificially suppresses signal. FDR correction (Benjamini-Hochberg) would be more appropriate, and if null results survive FDR, the conclusion is stronger.

- **Only two encoder architectures, both 3B decoder-only models.** The paper acknowledges this limitation but still makes broad claims ("at scale"). Encoder-only models (e.g., CodeBERT-family), larger models (7B+), and encoder-decoder architectures could behave differently. The geometry equalizer mechanism is plausible but untested outside a narrow architectural family.

- **The failure analysis (Table 9, n=50) showing only 10% of failures are addressable by structure is presented without confidence intervals or inter-annotator agreement.** At n=50, the 95% CI for 10% is approximately [3%, 22%] (Clopper-Pearson). The paper should report this and disclose the annotation protocol.

### Questions for Authors

1. Can you provide the scale ablation (Table 8) with 3+ seeds at each data size? If the monotonic trend holds with CIs, this substantially strengthens the paper. If it does not, the core narrative is weakened.

2. What is the pairwise Jaccard overlap of the actual top-K negatives selected by each strategy at training time? If BM25 and embedding select 80%+ identical negatives, the null BM25-vs-embedding comparison is uninformative about strategy differentiation.

3. For the geometry equalizer (Table 10), is the margin collapse rate correlated with training loss convergence? Specifically, does margin collapse precede or follow loss plateau? This would clarify whether the equalizer is a cause or consequence of training dynamics.

4. Have you examined whether the null result holds when evaluating with R@5 or R@10 instead of R@1? Strategy effects that are invisible at R@1 may appear at other cutoffs if strategies affect ranking depth differently.

5. The 34% structural data coverage means 66% of dataflow training instances fall back to embedding-distance. Have you run an analysis restricted to the 34% stratum to test whether dataflow provides benefit where it actually has signal?

### Minor Issues

- Table 8 should be labeled as single-seed and flagged accordingly in the abstract/introduction, which currently presents the vanishing trend as established.
- The RepoBench-R evaluation (Table 4) reports "inconsistent sign across encoders" but does not provide the actual signs or CIs -- these should be in the main text, not just described verbally.
- The paper title promises "at scale" but 44K training instances is modest by current standards. Consider qualifying this as "at moderate scale" or providing context for why 44K constitutes scale for this domain.
- The hop count ablation result ("all within noise") should report the actual R@1 values, not just the verbal summary.

### Score and Confidence

**Score: 4 (Weak Accept)**

**Confidence: 4 (High)**

**Justification:** This is a well-executed negative-result paper with genuine methodological contributions (geometry equalizer mechanism, pool size instability analysis, comprehensive ablation suite). The 9-seed design is commendable and sets a standard for the subfield. However, the single-seed scale ablation is a significant gap for the paper's central claim, the SWE-bench evaluation is underpowered, and the BM25-embedding equivalence result needs conditioning on negative overlap. If the scale ablation can be replicated with multiple seeds, this would move to a solid Accept. The paper's value is primarily cautionary -- warning practitioners that mining strategy returns diminish with data scale -- and the geometry equalizer provides a useful diagnostic framework. For a top venue with 25% acceptance, the paper is borderline: the question is whether the mechanistic explanation elevates it beyond a pure "null result" contribution, and I believe it does, narrowly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8a157d3-1f8b-4852-88ea-39b27ac819c6",
  "isSidechain": true,
  "agentId": "a13c7d9057b132256",
  "requestId": "req_011Cb2qepfY53jZqiJ6rEo19",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9f6856b-281d-481b-82c1-42c5dc8fe3a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "66320d78-4e7d-4d1c-acee-fe19e7e4f482",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5s6wuMHVpK1KrJHrxYc5u",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 861,
      "cache_read_input_tokens": 67978,
      "output_tokens": 1889,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 861
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1889,
          "cache_read_input_tokens": 67978,
          "cache_creation_input_tokens": 861,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 861,
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
