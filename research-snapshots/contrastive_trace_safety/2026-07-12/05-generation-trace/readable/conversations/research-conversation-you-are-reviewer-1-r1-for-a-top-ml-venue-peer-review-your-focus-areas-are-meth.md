# Research conversation: You are Reviewer 1 (R1) for a top ML venue peer review. Your focus areas are **methods** and **experiments**. Use a 6-po

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a34533294cfd6f579.jsonl`
- **Structured JSON:** [`b53d96fad57d2d1d6b28.json`](../../sessions/b5/b53d96fad57d2d1d6b28.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

50 recorded events

### User

_source line 1 · 2026-05-16T16:03:26.886Z_

You are Reviewer 1 (R1) for a top ML venue peer review. Your focus areas are **methods** and **experiments**. Use a 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept. Target venue acceptance rate ~25%.

## Paper Summary

**Title:** "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies, Representation Geometry, and Evaluation Methodology"

The paper presents a controlled comparison of 4 negative mining strategies (random, static embedding-distance, dataflow-aware structural, BM25-based) across 2 3B-parameter code encoders (Qwen2.5-Coder-3B and StarCoder2-3B). Three contributions claimed:
1. Static embedding-distance mining reliably improves retrieval (+1.4pp Qwen, +0.9pp StarCoder on held-out eval) at zero compute cost, refuting CoCoHaNeRe's claim that embedding negatives are ineffective (they used BM25 as proxy).
2. Structure-grounded negatives interact with encoder representation geometry—benefits concentrate in hard-instance strata.
3. Checkpoint selection criterion effects (Δ up to +16.3pp) exceed mining strategy effects (~1pp) by 7×, revealing evaluation methodology confound.

## Key Experimental Details

**Setup:** LoRA rank 16 fine-tuning on SWE-smith (5K instances), τ=0.1, K=7 negatives, 3 seeds (42,43,44).

**Tables in paper:**
- Table 1: Standard eval (best by R@1), 4 strategies × 2 encoders. Embed Δ small: Qwen +0.3pp, SC +0.6pp.
- Table 2: Query-split eval (D062, 2480 held-out queries). Embed Δ larger: Qwen +1.4pp, SC +0.9pp.
- Table 3: Bootstrap 95% CIs (10K resamples). Embed significant (p=0.012 Qwen, p=0.038 SC). Dataflow borderline (p=0.089 Qwen). BM25 harm significant.
- Table 4: UniXcoder 125M, 3 seeds × 3 strategies. All null (max span 0.37pp).
- Table 5: RepoBench-R test_hard (pool≈18). Embed: Qwen +1.2pp, SC +0.8pp. Non-overlapping CIs.
- Table 6: Neg difficulty quartile stratification. Q4 hardest: +2.3pp embed, Q1 easiest: +0.6pp.
- Table 7: Structural data availability. With dataflow (90%): embed +1.3pp, df +0.8pp. No dataflow (10%): embed +1.4pp, df +0.1pp.
- Table 8: Temperature ablation τ∈{0.05, 0.1, 0.2}. Ranking preserved. Embed Δ: 1.2–1.6pp Qwen.
- Table 9: Pool size sensitivity (50/100/200/500). 100% ranking stability. Delta peaks at pool=100 (+1.4pp).
- Table 10: Checkpoint criterion effect. Max gap=+16.3pp (s43, random, Qwen). Mean=+8.5pp. Criterion-to-mining ratio=7.1×.
- Table 11: Hop depth ablation 1/2/3-hop. 2-hop optimal (55.8%), inverted-U.
- Table 12: Data size scaling 1K/3K/5K. Ranking stable, delta grows (0.9→1.4pp).
- Table 13: Fusion head ablation. Embed-only (56.7%) > combined (56.4%) > structural-only (50.1%).
- Table 14: Failure analysis 50 cases. "Similar but wrong" 38%, embed helps 17/19.

**Additional ablations mentioned in text (no dedicated tables):** weighted vs binary negatives (+0.1-0.2pp, n.s.); static vs dynamic mining (+0.1-0.2pp, n.s.).

**Limitations disclosed:** SWE-bench OOD failure (R@1=0.04 vs BM25=0.273); only 2 3B decoder-only encoders.

## Experiment Design Reference (what was planned)

The full experiment plan included these experiments. Check coverage:
- BM25 baseline (plan_018) — covered in Tables 1-2
- RepoBench-R with bootstrap CIs (plan_004) — covered in Table 5
- Stratified analysis 5 strata (plan_005) — partially covered: neg difficulty quartile (Table 6) and structural availability (Table 7) shown; repo size, pool size, query-pos similarity mentioned in text but no dedicated tables
- Call-graph hop depth (plan_007) — Table 11
- Data size scaling (plan_008) — Table 12
- Fusion head ablation (plan_009) — Table 13
- Weighted vs binary (plan_010) — text mention only
- Failure analysis (plan_011) — Table 14
- Qualitative examples (plan_012) — NOT in paper (no case studies with Fig 8)
- Temperature ablation (plan_014) — Table 8
- Dynamic vs static mining (plan_015) — text mention only
- Bootstrap CIs (plan_016) — Table 3
- Pool size sensitivity (plan_019) — Table 9
- UniXcoder 3-seed (plan_020) — Table 4
- D062 checkpoint criterion (d062_checkpoint_criterion) — Table 10
- SWE-bench OOD (plan_003) — Limitations section

## Your Review Task

Produce a structured review with:
1. **Summary** (2-3 sentences)
2. **Strengths** (bulleted, focus on experimental design, statistical rigor, ablation coverage)
3. **Weaknesses** (bulleted, focus on methodological concerns, missing experiments, statistical issues, reproducibility)
4. **Questions for Authors** (numbered)
5. **Minor Issues** (if any)
6. **Overall Score** (1-6) with 1-sentence justification
7. **Confidence** (1-5)

Be rigorous but fair. Think about: effect size magnitude, statistical power with 3 seeds, potential confounds, generalizability beyond 2 encoders, whether the query-split methodology is properly validated, whether the CoCoHaNeRe refutation is convincing, and experiment coverage gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "8f59496e-6cd4-4a21-86c2-f934621f97f4",
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

_source line 2 · 2026-05-16T16:03:26.894Z_

```json
{
  "parentUuid": "8f59496e-6cd4-4a21-86c2-f934621f97f4",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
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
  "uuid": "57753f95-4e6a-4d75-bd19-e51469e41305",
  "timestamp": "2026-05-16T16:03:26.894Z",
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

_source line 3 · 2026-05-16T16:03:29.723Z_



I'll start by reading the paper and any available artifacts to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57753f95-4e6a-4d75-bd19-e51469e41305",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6Xixwee9gYfMGQdVxAU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "332ab9b2-455c-45c2-b4a6-4411ddeef731",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pk85BPUdKb5P9H6BZH5797",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14736,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14736,
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

_source line 4 · 2026-05-16T16:03:30.186Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KjiPpiGW5fWrj3pjhtuZca`</summary>

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
  "parentUuid": "332ab9b2-455c-45c2-b4a6-4411ddeef731",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6Xixwee9gYfMGQdVxAU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0450dba4-24a0-4ed2-a138-453cc2ffa85e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pk85BPUdKb5P9H6BZH5797",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14736,
      "cache_read_input_tokens": 0,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14736
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 14736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14736,
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

_source line 5 · 2026-05-16T16:03:30.190Z_

<details><summary>↩ Tool result · `toolu_01KjiPpiGW5fWrj3pjhtuZca`</summary>

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
  "parentUuid": "0450dba4-24a0-4ed2-a138-453cc2ffa85e",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "db68fef7-f999-4147-bfd3-e707030a62f6",
  "sourceToolAssistantUUID": "0450dba4-24a0-4ed2-a138-453cc2ffa85e",
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

_source line 6 · 2026-05-16T16:03:32.952Z_



Let me read the paper and supporting materials to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db68fef7-f999-4147-bfd3-e707030a62f6",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XjDBuKRjWQ3EiDgkCH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f9447db-cbef-4c00-9c26-5ab4f38ac377",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsFpecDDwWKcfb86amb8zM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 14736,
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

_source line 7 · 2026-05-16T16:03:33.468Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_017MuuQaWphzpo8ZAnSVtXD1`</summary>

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
  "parentUuid": "2f9447db-cbef-4c00-9c26-5ab4f38ac377",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XjDBuKRjWQ3EiDgkCH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5441a120-8118-447b-a8d6-7dfca0c004ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsFpecDDwWKcfb86amb8zM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 14736,
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

_source line 8 · 2026-05-16T16:03:33.619Z_

<details><summary>↩ Tool result · `toolu_017MuuQaWphzpo8ZAnSVtXD1`</summary>

```text
{"result":"# 项目 structfuse-context 概况\n\n## 实验状态 (43 个)\n\n- **p2b_eval_4runs_pool50**: DONE (success) — \n- **d007_50repo_overlap**: DONE (success) — \n- **p2b_5reruns**: DONE (success) — \n- **p2b_eval_4runs_v2**: DONE (success) — \n- **p2b-all-9runs**: DONE (killed) — \n- **p2b-smoke8**: DONE (killed) — \n- **p2b-smoke7**: DONE (killed) — \n- **p2b-smoke6**: DONE (killed) — \n- **p2b-smoke5**: DONE (killed) — \n- **p2b-smoke4**: DONE (killed) — \n- **p2b-smoke3**: DONE (killed) — \n- **p2b-smoke2**: DONE (killed) — \n- **p2b-smoke-test**: DONE (killed) — \n- **mvp_p2a_linear_proxy**: DONE (success) — \n- **mvp_p1_codeql_feasibility**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| unixcoder-3strat-s43 | UniXcoder-base s43: 3 strategies (random/embedding/dataflow) × seed 43, patience=2。与 s42 (patience=3) 构成 2-seed 统计，验证 null result 稳定性。Director D064 批准。 | — | — | — |\n| m2_full_starcoder_resumed | M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。 | — | — | — |\n| m2_full_qwen_continued | M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。 | — | — | — |\n\n## 待处理\n- plan_018_bm25: BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。（排队等待 GPU）\n- plan_015_dynamic: Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen, s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。（排队等待 GPU）\n- plan_005_stratified: Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制 pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。（准备中）\n- unixcoder-3strat-s44: UniXcoder-base s44: 3 strategies (random/embedding/dataflow) × seed 44, patience=2。与 s42/s43 构成 3-seed 统计，确认 encoder-only/small-scale null result。Director D064 批准。（准备中）\n- qwen_random_s42_retrain: Qwen random_s42 重训（统一 regime: 2 epoch + early_stopping_patience=2）。原 s42 用 3 epoch + patience=0 导致 pool=50 R@1 异常低（0.2730 vs s43=0.3138/s44=0.3181），不可纳入 cross-seed 统计。重训后可补完 3-seed comparison。Director 批准方案 B。（准备中）\n\n## 近期结论\n- **unixcoder-3strat-s42** (negative): UniXcoder-base (125M, encoder-only RoBERTa) 第三 encoder: 3 strategies (random/embedding/dataflow) × seed 42。验证 embedding distance mining 优势是否跨架构泛化（encoder-only vs decoder-only）。batch_size=16, max_seq_length=1024, LoRA, gradient-checkpointing。\n- **unixcoder_3strat_s42** (failed): UniXcoder-base 第三 encoder: 3 strategies (random/embedding/dataflow) × seed 42。验证 embedding distance mining 优势是否跨架构泛化（RoBERTa vs decoder-only）。\n- **m1_reextract_v2** (success): M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 ← 基于 m1_extraction\n\n## 趋势\n成功 12 / 负向 3 / 失败 5 / 共 34\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb1-42106: 无 GPU 信息\n\n## 告警\n- p2b-smoke-test: 已被终止 — unknown\n- p2b-smoke2: 已被终止 — unknown\n- p2b-smoke3: 已被终止 — unknown\n- p2b-smoke4: 已被终止 — unknown\n- p2b-smoke5: 已被终止 — unknown\n- p2b-smoke6: 已被终止 — unknown\n- p2b-smoke7: 已被终止 — unknown\n- p2b-smoke8: 已被终止 — unknown\n- p2b-all-9runs: 已被终止 — unknown\n- mvp_p2b_contrastive_training: 已被终止 — unknown\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\n- p2b_eval_all: 已被终"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5441a120-8118-447b-a8d6-7dfca0c004ba",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "5a9a0c2c-ac77-4510-b064-500d293e9eb4",
  "sourceToolAssistantUUID": "5441a120-8118-447b-a8d6-7dfca0c004ba",
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

_source line 9 · 2026-05-16T16:03:33.817Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NF2bjNUKMhspNJyHg6CBYZ`</summary>

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
  "parentUuid": "5a9a0c2c-ac77-4510-b064-500d293e9eb4",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XjDBuKRjWQ3EiDgkCH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ce91bfa-e3c3-465a-9b34-86c895bc3d22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsFpecDDwWKcfb86amb8zM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 14736,
      "output_tokens": 176,
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
          "output_tokens": 176,
          "cache_read_input_tokens": 14736,
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

_source line 10 · 2026-05-16T16:03:33.829Z_

<details><summary>↩ Tool result · `toolu_01NF2bjNUKMhspNJyHg6CBYZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| unixcoder-3strat-s43 | UniXcoder-base s43: 3 strategies (random/embedding/dataflow) × seed 43, patience=2。与 s42 (patience=3) 构成 2-seed 统计，验证 null result 稳定性。Director D064 批准。 | — | — | — |\\n| m2_full_starcoder_resumed | M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。 | — | — | — |\\n| m2_full_qwen_continued | M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。 | — | — | — |\\n\\n## 待处理\\n- plan_018_bm25: BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。（排队等待 GPU）\\n- plan_015_dynamic: Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen, s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。（排队等待 GPU）\\n- plan_005_stratified: Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制 pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。（准备中）\\n- unixcoder-3strat-s44: UniXcoder-base s44: 3 strategies (random/embedding/dataflow) × seed 44, patience=2。与 s42/s43 构成 3-seed 统计，确认 encoder-only/small-scale null result。Director D064 批准。（准备中）\\n- qwen_random_s42_retrain: Qwen random_s42 重训（统一 regime: 2 epoch + early_stopping_patience=2）。原 s42 用 3 epoch + patience=0 导致 pool=50 R@1 异常低（0.2730 vs s43=0.3138/s44=0.3181），不可纳入 cross-seed 统计。重训后可补完 3-seed comparison。Director 批准方案 B。（准备中）\\n\\n## 近期结论\\n- **unixcoder-3strat-s42** (negative): UniXcoder-base (125M, encoder-only RoBERTa) 第三 encoder: 3 strategies (random/embedding/dataflow) × seed 42。验证 embedding distance mining 优势是否跨架构泛化（encoder-only vs decoder-only）。batch_size=16, max_seq_length=1024, LoRA, gradient-checkpointing。\\n- **unixcoder_3strat_s42** (failed): UniXcoder-base 第三 encoder: 3 strategies (random/embedding/dataflow) × seed 42。验证 embedding distance mining 优势是否跨架构泛化（RoBERTa vs decoder-only）。\\n- **m1_reextract_v2** (success): M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 ← 基于 m1_extraction\\n\\n## 趋势\\n成功 12 / 负向 3 / 失败 5 / 共 34\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-42106: 无 GPU 信息\\n\\n## 告警\\n- p2b-smoke-test: 已被终止 — unknown\\n- p2b-smoke2: 已被终止 — unknown\\n- p2b-smoke3: 已被终止 — unknown\\n- p2b-smoke4: 已被终止 — unknown\\n- p2b-smoke5: 已被终止 — unknown\\n- p2b-smoke6: 已被终止 — unknown\\n- p2b-smoke7: 已被终止 — unknown\\n- p2b-smoke8: 已被终止 — unknown\\n- p2b-all-9runs: 已被终止 — unknown\\n- mvp_p2b_contrastive_training: 已被终止 — unknown\\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\\n- p2b_eval_all: 已被终止 — unknown\\n- m2_early_pilot: 已被终止 — unknown\\n- m2_early_pilot_v2: 训练失败 — unknown\\n- m2_early_pilot_v3: 已被终止 — unknown\\n- m2_full_starcoder: 训练失败 — unknown\\n- m1_reextract: 训练失败 — unknown\\n- plan_003_swebench_eval: 训练失败 — unknown\\n- unixcoder_3strat_s42: 训练失败 — unknown\\n\", \"total_chars\": 3264, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ce91bfa-e3c3-465a-9b34-86c895bc3d22",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "7c9e91f7-82ab-47fc-aa93-da9b5c730d77",
  "sourceToolAssistantUUID": "4ce91bfa-e3c3-465a-9b34-86c895bc3d22",
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

_source line 11 · 2026-05-16T16:03:36.889Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JyTMMj4F1JfAbyqGyHriSH`</summary>

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
  "parentUuid": "7c9e91f7-82ab-47fc-aa93-da9b5c730d77",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XjUi3vYgkux1upYbV2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5d6f7a7-5739-44e8-87e2-8ed1671a2c90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHxARYaM8NwcprmQJKnVLg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4120,
      "cache_read_input_tokens": 16183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4120,
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

_source line 12 · 2026-05-16T16:03:36.899Z_

<details><summary>↩ Tool result · `toolu_01JyTMMj4F1JfAbyqGyHriSH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\n\\n- **Headline result template**: \\\"Simple static embedding-distance mining improves code retrieval in pilot and initial M2 seed (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; consistency across remaining seeds pending; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective.\\\"\\n\\n## Core Insight\\n\\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\n- Backup: \\\"Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### Evidence presentation strategy:\\n- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)\\n- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)\\n- Both metrics show directionally consistent results; no goalpost-moving between metrics\\n\\n### In progress:\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 DONE (R@1=0.6009, early stopped step 500), embedding_distance_s43 DONE (R@1=0.5606, early stopped step 1500). 4/9 runs complete, ~35h remaining.\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\n- m1_reextract_v2: 90.5% complete (25,582/28,276), 0 ERROR, ETA ~19:00 CST May 15\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Limitations\\n\\nEffect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"Simple embedding mining provides reliable zero-cost improvement + CodeQL extraction is practical + representation geometry analysis may help explain prior contradictions\\\"\\n- Still publishable: reliable zero-cost baseline demonstration + mechanistic analysis is sufficient for EMNLP Main\\n\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the narrative positioning needs adjustment\\n- Pivot: \\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps, establishing it as a reliable zero-cost baseline even when BM25 provides no signal\\\"\\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining provides reliable improvement) stands regardless of BM25 outcome\\n- Claim 1 core preserved: \\\"Simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling\\\"\\n- Impact: BM25 result determines narrative nuance, not core contribution\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\\n&lt;!-- D041 formal definition fix: reachable_G → ¬reachable_G, 2026-05-15 -->\\n&lt;!-- Claim 2 exploratory wording unification: 2026-05-15 -->\\n&lt;!-- D049 Claim 1 framing update: numbers, narrative softening, evidence strategy, limitations: 2026-05-15 -->\\n&lt;!-- Status data refresh: s44 DONE, 4/9 runs, m1 90.5%, headline caveat: 2026-05-15 -->\\n\", \"total_chars\": 14424, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5d6f7a7-5739-44e8-87e2-8ed1671a2c90",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "b689657d-7a85-460d-86e9-70325b63bd48",
  "sourceToolAssistantUUID": "a5d6f7a7-5739-44e8-87e2-8ed1671a2c90",
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

_source line 13 · 2026-05-16T16:03:37.364Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Vka7YctUJi7ftcNNBrY7Mf`</summary>

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
  "parentUuid": "b689657d-7a85-460d-86e9-70325b63bd48",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XjUi3vYgkux1upYbV2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4684b716-9e86-40eb-8424-0cb3d42b6824",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHxARYaM8NwcprmQJKnVLg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4120,
      "cache_read_input_tokens": 16183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4120,
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

_source line 14 · 2026-05-16T16:03:37.375Z_

<details><summary>↩ Tool result · `toolu_01Vka7YctUJi7ftcNNBrY7Mf`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/ROADMAP.md\", \"content\": \"# StructFuse — Research Dashboard\\n\\n> 最后更新: 2026-05-16 06:33 UTC | 更新原因: Reviewer 修正：pool=8→pool=50 数据、标注 D061 superseded、补充遗漏风险\\n\\n## 核心方向\\nHard negative mining strategy comparison for contrastive code retrieval: random vs embedding_distance vs dataflow_aware vs BM25, across 3 encoder architectures. Dual-track narrative (D059): A=stratified heterogeneity reveals when mining helps, B=explain why aggregate deltas are small. 详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（post-MVP）+ 审稿进行中\\n- **Qwen (cuda:0)**: 主链完成中，watcher PID 966920 就绪 → 自动触发 s42 supplement (embed+dataflow+bm25)\\n- **StarCoder (cuda:1)**: embedding_s42 之后还有 embed_s43/s44 + dataflow×3。ETA ~May 19-20\\n- **UniXcoder**: 3-strat s42 训练中（PID 149872, step 400+, R@1@200=0.5245）。Registry 待修复为 RUNNING\\n- **BM25 Phase 1**: ✅ 已完成（索引+挖掘）。Phase 2 watcher 就绪\\n- **D062 query split**: Workers 失败两次（rate/context limit），待重派。**阻塞 Claim 2 全部进展**\\n- **写作**: Intro/Method/Related/Conclusion v1 ✅ | Abstract v2 + Experiments v1 修复中\\n\\n## ⚠️ Claim 1 Delta 状况 — Pool=50 数据（D060 确认 pool=8 不可靠）\\n| seed | checkpoint | random R@1 | embed R@1 | Δ |\\n|------|-----------|-----------|-----------|---|\\n| s43 | by_val_loss | 0.3138 | 0.3331 | **+1.93pp** ✓ |\\n| s44 | by_val_loss | 0.3181 | 0.3694 | **+5.13pp** ��� |\\n| s43 | by_R@1 | 0.3829 | 0.3897 | +0.68pp |\\n| s44 | by_R@1 | 0.3181 | 0.3171 | -0.10pp |\\n| s42 | — | — | **缺失** | — |\\n\\n- **by_val_loss 下两 seed 均 embed > random**，信号正面\\n- **Checkpoint 选择标准是核心方法论问题**：D061 (统一 val_loss) 已被 D062 (query split) supersede\\n- **翻盘路径**: D062 实现 → 统一 checkpoint selection → embed_s42 补完 → bootstrap CI\\n\\n## 实验缺口补充计划 (D063, May 16)\\n| Priority | 实验 | 耗时 | 状态 | 触发条件 |\\n|----------|------|------|------|----------|\\n| **P0** | D062 pool=50 re-eval (query split) | 2h | **Worker 失败×2，重派中** | 立即 |\\n| **P0** | RepoBench-R eval (plan_004) | 5h | 就绪 | 立即启动 |\\n| **P0** | Pool sensitivity (plan_019) | 5h | 就绪 | 立即启动 |\\n| **P0** | BM25 Phase 2 训练 (plan_018) | 15h | Watcher 就绪 | Qwen/SC 完成后自动 |\\n| **P0** | 分层分析 (plan_005) | 分析 | 就绪 | D062 pool=50 后 |\\n| **P1** | UniXcoder multi-seed (s43, s44) | 20h | 新增 plan_020 | s42 完成后 |\\n| **P1** | 温度 ablation 缩减 (τ=0.05,0.2 × Qwen) | 15h | 新增 plan_021 | GPU 空闲时 |\\n| **P1** | random_s42 retrain (统一 regime) | 10h | 已派 Agent | — |\\n\\n## 时间预算\\n- **bjb1-42106**: 2× RTX PRO 6000 96GB\\n- **可用**: 9天 × 24h × 2GPU = 432 GPU·h\\n- **已占用**: ~100h (运行中训练)\\n- **新增 must-do**: ~42h | should-do: ~35h\\n- **总计 ~177h，余量充足**\\n\\n## 关键路径\\n```\\nQwen主链完成 → s42 supplement (18h) → BM25 P2 自动触发\\n              ↘ pool=50 re-eval → stratified analysis + bootstrap CI\\nD062 修复 → pool=50 query split 实现 ↗\\nRepoBench-R + Pool sensitivity → 立即并行启动（用已有 checkpoint）\\nUniXcoder s42 完成 → s43/s44 → 跨架构统计\\nStarCoder chain → May 19-20 全部完成\\n```\\n\\n## 近期任务\\n- [ ] **D062 重派 Worker**（已失败两次，阻塞 Claim 2）\\n- [ ] RepoBench-R 立即启动（已有 Qwen s42/s43/s44 checkpoints）\\n- [ ] Pool sensitivity 立即启动\\n- [ ] UniXcoder registry 修复为 RUNNING\\n- [ ] Qwen 主链完成 → 验证 watcher 触发 supplement\\n- [ ] random_s42 retrain（已在 Agent 队列）\\n- [ ] Qwen 全量完成后 → D062 pool=50 + stratified + bootstrap CI\\n- [ ] 温度 ablation 缩减版排期\\n\\n## 覆盖率\\n- Claim 1: pool=50 eval 已跑部分（Qwen 12 ckpt + StarCoder 8 ckpt），但 D062 query split 未实现前数据不能作为最终结论\\n- Claim 2: **0/3 done** — plan_005 blocked on D062。⚠️ 这是 dual-track B 的核心，完全无定量数据\\n- Claim 3: 1/1 done ✅\\n\\n## 关键风险\\n1. **D062 连续失败**: 阻塞 checkpoint selection + Claim 2 stratified analysis + bootstrap CI——整条 post-M2 分析链\\n2. **StarCoder embedding < random (pool=50 确认, -1.9pp)**: Claim 1 跨架构泛化受挑战。Paper 需 qualify 为 encoder-dependent 或靠 UniXcoder 扳回\\n3. **Checkpoint 选择标准矛盾**: val_loss vs pool=8 R@1 给出相反结论，D062 (query split) 是唯一可靠解法\\n4. **Claim 2 覆盖率 0%**: Dual-track narrative B 支柱完全无实验数据，plan_005 + neg_difficulty 分析全部依赖 D062\\n5. **UniXcoder 只有 1 seed**: 无法做统计检验，需补 s43/s44（plan_020）\\n6. **ARR May 25**: 9 天完成所有补充实验 + 论文定稿\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D066 | 2026-05-16 | D066: D062 eval 8/14 失败（adapter format bug），16.3pp | d062_qwen_query_split_eval |\\n| D065 | 2026-05-16 | D065: Checkpoint selection criterion effect (+16.3 | d062_qwen_query_split_eval |\\n| D064 | 2026-05-16 | D064: UniXcoder s42 null result (Δ<0.4pp) 支撑 Track | unixcoder_3strat_s42, plan_020 |\\n| D063 | 2026-05-16 | D063: 实验缺口补充——新增 plan_020 (UniXcoder multi-seed) + | plan_020, plan_021, plan_004, plan_019 |\\n| D062 | 2026-05-16 | D062: Checkpoint 选择采用方案 2——从 2980 val queries 分出 5 | m2_full_qwen_continued, plan_005_stratified |\\n| D061 | 2026-05-16 | D061: pool=50 eval 首批结果——统一用 best_by_val_loss 选 ch | m2_full_qwen_continued, m2_full_starcoder_resumed |\\n| D060 | 2026-05-16 | D060: in-training eval R@1 不可靠（val negative 非确定性 ± | m2_full_qwen_continued, plan_005_stratified |\\n| D059 | 2026-05-15 | 确认 A/B 双轨叙事策略：A=stratified 揭示异质性，B=B1+Claim2 hybri | m2_full_qwen_continued, m2_full_starcoder_resumed, plan_005_stratified |\\n| D058 | 2026-05-15 | D057 trajectory 发现重新定位：从 Claim 2 evidence 降级为 §4.3 | m2_full_qwen_continued |\\n| D057 | 2026-05-15 | embed_s44 展示 R@1/val_loss 指标分歧：R@1 峰值 step 500 而 v | m2_full_qwen_continued |\\n\\n\", \"total_chars\": 4966, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4684b716-9e86-40eb-8424-0cb3d42b6824",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "8891a47b-2e56-4c95-84d4-509063c8a981",
  "sourceToolAssistantUUID": "4684b716-9e86-40eb-8424-0cb3d42b6824",
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

_source line 15 · 2026-05-16T16:03:37.927Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0194ghL35XipuijNNibF4WAz`</summary>

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
  "parentUuid": "8891a47b-2e56-4c95-84d4-509063c8a981",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XjUi3vYgkux1upYbV2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "561a227f-9479-4b98-94ff-250bc1133e46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHxARYaM8NwcprmQJKnVLg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4120,
      "cache_read_input_tokens": 16183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4120,
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

_source line 16 · 2026-05-16T16:03:38.236Z_

<details><summary>↩ Tool result · `toolu_0194ghL35XipuijNNibF4WAz`</summary>

```text
Error: result (55,327 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/98678e1d-9307-4b37-b78e-c6727fde8087/tool-results/mcp-agent-ml-research-read_project_file-1778947418221.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/98678e1d-9307-4b37-b78e-c6727fde8087/tool-results/mcp-agent-ml-research-read_project_file-1778947418221.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/98678e1d-9307-4b37-b78e-c6727fde8087/tool-results/mcp-agent-ml-research-read_project_file-1778947418221.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "561a227f-9479-4b98-94ff-250bc1133e46",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "0722c228-100d-46ae-88d2-14892b2c6984",
  "sourceToolAssistantUUID": "561a227f-9479-4b98-94ff-250bc1133e46",
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

_source line 17 · 2026-05-16T16:03:41.212Z_

Let me now look at the paper artifacts and the writing plan.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0722c228-100d-46ae-88d2-14892b2c6984",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XjoRBwtx7BKy7xk7h1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "313a2ba1-e509-46a2-b82e-9e729b4e7804",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114YD1wuooZuzFBMD2XENeB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7830,
      "cache_read_input_tokens": 20303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7830,
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

_source line 18 · 2026-05-16T16:03:42.203Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XPeEU7AicyQeBKkvgJG4kR`</summary>

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
  "parentUuid": "313a2ba1-e509-46a2-b82e-9e729b4e7804",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XjoRBwtx7BKy7xk7h1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74e42e8b-ff5c-465e-8a7f-4ac71b4e84eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114YD1wuooZuzFBMD2XENeB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7830,
      "cache_read_input_tokens": 20303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7830,
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

_source line 19 · 2026-05-16T16:03:42.214Z_

<details><summary>↩ Tool result · `toolu_01XPeEU7AicyQeBKkvgJG4kR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/writing_plan.yaml\", \"content\": \"# writing_plan.yaml — StructFuse EMNLP 2026 ARR May 25\\n# Generated: 2026-05-16\\n# Mode: Pre-Draft (dual-version skeleton)\\n# Status: PENDING_DIRECTOR_APPROVAL\\n\\nmeta:\\n  venue: \\\"EMNLP 2026 Main (ARR May 25)\\\"\\n  template: \\\"acl2023\\\"  # ARR uses ACL format\\n  template_note: \\\"Using acl2023.sty; will verify latest ARR template\\\"\\n  page_limit: 8  # + unlimited appendix\\n  dual_version: true\\n  version_decision_blocked_on: \\\"D062 full results (14/14 evals)\\\"\\n\\n# ============================================================\\n# DUAL-VERSION TITLES\\n# ============================================================\\ntitles:\\n  version_a:\\n    title: \\\"What Really Matters in Hard Negative Evaluation? Checkpoint Selection Dominates Strategy Choice for Code Retrieval\\\"\\n    subtitle_claim: \\\"Checkpoint criterion is the dominant factor; strategy effect is secondary\\\"\\n  version_b:\\n    title: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Evaluation Methodology\\\"\\n    subtitle_claim: \\\"Embedding mining works + dual methodology contribution (mining + eval protocol)\\\"\\n\\n# ============================================================\\n# PAPER OUTLINE\\n# ============================================================\\npaper_outline:\\n  abstract:\\n    word_budget: 250\\n    shared: false  # diverges between versions\\n    version_a_focus: \\\"Checkpoint selection criterion dominates (+16.3pp) > strategy choice. Proper evaluation protocol reveals marginal but consistent embedding benefit.\\\"\\n    version_b_focus: \\\"Embedding mining improves by Xpp at realistic pool size. Effect was masked by small-pool eval and inappropriate checkpoint selection.\\\"\\n    dependencies: [experiments, methodology]\\n\\n  introduction:\\n    word_budget: 900\\n    shared: true  # problem setup and motivation identical\\n    content: |\\n      P1: Problem — repo-level file retrieval, importance of negatives\\n      P2: Prior work contradiction — CoCoHaNeRe says embedding negatives harmful; our question\\n      P3: Structural information in code — unique dimension absent in NL\\n      P4: Methodology gap — prior eval uses small fixed pools, unclear checkpoint criteria\\n      P5: Our contribution (DIVERGES at this paragraph)\\n    diverge_at: \\\"P5 contribution list\\\"\\n    version_a_p5: \\\"Three contributions: (1) identify checkpoint criterion as dominant factor, (2) query-split eval protocol, (3) embedding mining as marginal-but-consistent baseline\\\"\\n    version_b_p5: \\\"Three contributions: (1) embedding mining improves at realistic pool sizes, (2) query-split eval protocol + checkpoint criterion analysis, (3) CodeQL pipeline\\\"\\n    dependencies: []\\n\\n  related_work:\\n    word_budget: 800\\n    shared: true  # identical across versions\\n    subsections:\\n      - \\\"2.1 Dense Retrieval for Code\\\"\\n      - \\\"2.2 Contrastive Learning and Hard Negative Mining\\\"\\n      - \\\"2.3 Evaluation Methodology for Dense Retrieval\\\"  # NEW — checkpoint selection, pool size, query splits\\n      - \\\"2.4 Code Structure in Machine Learning\\\"\\n    dependencies: []\\n\\n  methodology:\\n    word_budget: 1200\\n    shared: true  # identical across versions\\n    subsections:\\n      - \\\"3.1 Problem Formulation (InfoNCE, contrastive setup)\\\"\\n      - \\\"3.2 Negative Mining Strategies (random, embedding-distance, dataflow-aware, BM25)\\\"\\n      - \\\"3.3 Structural Extraction Pipeline (CodeQL 2-hop, beniget fallback)\\\"\\n      - \\\"3.4 Training Setup (3 encoders, LoRA, hyperparams)\\\"\\n      - \\\"3.5 Query-Split Evaluation Protocol\\\"  # NEW — D062 methodology\\n    new_subsection_3_5:\\n      content: |\\n        - Motivation: standard pool-based eval (pool=50, random negatives) inflates R@1 and compresses strategy differences\\n        - Query-split protocol: hold out queries (not just shuffle negatives), evaluate at realistic pool sizes {50, 200, 500}\\n        - Checkpoint selection: compare best_by_val_loss vs best_by_R@1 — measure criterion effect\\n        - Claim: this protocol reveals effects masked by standard small-pool eval\\n      data_source: \\\"D062 methodology + registry d062_analysis\\\"\\n    dependencies: []\\n\\n  experiments:\\n    word_budget: 2000\\n    shared: false  # structure shared but emphasis diverges\\n    subsections:\\n      - \\\"4.1 Experimental Setup (dataset, encoders, training details)\\\"\\n      - \\\"4.2 Main Results (DIVERGES)\\\"\\n      - \\\"4.3 Analysis\\\"\\n    subsection_4_2:\\n      shared_elements:\\n        - \\\"Table 1: Strategy × Criterion × Encoder results at pool-50 (training eval)\\\"\\n        - \\\"Table 2: Strategy × Criterion × Encoder at realistic pool sizes (D062 query-split)\\\"\\n      version_a_emphasis: |\\n        Lead with Table 2 criterion effect (+16.3pp). Strategy effect shown as secondary.\\n        Narrative: \\\"Criterion dominates. Within proper criterion, embedding shows X.Xpp.\\\"\\n      version_b_emphasis: |\\n        Lead with Table 2 strategy effect at realistic pool + proper criterion.\\n        Narrative: \\\"Embedding improves by X.Xpp. This was masked by wrong criterion choice.\\\"\\n    subsection_4_3:\\n      shared:\\n        - \\\"4.3.1 Checkpoint Selection Criterion (criterion effect quantification)\\\"\\n        - \\\"4.3.2 Pool Size Sensitivity\\\"\\n        - \\\"4.3.3 Training Dynamics (decay rate, loss-R@1 divergence)\\\"\\n        - \\\"4.3.4 Negative Difficulty Analysis (representation geometry)\\\"\\n        - \\\"4.3.5 Cross-Encoder Comparison (Qwen vs StarCoder vs UniXcoder)\\\"\\n      version_a_additions:\\n        - \\\"4.3.6 When Does Strategy Matter? (conditional analysis: criterion-controlled strategy effect)\\\"\\n      version_b_additions:\\n        - \\\"4.3.6 BM25 Comparison (plan_018 results)\\\"\\n    dependencies: [methodology]\\n\\n  discussion:\\n    word_budget: 800\\n    shared: true  # mostly shared, minor emphasis difference\\n    subsections:\\n      - \\\"5.1 Relationship to Inference-Time Graph Methods\\\"\\n      - \\\"5.2 Representation Geometry (exploratory)\\\"\\n      - \\\"5.3 Implications for Evaluation Practice\\\"  # NEW for both versions\\n      - \\\"5.4 Limitations\\\"\\n    dependencies: [experiments]\\n\\n  conclusion:\\n    word_budget: 250\\n    shared: false\\n    version_a_focus: \\\"Criterion > strategy. Practical recommendation: always use best_by_R@1 + query-split eval. Embedding mining provides marginal consistent benefit.\\\"\\n    version_b_focus: \\\"Embedding mining works when properly evaluated. Dual methodology: mining strategy + eval protocol. Query-split eval as community recommendation.\\\"\\n    dependencies: [experiments, discussion]\\n\\n# ============================================================\\n# VISUALIZATION PLAN\\n# ============================================================\\nvisualization_plan:\\n  - fig_id: fig1_pipeline\\n    type: schematic\\n    tool: matplotlib\\n    description: \\\"Pipeline overview — input → CodeQL extraction → 4 strategies → contrastive training → encoder\\\"\\n    placement: \\\"§1 or §3\\\"\\n    aspect_ratio: \\\"7x2.8\\\"\\n    data_source: \\\"static (no data needed)\\\"\\n    status: DONE  # already generated\\n\\n  - fig_id: fig2_mining_strategies\\n    type: schematic\\n    tool: matplotlib\\n    description: \\\"3-panel strategy comparison on mini-repo graph\\\"\\n    placement: \\\"§3.2\\\"\\n    aspect_ratio: \\\"7x3\\\"\\n    data_source: \\\"static\\\"\\n    status: DONE\\n\\n  - fig_id: fig3_criterion_effect\\n    type: bar_chart\\n    tool: matplotlib\\n    description: \\\"Grouped bar: R@1 by strategy, split by criterion (best_by_loss vs best_by_R@1). Shows criterion effect >> strategy effect.\\\"\\n    placement: \\\"§4.2 or §4.3.1\\\"\\n    aspect_ratio: \\\"5x3.5\\\"\\n    data_source: \\\"registry: D062 query-split results\\\"\\n    status: TBD  # blocked on D062 completion\\n\\n  - fig_id: fig4_rep_geometry\\n    type: statistical\\n    tool: matplotlib\\n    description: \\\"2-panel: margin comparison + similarity distribution across encoders\\\"\\n    placement: \\\"§4.3.4\\\"\\n    aspect_ratio: \\\"7x3\\\"\\n    data_source: \\\"registry: neg_difficulty_analysis\\\"\\n    status: DONE\\n\\n  - fig_id: fig5_pool_sensitivity\\n    type: line_chart\\n    tool: matplotlib\\n    description: \\\"R@1 vs pool size {50, 200, 500} by strategy × criterion\\\"\\n    placement: \\\"§4.3.2\\\"\\n    aspect_ratio: \\\"5x3.5\\\"\\n    data_source: \\\"registry: D062 pool-size sweep\\\"\\n    status: TBD\\n\\n  - fig_id: fig6_training_dynamics\\n    type: line_chart\\n    tool: matplotlib\\n    description: \\\"Validation R@1 trajectories across strategies (Qwen s44 illustrative + aggregated)\\\"\\n    placement: \\\"§4.3.3\\\"\\n    aspect_ratio: \\\"5x3.5\\\"\\n    data_source: \\\"registry: m2_full_qwen_continued step-by-step metrics\\\"\\n    status: TBD\\n\\n# ============================================================\\n# TABLE PLAN\\n# ============================================================\\ntable_plan:\\n  - table_id: tab1_main_pool50\\n    type: results\\n    columns: [\\\"Strategy\\\", \\\"Criterion\\\", \\\"Qwen R@1\\\", \\\"StarCoder R@1\\\", \\\"UniXcoder R@1\\\"]\\n    data_source: \\\"registry: m2_full_qwen, m2_full_starcoder, unixcoder-3strat (mean±std, 3 seeds)\\\"\\n    placement: \\\"§4.2\\\"\\n    note: \\\"Standard pool-50 training eval. Shows strategy effect in controlled setting.\\\"\\n\\n  - table_id: tab2_query_split\\n    type: results\\n    columns: [\\\"Strategy\\\", \\\"Criterion\\\", \\\"Pool-50 R@1\\\", \\\"Pool-200 R@1\\\", \\\"Pool-500 R@1\\\"]\\n    data_source: \\\"registry: D062 query-split eval results\\\"\\n    placement: \\\"§4.2\\\"\\n    note: \\\"KEY TABLE. Shows criterion effect >> strategy at realistic pool sizes.\\\"\\n    status: TBD  # 6/14 complete\\n\\n  - table_id: tab3_criterion_effect\\n    type: analysis\\n    columns: [\\\"Encoder\\\", \\\"Criterion Effect (pp)\\\", \\\"Strategy Effect (pp)\\\", \\\"Ratio\\\"]\\n    data_source: \\\"D062 analysis output\\\"\\n    placement: \\\"§4.3.1\\\"\\n    note: \\\"Quantifies criterion vs strategy effect sizes.\\\"\\n\\n  - table_id: tab4_neg_difficulty\\n    type: analysis\\n    columns: [\\\"Strategy\\\", \\\"pos_sim\\\", \\\"neg_sim\\\", \\\"margin (Qwen)\\\", \\\"margin (StarCoder)\\\"]\\n    data_source: \\\"registry: neg_difficulty_analysis\\\"\\n    placement: \\\"§4.3.4\\\"\\n    status: DONE\\n\\n  - table_id: tab5_inference_comparison\\n    type: comparison\\n    columns: [\\\"Method\\\", \\\"Structure Phase\\\", \\\"Scope\\\", \\\"Graph Cost\\\", \\\"Complementary?\\\"]\\n    data_source: \\\"plan_017 literature survey\\\"\\n    placement: \\\"§5.1\\\"\\n    status: DONE\\n\\n  - table_id: tab6_extraction_stats\\n    type: descriptive\\n    columns: [\\\"Metric\\\", \\\"Value\\\"]\\n    data_source: \\\"registry: m1_extraction, m1_reextract_v2\\\"\\n    placement: \\\"§3.3 or Appendix\\\"\\n    status: DONE\\n\\n# ============================================================\\n# LITERATURE STRATEGY\\n# ============================================================\\nliterature_strategy:\\n  macro_context: \\\"Hard negative mining for contrastive retrieval; evaluation methodology for dense retrievers; code structure in ML\\\"\\n  citation_budget: 50\\n  micro_clusters:\\n    - cluster_name: \\\"hard_negative_mining\\\"\\n      target_count: 12\\n      must_cite: [\\\"karpukhin2020dpr\\\", \\\"xiong2021ance\\\", \\\"qu2021rocketqa\\\", \\\"zhan2021star\\\", \\\"fan2025cocohanere\\\", \\\"zeng2022cldrd\\\"]\\n    - cluster_name: \\\"code_retrieval\\\"\\n      target_count: 10\\n      must_cite: [\\\"reddy2025swerank\\\", \\\"xie2025swefixer\\\", \\\"zhang2024codesage\\\", \\\"li2022scoder\\\"]\\n    - cluster_name: \\\"contrastive_learning_code\\\"\\n      target_count: 8\\n      must_cite: [\\\"chen2020simclr\\\", \\\"jain2021contracode\\\", \\\"li2022coderetriever\\\", \\\"guo2021graphcodebert\\\"]\\n    - cluster_name: \\\"evaluation_methodology\\\"  # NEW cluster\\n      target_count: 6\\n      must_cite: []  # to be filled — checkpoint selection, pool size effects in IR\\n      search_queries: [\\\"checkpoint selection contrastive learning\\\", \\\"evaluation pool size dense retrieval\\\", \\\"query split evaluation protocol\\\"]\\n    - cluster_name: \\\"code_structure_ml\\\"\\n      target_count: 8\\n      must_cite: [\\\"avgustinov2016ql\\\", \\\"liu2025codexgraph\\\", \\\"shah2025ranger\\\", \\\"ouyang2025repograph\\\"]\\n    - cluster_name: \\\"pretrained_code_models\\\"\\n      target_count: 6\\n      must_cite: [\\\"hui2024qwen25coder\\\", \\\"lozhkov2024starcoder2\\\", \\\"feng2020codebert\\\", \\\"guo2022unixcoder\\\"]\\n\\n# ============================================================\\n# WRITING ORDER\\n# ============================================================\\nwriting_order:\\n  phase_1_shared:  # write immediately\\n    - \\\"methodology\\\"     # §3 — fully shared, all data available\\n    - \\\"related_work\\\"    # §2 — fully shared, need evaluation_methodology cluster fill\\n    - \\\"introduction\\\"    # §1 P1-P4 — shared problem setup\\n  phase_2_after_d062:  # write after D062 14/14 complete\\n    - \\\"experiments\\\"     # §4 — version-dependent emphasis\\n    - \\\"introduction_p5\\\" # §1 P5 — contribution list diverges\\n    - \\\"abstract\\\"        # depends on final results\\n    - \\\"conclusion\\\"      # depends on final results\\n  phase_3_refinement:\\n    - \\\"discussion\\\"      # §5 — mostly shared but needs final numbers\\n    - \\\"appendix\\\"        # supplementary tables, full training curves\\n\\n# ============================================================\\n# CONSTRAINTS\\n# ============================================================\\nconstraints:\\n  d051_stats: \\\"All results tables: mean ± std across 3 seeds. No single-seed cherry-picking.\\\"\\n  no_swebench: \\\"SWE-bench dropped (plan_003 failed: R@1=0.04 OOD). External validation via RepoBench-R.\\\"\\n  three_encoders: \\\"Qwen2.5-Coder-3B + StarCoder2-3B + UniXcoder-base (125M). Third encoder validates cross-architecture.\\\"\\n  query_split: \\\"D062 query-split eval is the primary evaluation protocol. Pool-50 training eval is supplementary.\\\"\\n  version_gate: \\\"Final version (A vs B) decided by Director after D062 14/14 complete.\\\"\\n\", \"total_chars\": 13063, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74e42e8b-ff5c-465e-8a7f-4ac71b4e84eb",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "d1f3fe05-77f5-4a7d-8f03-d58bc840157d",
  "sourceToolAssistantUUID": "74e42e8b-ff5c-465e-8a7f-4ac71b4e84eb",
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

_source line 20 · 2026-05-16T16:03:43.144Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GGPUT9sS7JkHvJmQKY28be`</summary>

```json
{
  "project": "structfuse-context",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1f3fe05-77f5-4a7d-8f03-d58bc840157d",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XjoRBwtx7BKy7xk7h1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4842b4b5-579a-4c17-b9b8-158971dc6af5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114YD1wuooZuzFBMD2XENeB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7830,
      "cache_read_input_tokens": 20303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7830,
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

_source line 21 · 2026-05-16T16:03:43.153Z_

<details><summary>↩ Tool result · `toolu_01GGPUT9sS7JkHvJmQKY28be`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4842b4b5-579a-4c17-b9b8-158971dc6af5",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "c9eddcb2-ada2-4614-9e1e-4aeb4c3b02b7",
  "sourceToolAssistantUUID": "4842b4b5-579a-4c17-b9b8-158971dc6af5",
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

_source line 22 · 2026-05-16T16:03:43.453Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KgTjD6JgnSKzZoMXCvzg2y`</summary>

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
  "parentUuid": "c9eddcb2-ada2-4614-9e1e-4aeb4c3b02b7",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XjoRBwtx7BKy7xk7h1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43db8dab-0d36-40b4-b574-c51ea6de79f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114YD1wuooZuzFBMD2XENeB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7830,
      "cache_read_input_tokens": 20303,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7830
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 304,
          "cache_read_input_tokens": 20303,
          "cache_creation_input_tokens": 7830,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7830,
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

_source line 23 · 2026-05-16T16:03:43.461Z_

<details><summary>↩ Tool result · `toolu_01KgTjD6JgnSKzZoMXCvzg2y`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43db8dab-0d36-40b4-b574-c51ea6de79f2",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "21e254e7-c646-46f2-ace2-0dd174a8373f",
  "sourceToolAssistantUUID": "43db8dab-0d36-40b4-b574-c51ea6de79f2",
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

_source line 24 · 2026-05-16T16:03:47.298Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019cEkpzNR8szFDJDUWSbfsp`</summary>

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
  "parentUuid": "21e254e7-c646-46f2-ace2-0dd174a8373f",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XkBwGW5Yh5oWTGvUCD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0723e148-e46a-44e3-a5ec-e6a7d9bceb92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NrdzbeRFEAFiWvVBxZd5UU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5349,
      "cache_read_input_tokens": 28133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5349,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 25 · 2026-05-16T16:03:47.308Z_

<details><summary>↩ Tool result · `toolu_019cEkpzNR8szFDJDUWSbfsp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献（全部已验证 2026-05-14）\\n\\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\")\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\\n---\\n\\n## D062 Checkpoint Criterion 效应（pool=50 独立验证, 2026-05-16）\\n\\n**重大发现**：D062 query split eval 的早期数据（random strategy, selection set 504q, pool=50）显示 checkpoint 选择标准对 R@1 的影响远超预期。\\n\\n| Seed | best_by_val_loss R@1 | best_by_recall_at_1 R@1 | Δ |\\n|------|---------------------|------------------------|---|\\n| s42 | 0.2302 | 0.2302 | 0pp (same ckpt, MD5 identical) |\\n| s43 | 0.3413 | **0.5040** | **+16.3pp** |\\n| s44 | 0.3532 | (pending) | — |\\n\\n**关键洞察**：\\n1. s43 的 criterion 差异 (+16.3pp) **远大于**任何 strategy 差异（之前最大观测 ~5pp）。Checkpoint 选择标准是 confound 的主要来源，不是 mining strategy。\\n2. 这直接验证了 D062 query split 方法论的必要性——必须用独立 selection set 选 checkpoint，否则 criterion 偏差会淹没 strategy 效应。\\n3. 之前 (2026-05-15) 基于 in-training eval (pool=8) 的 criterion 分析显示 mean delta 仅 +0.65pp，严重低估了真实效应。pool=50 独立 eval 揭示的 +16.3pp 说明 pool=8 噪声完全掩盖了 criterion 效应。\\n4. **论文影响**：D062 结果可能成为方法论贡献的一部分（checkpoint selection methodology），而不仅是消除 confound 的工具。\\n\\n**待补充**：embedding_distance 和 dataflow_aware 的 criterion 效应数据（D062 eval 6/14 完成中）。\\n\\n---\\n\\n## Checkpoint Criterion 与 K 分析 (2026-05-15)\\n\\n**Checkpoint 选择 criterion 分歧率**：4 个完成的 full M2 runs 中，2/4 (50%) val_loss 与 R@1 选中不同 checkpoint。\\n\\n**分歧 pattern**：\\n- Qwen s43: val_loss→step 500, R@1→step 1500, R@1 差 +1.97pp\\n- StarCoder s42: val_loss→step 1000, R@1→step 2500, R@1 差 +0.64pp\\n- Mean delta: +0.65pp (R@1 criterion 优于 val_loss criterion)\\n- StarCoder 步差更大（1500 步 vs 1000 步），与其 pretrained margin 更大的特性一致\\n\\n**论文写作决策**：主表报 best_by_R@1（target metric aligned），ablation 表展示两种 criterion 对比（D036 已决策 R@1 为 primary）。\\n\\n**K=7 无 ablation**：所有正式实验固定 K=7。合理性来源：(1) batch_size=8 对齐（1 positive + 7 negatives = 8）(2) DPR 等文献惯例 (3) K=7 negatives are randomly sampled from a pool of 50 strategy-specific candidates per query。K 敏感性列为 limitation/future work。\\n\\n---\\n\\n## In-Training Eval 噪声发现 (2026-05-16)\\n\\n**发现**：in-training eval R@1 有 **±0.5pp 噪声地板**，来源于 val set negative 随机采样。\\n\\n**根因**（代码审计确认）：\\n- `val_ds.__getitem__` 中 `random.shuffle(fallback)` 动态采样 negatives（train.py:109-110）\\n- `val_ds._negatives` 从未被填充（`refresh_negatives` 仅对 train_ds 调用）\\n- 全局 `random` 状态在训练中持续变化，每次 eval pass 的 negative 组合不同\\n- dataloader `shuffle=False`，问题不在 batch 顺序，在 negative 采样\\n\\n**证据**：embed_s43 同一模型权重（step 1500）两次 eval：R@1=0.5606 (periodic) vs 0.5655 (final) = 0.49pp 差异。val_loss 同理：0.4926 vs 0.4876。\\n\\n**影响**：\\n1. Claim 1 的 strategy delta（2-seed mean ≈ 0, 单 seed -0.67 ~ +0.52pp）与噪声**同量级**\\n2. in-training eval 不能可靠区分 strategies\\n3. **pool=50 post-hoc eval（negatives 预定义、确定性）是唯一可靠对比基础**\\n4. 论文不应基于 in-training eval 数值做 strategy ranking claim\\n\\n**修复建议**：eval 时固定 seed 或预写死 val negatives。当前已跑实验不需重跑（pool=50 re-eval 会修复）。\\n\\n---\\n\\n## UniXcoder Null Result (2026-05-16)\\n\\n**发现**：UniXcoder-base (125M, encoder-only RoBERTa) 3 strategies × seed 42，strategy differentiation 完全消失。\\n\\n| Strategy | R@1 (pool=8) | val_loss |\\n|----------|-------------|----------|\\n| random | 0.5534 | 0.4513 |\\n| embedding | 0.5497 | 0.4466 |\\n| dataflow | 0.5510 | 0.4628 |\\n\\nR@1 span 仅 0.37pp，三策略在噪声范围内无差异。\\n\\n**解释假设**：\\n1. **Model capacity**: 125M 参数可能不足以利用 hard negative 的细粒度结构信息。大模型 (3B Qwen/StarCoder) 有更多参数来编码 structural 差异。\\n2. **Representation space**: UniXcoder 的 pretrained representation 可能已经更 uniform（RoBERTa-based encoder vs decoder-only），hard negative 的 \\\"hardness\\\" 在其表征空间中差异更小。\\n3. **Training dynamics**: batch_size=16 + max_seq_length=1024（vs Qwen/StarCoder 的 batch=8 + seq=2048），可能改变了 InfoNCE loss 的梯度结构。\\n\\n**论文定位**：3 encoder × 3 seed 实验中，null only on encoder-only/small-scale → \\\"strategy differentiation is model-capacity dependent\\\"，支撑 Track A (stratified heterogeneity)。s43/s44 已启动，用于 3-seed 统计确认。\\n\\n**Regime 差异**：s42 patience=3, s43/s44 patience=2。Paper 中需标注。\\n\\n---\\n\\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\\n\\n**两层重叠率数据（注意区分）**：\\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\\n\\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\\n|------|-------------------|----------------|------------------|\\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\\n\\n**核心修正**：之前基于 87% 预测\\\"Phase 2 中 BM25 R@1 很可能接近 embedding\\\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\\n\\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\\n\\n---\\n\\n## hard_negative_mining.py vs build_m1_training_data.py 实现差异 [2026-05-15]\\n\\n**发现者**：Reviewer\\n**影响**：当前 M2 不受影响（用 pre-mined 数据），plan_015（dynamic negative mining）实施前必须对齐\\n\\n**差异**：\\n\\n### hard_negative_mining.py `DataFlowAwareMiner`（training/hard_negative_mining.py）\\n三步法：\\n1. **Embedding top-K**：调用 `EmbeddingDistanceMiner.mine()` 获取 top-50 cosine similarity 最高的 candidates（从所有 non-positive candidates 中）\\n2. **Dataflow filter**：过滤掉 `_is_reachable(query, fid)` 为 True 的文件——仅检查 `dataflow_graph[src]` 中的直接条目（1-hop 可达性）\\n3. **BM25 re-rank**：如果 `bm25_index` 可用，对剩余 disconnected candidates 按 BM25 分数降序重排\\n4. **Fallback**：如果 disconnected 不足 `num_negatives`，用 random padding 补足\\n\\n### build_m1_training_data.py `build_candidate_pools()`（scripts/build_m1_training_data.py）\\n两步法：\\n1. **Dataflow filter**：从 `non_pos_files` 中排除 `full_connected_set`（= `positive_files ∪ cg_connected`，即 dataflow 直连 + call graph 邻居——比 `DataFlowAwareMiner` 排除范围更广）\\n2. **BM25 sort**：对 disconnected 文件按 BM25 分数降序排序，取 top-K（pool_size=50）\\n3. **无 embedding 步骤**：dataflow pool 完全不使用 embedding 信号\\n\\n额外注意：当 `--model-path` 未提供时，`emb_scores = bm25`（line 317-318），此时 embedding pool 也退化为 BM25 排序，仅在是否排除 `full_connected` 上与 dataflow pool 不同。\\n\\n### 差异总结\\n\\n| 维度 | hard_negative_mining.py | build_m1_training_data.py |\\n|------|------------------------|--------------------------|\\n| Candidate 初筛 | Embedding cosine top-50 | 全部 non-positive（无初筛） |\\n| Dataflow 排除范围 | `dataflow_graph[src]` 直接条目 | `positive_files ∪ cg_connected`（更广） |\\n| 排序信号 | Embedding 为主 → BM25 re-rank | 纯 BM25 排序 |\\n| Embedding 角色 | 主选择器（决定候选池） | 不参与 dataflow pool |\\n| BM25 角色 | 可选的 re-ranker | 唯一排序信号 |\\n\\n### 对齐建议\\nplan_015 实施 dynamic negative mining 时需统一为一种逻辑。建议：\\n1. **排除范围统一**：采用 `build_m1_training_data.py` 的 `full_connected`（dataflow + call graph），因为 call graph 邻居也不应作为 hard negatives\\n2. **选择信号**：dynamic mining 应使用当前 epoch 的 encoder embedding（不是 pretrained），这是 dynamic mining 的核心价值——所以 `DataFlowAwareMiner` 的 embedding→filter→BM25 三步法更合理，但需将排除范围从 1-hop dataflow 扩展到 full_connected\\n3. **具体改动**：修改 `DataFlowAwareMiner._is_reachable()` 使其也排除 call graph 连接，或在 `mine()` 中接受 `full_connected_set` 参数\\n\\n---\\n\\n## SWE-bench eval 脚本路径 [2026-05-15, Reviewer 纠正]\\n\\neval_swebench 脚本已存在（之前 Worker 搜索了错误目录 /root/structfuse）：\\n- `/root/structfuse-context/evaluation/eval_swebench.py`（含 .bak 和 .pyc）\\n- `/root/structfuse-context/scripts/eval_swebench_e2e.py`\\n\\nAgent 通过 OpenAI-compatible API 调用（非本地推理），配置项：STRUCTFUSE_LLM_BACKEND=api, STRUCTFUSE_LLM_API_BASE, STRUCTFUSE_LLM_API_KEY, STRUCTFUSE_LLM_MODEL。Retriever 和 agent 分离，单卡 VRAM 无压力。plan_003 基于现有脚本执行，不需要从头创建。\\n\\n---\\n\\n## Qwen 链日志缓冲问题 [2026-05-15, Reviewer 发现]\\n\\nQwen 链脚本用 `python`（有 stdout 缓冲），导致日志延迟输出，监控出现盲区。StarCoder 链用了 `python -u` 没此问题。**后续 Qwen subrun 启动时须加 `PYTHONUNBUFFERED=1` 环境变量或 `python -u`**，保证日志实时输出。当前 run 不需要重启。\\n\\n---\\n\\n## 运维经验 (2026-05-14)\\n\\n**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。\\n\\n**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。\\n\\n**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。\\n\\n---\\n\\n## 关键决策记录\\n\\n**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。\\n\\n---\\n\\n## Related Work Gap 分析 [2026-05-15]\\n\\n当前 literature_map.yaml 39 篇，已超 25+ 目标，但覆盖不均。最薄弱：contrastive learning for code（仅 3 篇）、通用 hard negative mining 方法论。推荐添加 7 篇（全部 WebSearch 验证）：\\n- **必须加**：RocketQA (NAACL 2021)、ContraBERT (ICSE 2023)、ProGraML (ICML 2021)、CrossCodeEval (NeurIPS 2023)\\n- **强烈建议**：SynCoBERT (arXiv 2021)、CAPSTONE (EMNLP 2023)\\n- **可选**：CoSQA (ACL 2021)\\n\\n---\\n\\n## Qwen random_s42 训练 Regime 异常 [2026-05-16]\\n\\n**根因确认**：s42 使用 3 epoch / patience=0（D026 设计，提供 overfitting curve），而 s43/s44 使用 2 epoch / patience=2（D050 统一 regime）。这导致：\\n- warmup 424 步 vs 283 步，step 500 时 s42 val_loss 已比 s43/s44 差 (0.4869 vs 0.4476/0.4252)\\n- s42 两个 checkpoint (best_by_val_loss + best_by_recall_at_1) MD5 完全相同（均 step 1000），pool=50 R@1 两种选法结果一致是预期行为\\n- pool=50 R@1: s42=0.2730 vs s43=0.3138 / s44=0.3181，差距 4pp+ 主要由 regime 差异解释\\n\\n**决策影响**：当前 random_s42 不应纳入 cross-seed 统计。需用统一 2-epoch/patience=2 regime 重训才能获得可比结果。Supplement chain (embed_s42/dataflow_s42/bm25_s42) 已用 D050 统一 regime，不受影响。\\n\", \"total_chars\": 17513, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0723e148-e46a-44e3-a5ec-e6a7d9bceb92",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "d46601a6-78e3-449f-9395-e808ffe9c595",
  "sourceToolAssistantUUID": "0723e148-e46a-44e3-a5ec-e6a7d9bceb92",
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

_source line 26 · 2026-05-16T16:03:47.888Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MhTPXachDJArdBAA2AMm2P`</summary>

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
  "parentUuid": "d46601a6-78e3-449f-9395-e808ffe9c595",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XkBwGW5Yh5oWTGvUCD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8225a337-b563-40cf-b65a-fe735b11042e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NrdzbeRFEAFiWvVBxZd5UU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5349,
      "cache_read_input_tokens": 28133,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5349
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 28133,
          "cache_creation_input_tokens": 5349,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5349,
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

_source line 27 · 2026-05-16T16:03:47.904Z_

<details><summary>↩ Tool result · `toolu_01MhTPXachDJArdBAA2AMm2P`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-14\\n# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。\\n# 总计: 60 entries (含 2 个软件工具引用)\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang\\\"\\n        venue: \\\"NeurIPS (Datasets & Benchmarks, Spotlight)\\\"\\n        year: 2025\\n        relation: building-block\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。\\\"\\n\\n      - title: \\\"SweRank: Software Issue Localization with Code Ranking\\\"\\n        authors: \\\"Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。\\\"\\n\\n      - title: \\\"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution\\\"\\n        authors: \\\"Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen\\\"\\n        venue: \\\"ACL (Findings)\\\"\\n        year: 2025\\n        relation: competitor\\n        summary: \\\"BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Curriculum Learning for Dense Retrieval Distillation\\\"\\n        authors: \\\"Hansi Zeng, Hamed Zamani, Vishwa Vinay\\\"\\n        venue: \\\"SIGIR (Best Short Paper)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。\\\"\\n\\n      - title: \\\"Effective Hard Negative Mining for Contrastive Learning-Based Code Search\\\"\\n        authors: \\\"Fan Y., Li C., Ge J., Huang L., Luo B.\\\"\\n        venue: \\\"ACM TOSEM\\\"\\n        year: 2025\\n        relation: contrast-target\\n        summary: \\\"CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。\\\"\\n        note: \\\"关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。\\\"\\n\\n      - title: \\\"Representation Learning with Contrastive Predictive Coding\\\"\\n        authors: \\\"Aaron van den Oord, Yazhe Li, Oriol Vinyals\\\"\\n        venue: arXiv\\n        year: 2018\\n        relation: background\\n        summary: \\\"InfoNCE 损失函数：对比预测编码的无监督表示学习。StructFuse 训练目标的理论根基。\\\"\\n\\n      - title: \\\"Contrastive Learning with Hard Negative Samples\\\"\\n        authors: \\\"Joshua David Robinson, Ching-Yao Chuang, Suvrit Sra, Stefanie Jegelka\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: method-component\\n        summary: \\\"HCL: 可控 hard negative 采样，证明更难的 negatives 加速和改善学习，但暗示过度 hard 会导致问题。StructFuse difficulty analysis 的理论起点。\\\"\\n\\n      - title: \\\"Debiased Contrastive Learning\\\"\\n        authors: \\\"Ching-Yao Chuang, Joshua Robinson, Yen-Chen Lin, Antonio Torralba, Stefanie Jegelka\\\"\\n        venue: NeurIPS\\n        year: 2020\\n        relation: method-component\\n        summary: \\\"DCL: 去偏对比目标，修正 false negatives（同类样本被当作 negatives）问题。False negative 是 hard negative 过拟合的重要来源。\\\"\\n\\n      - title: \\\"Hard Negative Mixing for Contrastive Learning\\\"\\n        authors: \\\"Yannis Kalantidis, Mert Bulent Sariyildiz, Noe Pion, Philippe Weinzaepfel, Diane Larlus\\\"\\n        venue: NeurIPS\\n        year: 2020\\n        relation: method-component\\n        summary: \\\"MoCHi: feature-level hard negative 混合合成，开销极小。与 StructFuse 的 structure-based negative mining 形成对比。\\\"\\n\\n      - title: \\\"Understanding Hard Negatives in Noise Contrastive Estimation\\\"\\n        authors: \\\"Wenzheng Zhang, Karl Stratos\\\"\\n        venue: NAACL\\n        year: 2021\\n        relation: background\\n        summary: \\\"理论分析：用模型分布作为 negative 分布可减少梯度偏差。为 hard negative 作用提供理论解释。\\\"\\n\\n      - title: \\\"ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning\\\"\\n        authors: \\\"Jun Xia, Lirong Wu, Ge Wang, Jintao Chen, Stan Z. Li\\\"\\n        venue: ICML\\n        year: 2022\\n        relation: method-component\\n        summary: \\\"揭示图对比学习中 hard negative = false negative 的陷阱，提出基于概率的 hardness 区分 true/false negatives。与 StructFuse difficulty-overfitting 发现呼应。\\\"\\n\\n      - title: \\\"Difficulty-Based Sampling for Debiased Contrastive Representation Learning\\\"\\n        authors: \\\"Taeuk Jang, Xiaoqian Wang\\\"\\n        venue: CVPR\\n        year: 2023\\n        relation: method-component\\n        summary: \\\"WCL: 用 difficulty 分层采样 + bias-amplifying encoder 找信息性 hard negatives 同时避免 false negatives。与 StructFuse difficulty stratification 思路最接近。\\\"\\n\\n      - title: \\\"CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion\\\"\\n        authors: \\\"Xingwei He, Yeyun Gong, A-Long Jin, Hang Zhang, Anlei Dong, Jian Jiao, Siu Ming Yiu, Nan Duan\\\"\\n        venue: EMNLP\\n        year: 2023\\n        relation: background\\n        summary: \\\"课程采样策略 + pseudo-query 文档扩展，解决双塔检索训练-推理差异。StructFuse 的 structure-grounded negatives 提供正交的课程形式。\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Contrastive Learning for Code\\n  # ==========================================================================\\n  contrastive_code_learning:\\n    description: \\\"代码领域的对比学习方法，训练时利用代码特性构建正负样本\\\"\\n    papers:\\n\\n      - title: \\\"Contrastive Code Representation Learning\\\"\\n        authors: \\\"Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\\\"\\n        venue: EMNLP\\n        year: 2021\\n        relation: background\\n        summary: \\\"ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。\\\"\\n\\n      - title: \\\"CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search\\\"\\n        authors: \\\"Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan\\\"\\n        venue: EMNLP\\n        year: 2022\\n        relation: background\\n        summary: \\\"结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。\\\"\\n\\n      - title: \\\"Towards Learning (Dis)-Similarity of Source Code from Program Contrasts\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: \\\"ACL (Long Papers)\\\"\\n        year: 2022\\n        relation: background\\n        summary: \\\"利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。\\\"\\n\\n      - title: \\\"CoCoSoDa: Effective Contrastive Learning for Code Search\\\"\\n        authors: \\\"Ensheng Shi, Yanlin Wang, Wenchao Gu, Lun Du, Hongyu Zhang, Shi Han, Dongmei Zhang, Hongbin Sun\\\"\\n        venue: ICSE\\n        year: 2023\\n        relation: direct-competitor\\n        summary: \\\"对比代码搜索 + soft data augmentation + momentum-based negative enrichment。在 negative 数量维度与 StructFuse 互补（momentum queue vs. difficulty-aware selection）。\\\"\\n\\n      - title: \\\"SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation\\\"\\n        authors: \\\"Xin Wang, Yasheng Wang, Fei Mi, Pingyi Zhou, Yao Wan, Xiao Liu, Li Li, Hao Wu, Jin Liu, Xin Jiang\\\"\\n        venue: arXiv\\n        year: 2021\\n        relation: background\\n        summary: \\\"语法引导的多模态对比预训练，对齐 code/NL/AST 三模态。通过 identifier prediction 和 AST edge prediction 显式编码句法结构。\\\"\\n\\n      - title: \\\"ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning\\\"\\n        authors: \\\"Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, Yang Liu\\\"\\n        venue: ICSE\\n        year: 2023\\n        relation: background\\n        summary: \\\"鲁棒性导向的对比预训练，设计 9 种对抗增强算子（identifier renaming, dead code insertion, operand swapping 等），提升模型对对抗攻击的鲁棒性。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n      - title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\"\\n        authors: \\\"Shahd Seddik, Fatemeh Fard\\\"\\n        venue: arXiv\\n        year: 2026\\n        relation: contrast\\n        summary: \\\"用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。\\\"\\n\\n      - title: \\\"ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimization\\\"\\n        authors: \\\"Chris Cummins, Zacharias V. Fisches, Tal Ben-Nun, Torsten Hoefler, Michael FP O'Boyle, Hugh Leather\\\"\\n        venue: ICML\\n        year: 2021\\n        relation: background\\n        summary: \\\"语言无关的全程序图表示（control-flow + data-flow + call relations），证明整程序结构表示可学习且有效。StructFuse 使用 inter-procedural data-flow 的概念根基。\\\"\\n\\n      - title: \\\"CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion\\\"\\n        authors: \\\"Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Hantian Ding, Ming Tan, Nihal Jain, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, Bing Xiang\\\"\\n        venue: NeurIPS\\n        year: 2023\\n        relation: background\\n        summary: \\\"多语言 cross-file 代码补全 benchmark，用静态分析确定需 cross-file 依赖的补全目标。验证了跨文件上下文对代码任务的关键性。\\\"\\n\\n  # ==========================================================================\\n  # Category 5: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: \\\"EMNLP (Findings)\\\"\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: building-block\\n        summary: \\\"大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n\\n      - title: \\\"DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence\\\"\\n        authors: \\\"Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: background\\n        summary: \\\"开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。\\\"\\n\\n      - title: \\\"RepoFusion: Training Code Models to Understand Your Repository\\\"\\n        authors: \\\"Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。\\\"\\n\\n      - title: \\\"BM25\\\"\\n        authors: \\\"Stephen Robertson, Hugo Zaragoza\\\"\\n        venue: \\\"Foundations and Trends in Information Retrieval\\\"\\n        year: 2009\\n        relation: baseline\\n        summary: \\\"经典稀疏检索方法，StructFuse 的 baseline 之一。\\\"\\n\\n      - title: \\\"CoSQA: 20,000+ Web Queries for Code Search and Question Answering\\\"\\n        authors: \\\"Junjie Huang, Duyu Tang, Linjun Shou, Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, Nan Duan\\\"\\n        venue: ACL\\n        year: 2021\\n        relation: background\\n        summary: \\\"20,000+ 真实 web 查询与 Python 代码配对的大规模数据集，弥合合成 benchmark 与真实开发者需求的差距。\\\"\\n\\n  # ==========================================================================\\n  # Category 6: Graph-Guided Code Navigation (Inference-Time)\\n  # ==========================================================================\\n  graph_guided_inference:\\n    description: \\\"推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）\\\"\\n    papers:\\n\\n      - title: \\\"LocAgent: Graph-Guided LLM Agents for Code Localization\\\"\\n        authors: \\\"Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang\\\"\\n        venue: ACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。\\\"\\n\\n      - title: \\\"CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases\\\"\\n        authors: \\\"Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou\\\"\\n        venue: NAACL\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。\\\"\\n\\n      - title: \\\"RANGER: Repository-Level Agent for Graph-Enhanced Retrieval\\\"\\n        authors: \\\"Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。\\\"\\n\\n      - title: \\\"RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph\\\"\\n        authors: \\\"Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu\\\"\\n        venue: ICLR\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。\\\"\\n\\n      - title: \\\"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph\\\"\\n        authors: \\\"Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang\\\"\\n        venue: ASE\\n        year: 2024\\n        relation: contrast\\n        summary: \\\"构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。\\\"\\n\\n      - title: \\\"GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion\\\"\\n        authors: \\\"Xingliang Wang, Baoyi Wang, Chen Zhi, Junxiao Han, Xinkui Zhao, Jianwei Yin, Shuiguang Deng\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: contrast\\n        summary: \\\"构建 repo/module/function 三层多语义代码图（AST + CFG + DFG + call graph + class hierarchy），用 GNN-based hybrid retriever 做层次化检索增强代码补全。推理时图方法，与 StructFuse 训练时结构信号互补。\\\"\\n\\n  # ==========================================================================\\n  # Category 7: Representation Geometry / Similarity Saturation\\n  # ==========================================================================\\n  representation_geometry:\\n    description: \\\"预训练模型表示空间几何分析及各向异性修正方法\\\"\\n    papers:\\n\\n      - title: \\\"Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere\\\"\\n        authors: \\\"Tongzhou Wang, Phillip Isola\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: method-component\\n        summary: \\\"定义 alignment/uniformity 两个对比学习关键属性，证明对比损失渐近优化两者。StructFuse 分析 embedding space 质量的理论工具。\\\"\\n\\n      - title: \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\"\\n        authors: \\\"Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"揭示预训练 LM embedding 退化为窄锥的现象，StructFuse 观察到的 similarity saturation 可追溯到此。\\\"\\n\\n      - title: \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\"\\n        authors: \\\"Kawin Ethayarajh\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"实证发现 BERT/ELMo/GPT-2 表示占据窄锥（各向异性），StructFuse 使用的 code encoder 继承此问题。\\\"\\n\\n      - title: \\\"On the Sentence Embeddings from Pre-trained Language Models\\\"\\n        authors: \\\"Bohan Li, Hao Zhou, Junxian He, Mingxuan Wang, Yiming Yang, Lei Li\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: method-component\\n        summary: \\\"BERT-flow: 用 normalizing flows 将各向异性句子嵌入变换为各向同性高斯分布。\\\"\\n\\n      - title: \\\"SimCSE: Simple Contrastive Learning of Sentence Embeddings\\\"\\n        authors: \\\"Tianyu Gao, Xingcheng Yao, Danqi Chen\\\"\\n        venue: EMNLP\\n        year: 2021\\n        relation: method-component\\n        summary: \\\"用 dropout 作为最小增强的对比学习，直接证明 contrastive learning 改善 anisotropy。StructFuse 可引用其 uniformity 分析框架。\\\"\\n\\n      - title: \\\"Whitening Sentence Representations for Better Semantics and Faster Retrieval\\\"\\n        authors: \\\"Jianlin Su, Jiarun Cao, Weijie Liu, Yangyiwen Ou\\\"\\n        venue: arXiv\\n        year: 2021\\n        relation: method-component\\n        summary: \\\"白化操作增强句子表示各向同性并降维，与 StructFuse embedding post-processing 讨论相关。\\\"\\n\\n  # ==========================================================================\\n  # Category 8: Infrastructure / Tools\\n  # ==========================================================================\\n  infrastructure:\\n    description: \\\"StructFuse 依赖的核心基础设施和工具\\\"\\n    papers:\\n\\n      - title: \\\"Billion-Scale Similarity Search with GPUs\\\"\\n        authors: \\\"Jeff Johnson, Matthijs Douze, Herve Jegou\\\"\\n        venue: \\\"IEEE Transactions on Big Data\\\"\\n        year: 2021\\n        relation: building-block\\n        summary: \\\"FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。\\\"\\n\\n      - title: \\\"Tree-sitter: An Incremental Parsing System for Programming Tools\\\"\\n        authors: \\\"Max Brunsfeld et al.\\\"\\n        venue: \\\"Software (Zenodo DOI: 10.5281/zenodo.13375512)\\\"\\n        year: 2018\\n        relation: building-block\\n        summary: \\\"增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。\\\"\\n        note: \\\"软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。\\\"\\n\", \"total_chars\": 23891, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8225a337-b563-40cf-b65a-fe735b11042e",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "b7bb092e-f64d-41f4-9e8e-0d8a9782e5d3",
  "sourceToolAssistantUUID": "8225a337-b563-40cf-b65a-fe735b11042e",
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

_source line 28 · 2026-05-16T16:03:50.984Z_

Now let me look at the actual paper artifacts (LaTeX files) to verify what's actually written.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7bb092e-f64d-41f4-9e8e-0d8a9782e5d3",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XkWv339kN6mMp5WPEQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8aa868b-fa02-48bf-ac71-b56e2fee632d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuYjGpwzyh74jcZAY5Ejnf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18361,
      "cache_read_input_tokens": 33482,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18361,
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

_source line 29 · 2026-05-16T16:03:52.834Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Y4H5pvdgFwUVWxzccx7paQ`</summary>

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
  "parentUuid": "e8aa868b-fa02-48bf-ac71-b56e2fee632d",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XkWv339kN6mMp5WPEQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9da3f10-761c-4bd5-bb1c-b39935808966",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuYjGpwzyh74jcZAY5Ejnf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18361,
      "cache_read_input_tokens": 33482,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18361,
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

_source line 30 · 2026-05-16T16:03:52.852Z_

<details><summary>↩ Tool result · `toolu_01Y4H5pvdgFwUVWxzccx7paQ`</summary>

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
  "parentUuid": "b9da3f10-761c-4bd5-bb1c-b39935808966",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "80893518-a40c-4777-988f-dbc4fc126054",
  "sourceToolAssistantUUID": "b9da3f10-761c-4bd5-bb1c-b39935808966",
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

_source line 31 · 2026-05-16T16:03:53.139Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01AFdRCT75sa9pTDbF7Fa7JQ`</summary>

```json
{
  "pattern": "**/paper*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80893518-a40c-4777-988f-dbc4fc126054",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XkWv339kN6mMp5WPEQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94869c45-7343-40e0-af7e-8a154979766f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuYjGpwzyh74jcZAY5Ejnf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18361,
      "cache_read_input_tokens": 33482,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18361
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 33482,
          "cache_creation_input_tokens": 18361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18361,
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

_source line 32 · 2026-05-16T16:03:53.150Z_

<details><summary>↩ Tool result · `toolu_01AFdRCT75sa9pTDbF7Fa7JQ`</summary>

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
artifacts/dream_reports/dream_20260516T150348/best/paper.tex
artifacts/dream_reports/dream_20260516T150348/median/paper.tex
artifacts/dream_reports/dream_20260516T150348/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94869c45-7343-40e0-af7e-8a154979766f",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "e7656015-00c7-4f1b-8944-2eb4f90af186",
  "sourceToolAssistantUUID": "94869c45-7343-40e0-af7e-8a154979766f",
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

_source line 33 · 2026-05-16T16:03:56.096Z_

Let me read the latest dream review paper (the most recent full paper draft) and the experiments section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7656015-00c7-4f1b-8944-2eb4f90af186",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XkuPPatC6EbBYbMv8k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f40e1ca3-913f-4616-afbe-97abe42552cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HxZ4zqGS3eA9u6NVvqnM9d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 948,
      "cache_read_input_tokens": 51843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 948,
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

_source line 34 · 2026-05-16T16:03:57.092Z_

<details open><summary>🔧 Tool call — Read · `toolu_016WpxxC54GeH2avdYpzr4ML`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f40e1ca3-913f-4616-afbe-97abe42552cf",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XkuPPatC6EbBYbMv8k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad03e83c-0633-4202-a5a0-74fec2005ab3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HxZ4zqGS3eA9u6NVvqnM9d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 948,
      "cache_read_input_tokens": 51843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 948,
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

_source line 35 · 2026-05-16T16:03:57.287Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PTsufuD1vZcBcAMbSEtdpC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/v2/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad03e83c-0633-4202-a5a0-74fec2005ab3",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XkuPPatC6EbBYbMv8k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "307737b4-644d-426c-b95b-1bab627ca624",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HxZ4zqGS3eA9u6NVvqnM9d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 948,
      "cache_read_input_tokens": 51843,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 948
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 51843,
          "cache_creation_input_tokens": 948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 948,
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

_source line 36 · 2026-05-16T16:03:57.350Z_

<details><summary>↩ Tool result · `toolu_016WpxxC54GeH2avdYpzr4ML`</summary>

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
  "parentUuid": "ad03e83c-0633-4202-a5a0-74fec2005ab3",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "37d2f923-04c9-4d00-8795-dc8536f473a3",
  "sourceToolAssistantUUID": "ad03e83c-0633-4202-a5a0-74fec2005ab3",
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

### Tool result

_source line 37 · 2026-05-16T16:03:57.292Z_

<details><summary>↩ Tool result · `toolu_01PTsufuD1vZcBcAMbSEtdpC`</summary>

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
  "parentUuid": "307737b4-644d-426c-b95b-1bab627ca624",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "a6e46688-6977-4e8c-84fa-7ae0368e643f",
  "sourceToolAssistantUUID": "307737b4-644d-426c-b95b-1bab627ca624",
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

_source line 38 · 2026-05-16T16:04:00.517Z_

Now let me also read the dream review reports to understand prior reviewer feedback.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6e46688-6977-4e8c-84fa-7ae0368e643f",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XmDBiBrD4JtedZden7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78383eef-bbdc-4c06-880d-073bee890902",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPzVTstgNCivu8fiu5pBU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14676,
      "cache_read_input_tokens": 52791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14676,
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

_source line 39 · 2026-05-16T16:04:02.369Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01M8B6N817fwQpiSQ6aCXVwt`</summary>

```json
{
  "pattern": "**/dream_20260516T150348/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78383eef-bbdc-4c06-880d-073bee890902",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XmDBiBrD4JtedZden7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8396d756-e706-47ad-96b8-4a725117ce49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPzVTstgNCivu8fiu5pBU9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14676,
      "cache_read_input_tokens": 52791,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14676
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 128,
          "cache_read_input_tokens": 52791,
          "cache_creation_input_tokens": 14676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14676,
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

_source line 40 · 2026-05-16T16:04:02.383Z_

<details><summary>↩ Tool result · `toolu_01M8B6N817fwQpiSQ6aCXVwt`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8396d756-e706-47ad-96b8-4a725117ce49",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "091b9d1c-17b1-41e9-a501-697c6b02be08",
  "sourceToolAssistantUUID": "8396d756-e706-47ad-96b8-4a725117ce49",
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

_source line 41 · 2026-05-16T16:04:05.122Z_

<details open><summary>🔧 Tool call — Glob · `toolu_017DuthctyrLWAR5rrAeM2Gb`</summary>

```json
{
  "pattern": "**/dream_20260516T150348/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "091b9d1c-17b1-41e9-a501-697c6b02be08",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XmapDL7YDe6NGUaGN6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e81d045e-e685-47a3-92b5-ef4034fac9a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013idZRq4ZpE47yFGmWfZK6e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 246,
      "cache_read_input_tokens": 67467,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 246
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 112,
          "cache_read_input_tokens": 67467,
          "cache_creation_input_tokens": 246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 246,
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

_source line 42 · 2026-05-16T16:04:05.142Z_

<details><summary>↩ Tool result · `toolu_017DuthctyrLWAR5rrAeM2Gb`</summary>

```text
artifacts/dream_reports/dream_20260516T150348/logs/orchestrator.log
artifacts/dream_reports/dream_20260516T150348/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260516T150348/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260516T150348/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260516T150348/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260516T150348/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T150348/best/experiment_data.json
artifacts/dream_reports/dream_20260516T150348/best/paper_framing.md
artifacts/dream_reports/dream_20260516T150348/best/paper.tex
artifacts/dream_reports/dream_20260516T150348/best/paper.aux
artifacts/dream_reports/dream_20260516T150348/best/paper.out
artifacts/dream_reports/dream_20260516T150348/best/paper.pdf
artifacts/dream_reports/dream_20260516T150348/best/paper.log
artifacts/dream_reports/dream_20260516T150348/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260516T150348/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T150348/median/experiment_data.json
artifacts/dream_reports/dream_20260516T150348/median/paper_framing.md
artifacts/dream_reports/dream_20260516T150348/median/paper.tex
artifacts/dream_reports/dream_20260516T150348/median/paper.aux
artifacts/dream_reports/dream_20260516T150348/median/paper.out
artifacts/dream_reports/dream_20260516T150348/median/paper.pdf
artifacts/dream_reports/dream_20260516T150348/median/paper.log
artifacts/dream_reports/dream_20260516T150348/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260516T150348/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T150348/worst/experiment_data.json
artifacts/dream_reports/dream_20260516T150348/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T150348/worst/paper.tex
artifacts/dream_reports/dream_20260516T150348/worst/paper.aux
artifacts/dream_reports/dream_20260516T150348/worst/paper.out
artifacts/dream_reports/dream_20260516T150348/worst/paper.pdf
artifacts/dream_reports/dream_20260516T150348/worst/paper.log
artifacts/dream_reports/dream_20260516T150348/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260516T150348/best/review_context.yaml
artifacts/dream_reports/dream_20260516T150348/logs/review_best.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e81d045e-e685-47a3-92b5-ef4034fac9a3",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "f41ae6cb-da6a-4046-a2e0-3d262f204def",
  "sourceToolAssistantUUID": "e81d045e-e685-47a3-92b5-ef4034fac9a3",
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

_source line 43 · 2026-05-16T16:04:08.529Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T8ZajpyPaaNePSGep7CKn5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f41ae6cb-da6a-4046-a2e0-3d262f204def",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XmnZu5NkzLa2hnBR9Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b50afff-fade-45bf-b528-d57ef9cdc99f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014WFJo6ABBy21ZUf9R53gn2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 900,
      "cache_read_input_tokens": 67713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 900,
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

_source line 44 · 2026-05-16T16:04:09.066Z_

<details><summary>↩ Tool result · `toolu_01T8ZajpyPaaNePSGep7CKn5`</summary>

```text
1	narrative_guidance: 'Framing B 完全成立：Paper = systematic mining study + methodological
2	  contribution。
3	
4	  Standard eval 上 embed Δ 较小（Qwen ~+0.4pp, StarCoder ~+0.6pp），但 D062 query-split  evaluation
5	  揭示标准评估因 checkpoint 过拟合掩盖了真实效应——held-out evaluation 上 embed Δ  恢复至 Qwen +1.4pp, StarCoder
6	  +0.9pp（均在 best 档预设范围内）。这一发现本身就是方法论贡献： checkpoint selection criterion effect (+16.3pp
7	  max) > mining strategy effect (~1pp)， 说明社区低估了 mining 效果是因为评估方法论缺陷。
8	
9	  BM25 negatives 在两个 encoder 上均 harm（Δ ≤ -1.5pp），empirically 关闭 CoCoHaNeRe 修正论证。 UniXcoder
10	  3-seed null result 干净地归因于 125M scale boundary condition。 RepoBench-R 替代 SWE-bench
11	  作为 held-out external validation，CIs non-overlapping。
12	
13	  3 claims 原样成立：Claim 1 (embed mining reliable) + Claim 2 (exploratory representation  geometry
14	  interaction) + 额外贡献 (checkpoint criterion methodology)。EMNLP Main 强投。
15	
16	  M2 anchors — Standard eval: Qwen random=0.570, embed=0.573, SC random=0.479, embed=0.485。
17	  D062 query-split: Qwen random=0.361, embed=0.375, SC random=0.305, embed=0.314。
18	
19	  '
20	imagined_experiments:
21	- name: M3a SWE-bench Lite E2E — OOD Limitation Disclosure
22	  plan_id: plan_003
23	  description: '3 strategies × best Qwen checkpoint on SWE-bench Lite 300 instances。
24	    实际已完成（random_s42, 100 instances + BM25 baseline 300）。结果为 OOD 泛化失败， 在论文中作为 limitation
25	    呈现而非贡献。
26	
27	    '
28	  expected_results:
29	    random_s42_100:
30	      R_at_1: 0.04
31	      R_at_5: 0.11
32	      R_at_10: 0.14
33	      R_at_20: 0.16
34	      MRR: 0.0698
35	    bm25_baseline_300:
36	      R_at_1: 0.2733
37	      R_at_5: 0.4667
38	      R_at_10: 0.55
39	    neural_vs_bm25_gap_R1_pp: -23.3
40	    status: DONE_FAILED
41	    director_decision: 放弃 SWE-bench 作为论文贡献，外部验证改用 RepoBench-R
42	  result_rationale: 'R@1=0.04 vs BM25=0.2733 表明 contrastive retriever 在 OOD 跨 repo
43	    场景完全失败。 根因：SWE-smith 训练数据是 intra-repo 检索（query 与 candidates 来自同一 repo）， 而 SWE-bench
44	    是 cross-repo 设置（模型未见过的 repo）。Contrastive fine-tuning在小 pool  内 intra-repo 检索上过拟合，丧失了
45	    pretrained encoder 的 cross-repo 泛化能力。 BM25 因为是 lexical matching（不依赖 learned representations）所以不受此影响。
46	
47	    在 best tier 下，这一失败被 strategically 利用：(1) 诚实报告增强论文可信度， (2) 明确 scope boundary "our
48	    results apply to intra-repo retrieval settings"， (3) 激发 future work 方向 "bridging
49	    the intra/cross-repo gap"。 RepoBench-R 替代作为 held-out evaluation（仍是 cross-file
50	    但 repo-aware 设置）。
51	
52	    '
53	  tables:
54	  - name: 'Table S4: SWE-bench OOD Evaluation (Limitation)'
55	    columns:
56	    - Retriever
57	    - R@1
58	    - R@5
59	    - R@10
60	    - MRR
61	    - N
62	    rows:
63	    - - BM25 (reference)
64	      - 0.273
65	      - 0.467
66	      - 0.55
67	      - 0.36
68	      - 300
69	    - - StructFuse-random
70	      - 0.04
71	      - 0.11
72	      - 0.14
73	      - 0.07
74	      - 100
75	  figures_description:
76	  - 'Fig S7: SWE-bench R@K curve showing neural retriever collapse below BM25 at all
77	    K'
78	  analysis: 'SWE-bench failure 在 best tier 下反而加强了论文：它划定了清晰的 scope boundary， 展示了作者的自我审视能力。Reviewer
79	    concern "no downstream eval" 由 RepoBench-R 回应， SWE-bench 失败则作为 honest limitation
80	    处理，1-2 段落放在 Limitations section。
81	
82	    '
83	- name: RepoBench-R Cross-File Retrieval with 3-Seed Bootstrap CIs
84	  plan_id: plan_004
85	  description: 'RepoBench-R test_easy (pool ~6) 和 test_hard (pool ~18) 上评估 3 seeds
86	    ×  3 strategies × 2 encoders（Qwen, StarCoder）。报告 R@1 均值 + 95% bootstrap CI。 这是
87	    SWE-bench 失败后的替代 held-out external validation。
88	
89	    '
90	  expected_results:
91	    qwen_test_hard:
92	      random_R1_mean: 0.62
93	      random_R1_ci:
94	      - 0.615
95	      - 0.625
96	      embedding_R1_mean: 0.632
97	      embedding_R1_ci:
98	      - 0.626
99	      - 0.638
100	      dataflow_R1_mean: 0.626
101	      dataflow_R1_ci:
102	      - 0.62
103	      - 0.632
104	      bm25_R1_mean: 0.601
105	      bm25_R1_ci:
106	      - 0.595
107	      - 0.607
108	      embedding_minus_random_pp: 1.2
109	      bm25_minus_random_pp: -1.9
110	    qwen_test_easy:
111	      random_R1_mean: 0.842
112	      embedding_R1_mean: 0.851
113	      dataflow_R1_mean: 0.847
114	      embedding_minus_random_pp: 0.9
115	    starcoder_test_hard:
116	      random_R1_mean: 0.571
117	      random_R1_ci:
118	      - 0.565
119	      - 0.577
120	      embedding_R1_mean: 0.579
121	      embedding_R1_ci:
122	      - 0.573
123	      - 0.585
124	      dataflow_R1_mean: 0.568
125	      dataflow_R1_ci:
126	      - 0.562
127	      - 0.574
128	      bm25_R1_mean: 0.553
129	      bm25_R1_ci:
130	      - 0.547
131	      - 0.559
132	      embedding_minus_random_pp: 0.8
133	      bm25_minus_random_pp: -1.8
134	    starcoder_test_easy:
135	      random_R1_mean: 0.81
136	      embedding_R1_mean: 0.816
137	      embedding_minus_random_pp: 0.6
138	    repobench_embed_vs_random_avg_pp: 1.0
139	    CI_non_overlapping_embed_vs_random: true
140	    bootstrap_N: 10000
141	  result_rationale: 'RepoBench-R 是 cross-file code completion 任务，与 SWE-smith (bug-fix
142	    retrieval)  领域不同但任务结构相似（从 repo 内候选文件中检索正确文件）。Pool=18 (test_hard) 提供 足够的 distractor
143	    使 mining 质量差异体现。
144	
145	    Embedding mining 在 test_hard 上持续帮助两个 encoder（Qwen +1.2pp, StarCoder +0.8pp）， 因为
146	    harder negatives 训练使 encoder 更善于区分 "semantically similar but functionally  distinct"
147	    文件——这一能力跨任务泛化。CIs non-overlapping 因为 8K test instances 提供 足够的统计功效，即使只有 3 seeds，instance-level
148	    bootstrap 也能给出 tight CIs。
149	
150	    BM25 negatives 在 RepoBench-R 上同样 harm（-1.8 to -1.9pp），与 SWE-smith 一致， 说明 BM25
151	    harm 不是 benchmark-specific artifact 而是 strategy 固有问题。
152	
153	    Test_easy (pool=6) 上 delta 压缩至 0.6-0.9pp 是预期的 ceiling effect—— 6 candidates 中选对
154	    1 个的 baseline 已经很高。
155	
156	    Dataflow 在 Qwen test_hard 上 +0.6pp 但 CI 与 random 接近重叠， StarCoder 上 -0.3pp（CI 含零）——与
157	    SWE-smith encoder-strategy interaction 一致。
158	
159	    '
160	  tables:
161	  - name: 'Table 5: RepoBench-R Results (test_hard, pool≈18)'
162	    columns:
163	    - Encoder
164	    - Strategy
165	    - R@1 (%)
166	    - 95% CI
167	    - Δ vs Random (pp)
168	    rows:
169	    - - Qwen
170	      - BM25
171	      - 60.1
172	      - '[59.5, 60.7]'
173	      - '-1.9'
174	    - - Qwen
175	      - random
176	      - 62.0
177	      - '[61.5, 62.5]'
178	      - —
179	    - - Qwen
180	      - dataflow
181	      - 62.6
182	      - '[62.0, 63.2]'
183	      - '+0.6'
184	    - - Qwen
185	      - embedding
186	      - 63.2
187	      - '[62.6, 63.8]'
188	      - '+1.2'
189	    - - StarCoder
190	      - BM25
191	      - 55.3
192	      - '[54.7, 55.9]'
193	      - '-1.8'
194	    - - StarCoder
195	      - random
196	      - 57.1
197	      - '[56.5, 57.7]'
198	      - —
199	    - - StarCoder
200	      - dataflow
201	      - 56.8
202	      - '[56.2, 57.4]'
203	      - '-0.3'
204	    - - StarCoder
205	      - embedding
206	      - 57.9
207	      - '[57.3, 58.5]'
208	      - '+0.8'
209	  figures_description:
210	  - 'Fig 5: RepoBench-R R@1 grouped bar chart (2 encoders × 4 strategies) with CI
211	    whiskers'
212	  - 'Fig 5b: test_easy vs test_hard side-by-side, showing ceiling compression'
213	  analysis: 'Cross-benchmark 一致性是 best tier 核心证据：embedding mining 在 SWE-smith 和  RepoBench-R
214	    上均显著提升两个 encoder，BM25 均 harm。这排除了 "单 benchmark artifact"  reviewer concern。Strategy
215	    ranking BM25 < random < dataflow ≤ embedding 完美保持。 test_easy ceiling effect 间接验证了
216	    pool size 对效果幅度的调节作用（与 plan_019 互补）。
217	
218	    '
219	- name: Stratified Analysis with 5 Strata (D062 Query-Split Evaluation)
220	  plan_id: plan_005
221	  description: '5 层分层分析：repo size / pool size / query-positive similarity /  structural
222	    data availability (90% with m1_reextract_v2 vs 10% remaining errors) /  neg_difficulty
223	    quartile。使用 M2 best checkpoints 在 D062 query-split held-out  evaluation 上重新评估。
224	
225	    '
226	  expected_results:
227	    stratum_structural_available:
228	      with_dataflow_90pct:
229	        qwen_dataflow_minus_random_pp: 0.8
230	        qwen_embed_minus_random_pp: 1.3
231	        starcoder_dataflow_minus_random_pp: -0.2
232	        n_instances: ~13000
233	        note: m1_reextract_v2 提升 coverage 从 34% 到 90%
234	      no_dataflow_10pct:
235	        qwen_dataflow_minus_random_pp: 0.1
236	        qwen_embed_minus_random_pp: 1.4
237	        n_instances: ~1400
238	    stratum_neg_difficulty_quartile:
239	      Q1_easiest:
240	        qwen_embed_minus_random_pp: 0.6
241	        qwen_dataflow_minus_random_pp: 0.2
242	      Q2:
243	        qwen_embed_minus_random_pp: 1.1
244	        qwen_dataflow_minus_random_pp: 0.5
245	      Q3:
246	        qwen_embed_minus_random_pp: 1.7
247	        qwen_dataflow_minus_random_pp: 0.9
248	      Q4_hardest:
249	        qwen_embed_minus_random_pp: 2.3
250	        qwen_dataflow_minus_random_pp: 1.5
251	    stratum_repo_size:
252	      small_lt50:
253	        embedding_delta_pp: 2.0
254	        n: ~500
255	      medium_50_200:
256	        embedding_delta_pp: 1.6
257	        n: ~4100
258	      large_200_500:
259	        embedding_delta_pp: 1.3
260	        n: ~5500
261	      xlarge_500plus:
262	        embedding_delta_pp: 1.0
263	        n: ~5100
264	    stratum_pool_size:
265	      pool_lt20:
266	        embedding_delta_pp: 0.7
267	        dataflow_delta_pp: 0.2
268	      pool_20_50:
269	        embedding_delta_pp: 1.5
270	        dataflow_delta_pp: 0.6
271	      pool_gt50:
272	        embedding_delta_pp: 1.9
273	        dataflow_delta_pp: 0.9
274	    stratum_query_pos_sim:
275	      high_sim_gt095:
276	        embedding_delta_pp: 1.8
277	        dataflow_delta_pp: 1.2
278	      medium_sim_085_095:
279	        embedding_delta_pp: 1.3
280	        dataflow_delta_pp: 0.5
281	      low_sim_lt085:
282	        embedding_delta_pp: 0.8
283	        dataflow_delta_pp: 0.1
284	  result_rationale: 'm1_reextract_v2 将 structural data rate 从 34% 提升到 90%，彻底改变了 structural  stratum
285	    分析。90% stratum 上 dataflow Δ=+0.8pp（显著）因为绝大部分 instance 现在 获得真实 dataflow-disconnected
286	    negatives。10% remaining errors 上 dataflow 退化为  random（Δ≈0），因为缺乏结构数据意味着 fallback
287	    策略无差异。
288	
289	    Neg difficulty Q4（最难 quartile）embed Δ=+2.3pp 是 overall 的 ~1.6 倍——越难的  instance（margin
290	    最小）从 harder negatives 获益最多，这是 representation saturation  理论的直接预测。Q1（最易）Δ 最小（0.6pp）因为
291	    random negatives 已足够区分。
292	
293	    Repo size 上 small repo Δ 最大（2.0pp）因为小 repo candidate pool 集中，mining  质量差异更容易体现。Pool
294	    size > 50 时 delta 增大到 1.9pp，说明 mining 在更大搜索 空间下更有价值。
295	
296	    Query-positive similarity 分层显示 high sim（>0.95）时 delta 最大，与 Qwen  saturation 分析一致——高相似度区域是
297	    embedding mining 最有价值的场景。
298	
299	    '
300	  tables:
301	  - name: 'Table 6: Stratified Embed-Random Δ by Neg Difficulty Quartile (Qwen, D062
302	      eval)'
303	    columns:
304	    - Quartile
305	    - margin_mean
306	    - emb−rand (pp)
307	    - df−rand (pp)
308	    rows:
309	    - - Q1 (easiest)
310	      - 0.135
311	      - '+0.6'
312	      - '+0.2'
313	    - - Q2
314	      - 0.072
315	      - '+1.1'
316	      - '+0.5'
317	    - - Q3
318	      - 0.028
319	      - '+1.7'
320	      - '+0.9'
321	    - - Q4 (hardest)
322	      - 0.007
323	      - '+2.3'
324	      - '+1.5'
325	  - name: 'Table 6b: Stratified by Structural Data Availability (Qwen)'
326	    columns:
327	    - Stratum
328	    - N
329	    - emb−rand (pp)
330	    - df−rand (pp)
331	    rows:
332	    - - With dataflow (90%)
333	      - ~13K
334	      - '+1.3'
335	      - '+0.8'
336	    - - No dataflow (10%)
337	      - ~1.4K
338	      - '+1.4'
339	      - '+0.1'
340	  figures_description:
341	  - 'Fig 6: Neg difficulty quartile × strategy interaction line plot'
342	  - 'Fig 7: Heatmap — R@1 delta (strategy × stratum), separate panels for Qwen and
343	    StarCoder'
344	  analysis: 'Neg difficulty quartile 分析是 best tier 最强 mechanistic 证据。Q4 的 2.3pp  embed
345	    delta 是 overall 1.4pp 的 1.6 倍——直接验证 "harder instances benefit more  from harder
346	    negatives" 的理论预测。Structural availability 分析从 34%→90% coverage  升级后说服力大增——90% stratum
347	    的 dataflow Δ=+0.8pp 是 clean signal。 Confound analysis（rich-dataflow 99.3% 在 large/xlarge
348	    repo）仍需控制 repo size  来隔离 dataflow richness 独立效应。
349	
350	    '
351	- name: Call-Graph Hop Depth Ablation (1/2/3-hop)
352	  plan_id: plan_007
353	  description: '比较 1-hop / 2-hop / 3-hop call-graph bounding 对 dataflow negative 质量影响。
354	    Qwen encoder, 1 seed, SWE-smith validation。使用 m1_reextract_v2 数据（90% coverage）。
355	
356	    '
357	  expected_results:
358	    hop_1:
359	      R1: 0.548
360	      connected_coverage_pct: 15.2
361	      negatives_per_query_mean: 21.4
362	    hop_2:
363	      R1: 0.558
364	      connected_coverage_pct: 45.8
365	      negatives_per_query_mean: 38.6
366	    hop_3:
367	      R1: 0.553
368	      connected_coverage_pct: 72.1
369	      negatives_per_query_mean: 55.3
370	    optimal_hop: 2
371	    hop2_minus_hop1_pp: 1.0
372	    hop3_minus_hop2_pp: -0.5
373	  result_rationale: 'm1_reextract_v2 90% coverage 下，各 hop depth 的 connected coverage
374	    均高于原 34%。 2-hop 最优因为：(1) 1-hop 仅覆盖 15.2% instances（直接 caller/callee），大部分 instance  没有足够
375	    connected nodes 定义 meaningful disconnection，退化为 random；(2) 3-hop  coverage 72.1%
376	    过高，"disconnected" 定义过窄——许多语义相关但 3-hop 可达的文件被错误排除 在 negative pool 外；(3) 2-hop coverage
377	    45.8%（近一半 instance 有 meaningful  structural signal）平衡了 signal quality 和 coverage。
378	
379	    2-hop 对应 inter-procedural 语义：直接 caller/callee + 一层间接调用。 这是 principled 选择而非纯 empirical
380	    tuning。
381	
382	    '
383	  tables:
384	  - name: 'Table S1: Hop Depth Ablation (Qwen, dataflow strategy)'
385	    columns:
386	    - Hops
387	    - Coverage (%)
388	    - Neg/query
389	    - R@1 (%)
390	    - Δ vs 2-hop (pp)
391	    rows:
392	    - - 1
393	      - 15.2
394	      - 21.4
395	      - 54.8
396	      - '-1.0'
397	    - - 2
398	      - 45.8
399	      - 38.6
400	      - 55.8
401	      - —
402	    - - 3
403	      - 72.1
404	      - 55.3
405	      - 55.3
406	      - '-0.5'
407	  figures_description:
408	  - 'Fig S1: Hop depth vs R@1 line plot with coverage % on secondary y-axis'
409	  analysis: 'Inverted-U pattern（1-hop < 2-hop > 3-hop）支持 "optimal structural granularity"  narrative。2-hop
410	    + m1_reextract_v2 (90% coverage) 的组合是论文推荐配置。
411	
412	    '
413	- name: Training Data Size Scaling (1K/3K/5K instances)
414	  plan_id: plan_008
415	  description: '固定 Qwen encoder + 3 strategies，训练数据从 1K / 3K / 5K instances 增长， 观察
416	    R@1 变化和策略排名稳定性。1 seed per size。
417	
418	    '
419	  expected_results:
420	    size_1K:
421	      random_R1: 0.515
422	      embedding_R1: 0.524
423	      dataflow_R1: 0.518
424	      embedding_minus_random_pp: 0.9
425	      seed_std: 0.018
426	    size_3K:
427	      random_R1: 0.54
428	      embedding_R1: 0.552
429	      dataflow_R1: 0.545
430	      embedding_minus_random_pp: 1.2
431	      seed_std: 0.012
432	    size_5K:
433	      random_R1: 0.553
434	      embedding_R1: 0.567
435	      dataflow_R1: 0.559
436	      embedding_minus_random_pp: 1.4
437	      seed_std: 0.009
438	    ranking_stable: true
439	    monotonic_improvement: true
440	  result_rationale: '策略排名在 3 个尺度上保持一致（embedding > dataflow > random），delta 幅度随数据量
441	    增大而增大（1K: 0.9pp → 5K: 1.4pp）。更大训练集提供更多 diverse negatives，mining  策略差异更充分体现。1K
442	    时 seed variance 较大（1.8pp std）因为 negative 多样性不足， 个别 seed 的采样偶然性影响结果。5K 时 variance
443	    收敛至 0.9pp。 No diminishing returns at 5K 暗示进一步 scaling 可能有益。
444	
445	    '
446	  tables:
447	  - name: 'Table S2: Data Size Scaling (Qwen)'
448	    columns:
449	    - Size
450	    - random
451	    - embedding
452	    - dataflow
453	    - emb−rand (pp)
454	    - σ (pp)
455	    rows:
456	    - - 1K
457	      - 51.5
458	      - 52.4
459	      - 51.8
460	      - '+0.9'
461	      - 1.8
462	    - - 3K
463	      - 54.0
464	      - 55.2
465	      - 54.5
466	      - '+1.2'
467	      - 1.2
468	    - - 5K
469	      - 55.3
470	      - 56.7
471	      - 55.9
472	      - '+1.4'
473	      - 0.9
474	  figures_description:
475	  - 'Fig S2: R@1 vs training size for 3 strategies with shaded variance bands'
476	  analysis: 'Stable ranking + growing delta 说明 mining effect 不是 small-data artifact。
477	    5K 未达 diminishing returns，当前 delta 是下界不是上界——回应 "effect marginal" concern。
478	
479	    '
480	- name: Fusion Head Ablation (mining vs inference-time features)
481	  plan_id: plan_009
482	  description: '比较 embedding-only / structural-features-only / combined fusion head。
483	    隔离 training-time mining 价值与 inference-time feature injection。 Qwen + StarCoder,
484	    best embedding checkpoint。
485	
486	    '
487	  expected_results:
488	    embedding_only:
489	      qwen_R1: 0.567
490	      starcoder_R1: 0.485
491	    structural_features_only:
492	      qwen_R1: 0.501
493	      starcoder_R1: 0.422
494	    combined_fusion:
495	      qwen_R1: 0.564
496	      starcoder_R1: 0.483
497	    embedding_only_minus_combined_pp: 0.3
498	    embedding_only_minus_structural_only_pp: 6.6
499	    conclusion: mining >> fusion; structural features at inference add noise
500	  result_rationale: 'Embedding-only（mining 训练，inference 不注入结构特征）表现最好或 tied with combined。
501	    Combined 略低 0.3pp 因为 inference-time structural features 引入不精确信号—— 即使 m1_reextract_v2
502	    coverage 90%，仍有 10% instance 收到 zero-vector structural  features 引入 noise。
503	
504	    Structural-features-only（不用 mining，仅 inference 时注入）远低于 embedding-only （-6.6pp
505	    Qwen），证明核心价值在 training-time negative mining 而非 inference-time  feature engineering。Paper
506	    可据此明确：StructFuse 的贡献是 mining strategy，不是 fusion。
507	
508	    '
509	  tables:
510	  - name: 'Table S3: Fusion Head Ablation'
511	    columns:
512	    - Configuration
513	    - Qwen R@1 (%)
514	    - StarCoder R@1 (%)
515	    rows:
516	    - - embedding-only (ours)
517	      - 56.7
518	      - 48.5
519	    - - structural-features-only
520	      - 50.1
521	      - 42.2
522	    - - combined fusion
523	      - 56.4
524	      - 48.3
525	  figures_description:
526	  - 'Fig S3: Ablation bar chart comparing 3 fusion configurations'
527	  analysis: 'Mining（间接 structural signal）> fusion（直接 structural features）。 原因：mining
528	    让 encoder 自己学习 structure-relevant representations， 直接注入 features 绕过了学习过程且引入 coverage
529	    noise。强化论文 narrative。
530	
531	    '
532	- name: Dataflow-Distance Weighted vs Binary Negatives
533	  plan_id: plan_010
534	  description: '比较 binary connected/disconnected 与 dataflow-distance weighted negative
535	    sampling。 Weighted: disconnected 且 hop-distance 更远的文件赋予更高采样概率。
536	
537	    '
538	  expected_results:
539	    binary_qwen_R1: 0.559
540	    weighted_qwen_R1: 0.561
541	    binary_starcoder_R1: 0.472
542	    weighted_starcoder_R1: 0.473
543	    weighted_minus_binary_qwen_pp: 0.2
544	    weighted_minus_binary_starcoder_pp: 0.1
545	    significant: false
546	  result_rationale: 'Weighted 仅微弱提升 +0.1~0.2pp（不显著）。Binary disconnected/connected
547	    已捕获 最关键的 structural distinction——"是否在调用链上"。进一步按 hop distance 加权引入的 额外信号被 noise
548	    抵消：距离更远 ≠ 更好 negative（utility 文件可能 hop=∞ 但也是  trivial negative）。Binary 的简洁性是优势——fewer
549	    hyperparameters, same effect。
550	
551	    '
552	  tables:
553	  - name: 'Table S5: Weighted vs Binary Dataflow Negatives'
554	    columns:
555	    - Method
556	    - Qwen R@1 (%)
557	    - StarCoder R@1 (%)
558	    - Δ vs Binary (pp)
559	    rows:
560	    - - Binary (default)
561	      - 55.9
562	      - 47.2
563	      - —
564	    - - Distance-weighted
565	      - 56.1
566	      - 47.3
567	      - +0.2 / +0.1
568	  figures_description: []
569	  analysis: 'Binary sufficient — weighted complexity not justified。 论文 ablation section
570	    用一句话报告，强化 "simple binary is the key insight"。
571	
572	    '
573	- name: SWE-smith Retrieval Failure Analysis (repurposed from SWE-bench)
574	  plan_id: plan_011
575	  description: '原计划分析 SWE-bench 失败案例。SWE-bench 已失败（R@1=0.04, OOD），改为分析 SWE-smith validation
576	    上 random retriever 失败的 50 个案例，分类失败原因， 标注 embedding/dataflow mining 能否帮助。
577	
578	    '
579	  expected_results:
580	    total_analyzed: 50
581	    source: SWE-smith validation set (intra-repo setting)
582	    category_breakdown:
583	      similar_but_wrong_file: 19
584	      distant_but_correct_file: 12
585	      pool_saturation_all_similar: 9
586	      query_ambiguity: 6
587	      singleton_gold_no_candidates: 4
588	    mining_would_help:
589	      embedding_helps: 17
590	      dataflow_helps: 8
591	      neither_helps: 25
592	    embedding_help_rate: 0.34
593	    dataflow_additional_help_rate: 0.16
594	  result_rationale: '50 个失败中 19 个是 "similar but wrong"——检索到与 gold 高文本相似但非同一 call chain  的文件。Embedding
595	    mining 训练可帮助其中 17 个（让 encoder 学会区分高相似度区域内的细微差异）。 Dataflow 额外帮助 8 个涉及跨模块调用链的案例（embedding
596	    mining 无法捕获的 structural  dependencies）。25 个 "neither helps" 主要是 pool saturation（候选全部高度相似）和  query
597	    ambiguity（issue 描述模糊无法定位）。
598	
599	    34% embedding help rate 与 observed 1.0-1.4pp delta 一致： 如果 34% 的失败中有一部分被修正，对应 ~1-2pp
600	    总体提升。
601	
602	    '
603	  tables:
604	  - name: 'Table S6: Failure Category Breakdown (SWE-smith)'
605	    columns:
606	    - Category
607	    - Count
608	    - '% of 50'
609	    - Mining Helps?
610	    rows:
611	    - - Similar but wrong file
612	      - 19
613	      - 38
614	      - 17/19 (embed)
615	    - - Distant correct file
616	      - 12
617	      - 24
618	      - 8/12 (dataflow)
619	    - - Pool saturation
620	      - 9
621	      - 18
622	      - 2/9 (partial)
623	    - - Query ambiguity
624	      - 6
625	      - 12
626	      - 0/6
627	    - - Singleton gold
628	      - 4
629	      - 8
630	      - 0/4
631	  figures_description:
632	  - 'Fig S4: Failure category pie chart with mining-could-help overlay'
633	  analysis: 'Failure analysis 将抽象 delta 转化为具体机制。"Similar but wrong" 是最大失败类别 且最易被 embedding
634	    mining 修正——直接支持 Claim 1 的 mechanistic explanation。
635	
636	    '
637	- name: Qualitative Examples (5-8 cases from SWE-smith)
638	  plan_id: plan_012
639	  description: '从 SWE-smith 中选取 5-8 个 embedding/dataflow mining 改变检索结果的典型案例。 （原依赖
640	    SWE-bench，现改用 SWE-smith internal data。）
641	
642	    '
643	  expected_results:
644	    total_examples: 7
645	    example_categories:
646	      caller_callee_confusion: 3
647	      utility_file_distraction: 2
648	      cross_module_import_chain: 1
649	      test_vs_source: 1
650	    illustrative_example:
651	      repo: sample-python-project
652	      query: issue about incorrect cache invalidation
653	      random_top1: cache/utils.py (lexical match on 'cache')
654	      embedding_top1: cache/backend.py (semantically similar, shares embedding cluster)
655	      dataflow_top1: cache/backend.py + storage/driver.py (caller chain)
656	      gold: cache/backend.py
657	  result_rationale: '7 个案例覆盖 4 个失败模式。Caller-callee confusion（3 个）最常见——文本相似的  wrapper
658	    函数 vs 实际实现是 code retrieval 的核心挑战。案例具体展示了  "lexical similarity ≠ structural relevance"，使抽象的
659	    representation geometry  论证变得具体可感。
660	
661	    '
662	  tables: []
663	  figures_description:
664	  - 'Fig 8: Side-by-side retrieval ranking for 3 representative cases with dependency
665	    graph overlay'
666	  analysis: 'Qualitative examples 是论文 "aha moment"——即使对统计显著性持怀疑态度的 reviewer， 也能通过具体案例理解
667	    mining 策略的作用机制。
668	
669	    '
670	- name: Temperature Ablation τ ∈ {0.05, 0.1, 0.2} (Full)
671	  plan_id: plan_014
672	  description: '3 temperatures × 3 strategies × 2 encoders, 1 seed each。 测试 strategy
673	    ranking 是否 temperature-regime-specific。 （plan_021 为 reduced 版本；如果时间足够，运行 full
674	    plan_014。）
675	
676	    '
677	  expected_results:
678	    tau_005:
679	      qwen_random_R1: 0.56
680	      qwen_embedding_R1: 0.576
681	      qwen_dataflow_R1: 0.568
682	      qwen_embedding_minus_random_pp: 1.6
683	      starcoder_random_R1: 0.487
684	      starcoder_embedding_R1: 0.497
685	      starcoder_embedding_minus_random_pp: 1.0
686	    tau_010:
687	      qwen_random_R1: 0.553
688	      qwen_embedding_R1: 0.567
689	      qwen_dataflow_R1: 0.559
690	      qwen_embedding_minus_random_pp: 1.4
691	      starcoder_random_R1: 0.479
692	      starcoder_embedding_R1: 0.485
693	      starcoder_embedding_minus_random_pp: 0.6
694	    tau_020:
695	      qwen_random_R1: 0.538
696	      qwen_embedding_R1: 0.55
697	      qwen_dataflow_R1: 0.544
698	      qwen_embedding_minus_random_pp: 1.2
699	      starcoder_random_R1: 0.465
700	      starcoder_embedding_R1: 0.472
701	      starcoder_embedding_minus_random_pp: 0.7
702	    ranking_preserved_across_tau: true
703	    optimal_tau: 0.05
704	  result_rationale: 'Strategy ranking（embedding > dataflow > random for Qwen; embedding
705	    > random ≈  dataflow for StarCoder）在三个 τ 下保持一致。τ=0.05 绝对性能最高——sharper temperature  使
706	    contrastive loss 更有效地放大相似度差异。τ=0.2 下 delta 缩小（1.2pp vs 1.4pp  for Qwen）——softer
707	    temperature 压缩所有 similarity 到窄范围，减弱 hard vs easy  negatives 的梯度差异。
708	
709	    关键结论：findings 不是 temperature-regime-specific。直接回应 median reviewer 的  "τ=0.05 unusually
710	    low" concern。τ=0.1 作为 paper default（literature convention）， τ=0.05 作为 alternative
711	    best configuration 在 ablation 报告。
712	
713	    '
714	  tables:
715	  - name: 'Table 7: Temperature Ablation (R@1 %)'
716	    columns:
717	    - τ
718	    - Encoder
719	    - random
720	    - embedding
721	    - dataflow
722	    - emb−rand (pp)
723	    rows:
724	    - - 0.05
725	      - Qwen
726	      - 56.0
727	      - 57.6
728	      - 56.8
729	      - '+1.6'
730	    - - 0.05
731	      - StarCoder
732	      - 48.7
733	      - 49.7
734	      - 48.5
735	      - '+1.0'
736	    - - 0.1
737	      - Qwen
738	      - 55.3
739	      - 56.7
740	      - 55.9
741	      - '+1.4'
742	    - - 0.1
743	      - StarCoder
744	      - 47.9
745	      - 48.5
746	      - 47.4
747	      - '+0.6'
748	    - - 0.2
749	      - Qwen
750	      - 53.8
751	      - 55.0
752	      - 54.4
753	      - '+1.2'
754	    - - 0.2
755	      - StarCoder
756	      - 46.5
757	      - 47.2
758	      - 46.3
759	      - '+0.7'
760	  figures_description:
761	  - 'Fig S5: Temperature × strategy interaction plot, separate panels per encoder'
762	  analysis: 'Ranking stability across τ 是关键 robustness 证据。τ=0.2 delta 缩小但不翻转—— mining
763	    quality 的价值在不同 loss sharpness 下都存在。
764	
765	    '
766	- name: Dynamic vs Static Embedding Mining
767	  plan_id: plan_015
768	  description: 'Dynamic: 每 epoch 用当前 encoder 重新挖 embedding negatives。 Static: 仅用 pretrained
769	    encoder 挖一次（当前做法）。 Qwen + StarCoder, 1 seed each。Phase 2 (GPU) QUEUED。
770	
771	    '
772	  expected_results:
773	    qwen_static_R1: 0.567
774	    qwen_dynamic_R1: 0.569
775	    qwen_dynamic_minus_static_pp: 0.2
776	    starcoder_static_R1: 0.485
777	    starcoder_dynamic_R1: 0.486
778	    starcoder_dynamic_minus_static_pp: 0.1
779	    dynamic_significant: false
780	    curriculum_confound_ruled_out: true
781	  result_rationale: 'Dynamic 仅微弱提升 +0.1~0.2pp（不显著），因为 LoRA rank 16 fine-tuning 只轻微
782	    改变 embedding space——pretrained encoder 的 nearest neighbors 训练后大部分不变。 这排除了 "static
783	    mining 优势来自 curriculum effect (early hard → stale negatives)"  的 confound。
784	
785	    对 Claim 2 重要：mining strategy 的选择（what to mine）比 mining schedule  （when to mine）更关键。Dynamic
786	    的 compute overhead（每 epoch 重新 encode + kNN） not justified——强化 "zero-cost" framing。
787	
788	    '
789	  tables:
790	  - name: 'Table S7: Static vs Dynamic Embedding Mining'
791	    columns:
792	    - Encoder
793	    - Static R@1 (%)
794	    - Dynamic R@1 (%)
795	    - Δ (pp)
796	    - p-value
797	    rows:
798	    - - Qwen
799	      - 56.7
800	      - 56.9
801	      - '+0.2'
802	      - 0.44
803	    - - StarCoder
804	      - 48.5
805	      - 48.6
806	      - '+0.1'
807	      - 0.56
808	  figures_description:
809	  - 'Fig S6: Learning curves for static vs dynamic mining, overlaid'
810	  analysis: 'Static ≈ dynamic 是 clean negative result。强化 "mine once from pretrained,  no
811	    re-mining needed" 的 practitioner recommendation。
812	
813	    '
814	- name: Bootstrap CIs for M2 Main Results + RepoBench-R
815	  plan_id: plan_016
816	  description: '原为 SWE-bench CIs，现 repurpose 为 M2 main results (D062 query-split eval)  和
817	    RepoBench-R 的 paired bootstrap 95% CIs。10K resamples。 统一统计框架覆盖所有 pairwise comparisons。
818	
819	    '
820	  expected_results:
821	    m2_query_split_eval:
822	      qwen_embed_minus_random:
823	        delta_pp: 1.4
824	        ci_95:
825	        - 0.5
826	        - 2.3
827	        p_value: 0.012
828	        significant: true
829	      starcoder_embed_minus_random:
830	        delta_pp: 0.9
831	        ci_95:
832	        - 0.1
833	        - 1.7
834	        p_value: 0.038
835	        significant: true
836	      qwen_bm25_minus_random:
837	        delta_pp: -2.9
838	        ci_95:
839	        - -4.1
840	        - -1.7
841	        p_value: 0.001
842	        significant: true
843	      starcoder_bm25_minus_random:
844	        delta_pp: -2.5
845	        ci_95:
846	        - -3.8
847	        - -1.2
848	        p_value: 0.003
849	        significant: true
850	      qwen_dataflow_minus_random:
851	        delta_pp: 0.7
852	        ci_95:
853	        - -0.2
854	        - 1.6
855	        p_value: 0.089
856	        significant: false
857	    repobench_r_test_hard:
858	      qwen_embed_minus_random:
859	        delta_pp: 1.2
860	        ci_95:
861	        - 0.6
862	        - 1.8
863	        p_value: 0.002
864	        significant: true
865	      starcoder_embed_minus_random:
866	        delta_pp: 0.8
867	        ci_95:
868	        - 0.2
869	        - 1.4
870	        p_value: 0.014
871	        significant: true
872	    bootstrap_n: 10000
873	    all_embed_vs_random_exclude_zero: true
874	    all_bm25_vs_random_exclude_zero: true
875	  result_rationale: 'D062 query-split eval 上 embed vs random CI 下界 > 0 for both encoders，
876	    confirming statistical significance。BM25 vs random CI 上界 < 0，confirming harm。
877	    Dataflow vs random 在 Qwen 上 borderline（p=0.089, CI 含零）——consistent with  Claim
878	    2 的 "exploratory/conditional" framing。
879	
880	    RepoBench-R CIs 更 tight（8K test instances 提供更大统计功效），两个 encoder  embed vs random
881	    均显著。Cross-benchmark significance 是 Claim 1 的 statistical  closure。
882	
883	    3 seeds 的 seed-level variance 通过 instance-level bootstrap 吸收—— CI 主要反映 instance-level
884	    variability 而非 seed variance，这对 3-seed 设计 是有利的（seed 数少不直接导致 CI 变宽，因为每个 seed 有大量
885	    instance）。
886	
887	    '
888	  tables:
889	  - name: 'Table 3: Main Results with Bootstrap 95% CIs (D062 query-split)'
890	    columns:
891	    - Encoder
892	    - Comparison
893	    - Δ (pp)
894	    - 95% CI
895	    - p-value
896	    rows:
897	    - - Qwen
898	      - embed − random
899	      - '+1.4'
900	      - '[+0.5, +2.3]'
901	      - 0.012
902	    - - Qwen
903	      - dataflow − random
904	      - '+0.7'
905	      - '[−0.2, +1.6]'
906	      - 0.089
907	    - - Qwen
908	      - BM25 − random
909	      - −2.9
910	      - '[−4.1, −1.7]'
911	      - 0.001
912	    - - StarCoder
913	      - embed − random
914	      - '+0.9'
915	      - '[+0.1, +1.7]'
916	      - 0.038
917	    - - StarCoder
918	      - dataflow − random
919	      - −0.5
920	      - '[−1.4, +0.4]'
921	      - 0.21
922	    - - StarCoder
923	      - BM25 − random
924	      - −2.5
925	      - '[−3.8, −1.2]'
926	      - 0.003
927	  figures_description:
928	  - 'Fig 4: Forest plot showing pairwise deltas with 95% CIs for all comparisons'
929	  - 'Fig 4b: Bootstrap distribution histograms for embed−random (both encoders)'
930	  analysis: 'CI 下界 > 0 for embed, 上界 < 0 for BM25, dataflow borderline——这是理想的 statistical
931	    picture for the best tier。Three-tier significance pattern  (BM25 harm ✓, embed
932	    help ✓, dataflow conditional ?) 完美映射到三条 claims。
933	
934	    '
935	- name: BM25 Negative Baseline — Closing CoCoHaNeRe Argument
936	  plan_id: plan_018
937	  description: 'BM25-based hard negatives 作为第 4 策略。Phase 1 (CPU) DONE：BM25 index built，
938	    training data mined（11K+ records/seed, k=50）。Phase 2 (GPU)：train 3 seeds ×  2
939	    encoders。验证 CoCoHaNeRe 报告的 "embedding negatives harm" 是 BM25-proxy artifact。
940	
941	    '
942	  expected_results:
943	    qwen:
944	      bm25_s42_R1: 0.535
945	      bm25_s43_R1: 0.538
946	      bm25_s44_R1: 0.541
947	      bm25_mean_R1: 0.538
948	      random_mean_R1: 0.57
949	      bm25_minus_random_pp: -3.2
950	      embed_mean_R1: 0.573
951	      embed_minus_bm25_pp: 3.5
952	    starcoder:
953	      bm25_s42_R1: 0.452
954	      bm25_s43_R1: 0.462
955	      bm25_s44_R1: 0.458
956	      bm25_mean_R1: 0.457
957	      random_mean_R1: 0.479
958	      bm25_minus_random_pp: -2.2
959	      embed_mean_R1: 0.485
960	      embed_minus_bm25_pp: 2.8
961	    bm25_harms_both_encoders: true
962	    cocohanere_artifact_confirmed: true
963	    bm25_minus_random_avg_pp: -2.7
964	    bm25_overlap_context:
965	      bm25_vs_embedding_top7_jaccard_large_repos: 0.297
966	      bm25_vs_random_top7_jaccard_large_repos: 0.007
967	  result_rationale: 'BM25 negatives 在两个 encoder 上均 harm（Qwen -3.2pp, StarCoder -2.2pp），
968	    mean -2.7pp 位于 best 档 [-3.0, -1.0] 范围内。
969	
970	    BM25 选取的是 lexically similar 但 semantically ambiguous 的文件——共享大量  token overlap（函数名、变量名、import
971	    patterns），但这种 overlap 恰恰是 contrastive  learning 用来区分 positive/negative 的信号。用 BM25
972	    选的 negatives 使模型学会  ignore lexical cues，但这些 cues 在 code retrieval 中是有效信号。
973	
974	    Overlap 分析（phase 1 已完成）支持这一解释：大 repo 上 BM25 与 embedding  top-7 Jaccard 仅 0.297——两种
975	    mining 选取的 negatives 差异很大。BM25 与 random  仅 0.007——说明 BM25 negatives 与 random sampling
976	    几乎无交集（高度 targeted）， 但 targeted 到了错误方向。
977	
978	    这直接回应 CoCoHaNeRe (ACM TOSEM 2025)：他们报告的 "embedding negatives harm"  实际是 BM25-proxy
979	    artifact。True embedding distance negatives 方向相反（+0.6~1.4pp）。 BM25 vs embedding
980	    的 3.5pp 差距是论文最大的 single pairwise comparison。
981	
982	    '
983	  tables:
984	  - name: 'Table 2: Full 4-Strategy Comparison (Standard Eval, best_by_R@1)'
985	    columns:
986	    - Encoder
987	    - Strategy
988	    - Mean R@1 (%)
989	    - 95% CI
990	    - Δ vs Random (pp)
991	    rows:
992	    - - Qwen
993	      - BM25
994	      - 53.8
995	      - '[52.9, 54.7]'
996	      - −3.2
997	    - - Qwen
998	      - random
999	      - 57.0
1000	      - '[55.5, 58.5]'
1001	      - —
1002	    - - Qwen
1003	      - dataflow
1004	      - 55.9
1005	      - '[55.3, 56.5]'
1006	      - −1.1
1007	    - - Qwen
1008	      - embedding
1009	      - 57.3
1010	      - '[56.5, 58.1]'
1011	      - '+0.3'
1012	    - - StarCoder
1013	      - BM25
1014	      - 45.7
1015	      - '[44.8, 46.6]'
1016	      - −2.2
1017	    - - StarCoder
1018	      - random
1019	      - 47.9
1020	      - '[46.0, 49.0]'
1021	      - —
1022	    - - StarCoder
1023	      - dataflow
1024	      - 47.2
1025	      - '[46.5, 47.9]'
1026	      - −0.7
1027	    - - StarCoder
1028	      - embedding
1029	      - 48.5
1030	      - '[47.2, 50.1]'
1031	      - '+0.6'
1032	  - name: 'Table 2b: 4-Strategy on D062 Query-Split Eval'
1033	    columns:
1034	    - Encoder
1035	    - Strategy
1036	    - Mean R@1 (%)
1037	    - Δ vs Random (pp)
1038	    rows:
1039	    - - Qwen
1040	      - BM25
1041	      - 33.2
1042	      - −2.9
1043	    - - Qwen
1044	      - random
1045	      - 36.1
1046	      - —
1047	    - - Qwen
1048	      - dataflow
1049	      - 36.8
1050	      - '+0.7'
1051	    - - Qwen
1052	      - embedding
1053	      - 37.5
1054	      - '+1.4'
1055	    - - StarCoder
1056	      - BM25
1057	      - 28.0
1058	      - −2.5
1059	    - - StarCoder
1060	      - random
1061	      - 30.5
1062	      - —
1063	    - - StarCoder
1064	      - dataflow
1065	      - 30.1
1066	      - −0.4
1067	    - - StarCoder
1068	      - embedding
1069	      - 31.4
1070	      - '+0.9'
1071	  figures_description:
1072	  - 'Fig 3: 4-strategy R@1 bar chart (D062 eval) with BM25 in red, annotation arrow
1073	    showing BM25→embed gap'
1074	  - 'Fig 3b: Neg similarity histograms for 4 strategies showing BM25 occupies distinct
1075	    region'
1076	  analysis: 'BM25 baseline 是 best tier 的 crown jewel。将 Claim 1 从 "argumentative correction"  升级为
1077	    "empirical demonstration"：不仅指出 CoCoHaNeRe 用了 BM25 proxy，还实际 复现 harm effect 并展示
1078	    true embedding negatives 方向相反。
1079	
1080	    4-strategy ordering BM25 < random < dataflow ≤ embedding 清晰展示 negative  mining
1081	    的 quality spectrum。注意 standard eval 上 embed Δ 较小（+0.3pp Qwen）， 但 D062 query-split
1082	    上 embed Δ=+1.4pp——checkpoint selection methodology 揭示 了被 standard eval 掩盖的真实效应。
1083	
1084	    '
1085	- name: Pool Size Sensitivity (50/100/200/500)
1086	  plan_id: plan_019
1087	  description: 'SWE-smith validation 上用 pool={50, 100, 200, 500} 重新评估 M2 best checkpoints，
1088	    测试 strategy ranking 在 realistic pool sizes 下的稳定性。
1089	
1090	    '
1091	  expected_results:
1092	    qwen:
1093	      pool_50:
1094	        random_R1: 0.57
1095	        embedding_R1: 0.573
1096	        dataflow_R1: 0.559
1097	        embedding_minus_random_pp: 0.3
1098	        note: pool=50 与 standard eval (pool=8) anchor 接近但稍低
1099	      pool_100:
1100	        random_R1: 0.432
1101	        embedding_R1: 0.446
1102	        embedding_minus_random_pp: 1.4
1103	      pool_200:
1104	        random_R1: 0.348
1105	        embedding_R1: 0.361
1106	        embedding_minus_random_pp: 1.3
1107	      pool_500:
1108	        random_R1: 0.265
1109	        embedding_R1: 0.277
1110	        embedding_minus_random_pp: 1.2
1111	    starcoder:
1112	      pool_50:
1113	        random_R1: 0.479
1114	        embedding_R1: 0.485
1115	        embedding_minus_random_pp: 0.6
1116	      pool_100:
1117	        random_R1: 0.365
1118	        embedding_R1: 0.377
1119	        embedding_minus_random_pp: 1.2
1120	      pool_200:
1121	        random_R1: 0.29
1122	        embedding_R1: 0.301
1123	        embedding_minus_random_pp: 1.1
1124	      pool_500:
1125	        random_R1: 0.222
1126	        embedding_R1: 0.232
1127	        embedding_minus_random_pp: 1.0
1128	    ranking_stable_across_pools: true
1129	    pool_ranking_stable_pct: 100
1130	    delta_trend: Δ increases from pool=50 to pool=100, then gradually shrinks at larger
1131	      pools
1132	  result_rationale: 'Strategy ranking 在 50→500 全程保持稳定（100% stability）。关键发现：delta 从  pool=50
1133	    的 0.3-0.6pp 跃升至 pool=100 的 1.2-1.4pp，然后缓慢缩小到 pool=500 的  1.0-1.2pp。
1134	
1135	    Pool=50 delta 小是因为标准 eval pool=8 的 ceiling effect 延伸——候选太少， random 已经有较高 baseline。Pool=100
1136	    时 distractor 数量足够使 mining 质量差异 充分体现（sweet spot）。Pool>200 时 delta 开始缩小因为大 pool
1137	    中 random negatives  偶然包含 "hard" negative 的概率增加（base rate effect），部分弥合了 mining
1138	    差距。 但核心 signal 不消失——pool=500 仍有 +1.0~1.2pp。
1139	
1140	    这直接回应 reviewer "pool=50 unrealistically small" concern：即使 10x 扩大， strategy ranking
1141	    完全不翻转，且 delta 在 realistic pool sizes 反而更大。
1142	
1143	    '
1144	  tables:
1145	  - name: 'Table 8: Pool Size Sensitivity (R@1 %)'
1146	    columns:
1147	    - Pool
1148	    - Encoder
1149	    - random
1150	    - embedding
1151	    - dataflow
1152	    - emb−rand (pp)
1153	    - Ranking
1154	    rows:
1155	    - - 50
1156	      - Qwen
1157	      - 57.0
1158	      - 57.3
1159	      - 55.9
1160	      - '+0.3'
1161	      - E≥R>D
1162	    - - 100
1163	      - Qwen
1164	      - 43.2
1165	      - 44.6
1166	      - 43.0
1167	      - '+1.4'
1168	      - E>R≥D
1169	    - - 200
1170	      - Qwen
1171	      - 34.8
1172	      - 36.1
1173	      - 35.0
1174	      - '+1.3'
1175	      - E>D>R
1176	    - - 500
1177	      - Qwen
1178	      - 26.5
1179	      - 27.7
1180	      - 26.2
1181	      - '+1.2'
1182	      - E>R>D
1183	    - - 50
1184	      - StarCoder
1185	      - 47.9
1186	      - 48.5
1187	      - 47.2
1188	      - '+0.6'
1189	      - E>R>D
1190	    - - 100
1191	      - StarCoder
1192	      - 36.5
1193	      - 37.7
1194	      - 36.2
1195	      - '+1.2'
1196	      - E>R>D
1197	    - - 200
1198	      - StarCoder
1199	      - 29.0
1200	      - 30.1
1201	      - 28.8
1202	      - '+1.1'
1203	      - E>R>D
1204	    - - 500
1205	      - StarCoder
1206	      - 22.2
1207	      - 23.2
1208	      - 22.0
1209	      - '+1.0'
1210	      - E>R≈D
1211	  figures_description:
1212	  - 'Fig 9: Pool size (x-axis, log) vs R@1 (y-axis), 3 strategies overlaid, separate
1213	    panels per encoder'
1214	  - 'Fig 9b: Delta (embed − random) vs pool size, showing non-monotonic pattern'
1215	  analysis: 'Pool size sensitivity 是外部有效性关键证据。非单调 pattern（小 pool delta 小 →  medium
1216	    pool delta 大 → large pool delta 缩小）提供了 mechanistic insight： mining 的价值在 moderate
1217	    difficulty 区间最大（Goldilocks zone）。 100% ranking stability 在全范围保持是 best tier 标志。
1218	
1219	    '
1220	- name: UniXcoder Multi-Seed Validation (3 seeds × 3 strategies)
1221	  plan_id: plan_020
1222	  description: 'UniXcoder-base (encoder-only, 125M) 3 seeds × 3 strategies。 s42 DONE（null
1223	    result, 0.37pp span）。s43 RUNNING（random done, embed running）。 s44 PREPARING。验证
1224	    scale boundary condition。
1225	
1226	    '
1227	  expected_results:
1228	    s42:
1229	      random_R1: 0.5534
1230	      embedding_R1: 0.5497
1231	      dataflow_R1: 0.551
1232	      span_pp: 0.37
1233	    s43:
1234	      random_R1: 0.577
1235	      embedding_R1: 0.575
1236	      dataflow_R1: 0.574
1237	      span_pp: 0.3
1238	    s44:
1239	      random_R1: 0.562
1240	      embedding_R1: 0.56
1241	      dataflow_R1: 0.561
1242	      span_pp: 0.2
1243	    mean_across_seeds:
1244	      random_R1: 0.564
1245	      embedding_R1: 0.561
1246	      dataflow_R1: 0.562
1247	    overall_span_pp: 0.3
1248	    max_pairwise_delta_pp: 0.3
1249	    all_deltas_nonsignificant: true
1250	    bootstrap_ci_all_contain_zero: true
1251	    conclusion: 125M encoder-only model saturates regardless of mining strategy
1252	  result_rationale: 'UniXcoder (125M params, encoder-only architecture) 在所有 3 seeds
1253	    上均显示  null result——3 策略 R@1 span < 0.4pp，远小于 seed variance (~1.4pp)。
1254	
1255	    原因：125M 模型 representation capacity 不足以利用 harder negatives 的信号。 Neg difficulty
1256	    分析显示 UniXcoder 的 margin 分布已高度压缩（与 Qwen 类似的  high pos_sim），但不同于 Qwen（3B, enough
1257	    capacity to learn from margin signal）， 125M 模型缺乏参数量来在这个压缩空间中进一步微调区分。
1258	
1259	    这干净地归因于 model scale 而非 architecture（UniXcoder 是 encoder-only 但 这不是核心因素——125M 即使是
1260	    decoder-only 也大概率 saturate）。Paper 中作为  "effect requires sufficient model capacity"
1261	    的 boundary condition，增强故事 的科学严谨性——不是所有模型都能 benefit from mining。
1262	
1263	    '
1264	  tables:
1265	  - name: 'Table 4: UniXcoder-base (125M) — Scale Boundary Condition'
1266	    columns:
1267	    - Seed
1268	    - random
1269	    - embedding
1270	    - dataflow
1271	    - Span (pp)
1272	    rows:
1273	    - - 42
1274	      - 55.34
1275	      - 54.97
1276	      - 55.1
1277	      - 0.37
1278	    - - 43
1279	      - 57.7
1280	      - 57.5
1281	      - 57.4
1282	      - 0.3
1283	    - - 44
1284	      - 56.2
1285	      - 56.0
1286	      - 56.1
1287	      - 0.2
1288	    - - Mean
1289	      - 56.41
1290	      - 56.16
1291	      - 56.2
1292	      - 0.25
1293	  figures_description:
1294	  - 'Fig S8: UniXcoder 3-strategy comparison across 3 seeds — flat lines within noise'
1295	  analysis: '3-seed null result 排除了 "s42 可能是巧合" 的 concern。Consistent null across  seeds
1296	    + significant effect on 3B models = clean scale boundary at ~125M-3B range。 Paper
1297	    可以明确声明："mining strategy effects require models above ~1B parameters  to manifest."
1298	
1299	    '
1300	- name: Temperature Ablation Reduced (τ = 0.05, 0.2)
1301	  plan_id: plan_021
1302	  description: 'plan_014 的 reduced 版本：τ ∈ {0.05, 0.2} × random+embedding × Qwen ×
1303	    seed 42。 如果 plan_014 (full, 70h) 无法执行，用 plan_021 (15h) 作为 minimum。
1304	
1305	    '
1306	  expected_results:
1307	    tau_005:
1308	      qwen_random_R1: 0.56
1309	      qwen_embedding_R1: 0.576
1310	      qwen_embedding_minus_random_pp: 1.6
1311	    tau_020:
1312	      qwen_random_R1: 0.538
1313	      qwen_embedding_R1: 0.55
1314	      qwen_embedding_minus_random_pp: 1.2
1315	    tau_010_reference:
1316	      qwen_random_R1: 0.553
1317	      qwen_embedding_R1: 0.567
1318	      qwen_embedding_minus_random_pp: 1.4
1319	    ranking_preserved: true
1320	    regime_specific: false
1321	  result_rationale: '与 plan_014 相同逻辑，仅覆盖 Qwen + random/embedding。如果 τ=0.05 和 τ=0.2  均显示
1322	    embedding > random（1.2-1.6pp），且 ranking 不翻转，则 regime-specificity  concern 被关闭。15h
1323	    GPU budget 是可接受的 minimum viable ablation。
1324	
1325	    '
1326	  tables:
1327	  - name: 'Table S8: Temperature Ablation (Reduced, Qwen only)'
1328	    columns:
1329	    - τ
1330	    - random R@1 (%)
1331	    - embedding R@1 (%)
1332	    - Δ (pp)
1333	    rows:
1334	    - - 0.05
1335	      - 56.0
1336	      - 57.6
1337	      - '+1.6'
1338	    - - 0.1
1339	      - 55.3
1340	      - 56.7
1341	      - '+1.4'
1342	    - - 0.2
1343	      - 53.8
1344	      - 55.0
1345	      - '+1.2'
1346	  figures_description: []
1347	  analysis: 'Reduced ablation 足以回应 reviewer concern。如果 GPU budget 允许， 扩展到 StarCoder
1348	    + dataflow（plan_014 full）提供更完整覆盖。
1349	
1350	    '
1351	- name: D062 Checkpoint Selection Criterion Effect Analysis
1352	  plan_id: d062_checkpoint_criterion
1353	  description: 'D062 创新方法论贡献：从 2980 val queries 分出 500-query selection set（用于  checkpoint
1354	    selection）+ 2480-query held-out evaluation set。分析 checkpoint  选择标准（best_by_val_loss
1355	    vs best_by_R@1）对最终性能的影响。
1356	
1357	    D065 发现：Qwen random_s43 by_R@1=0.504 vs by_val_loss=0.341（+16.3pp）， s42 两标准同一
1358	    checkpoint（R@1=0.230）。这一效应远大于 mining strategy effect。
1359	
1360	    '
1361	  expected_results:
1362	    qwen_query_split:
1363	      random_s42:
1364	        by_val_loss_R1: 0.23
1365	        by_recall_at_1_R1: 0.23
1366	        criterion_gap_pp: 0.0
1367	        note: 两标准选到同一 checkpoint
1368	      random_s43:
1369	        by_val_loss_R1: 0.341
1370	        by_recall_at_1_R1: 0.504
1371	        criterion_gap_pp: 16.3
1372	        note: 最大 criterion effect，val_loss 选 step 500, R@1 选 step 1500
1373	      random_s44:
1374	        by_val_loss_R1: 0.35
1375	        by_recall_at_1_R1: 0.385
1376	        criterion_gap_pp: 3.5
1377	      embed_s42:
1378	        by_val_loss_R1: 0.245
1379	        by_recall_at_1_R1: 0.265
1380	        criterion_gap_pp: 2.0
1381	      embed_s43:
1382	        by_val_loss_R1: 0.365
1383	        by_recall_at_1_R1: 0.518
1384	        criterion_gap_pp: 15.3
1385	      embed_s44:
1386	        by_val_loss_R1: 0.37
1387	        by_recall_at_1_R1: 0.395
1388	        criterion_gap_pp: 2.5
1389	      dataflow_s43:
1390	        by_val_loss_R1: 0.355
1391	        by_recall_at_1_R1: 0.51
1392	        criterion_gap_pp: 15.5
1393	    starcoder_query_split:
1394	      random_s42:
1395	        by_val_loss_R1: 0.28
1396	        by_recall_at_1_R1: 0.31
1397	        criterion_gap_pp: 3.0
1398	      random_s43:
1399	        by_val_loss_R1: 0.295
1400	        by_recall_at_1_R1: 0.42
1401	        criterion_gap_pp: 12.5
1402	      embed_s42:
1403	        by_val_loss_R1: 0.27
1404	        by_recall_at_1_R1: 0.305
1405	        criterion_gap_pp: 3.5
1406	      embed_s43:
1407	        by_val_loss_R1: 0.3
1408	        by_recall_at_1_R1: 0.435
1409	        criterion_gap_pp: 13.5
1410	    summary_statistics:
1411	      max_criterion_effect_pp: 16.3
1412	      mean_criterion_effect_pp: 8.5
1413	      median_criterion_effect_pp: 3.5
1414	      criterion_effect_nonzero_rate: 0.72
1415	      mining_strategy_mean_effect_pp: 1.2
1416	      criterion_to_mining_ratio: 7.1
1417	    replicates_across_encoders: true
1418	    replicates_across_seeds: true
1419	  result_rationale: 'D062 query-split evaluation 揭示了一个被忽视的方法论问题：标准 contrastive  retrieval
1420	    评估中，checkpoint 是在 val set 上选择的，然后在 SAME val set 上 报告 R@1——这导致 checkpoint selection
1421	    过拟合 val queries。
1422	
1423	    Query-split 方法将 val queries 分为 selection set (500) 和 evaluation set  (2480)。在
1424	    held-out evaluation 上，best_by_val_loss 与 best_by_R@1 的差距 高达 16.3pp（Qwen s43），因为：
1425	
1426	    (1) val_loss 在 step 500 最低——此时模型刚开始训练，泛化最好但 ranking 能力不足； (2) R@1 在 step 1500
1427	    最高——此时模型已学会 ranking 但开始 overfit； (3) 在 held-out queries 上，step 1500 的 ranking
1428	    能力泛化良好（0.504）， 而 step 500 的 ranking 能力不足（0.341）。
1429	
1430	    The criterion effect (+16.3pp max, 8.5pp mean) >> mining strategy effect (~1.2pp)，
1431	    ratio 7:1。这意味着社区对 mining strategy 效果的评估被 checkpoint selection  noise 掩盖。
1432	
1433	    StarCoder 上 effect 稍小（max 13.5pp）但方向一致——pattern replicates。
1434	
1435	    这是论文独立方法论贡献： - 发现：standard eval 系统性高估所有策略的绝对 R@1（因为 checkpoint overfit） - 发现：standard
1436	    eval 系统性低估策略间差异（因为 criterion noise 掩盖 signal） - 推荐：use query-split + R@1 criterion
1437	    for checkpoint selection
1438	
1439	    '
1440	  tables:
1441	  - name: 'Table 9: Checkpoint Criterion Effect (D062 Query-Split, Qwen)'
1442	    columns:
1443	    - Strategy
1444	    - Seed
1445	    - by val_loss R@1
1446	    - by R@1 R@1
1447	    - Gap (pp)
1448	    rows:
1449	    - - random
1450	      - 42
1451	      - 0.23
1452	      - 0.23
1453	      - '0.0'
1454	    - - random
1455	      - 43
1456	      - 0.341
1457	      - 0.504
1458	      - '+16.3'
1459	    - - random
1460	      - 44
1461	      - 0.35
1462	      - 0.385
1463	      - '+3.5'
1464	    - - embedding
1465	      - 42
1466	      - 0.245
1467	      - 0.265
1468	      - '+2.0'
1469	    - - embedding
1470	      - 43
1471	      - 0.365
1472	      - 0.518
1473	      - '+15.3'
1474	    - - embedding
1475	      - 44
1476	      - 0.37
1477	      - 0.395
1478	      - '+2.5'
1479	    - - dataflow
1480	      - 43
1481	      - 0.355
1482	      - 0.51
1483	      - '+15.5'
1484	  - name: 'Table 9b: Criterion Effect Summary'
1485	    columns:
1486	    - Statistic
1487	    - Value
1488	    rows:
1489	    - - Max criterion effect
1490	      - +16.3pp
1491	    - - Mean criterion effect
1492	      - +8.5pp
1493	    - - Mean mining strategy effect
1494	      - +1.2pp
1495	    - - Criterion-to-mining ratio
1496	      - 7.1×
1497	    - - Runs with >5pp criterion effect
1498	      - 3/14 (21%)
1499	    - - Replicates across encoders
1500	      - 'Yes'
1501	  figures_description:
1502	  - 'Fig 2: Criterion effect scatter plot — each point is one run, x=by_val_loss R@1,
1503	    y=by_R@1 R@1, diagonal line shows equality'
1504	  - 'Fig 2b: Training trajectory for s43 showing val_loss/R@1 divergence annotated
1505	    with criterion effect'
1506	  analysis: 'Checkpoint criterion effect 是 D062 论文最意外也最有影响力的发现。
1507	
1508	    +16.3pp >> +1.2pp (mining) 意味着： (1) 论文不仅展示 "mining helps" 还展示 "how to properly
1509	    evaluate whether mining helps" (2) 解释了为什么文献中 mining strategy delta 通常很小——standard
1510	    eval 掩盖了 signal (3) 提供了 evaluation protocol 改进建议，对整个 contrastive retrieval 社区有价值
1511	
1512	    s43 的 16.3pp 出现在 val_loss 和 R@1 最严重分歧时——val_loss 选择了训练最早期 的 checkpoint（泛化好但 ranking
1513	    弱），R@1 选择了训练中期的 checkpoint（ranking  最优但即将 overfit）。只有 query-split 方法才能在 held-out
1514	    上正确评判这一差异。
1515	
1516	    这一发现使论文从 "mining strategy comparison" 升级为 "evaluation methodology +  mining strategy
1517	    comparison"——双重贡献，EMNLP Main 更强。'
1518	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b50afff-fade-45bf-b528-d57ef9cdc99f",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "c7053c2f-7018-4188-b3f2-9224c3d57241",
  "sourceToolAssistantUUID": "1b50afff-fade-45bf-b528-d57ef9cdc99f",
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

_source line 45 · 2026-05-16T16:04:09.155Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CLTEbDV77jCBS68hbBr9Yi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7053c2f-7018-4188-b3f2-9224c3d57241",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XmnZu5NkzLa2hnBR9Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "592746ea-d2dd-4ece-9ab8-f0c8120cc9d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014WFJo6ABBy21ZUf9R53gn2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 900,
      "cache_read_input_tokens": 67713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 900,
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

_source line 46 · 2026-05-16T16:04:09.501Z_

<details><summary>↩ Tool result · `toolu_01CLTEbDV77jCBS68hbBr9Yi`</summary>

```text
1	tier: best
2	narrative_guidance: 'Framing B 完全成立：Paper = systematic mining study + methodological
3	  contribution。
4	
5	  Standard eval 上 embed Δ 较小（Qwen ~+0.4pp, StarCoder ~+0.6pp），但 D062 query-split  evaluation
6	  揭示标准评估因 checkpoint 过拟合掩盖了真实效应——held-out evaluation 上 embed Δ  恢复至 Qwen +1.4pp, StarCoder
7	  +0.9pp（均在 best 档预设范围内）。这一发现本身就是方法论贡献： checkpoint selection criterion effect (+16.3pp
8	  max) > mining strategy effect (~1pp)， 说明社区低估了 mining 效果是因为评估方法论缺陷。
9	
10	  BM25 negatives 在两个 encoder 上均 harm（Δ ≤ -1.5pp），empirically 关闭 CoCoHaNeRe 修正论证。 UniXcoder
11	  3-seed null result 干净地归因于 125M scale boundary condition。 RepoBench-R 替代 SWE-bench
12	  作为 held-out external validation，CIs non-overlapping。
13	
14	  3 claims 原样成立：Claim 1 (embed mining reliable) + Claim 2 (exploratory representation  geometry
15	  interaction) + 额外贡献 (checkpoint criterion methodology)。EMNLP Main 强投。
16	
17	  M2 anchors — Standard eval: Qwen random=0.570, embed=0.573, SC random=0.479, embed=0.485。
18	  D062 query-split: Qwen random=0.361, embed=0.375, SC random=0.305, embed=0.314。
19	
20	  '
21	imagined_experiments:
22	- name: M3a SWE-bench Lite E2E — OOD Limitation Disclosure
23	  plan_id: plan_003
24	  description: '3 strategies × best Qwen checkpoint on SWE-bench Lite 300 instances。
25	    实际已完成（random_s42, 100 instances + BM25 baseline 300）。结果为 OOD 泛化失败， 在论文中作为 limitation
26	    呈现而非贡献。
27	
28	    '
29	  expected_results:
30	    random_s42_100:
31	      R_at_1: 0.04
32	      R_at_5: 0.11
33	      R_at_10: 0.14
34	      R_at_20: 0.16
35	      MRR: 0.0698
36	    bm25_baseline_300:
37	      R_at_1: 0.2733
38	      R_at_5: 0.4667
39	      R_at_10: 0.55
40	    neural_vs_bm25_gap_R1_pp: -23.3
41	    status: DONE_FAILED
42	    director_decision: 放弃 SWE-bench 作为论文贡献，外部验证改用 RepoBench-R
43	  result_rationale: 'R@1=0.04 vs BM25=0.2733 表明 contrastive retriever 在 OOD 跨 repo
44	    场景完全失败。 根因：SWE-smith 训练数据是 intra-repo 检索（query 与 candidates 来自同一 repo）， 而 SWE-bench
45	    是 cross-repo 设置（模型未见过的 repo）。Contrastive fine-tuning在小 pool  内 intra-repo 检索上过拟合，丧失了
46	    pretrained encoder 的 cross-repo 泛化能力。 BM25 因为是 lexical matching（不依赖 learned representations）所以不受此影响。
47	
48	    在 best tier 下，这一失败被 strategically 利用：(1) 诚实报告增强论文可信度， (2) 明确 scope boundary "our
49	    results apply to intra-repo retrieval settings"， (3) 激发 future work 方向 "bridging
50	    the intra/cross-repo gap"。 RepoBench-R 替代作为 held-out evaluation（仍是 cross-file
51	    但 repo-aware 设置）。
52	
53	    '
54	  tables:
55	  - name: 'Table S4: SWE-bench OOD Evaluation (Limitation)'
56	    columns:
57	    - Retriever
58	    - R@1
59	    - R@5
60	    - R@10
61	    - MRR
62	    - N
63	    rows:
64	    - - BM25 (reference)
65	      - 0.273
66	      - 0.467
67	      - 0.55
68	      - 0.36
69	      - 300
70	    - - StructFuse-random
71	      - 0.04
72	      - 0.11
73	      - 0.14
74	      - 0.07
75	      - 100
76	  figures_description:
77	  - 'Fig S7: SWE-bench R@K curve showing neural retriever collapse below BM25 at all
78	    K'
79	  analysis: 'SWE-bench failure 在 best tier 下反而加强了论文：它划定了清晰的 scope boundary， 展示了作者的自我审视能力。Reviewer
80	    concern "no downstream eval" 由 RepoBench-R 回应， SWE-bench 失败则作为 honest limitation
81	    处理，1-2 段落放在 Limitations section。
82	
83	    '
84	- name: RepoBench-R Cross-File Retrieval with 3-Seed Bootstrap CIs
85	  plan_id: plan_004
86	  description: 'RepoBench-R test_easy (pool ~6) 和 test_hard (pool ~18) 上评估 3 seeds
87	    ×  3 strategies × 2 encoders（Qwen, StarCoder）。报告 R@1 均值 + 95% bootstrap CI。 这是
88	    SWE-bench 失败后的替代 held-out external validation。
89	
90	    '
91	  expected_results:
92	    qwen_test_hard:
93	      random_R1_mean: 0.62
94	      random_R1_ci:
95	      - 0.615
96	      - 0.625
97	      embedding_R1_mean: 0.632
98	      embedding_R1_ci:
99	      - 0.626
100	      - 0.638
101	      dataflow_R1_mean: 0.626
102	      dataflow_R1_ci:
103	      - 0.62
104	      - 0.632
105	      bm25_R1_mean: 0.601
106	      bm25_R1_ci:
107	      - 0.595
108	      - 0.607
109	      embedding_minus_random_pp: 1.2
110	      bm25_minus_random_pp: -1.9
111	    qwen_test_easy:
112	      random_R1_mean: 0.842
113	      embedding_R1_mean: 0.851
114	      dataflow_R1_mean: 0.847
115	      embedding_minus_random_pp: 0.9
116	    starcoder_test_hard:
117	      random_R1_mean: 0.571
118	      random_R1_ci:
119	      - 0.565
120	      - 0.577
121	      embedding_R1_mean: 0.579
122	      embedding_R1_ci:
123	      - 0.573
124	      - 0.585
125	      dataflow_R1_mean: 0.568
126	      dataflow_R1_ci:
127	      - 0.562
128	      - 0.574
129	      bm25_R1_mean: 0.553
130	      bm25_R1_ci:
131	      - 0.547
132	      - 0.559
133	      embedding_minus_random_pp: 0.8
134	      bm25_minus_random_pp: -1.8
135	    starcoder_test_easy:
136	      random_R1_mean: 0.81
137	      embedding_R1_mean: 0.816
138	      embedding_minus_random_pp: 0.6
139	    repobench_embed_vs_random_avg_pp: 1.0
140	    CI_non_overlapping_embed_vs_random: true
141	    bootstrap_N: 10000
142	  result_rationale: 'RepoBench-R 是 cross-file code completion 任务，与 SWE-smith (bug-fix
143	    retrieval)  领域不同但任务结构相似（从 repo 内候选文件中检索正确文件）。Pool=18 (test_hard) 提供 足够的 distractor
144	    使 mining 质量差异体现。
145	
146	    Embedding mining 在 test_hard 上持续帮助两个 encoder（Qwen +1.2pp, StarCoder +0.8pp）， 因为
147	    harder negatives 训练使 encoder 更善于区分 "semantically similar but functionally  distinct"
148	    文件——这一能力跨任务泛化。CIs non-overlapping 因为 8K test instances 提供 足够的统计功效，即使只有 3 seeds，instance-level
149	    bootstrap 也能给出 tight CIs。
150	
151	    BM25 negatives 在 RepoBench-R 上同样 harm（-1.8 to -1.9pp），与 SWE-smith 一致， 说明 BM25
152	    harm 不是 benchmark-specific artifact 而是 strategy 固有问题。
153	
154	    Test_easy (pool=6) 上 delta 压缩至 0.6-0.9pp 是预期的 ceiling effect—— 6 candidates 中选对
155	    1 个的 baseline 已经很高。
156	
157	    Dataflow 在 Qwen test_hard 上 +0.6pp 但 CI 与 random 接近重叠， StarCoder 上 -0.3pp（CI 含零）——与
158	    SWE-smith encoder-strategy interaction 一致。
159	
160	    '
161	  tables:
162	  - name: 'Table 5: RepoBench-R Results (test_hard, pool≈18)'
163	    columns:
164	    - Encoder
165	    - Strategy
166	    - R@1 (%)
167	    - 95% CI
168	    - Δ vs Random (pp)
169	    rows:
170	    - - Qwen
171	      - BM25
172	      - 60.1
173	      - '[59.5, 60.7]'
174	      - '-1.9'
175	    - - Qwen
176	      - random
177	      - 62.0
178	      - '[61.5, 62.5]'
179	      - —
180	    - - Qwen
181	      - dataflow
182	      - 62.6
183	      - '[62.0, 63.2]'
184	      - '+0.6'
185	    - - Qwen
186	      - embedding
187	      - 63.2
188	      - '[62.6, 63.8]'
189	      - '+1.2'
190	    - - StarCoder
191	      - BM25
192	      - 55.3
193	      - '[54.7, 55.9]'
194	      - '-1.8'
195	    - - StarCoder
196	      - random
197	      - 57.1
198	      - '[56.5, 57.7]'
199	      - —
200	    - - StarCoder
201	      - dataflow
202	      - 56.8
203	      - '[56.2, 57.4]'
204	      - '-0.3'
205	    - - StarCoder
206	      - embedding
207	      - 57.9
208	      - '[57.3, 58.5]'
209	      - '+0.8'
210	  figures_description:
211	  - 'Fig 5: RepoBench-R R@1 grouped bar chart (2 encoders × 4 strategies) with CI
212	    whiskers'
213	  - 'Fig 5b: test_easy vs test_hard side-by-side, showing ceiling compression'
214	  analysis: 'Cross-benchmark 一致性是 best tier 核心证据：embedding mining 在 SWE-smith 和  RepoBench-R
215	    上均显著提升两个 encoder，BM25 均 harm。这排除了 "单 benchmark artifact"  reviewer concern。Strategy
216	    ranking BM25 < random < dataflow ≤ embedding 完美保持。 test_easy ceiling effect 间接验证了
217	    pool size 对效果幅度的调节作用（与 plan_019 互补）。
218	
219	    '
220	- name: Stratified Analysis with 5 Strata (D062 Query-Split Evaluation)
221	  plan_id: plan_005
222	  description: '5 层分层分析：repo size / pool size / query-positive similarity /  structural
223	    data availability (90% with m1_reextract_v2 vs 10% remaining errors) /  neg_difficulty
224	    quartile。使用 M2 best checkpoints 在 D062 query-split held-out  evaluation 上重新评估。
225	
226	    '
227	  expected_results:
228	    stratum_structural_available:
229	      with_dataflow_90pct:
230	        qwen_dataflow_minus_random_pp: 0.8
231	        qwen_embed_minus_random_pp: 1.3
232	        starcoder_dataflow_minus_random_pp: -0.2
233	        n_instances: ~13000
234	        note: m1_reextract_v2 提升 coverage 从 34% 到 90%
235	      no_dataflow_10pct:
236	        qwen_dataflow_minus_random_pp: 0.1
237	        qwen_embed_minus_random_pp: 1.4
238	        n_instances: ~1400
239	    stratum_neg_difficulty_quartile:
240	      Q1_easiest:
241	        qwen_embed_minus_random_pp: 0.6
242	        qwen_dataflow_minus_random_pp: 0.2
243	      Q2:
244	        qwen_embed_minus_random_pp: 1.1
245	        qwen_dataflow_minus_random_pp: 0.5
246	      Q3:
247	        qwen_embed_minus_random_pp: 1.7
248	        qwen_dataflow_minus_random_pp: 0.9
249	      Q4_hardest:
250	        qwen_embed_minus_random_pp: 2.3
251	        qwen_dataflow_minus_random_pp: 1.5
252	    stratum_repo_size:
253	      small_lt50:
254	        embedding_delta_pp: 2.0
255	        n: ~500
256	      medium_50_200:
257	        embedding_delta_pp: 1.6
258	        n: ~4100
259	      large_200_500:
260	        embedding_delta_pp: 1.3
261	        n: ~5500
262	      xlarge_500plus:
263	        embedding_delta_pp: 1.0
264	        n: ~5100
265	    stratum_pool_size:
266	      pool_lt20:
267	        embedding_delta_pp: 0.7
268	        dataflow_delta_pp: 0.2
269	      pool_20_50:
270	        embedding_delta_pp: 1.5
271	        dataflow_delta_pp: 0.6
272	      pool_gt50:
273	        embedding_delta_pp: 1.9
274	        dataflow_delta_pp: 0.9
275	    stratum_query_pos_sim:
276	      high_sim_gt095:
277	        embedding_delta_pp: 1.8
278	        dataflow_delta_pp: 1.2
279	      medium_sim_085_095:
280	        embedding_delta_pp: 1.3
281	        dataflow_delta_pp: 0.5
282	      low_sim_lt085:
283	        embedding_delta_pp: 0.8
284	        dataflow_delta_pp: 0.1
285	  result_rationale: 'm1_reextract_v2 将 structural data rate 从 34% 提升到 90%，彻底改变了 structural  stratum
286	    分析。90% stratum 上 dataflow Δ=+0.8pp（显著）因为绝大部分 instance 现在 获得真实 dataflow-disconnected
287	    negatives。10% remaining errors 上 dataflow 退化为  random（Δ≈0），因为缺乏结构数据意味着 fallback
288	    策略无差异。
289	
290	    Neg difficulty Q4（最难 quartile）embed Δ=+2.3pp 是 overall 的 ~1.6 倍——越难的  instance（margin
291	    最小）从 harder negatives 获益最多，这是 representation saturation  理论的直接预测。Q1（最易）Δ 最小（0.6pp）因为
292	    random negatives 已足够区分。
293	
294	    Repo size 上 small repo Δ 最大（2.0pp）因为小 repo candidate pool 集中，mining  质量差异更容易体现。Pool
295	    size > 50 时 delta 增大到 1.9pp，说明 mining 在更大搜索 空间下更有价值。
296	
297	    Query-positive similarity 分层显示 high sim（>0.95）时 delta 最大，与 Qwen  saturation 分析一致——高相似度区域是
298	    embedding mining 最有价值的场景。
299	
300	    '
301	  tables:
302	  - name: 'Table 6: Stratified Embed-Random Δ by Neg Difficulty Quartile (Qwen, D062
303	      eval)'
304	    columns:
305	    - Quartile
306	    - margin_mean
307	    - emb−rand (pp)
308	    - df−rand (pp)
309	    rows:
310	    - - Q1 (easiest)
311	      - 0.135
312	      - '+0.6'
313	      - '+0.2'
314	    - - Q2
315	      - 0.072
316	      - '+1.1'
317	      - '+0.5'
318	    - - Q3
319	      - 0.028
320	      - '+1.7'
321	      - '+0.9'
322	    - - Q4 (hardest)
323	      - 0.007
324	      - '+2.3'
325	      - '+1.5'
326	  - name: 'Table 6b: Stratified by Structural Data Availability (Qwen)'
327	    columns:
328	    - Stratum
329	    - N
330	    - emb−rand (pp)
331	    - df−rand (pp)
332	    rows:
333	    - - With dataflow (90%)
334	      - ~13K
335	      - '+1.3'
336	      - '+0.8'
337	    - - No dataflow (10%)
338	      - ~1.4K
339	      - '+1.4'
340	      - '+0.1'
341	  figures_description:
342	  - 'Fig 6: Neg difficulty quartile × strategy interaction line plot'
343	  - 'Fig 7: Heatmap — R@1 delta (strategy × stratum), separate panels for Qwen and
344	    StarCoder'
345	  analysis: 'Neg difficulty quartile 分析是 best tier 最强 mechanistic 证据。Q4 的 2.3pp  embed
346	    delta 是 overall 1.4pp 的 1.6 倍——直接验证 "harder instances benefit more  from harder
347	    negatives" 的理论预测。Structural availability 分析从 34%→90% coverage  升级后说服力大增——90% stratum
348	    的 dataflow Δ=+0.8pp 是 clean signal。 Confound analysis（rich-dataflow 99.3% 在 large/xlarge
349	    repo）仍需控制 repo size  来隔离 dataflow richness 独立效应。
350	
351	    '
352	- name: Call-Graph Hop Depth Ablation (1/2/3-hop)
353	  plan_id: plan_007
354	  description: '比较 1-hop / 2-hop / 3-hop call-graph bounding 对 dataflow negative 质量影响。
355	    Qwen encoder, 1 seed, SWE-smith validation。使用 m1_reextract_v2 数据（90% coverage）。
356	
357	    '
358	  expected_results:
359	    hop_1:
360	      R1: 0.548
361	      connected_coverage_pct: 15.2
362	      negatives_per_query_mean: 21.4
363	    hop_2:
364	      R1: 0.558
365	      connected_coverage_pct: 45.8
366	      negatives_per_query_mean: 38.6
367	    hop_3:
368	      R1: 0.553
369	      connected_coverage_pct: 72.1
370	      negatives_per_query_mean: 55.3
371	    optimal_hop: 2
372	    hop2_minus_hop1_pp: 1.0
373	    hop3_minus_hop2_pp: -0.5
374	  result_rationale: 'm1_reextract_v2 90% coverage 下，各 hop depth 的 connected coverage
375	    均高于原 34%。 2-hop 最优因为：(1) 1-hop 仅覆盖 15.2% instances（直接 caller/callee），大部分 instance  没有足够
376	    connected nodes 定义 meaningful disconnection，退化为 random；(2) 3-hop  coverage 72.1%
377	    过高，"disconnected" 定义过窄——许多语义相关但 3-hop 可达的文件被错误排除 在 negative pool 外；(3) 2-hop coverage
378	    45.8%（近一半 instance 有 meaningful  structural signal）平衡了 signal quality 和 coverage。
379	
380	    2-hop 对应 inter-procedural 语义：直接 caller/callee + 一层间接调用。 这是 principled 选择而非纯 empirical
381	    tuning。
382	
383	    '
384	  tables:
385	  - name: 'Table S1: Hop Depth Ablation (Qwen, dataflow strategy)'
386	    columns:
387	    - Hops
388	    - Coverage (%)
389	    - Neg/query
390	    - R@1 (%)
391	    - Δ vs 2-hop (pp)
392	    rows:
393	    - - 1
394	      - 15.2
395	      - 21.4
396	      - 54.8
397	      - '-1.0'
398	    - - 2
399	      - 45.8
400	      - 38.6
401	      - 55.8
402	      - —
403	    - - 3
404	      - 72.1
405	      - 55.3
406	      - 55.3
407	      - '-0.5'
408	  figures_description:
409	  - 'Fig S1: Hop depth vs R@1 line plot with coverage % on secondary y-axis'
410	  analysis: 'Inverted-U pattern（1-hop < 2-hop > 3-hop）支持 "optimal structural granularity"  narrative。2-hop
411	    + m1_reextract_v2 (90% coverage) 的组合是论文推荐配置。
412	
413	    '
414	- name: Training Data Size Scaling (1K/3K/5K instances)
415	  plan_id: plan_008
416	  description: '固定 Qwen encoder + 3 strategies，训练数据从 1K / 3K / 5K instances 增长， 观察
417	    R@1 变化和策略排名稳定性。1 seed per size。
418	
419	    '
420	  expected_results:
421	    size_1K:
422	      random_R1: 0.515
423	      embedding_R1: 0.524
424	      dataflow_R1: 0.518
425	      embedding_minus_random_pp: 0.9
426	      seed_std: 0.018
427	    size_3K:
428	      random_R1: 0.54
429	      embedding_R1: 0.552
430	      dataflow_R1: 0.545
431	      embedding_minus_random_pp: 1.2
432	      seed_std: 0.012
433	    size_5K:
434	      random_R1: 0.553
435	      embedding_R1: 0.567
436	      dataflow_R1: 0.559
437	      embedding_minus_random_pp: 1.4
438	      seed_std: 0.009
439	    ranking_stable: true
440	    monotonic_improvement: true
441	  result_rationale: '策略排名在 3 个尺度上保持一致（embedding > dataflow > random），delta 幅度随数据量
442	    增大而增大（1K: 0.9pp → 5K: 1.4pp）。更大训练集提供更多 diverse negatives，mining  策略差异更充分体现。1K
443	    时 seed variance 较大（1.8pp std）因为 negative 多样性不足， 个别 seed 的采样偶然性影响结果。5K 时 variance
444	    收敛至 0.9pp。 No diminishing returns at 5K 暗示进一步 scaling 可能有益。
445	
446	    '
447	  tables:
448	  - name: 'Table S2: Data Size Scaling (Qwen)'
449	    columns:
450	    - Size
451	    - random
452	    - embedding
453	    - dataflow
454	    - emb−rand (pp)
455	    - σ (pp)
456	    rows:
457	    - - 1K
458	      - 51.5
459	      - 52.4
460	      - 51.8
461	      - '+0.9'
462	      - 1.8
463	    - - 3K
464	      - 54.0
465	      - 55.2
466	      - 54.5
467	      - '+1.2'
468	      - 1.2
469	    - - 5K
470	      - 55.3
471	      - 56.7
472	      - 55.9
473	      - '+1.4'
474	      - 0.9
475	  figures_description:
476	  - 'Fig S2: R@1 vs training size for 3 strategies with shaded variance bands'
477	  analysis: 'Stable ranking + growing delta 说明 mining effect 不是 small-data artifact。
478	    5K 未达 diminishing returns，当前 delta 是下界不是上界——回应 "effect marginal" concern。
479	
480	    '
481	- name: Fusion Head Ablation (mining vs inference-time features)
482	  plan_id: plan_009
483	  description: '比较 embedding-only / structural-features-only / combined fusion head。
484	    隔离 training-time mining 价值与 inference-time feature injection。 Qwen + StarCoder,
485	    best embedding checkpoint。
486	
487	    '
488	  expected_results:
489	    embedding_only:
490	      qwen_R1: 0.567
491	      starcoder_R1: 0.485
492	    structural_features_only:
493	      qwen_R1: 0.501
494	      starcoder_R1: 0.422
495	    combined_fusion:
496	      qwen_R1: 0.564
497	      starcoder_R1: 0.483
498	    embedding_only_minus_combined_pp: 0.3
499	    embedding_only_minus_structural_only_pp: 6.6
500	    conclusion: mining >> fusion; structural features at inference add noise
501	  result_rationale: 'Embedding-only（mining 训练，inference 不注入结构特征）表现最好或 tied with combined。
502	    Combined 略低 0.3pp 因为 inference-time structural features 引入不精确信号—— 即使 m1_reextract_v2
503	    coverage 90%，仍有 10% instance 收到 zero-vector structural  features 引入 noise。
504	
505	    Structural-features-only（不用 mining，仅 inference 时注入）远低于 embedding-only （-6.6pp
506	    Qwen），证明核心价值在 training-time negative mining 而非 inference-time  feature engineering。Paper
507	    可据此明确：StructFuse 的贡献是 mining strategy，不是 fusion。
508	
509	    '
510	  tables:
511	  - name: 'Table S3: Fusion Head Ablation'
512	    columns:
513	    - Configuration
514	    - Qwen R@1 (%)
515	    - StarCoder R@1 (%)
516	    rows:
517	    - - embedding-only (ours)
518	      - 56.7
519	      - 48.5
520	    - - structural-features-only
521	      - 50.1
522	      - 42.2
523	    - - combined fusion
524	      - 56.4
525	      - 48.3
526	  figures_description:
527	  - 'Fig S3: Ablation bar chart comparing 3 fusion configurations'
528	  analysis: 'Mining（间接 structural signal）> fusion（直接 structural features）。 原因：mining
529	    让 encoder 自己学习 structure-relevant representations， 直接注入 features 绕过了学习过程且引入 coverage
530	    noise。强化论文 narrative。
531	
532	    '
533	- name: Dataflow-Distance Weighted vs Binary Negatives
534	  plan_id: plan_010
535	  description: '比较 binary connected/disconnected 与 dataflow-distance weighted negative
536	    sampling。 Weighted: disconnected 且 hop-distance 更远的文件赋予更高采样概率。
537	
538	    '
539	  expected_results:
540	    binary_qwen_R1: 0.559
541	    weighted_qwen_R1: 0.561
542	    binary_starcoder_R1: 0.472
543	    weighted_starcoder_R1: 0.473
544	    weighted_minus_binary_qwen_pp: 0.2
545	    weighted_minus_binary_starcoder_pp: 0.1
546	    significant: false
547	  result_rationale: 'Weighted 仅微弱提升 +0.1~0.2pp（不显著）。Binary disconnected/connected
548	    已捕获 最关键的 structural distinction——"是否在调用链上"。进一步按 hop distance 加权引入的 额外信号被 noise
549	    抵消：距离更远 ≠ 更好 negative（utility 文件可能 hop=∞ 但也是  trivial negative）。Binary 的简洁性是优势——fewer
550	    hyperparameters, same effect。
551	
552	    '
553	  tables:
554	  - name: 'Table S5: Weighted vs Binary Dataflow Negatives'
555	    columns:
556	    - Method
557	    - Qwen R@1 (%)
558	    - StarCoder R@1 (%)
559	    - Δ vs Binary (pp)
560	    rows:
561	    - - Binary (default)
562	      - 55.9
563	      - 47.2
564	      - —
565	    - - Distance-weighted
566	      - 56.1
567	      - 47.3
568	      - +0.2 / +0.1
569	  figures_description: []
570	  analysis: 'Binary sufficient — weighted complexity not justified。 论文 ablation section
571	    用一句话报告，强化 "simple binary is the key insight"。
572	
573	    '
574	- name: SWE-smith Retrieval Failure Analysis (repurposed from SWE-bench)
575	  plan_id: plan_011
576	  description: '原计划分析 SWE-bench 失败案例。SWE-bench 已失败（R@1=0.04, OOD），改为分析 SWE-smith validation
577	    上 random retriever 失败的 50 个案例，分类失败原因， 标注 embedding/dataflow mining 能否帮助。
578	
579	    '
580	  expected_results:
581	    total_analyzed: 50
582	    source: SWE-smith validation set (intra-repo setting)
583	    category_breakdown:
584	      similar_but_wrong_file: 19
585	      distant_but_correct_file: 12
586	      pool_saturation_all_similar: 9
587	      query_ambiguity: 6
588	      singleton_gold_no_candidates: 4
589	    mining_would_help:
590	      embedding_helps: 17
591	      dataflow_helps: 8
592	      neither_helps: 25
593	    embedding_help_rate: 0.34
594	    dataflow_additional_help_rate: 0.16
595	  result_rationale: '50 个失败中 19 个是 "similar but wrong"——检索到与 gold 高文本相似但非同一 call chain  的文件。Embedding
596	    mining 训练可帮助其中 17 个（让 encoder 学会区分高相似度区域内的细微差异）。 Dataflow 额外帮助 8 个涉及跨模块调用链的案例（embedding
597	    mining 无法捕获的 structural  dependencies）。25 个 "neither helps" 主要是 pool saturation（候选全部高度相似）和  query
598	    ambiguity（issue 描述模糊无法定位）。
599	
600	    34% embedding help rate 与 observed 1.0-1.4pp delta 一致： 如果 34% 的失败中有一部分被修正，对应 ~1-2pp
601	    总体提升。
602	
603	    '
604	  tables:
605	  - name: 'Table S6: Failure Category Breakdown (SWE-smith)'
606	    columns:
607	    - Category
608	    - Count
609	    - '% of 50'
610	    - Mining Helps?
611	    rows:
612	    - - Similar but wrong file
613	      - 19
614	      - 38
615	      - 17/19 (embed)
616	    - - Distant correct file
617	      - 12
618	      - 24
619	      - 8/12 (dataflow)
620	    - - Pool saturation
621	      - 9
622	      - 18
623	      - 2/9 (partial)
624	    - - Query ambiguity
625	      - 6
626	      - 12
627	      - 0/6
628	    - - Singleton gold
629	      - 4
630	      - 8
631	      - 0/4
632	  figures_description:
633	  - 'Fig S4: Failure category pie chart with mining-could-help overlay'
634	  analysis: 'Failure analysis 将抽象 delta 转化为具体机制。"Similar but wrong" 是最大失败类别 且最易被 embedding
635	    mining 修正——直接支持 Claim 1 的 mechanistic explanation。
636	
637	    '
638	- name: Qualitative Examples (5-8 cases from SWE-smith)
639	  plan_id: plan_012
640	  description: '从 SWE-smith 中选取 5-8 个 embedding/dataflow mining 改变检索结果的典型案例。 （原依赖
641	    SWE-bench，现改用 SWE-smith internal data。）
642	
643	    '
644	  expected_results:
645	    total_examples: 7
646	    example_categories:
647	      caller_callee_confusion: 3
648	      utility_file_distraction: 2
649	      cross_module_import_chain: 1
650	      test_vs_source: 1
651	    illustrative_example:
652	      repo: sample-python-project
653	      query: issue about incorrect cache invalidation
654	      random_top1: cache/utils.py (lexical match on 'cache')
655	      embedding_top1: cache/backend.py (semantically similar, shares embedding cluster)
656	      dataflow_top1: cache/backend.py + storage/driver.py (caller chain)
657	      gold: cache/backend.py
658	  result_rationale: '7 个案例覆盖 4 个失败模式。Caller-callee confusion（3 个）最常见——文本相似的  wrapper
659	    函数 vs 实际实现是 code retrieval 的核心挑战。案例具体展示了  "lexical similarity ≠ structural relevance"，使抽象的
660	    representation geometry  论证变得具体可感。
661	
662	    '
663	  tables: []
664	  figures_description:
665	  - 'Fig 8: Side-by-side retrieval ranking for 3 representative cases with dependency
666	    graph overlay'
667	  analysis: 'Qualitative examples 是论文 "aha moment"——即使对统计显著性持怀疑态度的 reviewer， 也能通过具体案例理解
668	    mining 策略的作用机制。
669	
670	    '
671	- name: Temperature Ablation τ ∈ {0.05, 0.1, 0.2} (Full)
672	  plan_id: plan_014
673	  description: '3 temperatures × 3 strategies × 2 encoders, 1 seed each。 测试 strategy
674	    ranking 是否 temperature-regime-specific。 （plan_021 为 reduced 版本；如果时间足够，运行 full
675	    plan_014。）
676	
677	    '
678	  expected_results:
679	    tau_005:
680	      qwen_random_R1: 0.56
681	      qwen_embedding_R1: 0.576
682	      qwen_dataflow_R1: 0.568
683	      qwen_embedding_minus_random_pp: 1.6
684	      starcoder_random_R1: 0.487
685	      starcoder_embedding_R1: 0.497
686	      starcoder_embedding_minus_random_pp: 1.0
687	    tau_010:
688	      qwen_random_R1: 0.553
689	      qwen_embedding_R1: 0.567
690	      qwen_dataflow_R1: 0.559
691	      qwen_embedding_minus_random_pp: 1.4
692	      starcoder_random_R1: 0.479
693	      starcoder_embedding_R1: 0.485
694	      starcoder_embedding_minus_random_pp: 0.6
695	    tau_020:
696	      qwen_random_R1: 0.538
697	      qwen_embedding_R1: 0.55
698	      qwen_dataflow_R1: 0.544
699	      qwen_embedding_minus_random_pp: 1.2
700	      starcoder_random_R1: 0.465
701	      starcoder_embedding_R1: 0.472
702	      starcoder_embedding_minus_random_pp: 0.7
703	    ranking_preserved_across_tau: true
704	    optimal_tau: 0.05
705	  result_rationale: 'Strategy ranking（embedding > dataflow > random for Qwen; embedding
706	    > random ≈  dataflow for StarCoder）在三个 τ 下保持一致。τ=0.05 绝对性能最高——sharper temperature  使
707	    contrastive loss 更有效地放大相似度差异。τ=0.2 下 delta 缩小（1.2pp vs 1.4pp  for Qwen）——softer
708	    temperature 压缩所有 similarity 到窄范围，减弱 hard vs easy  negatives 的梯度差异。
709	
710	    关键结论：findings 不是 temperature-regime-specific。直接回应 median reviewer 的  "τ=0.05 unusually
711	    low" concern。τ=0.1 作为 paper default（literature convention）， τ=0.05 作为 alternative
712	    best configuration 在 ablation 报告。
713	
714	    '
715	  tables:
716	  - name: 'Table 7: Temperature Ablation (R@1 %)'
717	    columns:
718	    - τ
719	    - Encoder
720	    - random
721	    - embedding
722	    - dataflow
723	    - emb−rand (pp)
724	    rows:
725	    - - 0.05
726	      - Qwen
727	      - 56.0
728	      - 57.6
729	      - 56.8
730	      - '+1.6'
731	    - - 0.05
732	      - StarCoder
733	      - 48.7
734	      - 49.7
735	      - 48.5
736	      - '+1.0'
737	    - - 0.1
738	      - Qwen
739	      - 55.3
740	      - 56.7
741	      - 55.9
742	      - '+1.4'
743	    - - 0.1
744	      - StarCoder
745	      - 47.9
746	      - 48.5
747	      - 47.4
748	      - '+0.6'
749	    - - 0.2
750	      - Qwen
751	      - 53.8
752	      - 55.0
753	      - 54.4
754	      - '+1.2'
755	    - - 0.2
756	      - StarCoder
757	      - 46.5
758	      - 47.2
759	      - 46.3
760	      - '+0.7'
761	  figures_description:
762	  - 'Fig S5: Temperature × strategy interaction plot, separate panels per encoder'
763	  analysis: 'Ranking stability across τ 是关键 robustness 证据。τ=0.2 delta 缩小但不翻转—— mining
764	    quality 的价值在不同 loss sharpness 下都存在。
765	
766	    '
767	- name: Dynamic vs Static Embedding Mining
768	  plan_id: plan_015
769	  description: 'Dynamic: 每 epoch 用当前 encoder 重新挖 embedding negatives。 Static: 仅用 pretrained
770	    encoder 挖一次（当前做法）。 Qwen + StarCoder, 1 seed each。Phase 2 (GPU) QUEUED。
771	
772	    '
773	  expected_results:
774	    qwen_static_R1: 0.567
775	    qwen_dynamic_R1: 0.569
776	    qwen_dynamic_minus_static_pp: 0.2
777	    starcoder_static_R1: 0.485
778	    starcoder_dynamic_R1: 0.486
779	    starcoder_dynamic_minus_static_pp: 0.1
780	    dynamic_significant: false
781	    curriculum_confound_ruled_out: true
782	  result_rationale: 'Dynamic 仅微弱提升 +0.1~0.2pp（不显著），因为 LoRA rank 16 fine-tuning 只轻微
783	    改变 embedding space——pretrained encoder 的 nearest neighbors 训练后大部分不变。 这排除了 "static
784	    mining 优势来自 curriculum effect (early hard → stale negatives)"  的 confound。
785	
786	    对 Claim 2 重要：mining strategy 的选择（what to mine）比 mining schedule  （when to mine）更关键。Dynamic
787	    的 compute overhead（每 epoch 重新 encode + kNN） not justified——强化 "zero-cost" framing。
788	
789	    '
790	  tables:
791	  - name: 'Table S7: Static vs Dynamic Embedding Mining'
792	    columns:
793	    - Encoder
794	    - Static R@1 (%)
795	    - Dynamic R@1 (%)
796	    - Δ (pp)
797	    - p-value
798	    rows:
799	    - - Qwen
800	      - 56.7
801	      - 56.9
802	      - '+0.2'
803	      - 0.44
804	    - - StarCoder
805	      - 48.5
806	      - 48.6
807	      - '+0.1'
808	      - 0.56
809	  figures_description:
810	  - 'Fig S6: Learning curves for static vs dynamic mining, overlaid'
811	  analysis: 'Static ≈ dynamic 是 clean negative result。强化 "mine once from pretrained,  no
812	    re-mining needed" 的 practitioner recommendation。
813	
814	    '
815	- name: Bootstrap CIs for M2 Main Results + RepoBench-R
816	  plan_id: plan_016
817	  description: '原为 SWE-bench CIs，现 repurpose 为 M2 main results (D062 query-split eval)  和
818	    RepoBench-R 的 paired bootstrap 95% CIs。10K resamples。 统一统计框架覆盖所有 pairwise comparisons。
819	
820	    '
821	  expected_results:
822	    m2_query_split_eval:
823	      qwen_embed_minus_random:
824	        delta_pp: 1.4
825	        ci_95:
826	        - 0.5
827	        - 2.3
828	        p_value: 0.012
829	        significant: true
830	      starcoder_embed_minus_random:
831	        delta_pp: 0.9
832	        ci_95:
833	        - 0.1
834	        - 1.7
835	        p_value: 0.038
836	        significant: true
837	      qwen_bm25_minus_random:
838	        delta_pp: -2.9
839	        ci_95:
840	        - -4.1
841	        - -1.7
842	        p_value: 0.001
843	        significant: true
844	      starcoder_bm25_minus_random:
845	        delta_pp: -2.5
846	        ci_95:
847	        - -3.8
848	        - -1.2
849	        p_value: 0.003
850	        significant: true
851	      qwen_dataflow_minus_random:
852	        delta_pp: 0.7
853	        ci_95:
854	        - -0.2
855	        - 1.6
856	        p_value: 0.089
857	        significant: false
858	    repobench_r_test_hard:
859	      qwen_embed_minus_random:
860	        delta_pp: 1.2
861	        ci_95:
862	        - 0.6
863	        - 1.8
864	        p_value: 0.002
865	        significant: true
866	      starcoder_embed_minus_random:
867	        delta_pp: 0.8
868	        ci_95:
869	        - 0.2
870	        - 1.4
871	        p_value: 0.014
872	        significant: true
873	    bootstrap_n: 10000
874	    all_embed_vs_random_exclude_zero: true
875	    all_bm25_vs_random_exclude_zero: true
876	  result_rationale: 'D062 query-split eval 上 embed vs random CI 下界 > 0 for both encoders，
877	    confirming statistical significance。BM25 vs random CI 上界 < 0，confirming harm。
878	    Dataflow vs random 在 Qwen 上 borderline（p=0.089, CI 含零）——consistent with  Claim
879	    2 的 "exploratory/conditional" framing。
880	
881	    RepoBench-R CIs 更 tight（8K test instances 提供更大统计功效），两个 encoder  embed vs random
882	    均显著。Cross-benchmark significance 是 Claim 1 的 statistical  closure。
883	
884	    3 seeds 的 seed-level variance 通过 instance-level bootstrap 吸收—— CI 主要反映 instance-level
885	    variability 而非 seed variance，这对 3-seed 设计 是有利的（seed 数少不直接导致 CI 变宽，因为每个 seed 有大量
886	    instance）。
887	
888	    '
889	  tables:
890	  - name: 'Table 3: Main Results with Bootstrap 95% CIs (D062 query-split)'
891	    columns:
892	    - Encoder
893	    - Comparison
894	    - Δ (pp)
895	    - 95% CI
896	    - p-value
897	    rows:
898	    - - Qwen
899	      - embed − random
900	      - '+1.4'
901	      - '[+0.5, +2.3]'
902	      - 0.012
903	    - - Qwen
904	      - dataflow − random
905	      - '+0.7'
906	      - '[−0.2, +1.6]'
907	      - 0.089
908	    - - Qwen
909	      - BM25 − random
910	      - −2.9
911	      - '[−4.1, −1.7]'
912	      - 0.001
913	    - - StarCoder
914	      - embed − random
915	      - '+0.9'
916	      - '[+0.1, +1.7]'
917	      - 0.038
918	    - - StarCoder
919	      - dataflow − random
920	      - −0.5
921	      - '[−1.4, +0.4]'
922	      - 0.21
923	    - - StarCoder
924	      - BM25 − random
925	      - −2.5
926	      - '[−3.8, −1.2]'
927	      - 0.003
928	  figures_description:
929	  - 'Fig 4: Forest plot showing pairwise deltas with 95% CIs for all comparisons'
930	  - 'Fig 4b: Bootstrap distribution histograms for embed−random (both encoders)'
931	  analysis: 'CI 下界 > 0 for embed, 上界 < 0 for BM25, dataflow borderline——这是理想的 statistical
932	    picture for the best tier。Three-tier significance pattern  (BM25 harm ✓, embed
933	    help ✓, dataflow conditional ?) 完美映射到三条 claims。
934	
935	    '
936	- name: BM25 Negative Baseline — Closing CoCoHaNeRe Argument
937	  plan_id: plan_018
938	  description: 'BM25-based hard negatives 作为第 4 策略。Phase 1 (CPU) DONE：BM25 index built，
939	    training data mined（11K+ records/seed, k=50）。Phase 2 (GPU)：train 3 seeds ×  2
940	    encoders。验证 CoCoHaNeRe 报告的 "embedding negatives harm" 是 BM25-proxy artifact。
941	
942	    '
943	  expected_results:
944	    qwen:
945	      bm25_s42_R1: 0.535
946	      bm25_s43_R1: 0.538
947	      bm25_s44_R1: 0.541
948	      bm25_mean_R1: 0.538
949	      random_mean_R1: 0.57
950	      bm25_minus_random_pp: -3.2
951	      embed_mean_R1: 0.573
952	      embed_minus_bm25_pp: 3.5
953	    starcoder:
954	      bm25_s42_R1: 0.452
955	      bm25_s43_R1: 0.462
956	      bm25_s44_R1: 0.458
957	      bm25_mean_R1: 0.457
958	      random_mean_R1: 0.479
959	      bm25_minus_random_pp: -2.2
960	      embed_mean_R1: 0.485
961	      embed_minus_bm25_pp: 2.8
962	    bm25_harms_both_encoders: true
963	    cocohanere_artifact_confirmed: true
964	    bm25_minus_random_avg_pp: -2.7
965	    bm25_overlap_context:
966	      bm25_vs_embedding_top7_jaccard_large_repos: 0.297
967	      bm25_vs_random_top7_jaccard_large_repos: 0.007
968	  result_rationale: 'BM25 negatives 在两个 encoder 上均 harm（Qwen -3.2pp, StarCoder -2.2pp），
969	    mean -2.7pp 位于 best 档 [-3.0, -1.0] 范围内。
970	
971	    BM25 选取的是 lexically similar 但 semantically ambiguous 的文件——共享大量  token overlap（函数名、变量名、import
972	    patterns），但这种 overlap 恰恰是 contrastive  learning 用来区分 positive/negative 的信号。用 BM25
973	    选的 negatives 使模型学会  ignore lexical cues，但这些 cues 在 code retrieval 中是有效信号。
974	
975	    Overlap 分析（phase 1 已完成）支持这一解释：大 repo 上 BM25 与 embedding  top-7 Jaccard 仅 0.297——两种
976	    mining 选取的 negatives 差异很大。BM25 与 random  仅 0.007——说明 BM25 negatives 与 random sampling
977	    几乎无交集（高度 targeted）， 但 targeted 到了错误方向。
978	
979	    这直接回应 CoCoHaNeRe (ACM TOSEM 2025)：他们报告的 "embedding negatives harm"  实际是 BM25-proxy
980	    artifact。True embedding distance negatives 方向相反（+0.6~1.4pp）。 BM25 vs embedding
981	    的 3.5pp 差距是论文最大的 single pairwise comparison。
982	
983	    '
984	  tables:
985	  - name: 'Table 2: Full 4-Strategy Comparison (Standard Eval, best_by_R@1)'
986	    columns:
987	    - Encoder
988	    - Strategy
989	    - Mean R@1 (%)
990	    - 95% CI
991	    - Δ vs Random (pp)
992	    rows:
993	    - - Qwen
994	      - BM25
995	      - 53.8
996	      - '[52.9, 54.7]'
997	      - −3.2
998	    - - Qwen
999	      - random
1000	      - 57.0
1001	      - '[55.5, 58.5]'
1002	      - —
1003	    - - Qwen
1004	      - dataflow
1005	      - 55.9
1006	      - '[55.3, 56.5]'
1007	      - −1.1
1008	    - - Qwen
1009	      - embedding
1010	      - 57.3
1011	      - '[56.5, 58.1]'
1012	      - '+0.3'
1013	    - - StarCoder
1014	      - BM25
1015	      - 45.7
1016	      - '[44.8, 46.6]'
1017	      - −2.2
1018	    - - StarCoder
1019	      - random
1020	      - 47.9
1021	      - '[46.0, 49.0]'
1022	      - —
1023	    - - StarCoder
1024	      - dataflow
1025	      - 47.2
1026	      - '[46.5, 47.9]'
1027	      - −0.7
1028	    - - StarCoder
1029	      - embedding
1030	      - 48.5
1031	      - '[47.2, 50.1]'
1032	      - '+0.6'
1033	  - name: 'Table 2b: 4-Strategy on D062 Query-Split Eval'
1034	    columns:
1035	    - Encoder
1036	    - Strategy
1037	    - Mean R@1 (%)
1038	    - Δ vs Random (pp)
1039	    rows:
1040	    - - Qwen
1041	      - BM25
1042	      - 33.2
1043	      - −2.9
1044	    - - Qwen
1045	      - random
1046	      - 36.1
1047	      - —
1048	    - - Qwen
1049	      - dataflow
1050	      - 36.8
1051	      - '+0.7'
1052	    - - Qwen
1053	      - embedding
1054	      - 37.5
1055	      - '+1.4'
1056	    - - StarCoder
1057	      - BM25
1058	      - 28.0
1059	      - −2.5
1060	    - - StarCoder
1061	      - random
1062	      - 30.5
1063	      - —
1064	    - - StarCoder
1065	      - dataflow
1066	      - 30.1
1067	      - −0.4
1068	    - - StarCoder
1069	      - embedding
1070	      - 31.4
1071	      - '+0.9'
1072	  figures_description:
1073	  - 'Fig 3: 4-strategy R@1 bar chart (D062 eval) with BM25 in red, annotation arrow
1074	    showing BM25→embed gap'
1075	  - 'Fig 3b: Neg similarity histograms for 4 strategies showing BM25 occupies distinct
1076	    region'
1077	  analysis: 'BM25 baseline 是 best tier 的 crown jewel。将 Claim 1 从 "argumentative correction"  升级为
1078	    "empirical demonstration"：不仅指出 CoCoHaNeRe 用了 BM25 proxy，还实际 复现 harm effect 并展示
1079	    true embedding negatives 方向相反。
1080	
1081	    4-strategy ordering BM25 < random < dataflow ≤ embedding 清晰展示 negative  mining
1082	    的 quality spectrum。注意 standard eval 上 embed Δ 较小（+0.3pp Qwen）， 但 D062 query-split
1083	    上 embed Δ=+1.4pp——checkpoint selection methodology 揭示 了被 standard eval 掩盖的真实效应。
1084	
1085	    '
1086	- name: Pool Size Sensitivity (50/100/200/500)
1087	  plan_id: plan_019
1088	  description: 'SWE-smith validation 上用 pool={50, 100, 200, 500} 重新评估 M2 best checkpoints，
1089	    测试 strategy ranking 在 realistic pool sizes 下的稳定性。
1090	
1091	    '
1092	  expected_results:
1093	    qwen:
1094	      pool_50:
1095	        random_R1: 0.57
1096	        embedding_R1: 0.573
1097	        dataflow_R1: 0.559
1098	        embedding_minus_random_pp: 0.3
1099	        note: pool=50 与 standard eval (pool=8) anchor 接近但稍低
1100	      pool_100:
1101	        random_R1: 0.432
1102	        embedding_R1: 0.446
1103	        embedding_minus_random_pp: 1.4
1104	      pool_200:
1105	        random_R1: 0.348
1106	        embedding_R1: 0.361
1107	        embedding_minus_random_pp: 1.3
1108	      pool_500:
1109	        random_R1: 0.265
1110	        embedding_R1: 0.277
1111	        embedding_minus_random_pp: 1.2
1112	    starcoder:
1113	      pool_50:
1114	        random_R1: 0.479
1115	        embedding_R1: 0.485
1116	        embedding_minus_random_pp: 0.6
1117	      pool_100:
1118	        random_R1: 0.365
1119	        embedding_R1: 0.377
1120	        embedding_minus_random_pp: 1.2
1121	      pool_200:
1122	        random_R1: 0.29
1123	        embedding_R1: 0.301
1124	        embedding_minus_random_pp: 1.1
1125	      pool_500:
1126	        random_R1: 0.222
1127	        embedding_R1: 0.232
1128	        embedding_minus_random_pp: 1.0
1129	    ranking_stable_across_pools: true
1130	    pool_ranking_stable_pct: 100
1131	    delta_trend: Δ increases from pool=50 to pool=100, then gradually shrinks at larger
1132	      pools
1133	  result_rationale: 'Strategy ranking 在 50→500 全程保持稳定（100% stability）。关键发现：delta 从  pool=50
1134	    的 0.3-0.6pp 跃升至 pool=100 的 1.2-1.4pp，然后缓慢缩小到 pool=500 的  1.0-1.2pp。
1135	
1136	    Pool=50 delta 小是因为标准 eval pool=8 的 ceiling effect 延伸——候选太少， random 已经有较高 baseline。Pool=100
1137	    时 distractor 数量足够使 mining 质量差异 充分体现（sweet spot）。Pool>200 时 delta 开始缩小因为大 pool
1138	    中 random negatives  偶然包含 "hard" negative 的概率增加（base rate effect），部分弥合了 mining
1139	    差距。 但核心 signal 不消失——pool=500 仍有 +1.0~1.2pp。
1140	
1141	    这直接回应 reviewer "pool=50 unrealistically small" concern：即使 10x 扩大， strategy ranking
1142	    完全不翻转，且 delta 在 realistic pool sizes 反而更大。
1143	
1144	    '
1145	  tables:
1146	  - name: 'Table 8: Pool Size Sensitivity (R@1 %)'
1147	    columns:
1148	    - Pool
1149	    - Encoder
1150	    - random
1151	    - embedding
1152	    - dataflow
1153	    - emb−rand (pp)
1154	    - Ranking
1155	    rows:
1156	    - - 50
1157	      - Qwen
1158	      - 57.0
1159	      - 57.3
1160	      - 55.9
1161	      - '+0.3'
1162	      - E≥R>D
1163	    - - 100
1164	      - Qwen
1165	      - 43.2
1166	      - 44.6
1167	      - 43.0
1168	      - '+1.4'
1169	      - E>R≥D
1170	    - - 200
1171	      - Qwen
1172	      - 34.8
1173	      - 36.1
1174	      - 35.0
1175	      - '+1.3'
1176	      - E>D>R
1177	    - - 500
1178	      - Qwen
1179	      - 26.5
1180	      - 27.7
1181	      - 26.2
1182	      - '+1.2'
1183	      - E>R>D
1184	    - - 50
1185	      - StarCoder
1186	      - 47.9
1187	      - 48.5
1188	      - 47.2
1189	      - '+0.6'
1190	      - E>R>D
1191	    - - 100
1192	      - StarCoder
1193	      - 36.5
1194	      - 37.7
1195	      - 36.2
1196	      - '+1.2'
1197	      - E>R>D
1198	    - - 200
1199	      - StarCoder
1200	      - 29.0
1201	      - 30.1
1202	      - 28.8
1203	      - '+1.1'
1204	      - E>R>D
1205	    - - 500
1206	      - StarCoder
1207	      - 22.2
1208	      - 23.2
1209	      - 22.0
1210	      - '+1.0'
1211	      - E>R≈D
1212	  figures_description:
1213	  - 'Fig 9: Pool size (x-axis, log) vs R@1 (y-axis), 3 strategies overlaid, separate
1214	    panels per encoder'
1215	  - 'Fig 9b: Delta (embed − random) vs pool size, showing non-monotonic pattern'
1216	  analysis: 'Pool size sensitivity 是外部有效性关键证据。非单调 pattern（小 pool delta 小 →  medium
1217	    pool delta 大 → large pool delta 缩小）提供了 mechanistic insight： mining 的价值在 moderate
1218	    difficulty 区间最大（Goldilocks zone）。 100% ranking stability 在全范围保持是 best tier 标志。
1219	
1220	    '
1221	- name: UniXcoder Multi-Seed Validation (3 seeds × 3 strategies)
1222	  plan_id: plan_020
1223	  description: 'UniXcoder-base (encoder-only, 125M) 3 seeds × 3 strategies。 s42 DONE（null
1224	    result, 0.37pp span）。s43 RUNNING（random done, embed running）。 s44 PREPARING。验证
1225	    scale boundary condition。
1226	
1227	    '
1228	  expected_results:
1229	    s42:
1230	      random_R1: 0.5534
1231	      embedding_R1: 0.5497
1232	      dataflow_R1: 0.551
1233	      span_pp: 0.37
1234	    s43:
1235	      random_R1: 0.577
1236	      embedding_R1: 0.575
1237	      dataflow_R1: 0.574
1238	      span_pp: 0.3
1239	    s44:
1240	      random_R1: 0.562
1241	      embedding_R1: 0.56
1242	      dataflow_R1: 0.561
1243	      span_pp: 0.2
1244	    mean_across_seeds:
1245	      random_R1: 0.564
1246	      embedding_R1: 0.561
1247	      dataflow_R1: 0.562
1248	    overall_span_pp: 0.3
1249	    max_pairwise_delta_pp: 0.3
1250	    all_deltas_nonsignificant: true
1251	    bootstrap_ci_all_contain_zero: true
1252	    conclusion: 125M encoder-only model saturates regardless of mining strategy
1253	  result_rationale: 'UniXcoder (125M params, encoder-only architecture) 在所有 3 seeds
1254	    上均显示  null result——3 策略 R@1 span < 0.4pp，远小于 seed variance (~1.4pp)。
1255	
1256	    原因：125M 模型 representation capacity 不足以利用 harder negatives 的信号。 Neg difficulty
1257	    分析显示 UniXcoder 的 margin 分布已高度压缩（与 Qwen 类似的  high pos_sim），但不同于 Qwen（3B, enough
1258	    capacity to learn from margin signal）， 125M 模型缺乏参数量来在这个压缩空间中进一步微调区分。
1259	
1260	    这干净地归因于 model scale 而非 architecture（UniXcoder 是 encoder-only 但 这不是核心因素——125M 即使是
1261	    decoder-only 也大概率 saturate）。Paper 中作为  "effect requires sufficient model capacity"
1262	    的 boundary condition，增强故事 的科学严谨性——不是所有模型都能 benefit from mining。
1263	
1264	    '
1265	  tables:
1266	  - name: 'Table 4: UniXcoder-base (125M) — Scale Boundary Condition'
1267	    columns:
1268	    - Seed
1269	    - random
1270	    - embedding
1271	    - dataflow
1272	    - Span (pp)
1273	    rows:
1274	    - - 42
1275	      - 55.34
1276	      - 54.97
1277	      - 55.1
1278	      - 0.37
1279	    - - 43
1280	      - 57.7
1281	      - 57.5
1282	      - 57.4
1283	      - 0.3
1284	    - - 44
1285	      - 56.2
1286	      - 56.0
1287	      - 56.1
1288	      - 0.2
1289	    - - Mean
1290	      - 56.41
1291	      - 56.16
1292	      - 56.2
1293	      - 0.25
1294	  figures_description:
1295	  - 'Fig S8: UniXcoder 3-strategy comparison across 3 seeds — flat lines within noise'
1296	  analysis: '3-seed null result 排除了 "s42 可能是巧合" 的 concern。Consistent null across  seeds
1297	    + significant effect on 3B models = clean scale boundary at ~125M-3B range。 Paper
1298	    可以明确声明："mining strategy effects require models above ~1B parameters  to manifest."
1299	
1300	    '
1301	- name: Temperature Ablation Reduced (τ = 0.05, 0.2)
1302	  plan_id: plan_021
1303	  description: 'plan_014 的 reduced 版本：τ ∈ {0.05, 0.2} × random+embedding × Qwen ×
1304	    seed 42。 如果 plan_014 (full, 70h) 无法执行，用 plan_021 (15h) 作为 minimum。
1305	
1306	    '
1307	  expected_results:
1308	    tau_005:
1309	      qwen_random_R1: 0.56
1310	      qwen_embedding_R1: 0.576
1311	      qwen_embedding_minus_random_pp: 1.6
1312	    tau_020:
1313	      qwen_random_R1: 0.538
1314	      qwen_embedding_R1: 0.55
1315	      qwen_embedding_minus_random_pp: 1.2
1316	    tau_010_reference:
1317	      qwen_random_R1: 0.553
1318	      qwen_embedding_R1: 0.567
1319	      qwen_embedding_minus_random_pp: 1.4
1320	    ranking_preserved: true
1321	    regime_specific: false
1322	  result_rationale: '与 plan_014 相同逻辑，仅覆盖 Qwen + random/embedding。如果 τ=0.05 和 τ=0.2  均显示
1323	    embedding > random（1.2-1.6pp），且 ranking 不翻转，则 regime-specificity  concern 被关闭。15h
1324	    GPU budget 是可接受的 minimum viable ablation。
1325	
1326	    '
1327	  tables:
1328	  - name: 'Table S8: Temperature Ablation (Reduced, Qwen only)'
1329	    columns:
1330	    - τ
1331	    - random R@1 (%)
1332	    - embedding R@1 (%)
1333	    - Δ (pp)
1334	    rows:
1335	    - - 0.05
1336	      - 56.0
1337	      - 57.6
1338	      - '+1.6'
1339	    - - 0.1
1340	      - 55.3
1341	      - 56.7
1342	      - '+1.4'
1343	    - - 0.2
1344	      - 53.8
1345	      - 55.0
1346	      - '+1.2'
1347	  figures_description: []
1348	  analysis: 'Reduced ablation 足以回应 reviewer concern。如果 GPU budget 允许， 扩展到 StarCoder
1349	    + dataflow（plan_014 full）提供更完整覆盖。
1350	
1351	    '
1352	- name: D062 Checkpoint Selection Criterion Effect Analysis
1353	  plan_id: d062_checkpoint_criterion
1354	  description: 'D062 创新方法论贡献：从 2980 val queries 分出 500-query selection set（用于  checkpoint
1355	    selection）+ 2480-query held-out evaluation set。分析 checkpoint  选择标准（best_by_val_loss
1356	    vs best_by_R@1）对最终性能的影响。
1357	
1358	    D065 发现：Qwen random_s43 by_R@1=0.504 vs by_val_loss=0.341（+16.3pp）， s42 两标准同一
1359	    checkpoint（R@1=0.230）。这一效应远大于 mining strategy effect。
1360	
1361	    '
1362	  expected_results:
1363	    qwen_query_split:
1364	      random_s42:
1365	        by_val_loss_R1: 0.23
1366	        by_recall_at_1_R1: 0.23
1367	        criterion_gap_pp: 0.0
1368	        note: 两标准选到同一 checkpoint
1369	      random_s43:
1370	        by_val_loss_R1: 0.341
1371	        by_recall_at_1_R1: 0.504
1372	        criterion_gap_pp: 16.3
1373	        note: 最大 criterion effect，val_loss 选 step 500, R@1 选 step 1500
1374	      random_s44:
1375	        by_val_loss_R1: 0.35
1376	        by_recall_at_1_R1: 0.385
1377	        criterion_gap_pp: 3.5
1378	      embed_s42:
1379	        by_val_loss_R1: 0.245
1380	        by_recall_at_1_R1: 0.265
1381	        criterion_gap_pp: 2.0
1382	      embed_s43:
1383	        by_val_loss_R1: 0.365
1384	        by_recall_at_1_R1: 0.518
1385	        criterion_gap_pp: 15.3
1386	      embed_s44:
1387	        by_val_loss_R1: 0.37
1388	        by_recall_at_1_R1: 0.395
1389	        criterion_gap_pp: 2.5
1390	      dataflow_s43:
1391	        by_val_loss_R1: 0.355
1392	        by_recall_at_1_R1: 0.51
1393	        criterion_gap_pp: 15.5
1394	    starcoder_query_split:
1395	      random_s42:
1396	        by_val_loss_R1: 0.28
1397	        by_recall_at_1_R1: 0.31
1398	        criterion_gap_pp: 3.0
1399	      random_s43:
1400	        by_val_loss_R1: 0.295
1401	        by_recall_at_1_R1: 0.42
1402	        criterion_gap_pp: 12.5
1403	      embed_s42:
1404	        by_val_loss_R1: 0.27
1405	        by_recall_at_1_R1: 0.305
1406	        criterion_gap_pp: 3.5
1407	      embed_s43:
1408	        by_val_loss_R1: 0.3
1409	        by_recall_at_1_R1: 0.435
1410	        criterion_gap_pp: 13.5
1411	    summary_statistics:
1412	      max_criterion_effect_pp: 16.3
1413	      mean_criterion_effect_pp: 8.5
1414	      median_criterion_effect_pp: 3.5
1415	      criterion_effect_nonzero_rate: 0.72
1416	      mining_strategy_mean_effect_pp: 1.2
1417	      criterion_to_mining_ratio: 7.1
1418	    replicates_across_encoders: true
1419	    replicates_across_seeds: true
1420	  result_rationale: 'D062 query-split evaluation 揭示了一个被忽视的方法论问题：标准 contrastive  retrieval
1421	    评估中，checkpoint 是在 val set 上选择的，然后在 SAME val set 上 报告 R@1——这导致 checkpoint selection
1422	    过拟合 val queries。
1423	
1424	    Query-split 方法将 val queries 分为 selection set (500) 和 evaluation set  (2480)。在
1425	    held-out evaluation 上，best_by_val_loss 与 best_by_R@1 的差距 高达 16.3pp（Qwen s43），因为：
1426	
1427	    (1) val_loss 在 step 500 最低——此时模型刚开始训练，泛化最好但 ranking 能力不足； (2) R@1 在 step 1500
1428	    最高——此时模型已学会 ranking 但开始 overfit； (3) 在 held-out queries 上，step 1500 的 ranking
1429	    能力泛化良好（0.504）， 而 step 500 的 ranking 能力不足（0.341）。
1430	
1431	    The criterion effect (+16.3pp max, 8.5pp mean) >> mining strategy effect (~1.2pp)，
1432	    ratio 7:1。这意味着社区对 mining strategy 效果的评估被 checkpoint selection  noise 掩盖。
1433	
1434	    StarCoder 上 effect 稍小（max 13.5pp）但方向一致——pattern replicates。
1435	
1436	    这是论文独立方法论贡献： - 发现：standard eval 系统性高估所有策略的绝对 R@1（因为 checkpoint overfit） - 发现：standard
1437	    eval 系统性低估策略间差异（因为 criterion noise 掩盖 signal） - 推荐：use query-split + R@1 criterion
1438	    for checkpoint selection
1439	
1440	    '
1441	  tables:
1442	  - name: 'Table 9: Checkpoint Criterion Effect (D062 Query-Split, Qwen)'
1443	    columns:
1444	    - Strategy
1445	    - Seed
1446	    - by val_loss R@1
1447	    - by R@1 R@1
1448	    - Gap (pp)
1449	    rows:
1450	    - - random
1451	      - 42
1452	      - 0.23
1453	      - 0.23
1454	      - '0.0'
1455	    - - random
1456	      - 43
1457	      - 0.341
1458	      - 0.504
1459	      - '+16.3'
1460	    - - random
1461	      - 44
1462	      - 0.35
1463	      - 0.385
1464	      - '+3.5'
1465	    - - embedding
1466	      - 42
1467	      - 0.245
1468	      - 0.265
1469	      - '+2.0'
1470	    - - embedding
1471	      - 43
1472	      - 0.365
1473	      - 0.518
1474	      - '+15.3'
1475	    - - embedding
1476	      - 44
1477	      - 0.37
1478	      - 0.395
1479	      - '+2.5'
1480	    - - dataflow
1481	      - 43
1482	      - 0.355
1483	      - 0.51
1484	      - '+15.5'
1485	  - name: 'Table 9b: Criterion Effect Summary'
1486	    columns:
1487	    - Statistic
1488	    - Value
1489	    rows:
1490	    - - Max criterion effect
1491	      - +16.3pp
1492	    - - Mean criterion effect
1493	      - +8.5pp
1494	    - - Mean mining strategy effect
1495	      - +1.2pp
1496	    - - Criterion-to-mining ratio
1497	      - 7.1×
1498	    - - Runs with >5pp criterion effect
1499	      - 3/14 (21%)
1500	    - - Replicates across encoders
1501	      - 'Yes'
1502	  figures_description:
1503	  - 'Fig 2: Criterion effect scatter plot — each point is one run, x=by_val_loss R@1,
1504	    y=by_R@1 R@1, diagonal line shows equality'
1505	  - 'Fig 2b: Training trajectory for s43 showing val_loss/R@1 divergence annotated
1506	    with criterion effect'
1507	  analysis: 'Checkpoint criterion effect 是 D062 论文最意外也最有影响力的发现。
1508	
1509	    +16.3pp >> +1.2pp (mining) 意味着： (1) 论文不仅展示 "mining helps" 还展示 "how to properly
1510	    evaluate whether mining helps" (2) 解释了为什么文献中 mining strategy delta 通常很小——standard
1511	    eval 掩盖了 signal (3) 提供了 evaluation protocol 改进建议，对整个 contrastive retrieval 社区有价值
1512	
1513	    s43 的 16.3pp 出现在 val_loss 和 R@1 最严重分歧时——val_loss 选择了训练最早期 的 checkpoint（泛化好但 ranking
1514	    弱），R@1 选择了训练中期的 checkpoint（ranking  最优但即将 overfit）。只有 query-split 方法才能在 held-out
1515	    上正确评判这一差异。
1516	
1517	    这一发现使论文从 "mining strategy comparison" 升级为 "evaluation methodology +  mining strategy
1518	    comparison"——双重贡献，EMNLP Main 更强。'
1519	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "592746ea-d2dd-4ece-9ab8-f0c8120cc9d4",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "c47c518c-45e7-406d-a53c-f13028df1d44",
  "sourceToolAssistantUUID": "592746ea-d2dd-4ece-9ab8-f0c8120cc9d4",
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

_source line 47 · 2026-05-16T16:04:13.790Z_

I now have a thorough understanding of the paper, its experimental setup, the actual vs. imagined results, the internal project state, and the claims being made. Let me now submit my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c47c518c-45e7-406d-a53c-f13028df1d44",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6Xn7BaaqE62ohf528ix",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6fc83e3-b168-425b-9c91-d754fcf179d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rRC3KaThXvLudZtMBaSu5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 46834,
      "cache_read_input_tokens": 68613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 46834,
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

_source line 48 · 2026-05-16T16:04:14.512Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018pGDkgWx1mU4EKAwB1B4RH`</summary>

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
  "parentUuid": "d6fc83e3-b168-425b-9c91-d754fcf179d5",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6Xn7BaaqE62ohf528ix",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c84d311d-78b7-49a4-a79c-f3a70e7e7cb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rRC3KaThXvLudZtMBaSu5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 46834,
      "cache_read_input_tokens": 68613,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 46834
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 68613,
          "cache_creation_input_tokens": 46834,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 46834,
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

_source line 49 · 2026-05-16T16:04:14.514Z_

<details><summary>↩ Tool result · `toolu_018pGDkgWx1mU4EKAwB1B4RH`</summary>

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
  "parentUuid": "c84d311d-78b7-49a4-a79c-f3a70e7e7cb9",
  "isSidechain": true,
  "promptId": "224f9b96-0063-49fc-934b-767a227b7e11",
  "agentId": "a34533294cfd6f579",
  "type": "user",
  "uuid": "aa564170-07b7-4bb5-968d-9cff7faea786",
  "sourceToolAssistantUUID": "c84d311d-78b7-49a4-a79c-f3a70e7e7cb9",
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

_source line 50 · 2026-05-16T16:05:32.312Z_



Now I have all the information needed to produce a rigorous review. Let me synthesize my findings.

---

## Review: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies, Representation Geometry, and Evaluation Methodology"

### 1. Summary

This paper presents a controlled comparison of four hard negative mining strategies (random, static embedding-distance, dataflow-aware, BM25) for contrastive code retrieval across two 3B decoder-only encoders and one 125M encoder-only model. The main findings are: (1) static embedding-distance mining yields modest but statistically significant improvements (+0.9--1.4pp R@1) at zero additional compute; (2) structure-grounded negatives show encoder-dependent effects concentrated in hard-instance strata; (3) checkpoint selection criterion introduces variation up to 16.3pp, exceeding mining strategy effects by 7x, revealing a previously unrecognized evaluation methodology confound.

### 2. Strengths

- **Well-controlled experimental design.** The 4-strategy x 2-encoder x 3-seed matrix with a fixed training pipeline (same LoRA config, same data, same K=7) isolates the mining strategy variable cleanly. This is methodologically superior to most mining strategy papers that change multiple variables simultaneously.

- **Strong statistical reporting.** Paired bootstrap CIs with 10K resamples on held-out queries, explicit p-values, and honest reporting of borderline results (dataflow p=0.089) set a good standard. The authors do not overclaim non-significant results.

- **The checkpoint criterion finding (Contribution 3) is genuinely valuable.** The observation that checkpoint selection criterion effects (+16.3pp max, 7.1x mining effect) dominate strategy effects is a novel methodological insight. The query-split evaluation protocol is a practical recommendation that the community should adopt. This is the paper's strongest contribution.

- **Comprehensive ablation coverage.** Temperature (3 settings), pool size (4 settings), hop depth (3 settings), data scaling (3 sizes), fusion head, weighted vs. binary, static vs. dynamic mining, and UniXcoder scale boundary are all covered. The ablation matrix is unusually thorough for an empirical study.

- **Honest limitation disclosure.** The SWE-bench OOD failure (R@1=0.04 vs BM25=0.273) is reported transparently and used to scope the contribution rather than being hidden. This builds credibility.

- **BM25 baseline closes an important argumentative gap.** Including BM25 negatives as a 4th strategy directly addresses the CoCoHaNeRe conflation claim with empirical evidence rather than just argumentation.

- **Cross-benchmark validation.** RepoBench-R results with non-overlapping CIs confirm the strategy ranking transfers beyond the training domain.

### 3. Weaknesses

- **The primary effect size (Claim 1) is very small and its practical significance is questionable.** The headline improvement is +1.4pp (Qwen) and +0.9pp (StarCoder) R@1 on the query-split evaluation. Even the authors' own analysis shows this is within the noise floor of standard evaluation (+0.3pp and +0.6pp under standard eval). While statistically significant, the practical impact of a 1pp improvement in R@1 for downstream code repair is unclear. The paper would benefit from connecting these R@1 improvements to downstream task performance -- but the one attempt at this (SWE-bench) failed catastrophically.

- **Three seeds is underpowered for the claims being made.** With only 3 random seeds per configuration, the seed-level variance is poorly estimated. The authors acknowledge that seed 42 (Qwen random) required a different training regime (3 epochs/patience=0 vs 2 epochs/patience=2 for seeds 43-44), making it non-comparable. This effectively reduces some comparisons to 2 seeds. The bootstrap CIs are computed at the instance level, which hides seed-level variance -- a model trained with seed X consistently outperforming seed Y across all instances would show tight instance-level CIs while the between-seed effect remains uncharacterized. This is a significant confound that the paper does not adequately address.

- **The CoCoHaNeRe "refutation" is overstated.** The paper claims to "empirically refute" CoCoHaNeRe's finding that embedding negatives are ineffective. However: (a) CoCoHaNeRe studies code search (NL-to-code), while this paper studies code-to-code file retrieval -- different tasks with different similarity structures; (b) CoCoHaNeRe uses gradient-based methods as the comparison target, which this paper does not implement; (c) the claim that CoCoHaNeRe "conflates BM25 with embedding negatives" needs stronger textual evidence from the cited paper. The argument would be more convincing framed as "our results show embedding mining works in a different setting" rather than "CoCoHaNeRe is wrong."

- **Dataflow-aware strategy (Claim 2) lacks convincing evidence.** Dataflow negatives show p=0.089 for Qwen (borderline) and p=0.210 for StarCoder (non-significant). Under standard evaluation, dataflow actually *hurts* both encoders (Qwen -1.1pp, StarCoder -0.7pp). The claim that "structure-grounded negatives interact with encoder representation geometry" is not well-supported when the effect is non-significant on one encoder and borderline on the other. The stratified analysis showing benefits in hard-instance strata is interesting but post-hoc and not corrected for multiple comparisons across the 5 stratification dimensions.

- **The 16.3pp checkpoint criterion effect appears seed-specific, not systematic.** Table 10 shows the maximum gap is +16.3pp (seed 43), but seed 42 shows 0.0pp gap (identical checkpoints). The median effect is only +3.5pp, and the mean (+8.5pp) is heavily skewed by the s43 outlier across multiple strategies. The "7.1x ratio" is computed using the mean, which is dominated by this one seed. A more honest characterization would acknowledge the high variance of this effect (0.0pp to 16.3pp) and use the median ratio instead.

- **UniXcoder null result conflates model scale with architecture.** The paper claims a "clean scale boundary at 125M parameters." However, UniXcoder is encoder-only (RoBERTa-based) while the 3B models are decoder-only. The null result could be due to architecture differences, not scale. Without a decoder-only model at an intermediate scale (e.g., 1B), the "scale boundary" claim is not separable from an "architecture boundary" alternative explanation. The paper acknowledges this in limitations but still makes the scale claim in the main text.

- **Many experiments appear to be "imagined" rather than actually completed.** Cross-referencing the paper's tables with the project roadmap reveals that several key experiments were still running or queued at paper writing time (e.g., StarCoder full chain, UniXcoder s43/s44, BM25 Phase 2 training, D062 query-split only 6/14 evaluations complete). The experiments section of the actual draft (v2/experiments.tex) contains numerous `\placeholder{}` markers. This raises concerns about whether the reported numbers represent actual experimental outcomes or projected/interpolated results.

- **No K ablation.** K=7 negatives is fixed throughout all experiments. The authors justify this as "batch size alignment" but do not test sensitivity. Given that K directly controls the hardness-to-noise ratio in InfoNCE, this is a meaningful omission.

- **Missing qualitative examples.** Plan_012 (qualitative case studies) appears in the experiment plan but not in the paper. For a paper claiming to understand *why* strategies work differently, concrete examples would substantially strengthen the narrative.

### 4. Questions for Authors

1. Can you report seed-level means and standard deviations for the main Table 2 comparisons, in addition to the instance-level bootstrap CIs? Specifically, what is the embedding-vs-random delta for each individual seed, and how variable is it across seeds?

2. The checkpoint criterion effect (Table 10) shows enormous variance across seeds (0.0pp to 16.3pp). What determines whether a seed exhibits this divergence? Is it related to the training dynamics of that specific seed, or is it a stable property? Have you verified that the 16.3pp gap is not due to a pathological training run for seed 43?

3. For the CoCoHaNeRe comparison: can you provide the specific passage where they use BM25 as a proxy for embedding negatives? Also, do you acknowledge that they study NL-to-code search (bimodal) while you study code-to-code retrieval (unimodal)?

4. The stratified analysis (Tables 6-7) reports deltas without bootstrap CIs or significance tests. Given 5 stratification dimensions x multiple strata, how do you control for multiple comparisons? Could the Q4 result (+2.3pp) be a statistical artifact of smaller sample size in extreme quartiles?

5. How do you reconcile the fact that under standard evaluation (Table 1), dataflow negatives *harm* both encoders (-1.1pp Qwen, -0.7pp StarCoder), while under query-split evaluation (Table 2), dataflow helps Qwen (+0.7pp) but still harms StarCoder (-0.4pp)? This inconsistency weakens the claim that query-split evaluation "reveals the true signal."

6. The paper states the temperature is learnable (experiments.tex line 21: "InfoNCE with learnable tau"), but the ablation (Table 8) tests fixed tau values {0.05, 0.1, 0.2}. Which is it? If learnable, what values does tau converge to for each strategy?

7. What is the overlap between the RepoBench-R evaluation repositories and the SWE-smith training repositories? If there is leakage, the "external validation" claim is weakened.

### 5. Minor Issues

- Table 1 (standard eval) and Table 2 (query-split eval) show very different absolute R@1 values (Qwen: 57% vs 37.5%). The paper should more clearly explain this gap -- is it entirely due to query difficulty, or also pool composition?
- The paper mentions "3 encoders" in the title/abstract area but UniXcoder is only used for the null result. Framing it as a third encoder overstates its role.
- The bibliography is incomplete (only 7 references in the paper.tex). Several important citations mentioned in the text (ARISE, RANGER, RepoGraph, DPR, SimCLR, Robinson et al. 2021 HCL) are missing.
- The abstract claims "Code and data will be released" but provides no anonymized link or supplementary materials.
- Table 10 has incomplete data: dataflow only has seed 43 (missing s42, s44), and BM25 is absent entirely. This asymmetry suggests incomplete experiments.

### 6. Overall Score: 3 (Weak Reject)

The paper tackles an important question with commendable experimental rigor in its design, and the checkpoint criterion finding (Contribution 3) is a genuine insight. However, the primary mining strategy effect (Claim 1) is very small (~1pp), the statistical framework masks seed-level variance by bootstrapping at the instance level, the CoCoHaNeRe refutation is overstated, and there are strong indicators that multiple experiments were not actually completed at writing time. The paper reads as a well-designed study whose results turned out to be more modest than hoped, with the evaluation methodology finding retrofitted as a primary contribution to compensate. With completed experiments, proper seed-level statistics, and appropriately scoped claims, this could become a solid contribution.

### 7. Confidence: 4/5

I have carefully examined the paper, the experimental artifacts, the project roadmap, and the internal decision logs. I am confident in my assessment of the experimental design quality and the statistical concerns. My only uncertainty is whether additional completed experiments (StarCoder full chain, UniXcoder multi-seed) might materially change the picture -- but based on the patterns observed so far, I expect they would confirm rather than overturn my assessment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa564170-07b7-4bb5-968d-9cff7faea786",
  "isSidechain": true,
  "agentId": "a34533294cfd6f579",
  "requestId": "req_011Cb6XnUn6arCSQhSGcaUgS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a46e14b-c915-4c2e-b012-3e4a22fc316f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "98678e1d-9307-4b37-b78e-c6727fde8087",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015c7wdc7bm5b1Bit1qnPWEm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 115447,
      "output_tokens": 2907,
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
          "output_tokens": 2907,
          "cache_read_input_tokens": 115447,
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
