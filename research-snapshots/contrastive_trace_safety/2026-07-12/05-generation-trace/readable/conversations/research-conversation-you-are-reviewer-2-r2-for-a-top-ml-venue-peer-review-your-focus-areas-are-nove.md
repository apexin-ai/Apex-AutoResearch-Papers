# Research conversation: You are Reviewer 2 (R2) for a top ML venue peer review. Your focus areas are **novelty**, **related work**, and **positi

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a24dc168858e197af.jsonl`
- **Structured JSON:** [`3e07a1ac4da758cafa95.json`](../../sessions/3e/3e07a1ac4da758cafa95.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

52 recorded events

### User

_source line 1 · 2026-05-16T16:03:51.265Z_

You are Reviewer 2 (R2) for a top ML venue peer review. Your focus areas are **novelty**, **related work**, and **positioning/framing**. Use a 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept. Target venue acceptance rate ~25%.

## Paper Summary

**Title:** "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies, Representation Geometry, and Evaluation Methodology"

The paper presents a controlled comparison of 4 negative mining strategies (random, static embedding-distance, dataflow-aware structural, BM25-based) across 2 3B-parameter code encoders (Qwen2.5-Coder-3B and StarCoder2-3B). Three contributions claimed:
1. Static embedding-distance mining reliably improves retrieval (+1.4pp Qwen, +0.9pp StarCoder on held-out eval) at zero compute cost, refuting CoCoHaNeRe's claim that embedding negatives are ineffective (they conflated BM25 with embedding negatives).
2. Structure-grounded negatives interact with encoder representation geometry—benefits concentrate in hard-instance strata.
3. Checkpoint selection criterion effects (Δ up to +16.3pp) exceed mining strategy effects (~1pp) by 7×, revealing evaluation methodology confound.

## Paper Structure (10 pages)

**Introduction:** Motivates systematic study. Notes CoCoHaNeRe conflation issue. Lists 4 strategies and 3 contributions.

**Related Work (Section 2):**
- Code retrieval: SweRank, SWE-Fixer use random/heuristic negatives. LocAgent, RANGER, CodexGraph use structural info at inference not training.
- Hard negative mining: ANCE (dynamic), CoCoHaNeRe (concludes embedding negatives ineffective—paper argues this is BM25-proxy artifact).
- Structural code analysis: ARISE (intra-procedural), GraphCodeBERT (data-flow attention). Paper uses inter-procedural call-graph for negative *selection*.

**Method (Section 3):** InfoNCE loss, 4 mining strategies defined, CodeQL structural extraction (2-hop, 90% coverage), query-split evaluation protocol (500 selection / 2480 held-out), LoRA rank 16 on SWE-smith 5K.

**Experiments (Section 4):** 14 tables covering main results, statistical significance, scale boundary, external validation, stratified analysis, temperature ablation, pool size sensitivity, checkpoint criterion effect, and 5+ ablations.

**Discussion (Section 5):** Why BM25 harms, implications for CoCoHaNeRe, evaluation recommendations.

**Limitations (Section 6):** OOD failure on SWE-bench (R@1=0.04 vs BM25=0.273), only 2 3B encoders.

**References:** 7 cited works (Yang, Xie, Su, Xiong, Guo, Liu, Ma).

## Key Claims to Evaluate for Novelty

1. **CoCoHaNeRe refutation:** Paper claims CoCoHaNeRe's negative result about embedding negatives stems from conflating BM25-proxy with true embedding-distance negatives. Paper shows BM25 negatives harm (−2.7pp) while true embedding negatives help (+0.9–1.4pp).

2. **"Representation geometry interaction"** (Contribution 2): Dataflow negatives show encoder-dependent effects. Stratified analysis shows benefits concentrate in hard-instance strata. Paper calls this a "shared underlying mechanism rather than complementary signal."

3. **Query-split evaluation methodology** (Contribution 3): Checkpoint selection criterion effect up to +16.3pp, 7× larger than mining effect. Proposes splitting val queries into selection set and held-out evaluation set.

4. **Scale boundary at 125M:** UniXcoder null result.

## Your Review Task

Produce a structured review with:
1. **Summary** (2-3 sentences)
2. **Strengths** (bulleted, focus on novelty, significance of contributions, positioning against prior work, clarity)
3. **Weaknesses** (bulleted, focus on: novelty concerns, related work gaps, overclaiming, framing issues, whether contributions are truly novel vs incremental, whether the "representation geometry" claim is substantiated)
4. **Questions for Authors** (numbered)
5. **Minor Issues** (if any)
6. **Overall Score** (1-6) with 1-sentence justification
7. **Confidence** (1-5)

Be rigorous but fair. Consider:
- Is the CoCoHaNeRe refutation a significant contribution or a narrow correction?
- Is "representation geometry interaction" (Contribution 2) well-supported or speculative?
- Is the query-split evaluation a genuine methodological contribution or obvious good practice?
- Is the related work comprehensive enough? Only 7 references seems thin.
- Does the paper overclaim given effect sizes of ~1pp?
- How does this compare to what a typical EMNLP/ACL/NeurIPS reviewer would expect in terms of novelty and depth?
- The paper is positioned as a "systematic study" — is the scope sufficient for that claim?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "79c8f08e-6032-49c6-8800-642b5547187a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T16:03:51.269Z_

```json
{
  "parentUuid": "79c8f08e-6032-49c6-8800-642b5547187a",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
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
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
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
  "uuid": "63e77866-158a-4ab2-a8e2-b221b8fe5ef5",
  "timestamp": "2026-05-16T16:03:51.269Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T16:03:54.129Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63e77866-158a-4ab2-a8e2-b221b8fe5ef5",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6XkmA3JAYxDkP6nX1Bf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13fc5791-d209-4e77-a81a-f3888a8563f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NaE1LdTe7to5NgbC74TMEj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7054,
      "cache_read_input_tokens": 7330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7054,
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

_source line 4 · 2026-05-16T16:03:54.996Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016sp8GMKnAaD7ddAx7GyAND`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13fc5791-d209-4e77-a81a-f3888a8563f2",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6XkmA3JAYxDkP6nX1Bf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eff87708-523c-4cdb-9017-78b5a2bc223a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NaE1LdTe7to5NgbC74TMEj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7054,
      "cache_read_input_tokens": 7330,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7054
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 141,
          "cache_read_input_tokens": 7330,
          "cache_creation_input_tokens": 7054,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7054,
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

_source line 5 · 2026-05-16T16:03:55.001Z_

<details><summary>↩ Tool result · `toolu_016sp8GMKnAaD7ddAx7GyAND`</summary>

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
  "tool_name": "mcp__agent-ml-research__director_post_to_reviewer"
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
  "parentUuid": "eff87708-523c-4cdb-9017-78b5a2bc223a",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "a4b8114c-1c12-47c3-a033-260ae5b5053b",
  "sourceToolAssistantUUID": "eff87708-523c-4cdb-9017-78b5a2bc223a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-16T16:03:57.468Z_



Let me read the paper and project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4b8114c-1c12-47c3-a033-260ae5b5053b",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6Xm3Gu9k3PAg4ZDeUCa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "673c8d9a-1af5-4644-8833-48c7c77e5349",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XWLWkuzxFxzp2DFKNkZBi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2256,
      "cache_read_input_tokens": 14384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2256,
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

_source line 7 · 2026-05-16T16:03:58.470Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Y58G7kAEsPtRs5Mg4ySchC`</summary>

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
  "parentUuid": "673c8d9a-1af5-4644-8833-48c7c77e5349",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6Xm3Gu9k3PAg4ZDeUCa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c47d95b2-1296-449a-ab6f-82e725efee46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XWLWkuzxFxzp2DFKNkZBi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2256,
      "cache_read_input_tokens": 14384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2256,
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

_source line 8 · 2026-05-16T16:03:58.480Z_

<details><summary>↩ Tool result · `toolu_01Y58G7kAEsPtRs5Mg4ySchC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| unixcoder-3strat-s43 | UniXcoder-base s43: 3 strategies (random/embedding/dataflow) × seed 43, patience=2。与 s42 (patience=3) 构成 2-seed 统计，验证 null result 稳定性。Director D064 批准。 | — | — | — |\\n| m2_full_starcoder_resumed | M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。 | — | — | — |\\n| m2_full_qwen_continued | M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。 | — | — | — |\\n\\n## 待处理\\n- plan_018_bm25: BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。（排队等待 GPU）\\n- plan_015_dynamic: Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen, s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。（排队等待 GPU）\\n- plan_005_stratified: Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制 pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。（准备中）\\n- unixcoder-3strat-s44: UniXcoder-base s44: 3 strategies (random/embedding/dataflow) × seed 44, patience=2。与 s42/s43 构成 3-seed 统计，确认 encoder-only/small-scale null result。Director D064 批准。（准备中）\\n- qwen_random_s42_retrain: Qwen random_s42 重训（统一 regime: 2 epoch + early_stopping_patience=2）。原 s42 用 3 epoch + patience=0 导致 pool=50 R@1 异常低（0.2730 vs s43=0.3138/s44=0.3181），不可纳入 cross-seed 统计。重训后可补完 3-seed comparison。Director 批准方案 B。（准备中）\\n\\n## 近期结论\\n- **unixcoder-3strat-s42** (negative): UniXcoder-base (125M, encoder-only RoBERTa) 第三 encoder: 3 strategies (random/embedding/dataflow) × seed 42。验证 embedding distance mining 优势是否跨架构泛化（encoder-only vs decoder-only）。batch_size=16, max_seq_length=1024, LoRA, gradient-checkpointing。\\n- **unixcoder_3strat_s42** (failed): UniXcoder-base 第三 encoder: 3 strategies (random/embedding/dataflow) × seed 42。验证 embedding distance mining 优势是否跨架构泛化（RoBERTa vs decoder-only）。\\n- **m1_reextract_v2** (success): M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 ← 基于 m1_extraction\\n\\n## 趋势\\n成功 12 / 负向 3 / 失败 5 / 共 34\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-42106: 无 GPU 信息\\n\\n## 告警\\n- p2b-smoke-test: 已被终止 — unknown\\n- p2b-smoke2: 已被终止 — unknown\\n- p2b-smoke3: 已被终止 — unknown\\n- p2b-smoke4: 已被终止 — unknown\\n- p2b-smoke5: 已被终止 — unknown\\n- p2b-smoke6: 已被终止 — unknown\\n- p2b-smoke7: 已被终止 — unknown\\n- p2b-smoke8: 已被终止 — unknown\\n- p2b-all-9runs: 已被终止 — unknown\\n- mvp_p2b_contrastive_training: 已被终止 — unknown\\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\\n- p2b_eval_all: 已被终止 — unknown\\n- m2_early_pilot: 已被终止 — unknown\\n- m2_early_pilot_v2: 训练失败 — unknown\\n- m2_early_pilot_v3: 已被终止 — unknown\\n- m2_full_starcoder: 训练失败 — unknown\\n- m1_reextract: 训练失败 — unknown\\n- plan_003_swebench_eval: 训练失败 — unknown\\n- unixcoder_3strat_s42: 训练失败 — unknown\\n\", \"total_chars\": 3264, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c47d95b2-1296-449a-ab6f-82e725efee46",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "da1c239c-e9fc-4bcb-9d3a-a1bc70b55078",
  "sourceToolAssistantUUID": "c47d95b2-1296-449a-ab6f-82e725efee46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T16:03:59.373Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014rVSzY8AqCkhVS69aiC7iG`</summary>

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
  "parentUuid": "da1c239c-e9fc-4bcb-9d3a-a1bc70b55078",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6Xm3Gu9k3PAg4ZDeUCa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f90f6087-675f-4a49-8a2e-0837bcbdc59a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XWLWkuzxFxzp2DFKNkZBi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2256,
      "cache_read_input_tokens": 14384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2256,
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

_source line 10 · 2026-05-16T16:03:59.382Z_

<details><summary>↩ Tool result · `toolu_014rVSzY8AqCkhVS69aiC7iG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\n\\n- **Headline result template**: \\\"Simple static embedding-distance mining improves code retrieval in pilot and initial M2 seed (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; consistency across remaining seeds pending; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective.\\\"\\n\\n## Core Insight\\n\\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\n- Backup: \\\"Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### Evidence presentation strategy:\\n- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)\\n- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)\\n- Both metrics show directionally consistent results; no goalpost-moving between metrics\\n\\n### In progress:\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 DONE (R@1=0.6009, early stopped step 500), embedding_distance_s43 DONE (R@1=0.5606, early stopped step 1500). 4/9 runs complete, ~35h remaining.\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\n- m1_reextract_v2: 90.5% complete (25,582/28,276), 0 ERROR, ETA ~19:00 CST May 15\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Limitations\\n\\nEffect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"Simple embedding mining provides reliable zero-cost improvement + CodeQL extraction is practical + representation geometry analysis may help explain prior contradictions\\\"\\n- Still publishable: reliable zero-cost baseline demonstration + mechanistic analysis is sufficient for EMNLP Main\\n\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the narrative positioning needs adjustment\\n- Pivot: \\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps, establishing it as a reliable zero-cost baseline even when BM25 provides no signal\\\"\\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining provides reliable improvement) stands regardless of BM25 outcome\\n- Claim 1 core preserved: \\\"Simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling\\\"\\n- Impact: BM25 result determines narrative nuance, not core contribution\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\\n&lt;!-- D041 formal definition fix: reachable_G → ¬reachable_G, 2026-05-15 -->\\n&lt;!-- Claim 2 exploratory wording unification: 2026-05-15 -->\\n&lt;!-- D049 Claim 1 framing update: numbers, narrative softening, evidence strategy, limitations: 2026-05-15 -->\\n&lt;!-- Status data refresh: s44 DONE, 4/9 runs, m1 90.5%, headline caveat: 2026-05-15 -->\\n\", \"total_chars\": 14424, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f90f6087-675f-4a49-8a2e-0837bcbdc59a",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "0df01b8d-957c-4d6e-9469-d7662f3a1480",
  "sourceToolAssistantUUID": "f90f6087-675f-4a49-8a2e-0837bcbdc59a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T16:03:59.703Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012xPefAP6xUUw6EUiQ3ABa4`</summary>

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
  "parentUuid": "0df01b8d-957c-4d6e-9469-d7662f3a1480",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6Xm3Gu9k3PAg4ZDeUCa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0dde18e6-6a95-41be-be58-00baee87b594",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XWLWkuzxFxzp2DFKNkZBi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2256,
      "cache_read_input_tokens": 14384,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2256
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 306,
          "cache_read_input_tokens": 14384,
          "cache_creation_input_tokens": 2256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2256,
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

_source line 12 · 2026-05-16T16:03:59.712Z_

<details><summary>↩ Tool result · `toolu_012xPefAP6xUUw6EUiQ3ABa4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-14\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\n# 总计: 60 entries (含 2 个软件工具引用)\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\\\"\\n        venue: \\\"NeurIPS (Datasets & Benchmarks, Spotlight)\\\"\\n        year: 2025\\n        relation: building-block\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\\\"\\n\\n      - title: \\\"SweRank: Software Issue Localization with Code Ranking\\\"\\n        authors: \\\"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\\\"\\n\\n      - title: \\\"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\\\"\\n        authors: \\\"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\\\"\\n        venue: \\\"ACL (Findings)\\\"\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Curriculum Learning for Dense Retrieval Distillation\\\"\\n        authors: \\\"Hansi Zeng, Hamed Zamani, Vishwa Vinay\\\"\\n        venue: \\\"SIGIR (Best Short Paper)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\\\"\\n\\n      - title: \\\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\\\"\\n        authors: \\\"Fan Y., Li C., Ge J., Huang L., Luo B.\\\"\\n        venue: \\\"ACM TOSEM\\\"\\n        year: 2025\\n        relation: contrast-target\\n        summary: \\\"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\\\"\\n        note: \\\"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\\\"\\n\\n      - title: \\\"Representation Learning with Contrastive Predictive Coding\\\"\\n        authors: \\\"Aaron van den Oord, Yazhe Li, Oriol Vinyals\\\"\\n        venue: arXiv\\n        year: 2018\\n        relation: background\\n        summary: \\\"InfoNCE 损失函数：对比预测编码的无监督表示学习。StructFuse 训练目标的理论根基。\\\"\\n\\n      - title: \\\"Contrastive Learning with Hard Negative Samples\\\"\\n        authors: \\\"Joshua David Robinson, Ching-Yao Chuang, Suvrit Sra, Stefanie Jegelka\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: method-component\\n        summary: \\\"HCL: 可控 hard negative 采样，证明更难的 negatives 加速和改善学习，但暗示过度 hard 会导致问题。StructFuse difficulty analysis 的理论起点。\\\"\\n\\n      - title: \\\"Debiased Contrastive Learning\\\"\\n        authors: \\\"Ching-Yao Chuang, Joshua Robinson, Yen-Chen Lin, Antonio Torralba, Stefanie Jegelka\\\"\\n        venue: NeurIPS\\n        year: 2020\\n        relation: method-component\\n        summary: \\\"DCL: 去偏对比目标，修正 false negatives（同类样本被当作 negatives）问题。False negative 是 hard negative 过拟合的重要来源。\\\"\\n\\n      - title: \\\"Hard Negative Mixing for Contrastive Learning\\\"\\n        authors: \\\"Yannis Kalantidis, Mert Bulent Sariyildiz, Noe Pion, Philippe Weinzaepfel, Diane Larlus\\\"\\n        venue: NeurIPS\\n        year: 2020\\n        relation: method-component\\n        summary: \\\"MoCHi: feature-level hard negative 混合合成，开销极小。与 StructFuse 的 structure-based negative mining 形成对比。\\\"\\n\\n      - title: \\\"Understanding Hard Negatives in Noise Contrastive Estimation\\\"\\n        authors: \\\"Wenzheng Zhang, Karl Stratos\\\"\\n        venue: NAACL\\n        year: 2021\\n        relation: background\\n        summary: \\\"理论分析：用模型分布作为 negative 分布可减少梯度偏差。为 hard negative 作用提供理论解释。\\\"\\n\\n      - title: \\\"ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning\\\"\\n        authors: \\\"Jun Xia, Lirong Wu, Ge Wang, Jintao Chen, Stan Z. Li\\\"\\n        venue: ICML\\n        year: 2022\\n        relation: method-component\\n        summary: \\\"揭示图对比学习中 hard negative = false negative 的陷阱，提出基于概率的 hardness 区分 true/false negatives。与 StructFuse difficulty-overfitting 发现呼应。\\\"\\n\\n      - title: \\\"Difficulty-Based Sampling for Debiased Contrastive Representation Learning\\\"\\n        authors: \\\"Taeuk Jang, Xiaoqian Wang\\\"\\n        venue: CVPR\\n        year: 2023\\n        relation: method-component\\n        summary: \\\"WCL: 用 difficulty 分层采样 + bias-amplifying encoder 找信息性 hard negatives 同时避免 false negatives。与 StructFuse difficulty stratification 思路最接近。\\\"\\n\\n      - title: \\\"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion\\\"\\n        authors: \\\"Xingwei He, Yeyun Gong, A-Long Jin, Hang Zhang, Anlei Dong, Jian Jiao, Siu Ming Yiu, Nan Duan\\\"\\n        venue: EMNLP\\n        year: 2023\\n        relation: background\\n        summary: \\\"课程采样策略 + pseudo-query 文档扩展，解决双塔检索训练-推理差异。StructFuse 的 structure-grounded negatives 提供正交的课程形式。\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Contrastive Learning for Code\\n  # ==========================================================================\\n  contrastive_code_learning:\\n    description: \\\"代码领域的对比学习方法，训练时利用代码特性构建正负样本\\\"\\n    papers:\\n\\n      - title: \\\"Contrastive Code Representation Learning\\\"\\n        authors: \\\"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\\\"\\n        venue: EMNLP\\n        year: 2021\\n        relation: background\\n        summary: \\\"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\\\"\\n\\n      - title: \\\"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\\\"\\n        authors: \\\"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\\\"\\n        venue: EMNLP\\n        year: 2022\\n        relation: background\\n        summary: \\\"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\\\"\\n\\n      - title: \\\"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: \\\"ACL (Long Papers)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\\\"\\n\\n      - title: \\\"CoCoSoDa: Effective Contrastive Learning for Code Search\\\"\\n        authors: \\\"Ensheng Shi, Yanlin Wang, Wenchao Gu, Lun Du, Hongyu Zhang, Shi Han, Dongmei Zhang, Hongbin Sun\\\"\\n        venue: ICSE\\n        year: 2023\\n        relation: direct-competitor\\n        summary: \\\"对比代码搜索 + soft data augmentation + momentum-based negative enrichment。在 negative 数量维度与 StructFuse 互补（momentum queue vs. difficulty-aware selection）。\\\"\\n\\n      - title: \\\"SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation\\\"\\n        authors: \\\"Xin Wang, Yasheng Wang, Fei Mi, Pingyi Zhou, Yao Wan, Xiao Liu, Li Li, Hao Wu, Jin Liu, Xin Jiang\\\"\\n        venue: arXiv\\n        year: 2021\\n        relation: background\\n        summary: \\\"语法引导的多模态对比预训练，对齐 code/NL/AST 三模态。通过 identifier prediction 和 AST edge prediction 显式编码句法结构。\\\"\\n\\n      - title: \\\"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning\\\"\\n        authors: \\\"Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, Yang Liu\\\"\\n        venue: ICSE\\n        year: 2023\\n        relation: background\\n        summary: \\\"鲁棒性导向的对比预训练，设计 9 种对抗增强算子（identifier renaming, dead code insertion, operand swapping 等），提升模型对对抗攻击的鲁棒性。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n      - title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\"\\n        authors: \\\"Shahd Seddik, Fatemeh Fard\\\"\\n        venue: arXiv\\n        year: 2026\\n        relation: contrast\\n        summary: \\\"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\\\"\\n\\n      - title: \\\"ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimization\\\"\\n        authors: \\\"Chris Cummins, Zacharias V. Fisches, Tal Ben-Nun, Torsten Hoefler, Michael FP O'Boyle, Hugh Leather\\\"\\n        venue: ICML\\n        year: 2021\\n        relation: background\\n        summary: \\\"语言无关的全程序图表示（control-flow + data-flow + call relations），证明整程序结构表示可学习且有效。StructFuse 使用 inter-procedural data-flow 的概念根基。\\\"\\n\\n      - title: \\\"CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion\\\"\\n        authors: \\\"Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Hantian Ding, Ming Tan, Nihal Jain, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, Bing Xiang\\\"\\n        venue: NeurIPS\\n        year: 2023\\n        relation: background\\n        summary: \\\"多语言 cross-file 代码补全 benchmark，用静态分析确定需 cross-file 依赖的补全目标。验证了跨文件上下文对代码任务的关键性。\\\"\\n\\n  # ==========================================================================\\n  # Category 5: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: \\\"EMNLP (Findings)\\\"\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: building-block\\n        summary: \\\"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n\\n      - title: \\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\"\\n        authors: \\\"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: background\\n        summary: \\\"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\\\"\\n\\n      - title: \\\"RepoFusion: Training Code Models to Understand Your Repository\\\"\\n        authors: \\\"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\\\"\\n\\n      - title: \\\"BM25\\\"\\n        authors: \\\"Stephen Robertson, Hugo Zaragoza\\\"\\n        venue: \\\"Foundations and Trends in Information Retrieval\\\"\\n        year: 2009\\n        relation: baseline\\n        summary: \\\"经典稀疏检索方法，StructFuse 的 baseline 之一。\\\"\\n\\n      - title: \\\"CoSQA: 20,000+ Web Queries for Code Search and Question Answering\\\"\\n        authors: \\\"Junjie Huang, Duyu Tang, Linjun Shou, Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, Nan Duan\\\"\\n        venue: ACL\\n        year: 2021\\n        relation: background\\n        summary: \\\"20,000+ 真实 web 查询与 Python 代码配对的大规模数据集，弥合合成 benchmark 与真实开发者需求的差距。\\\"\\n\\n  # ==========================================================================\\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\\n  # ==========================================================================\\n  graph_guided_inference:\\n    description: \\\"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\\\"\\n    papers:\\n\\n      - title: \\\"LocAgent: Graph-Guided LLM Agents for Code Localization\\\"\\n        authors: \\\"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\\\"\\n        venue: ACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\\\"\\n\\n      - title: \\\"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\\\"\\n        authors: \\\"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\\\"\\n        venue: NAACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\\\"\\n\\n      - title: \\\"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\\\"\\n        authors: \\\"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\\\"\\n\\n      - title: \\\"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\\\"\\n        authors: \\\"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\\\"\\n        venue: ICLR\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\\\"\\n\\n      - title: \\\"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\\\"\\n        authors: \\\"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\\\"\\n        venue: ASE\\n        year: 2024\\n        relation: contrast\\n        summary: \\\"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\\\"\\n\\n      - title: \\\"GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion\\\"\\n        authors: \\\"Xingliang Wang, Baoyi Wang, Chen Zhi, Junxiao Han, Xinkui Zhao, Jianwei Yin, Shuiguang Deng\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"构建 repo/module/function 三层多语义代码图（AST + CFG + DFG + call graph + class hierarchy），用 GNN-based hybrid retriever 做层次化检索增强代码补全。推理时图方法，与 StructFuse 训练时结构信号互补。\\\"\\n\\n  # ==========================================================================\\n  # Category 7: Representation Geometry / Similarity Saturation\\n  # ==========================================================================\\n  representation_geometry:\\n    description: \\\"预训练模型表示空间几何分析及各向异性修正方法\\\"\\n    papers:\\n\\n      - title: \\\"Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere\\\"\\n        authors: \\\"Tongzhou Wang, Phillip Isola\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: method-component\\n        summary: \\\"定义 alignment/uniformity 两个对比学习关键属性，证明对比损失渐近优化两者。StructFuse 分析 embedding space 质量的理论工具。\\\"\\n\\n      - title: \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\"\\n        authors: \\\"Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"揭示预训练 LM embedding 退化为窄锥的现象，StructFuse 观察到的 similarity saturation 可追溯到此。\\\"\\n\\n      - title: \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\"\\n        authors: \\\"Kawin Ethayarajh\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"实证发现 BERT/ELMo/GPT-2 表示占据窄锥（各向异性），StructFuse 使用的 code encoder 继承此问题。\\\"\\n\\n      - title: \\\"On the Sentence Embeddings from Pre-trained Language Models\\\"\\n        authors: \\\"Bohan Li, Hao Zhou, Junxian He, Mingxuan Wang, Yiming Yang, Lei Li\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: method-component\\n        summary: \\\"BERT-flow: 用 normalizing flows 将各向异性句子嵌入变换为各向同性高斯分布。\\\"\\n\\n      - title: \\\"SimCSE: Simple Contrastive Learning of Sentence Embeddings\\\"\\n        authors: \\\"Tianyu Gao, Xingcheng Yao, Danqi Chen\\\"\\n        venue: EMNLP\\n        year: 2021\\n        relation: method-component\\n        summary: \\\"用 dropout 作为最小增强的对比学习，直接证明 contrastive learning 改善 anisotropy。StructFuse 可引用其 uniformity 分析框架。\\\"\\n\\n      - title: \\\"Whitening Sentence Representations for Better Semantics and Faster Retrieval\\\"\\n        authors: \\\"Jianlin Su, Jiarun Cao, Weijie Liu, Yangyiwen Ou\\\"\\n        venue: arXiv\\n        year: 2021\\n        relation: method-component\\n        summary: \\\"白化操作增强句子表示各向同性并降维，与 StructFuse embedding post-processing 讨论相关。\\\"\\n\\n  # ==========================================================================\\n  # Category 8: Infrastructure / Tools\\n  # ==========================================================================\\n  infrastructure:\\n    description: \\\"StructFuse 依赖的核心基础设施和工具\\\"\\n    papers:\\n\\n      - title: \\\"Billion-Scale Similarity Search with GPUs\\\"\\n        authors: \\\"Jeff Johnson, Matthijs Douze, Herve Jegou\\\"\\n        venue: \\\"IEEE Transactions on Big Data\\\"\\n        year: 2021\\n        relation: building-block\\n        summary: \\\"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\\\"\\n\\n      - title: \\\"Tree-sitter: An Incremental Parsing System for Programming Tools\\\"\\n        authors: \\\"Max Brunsfeld et al.\\\"\\n        venue: \\\"Software (Zenodo DOI: 10.5281/zenodo.13375512)\\\"\\n        year: 2018\\n        relation: building-block\\n        summary: \\\"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\\\"\\n        note: \\\"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\\\"\\n\", \"total_chars\": 23891, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0dde18e6-6a95-41be-be58-00baee87b594",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "12c14dd1-d686-4fec-a957-0eaed69d4cc3",
  "sourceToolAssistantUUID": "0dde18e6-6a95-41be-be58-00baee87b594",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T16:04:03.503Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YFG6SEfgUMo86K89SxHLk9`</summary>

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
  "parentUuid": "12c14dd1-d686-4fec-a957-0eaed69d4cc3",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6XmPQ7txBrStEYAbc1z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8c75848-7d8f-4f59-b2e5-97b7e7392b82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JXBZBhapVSBK5x1ahL241P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16589,
      "cache_read_input_tokens": 16640,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16589,
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

_source line 14 · 2026-05-16T16:04:03.525Z_

<details><summary>↩ Tool result · `toolu_01YFG6SEfgUMo86K89SxHLk9`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8c75848-7d8f-4f59-b2e5-97b7e7392b82",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "12672f3f-7965-4dff-9125-2a1a326a23e2",
  "sourceToolAssistantUUID": "c8c75848-7d8f-4f59-b2e5-97b7e7392b82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T16:04:04.455Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01H7guoVdVn99JibdBnPYo9v`</summary>

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
  "parentUuid": "12672f3f-7965-4dff-9125-2a1a326a23e2",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6XmPQ7txBrStEYAbc1z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93e7c0d2-ea86-41ca-8183-2ab7c3fa92ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JXBZBhapVSBK5x1ahL241P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16589,
      "cache_read_input_tokens": 16640,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16589,
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

_source line 16 · 2026-05-16T16:04:04.489Z_

<details><summary>↩ Tool result · `toolu_01H7guoVdVn99JibdBnPYo9v`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/ROADMAP.md\", \"content\": \"# StructFuse — Research Dashboard\\n\\n> 最后更新: 2026-05-16 06:33 UTC | 更新原因: Reviewer 修正：pool=8→pool=50 数据、标注 D061 superseded、补充遗漏风险\\n\\n## 核心方向\\nHard negative mining strategy comparison for contrastive code retrieval: random vs embedding_distance vs dataflow_aware vs BM25, across 3 encoder architectures. Dual-track narrative (D059): A=stratified heterogeneity reveals when mining helps, B=explain why aggregate deltas are small. 详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（post-MVP）+ 审稿进行中\\n- **Qwen (cuda:0)**: 主链完成中，watcher PID 966920 就绪 → 自动触发 s42 supplement (embed+dataflow+bm25)\\n- **StarCoder (cuda:1)**: embedding_s42 之后还有 embed_s43/s44 + dataflow×3。ETA ~May 19-20\\n- **UniXcoder**: 3-strat s42 训练中（PID 149872, step 400+, R@1@200=0.5245）。Registry 待修复为 RUNNING\\n- **BM25 Phase 1**: ✅ 已完成（索引+挖掘）。Phase 2 watcher 就绪\\n- **D062 query split**: Workers 失败两次（rate/context limit），待重派。**阻塞 Claim 2 全部进展**\\n- **写作**: Intro/Method/Related/Conclusion v1 ✅ | Abstract v2 + Experiments v1 修复中\\n\\n## ⚠️ Claim 1 Delta 状况 — Pool=50 数据（D060 确认 pool=8 不可靠）\\n| seed | checkpoint | random R@1 | embed R@1 | Δ |\\n|------|-----------|-----------|-----------|---|\\n| s43 | by_val_loss | 0.3138 | 0.3331 | **+1.93pp** ✓ |\\n| s44 | by_val_loss | 0.3181 | 0.3694 | **+5.13pp** ��� |\\n| s43 | by_R@1 | 0.3829 | 0.3897 | +0.68pp |\\n| s44 | by_R@1 | 0.3181 | 0.3171 | -0.10pp |\\n| s42 | — | — | **缺失** | — |\\n\\n- **by_val_loss 下两 seed 均 embed > random**，信号正面\\n- **Checkpoint 选择标准是核心方法论问题**：D061 (统一 val_loss) 已被 D062 (query split) supersede\\n- **翻盘路径**: D062 实现 → 统一 checkpoint selection → embed_s42 补完 → bootstrap CI\\n\\n## 实验缺口补充计划 (D063, May 16)\\n| Priority | 实验 | 耗时 | 状态 | 触发条件 |\\n|----------|------|------|------|----------|\\n| **P0** | D062 pool=50 re-eval (query split) | 2h | **Worker 失败×2，重派中** | 立即 |\\n| **P0** | RepoBench-R eval (plan_004) | 5h | 就绪 | 立即启动 |\\n| **P0** | Pool sensitivity (plan_019) | 5h | 就绪 | 立即启动 |\\n| **P0** | BM25 Phase 2 训练 (plan_018) | 15h | Watcher 就绪 | Qwen/SC 完成后自动 |\\n| **P0** | 分层分析 (plan_005) | 分析 | 就绪 | D062 pool=50 后 |\\n| **P1** | UniXcoder multi-seed (s43, s44) | 20h | 新增 plan_020 | s42 完成后 |\\n| **P1** | 温度 ablation 缩减 (τ=0.05,0.2 × Qwen) | 15h | 新增 plan_021 | GPU 空闲时 |\\n| **P1** | random_s42 retrain (统一 regime) | 10h | 已派 Agent | — |\\n\\n## 时间预算\\n- **bjb1-42106**: 2× RTX PRO 6000 96GB\\n- **可用**: 9天 × 24h × 2GPU = 432 GPU·h\\n- **已占用**: ~100h (运行中训练)\\n- **新增 must-do**: ~42h | should-do: ~35h\\n- **总计 ~177h，余量充足**\\n\\n## 关键路径\\n```\\nQwen主链完成 → s42 supplement (18h) → BM25 P2 自动触发\\n              ↘ pool=50 re-eval → stratified analysis + bootstrap CI\\nD062 修复 → pool=50 query split 实现 ↗\\nRepoBench-R + Pool sensitivity → 立即并行启动（用已有 checkpoint）\\nUniXcoder s42 完成 → s43/s44 → 跨架构统计\\nStarCoder chain → May 19-20 全部完成\\n```\\n\\n## 近期任务\\n- [ ] **D062 重派 Worker**（已失败两次，阻塞 Claim 2）\\n- [ ] RepoBench-R 立即启动（已有 Qwen s42/s43/s44 checkpoints）\\n- [ ] Pool sensitivity 立即启动\\n- [ ] UniXcoder registry 修复为 RUNNING\\n- [ ] Qwen 主链完成 → 验证 watcher 触发 supplement\\n- [ ] random_s42 retrain（已在 Agent 队列）\\n- [ ] Qwen 全量完成后 → D062 pool=50 + stratified + bootstrap CI\\n- [ ] 温度 ablation 缩减版排期\\n\\n## 覆盖率\\n- Claim 1: pool=50 eval 已跑部分（Qwen 12 ckpt + StarCoder 8 ckpt），但 D062 query split 未实现前数据不能作为最终结论\\n- Claim 2: **0/3 done** — plan_005 blocked on D062。⚠️ 这是 dual-track B 的核心，完全无定量数据\\n- Claim 3: 1/1 done ✅\\n\\n## 关键风险\\n1. **D062 连续失败**: 阻塞 checkpoint selection + Claim 2 stratified analysis + bootstrap CI——整条 post-M2 分析链\\n2. **StarCoder embedding < random (pool=50 确认, -1.9pp)**: Claim 1 跨架构泛化受挑战。Paper 需 qualify 为 encoder-dependent 或靠 UniXcoder 扳回\\n3. **Checkpoint 选择标准矛盾**: val_loss vs pool=8 R@1 给出相反结论，D062 (query split) 是唯一可靠解法\\n4. **Claim 2 覆盖率 0%**: Dual-track narrative B 支柱完全无实验数据，plan_005 + neg_difficulty 分析全部依赖 D062\\n5. **UniXcoder 只有 1 seed**: 无法做统计检验，需补 s43/s44（plan_020）\\n6. **ARR May 25**: 9 天完成所有补充实验 + 论文定稿\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D066 | 2026-05-16 | D066: D062 eval 8/14 失败（adapter format bug），16.3pp | d062_qwen_query_split_eval |\\n| D065 | 2026-05-16 | D065: Checkpoint selection criterion effect (+16.3 | d062_qwen_query_split_eval |\\n| D064 | 2026-05-16 | D064: UniXcoder s42 null result (Δ<0.4pp) 支撑 Track | unixcoder_3strat_s42, plan_020 |\\n| D063 | 2026-05-16 | D063: 实验缺口补充——新增 plan_020 (UniXcoder multi-seed) + | plan_020, plan_021, plan_004, plan_019 |\\n| D062 | 2026-05-16 | D062: Checkpoint 选择采用方案 2——从 2980 val queries 分出 5 | m2_full_qwen_continued, plan_005_stratified |\\n| D061 | 2026-05-16 | D061: pool=50 eval 首批结果——统一用 best_by_val_loss 选 ch | m2_full_qwen_continued, m2_full_starcoder_resumed |\\n| D060 | 2026-05-16 | D060: in-training eval R@1 不可靠（val negative 非确定性 ± | m2_full_qwen_continued, plan_005_stratified |\\n| D059 | 2026-05-15 | 确认 A/B 双轨叙事策略：A=stratified 揭示异质性，B=B1+Claim2 hybri | m2_full_qwen_continued, m2_full_starcoder_resumed, plan_005_stratified |\\n| D058 | 2026-05-15 | D057 trajectory 发现重新定位：从 Claim 2 evidence 降级为 §4.3 | m2_full_qwen_continued |\\n| D057 | 2026-05-15 | embed_s44 展示 R@1/val_loss 指标分歧：R@1 峰值 step 500 而 v | m2_full_qwen_continued |\\n\\n\", \"total_chars\": 4966, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93e7c0d2-ea86-41ca-8183-2ab7c3fa92ae",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "560e6f44-2c20-4315-ab10-b782c77759b8",
  "sourceToolAssistantUUID": "93e7c0d2-ea86-41ca-8183-2ab7c3fa92ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T16:04:04.701Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QK8rrxhsiBnwW5ihstTUH4`</summary>

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
  "parentUuid": "560e6f44-2c20-4315-ab10-b782c77759b8",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6XmPQ7txBrStEYAbc1z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "574dcd7e-0a0a-4f83-b95b-f1fb7c585688",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JXBZBhapVSBK5x1ahL241P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16589,
      "cache_read_input_tokens": 16640,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16589,
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

_source line 18 · 2026-05-16T16:04:04.987Z_

<details><summary>↩ Tool result · `toolu_01QK8rrxhsiBnwW5ihstTUH4`</summary>

```text
Error: result (55,327 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/98678e1d-9307-4b37-b78e-c6727fde8087/tool-results/mcp-agent-ml-research-read_project_file-1778947444984.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/98678e1d-9307-4b37-b78e-c6727fde8087/tool-results/mcp-agent-ml-research-read_project_file-1778947444984.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/98678e1d-9307-4b37-b78e-c6727fde8087/tool-results/mcp-agent-ml-research-read_project_file-1778947444984.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "574dcd7e-0a0a-4f83-b95b-f1fb7c585688",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "5c64681b-692f-4a9f-a137-3a4e68f47dd2",
  "sourceToolAssistantUUID": "574dcd7e-0a0a-4f83-b95b-f1fb7c585688",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-16T16:04:08.098Z_

Let me look at the artifacts directory for the paper draft and any experiment results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c64681b-692f-4a9f-a137-3a4e68f47dd2",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6Xmmp157h5rAZCP78Eq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03c7764e-b97f-49ee-a547-26427ebb98d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dh1iweoZVHwd5426kNGRCA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3847,
      "cache_read_input_tokens": 33229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3847,
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

_source line 20 · 2026-05-16T16:04:09.068Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018KwUbRif9rHkMFt9C1FCdH`</summary>

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
  "parentUuid": "03c7764e-b97f-49ee-a547-26427ebb98d1",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6Xmmp157h5rAZCP78Eq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b9a5ccf-4a24-4196-9aac-366c59c7c7c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dh1iweoZVHwd5426kNGRCA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3847,
      "cache_read_input_tokens": 33229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3847,
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

_source line 21 · 2026-05-16T16:04:09.093Z_

<details><summary>↩ Tool result · `toolu_018KwUbRif9rHkMFt9C1FCdH`</summary>

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
artifacts/_project/paper/checkpoint_criterion_table.tex
artifacts/_project/paper/fixed_checkpoint_table.tex
artifacts/paper_drafts/checkpoint_criterion_table.tex
artifacts/paper_drafts/fixed_checkpoint_table.tex
artifacts/_project/paper/methodology.tex
artifacts/paper_drafts/v2/methodology.tex
artifacts/_project/paper/related_work.tex
artifacts/paper_drafts/v2/related_work.tex
artifacts/_project/paper/introduction.tex
artifacts/paper_drafts/v2/introduction.tex
artifacts/_project/paper/discussion.tex
artifacts/paper_drafts/v2/discussion.tex
artifacts/_project/paper/experiments.tex
artifacts/paper_drafts/v2/experiments.tex
artifacts/dream_reports/dream_20260516T150348/best/paper.tex
artifacts/dream_reports/dream_20260516T150348/median/paper.tex
artifacts/dream_reports/dream_20260516T150348/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b9a5ccf-4a24-4196-9aac-366c59c7c7c4",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "00b44d47-00ac-4a88-b20d-dd5d5b9c3a97",
  "sourceToolAssistantUUID": "6b9a5ccf-4a24-4196-9aac-366c59c7c7c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-16T16:04:09.346Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01AQWH3Kk8tKLf9pUEgnooEj`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00b44d47-00ac-4a88-b20d-dd5d5b9c3a97",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6Xmmp157h5rAZCP78Eq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1e95061-bcaa-4d8d-a065-1898a50dea40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dh1iweoZVHwd5426kNGRCA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3847,
      "cache_read_input_tokens": 33229,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3847
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 33229,
          "cache_creation_input_tokens": 3847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3847,
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

_source line 23 · 2026-05-16T16:04:09.432Z_

<details><summary>↩ Tool result · `toolu_01AQWH3Kk8tKLf9pUEgnooEj`</summary>

```text
artifacts/mvp_p1_codeql_feasibility/report/mvp_phase1_report.md
artifacts/mvp_p2b_contrastive_training/report/failure_diagnosis.md
artifacts/_project/report/50repo_overlap_report.md
artifacts/dream_reports/dream_20260512T204322/best/review_report.md
artifacts/dream_reports/dream_20260512T204322/median/review_report.md
artifacts/dream_reports/dream_20260512T204322/worst/review_report.md
artifacts/disk_cleanup_report_20260513.md
artifacts/_project/report/scalability_summary.md
artifacts/plan_006/scalability_summary.md
artifacts/m1_progress_0513.md
artifacts/bjb1_status_check.md
artifacts/_project/report/pilot_results_summary.md
artifacts/_project/report/pilot_results_summary_64aa24.md
artifacts/rename_safety_report.md
artifacts/plan003_swebench_eval_plan.md
artifacts/plan003_eval_readiness.md
artifacts/training_status_snapshot.md
artifacts/swebench_eval_readiness.md
artifacts/dream_reports/dream_20260514T075732/best/paper_framing.md
artifacts/dream_reports/dream_20260514T075732/median/paper_framing.md
artifacts/dream_reports/dream_20260514T075732/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T075732/best/review_report.md
artifacts/dream_reports/dream_20260514T075732/median/review_report.md
artifacts/dream_reports/dream_20260514T075732/worst/review_report.md
artifacts/analysis/plan017_literature_comparison.md
artifacts/m2_full_qwen_analysis.md
artifacts/m2_full_qwen/report/m2_full_qwen_analysis.md
artifacts/m2_qwen_status_check.md
artifacts/m2_full_starcoder/report/m2_starcoder_status_check.md
artifacts/m2_starcoder_status_check.md
artifacts/status_check_loop6.md
artifacts/_project/report/plan_015_dynamic_mining_design.md
artifacts/dream_reports/dream_20260514T162530/best/paper_framing.md
artifacts/dream_reports/dream_20260514T162530/median/paper_framing.md
artifacts/dream_reports/dream_20260514T162530/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T162530/best/review_report.md
artifacts/dream_reports/dream_20260514T162530/median/review_report.md
artifacts/dream_reports/dream_20260514T162530/worst/review_report.md
artifacts/_project/paper/experimental_setup_k_checkpoint.md
artifacts/status_check_20260514.md
artifacts/paper_drafts/experimental_setup_k_checkpoint.md
artifacts/plan003_swebench_dryrun_report.md
artifacts/plan005_stratified_analysis_report.md
artifacts/plan_005_stratified/report/v1_v2_changelog.md
artifacts/v1_v2_changelog.md
artifacts/m1_reextract_v2_status.md
artifacts/_project/report/related_work_expansion_report.md
artifacts/literature/related_work_expansion_report.md
artifacts/plan_003/report/swebench_dryrun_report.md
artifacts/plan_003/swebench_dryrun_report.md
artifacts/_project/paper/related_work_v1_dc54a3.md
artifacts/_project/paper/introduction_v1.md
artifacts/_project/paper/figure_design_v1.md
artifacts/paper_drafts/figure_design_v1.md
artifacts/_project/paper/experiments_v1_054f8d.md
artifacts/_project/paper/method_v1_3cf111.md
artifacts/_project/paper/method_v1_ce3556.md
artifacts/_project/paper/experiments_v1_eccca0.md
artifacts/_project/paper/experiments_v1_bcd130.md
artifacts/_project/paper/experiments_v1_d4b180.md
artifacts/_project/paper/method_v1_ae4280.md
artifacts/paper_drafts/claim2_wording_review.md
artifacts/paper_drafts/bm25_code_review.md
artifacts/_project/paper/discussion_v2.md
artifacts/_project/paper/related_work_v1.md
artifacts/_project/paper/method_v1.md
artifacts/_project/paper/introduction_v2.md
artifacts/paper_drafts/introduction_v2.md
artifacts/paper_drafts/experiment_setup_v1.md
artifacts/_project/paper/experiment_setup_v1.md
artifacts/checkpoint_criterion_analysis.md
artifacts/_project/report/checkpoint_criterion_analysis.md
artifacts/plan_005/report/plan005_stratification_spec.md
artifacts/plan005_stratification_spec.md
artifacts/paper_drafts/discussion_valloss_divergence.md
artifacts/_project/paper/introduction_v1_c7f173.md
artifacts/paper_drafts/introduction_v1.md
artifacts/_project/paper/method_v1_82f7f1.md
artifacts/_project/paper/related_work_v1_5cf1f6.md
artifacts/paper_drafts/abstract_v1.md
artifacts/_project/paper/conclusion_v1.md
artifacts/paper_drafts/related_work_v1.md
artifacts/paper_drafts/method_v1.md
artifacts/paper_drafts/conclusion_v1.md
artifacts/_project/paper/experiments_v1_1b36e4.md
artifacts/_project/paper/abstract_v2.md
artifacts/_project/paper/abstract_v2_e63490.md
artifacts/paper_drafts/abstract_v2.md
artifacts/plan_006_scalability/paper/experiments_v1.md
artifacts/_project/paper/experiments_v1.md
artifacts/paper_drafts/experiments_v1.md
artifacts/paper_drafts/discussion_v2.md
artifacts/_project/report/training_dynamics_analysis.md
artifacts/analysis/training_dynamics_analysis.md
artifacts/plan_003_swebench_eval/data/swebench_bm25_baseline_300.md
artifacts/_project/report/m2_eval_summary.md
artifacts/m2_eval_summary.md
artifacts/_project/report/related_work_references.md
artifacts/literature/related_work_references.md
artifacts/paper_drafts/related_work_supplement.md
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1e95061-bcaa-4d8d-a065-1898a50dea40",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "921f98b7-f9e5-4e53-b87c-072c34be20c0",
  "sourceToolAssistantUUID": "b1e95061-bcaa-4d8d-a065-1898a50dea40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-16T16:04:13.405Z_

Let me read the latest dream review reports and the actual paper drafts to understand the paper's current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "921f98b7-f9e5-4e53-b87c-072c34be20c0",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6Xn739XqsaQcBovpe7p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7eaad060-c8d7-4ce2-83e8-d3062e1441cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KhGJ2dMgtqRnGkpETWa96U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2485,
      "cache_read_input_tokens": 37076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2485,
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

_source line 25 · 2026-05-16T16:04:14.193Z_

<details open><summary>🔧 Tool call — Read · `toolu_014oR9fTJui54CAL9HvGnHFN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7eaad060-c8d7-4ce2-83e8-d3062e1441cc",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6Xn739XqsaQcBovpe7p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32258290-a463-4b26-9c08-b7a20b36a8ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KhGJ2dMgtqRnGkpETWa96U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2485,
      "cache_read_input_tokens": 37076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2485,
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

### Tool result

_source line 26 · 2026-05-16T16:04:14.197Z_

<details><summary>↩ Tool result · `toolu_014oR9fTJui54CAL9HvGnHFN`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{amsmath}
5	\usepackage{amssymb}
6	\usepackage{booktabs}
7	\usepackage{multirow}
8	\usepackage{graphicx}
9	\usepackage{xcolor}
10	\usepackage{url}
11	\usepackage{natbib}
12	\usepackage{hyperref}
13	
14	\title{What Makes Hard Negatives Work for Code Retrieval?\\A Systematic Study of Mining Strategies, Representation Geometry,\\and Evaluation Methodology}
15	
16	\author{Anonymous}
17	
18	\begin{document}
19	\maketitle
20	
21	\begin{abstract}
22	Hard negative mining is widely used to improve contrastive code retrievers, yet the field lacks systematic understanding of what strategies work, when they work, and how to properly evaluate them. We present a controlled comparison of four negative mining strategies---random, static embedding-distance, dataflow-aware structural, and BM25-based---across two 3B-parameter code encoders (Qwen2.5-Coder-3B and StarCoder2-3B) with distinct representation geometries. Our study yields three contributions: (1) Simple static embedding-distance mining provides a reliable retrieval improvement (+1.4pp Qwen, +0.9pp StarCoder on held-out evaluation; $p < 0.05$, non-overlapping 95\% CIs on RepoBench-R) at zero additional computational cost, empirically refuting claims that non-differentiable embedding negatives are ineffective for code retrieval. (2) We observe that structure-grounded negatives interact with encoder representation geometry---their benefit concentrates in hard-instance strata where embedding mining also excels, suggesting a shared underlying mechanism rather than complementary signal. (3) We discover that checkpoint selection criterion effects ($\Delta$ up to +16.3pp) exceed mining strategy effects ($\sim$1pp) by 7$\times$, revealing that standard evaluation practices systematically mask mining quality differences. We validate findings on RepoBench-R cross-file retrieval with non-overlapping bootstrap confidence intervals and identify a clean scale boundary condition at 125M parameters. Code and data will be released.
23	\end{abstract}
24	
25	\section{Introduction}
26	
27	Repository-level code repair and retrieval require identifying relevant files from large codebases given a natural language query (e.g., a bug report). Contrastive learning is the dominant paradigm for training such retrievers \cite{swerank,swefixer}, where hard negative mining---the selection of informative negative examples during training---is a critical design decision.
28	
29	Despite its importance, the field lacks systematic understanding of negative mining strategies for code retrieval. CoCoHaNeRe \cite{cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based methods. However, their analysis conflates BM25-based lexical negatives with true embedding-distance negatives---a distinction we show is critical.
30	
31	We present a controlled study comparing four mining strategies across two code encoders with distinct representation geometries:
32	\begin{itemize}
33	\item \textbf{Random}: uniform sampling from the candidate pool (baseline).
34	\item \textbf{Embedding-distance}: select negatives nearest to the query in pretrained embedding space (static, computed once).
35	\item \textbf{Dataflow-aware}: select structurally disconnected files (via CodeQL call-graph analysis) ranked by BM25.
36	\item \textbf{BM25}: select lexically similar negatives by BM25 score alone.
37	\end{itemize}
38	
39	Our study yields three contributions:
40	
41	\paragraph{Contribution 1: Embedding mining as reliable zero-cost baseline.} Static embedding-distance mining consistently improves retrieval across both encoders (+1.4pp Qwen, +0.9pp StarCoder on held-out evaluation), with non-overlapping confidence intervals on an external benchmark. This directly contradicts CoCoHaNeRe's claim---we show their negative result stems from using BM25 as a proxy for embedding negatives. True BM25 negatives \emph{harm} performance ($-2.7$pp average), while true embedding negatives help.
42	
43	\paragraph{Contribution 2: Representation geometry interaction.} Dataflow-aware negatives show encoder-dependent effects (Qwen +0.7pp, $p=0.089$; StarCoder $-0.5$pp, n.s.). Stratified analysis reveals that mining benefits concentrate in hard-instance strata (Q4 neg difficulty: +2.3pp vs Q1: +0.6pp), suggesting representation geometry mediates strategy effectiveness.
44	
45	\paragraph{Contribution 3: Evaluation methodology.} We discover that checkpoint selection criterion introduces up to +16.3pp variation---7$\times$ larger than mining strategy effects. Standard evaluation (select and evaluate on the same validation set) systematically masks mining quality differences. We propose query-split evaluation to recover the true signal.
46	
47	\section{Related Work}
48	
49	\paragraph{Code retrieval for repository-level tasks.} SweRank \cite{swerank} and SWE-Fixer \cite{swefixer} train contrastive retrievers on repository-level bug-fix data but rely on random or simple heuristic negative selection. LocAgent \cite{locagent}, RANGER, and CodexGraph use structural information (call graphs, import trees) at inference time but not during training.
50	
51	\paragraph{Hard negative mining.} ANCE \cite{ance} uses asynchronous index updates for dynamic mining. CoCoHaNeRe \cite{cocohanere} (ACM TOSEM 2025) compares gradient-based and non-differentiable mining, concluding embedding negatives are ineffective. We show this conclusion stems from conflating BM25-proxy with true embedding-distance negatives.
52	
53	\paragraph{Structural code analysis.} ARISE uses intra-procedural data-flow analysis. GraphCodeBERT \cite{graphcodebert} incorporates data-flow edges as attention bias. Our approach differs: we use inter-procedural call-graph analysis (via CodeQL) to define structural connectivity for negative \emph{selection}, not inference-time augmentation.
54	
55	\section{Method}
56	
57	\subsection{Problem Setting}
58	
59	Given a repository $\mathcal{R}$ with files $\{f_1, \ldots, f_n\}$ and a query $q$ (bug report), the retrieval task is to rank files by relevance. We train contrastive encoders with InfoNCE loss:
60	\begin{equation}
61	\mathcal{L} = -\log \frac{\exp(\text{sim}(q, f^+)/\tau)}{\exp(\text{sim}(q, f^+)/\tau) + \sum_{i=1}^{K} \exp(\text{sim}(q, f_i^-)/\tau)}
62	\end{equation}
63	where $\tau$ is the temperature, $f^+$ is the gold file, and $\{f_i^-\}_{i=1}^K$ are negatives selected by the mining strategy.
64	
65	\subsection{Mining Strategies}
66	
67	\paragraph{Random.} $f_i^- \sim \text{Uniform}(\mathcal{R} \setminus \{f^+\})$. Zero-cost baseline.
68	
69	\paragraph{Embedding-distance.} $f_i^- = \text{top-}K_{f \in \mathcal{R} \setminus \{f^+\}} \cos(E(q), E(f))$, where $E$ is the pretrained encoder (before fine-tuning). Computed once; no re-mining during training.
70	
71	\paragraph{Dataflow-aware.} Let $G$ be the inter-procedural call graph extracted by CodeQL (2-hop boundary). $f_i^- = \text{top-}K_{\text{BM25}} \{f : f \notin \text{Reachable}_G(q) \wedge f \neq f^+\}$. Negatives are structurally disconnected from the query file and ranked by lexical similarity.
72	
73	\paragraph{BM25.} $f_i^- = \text{top-}K_{\text{BM25}}(\mathcal{R} \setminus \{f^+\})$. Lexically similar negatives without structural filtering.
74	
75	\subsection{CodeQL Structural Extraction}
76	
77	We extract inter-procedural call graphs using CodeQL with 2-hop bounding. The pipeline achieves 90\% coverage (25,582/28,276 instances) after re-extraction with optimized queries, 0\% timeout rate across 123 repositories. The 2-hop boundary is empirically optimal (Section~\ref{sec:ablations}).
78	
79	\subsection{Query-Split Evaluation Protocol}
80	\label{sec:querysplit}
81	
82	Standard contrastive retrieval evaluation selects checkpoints on a validation set and reports performance on the \emph{same} set---creating selection bias. We split 2,980 validation queries into:
83	\begin{itemize}
84	\item \textbf{Selection set} (500 queries): used for checkpoint selection by R@1.
85	\item \textbf{Held-out evaluation set} (2,480 queries): used for final performance reporting.
86	\end{itemize}
87	This decouples checkpoint selection from evaluation and reveals true strategy differences masked by standard practice.
88	
89	\subsection{Training Configuration}
90	
91	We fine-tune with LoRA (rank 16) on SWE-smith training data (5K instances). Temperature $\tau=0.1$ (default), $K=7$ negatives per query. Three random seeds (42, 43, 44) per configuration. Encoders: Qwen2.5-Coder-3B-Instruct and StarCoder2-3B.
92	
93	\section{Experiments}
94	
95	\subsection{Main Results: Standard vs.\ Query-Split Evaluation}
96	\label{sec:main}
97	
98	Table~\ref{tab:main_standard} presents the full 4-strategy comparison under standard evaluation (best checkpoint by R@1 on the full validation set). Embedding mining shows modest improvements (Qwen +0.3pp, StarCoder +0.6pp), while BM25 negatives significantly harm both encoders (Qwen $-3.2$pp, StarCoder $-2.2$pp).
99	
100	\begin{table}[t]
101	\centering
102	\small
103	\caption{4-Strategy comparison under standard evaluation (best\_by\_R@1). Mean over 3 seeds with 95\% CIs.}
104	\label{tab:main_standard}
105	\begin{tabular}{llccc}
106	\toprule
107	Encoder & Strategy & R@1 (\%) & 95\% CI & $\Delta$ (pp) \\
108	\midrule
109	\multirow{4}{*}{Qwen} & BM25 & 53.8 & [52.9, 54.7] & $-3.2$ \\
110	& random & 57.0 & [55.5, 58.5] & --- \\
111	& dataflow & 55.9 & [55.3, 56.5] & $-1.1$ \\
112	& embedding & 57.3 & [56.5, 58.1] & $+0.3$ \\
113	\midrule
114	\multirow{4}{*}{StarCoder} & BM25 & 45.7 & [44.8, 46.6] & $-2.2$ \\
115	& random & 47.9 & [46.0, 49.0] & --- \\
116	& dataflow & 47.2 & [46.5, 47.9] & $-0.7$ \\
117	& embedding & 48.5 & [47.2, 50.1] & $+0.6$ \\
118	\bottomrule
119	\end{tabular}
120	\end{table}
121	
122	However, query-split evaluation (Table~\ref{tab:main_querysplit}) reveals that standard evaluation masks the true effect. On held-out queries, embedding mining improves by +1.4pp (Qwen) and +0.9pp (StarCoder)---3--4$\times$ larger than standard evaluation suggests.
123	
124	\begin{table}[t]
125	\centering
126	\small
127	\caption{4-Strategy comparison under query-split evaluation (D062 held-out set, 2,480 queries). Checkpoint selected by R@1 on 500-query selection set.}
128	\label{tab:main_querysplit}
129	\begin{tabular}{llcc}
130	\toprule
131	Encoder & Strategy & R@1 (\%) & $\Delta$ (pp) \\
132	\midrule
133	\multirow{4}{*}{Qwen} & BM25 & 33.2 & $-2.9$ \\
134	& random & 36.1 & --- \\
135	& dataflow & 36.8 & $+0.7$ \\
136	& embedding & 37.5 & $+1.4$ \\
137	\midrule
138	\multirow{4}{*}{StarCoder} & BM25 & 28.0 & $-2.5$ \\
139	& random & 30.5 & --- \\
140	& dataflow & 30.1 & $-0.4$ \\
141	& embedding & 31.4 & $+0.9$ \\
142	\bottomrule
143	\end{tabular}
144	\end{table}
145	
146	The strategy ordering BM25 $<$ random $<$ dataflow $\leq$ embedding is consistent across both evaluation protocols and both encoders.
147	
148	\subsection{Statistical Significance}
149	\label{sec:stats}
150	
151	Table~\ref{tab:bootstrap} reports paired bootstrap 95\% CIs (10K resamples) on the D062 query-split evaluation. Embedding mining is statistically significant for both encoders ($p < 0.05$, CI excludes zero). BM25 harm is highly significant ($p \leq 0.003$). Dataflow shows a borderline effect for Qwen ($p = 0.089$), consistent with its exploratory framing.
152	
153	\begin{table}[t]
154	\centering
155	\small
156	\caption{Bootstrap 95\% CIs for pairwise comparisons (D062 query-split, 10K resamples).}
157	\label{tab:bootstrap}
158	\begin{tabular}{llccc}
159	\toprule
160	Encoder & Comparison & $\Delta$ (pp) & 95\% CI & $p$ \\
161	\midrule
162	\multirow{3}{*}{Qwen} & embed $-$ random & $+1.4$ & [$+0.5$, $+2.3$] & 0.012 \\
163	& dataflow $-$ random & $+0.7$ & [$-0.2$, $+1.6$] & 0.089 \\
164	& BM25 $-$ random & $-2.9$ & [$-4.1$, $-1.7$] & 0.001 \\
165	\midrule
166	\multirow{3}{*}{StarCoder} & embed $-$ random & $+0.9$ & [$+0.1$, $+1.7$] & 0.038 \\
167	& dataflow $-$ random & $-0.5$ & [$-1.4$, $+0.4$] & 0.210 \\
168	& BM25 $-$ random & $-2.5$ & [$-3.8$, $-1.2$] & 0.003 \\
169	\bottomrule
170	\end{tabular}
171	\end{table}
172	
173	\subsection{Scale Boundary: UniXcoder (125M)}
174	\label{sec:unixcoder}
175	
176	To identify when mining strategies become effective, we evaluate UniXcoder-base (125M parameters, encoder-only) with 3 seeds $\times$ 3 strategies (Table~\ref{tab:unixcoder}). All strategy differences are non-significant (max span 0.37pp, all bootstrap CIs contain zero). This establishes a clean scale boundary: mining strategy effects require models above $\sim$1B parameters to manifest.
177	
178	\begin{table}[t]
179	\centering
180	\small
181	\caption{UniXcoder-base (125M)---scale boundary condition. R@1 (\%) on SWE-smith validation. All pairwise differences non-significant.}
182	\label{tab:unixcoder}
183	\begin{tabular}{lcccc}
184	\toprule
185	Seed & random & embedding & dataflow & Span (pp) \\
186	\midrule
187	42 & 55.34 & 54.97 & 55.10 & 0.37 \\
188	43 & 57.70 & 57.50 & 57.40 & 0.30 \\
189	44 & 56.20 & 56.00 & 56.10 & 0.20 \\
190	\midrule
191	Mean & 56.41 & 56.16 & 56.20 & 0.25 \\
192	\bottomrule
193	\end{tabular}
194	\end{table}
195	
196	\subsection{External Validation: RepoBench-R}
197	\label{sec:repobench}
198	
199	We validate on RepoBench-R \cite{repobench}, a cross-file code completion benchmark independent of our training domain. Table~\ref{tab:repobench} shows results on test\_hard (pool $\approx$ 18 candidates). Embedding mining improves both encoders (Qwen +1.2pp, StarCoder +0.8pp) with non-overlapping 95\% bootstrap CIs. BM25 negatives again harm ($-1.8$ to $-1.9$pp). Strategy ranking is perfectly preserved across benchmarks.
200	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32258290-a463-4b26-9c08-b7a20b36a8ee",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "ac0113f0-0848-41c7-8d84-ee9968caee69",
  "sourceToolAssistantUUID": "32258290-a463-4b26-9c08-b7a20b36a8ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T16:04:14.914Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GzXgALr5cpW4KKPBqztW6d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments.tex",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac0113f0-0848-41c7-8d84-ee9968caee69",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6Xn739XqsaQcBovpe7p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18fc4476-0d12-4a78-9d5a-99e8853f05d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KhGJ2dMgtqRnGkpETWa96U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2485,
      "cache_read_input_tokens": 37076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2485,
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

### Tool result

_source line 28 · 2026-05-16T16:04:14.924Z_

<details><summary>↩ Tool result · `toolu_01GzXgALr5cpW4KKPBqztW6d`</summary>

```text
1	%==============================================================================
2	\section{Experiments}
3	\label{sec:experiments}
4	%==============================================================================
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Dataset.}
10	We construct a code retrieval dataset from SWE-smith~\cite{yang2025swesmith}, a large-scale collection of synthetic Python bug-fix instances derived from real-world GitHub repositories.
11	After excluding repositories with failed clones, 44,173 instances across 123 repositories remain.
12	Our structural extraction pipeline (\S\ref{sec:extraction}) produces inter-procedural data-flow graphs for \placeholder{39,750} instances (\placeholder{90\%}).
13	Per-seed stratified splits produce $\sim$11,300 training and $\sim$3,000 validation instances, preserving repository-level distribution across partitions.
14	A separate query-split evaluation set of \placeholder{504} held-out queries is reserved for the D062 protocol (\S\ref{sec:query-split}).
15	
16	\paragraph{Encoders.}
17	We evaluate three encoders: Qwen2.5-Coder-3B~\cite{hui2024qwen25coder} (decoder-only, saturated geometry), StarCoder2-3B~\cite{lozhkov2024starcoder2} (decoder-only, healthy separation), and UniXcoder-base~\cite{guo2022unixcoder} (125M encoder-only, architecture-scale boundary).
18	Full specifications appear in \S\ref{sec:training}.
19	
20	\paragraph{Training.}
21	All fine-tuning details follow \S\ref{sec:training}: LoRA ($r{=}16$, $\alpha{=}32$) on $W_q/W_v$, InfoNCE with learnable $\tau$, AdamW ($\text{lr}{=}2{\times}10^{-5}$).
22	Seed 42 trains for 3 epochs (overfitting diagnostic); seeds 43--44 use 2 epochs with early stopping (patience 2).
23	We maintain dual checkpoints: $\theta^*_{\text{loss}}$ (best validation loss) and $\theta^*_{\text{R@1}}$ (best validation Recall@1).
24	
25	\paragraph{Evaluation.}
26	We report two evaluation protocols:
27	\begin{itemize}
28	\item \textbf{Pool-50 (training eval):} Standard pool-based retrieval, pool size 50 (1 positive + 49 negatives from same repository). Reported for comparability with prior work.
29	\item \textbf{Query-split (D062 protocol):} Held-out queries evaluated at pool sizes \{50, 200, 500\}. Both $\theta^*_{\text{loss}}$ and $\theta^*_{\text{R@1}}$ checkpoints evaluated per configuration. Primary metric: R@1.
30	\end{itemize}
31	Bootstrap 95\% confidence intervals computed over query-level outcomes.
32	
33	\paragraph{Configurations.}
34	Each encoder $\times$ strategy combination is trained with 3 random seeds (42, 43, 44), yielding:
35	\begin{itemize}
36	\item Qwen: 4 strategies $\times$ 3 seeds = 12 runs
37	\item StarCoder: 4 strategies $\times$ 3 seeds = 12 runs
38	\item UniXcoder: 4 strategies $\times$ 3 seeds = 12 runs (pool=8 for s42; pool=50 for s43--44)
39	\end{itemize}
40	Total: 36 runs. D062 query-split evaluation: \placeholder{14} checkpoint evaluations across strategies and criteria.
41	
42	
43	\subsection{Main Results}
44	\label{sec:results}
45	
46	% ===========================================================
47	% VERSION-DEPENDENT: Lead table and narrative differ
48	% ===========================================================
49	
50	\begin{table*}[t]
51	\centering
52	\caption{Pool-50 training evaluation: R@1 (mean $\pm$ std across 3 seeds) by strategy and encoder. $\theta^*_{\text{R@1}}$ checkpoint.}
53	\label{tab:pool50}
54	\small
55	\begin{tabular}{lcccc}
56	\toprule
57	Strategy & Qwen2.5-Coder-3B & StarCoder2-3B & UniXcoder-base \\
58	\midrule
59	Random           & \placeholder{X.XX $\pm$ X.XX} & \placeholder{X.XX $\pm$ X.XX} & \placeholder{X.XX $\pm$ X.XX} \\
60	Embedding-dist.  & \placeholder{X.XX $\pm$ X.XX} & \placeholder{X.XX $\pm$ X.XX} & \placeholder{X.XX $\pm$ X.XX} \\
61	BM25             & \placeholder{X.XX $\pm$ X.XX} & \placeholder{X.XX $\pm$ X.XX} & \placeholder{X.XX $\pm$ X.XX} \\
62	Dataflow-aware   & \placeholder{X.XX $\pm$ X.XX} & \placeholder{X.XX $\pm$ X.XX} & \placeholder{X.XX $\pm$ X.XX} \\
63	\bottomrule
64	\end{tabular}
65	\end{table*}
66	
67	\begin{table*}[t]
68	\centering
69	\caption{Query-split evaluation (D062 protocol): R@1 by strategy, checkpoint criterion, and pool size. Qwen2.5-Coder-3B, \placeholder{N} seeds.}
70	\label{tab:querysplit}
71	\small
72	\begin{tabular}{llccc}
73	\toprule
74	Strategy & Criterion & Pool-50 & Pool-200 & Pool-500 \\
75	\midrule
76	Random          & $\theta^*_{\text{loss}}$ & \placeholder{XX.X} & \placeholder{XX.X} & \placeholder{XX.X} \\
77	Random          & $\theta^*_{\text{R@1}}$  & \placeholder{XX.X} & \placeholder{XX.X} & \placeholder{XX.X} \\
78	\midrule
79	Embedding-dist. & $\theta^*_{\text{loss}}$ & \placeholder{XX.X} & \placeholder{XX.X} & \placeholder{XX.X} \\
80	Embedding-dist. & $\theta^*_{\text{R@1}}$  & \placeholder{XX.X} & \placeholder{XX.X} & \placeholder{XX.X} \\
81	\midrule
82	Dataflow-aware  & $\theta^*_{\text{loss}}$ & \placeholder{XX.X} & \placeholder{XX.X} & \placeholder{XX.X} \\
83	Dataflow-aware  & $\theta^*_{\text{R@1}}$  & \placeholder{XX.X} & \placeholder{XX.X} & \placeholder{XX.X} \\
84	\bottomrule
85	\end{tabular}
86	\end{table*}
87	
88	\placeholder{[Main results narrative — version-dependent. Version A leads with criterion effect; Version B leads with strategy effect at realistic pool size.]}
89	
90	
91	\subsection{Analysis}
92	\label{sec:analysis}
93	
94	\subsubsection{Checkpoint Selection Criterion}
95	\label{sec:criterion}
96	
97	\begin{figure}[t]
98	\centering
99	\includegraphics[width=\columnwidth]{\placeholder{figures/fig3_criterion_effect.pdf}}
100	\caption{Criterion effect vs.\ strategy effect. The R@1 gap between $\theta^*_{\text{R@1}}$ and $\theta^*_{\text{loss}}$ (criterion effect, \placeholder{+16.3pp}) substantially exceeds the gap between strategies under the same criterion (strategy effect, \placeholder{+X.Xpp}).}
101	\label{fig:criterion-effect}
102	\end{figure}
103	
104	Among \placeholder{6/14} completed query-split evaluations, the criterion effect averages \placeholder{+16.3pp}: selecting checkpoints by validation R@1 rather than validation loss yields dramatically higher retrieval performance on held-out queries.
105	This effect is consistent across strategies, indicating that loss--R@1 divergence (\S\ref{sec:training-dynamics}) is a general property of contrastive fine-tuning rather than a strategy-specific phenomenon.
106	
107	\placeholder{[Full 14/14 statistics after D062 completion. Report: criterion main effect, strategy main effect, interaction, per-encoder breakdown.]}
108	
109	\subsubsection{Pool Size Sensitivity}
110	\label{sec:pool-size}
111	
112	\begin{figure}[t]
113	\centering
114	\includegraphics[width=\columnwidth]{\placeholder{figures/fig5_pool_sensitivity.pdf}}
115	\caption{R@1 vs.\ pool size by strategy ($\theta^*_{\text{R@1}}$ criterion). Strategy differences \placeholder{amplify / compress} at larger pool sizes.}
116	\label{fig:pool-sensitivity}
117	\end{figure}
118	
119	\placeholder{[Pool size analysis. Report R@1 × strategy × pool size {50, 200, 500}. Key question: do strategy differences amplify or compress at realistic pool sizes?]}
120	
121	\subsubsection{Training Dynamics}
122	\label{sec:training-dynamics}
123	
124	We define two metrics to characterize training trajectories:
125	\begin{itemize}
126	\item \textbf{R@1 decay rate} ($\delta_{\text{R@1}}$): per-500-step R@1 drop after peak.
127	\item \textbf{Loss--R@1 divergence}: whether $\theta^*_{\text{loss}}$ and $\theta^*_{\text{R@1}}$ select different steps.
128	\end{itemize}
129	
130	Loss--R@1 divergence occurs in \placeholder{60\%} of completed runs across both strategies, confirming it is a general property of contrastive fine-tuning (\S\ref{sec:criterion}).
131	Post-peak decay differs by strategy: embedding-distance negatives show \placeholder{$-$2.2\%} per 500 steps vs.\ \placeholder{$-$6.2\%} for random (Qwen seed 44 controlled comparison), suggesting harder negatives provide a regularizing effect.
132	
133	\placeholder{[Aggregate statistics across all runs after M2 completion.]}
134	
135	\subsubsection{Negative Difficulty Analysis}
136	\label{sec:neg-difficulty}
137	
138	\begin{figure}[t]
139	\centering
140	\includegraphics[width=\columnwidth]{figures/fig4_rep_geometry.pdf}
141	\caption{Representation geometry across encoders and strategies. (a) Positive-negative margin comparison. (b) Similarity distribution. Qwen's near-saturated space (pos\_sim $=$ 0.986) compresses margins to 0.017--0.074; StarCoder maintains 2.6--4.1$\times$ larger margins.}
142	\label{fig:rep-geometry}
143	\end{figure}
144	
145	Table~\ref{tab:neg-difficulty} reports pretrained embedding space statistics.
146	Both encoders follow the expected difficulty ordering: embedding-distance negatives are hardest (smallest margin), dataflow-aware intermediate, random easiest.
147	Qwen's margin compression is more severe (77\% reduction from random to embedding) than StarCoder's (65\%), consistent with the representation geometry hypothesis (\S\ref{sec:discuss-when}).
148	
149	\begin{table}[t]
150	\centering
151	\caption{Negative difficulty in pretrained embedding space (2048-token context).}
152	\label{tab:neg-difficulty}
153	\small
154	\begin{tabular}{lcccccc}
155	\toprule
156	 & \multicolumn{3}{c}{Qwen2.5-Coder-3B} & \multicolumn{3}{c}{StarCoder2-3B} \\
157	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
158	Strategy & pos\_sim & neg\_sim & margin & pos\_sim & neg\_sim & margin \\
159	\midrule
160	Random          & 0.986 & 0.911 & 0.074 & 0.799 & 0.605 & 0.194 \\
161	Embedding-dist. & 0.986 & 0.969 & 0.017 & 0.808 & 0.741 & 0.067 \\
162	BM25            & \placeholder{X.XX} & \placeholder{X.XX} & \placeholder{X.XX} & \placeholder{X.XX} & \placeholder{X.XX} & \placeholder{X.XX} \\
163	Dataflow-aware  & 0.986 & 0.956 & 0.029 & 0.801 & 0.682 & 0.119 \\
164	\bottomrule
165	\end{tabular}
166	\end{table}
167	
168	\subsubsection{Cross-Encoder Comparison}
169	\label{sec:cross-encoder}
170	
171	\paragraph{Architecture-scale boundary.}
172	UniXcoder-base (125M) shows negligible strategy differentiation (\placeholder{0.37pp} span, seed 42) compared to the 3B encoders.
173	This null result establishes a boundary condition: mining strategy benefits appear contingent on sufficient encoder capacity.
174	
175	\placeholder{[UniXcoder s43/s44 multi-seed confirmation. Report mean ± std. If null persists → boundary confirmed. If effect emerges → pool-size interaction.]}
176	
177	\paragraph{Decoder-only encoder comparison.}
178	\placeholder{[Qwen vs StarCoder strategy rankings. Report whether ordering is consistent across encoders.]}
179	
180	%==============================================================================
181	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18fc4476-0d12-4a78-9d5a-99e8853f05d3",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "835f0f1d-29ae-4269-ba88-d98af20218cb",
  "sourceToolAssistantUUID": "18fc4476-0d12-4a78-9d5a-99e8853f05d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T16:04:16.015Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NY5jJbvFo6uWX5HnrrU39z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/introduction.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "835f0f1d-29ae-4269-ba88-d98af20218cb",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6Xn739XqsaQcBovpe7p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5552752-c78e-4d98-bd9d-b64eb7730d9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KhGJ2dMgtqRnGkpETWa96U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2485,
      "cache_read_input_tokens": 37076,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2485
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 318,
          "cache_read_input_tokens": 37076,
          "cache_creation_input_tokens": 2485,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2485,
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

_source line 30 · 2026-05-16T16:04:16.025Z_

<details><summary>↩ Tool result · `toolu_01NY5jJbvFo6uWX5HnrrU39z`</summary>

```text
1	%==============================================================================
2	\section{Introduction}
3	\label{sec:intro}
4	%==============================================================================
5	
6	% P1: Problem — repo-level file retrieval, importance of negatives
7	Resolving real-world software issues in large repositories requires accurately localizing the relevant source files from hundreds or thousands of candidates~\cite{jimenez2024swebench}.
8	Dense retrieval has emerged as the dominant paradigm for this task, with recent systems employing contrastive learning to train encoders that map issue descriptions and code files into a shared embedding space~\cite{reddy2025swerank,xie2025swefixer}.
9	The quality of these retrievers depends critically on the selection of \emph{negative} examples during training: which non-relevant files the model learns to distinguish from the ground truth.
10	Hard negative mining---selecting challenging negatives that expose the model to confusable examples---has proven essential for training effective dense retrievers in open-domain text retrieval~\cite{karpukhin2020dpr,xiong2021ance,zhan2021star}.
11	Yet for code retrieval, systematic understanding of what mining strategies work and why remains limited.
12	
13	% P2: Prior work contradiction — CoCoHaNeRe says embedding negatives harmful; our question
14	In the code domain, the most relevant prior study is CoCoHaNeRe~\cite{fan2025cocohanere}, which proposes gradient-based hard negative mechanisms for code search and reports that non-differentiable embedding-based negatives are ``slow and ineffective,'' harming retrieval performance.
15	This finding has influenced subsequent work to avoid embedding-based mining for code.
16	However, we observe that CoCoHaNeRe used BM25-based retrieval as a proxy for embedding distance---a critical methodological conflation, as BM25 selects lexically similar negatives that may destroy useful token-overlap signals during contrastive training.
17	This raises a natural question: does \emph{true} embedding-distance mining---using the encoder's own pretrained representations---genuinely fail for code retrieval, or has its potential been obscured by evaluation confounds?
18	
19	% P3: Code structure as unique dimension + evaluation methodology gap
20	We identify two underexplored dimensions in this space.
21	First, code possesses rich structural information---call graphs, data-flow dependencies, inter-procedural taint tracking---absent in natural language text.
22	This structural connectivity can serve as an independent signal for constructing hard negatives: files that are structurally disconnected from the query yet lexically similar provide training examples grounded in program semantics.
23	We operationalize this insight using CodeQL~\cite{avgustinov2016ql} inter-procedural data-flow analysis to compute structural connectivity at repository scale.
24	
25	% P4: Evaluation methodology gap
26	Second, we identify that \emph{evaluation methodology} critically affects measured strategy effectiveness.
27	Standard pool-based evaluation---small fixed pools with random negatives, unclear checkpoint selection criteria---can mask genuine strategy effects or create illusory ones.
28	We find that the choice of checkpoint selection criterion alone (best-by-validation-loss vs.\ best-by-R@1) yields a \placeholder{+16.3pp} R@1 difference, substantially exceeding any strategy effect.
29	When evaluation controls for these confounds via query-split protocols and realistic pool sizes, a clearer picture of strategy effectiveness emerges.
30	
31	% P5: Contributions — VERSION-DEPENDENT
32	% ===========================================================
33	% VERSION A (criterion dominates):
34	% Our systematic comparison of four negative mining strategies---random, BM25,
35	% embedding-distance, and dataflow-aware---across three encoders yields the
36	% following findings:
37	% (1) Checkpoint selection criterion is the dominant factor in contrastive
38	%     retrieval evaluation (+16.3pp), exceeding all strategy effects.
39	% (2) A query-split evaluation protocol reveals effects masked by standard eval.
40	% (3) When evaluation is properly controlled, embedding mining shows marginal
41	%     but consistent benefit.
42	% ===========================================================
43	% VERSION B (mining works + methodology):
44	% Our systematic comparison yields:
45	% (1) Simple static embedding-distance mining improves code retrieval by
46	%     \placeholder{X.Xpp} at realistic pool sizes, an effect masked by
47	%     small-pool evaluation and inappropriate checkpoint selection.
48	% (2) A query-split evaluation protocol with explicit checkpoint criterion
49	%     reporting reveals effects obscured by standard methodology.
50	% (3) Structure-grounded (dataflow) negatives exhibit encoder-dependent
51	%     interaction patterns mediated by representation geometry.
52	% ===========================================================
53	
54	\placeholder{[P5: Version-dependent contribution paragraph. Final version determined after D062 14/14 completion.]}
55	
56	%==============================================================================
57	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5552752-c78e-4d98-bd9d-b64eb7730d9b",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "40c42a75-36ec-4fce-b145-ad32a7fac6d8",
  "sourceToolAssistantUUID": "c5552752-c78e-4d98-bd9d-b64eb7730d9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T16:04:21.101Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AaBuduPEw4DYFub3WttNDv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/paper.tex",
  "offset": 200,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40c42a75-36ec-4fce-b145-ad32a7fac6d8",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6XnbKFV19CDSbNJL9iZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb53b8b3-bd22-45d1-ac75-9f10f7f4181c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWUGvXSVMfVHJa9Y7W6adc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10051,
      "cache_read_input_tokens": 39561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10051,
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

_source line 32 · 2026-05-16T16:04:21.105Z_

<details><summary>↩ Tool result · `toolu_01AaBuduPEw4DYFub3WttNDv`</summary>

```text
200	
201	\begin{table}[t]
202	\centering
203	\small
204	\caption{RepoBench-R test\_hard results (pool $\approx$ 18). 3 seeds, 10K bootstrap CIs.}
205	\label{tab:repobench}
206	\begin{tabular}{llccc}
207	\toprule
208	Encoder & Strategy & R@1 (\%) & 95\% CI & $\Delta$ (pp) \\
209	\midrule
210	\multirow{4}{*}{Qwen} & BM25 & 60.1 & [59.5, 60.7] & $-1.9$ \\
211	& random & 62.0 & [61.5, 62.5] & --- \\
212	& dataflow & 62.6 & [62.0, 63.2] & $+0.6$ \\
213	& embedding & 63.2 & [62.6, 63.8] & $+1.2$ \\
214	\midrule
215	\multirow{4}{*}{StarCoder} & BM25 & 55.3 & [54.7, 55.9] & $-1.8$ \\
216	& random & 57.1 & [56.5, 57.7] & --- \\
217	& dataflow & 56.8 & [56.2, 57.4] & $-0.3$ \\
218	& embedding & 57.9 & [57.3, 58.5] & $+0.8$ \\
219	\bottomrule
220	\end{tabular}
221	\end{table}
222	
223	\subsection{Stratified Analysis}
224	\label{sec:stratified}
225	
226	To understand \emph{when} mining helps most, we stratify by negative difficulty quartile (Table~\ref{tab:stratified_neg}) and structural data availability (Table~\ref{tab:stratified_struct}).
227	
228	\begin{table}[t]
229	\centering
230	\small
231	\caption{Embed$-$random $\Delta$ by negative difficulty quartile (Qwen, D062 query-split). Q4 = hardest instances (smallest retrieval margin).}
232	\label{tab:stratified_neg}
233	\begin{tabular}{lccc}
234	\toprule
235	Quartile & Margin (mean) & emb$-$rand (pp) & df$-$rand (pp) \\
236	\midrule
237	Q1 (easiest) & 0.135 & $+0.6$ & $+0.2$ \\
238	Q2 & 0.072 & $+1.1$ & $+0.5$ \\
239	Q3 & 0.028 & $+1.7$ & $+0.9$ \\
240	Q4 (hardest) & 0.007 & $+2.3$ & $+1.5$ \\
241	\bottomrule
242	\end{tabular}
243	\end{table}
244	
245	The hardest quartile (Q4, margin = 0.007) shows 2.3pp embedding benefit---1.6$\times$ the overall average. This directly validates the theoretical prediction that instances with smaller margins benefit most from harder negatives.
246	
247	\begin{table}[t]
248	\centering
249	\small
250	\caption{Stratified by structural data availability (Qwen, D062 query-split).}
251	\label{tab:stratified_struct}
252	\begin{tabular}{lccc}
253	\toprule
254	Stratum & $N$ & emb$-$rand (pp) & df$-$rand (pp) \\
255	\midrule
256	With dataflow (90\%) & $\sim$13K & $+1.3$ & $+0.8$ \\
257	No dataflow (10\%) & $\sim$1.4K & $+1.4$ & $+0.1$ \\
258	\bottomrule
259	\end{tabular}
260	\end{table}
261	
262	Embedding mining helps regardless of structural data availability (+1.3--1.4pp), while dataflow mining requires actual structural connectivity to provide benefit (+0.8pp with data, +0.1pp without).
263	
264	Pool size and repo size strata show consistent patterns: embedding delta increases from pool$<$20 (+0.7pp) to pool$>$50 (+1.9pp), confirming mining is most valuable in larger search spaces. Small repositories ($<$50 files) show the largest embedding benefit (+2.0pp) as mining quality differences are amplified in concentrated pools.
265	
266	\subsection{Temperature Ablation}
267	\label{sec:temperature}
268	
269	Table~\ref{tab:temperature} shows that strategy ranking is preserved across temperature regimes ($\tau \in \{0.05, 0.1, 0.2\}$). Embedding mining helps at all temperatures (+1.2--1.6pp Qwen, +0.7--1.0pp StarCoder). Lower temperatures amplify the effect modestly, but findings are not regime-specific.
270	
271	\begin{table}[t]
272	\centering
273	\small
274	\caption{Temperature ablation. Strategy ranking preserved across all $\tau$.}
275	\label{tab:temperature}
276	\begin{tabular}{clcccc}
277	\toprule
278	$\tau$ & Encoder & random & embed & dataflow & emb$-$rand \\
279	\midrule
280	\multirow{2}{*}{0.05} & Qwen & 56.0 & 57.6 & 56.8 & $+1.6$ \\
281	& StarCoder & 48.7 & 49.7 & 48.5 & $+1.0$ \\
282	\midrule
283	\multirow{2}{*}{0.10} & Qwen & 55.3 & 56.7 & 55.9 & $+1.4$ \\
284	& StarCoder & 47.9 & 48.5 & 47.4 & $+0.6$ \\
285	\midrule
286	\multirow{2}{*}{0.20} & Qwen & 53.8 & 55.0 & 54.4 & $+1.2$ \\
287	& StarCoder & 46.5 & 47.2 & 46.3 & $+0.7$ \\
288	\bottomrule
289	\end{tabular}
290	\end{table}
291	
292	\subsection{Pool Size Sensitivity}
293	\label{sec:poolsize}
294	
295	To address concerns about evaluation pool size, we re-evaluate at pool sizes 50--500 (Table~\ref{tab:poolsize}). Strategy ranking is 100\% stable across all pool sizes. The embedding delta peaks at pool=100 (+1.4pp) and remains substantial even at pool=500 (+1.0--1.2pp), confirming findings generalize to realistic retrieval settings.
296	
297	\begin{table}[t]
298	\centering
299	\small
300	\caption{Pool size sensitivity (R@1 \%). Strategy ranking stable across all pool sizes.}
301	\label{tab:poolsize}
302	\begin{tabular}{clcccc}
303	\toprule
304	Pool & Encoder & random & embed & emb$-$rand & Rank \\
305	\midrule
306	\multirow{2}{*}{50} & Qwen & 57.0 & 57.3 & $+0.3$ & E$\geq$R \\
307	& StarCoder & 47.9 & 48.5 & $+0.6$ & E$>$R \\
308	\midrule
309	\multirow{2}{*}{100} & Qwen & 43.2 & 44.6 & $+1.4$ & E$>$R \\
310	& StarCoder & 36.5 & 37.7 & $+1.2$ & E$>$R \\
311	\midrule
312	\multirow{2}{*}{200} & Qwen & 34.8 & 36.1 & $+1.3$ & E$>$R \\
313	& StarCoder & 29.0 & 30.1 & $+1.1$ & E$>$R \\
314	\midrule
315	\multirow{2}{*}{500} & Qwen & 26.5 & 27.7 & $+1.2$ & E$>$R \\
316	& StarCoder & 22.2 & 23.2 & $+1.0$ & E$>$R \\
317	\bottomrule
318	\end{tabular}
319	\end{table}
320	
321	\subsection{Checkpoint Selection Criterion Effect}
322	\label{sec:criterion}
323	
324	Our most surprising finding: the choice of checkpoint selection criterion (val\_loss vs.\ R@1) introduces variation far exceeding mining strategy effects. Table~\ref{tab:criterion} shows results on the D062 held-out evaluation set. Seed 43 exhibits a +16.3pp gap between criteria---the val\_loss-optimal checkpoint (step 500, early training) has good generalization but weak ranking, while the R@1-optimal checkpoint (step 1500) has strong ranking that generalizes to held-out queries.
325	
326	\begin{table}[t]
327	\centering
328	\small
329	\caption{Checkpoint criterion effect (Qwen, D062 query-split held-out eval). ``by val\_loss'' and ``by R@1'' select different checkpoints; gap measures their performance difference on held-out queries.}
330	\label{tab:criterion}
331	\begin{tabular}{llccc}
332	\toprule
333	Strategy & Seed & by val\_loss & by R@1 & Gap (pp) \\
334	\midrule
335	\multirow{3}{*}{random} & 42 & 0.230 & 0.230 & 0.0 \\
336	& 43 & 0.341 & 0.504 & $+16.3$ \\
337	& 44 & 0.350 & 0.385 & $+3.5$ \\
338	\midrule
339	\multirow{3}{*}{embedding} & 42 & 0.245 & 0.265 & $+2.0$ \\
340	& 43 & 0.365 & 0.518 & $+15.3$ \\
341	& 44 & 0.370 & 0.395 & $+2.5$ \\
342	\midrule
343	dataflow & 43 & 0.355 & 0.510 & $+15.5$ \\
344	\bottomrule
345	\end{tabular}
346	\end{table}
347	
348	Summary statistics: max criterion effect = +16.3pp, mean = +8.5pp, while mean mining strategy effect = +1.2pp. The criterion-to-mining ratio is \textbf{7.1$\times$}. This effect replicates across both encoders (StarCoder max = +13.5pp) and across strategies. We conclude that the community's inability to detect mining quality differences may partly stem from evaluation methodology noise rather than absent effects.
349	
350	\subsection{Ablation Studies}
351	\label{sec:ablations}
352	
353	\paragraph{Call-graph hop depth (Table~\ref{tab:hop}).} We compare 1/2/3-hop call-graph bounding for dataflow negatives. An inverted-U pattern emerges: 2-hop is optimal (R@1 = 55.8\%), as 1-hop coverage is too sparse (15.2\%) and 3-hop over-constrains the disconnection criterion.
354	
355	\begin{table}[t]
356	\centering
357	\small
358	\caption{Hop depth ablation (Qwen, dataflow strategy).}
359	\label{tab:hop}
360	\begin{tabular}{lcccc}
361	\toprule
362	Hops & Coverage (\%) & Neg/query & R@1 (\%) & $\Delta$ vs 2-hop \\
363	\midrule
364	1 & 15.2 & 21.4 & 54.8 & $-1.0$ \\
365	2 & 45.8 & 38.6 & 55.8 & --- \\
366	3 & 72.1 & 55.3 & 55.3 & $-0.5$ \\
367	\bottomrule
368	\end{tabular}
369	\end{table}
370	
371	\paragraph{Training data size scaling (Table~\ref{tab:scaling}).} Strategy ranking is stable from 1K to 5K instances. The embedding delta grows with data size (0.9pp $\to$ 1.4pp), indicating the effect is not a small-data artifact and has not reached diminishing returns.
372	
373	\begin{table}[t]
374	\centering
375	\small
376	\caption{Data size scaling (Qwen). Ranking stable; delta grows.}
377	\label{tab:scaling}
378	\begin{tabular}{lcccc}
379	\toprule
380	Size & random & embed & emb$-$rand (pp) & $\sigma$ (pp) \\
381	\midrule
382	1K & 51.5 & 52.4 & $+0.9$ & 1.8 \\
383	3K & 54.0 & 55.2 & $+1.2$ & 1.2 \\
384	5K & 55.3 & 56.7 & $+1.4$ & 0.9 \\
385	\bottomrule
386	\end{tabular}
387	\end{table}
388	
389	\paragraph{Fusion head ablation (Table~\ref{tab:fusion}).} We compare training-time mining (embedding-only) vs.\ inference-time structural feature injection (combined fusion). Mining alone outperforms combined fusion (Qwen: 56.7 vs 56.4), and structural-features-only is far inferior ($-6.6$pp). The core value lies in mining strategy, not feature engineering.
390	
391	\begin{table}[t]
392	\centering
393	\small
394	\caption{Fusion head ablation. Mining $\gg$ inference-time features.}
395	\label{tab:fusion}
396	\begin{tabular}{lcc}
397	\toprule
398	Configuration & Qwen R@1 (\%) & StarCoder R@1 (\%) \\
399	\midrule
400	embedding-only (ours) & 56.7 & 48.5 \\
401	structural-features-only & 50.1 & 42.2 \\
402	combined fusion & 56.4 & 48.3 \\
403	\bottomrule
404	\end{tabular}
405	\end{table}
406	
407	\paragraph{Weighted vs.\ binary negatives.} Distance-weighted dataflow sampling ($+0.1$--$0.2$pp, n.s.) does not justify added complexity. Binary connected/disconnected distinction captures the key structural signal.
408	
409	\paragraph{Static vs.\ dynamic mining.} Re-mining negatives each epoch with the current encoder ($+0.1$--$0.2$pp, n.s.) provides no benefit over static one-time mining. This confirms the ``mine once from pretrained, no re-mining needed'' recommendation and rules out curriculum confounds.
410	
411	\subsection{Failure Analysis}
412	
413	We analyze 50 retrieval failures from SWE-smith validation (Table~\ref{tab:failure}). The dominant failure mode is ``similar but wrong file'' (38\%)---the retriever selects a lexically similar file that shares variable/function names but is not in the correct call chain. Embedding mining addresses 17/19 such cases by training the encoder to distinguish within high-similarity clusters.
414	
415	\begin{table}[t]
416	\centering
417	\small
418	\caption{Failure category breakdown (50 cases from SWE-smith validation).}
419	\label{tab:failure}
420	\begin{tabular}{lccc}
421	\toprule
422	Category & Count & \% & Mining helps? \\
423	\midrule
424	Similar but wrong file & 19 & 38 & 17/19 (embed) \\
425	Distant correct file & 12 & 24 & 8/12 (dataflow) \\
426	Pool saturation & 9 & 18 & 2/9 (partial) \\
427	Query ambiguity & 6 & 12 & 0/6 \\
428	Singleton gold & 4 & 8 & 0/4 \\
429	\bottomrule
430	\end{tabular}
431	\end{table}
432	
433	The 34\% embedding help rate is consistent with the observed $\sim$1--1.4pp overall improvement: if a third of failures in a specific mode are correctable, the aggregate effect is modest but reliable.
434	
435	\section{Discussion}
436	
437	\paragraph{Why BM25 negatives harm.} BM25 selects files sharing lexical overlap (function names, imports, variable patterns) with the query. These cues are \emph{useful signals} for code retrieval---training the encoder to ignore them degrades performance. The BM25-vs-embedding Jaccard overlap is only 0.297 in large repos, confirming the two strategies select fundamentally different negatives.
438	
439	\paragraph{Implications for CoCoHaNeRe.} Our BM25 result ($-2.7$pp average harm) directly explains CoCoHaNeRe's reported ``embedding negatives harm'' finding. Their pipeline used BM25 as a proxy for embedding negatives; we show true embedding-distance negatives have the opposite effect (+0.9--1.4pp). The field's negative perception of non-differentiable mining may stem from this proxy conflation.
440	
441	\paragraph{Evaluation methodology recommendations.} The 7:1 criterion-to-mining ratio suggests that mining strategy comparisons in prior work may be unreliable unless checkpoint selection and evaluation are properly decoupled. We recommend: (1) use query-split evaluation, (2) select checkpoints by retrieval metric (not loss), (3) report both criteria as sensitivity analysis.
442	
443	\section{Limitations}
444	
445	\paragraph{Out-of-distribution generalization.} Our retrievers fail catastrophically on SWE-bench Lite (R@1 = 0.04 vs.\ BM25 = 0.273), a cross-repository setting where the model encounters unseen repositories. Contrastive fine-tuning on intra-repository data overfits to repository-specific patterns and loses the pretrained encoder's cross-repository generalization. Our results apply to intra-repository retrieval settings; bridging the intra/cross-repository gap is critical future work.
446	
447	\paragraph{Encoder diversity.} We study two 3B decoder-only encoders. While the scale boundary at 125M (UniXcoder null result) partially validates the model-size dimension, additional architectures (encoder-only at $>$1B, mixture-of-experts) remain untested.
448	
449	\paragraph{Effect sizes.} Absolute improvements of 0.9--1.4pp are modest. However, these are (a) statistically significant with non-overlapping CIs, (b) consistent across two benchmarks and two encoders, (c) achievable at zero additional compute cost, and (d) likely underestimates given that standard evaluation masks the true effect (Section~\ref{sec:criterion}).
450	
451	\section{Conclusion}
452	
453	We present a systematic study of hard negative mining strategies for contrastive code retrieval, yielding three contributions. First, simple static embedding-distance mining provides a reliable, zero-cost improvement (+1.4pp Qwen, +0.9pp StarCoder) that empirically refutes claims of non-differentiable mining's ineffectiveness---the prior negative result stemmed from conflating BM25 negatives (which harm, $-2.7$pp) with true embedding negatives. Second, stratified analysis reveals that mining benefits concentrate in hard-instance strata, with representation geometry mediating effectiveness. Third, we discover that checkpoint selection criterion effects (up to +16.3pp) exceed mining strategy effects by 7$\times$, revealing a previously unrecognized evaluation methodology confound. These findings suggest the community may have underestimated mining strategy effects due to evaluation methodology limitations rather than absence of real effects.
454	
455	\bibliographystyle{plainnat}
456	\begin{thebibliography}{10}
457	
458	\bibitem[Yang et~al.(2025)]{swerank}
459	Yang, J. et~al. (2025).
460	\newblock SweRank: Contrastive retrieval for repository-level code repair.
461	\newblock \emph{arXiv preprint}.
462	
463	\bibitem[Xie et~al.(2025)]{swefixer}
464	Xie, Z. et~al. (2025).
465	\newblock SWE-Fixer: Training open-source LLMs for effective and efficient GitHub issue resolution.
466	\newblock \emph{arXiv preprint}.
467	
468	\bibitem[Su et~al.(2025)]{cocohanere}
469	Su, H. et~al. (2025).
470	\newblock CoCoHaNeRe: Comparing hard negative mining techniques for code search.
471	\newblock \emph{ACM TOSEM}.
472	
473	\bibitem[Xiong et~al.(2021)]{ance}
474	Xiong, L. et~al. (2021).
475	\newblock Approximate nearest neighbor negative contrastive learning for dense text retrieval.
476	\newblock \emph{ICLR}.
477	
478	\bibitem[Guo et~al.(2021)]{graphcodebert}
479	Guo, D. et~al. (2021).
480	\newblock GraphCodeBERT: Pre-training code representations with data flow.
481	\newblock \emph{ICLR}.
482	
483	\bibitem[Liu et~al.(2023)]{repobench}
484	Liu, T. et~al. (2023).
485	\newblock RepoBench: Benchmarking repository-level code auto-completion systems.
486	\newblock \emph{ICLR}.
487	
488	\bibitem[Ma et~al.(2024)]{locagent}
489	Ma, K. et~al. (2024).
490	\newblock LocAgent: Graph-guided LLM agents for code localization.
491	\newblock \emph{arXiv preprint}.
492	
493	\end{thebibliography}
494	
495	\end{document}
496	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb53b8b3-bd22-45d1-ac75-9f10f7f4181c",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "51cef679-9f2f-4b89-b1b0-3d4138ab50d8",
  "sourceToolAssistantUUID": "fb53b8b3-bd22-45d1-ac75-9f10f7f4181c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T16:04:22.059Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KNYD9zUybmZrZTypPR2xgc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51cef679-9f2f-4b89-b1b0-3d4138ab50d8",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6XnbKFV19CDSbNJL9iZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19e37d0a-ea0d-4e2a-942b-dc3f4d61928c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWUGvXSVMfVHJa9Y7W6adc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10051,
      "cache_read_input_tokens": 39561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10051,
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

_source line 34 · 2026-05-16T16:04:22.064Z_

<details><summary>↩ Tool result · `toolu_01KNYD9zUybmZrZTypPR2xgc`</summary>

```text
1	%==============================================================================
2	\section{Related Work}
3	\label{sec:related}
4	%==============================================================================
5	
6	\subsection{Dense Retrieval for Code}
7	\label{sec:related-retrieval}
8	
9	Code retrieval has evolved from sparse lexical methods such as BM25~\cite{robertson2009bm25} to dense neural approaches.
10	Early pretrained code models---CodeBERT~\cite{feng2020codebert}, UniXcoder~\cite{guo2022unixcoder}, and InferCode~\cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap.
11	More recent large-scale code models, including StarCoder2~\cite{lozhkov2024starcoder2} and Qwen2.5-Coder~\cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens.
12	In the retrieval domain, CodeSage~\cite{zhang2024codesage} and SCodeR~\cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search.
13	
14	The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench~\cite{jimenez2024swebench}---has motivated specialized systems: SweRank~\cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer~\cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline.
15	Our work builds on this foundation by systematically comparing negative mining strategies for contrastive code retrieval, demonstrating that both mining strategy \emph{and} evaluation methodology meaningfully affect measured retrieval quality.
16	
17	\subsection{Contrastive Learning and Hard Negative Mining}
18	\label{sec:related-mining}
19	
20	Sentence-BERT~\cite{reimers2019sentencebert} established contrastive fine-tuning of pretrained encoders for dense text retrieval.
21	In open-domain text retrieval, DPR~\cite{karpukhin2020dpr} established BM25-retrieved passages as hard negatives.
22	ANCE~\cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA~\cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation.
23	STAR~\cite{zhan2021star} uses the retriever's own top-ranked passages as training negatives.
24	Curriculum-based approaches---CL-DRD~\cite{zeng2022cldrd} and CAPSTONE~\cite{he2023capstone}---schedule negative difficulty progressively during training.
25	
26	In the code domain, ContraCode~\cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations.
27	CodeRetriever~\cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives.
28	GraphCodeBERT~\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks.
29	CoCoHaNeRe~\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search, arguing that non-differentiable embedding-based negatives are ``slow and ineffective.''
30	However, their evaluation uses BM25-based retrieval as a proxy for embedding distance---a methodological conflation we disentangle by evaluating true embedding-distance mining and BM25 mining as separate strategies.
31	
32	\subsection{Evaluation Methodology for Dense Retrieval}
33	\label{sec:related-eval}
34	
35	The reliability of dense retrieval evaluation depends on choices that are often treated as implementation details rather than studied systematically.
36	
37	\paragraph{Checkpoint selection.}
38	Contrastive fine-tuning optimizes a surrogate loss (InfoNCE) that does not directly correspond to the downstream retrieval metric (Recall@$k$).
39	Prior work in NLP has documented loss--metric misalignment: validation loss can continue improving after task performance degrades~\cite{dodge2020finetuning} [VERIFY].
40	In dense retrieval specifically, Thakur et al.\ note that BEIR benchmark rankings are sensitive to checkpoint selection~\cite{thakur2021beir} [VERIFY], yet most papers report only a single ``best'' checkpoint without specifying the selection criterion.
41	We quantify this effect for code retrieval, finding that the choice between best-by-loss and best-by-R@1 checkpoints yields a \placeholder{+16.3pp} difference---larger than any strategy effect we measure.
42	
43	\paragraph{Evaluation pool size.}
44	Standard contrastive training evaluations use small fixed pools (often 50--100 candidates) where most negatives are trivially distinguishable.
45	BEIR~\cite{thakur2021beir} and MTEB~\cite{muennighoff2023mteb} [VERIFY] evaluate at corpus scale, but per-paper ablation studies typically use smaller pools for computational tractability.
46	The gap between small-pool and corpus-scale evaluation is well-documented in information retrieval~\cite{craswell2020overview} [VERIFY]: strategy differences that appear at small pool sizes may not transfer to realistic retrieval scenarios.
47	We evaluate at multiple pool sizes (\{50, 200, 500\}) to characterize this interaction.
48	
49	\paragraph{Query overlap.}
50	When evaluation queries overlap with training queries (differing only in the negative pool composition), performance reflects memorization of query-specific patterns rather than generalizable retrieval ability.
51	Query-split evaluation---holding out queries not seen during training---is standard in open-domain QA~\cite{karpukhin2020dpr} but is not consistently applied in code retrieval evaluations that use pool-based metrics.
52	We adopt a strict query-split protocol to ensure measured improvements reflect genuine retrieval generalization.
53	
54	\subsection{Code Structure in Machine Learning}
55	\label{sec:related-structure}
56	
57	Program dependence graphs~\cite{ferrante1987pdg} and code property graphs~\cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL~\cite{avgustinov2016ql} make inter-procedural analysis accessible at scale.
58	In machine learning, code2vec~\cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML~\cite{cummins2021programl} demonstrated that whole-program graph representations are learnable and effective for compiler optimization tasks.
59	
60	Recent inference-time graph methods bring structural reasoning to LLM-based software engineering.
61	CodexGraph~\cite{liu2025codexgraph} materializes code property graphs for LLM agent navigation; RepoGraph~\cite{ouyang2025repograph} provides line-level code graph navigation; LocAgent~\cite{chen2025locagent} and RANGER~\cite{shah2025ranger} employ multi-hop graph reasoning for fault localization and retrieval.
62	GraphCoder~\cite{liu2024graphcoder} and ARISE~\cite{seddik2026arise} incorporate data-flow edges but remain limited to intra-procedural scope.
63	GRACE~\cite{wang2025grace} constructs multi-level code graphs spanning repository, module, and function granularity for hierarchical retrieval-augmented completion.
64	
65	These methods leverage structural graphs at \emph{inference time}, incurring per-query latency proportional to graph complexity.
66	Our work operates in a complementary regime: we use inter-procedural data-flow graphs at \emph{training time} to construct hard negatives, with zero inference overhead.
67	A model trained with our approach can serve as an efficient first-stage retriever for inference-time graph systems.
68	
69	%==============================================================================
70	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19e37d0a-ea0d-4e2a-942b-dc3f4d61928c",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "d8ea7847-e5fe-4d05-8757-70b876fe6a4e",
  "sourceToolAssistantUUID": "19e37d0a-ea0d-4e2a-942b-dc3f4d61928c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T16:04:22.475Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RbcRfzuyK7BgqBScGMcH6V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8ea7847-e5fe-4d05-8757-70b876fe6a4e",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6XnbKFV19CDSbNJL9iZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80c4aaa4-7cf7-49fd-bece-72ca8e987c18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWUGvXSVMfVHJa9Y7W6adc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10051,
      "cache_read_input_tokens": 39561,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10051
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 280,
          "cache_read_input_tokens": 39561,
          "cache_creation_input_tokens": 10051,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10051,
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

_source line 36 · 2026-05-16T16:04:22.482Z_

<details><summary>↩ Tool result · `toolu_01RbcRfzuyK7BgqBScGMcH6V`</summary>

```text
1	%==============================================================================
2	\section{Discussion}
3	\label{sec:discussion}
4	%==============================================================================
5	
6	\subsection{Relationship to Inference-Time Graph Methods}
7	\label{sec:discuss-inference}
8	
9	A growing body of work leverages code structure graphs at inference time to improve LLM-based software engineering.
10	CodexGraph~\cite{liu2025codexgraph} materializes a code property graph in a Neo4j database that LLM agents query via Cypher; RepoGraph~\cite{ouyang2025repograph} provides line-level code graph navigation as a plug-in for SE agents; LocAgent~\cite{chen2025locagent} and RANGER~\cite{shah2025ranger} employ graph-guided multi-hop reasoning and MCTS-based traversal for fault localization and retrieval.
11	GraphCoder~\cite{liu2024graphcoder} and ARISE~\cite{seddik2026arise} incorporate data-flow edges but remain limited to intra-procedural scope.
12	
13	We highlight two axes along which our work occupies a distinct position.
14	First, \textbf{when structural information enters the pipeline}: inference-time methods construct and query graphs per request, incurring latency proportional to graph complexity.
15	Our approach amortizes all graph computation to training time (CodeQL extraction costs $\sim$8.9 seconds per instance, $\sim$110 CPU-hours for 44K instances), after which the trained encoder operates at standard embedding-lookup speed with zero graph overhead.
16	Second, \textbf{depth of data-flow analysis}: most inference-time methods use structural relations limited to call graphs and import dependencies, whereas we leverage CodeQL's bounded inter-procedural taint tracking (2-hop call-graph scope), capturing cross-function data-flow paths.
17	
18	The two paradigms are complementary: a model trained with structure-grounded negatives can serve as a first-stage retriever whose embeddings already encode data-flow semantics, reducing the search space for inference-time graph agents that perform targeted reranking.
19	
20	\subsection{When Does Mining Strategy Matter?}
21	\label{sec:discuss-when}
22	
23	Our results suggest that mining strategy effectiveness is not universal but depends on encoder properties and evaluation conditions.
24	
25	\paragraph{Architecture-scale boundary condition.}
26	UniXcoder-base (125M, encoder-only) exhibits negligible strategy differentiation: all four strategies produce R@1 within \placeholder{0.4pp} of each other.
27	This contrasts with the 3B decoder-only encoders, where strategy effects are measurable.
28	We interpret this as a capacity threshold: smaller encoders may lack the representational flexibility to exploit the additional signal in harder negatives.
29	The boundary between ``mining-sensitive'' and ``mining-insensitive'' encoders likely depends on both parameter count and pretraining quality, but our data (\placeholder{$n{=}3$} encoders) is insufficient to characterize the threshold precisely.
30	
31	\paragraph{Representation geometry hypothesis.}
32	Among the 3B encoders, Qwen2.5-Coder-3B (positive-pair cosine similarity 0.986) and StarCoder2-3B (0.798) respond differently to mining strategies.
33	Negative difficulty margin analysis shows that Qwen's near-saturated embedding space leaves minimal room for discrimination (random margin = 0.074), while StarCoder maintains 2.6$\times$ larger margins.
34	We offer this as a candidate heuristic---encoders with pos\_sim $>$ 0.98 may benefit most from the hardest available negatives---while noting that $n{=}2$ encoders at the same scale provides suggestive evidence, not a general law.
35	
36	\subsection{Evaluation Methodology Implications}
37	\label{sec:discuss-eval}
38	
39	Our finding that checkpoint selection criterion yields a \placeholder{+16.3pp} R@1 difference---exceeding all strategy effects---has practical implications for the community.
40	
41	\paragraph{Reporting recommendations.}
42	We recommend that contrastive retrieval papers explicitly report: (1) the checkpoint selection criterion used, (2) results under both best-by-loss and best-by-metric checkpoints as a minimum transparency standard, and (3) evaluation at multiple pool sizes to characterize the generalization of observed effects.
43	The dual-checkpoint protocol we adopt (reporting $\theta^*_{\text{R@1}}$ as primary with $\theta^*_{\text{loss}}$ as robustness check) provides a concrete template.
44	
45	\paragraph{Reinterpreting prior findings.}
46	The magnitude of the criterion effect raises questions about prior work that reports negative mining results without specifying checkpoint selection.
47	If prior studies selected checkpoints by validation loss---a reasonable default from the language modeling tradition---they may have systematically underestimated the benefit of harder negatives, which tend to produce loss--R@1 divergence more frequently (as observed in our training dynamics analysis, \S\ref{sec:training-dynamics}).
48	
49	\subsection{Limitations}
50	\label{sec:limitations}
51	
52	\paragraph{Encoder diversity.}
53	We evaluate three encoders spanning two architectures (encoder-only, decoder-only) and two scales (125M, 3B).
54	This is sufficient for initial observations about architecture-scale boundaries, but insufficient for characterizing general thresholds.
55	Encoder-only models at 3B scale and decoder-only models at 125M remain untested, confounding architecture with scale.
56	
57	\paragraph{Single benchmark.}
58	All training and primary evaluation uses SWE-smith-derived data from Python repositories.
59	Cross-benchmark validation (e.g., RepoBench-R) is planned but not yet complete.
60	The generalization of our findings to other languages, domains, or retrieval benchmarks is uncertain.
61	
62	\paragraph{Static mining.}
63	All negative mining is performed once before training and remains fixed throughout.
64	Dynamic re-mining~\cite{xiong2021ance}---where negatives are refreshed using the current encoder's embeddings---could yield progressively harder negatives as the model improves.
65	We do not evaluate this variant and acknowledge the static-vs-dynamic confound as a limitation.
66	
67	\paragraph{Structural extraction coverage.}
68	CodeQL extraction achieves \placeholder{90\%} structural data rate post-reextraction; the remaining \placeholder{10\%} falls back to beniget (AST-level) or embedding-distance negatives.
69	While high, this means a fraction of dataflow-aware training instances use degraded structural signal.
70	
71	\paragraph{No gradient-based comparison.}
72	We compare static mining strategies but do not implement gradient-based methods (e.g., CoCoHaNeRe's differentiable mechanism).
73	Our claim is that static embedding mining provides a reliable baseline, not that it matches or exceeds gradient-based approaches.
74	
75	\subsection{Future Work}
76	\label{sec:future}
77	
78	\paragraph{Hybrid retrieval pipelines.}
79	Integrating a structure-trained encoder as the first-stage retriever within inference-time graph systems could combine embedding efficiency with runtime graph precision.
80	
81	\paragraph{Representation-guided strategy selection.}
82	Our pos\_sim threshold observation, if validated across more encoders, could enable automated strategy selection without exhaustive ablation: compute representation geometry statistics on a calibration set, then select the appropriate mining strategy.
83	
84	\paragraph{Dynamic and multi-lingual extension.}
85	Adapting the pipeline to dynamically re-mine negatives during training, and extending CodeQL queries beyond Python, would address two current limitations.
86	
87	%==============================================================================
88	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80c4aaa4-7cf7-49fd-bece-72ca8e987c18",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "d7a31f59-a933-408d-ba2f-ac453b484cec",
  "sourceToolAssistantUUID": "80c4aaa4-7cf7-49fd-bece-72ca8e987c18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-16T16:04:25.780Z_

Now let me read the latest dream review reports for prior review context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7a31f59-a933-408d-ba2f-ac453b484cec",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6Xo51PZa5SG9gCn1bkp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46a65c3d-fc48-4c95-981c-a4a03f2298db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CknXoXnrrUPr4d6Nj9xs81",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10249,
      "cache_read_input_tokens": 49612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10249,
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

_source line 38 · 2026-05-16T16:04:28.139Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KWQWzaZuKoChwZ7dowppfc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46a65c3d-fc48-4c95-981c-a4a03f2298db",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6Xo51PZa5SG9gCn1bkp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94fe57cc-ca8e-40c4-8a84-3a6c6beea735",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CknXoXnrrUPr4d6Nj9xs81",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10249,
      "cache_read_input_tokens": 49612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10249,
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

_source line 39 · 2026-05-16T16:04:28.153Z_

<details><summary>↩ Tool result · reported error · `toolu_01KWQWzaZuKoChwZ7dowppfc`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94fe57cc-ca8e-40c4-8a84-3a6c6beea735",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "c706f56f-c8f8-4355-b29a-ade0c846e8b9",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context.",
  "sourceToolAssistantUUID": "94fe57cc-ca8e-40c4-8a84-3a6c6beea735",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T16:04:28.626Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GxFqogeq2CmCwNJB4iDRPV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c706f56f-c8f8-4355-b29a-ade0c846e8b9",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6Xo51PZa5SG9gCn1bkp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80bd67d5-1375-4b68-8ca9-5df1d61e930a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CknXoXnrrUPr4d6Nj9xs81",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10249,
      "cache_read_input_tokens": 49612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10249,
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

_source line 41 · 2026-05-16T16:04:28.631Z_

<details><summary>↩ Tool result · `toolu_01GxFqogeq2CmCwNJB4iDRPV`</summary>

```text
1	---
2	dream_id: dream_20260514T162530
3	tier: best
4	overall_score: 4/6 Weak Accept
5	timestamp: 2026-05-14T17:10:52.369829+00:00
6	---
7	
8	---
9	dream_id: dream_20260514T162530
10	tier: best
11	reviewer: R1 (Methods and Experiments)
12	overall_score: 4/6 Weak Accept
13	timestamp: 2026-05-14
14	---
15	
16	# R1 Review: Methods and Experiments
17	
18	**Paper**: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
19	
20	---
21	
22	## 1. Summary
23	
24	This paper presents a systematic empirical comparison of four hard negative mining strategies (random, BM25, embedding-distance, dataflow-disconnected) for contrastive code retrieval, evaluated across two 3B-parameter decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with 9 random seeds each. The central findings are: (1) true embedding-distance mining consistently improves R@1 over random (+2.0pp Qwen, +1.5pp StarCoder), correcting a prior finding from CoCoHaNeRe that conflated BM25-proxy negatives with embedding-distance negatives; (2) BM25 negatives harm both encoders, empirically confirming the artifact; (3) dataflow-disconnected negatives provide conditional benefit on Qwen but not StarCoder, with a representation saturation hypothesis offered as explanation. The paper includes an extensive ablation suite (temperature, pool size, data scaling, hop depth, dynamic vs. static mining, fusion head, weighted vs. binary dataflow) and evaluates on SWE-smith validation, RepoBench-R, and SWE-bench Lite.
25	
26	---
27	
28	## 2. Strengths
29	
30	- **S1: Exemplary statistical discipline.** 54 training runs (2 encoders x 3 strategies x 9 seeds) with bootstrap 95% CIs and explicit p-values for all main comparisons is substantially above community standard. The paired bootstrap design for SWE-bench Lite (10K resamples) is appropriate for the binary outcome variable.
31	
32	- **S2: Comprehensive and purposeful ablation suite.** Each of the 8 ablations addresses a specific methodological concern or potential confound: temperature regime-specificity (Table 8), pool size artifact (Table 12), static vs. dynamic mining curriculum confound (Table 13), hop depth selection (Table 9), data scaling (Table 10), fusion head isolation (Table 11), weighted vs. binary dataflow (Table 14). This is not ablation padding -- each result answers a genuine question. The dynamic mining ablation is particularly valuable: ruling out the curriculum effect (+0.3pp, non-significant) justifies the practical recommendation to mine once from the pretrained checkpoint.
33	
34	- **S3: Clean experimental control.** The comparison holds all variables constant (data, encoder, LoRA configuration, training schedule, evaluation protocol) except the negative selection strategy. This is the correct experimental design for isolating a single factor's effect.
35	
36	- **S4: BM25 baseline closes the CoCoHaNeRe correction empirically.** Including BM25 negatives as a fourth strategy (Table 1) transforms the "correction" from an argumentative claim into an empirical demonstration. The 4-strategy ordering BM25 < random < dataflow <= embedding, with BM25 harming both encoders (-2.5pp Qwen, -2.7pp StarCoder), is the paper's most clean-cut contribution.
37	
38	- **S5: Honest conditional framing.** The paper does not overclaim dataflow benefit as universal. The conditional framing (helps Qwen, not StarCoder; helps when representations are saturated) and the stratified decomposition (true per-instance effect +2.8pp on the 34% with structural data, diluted to +1.0pp overall) demonstrate intellectual honesty. Many papers would suppress the StarCoder null or report only the pooled +1.0pp.
39	
40	- **S6: Multi-benchmark consistency.** Embedding mining improves both encoders on both SWE-smith and RepoBench-R. The encoder-strategy interaction (dataflow helps Qwen, neutral on StarCoder) replicates across benchmarks. This cross-benchmark stability rules out benchmark-specific artifacts.
41	
42	- **S7: Pool size sensitivity analysis is thorough.** Testing at pool sizes 50, 100, 200, and 500 with 100% ranking stability and graceful delta degradation (-0.15pp per doubling) demonstrates the findings are not artifacts of unrealistically small pools. Embedding mining maintains +1.5pp at pool=500 for Qwen.
43	
44	- **S8: SWE-bench Lite evaluation connects retrieval to downstream impact.** The +2.5pp embedding (p=0.018) and +3.2pp dataflow (p=0.008) resolve rate improvements, with bootstrap CIs excluding zero, add practical credibility beyond retrieval-only metrics.
45	
46	---
47	
48	## 3. Weaknesses
49	
50	### Major
51	
52	- **W1: N=2 encoders is fundamentally insufficient for the "representation saturation mediates strategy effectiveness" claim.** The mechanistic story -- that pos_sim saturation (0.986 Qwen vs. 0.799 StarCoder) determines whether dataflow negatives help -- rests on exactly two data points. These two encoders differ in pretraining data, pretraining objective (fill-in-the-middle vs. fill-in-the-middle with different ratios), tokenizer, and model family. Any of these confounds could explain the observed interaction. The paper correctly frames Claim 2 as conditional ("when encoder representations are saturated"), but the Discussion section (Section 6) presents the saturation mechanism as explanatory rather than merely correlational. With n=2, any post-hoc explanation fits. The neg_difficulty quartile analysis (Table 7b) is descriptive evidence for the saturation hypothesis but is computed on the same two encoders, not an independent validation. This is the paper's most fundamental limitation and limits the mechanistic claim to hypothesis-generating status.
53	
54	- **W2: The dataflow strategy is a mixture strategy, not a pure structural signal.** Dataflow negatives are available for only 34% of instances; the remaining 66% fall back to embedding-distance or random selection. The headline comparison in Table 1 (dataflow vs. random) therefore compares "34% structural + 66% fallback" against "100% random." The stratified analysis (Table 6) decomposes this correctly (+2.8pp on structural-available, +0.1pp on fallback), but this decomposition should be the primary presentation, not a secondary analysis. More critically, the fallback strategy for the 66% is not clearly specified -- is it embedding-distance mining or random? If the former, the "dataflow" condition actually contains a substantial embedding-distance component, making the dataflow-vs-embedding comparison in Table 1 confounded: they share 66% of the same negatives.
55	
56	- **W3: SWE-bench Lite's statistical power is marginal for the reported claims.** With 300 instances, the bootstrap CIs are ~3.6pp wide. The embedding-vs-random comparison (p=0.018) is significant but borderline; the dataflow-vs-embedding comparison (p=0.134) is not. The paper acknowledges this but then reports Table 3 (SWE-bench complexity breakdown) with sub-group analyses (N=189 single-file, N=111 multi-file) that have even less power. The multi-file dataflow advantage (+5.4pp) is presented as evidence for the dataflow mechanism, but with N=111 and no reported CI or p-value for this sub-group, this is anecdotal evidence dressed up as statistical analysis. The paper should either report CIs for each sub-group or refrain from drawing sub-group conclusions.
57	
58	- **W4: Effect sizes are small enough that uncontrolled implementation details could explain them.** The headline embedding-vs-random delta is +2.0pp (Qwen) and +1.5pp (StarCoder). These are within the range affected by hyperparameter choices not ablated: number of negatives per query (K, which is never specified in the paper), sequence length truncation, learning rate, weight decay, LoRA target modules. The data scaling ablation (Table 10) shows embedding delta growing from +1.2pp (1K) to +2.0pp (5K) -- the delta at 1K (+1.2pp) is comparable to the seed standard deviation (sigma=1.5), meaning individual seed outcomes at 1K would not be significant. The 5K result is more convincing, but the fact that the delta is still growing suggests we are observing the beginning of a trend, not its convergent value. This creates uncertainty about whether the finding is robust or still regime-dependent on data scale.
59	
60	- **W5: Checkpoint selection criterion is not specified.** The internal project history (D017) reveals that strategy rankings change depending on whether checkpoints are selected by best validation loss or best R@1. Specifically, for Qwen: by val_loss, embedding > dataflow > random; by peak R@1, dataflow > embedding > random. This is a material design choice that affects the headline claims, yet the paper does not state which criterion is used. If val_loss-selected checkpoints are reported (as seems likely from the main results ordering), the paper should acknowledge that R@1-selected checkpoints would produce different rankings and discuss why val_loss selection is preferred.
61	
62	### Minor
63	
64	- **W6: The paper claims "strategy rankings never reverse across any experimental condition tested" (Conclusion).** This is an overstatement. Table 12 shows StarCoder dataflow ranking changes from E>R>D (pool=50) to E>R~D (pool=200+). While this is not a reversal of the embedding-vs-random ordering, it represents instability in the dataflow ranking. The claim should be narrowed to "embedding > random never reverses."
65	
66	- **W7: Number of negatives per query (K) is not stated.** Section 3.1 defines the loss with K negatives but never specifies the value used. The review_context mentions pool_size=50 at training time, but it is unclear whether K=49 (all non-positive files in the pool) or some smaller K. This is a basic reproducibility gap.
67	
68	- **W8: BM25-embedding overlap of 87%.** The memory.md notes reveal that BM25 and embedding-distance negatives overlap by 87.1%. This high overlap means the BM25 harm (-2.5pp) cannot be cleanly attributed to "BM25 selects lexically similar files that destroy useful token-overlap signals" (as the paper argues). If 87% of negatives are identical, the 13% difference in negative composition is driving a 4.5pp R@1 difference, which implies those 13% of negatives have outsized influence. This deserves investigation and reporting: what characterizes the non-overlapping 13%? Are they high-lexical-overlap but low-embedding-similarity files?
69	
70	- **W9: Overfitting patterns are not reported.** Project logs show train_loss dropping to 0.04 while val_loss remains at 0.52, with best checkpoint at step 1000 out of ~4200 steps (epoch 1 midpoint). This severe overfitting (best at 25% of training) is never discussed. Strategy-specific overfitting dynamics could be informative: does dataflow overfit faster (fewer unique negatives due to 34% coverage)? Does embedding overfit slower (higher negative diversity)?
71	
72	- **W10: The paper name "StructFuse" implies a fusion architecture, but the best-performing approach uses no fusion.** Table 11 shows fusion slightly degrades performance (-0.4pp). The name is misleading for an analysis paper whose main recommendation is "use embedding-distance mining."
73	
74	- **W11: RepoBench-R pool sizes are imprecise.** "Pool ~18" and "pool ~6" are stated but the exact evaluation protocol is not described. Are these the natural candidate sets from RepoBench-R, or are they constructed to match the SWE-smith protocol?
75	
76	---
77	
78	## 4. Questions for Authors
79	
80	1. **Checkpoint criterion:** Which checkpoint selection criterion (best-val-loss vs. best-R@1) is used for all main results? Given that D017 shows these criteria produce different strategy rankings, please report results under both criteria or justify the chosen one.
81	
82	2. **Number of negatives K:** What value of K (negatives per query) is used in training? How does varying K interact with the mining strategy comparison?
83	
84	3. **Dataflow fallback strategy:** For the 66% of instances without structural data, does the dataflow condition fall back to embedding-distance mining or random sampling? If embedding-distance, then the dataflow-vs-embedding comparison in Table 1 is confounded by shared negatives on 66% of instances.
85	
86	4. **BM25-embedding overlap:** Given the 87.1% overlap between BM25 and embedding negatives reported in your analysis, how do you explain the 4.5pp performance gap? What characterizes the 13% of non-overlapping negatives that apparently drive this difference?
87	
88	5. **Learned temperature values:** The training configuration includes a learnable log_temperature parameter. Do the converged temperature values differ systematically across strategies? If so, the temperature ablation (Table 8, which fixes initial temperature) does not fully control for this confound.
89	
90	6. **Positive weighting confound:** Does the dataflow strategy use a different positive weighting scheme (e.g., pos_weight = exp(-alpha * dataflow_distance)) compared to random and embedding strategies? If so, Table 1 conflates two treatment differences (negative selection + positive weighting).
91	
92	7. **Overfitting dynamics:** Best checkpoints occur at step 1000 (~25% through training). Do different strategies exhibit different overfitting speeds? Is the strategy ranking stable across checkpoints (e.g., at step 500, 1000, 1500, 2000)?
93	
94	8. **CoCoHaNeRe evidence:** What specific textual or code-level evidence from CoCoHaNeRe supports the claim that they used BM25 as a proxy for embedding-distance? The strength of Claim 1 depends on the precision of this attribution.
95	
96	---
97	
98	## 5. Minor Issues
99	
100	- Table 10 (data scaling): Sigma is reported as a single number per data size, but it should be reported per strategy. If sigma is pooled across strategies, it obscures whether mining quality reduces seed variance (which would be informative).
101	- Table 9 (hop depth ablation): Single seed, Qwen only. The optimal hop depth could differ for StarCoder. At minimum, note this limitation.
102	- Table 11 (fusion head ablation): No CIs or p-values. Given the small deltas (-0.4pp, -6.7pp), statistical significance should be reported.
103	- The SWE-bench Lite evaluation uses only the Qwen retriever, not StarCoder. This asymmetry should be acknowledged in the Limitations section.
104	- The failure analysis (Table 15) is based on 50 instances from the random retriever only. A matched analysis comparing failure modes across strategies (which instances does dataflow rescue that embedding does not?) would be more informative.
105	- Section 3.3: "0% timeout rate" for CodeQL is stated for 5K instances / 131 repos. Clarify whether this refers to individual query timeout or total repo processing timeout.
106	- The abstract states "+2.0pp R@1 Qwen, +1.5pp StarCoder" for embedding mining, but Table 1 in the body shows these exact numbers. The abstract should reference CIs or state "statistically significant" to distinguish from noise.
107	
108	---
109	
110	## 6. Overall Assessment
111	
112	**Score: 4/6 (Weak Accept)**
113	
114	**Confidence: 4/5 (High)**
115	
116	This paper asks a genuinely important question -- what makes hard negatives work for code retrieval -- and answers it with above-average experimental rigor. The 54-run statistical design with bootstrap CIs, the 4-strategy comparison that empirically closes the CoCoHaNeRe BM25-proxy debate, the multi-benchmark consistency, and the extensive ablation suite represent careful, honest empirical work. The CoCoHaNeRe correction (Claim 1) is the paper's strongest and most useful contribution: the BM25 < random < embedding ordering, validated across two encoders and two benchmarks, is a service to the community.
117	
118	However, several issues prevent confident acceptance:
119	
120	(a) The mechanistic claim about representation saturation (Claim 2) is hypothesis-generating at best with n=2 encoders. The paper should explicitly reframe this as an observation with a testable prediction, not a validated mechanism.
121	
122	(b) The dataflow strategy's 34% coverage makes it a mixture condition whose headline effect (+1.0pp) is diluted. The stratified decomposition (+2.8pp on structural-available instances) is more honest but raises the question of practical utility: if 66% of instances receive no structural signal, the practical recommendation simplifies to "use embedding mining."
123	
124	(c) Effect sizes throughout are small (1.0-2.0pp R@1) and within the range sensitive to uncontrolled implementation details (number of negatives K, checkpoint selection criterion, learnable temperature).
125	
126	(d) Several reporting gaps -- unspecified K, unspecified checkpoint criterion, unreported overfitting dynamics, unreported learned temperatures -- create unnecessary uncertainty about the robustness of the headline numbers.
127	
128	The paper is above-average in execution quality and intellectual honesty, but the combination of small effect sizes, limited encoder diversity (n=2), and unresolved confounds places it at the accept/reject boundary. Addressing items (a) through (d) in revision -- particularly the checkpoint criterion transparency, the K specification, and explicit reframing of Claim 2 as hypothesis -- would likely push this to a 5/6.
129	
130	**What would change my score:**
131	- To 5/6: Specify checkpoint criterion and K; report results under both checkpoint criteria; explicitly reframe Claim 2 as hypothesis; add CIs to sub-group analyses.
132	- To 3/6: If the learned temperature values differ systematically across strategies (explaining the R@1 deltas as a temperature artifact rather than a mining quality effect) or if the positive weighting confound is confirmed.
133	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80bd67d5-1375-4b68-8ca9-5df1d61e930a",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "84316f9b-8da0-40bc-b256-ab0eb4ff922b",
  "sourceToolAssistantUUID": "80bd67d5-1375-4b68-8ca9-5df1d61e930a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-16T16:04:37.442Z_

Now let me check the previous dream review reports to see R2's prior reviews and any other reviewer perspectives on novelty.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84316f9b-8da0-40bc-b256-ab0eb4ff922b",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6XoXmDaCRtJzYh7x7Uj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33e81faa-2eed-462a-b1fe-7d5dbe93cd58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5SpFWjMA9pp5jXCyEKKbt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5028,
      "cache_read_input_tokens": 59861,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5028,
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

_source line 43 · 2026-05-16T16:04:39.439Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HFSAJaZkCQJHbMXA1s32AE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33e81faa-2eed-462a-b1fe-7d5dbe93cd58",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6XoXmDaCRtJzYh7x7Uj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25d61532-d00f-404f-91db-1b7eeaed8d15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5SpFWjMA9pp5jXCyEKKbt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5028,
      "cache_read_input_tokens": 59861,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5028,
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

_source line 44 · 2026-05-16T16:04:39.456Z_

<details><summary>↩ Tool result · `toolu_01HFSAJaZkCQJHbMXA1s32AE`</summary>

```text
1	---
2	dream_id: dream_20260514T162530
3	tier: median
4	overall_score: 3/6 Weak Reject
5	timestamp: 2026-05-14T17:14:10.921742+00:00
6	---
7	
8	# Dream Review Report — Consolidated Roundtable
9	
10	**Paper:** "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
11	
12	**Reviewers:** R1 (Methods & Experiments), R2 (Novelty & Related Work)
13	**Initial scores:** R1 = 4/6 (Weak Accept), R2 = 3/6 (Weak Reject)
14	**Converged score: 3/6 (Weak Reject)**
15	**Confidence: 4/5**
16	
17	---
18	
19	## Roundtable Process
20	
21	### Step 1: Independent Reviews
22	
23	**R1 (Methods & Experiments) — 4/6:**
24	Praised the statistical discipline (54 training runs across strategy × encoder × seed, bootstrap CIs, multi-benchmark evaluation) and found the ablation suite unusually comprehensive for an analysis paper. Identified the BM25 vs. embedding separation as the paper's strongest contribution. Main concerns: n=2 encoders insufficient for the representation saturation mechanism, dataflow is a mixture strategy (34% structural + 66% random fallback), SWE-bench underpowered, effect sizes (1–2pp) small enough that uncontrolled implementation details could explain them, and checkpoint selection criterion unspecified.
25	
26	**R2 (Novelty & Related Work) — 3/6:**
27	Acknowledged the honest framing and ablation breadth but found fundamental deficiencies. The core recommendation ("use embedding-distance mining") recapitulates ANCE (2021) applied to code—not a novel contribution. The CoCoHaNeRe correction argument lacks evidentiary foundation (no proof CoCoHaNeRe actually used BM25 as proxy, p > 0.05, magnitude gap from −1.9pp to −27pp unexplained). The bibliography contains only 2 citations, critically insufficient for a "systematic study" paper. The dataflow contribution is dead weight (null result). Effect sizes at realistic pool sizes (200+) shrink to +0.2–0.5pp, within noise.
28	
29	### Step 2: Cross-Sharing — Points of Agreement
30	
31	Both reviewers converged on the following assessments:
32	
33	1. **The paper's intellectual honesty is commendable.** Claims are properly hedged, limitations are transparent, and the "analysis paper" positioning is appropriate for the evidence.
34	
35	2. **The ablation suite is unusually thorough.** Temperature, pool size, data scaling, hop count, static/dynamic, weighted/binary, and fusion head ablations each address a specific methodological question.
36	
37	3. **The stratified analysis by negative difficulty quartile is the paper's strongest analytical finding.** The monotonic Q1→Q4 pattern (embedding Δ from +0.3pp to +1.6pp) provides a plausible representation-geometry explanation.
38	
39	4. **n=2 encoders cannot support the representation geometry mechanism.** Both reviewers flagged that attributing the encoder–strategy interaction to pos_sim saturation from two data points is post-hoc and unfalsifiable.
40	
41	5. **The dataflow contribution is essentially null** across conditions and does not justify its inclusion as a named contribution.
42	
43	6. **Effect sizes are too small for practical impact** at realistic pool sizes.
44	
45	### Step 3: Convergence Discussion
46	
47	**R1 adjusted downward** after considering R2's bibliography and novelty critiques. R1 acknowledged that:
48	- The 2-citation bibliography is a serious scholarly deficiency that undermines the paper's positioning as a systematic study. Multiple methods are mentioned by name (SweRank, SWE-Fixer, GraphCodeBERT, CodexGraph, LocAgent, RANGER, ARISE, CoCoHaNeRe) without proper citations.
49	- The core recommendation is indeed ANCE applied to code, reducing the novelty of the main finding.
50	- The CoCoHaNeRe correction narrative requires concrete evidence of proxy conflation to be credible.
51	
52	**R2 adjusted slightly** after considering R1's statistical rigor analysis:
53	- The 54-run experimental matrix with bootstrap CIs represents above-average execution quality.
54	- The pool-size sensitivity analysis with 100% ranking stability on Qwen across pool=50–500 provides useful external validity.
55	
56	**Final convergence: 3/6 (Weak Reject).** The execution quality is good, but the contribution does not meet the bar for a top venue. The combination of minimal novelty, marginal effect sizes, statistically unsupported correction narrative, and inadequate bibliography is not addressable through minor revision.
57	
58	---
59	
60	## Consolidated Assessment
61	
62	### Strengths
63	
64	- **S1: Exemplary statistical practice.** 54 training runs (4 strategies × 2 encoders × 3 seeds + ablations), bootstrap CIs on all comparisons, power analysis for SWE-bench. This level of rigor is rare in code retrieval papers and sets a good methodological example.
65	
66	- **S2: Comprehensive ablation suite with clear purpose.** Each of 8 ablations answers a specific question (Is the finding temperature-dependent? Does it scale with data? Is dynamic re-mining worth the cost?). Results are reported even when null, avoiding publication bias.
67	
68	- **S3: Honest framing and claim calibration.** The paper does not overclaim. "Tends to help," "exploratory observation," and "directional support" are appropriate qualifications. The SWE-bench evaluation is correctly labeled as a sanity check. Limitations are thorough and specific.
69	
70	- **S4: Stratified analysis provides mechanistic insight.** The negative difficulty quartile decomposition (Q1: +0.3pp → Q4: +1.6pp for embedding) and structural availability stratification (34% with dataflow data vs. 66% fallback) provide the clearest explanations for when and why mining strategies differ.
71	
72	- **S5: Conceptual separation of BM25-proxy from true embedding mining.** Even without statistical significance, making this distinction explicit is a useful contribution to clarity in the field.
73	
74	### Weaknesses
75	
76	- **W1 (Major): Insufficient novelty.** The universal recommendation ("use embedding-distance mining") recapitulates ANCE (Xiong et al., 2021). The code-specific application does not constitute a novel methodological insight. The dataflow strategy, which would have been the novel element, is a null result. Analysis papers at top venues need to deliver substantial new understanding—this paper's core insight ("hard negatives help more when they're harder") is well-established in contrastive learning.
77	
78	- **W2 (Major): CoCoHaNeRe correction argument lacks foundation.** Three critical gaps: (a) BM25 harm is not statistically significant (p=0.12, p=0.18), (b) the magnitude gap between our −1.9pp and CoCoHaNeRe's −27pp is unexplained beyond vague "different protocol/pool size" hand-waving, and (c) no concrete evidence that CoCoHaNeRe actually used BM25 as a proxy for embedding-distance negatives. Without (c), the entire "proxy conflation" hypothesis is speculative.
79	
80	- **W3 (Major): Effect sizes at noise floor for practical relevance.** At pool=50 (training-time setup): +1.0pp Qwen, +0.7pp StarCoder. At pool=200 (realistic): +0.7pp Qwen, +0.4pp StarCoder. At pool=500: +0.5pp Qwen, +0.2pp StarCoder. SWE-bench downstream: < 1pp, p > 0.6. The practical takeaway is "negative mining strategy probably doesn't matter much," which is useful to know but thin as a publication contribution.
81	
82	- **W4 (Major): Bibliography critically insufficient.** Only 2 references cited. Missing: RocketQA, TAS-B, GPL, ColBERTv2 (hard negative mining for dense retrieval); ContraCode, contrastive learning for source code; formal citations for SweRank, SWE-Fixer, GraphCodeBERT, CodexGraph, LocAgent, RANGER, ARISE, CoCoHaNeRe. A "systematic study" paper cannot have a 2-entry bibliography.
83	
84	- **W5 (Major): n=2 encoders insufficient for mechanism claims.** The "representation saturation" hypothesis (Qwen pos_sim=0.99 benefits from structural negatives; StarCoder pos_sim=0.80 does not) is inferred from two data points. Any two encoders differ in multiple dimensions; attributing the interaction to pos_sim is unfalsifiable without more encoders.
85	
86	- **W6 (Significant): Dataflow contribution is dead weight.** Neutral on Qwen (+0.2pp overall, CI includes 0), negative on StarCoder (−0.6pp). Only 34% structural coverage; 66% falls back to random. Hop-count ablation < 0.5pp. Weighted-vs-binary ablation not significant. Including this as Contribution 4 dilutes the paper's focus without adding value.
87	
88	- **W7 (Significant): Dataflow is a confounded mixture strategy.** The "dataflow" condition is actually 34% structural + 66% random. The headline comparison in Table 1 mixes signal from two different strategies. A cleaner design would report the 34% stratum separately as the primary dataflow result.
89	
90	- **W8 (Moderate): 3 seeds with df=2 severely underpowers statistical tests.** With 3 seeds, t-test critical values are 4.303, making significance detection near-impossible for the observed deltas. Bootstrap with n=3 yields only 27 resamples. The paper should be explicit about this limitation.
91	
92	- **W9 (Moderate): Checkpoint selection unspecified.** The paper evaluates at steps {200, 500, 1000, 1500, 2000} and selects "best checkpoint" but does not specify the selection criterion or whether it could change strategy rankings.
93	
94	### Questions for Authors
95	
96	1. Can you provide specific evidence (CoCoHaNeRe code, methodology description, or author communication) that they used BM25 as a proxy for embedding-distance negatives? Without this, the "proxy conflation" hypothesis is speculative.
97	
98	2. What is the checkpoint selection criterion, and does it favor one strategy over another?
99	
100	3. At pool=500 on StarCoder, dataflow slightly exceeds embedding (0.197 vs. 0.196). Is this within noise? How robust is the "embedding mining maintains advantage" claim at realistic pool sizes?
101	
102	4. Have you evaluated a dataflow variant that falls back to embedding-distance (instead of random) for the 66% without structural data? This would isolate the structural signal more cleanly.
103	
104	5. What are the pos_sim values (query-positive cosine similarity) for each encoder? This is central to the representation geometry explanation but not reported.
105	
106	6. Why does the bibliography contain only 2 entries? Is this a formatting artifact? All methods mentioned by name (SweRank, SWE-Fixer, GraphCodeBERT, CodexGraph, LocAgent, RANGER, ARISE, CoCoHaNeRe, curriculum-based approaches) should be formally cited.
107	
108	7. The paper reports BM25 uses only 1 seed (vs. 3 for other strategies). What is the justification? How does this affect the BM25 CI widths?
109	
110	### Missing Experiments or Comparisons
111	
112	1. **More encoders** (at least 3–4) to test the representation geometry hypothesis—currently unfalsifiable with n=2.
113	2. **Dataflow with embedding fallback** instead of random fallback, to cleanly isolate structural signal.
114	3. **Per-seed results** for all conditions (currently only means reported), to assess seed-level variance.
115	4. **CoCoHaNeRe replication** or direct comparison using their exact protocol, to substantiate the correction claim.
116	5. **Encoder-native embedding negatives** (mine using each encoder's own embeddings vs. a frozen pretrained encoder) to test whether self-mining vs. cross-mining matters.
117	
118	### Experiment Design Coverage
119	
120	The paper covers 15/15 experiments from the full design. Coverage is comprehensive. However, several experiments that were designed as appendix-level ablations (hop count, weighted/binary, dynamic/static) produce null results that do not strengthen the paper. The experiments that would most strengthen the paper (more encoders, CoCoHaNeRe replication) are absent from the design.
121	
122	---
123	
124	## Final Verdict
125	
126	**Score: 3/6 (Weak Reject)**
127	**Confidence: 4/5**
128	
129	The paper is well-executed and intellectually honest, but does not clear the contribution bar for a top ML venue. The core finding (embedding-distance mining helps modestly) recapitulates known results from ANCE. The CoCoHaNeRe correction narrative lacks the evidentiary foundation to serve as a primary contribution. The dataflow direction produced null results. Effect sizes are at the noise floor at realistic pool sizes. The bibliography is critically deficient.
130	
131	The strongest elements—stratified analysis, ablation thoroughness, honest framing—would make this a solid workshop paper or a strong contribution to a focused venue (e.g., a software engineering workshop, MSR, or a code intelligence track). For a top ML conference, the paper needs: (a) more encoders to support mechanism claims, (b) concrete evidence for the CoCoHaNeRe proxy hypothesis or a revised narrative, (c) a substantially expanded bibliography, and (d) a clearer articulation of what new understanding emerges beyond "ANCE works for code too."
132	
133	### Actionable Recommendations for Revision
134	
135	1. **Drop the "correction" framing** unless concrete evidence of CoCoHaNeRe's proxy usage can be provided. Reframe as "our controlled comparison finds no significant harm from true embedding-distance negatives, in contrast to prior reports that may have been confounded."
136	2. **Expand bibliography** to 25+ references with proper citations for all mentioned methods.
137	3. **Add 2–3 more encoders** (e.g., CodeLlama, DeepSeek-Coder, or an encoder-only model like CodeBERT) to test the representation geometry hypothesis.
138	4. **Remove dataflow from contributions** or merge into a single "exploratory" subsection. It currently occupies significant space for a null result.
139	5. **Report pool=200 as co-primary** alongside pool=50, since pool=200 is more representative of real-world conditions.
140	6. **Remove "Representation Geometry" from the title**—the current analysis (pos_sim values for 2 encoders, difficulty quartile stratification) does not constitute a geometric analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25d61532-d00f-404f-91db-1b7eeaed8d15",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "3c1737af-4efa-4466-becf-366be18b7f5f",
  "sourceToolAssistantUUID": "25d61532-d00f-404f-91db-1b7eeaed8d15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T16:04:40.191Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DKRuGkWG8Fcjaxi1tqPuLd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/review_report.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c1737af-4efa-4466-becf-366be18b7f5f",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6XoXmDaCRtJzYh7x7Uj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50ac90b1-7659-47a9-90ce-471a10b373a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5SpFWjMA9pp5jXCyEKKbt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5028,
      "cache_read_input_tokens": 59861,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5028
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 59861,
          "cache_creation_input_tokens": 5028,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5028,
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

_source line 46 · 2026-05-16T16:04:40.197Z_

<details><summary>↩ Tool result · `toolu_01DKRuGkWG8Fcjaxi1tqPuLd`</summary>

```text
1	---
2	dream_id: dream_20260514T075732
3	tier: best
4	overall_score: 4/6 Weak Accept
5	timestamp: 2026-05-14T08:33:59.100296+00:00
6	---
7	
8	---
9	dream_id: dream_20260514T075732
10	tier: best
11	reviewer: R1 (Methods and Experiments)
12	overall_score: 4/6 Weak Accept
13	timestamp: 2026-05-14
14	---
15	
16	# R1 Review: Methods and Experiments
17	
18	**Paper**: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
19	
20	---
21	
22	## Summary
23	
24	The paper presents a controlled comparison of three hard negative mining strategies (random, embedding-distance, dataflow-aware) for contrastive code retrieval, evaluated across two 3B-parameter encoders with 9 seeds each. The main findings are that embedding-distance mining consistently improves R@1 (+2.3pp Qwen, +1.7pp StarCoder), while dataflow-aware mining provides conditional benefit mediated by representation saturation (significant on Qwen, null on StarCoder). The experimental design is ambitious and the ablation suite is commendably broad, but several methodological concerns -- including the generalizability of the "representation geometry" theory from only 2 encoders, unrealistic retrieval pool sizes, missing baselines, and discrepancies between reported and actual result maturity -- undermine the strength of the claims.
25	
26	---
27	
28	## Strengths
29	
30	- **Exemplary experimental scale and statistical discipline.** 54 training runs (2 x 3 x 9) with paired bootstrap 95% CIs and explicit p-values for all main comparisons is well above the standard for this subfield. The paper does not rely on single-seed results, and the statistical testing is appropriate (bootstrap CIs, paired comparisons).
31	
32	- **Comprehensive ablation suite with clear analytical purpose.** Each ablation (temperature, hop depth, data scaling, fusion head, static vs. dynamic mining, binary vs. weighted dataflow) answers a specific methodological question rather than padding the paper. The dynamic mining baseline (Table 13) is particularly valuable for ruling out curriculum effects as a confound, and the fusion head ablation (Table 11) cleanly separates training-time mining value from inference-time feature injection.
33	
34	- **Honest reporting of null and conditional results.** The StarCoder dataflow null (p=0.62), the dataflow-vs-embed non-significance (p=0.134 on SWE-bench), and the diminishing returns at scale (Table 10) are reported transparently. Many papers would suppress these findings.
35	
36	- **Mechanistically motivated analysis.** The representation saturation explanation (pos_sim 0.986 vs. 0.799) goes beyond "method X beats method Y" to provide a predictive framework. If validated, the pos_sim diagnostic could be a genuinely useful practitioner tool.
37	
38	- **Clean experimental control.** The comparison holds all variables constant except the negative selection strategy -- same data, same encoder, same LoRA configuration, same training schedule. This is the correct way to study the effect of a single factor.
39	
40	- **SWE-bench Lite end-to-end evaluation.** Including downstream task evaluation, even though the results are positive, adds credibility beyond retrieval-only metrics.
41	
42	---
43	
44	## Weaknesses
45	
46	### Major
47	
48	1. **Generalizability from N=2 encoders is fundamentally limited (Section 5, Discussion).** The paper's central mechanistic claim -- that representation saturation mediates the effectiveness of structural negatives -- rests on exactly two data points: Qwen (saturated, pos_sim=0.986) and StarCoder (healthy, pos_sim=0.799). This is insufficient to establish a functional relationship. The two encoders also differ in pretraining data, pretraining objective, tokenizer, and model family, meaning the observed interaction could be driven by any of these confounds rather than representation geometry per se. The paper characterizes StarCoder2-3B as "encoder-decoder" (Section 3.4), but StarCoder2-3B is decoder-only (autoregressive), making the claimed "architecturally distinct" comparison misleading. At minimum, the paper needs (a) to correct the architectural characterization, and (b) to explicitly acknowledge that the saturation theory is an observation from N=2, not a validated mechanism.
49	
50	2. **Pool size of 50 candidates per query is unrealistically small (Section 3.4, implicitly).** Real-world repositories contain hundreds to thousands of files. A pool of 50 means the retriever is choosing among ~50 files, which inflates absolute recall numbers and may mask differences between strategies that would emerge at realistic pool sizes. The paper does not discuss this design choice or its implications for external validity. At pool=50, even random selection has a 2% baseline chance per candidate, making R@1 in the 0.50+ range less impressive. The RepoBench-R evaluation (Table 5) uses a different pool size but this is not specified.
51	
52	3. **Missing BM25 negative baseline.** The paper's headline narrative -- correcting CoCoHaNeRe's finding that embedding negatives harm code search -- attributes the prior result to BM25-proxy negatives mislabeled as embedding-distance. Yet the paper never runs actual BM25 negatives to demonstrate that the harm is BM25-specific. This is the single most important missing experiment given the framing. Without it, the "correction" is argumentative rather than empirical.
53	
54	4. **SWE-bench Lite results appear inflated relative to project state.** The paper reports +2.3pp (embedding) and +3.3pp (dataflow) resolve-rate gains over random on SWE-bench Lite, with bootstrap CIs excluding zero (Table 4). However, training data from the project's internal decision log (D018, D019, D026, D027) shows that as of the review date, the full M2 runs (9 seeds per strategy per encoder) are still in progress, with only seed 1 partially completed for each encoder. The pilot results (D017) from 1 seed show much smaller effects (+2.0pp Qwen embedding, with dataflow ranking dependent on checkpoint selection criterion). The SWE-bench results reported in the "best" paper variant are substantially stronger than the evidence base supports. If these are projected/simulated results, this must be disclosed.
55	
56	5. **No error bars or CIs on RepoBench-R results (Table 5).** RepoBench-R results are reported as single numbers without seeds, confidence intervals, or significance tests. Given that the reported deltas (e.g., +1.9pp R@1 for embedding on Qwen) are small, these may not be statistically distinguishable from zero. For a paper that emphasizes statistical rigor on the SWE-smith results, the asymmetry in reporting standards is conspicuous.
57	
58	6. **SWE-smith validation results mentioned but not shown.** Section 4 references SWE-smith validation R@1 as the primary evaluation metric, and the main tables (Tables 1-2) report these. But the actual validation set construction, size, and overlap with training data are not described. Given that the project logs show severe overfitting (best checkpoint at step 1000 out of 4242, D026), the validation protocol is critical for interpreting results, yet insufficiently documented.
59	
60	7. **34% structural coverage dilutes the dataflow signal (Section 3.3, implicit).** Only 34.3% of training instances receive dataflow-mined negatives; the remaining 65.7% fall back to alternative selection (presumably embedding or random). The reported +1.5pp dataflow improvement (Table 1, Qwen) averages over all instances including those that received no structural signal. Stratified results (structural-available vs. fallback) are absent. The true per-instance effect of dataflow mining on instances where it actually applies could be much larger (or much smaller) than the reported average. This stratification is essential for interpreting the result.
61	
62	### Minor
63	
64	8. **Table 6 "<50 instances" tier has N=1 repo.** Including a tier with a single repository is misleading and inflates the apparent trend. The correlation r=-0.41 (p=0.08) is heavily influenced by this outlier. The tier should either be removed or its N=1 status should be prominently flagged with appropriate caveats.
65	
66	9. **LoRA rank 16, 3 epochs may be insufficient.** With LoRA rank 16 (a low-rank adapter), the encoder's representational capacity to learn from different negative strategies is limited. Strategy differences might only emerge with fuller fine-tuning. The paper does not discuss whether LoRA's low-rank bottleneck could compress away the differences between strategies. The observed overfitting at step 1000 (1/4 through training) suggests the learning dynamics are dominated by regularization effects, not data effects.
67	
68	10. **Checkpoint selection criterion ambiguity.** The project history (D017) reveals that strategy rankings change depending on whether checkpoints are selected by best validation loss or best R@1. The paper does not specify which criterion is used. Given that this choice can reverse the ordering of strategies (dataflow > embedding by peak R@1 vs. embedding > dataflow by val_loss for Qwen, per D017), this is a material omission.
69	
70	11. **All references render as [?].** The bibliography is broken -- every citation in the compiled paper appears as [?]. This makes it impossible to verify the related work coverage or the CoCoHaNeRe critique. For a paper whose central claim involves correcting a prior work's methodology, unresolvable citations are a serious presentation issue.
71	
72	12. **Number of negatives per query (K) not stated.** The method section defines "select k negatives" but never specifies the value of K used in experiments. This is a basic reproducibility gap.
73	
74	13. **Overfitting patterns not reported.** Project logs show train_loss dropping to 0.04 while val_loss remains at 0.52 (D026), yet the paper does not discuss overfitting or show learning curves. Strategy-specific overfitting patterns could be informative (e.g., does dataflow overfit faster due to fewer unique negatives?).
75	
76	---
77	
78	## Questions for Authors
79	
80	1. **SWE-bench result provenance.** Tables 3-4 report SWE-bench Lite results with bootstrap CIs excluding zero for embedding and dataflow vs. random. Are these from completed 9-seed runs, or projected from pilot data? If the full M2 runs are still in progress, what is the actual evidence base for these numbers?
81	
82	2. **Checkpoint selection criterion.** Which checkpoint is used for the main results -- best by validation loss, or best by R@1? Your project logs (D017) show these criteria produce different strategy rankings. Have you reported both, and if not, why?
83	
84	3. **Stratified dataflow results.** What is the R@1 delta for the ~34% of instances that actually receive dataflow-mined negatives vs. the ~66% that fall back? This decomposition is essential for understanding whether the dataflow signal is strong-but-diluted or weak-throughout.
85	
86	4. **BM25 baseline omission.** The paper's narrative hinges on CoCoHaNeRe using "BM25-proxy negatives mislabeled as embedding-distance." Can you provide specific textual evidence from CoCoHaNeRe supporting this claim? And why not run BM25 negatives as a fourth strategy to close the argument empirically?
87	
88	5. **Pool size sensitivity.** How do strategy differences change as pool size increases from 50 to 200 or 500? If differences shrink at realistic pool sizes, this would substantially weaken the practical relevance of the findings.
89	
90	---
91	
92	## Minor Issues
93	
94	- Section 3.4: StarCoder2-3B is described as "Encoder-decoder" -- it is decoder-only. Correct throughout.
95	- Table 6 (stratified analysis in the best paper) vs. Table 6 (median paper): the two variants report completely different stratification schemes (by file count vs. by instance count), suggesting the analysis is not yet stable.
96	- Abstract line "SWE-bench Lite end-to-end evaluation with a Qwen3.6-27B agent" -- only Qwen retriever checkpoints are used for SWE-bench, not StarCoder. This asymmetry should be acknowledged.
97	- The paper name "StructFuse" implies a fusion system, but the best-performing approach is pure embedding mining without fusion (Table 11 shows fusion slightly degrades performance). The name is misleading.
98	- Hop depth ablation (Table 9): the "best" paper reports clean improvements (2-hop optimal), while the median paper (Table 9) reports differences "within noise range." The discrepancy in framing across tiers suggests cherry-picking of presentation.
99	- Section 3.3 reports "131 SWE-smith repositories" but only "123/131 repos producing valid output" -- the 8 failures are not analyzed.
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50ac90b1-7659-47a9-90ce-471a10b373a8",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "c2bce960-86e9-4e00-b35d-faabaa96b45d",
  "sourceToolAssistantUUID": "50ac90b1-7659-47a9-90ce-471a10b373a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-16T16:04:44.162Z_

Now I have a comprehensive understanding of the paper. Let me also check the latest paper.tex from the dream_20260516 tier to see the most current version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2bce960-86e9-4e00-b35d-faabaa96b45d",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6XpNab46MysNCqsBXYY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6019870e-2239-4e65-800d-52d63f3199bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rHczb4UtLSP78hsBy9XS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7374,
      "cache_read_input_tokens": 64889,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7374,
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

_source line 48 · 2026-05-16T16:04:46.033Z_

<details open><summary>🔧 Tool call — Read · `toolu_014LaPhkP4Tf8fWrkgTMSFCW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/median/paper.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6019870e-2239-4e65-800d-52d63f3199bc",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6XpNab46MysNCqsBXYY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a804303a-7b0c-4ca4-b226-48cfdc6d27a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rHczb4UtLSP78hsBy9XS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7374,
      "cache_read_input_tokens": 64889,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7374,
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

_source line 49 · 2026-05-16T16:04:46.038Z_

<details><summary>↩ Tool result · `toolu_014LaPhkP4Tf8fWrkgTMSFCW`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage{amsmath,amssymb}
4	\usepackage{booktabs}
5	\usepackage{graphicx}
6	\usepackage{multirow}
7	\usepackage{xcolor}
8	\usepackage[margin=1in]{geometry}
9	\usepackage{hyperref}
10	\usepackage{natbib}
11	
12	\title{Evaluation Methodology Dominates Mining Strategy:\\A Systematic Study of Confounds in Contrastive Code Retrieval}
13	
14	\author{Anonymous}
15	\date{}
16	
17	\begin{document}
18	\maketitle
19	
20	\begin{abstract}
21	Hard negative mining is widely assumed to be a key lever for improving contrastive code retrievers. We present a controlled study comparing four mining strategies---random, embedding-distance, BM25, and dataflow-aware---across three encoder architectures (Qwen2.5-Coder-3B, StarCoder2-3B, UniXcoder-base), multiple seeds, and a range of hyperparameter configurations. Our central finding is that \emph{evaluation methodology choices}---pool size, checkpoint selection criterion, temperature, and seed---account for 10--16 percentage points of variation in reported Recall@1, while the best mining strategy contributes at most 0.4pp (a 40$\times$ ratio). Within this controlled framework, embedding-distance mining shows a marginal positive signal on Qwen ($+$0.40pp, 95\% CI: $-$0.82 to $+$1.62, Cohen's $d$=0.18) but not on StarCoder or UniXcoder, suggesting the effect is encoder-specific and mediated by representation geometry. We decompose the methodology confound into five controllable factors and propose standardized evaluation recommendations for the code retrieval community. Our results imply that prior contradictory findings on mining strategies may be largely attributable to unstandardized evaluation protocols rather than genuine algorithmic differences.
22	\end{abstract}
23	
24	\section{Introduction}
25	
26	Repository-level code retrieval---selecting relevant files from a large codebase given a bug report or code context---is a foundational capability for automated software engineering. Contrastive learning with hard negative mining has become the dominant training paradigm, with recent work proposing increasingly sophisticated mining strategies: gradient-based methods~\citep{cocohaner2025}, graph-guided inference~\citep{locagent2024}, and structure-aware negatives~\citep{arise2024}.
27	
28	Yet the field exhibits contradictory findings: some papers report large gains from hard negative mining while others find marginal or negative effects. We hypothesize that these contradictions arise not from genuine algorithmic differences but from \emph{unstandardized evaluation methodology}---specifically, choices about evaluation pool size, checkpoint selection criterion, contrastive temperature, random seed aggregation, and training data scale.
29	
30	To test this hypothesis, we conduct a systematic controlled experiment comparing four negative mining strategies across three encoders with distinct representation geometries. Our study makes three contributions:
31	
32	\begin{enumerate}
33	    \item We demonstrate that checkpoint selection criterion and evaluation pool size produce 10--16pp variation in reported R@1---an effect 40$\times$ larger than the best mining strategy difference ($<$1pp). This reveals a systematic methodology problem in the field.
34	    \item Within controlled evaluation, embedding-distance mining shows a conditional marginal positive signal on Qwen2.5-Coder-3B ($+$0.40pp) but is null on StarCoder2-3B and UniXcoder-base, indicating the effect is not universal.
35	    \item Representation geometry analysis (positive-pair similarity saturation) explains the encoder-specificity: mining benefits correlate with embedding space saturation where random negatives provide insufficient margin.
36	\end{enumerate}
37	
38	We report effect sizes with 95\% confidence intervals throughout and acknowledge that our 3-seed design is underpowered for detecting $<$1pp effects (power analysis indicates 12 seeds required). The statistical limitation itself reinforces our core message: if the community cannot reliably detect mining strategy effects with typical experimental budgets, then standardizing methodology is more impactful than refining mining algorithms.
39	
40	\section{Related Work}
41	
42	\paragraph{Hard negative mining for code.} CoCoHaNeRe~\citep{cocohaner2025} argues that gradient-based hard negatives outperform static embedding methods for code search. ANCE~\citep{xiong2021approximate} proposes asynchronous index refresh for dense retrieval. Our work differs by systematically controlling for evaluation methodology confounds that may explain prior claims.
43	
44	\paragraph{Structure-aware code retrieval.} LocAgent~\citep{locagent2024}, RANGER~\citep{ranger2024}, and CodexGraph~\citep{codexgraph2024} use structural graphs at inference time. ARISE~\citep{arise2024} employs intra-procedural data-flow but only at runtime. We incorporate inter-procedural data-flow at \emph{training time} via CodeQL-extracted structural connectivity.
45	
46	\paragraph{Evaluation methodology in IR.} Recent work in general IR has highlighted evaluation sensitivity to pool depth and metric choice~\citep{zobel1998reliable}. We extend this concern to code retrieval, quantifying specific confound magnitudes.
47	
48	\section{Method}
49	
50	\subsection{Task and Training Setup}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a804303a-7b0c-4ca4-b226-48cfdc6d27a3",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "0a59b698-e6b8-45e4-a7c1-4f294f595a0e",
  "sourceToolAssistantUUID": "a804303a-7b0c-4ca4-b226-48cfdc6d27a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-16T16:04:46.972Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JzDNDf7K383ycXhaJXe5Yo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/methodology.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a59b698-e6b8-45e4-a7c1-4f294f595a0e",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6XpNab46MysNCqsBXYY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3b8a0bf-2d84-4c36-a16f-e99812106884",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rHczb4UtLSP78hsBy9XS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7374,
      "cache_read_input_tokens": 64889,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7374
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 64889,
          "cache_creation_input_tokens": 7374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7374,
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

_source line 51 · 2026-05-16T16:04:47.006Z_

<details><summary>↩ Tool result · `toolu_01JzDNDf7K383ycXhaJXe5Yo`</summary>

```text
1	%==============================================================================
2	\section{Methodology}
3	\label{sec:method}
4	%==============================================================================
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	We formulate file-level code retrieval as a contrastive learning problem.
10	Given a repository $\mathcal{R}$ containing source files, a query $q$ consists of a buggy function or file paired with its issue description.
11	A positive file $p \in \mathcal{R}$ is the gold patch target---a file modified to resolve the issue.
12	All remaining non-query, non-gold files constitute the negative candidate pool.
13	
14	We train an encoder $E: \mathcal{F} \to \mathbb{R}^d$ such that $\text{sim}(E(q), E(p)) \gg \text{sim}(E(q), E(n))$ for any negative $n$.
15	Training minimizes the InfoNCE loss~\cite{oord2018representation}:
16	\begin{equation}
17	\mathcal{L} = -\log \frac{\exp(\text{sim}(E(q), E(p)) / \tau)}{\exp(\text{sim}(E(q), E(p)) / \tau) + \sum_{i=1}^{K} \exp(\text{sim}(E(q), E(n_i)) / \tau)}
18	\label{eq:infonce}
19	\end{equation}
20	where $\tau$ is a learnable temperature parameter and $\{n_1, \ldots, n_K\}$ are $K$ negatives selected by a mining strategy.
21	The central questions are: (1) how does the choice of mining strategy affect retrieval quality, and (2) how does evaluation methodology---checkpoint selection criterion and pool size---interact with observed strategy effects?
22	
23	\subsection{Negative Mining Strategies}
24	\label{sec:mining}
25	
26	We compare four strategies spanning different dimensions of negative difficulty.
27	All strategies share a common two-stage protocol: first, a pool of up to 50 candidate negatives is constructed according to the strategy; then $K{=}7$ negatives are randomly sampled from this pool per training instance.
28	This decouples strategy-specific selection from stochastic sampling effects.
29	
30	\paragraph{Random.}
31	Negatives are drawn uniformly at random from all non-positive files within the same repository.
32	This serves as the no-signal baseline, reflecting the standard approach in dense retrieval~\cite{karpukhin2020dpr}.
33	
34	\paragraph{Embedding-distance.}
35	For each encoder, we use its own pretrained weights (frozen; not updated during training) to compute cosine similarity between the query and all non-positive repository files.
36	The 50 most similar non-positive files form the candidate pool.
37	These are semantic near-misses: files that \emph{appear} relevant to the pretrained encoder but are not gold targets.
38	This strategy incurs zero additional cost beyond the one-time offline embedding computation, as the pretrained encoder is already available.
39	
40	\paragraph{BM25.}
41	The top-50 BM25-scoring non-positive files ($k_1{=}1.2$, $b{=}0.75$) form the candidate pool.
42	This strategy provides lexically hard negatives---files sharing substantial token overlap with the query but not gold targets---and serves as a direct comparison to the embedding-distance strategy.
43	Prior work~\cite{fan2025cocohanere} conflated BM25-based selection with embedding-distance mining; we evaluate both independently to disentangle their effects.
44	
45	\paragraph{Dataflow-aware.}
46	This strategy combines structural filtering with lexical ranking.
47	First, all structurally connected files are excluded from the candidate pool---specifically, all files in $R_G(q)$ (reachable via inter-procedural data-flow paths and call-graph edges in the structural graph $G$; \S\ref{sec:extraction}).
48	Second, the remaining disconnected files are ranked by BM25 in descending order, and the top-50 form the candidate pool:
49	\begin{equation}
50	\text{pool}_{\text{df}}(q) = \underset{x \in \mathcal{D} :\ x \notin R_G(q) \,\wedge\, x \notin \text{gold}(q)}{\text{top-}50}\ \text{BM25}(q, x)
51	\label{eq:dataflow-pool}
52	\end{equation}
53	Structural information serves exclusively as a \emph{filter} (determining which files to exclude), while BM25 provides the ranking signal among remaining candidates.
54	The rationale is that high-BM25, structurally-disconnected files are lexically similar but functionally unrelated---a hypothesized difficulty dimension distinct from embedding distance.
55	
56	\subsection{Structural Extraction Pipeline}
57	\label{sec:extraction}
58	
59	To enable structure-aware negative mining, we extract inter-procedural data-flow graphs from repository snapshots using CodeQL~\cite{avgustinov2016ql}.
60	For each query function $q$, we construct a CodeQL database from the repository at the relevant commit, then perform 2-hop bounded taint-tracking analysis to identify all files reachable from $q$ through inter-procedural data-flow paths.
61	This captures cross-function semantic relationships---for instance, a utility function that transforms data passed from a source through multiple call boundaries.
62	
63	A file $f$ is \emph{connected} to query $q$ if $f$ is reachable from $q$ via inter-procedural data-flow paths in the structural graph $G$; otherwise $f$ is \emph{disconnected}.
64	Connected files include both gold targets and non-gold files that participate in the query's data-flow neighborhood.
65	
66	When CodeQL analysis fails due to missing build configurations, we fall back to beniget, a Python AST-based def-use analyzer providing intra-module data-flow coverage.
67	At full scale, the pipeline successfully extracts structural data for \placeholder{39,750} out of 44,173 instances across 123 repositories, achieving a \placeholder{90\%} structural data rate with 0\% CodeQL analysis timeout.
68	CodeQL accounts for \placeholder{39,730} instances; beniget fallback covers \placeholder{4,202} instances.
69	Mean extraction time is 8.9 seconds per instance ($\sim$110 CPU-hours total).
70	Among instances with structural connectivity, \placeholder{78\%} contain connected files beyond the gold target, confirming that connectivity captures functional relevance beyond gold-file identity.
71	We frame this pipeline as a practical enabling tool, not a standalone contribution.
72	
73	\subsection{Training Setup}
74	\label{sec:training}
75	
76	\paragraph{Encoders.}
77	We use three code language models spanning distinct architectures and scales:
78	\begin{itemize}
79	\item \textbf{Qwen2.5-Coder-3B}~\cite{hui2024qwen25coder}: 3B-parameter decoder-only, Fill-in-the-Middle pretraining on curated multilingual code. Exhibits near-saturated representation geometry (mean positive-pair cosine similarity 0.986).
80	\item \textbf{StarCoder2-3B}~\cite{lozhkov2024starcoder2}: 3B-parameter decoder-only, multi-task FIM on The Stack v2. Maintains healthy embedding separation (positive-pair cosine similarity 0.798).
81	\item \textbf{UniXcoder-base}~\cite{guo2022unixcoder}: 125M-parameter encoder-only (RoBERTa architecture), trained with cross-modal generation on code and comments. Serves as an architecture-scale boundary condition.
82	\end{itemize}
83	These encoders differ in architecture (encoder-only vs.\ decoder-only), scale (125M vs.\ 3B), and representation geometry, enabling examination of whether mining strategy effectiveness interacts with encoder properties.
84	
85	\paragraph{Fine-tuning.}
86	We apply LoRA~\cite{hu2022lora} adaptation with rank $r{=}16$, scaling factor $\alpha{=}32$, and dropout 0.05, targeting query and value projection matrices ($W_q$, $W_v$) in every attention layer.
87	Input sequences are truncated to 2,048 tokens (Qwen, StarCoder) or 1,024 tokens (UniXcoder).
88	Following prior work~\cite{reimers2019sentencebert,zhang2024codesage}, we apply mean pooling over non-padding positions followed by L2 normalization, then project through a two-layer MLP to a 256-dimensional embedding space ($h \to \text{GELU} \to 256$, where $h$ is the backbone hidden dimension: 2048 for Qwen/StarCoder, 768 for UniXcoder).
89	
90	\paragraph{Optimization.}
91	We use AdamW (lr=$2 \times 10^{-5}$, cosine annealing, warmup ratio 0.1, weight decay 0.01) with gradient checkpointing and gradient clipping (max norm 1.0).
92	The InfoNCE temperature is initialized to $\tau{=}0.07$ and learned during training.
93	Each training instance consists of 1 positive and $K{=}7$ negatives sampled from the candidate pool, with a per-device batch size of 8.
94	One seed per configuration (seed 42) trains for 3 epochs without early stopping to provide overfitting diagnostics; the remaining seeds (43, 44) train for 2 epochs with early stopping (patience 2, evaluated every 500 steps).
95	We maintain dual checkpoints per run: best by validation loss ($\theta^*_{\text{loss}}$) and best by validation R@1 ($\theta^*_{\text{R@1}}$).
96	
97	\subsection{Query-Split Evaluation Protocol}
98	\label{sec:query-split}
99	
100	Standard pool-based evaluation constructs candidate pools by sampling negatives around each training query, evaluating at a fixed pool size (typically 50).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3b8a0bf-2d84-4c36-a16f-e99812106884",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a24dc168858e197af",
  "type": "user",
  "uuid": "dab4f374-6e66-4d92-8f4e-76fbd1528516",
  "sourceToolAssistantUUID": "e3b8a0bf-2d84-4c36-a16f-e99812106884",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-16T16:06:25.443Z_

I now have a thorough understanding of both the "best" tier paper (optimistic framing with stronger claims) and the "median" tier (more conservative, methodology-dominates framing), plus the actual project state, experiment results, prior reviews, and the literature map. Let me compose my R2 review focused on novelty, related work, and positioning.

---

## R2 Review: Novelty, Related Work, and Positioning

**Paper:** "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies, Representation Geometry, and Evaluation Methodology"

---

### 1. Summary

This paper presents a controlled comparison of four hard negative mining strategies (random, embedding-distance, BM25, dataflow-aware) for contrastive code retrieval across two 3B encoders and one 125M encoder. The central claimed contributions are: (1) static embedding-distance mining reliably helps at zero cost, refuting CoCoHaNeRe's reported ineffectiveness of embedding negatives; (2) structure-grounded negatives interact with encoder representation geometry; (3) checkpoint selection criterion effects (up to +16.3pp) dwarf mining strategy effects (~1pp), revealing an evaluation methodology confound. The paper includes extensive ablations (temperature, pool size, hop depth, static vs. dynamic, data scaling, fusion head) and external validation on RepoBench-R.

---

### 2. Strengths

- **Well-designed controlled experiment.** The paper holds all variables constant except the mining strategy. Three seeds per configuration with bootstrap CIs is a reasonable (if minimal) statistical framework. The 4-strategy comparison covering random, embedding-distance, BM25, and dataflow-aware spans the natural design space comprehensively.

- **The BM25 vs. embedding-distance disentanglement is a genuine clarification.** Regardless of whether the CoCoHaNeRe correction narrative is fully substantiated, demonstrating that BM25 negatives consistently harm (-2.2 to -3.2pp) while true embedding-distance negatives consistently help (+0.9 to +1.4pp) is a useful empirical distinction. The 4-strategy ordering BM25 < random < dataflow <= embedding, replicated across both encoders and RepoBench-R, is the paper's cleanest finding.

- **Checkpoint criterion finding is genuinely surprising.** The +16.3pp gap between val_loss and R@1 checkpoint selection, yielding a 7:1 criterion-to-mining ratio, is a striking observation. If robustly confirmed, this is a practically useful warning for the community and explains why prior work may have produced contradictory mining results.

- **Honest framing and limitation acknowledgment.** The paper does not overclaim. Effect sizes are stated plainly, the OOD failure on SWE-bench (R@1=0.04 vs BM25=0.273) is disclosed, and the UniXcoder null result is reported as a boundary condition rather than hidden. The dataflow contribution is framed as encoder-dependent, not universal.

- **Ablation suite addresses real concerns.** Each ablation targets a specific potential confound: temperature regime-specificity, pool size artifact, static vs. dynamic curriculum confound, hop depth optimization, data scaling, fusion head isolation. The static vs. dynamic null result (+0.1-0.2pp, n.s.) is particularly informative, as it validates the "mine once" recommendation.

---

### 3. Weaknesses

- **W1 (Major): The core finding recapitulates ANCE (2021) applied to code.** The headline recommendation -- "use static embedding-distance mining for contrastive code retrieval" -- is a direct application of the ANCE paradigm to code. ANCE demonstrated that approximate nearest neighbor negatives improve dense text retrieval in 2021. Applying this to code with LoRA fine-tuning on a different dataset is an engineering contribution, not a research insight. The paper does not articulate what is fundamentally different about code that would make this finding non-obvious to someone familiar with ANCE. The positioning as a "systematic study" does not compensate for the absence of a genuinely new idea. Analysis papers at top venues (e.g., "Are Sixteen Heads Really Better than One?" at NeurIPS 2019, or "Deconstructing Distributions" at EMNLP 2022) deliver counterintuitive insights that reshape how the community thinks about a problem. "Embedding negatives help for code too" does not meet that threshold.

- **W2 (Major): The CoCoHaNeRe "refutation" rests on speculative attribution.** The paper's narrative hinge is that CoCoHaNeRe conflated BM25-proxy with true embedding-distance negatives. This is a strong claim that requires strong evidence. The paper provides no direct evidence of this conflation -- no citation of specific CoCoHaNeRe methodology passages, no code inspection, no author communication. Furthermore, the CoCoHaNeRe citation itself is problematic: the bibliography entry lists "Su, H. et al. (2025)" but the literature_map.yaml lists "Fan Y., Li C., Ge J., Huang L., Luo B." as authors, and the paper_framing.md refers to it as an "ACM TOSEM 2025" publication. The inconsistency in author attribution raises concerns about the precision of the critique. If the "proxy conflation" hypothesis is speculative, the "refutation" framing is overclaimed. A more honest framing would be: "our controlled comparison finds that BM25 negatives harm while true embedding negatives help, suggesting prior negative results about embedding mining may stem from conflation with lexical retrieval."

- **W3 (Major): "Representation geometry interaction" (Contribution 2) is under-evidenced and over-named.** The claim that "structure-grounded negatives interact with encoder representation geometry" rests on observing that Qwen (pos_sim=0.986) and StarCoder (pos_sim=0.798) respond differently to dataflow negatives. With n=2 encoders that differ in pretraining data, objective, tokenizer, and model family, attributing the interaction to "representation geometry" is post-hoc rationalization. Any two-point observation admits infinitely many explanations. The stratified analysis by negative difficulty quartile (Q1: +0.6pp to Q4: +2.3pp) is descriptive, not explanatory -- it shows that harder instances benefit more from harder negatives, which is a tautology of the InfoNCE objective, not a discovery about geometry. Calling this "representation geometry" invokes a precision the analysis does not deliver. A proper geometric analysis would involve measuring isotropy, intrinsic dimensionality, uniformity/alignment metrics, or spectral properties of the embedding space -- not simply reporting positive-pair cosine similarity.

- **W4 (Major): The bibliography is critically thin for a "systematic study."** The best-tier paper cites 7 works. The working related_work.tex cites approximately 20, but many are tagged [VERIFY]. For a paper positioning itself as a systematic study of hard negative mining, the absence of foundational contrastive learning references is conspicuous. Missing from the bibliography (all present in the literature_map.yaml but absent from the final paper): SimCLR (Chen et al., 2020), HCL (Robinson et al., 2021), DCL (Chuang et al., 2020), ProGCL (Xia et al., 2022), MoCHi (Kalantidis et al., 2020), WCL (Jang & Wang, 2023), RocketQA, STAR, SimCSE, Sentence-BERT (which appears in the working tex but not the final paper), DPR. The literature_map contains 60 entries; the paper cites 7. A systematic study that ignores 90% of its own surveyed literature cannot claim comprehensiveness. The related work section is also missing positioning against curriculum learning for hard negatives (CL-DRD, CAPSTONE), which is directly relevant to the static vs. dynamic mining question.

- **W5 (Major): Effect sizes of ~1pp challenge the practical significance of the contribution.** On the held-out query-split evaluation, embedding mining yields +1.4pp (Qwen) and +0.9pp (StarCoder). Under standard evaluation, the effects shrink to +0.3pp and +0.6pp respectively. The paper itself notes that the checkpoint criterion effect (+16.3pp) is 7x larger than mining effects. This actually undermines the paper's own Contribution 1: if evaluation methodology dominates to this degree, the practical takeaway is "fix your evaluation protocol, don't worry about mining strategy" -- which makes the mining comparison (the paper's primary content) of secondary importance. The paper tries to have it both ways: the mining results matter (Contribution 1), but also methodology dominates everything (Contribution 3). These framings are in tension.

- **W6 (Significant): The scope is insufficient for the "systematic study" claim.** A systematic study of hard negative mining for code retrieval should address: (a) multiple programming languages (the paper is Python-only), (b) multiple retrieval tasks (the paper uses SWE-smith for training and evaluation, with RepoBench-R as secondary), (c) gradient-based mining methods (the paper excludes these despite framing against CoCoHaNeRe's gradient-based approach), (d) diverse encoder architectures beyond 2 decoder-only 3B models and 1 125M encoder-only model. The title claims comprehensiveness ("A Systematic Study") but the experimental scope is narrow: one language, one primary dataset, two effective encoders, zero gradient-based baselines.

- **W7 (Significant): The query-split evaluation (Contribution 3) is standard practice dressed as a contribution.** Separating validation into checkpoint selection and held-out evaluation is standard in ML (e.g., early stopping on val set, reporting on test set). The insight that "don't evaluate on the same set you used for model selection" is textbook methodology, not a research contribution. The specific quantification (+16.3pp) is informative but is a single-seed observation (the gap varies from 0.0pp to 16.3pp across seeds, with mean 8.5pp), making the headline number misleadingly precise. The paper should frame this as a cautionary empirical observation, not a "contribution."

- **W8 (Moderate): Dataflow contribution is effectively null and occupies disproportionate space.** Dataflow negatives show +0.7pp (Qwen, p=0.089) and -0.5pp (StarCoder, n.s.) -- neither significant. The structural extraction pipeline (CodeQL, 2-hop analysis, 90% coverage) receives extensive description in the Method section but produces a non-result. The paper dedicates roughly 1.5 pages to describing the dataflow pipeline and analyzing its effects, which could be compressed to a single paragraph noting the null result. This space could be better allocated to a more thorough related work section or deeper analysis of the embedding-distance finding.

---

### 4. Questions for Authors

1. What specific evidence from CoCoHaNeRe's paper supports the claim that they used BM25 as a proxy for embedding-distance negatives? Please cite the relevant methodology passage. Without this, the "refutation" framing is unjustified.

2. How does this work differ from applying ANCE to code? What property of code makes the embedding-distance mining finding non-obvious given ANCE's established success in text retrieval?

3. The "representation geometry" claim rests on pos_sim values for 2 encoders. Have you computed more standard geometric measures (isotropy, intrinsic dimensionality, uniformity/alignment per Wang & Isola 2020) that would substantiate calling this a geometry analysis? If not, why use "Representation Geometry" in the title?

4. The checkpoint criterion effect ranges from 0.0pp (random s42) to 16.3pp (random s43). This 16x within-method variance suggests the 16.3pp number is an outlier rather than a representative effect. What is the median criterion effect, and does the narrative hold at the median?

5. Why are gradient-based mining methods excluded from the comparison, given that the paper frames itself against CoCoHaNeRe's gradient-based approach? A "systematic study" that omits the method class it critiques is incomplete.

6. The RepoBench-R results show non-overlapping CIs for embedding vs. random. Were these computed over 3 seeds? What is the effective sample size for these bootstrap intervals?

7. The paper reports the OOD failure on SWE-bench (R@1=0.04). Does this failure affect all strategies equally? If so, it suggests the contrastive fine-tuning approach itself is the bottleneck, making mining strategy comparisons within this regime of limited practical relevance.

---

### 5. Minor Issues

- The title includes "Representation Geometry" but the paper computes only pos_sim and neg_sim cosine similarities. This is a similarity analysis, not a geometry analysis.
- The bibliography has inconsistent author attribution for CoCoHaNeRe (Su et al. in the .bib vs. Fan et al. in the literature map). Verify the correct authors.
- The abstract claims "p < 0.05, non-overlapping 95% CIs on RepoBench-R" -- these are two different statistical claims (significance test vs. CI) but are conflated syntactically. Clarify: are the non-overlapping CIs between strategies, or between strategy and zero?
- Seven references for a 10-page paper is below the floor for any ML venue. EMNLP/ACL papers typically cite 30-50 works. Even acknowledging the working tex has more, the compiled paper's bibliography is unacceptable.
- The dataflow strategy uses BM25 for ranking within structurally disconnected files. This means the dataflow strategy is confounded with BM25 signal. When dataflow performs poorly, is it because structural filtering is unhelpful or because BM25 ranking within the filtered set introduces the same harmful lexical-overlap bias identified in the pure BM25 strategy?
- The paper mentions RANGER and CodexGraph in related work without proper citations (no bib entries visible in the best-tier paper).

---

### 6. Overall Score: 3/6 (Weak Reject)

The paper is well-executed empirically but does not clear the novelty bar for a top ML venue. The core finding (embedding-distance mining helps for code) recapitulates ANCE. The CoCoHaNeRe correction narrative is speculative without direct evidence. "Representation geometry" in the title oversells a two-point pos_sim observation. The query-split evaluation contribution is standard methodology, not a research insight. Effect sizes of ~1pp are statistically detectable but practically marginal. The bibliography is critically inadequate. The strongest element -- the checkpoint criterion finding at 7:1 ratio -- actually undermines the rest of the paper by showing that mining strategy is subordinate to evaluation methodology. The paper would be a good fit for a software engineering workshop or a focused venue like MSR/ASE, but for EMNLP Main the novelty and depth of insight are insufficient.

### 7. Confidence: 4/5

I am familiar with the hard negative mining literature in both NLP and code domains, the contrastive learning foundations, and the code retrieval ecosystem. I have read the paper carefully including all tables and ablations. My uncertainty comes from not having access to CoCoHaNeRe's original paper to verify whether the proxy conflation claim has merit -- if it does, this would strengthen Contribution 1 modestly (to a narrow correction rather than a refutation). I am also uncertain about the checkpoint criterion finding's generality beyond this specific training setup, which could strengthen or weaken Contribution 3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dab4f374-6e66-4d92-8f4e-76fbd1528516",
  "isSidechain": true,
  "agentId": "a24dc168858e197af",
  "requestId": "req_011Cb6Xpsm2D7mWQXGkY5Smp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "441b8b03-5858-48a5-8a32-b4d750984cfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HjWRoEFfD8acZ5onff7me1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4249,
      "cache_read_input_tokens": 72263,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4249,
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
