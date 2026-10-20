# Research conversation: You are Reviewer R1 for a top ML venue review. Your focus areas are **Methods** and **Experiments**. Use a 6-point scale

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a4ff2b13031f226a3.jsonl`
- **Structured JSON:** [`b334971dde47196d95da.json`](../../sessions/b3/b334971dde47196d95da.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-14T17:07:56.707Z_

You are Reviewer R1 for a top ML venue review. Your focus areas are **Methods** and **Experiments**. Use a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target acceptance rate ~25%.

## Paper Summary

Title: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"

This is a **systematic empirical study** (self-described as an analysis paper, not a method contribution) comparing 4 hard negative mining strategies for contrastive code retrieval:
- **Random**: uniform sampling of non-gold files
- **BM25-Proxy**: top-K by BM25 score (approximates what CoCoHaNeRe called "embedding-distance" negatives)
- **Embedding-Distance**: true dense embedding nearest neighbors
- **Dataflow-Disconnected**: files structurally disconnected via CodeQL inter-procedural dataflow analysis

Setup: 2 decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B), SWE-smith training data (5K instances), pool size 50 at training time, LoRA fine-tuning, 3 seeds, InfoNCE loss with τ=0.05.

Evaluated on: SWE-smith validation (primary), RepoBench-R (cross-benchmark), SWE-bench Lite 300 instances (downstream E2E).

## Key Results

**Table 1 (Primary)**: R@1 on SWE-smith validation (pool=50):
- Qwen: Random 0.530, Embedding 0.540 (+1.0pp), Dataflow 0.532 (+0.2pp), BM25 0.521 (−0.9pp)
- StarCoder: Random 0.443, Embedding 0.450 (+0.7pp), Dataflow 0.437 (−0.6pp), BM25 0.436 (−0.7pp)
- BM25 harm not significant (p=0.12, p=0.18)

**Table 2**: BM25-Embedding gap: −1.9pp (Qwen) vs CoCoHaNeRe's reported −27pp. Direction consistent, magnitude much smaller.

**Table 3 (RepoBench-R)**: Embedding delta +0.5 to +1.0pp across conditions. CIs 2-4pp wide, all include or border zero. Dataflow negative on StarCoder, consistent with primary results.

**Tables 4-5 (SWE-bench Lite)**: All strategies resolve ~23%. Δ < 1pp, no significance. Bootstrap CIs ~8pp wide. Power analysis: N > 15,000 needed.

**Stratified Analysis (Tables 6-8)**:
- Repo size: embedding Δ ranges from +1.8pp (small repos) to +0.4pp (xlarge)
- Structural availability: dataflow Δ +0.6pp where data available (34%), +0.1pp on fallback (66%)
- Neg difficulty quartile: Q4 (hardest) emb +1.6pp, df +1.2pp; Q1 (easiest) emb +0.3pp, df −0.2pp

**Pool Size Sensitivity (Tables 9-10)**: Embedding Δ shrinks from +1.0pp (pool=50) to +0.5pp (pool=500) on Qwen. StarCoder rankings unstable at pool ≥ 200.

**Ablations**: Temperature (τ=0.05/0.1/0.2) — ranking preserved, delta shrinks at higher τ. Training data scaling (1K/3K/5K) — sub-linear scaling. Fusion head — combined only +0.2pp over emb-only. Hop count — < 0.5pp differences. Dynamic vs static mining — +0.4pp, CI includes 0, 2.3× cost. Binary vs weighted dataflow — +0.3pp, CI includes 0.

**Failure analysis**: 50 SWE-bench failures categorized. Structural gap 28%, lexical gap 36%. DF helps in 57% of structural gap cases.

**Table 20**: Comparison with inference-time graph methods (CodexGraph, LocAgent, RANGER) — positions StructFuse as complementary training-time approach.

## Experiment Design Reference (from review_context.yaml)

The full experiment design contains 14 imagined experiments. The paper covers essentially all of them:
- plan_003 (SWE-bench E2E) ✓
- plan_004 (RepoBench-R) ✓
- plan_005 (Stratified analysis) ✓ (3 of 5 strata shown; query-pos similarity and pool size strata appear separately)
- plan_007 (Hop count ablation) ✓
- plan_008 (Data size scaling) ✓
- plan_009 (Fusion head ablation) ✓
- plan_010 (Weighted vs binary DF) ✓
- plan_011 (Failure analysis) ✓
- plan_012 (Qualitative cases) ✓
- plan_014 (Temperature ablation) ✓
- plan_015 (Dynamic vs static mining) ✓
- plan_016 (Bootstrap CI) ✓
- plan_017 (Inference-time comparison) ✓
- plan_018 (BM25 baseline) ✓
- plan_019 (Pool size sensitivity) ✓

Key narrative guidance from design: Claims have been downgraded. Claim 1 → "tends to help" with wide CIs. Claim 2 (dataflow) → exploratory observation. SWE-bench delta < 1pp, cannot serve as independent evidence. Paper positioned as "Systematic Study."

## Your Review Task

Write a detailed review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (bullet points, with specific evidence from the paper)
3. **Weaknesses** (bullet points, with specific evidence)
4. **Questions for authors** (numbered)
5. **Minor issues** (if any)
6. **Overall assessment** with score and confidence

Focus specifically on:
- Methodological rigor: Is the experimental design sound? Are controls adequate?
- Statistical validity: Are CIs properly computed? Is statistical power discussed?
- Completeness of experiments: Are there missing experiments or comparisons?
- Ablation quality: Do ablations provide meaningful insight?
- Reproducibility concerns
- Whether the claims are properly calibrated to the evidence

Be critical but fair. This is an analysis paper with modest effect sizes — evaluate whether the analysis itself is valuable despite small deltas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a8e5f13c-b79e-4d5f-9dcc-e79744f9ec80",
  "agentId": "a4ff2b13031f226a3",
  "type": "user",
  "uuid": "3bfaa24d-f74e-4a1a-84fd-d616c60b4f37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T17:07:56.713Z_

```json
{
  "parentUuid": "3bfaa24d-f74e-4a1a-84fd-d616c60b4f37",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
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
  "uuid": "4dea4d3c-12ba-494c-a392-ec1020285346",
  "timestamp": "2026-05-14T17:07:56.713Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T17:08:00.844Z_



I'll start by loading the project files to get the full paper and any additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dea4d3c-12ba-494c-a392-ec1020285346",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q2Pxz1Q6L2dVLNaBnP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffd36a22-15bc-41e2-abf6-5bcad90871ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6qNf1nqJNHBjDmHiXktEu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7463,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7463,
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

_source line 4 · 2026-05-14T17:08:02.427Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01H1AAUSCT7Cju5QG76bBYEN`</summary>

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
  "parentUuid": "ffd36a22-15bc-41e2-abf6-5bcad90871ac",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q2Pxz1Q6L2dVLNaBnP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c24ba883-3e0b-4b1e-b4e9-49ecc2eb46f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6qNf1nqJNHBjDmHiXktEu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7463,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7463,
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

_source line 5 · 2026-05-14T17:08:02.431Z_

<details><summary>↩ Tool result · `toolu_01H1AAUSCT7Cju5QG76bBYEN`</summary>

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
  "parentUuid": "c24ba883-3e0b-4b1e-b4e9-49ecc2eb46f4",
  "isSidechain": true,
  "promptId": "a8e5f13c-b79e-4d5f-9dcc-e79744f9ec80",
  "agentId": "a4ff2b13031f226a3",
  "type": "user",
  "uuid": "07e398a2-9979-449a-a0c7-eadb3049b6fa",
  "sourceToolAssistantUUID": "c24ba883-3e0b-4b1e-b4e9-49ecc2eb46f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T17:08:10.970Z_



Let me read the paper report and key project files to ground my review in the actual manuscript.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07e398a2-9979-449a-a0c7-eadb3049b6fa",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q2prCKoYyaPkb168wD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca06f144-1d25-4095-ad19-2fb237b2fae6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6dSfSiGRkSbaABsLeX677",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 15712,
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

_source line 7 · 2026-05-14T17:08:11.916Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JGWjNsTzKRRZuGbhgxkkq9`</summary>

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
  "parentUuid": "ca06f144-1d25-4095-ad19-2fb237b2fae6",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q2prCKoYyaPkb168wD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a553c5ba-6a52-437c-bdae-0c1d51a9ebf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6dSfSiGRkSbaABsLeX677",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 15712,
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

_source line 8 · 2026-05-14T17:08:11.954Z_

<details><summary>↩ Tool result · `toolu_01JGWjNsTzKRRZuGbhgxkkq9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| m2_full_starcoder | Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent). | — | — | — |\\n| m1_reextract_v2 | M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 | — | — | — |\\n| m2_full_qwen | Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018. | — | — | — |\\n\\n## 待处理\\n- plan_015_dynamic（排队等待 GPU）\\n- plan_018_bm25: BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。（排队等待 GPU）\\n\\n## 近期结论\\n- **neg_difficulty_analysis** (success): Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\\n  [neg_difficulty_margin_comparison](/api/workspace-files/projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_margin_comparison_meta.txt)\\n- **m1_reextract** (failed): M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 ← 基于 m1_extraction\\n- **m1_extraction** (success): —\\n\\n## 趋势\\n成功 10 / 负向 2 / 失败 2 / 共 28\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-42106: 无 GPU 信息\\n\\n## 告警\\n- p2b-smoke-test: 已被终止 — unknown\\n- p2b-smoke2: 已被终止 — unknown\\n- p2b-smoke3: 已被终止 — unknown\\n- p2b-smoke4: 已被终止 — unknown\\n- p2b-smoke5: 已被终止 — unknown\\n- p2b-smoke6: 已被终止 — unknown\\n- p2b-smoke7: 已被终止 — unknown\\n- p2b-smoke8: 已被终止 — unknown\\n- p2b-all-9runs: 已被终止 — unknown\\n- mvp_p2b_contrastive_training: 已被终止 — unknown\\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\\n- p2b_eval_all: 已被终止 — unknown\\n- m2_early_pilot: 已被终止 — unknown\\n- m2_early_pilot_v2: 训练失败 — unknown\\n- m2_early_pilot_v3: 已被终止 — unknown\\n- m1_reextract: 训练失败 — unknown\\n\", \"total_chars\": 2314, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a553c5ba-6a52-437c-bdae-0c1d51a9ebf5",
  "isSidechain": true,
  "promptId": "a8e5f13c-b79e-4d5f-9dcc-e79744f9ec80",
  "agentId": "a4ff2b13031f226a3",
  "type": "user",
  "uuid": "4d260687-18d9-4df3-b95e-86f2c410f14a",
  "sourceToolAssistantUUID": "a553c5ba-6a52-437c-bdae-0c1d51a9ebf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T17:08:12.363Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016PuEscFk8HqfAnKz1cDCjM`</summary>

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
  "parentUuid": "4d260687-18d9-4df3-b95e-86f2c410f14a",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q2prCKoYyaPkb168wD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4dea24a5-e7b6-4f85-b2a9-ed47cc00e28d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6dSfSiGRkSbaABsLeX677",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 15712,
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

_source line 10 · 2026-05-14T17:08:12.395Z_

<details><summary>↩ Tool result · `toolu_016PuEscFk8HqfAnKz1cDCjM`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4dea24a5-e7b6-4f85-b2a9-ed47cc00e28d",
  "isSidechain": true,
  "promptId": "a8e5f13c-b79e-4d5f-9dcc-e79744f9ec80",
  "agentId": "a4ff2b13031f226a3",
  "type": "user",
  "uuid": "029b023c-bf00-4b6e-8634-66854eaa211f",
  "sourceToolAssistantUUID": "4dea24a5-e7b6-4f85-b2a9-ed47cc00e28d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T17:08:12.840Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XMYpwxCw2Dimcma92X8MKL`</summary>

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
  "parentUuid": "029b023c-bf00-4b6e-8634-66854eaa211f",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q2prCKoYyaPkb168wD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5076fb4f-bc53-428d-af68-c337842dae17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6dSfSiGRkSbaABsLeX677",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 15712,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2015
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 15712,
          "cache_creation_input_tokens": 2015,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2015,
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

_source line 12 · 2026-05-14T17:08:12.859Z_

<details><summary>↩ Tool result · `toolu_01XMYpwxCw2Dimcma92X8MKL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \\\"harm\\\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B).\\n\\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\\n\\n- **Headline result template**: \\\"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\\\"\\n\\n## Core Insight\\n\\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, similarity function s, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\\\"\\n- Backup: \\\"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically verify CoCoHaNeRe used BM25-proxy, closing the correction argument | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### In progress:\\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\\n- m1_reextract_v2: expanded extraction for higher coverage\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — closes CoCoHaNeRe correction argument)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\\\"\\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\\n\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the \\\"correcting misconception\\\" narrative loses empirical anchor\\n- Pivot: from \\\"CoCoHaNeRe was wrong because BM25 proxy\\\" → \\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; prior work's negative finding was likely due to uncontrolled variables (data, training protocol), not BM25 specifically\\\"\\n- Paper becomes less dramatic (\\\"correcting\\\" → \\\"clarifying\\\") but still valid as systematic analysis\\n- Claim 1 reworded: \\\"True embedding-distance mining consistently improves code retrieval\\\" (drop the \\\"correcting misconception\\\" framing, keep the empirical finding)\\n- Impact: weaker narrative hook but core experimental contribution survives\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\", \"total_chars\": 11181, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5076fb4f-bc53-428d-af68-c337842dae17",
  "isSidechain": true,
  "promptId": "a8e5f13c-b79e-4d5f-9dcc-e79744f9ec80",
  "agentId": "a4ff2b13031f226a3",
  "type": "user",
  "uuid": "b8cd59d8-cdab-4d31-922e-45daa4cd78d8",
  "sourceToolAssistantUUID": "5076fb4f-bc53-428d-af68-c337842dae17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T17:08:17.167Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PDvCCoae6kkTA4hasykFQy`</summary>

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
  "parentUuid": "b8cd59d8-cdab-4d31-922e-45daa4cd78d8",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q3b7yg8G1vsAAUpYAo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "193be9e6-5c0a-43e4-ae77-e763432d0659",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hs8rUGh8BuQcer2cwEWoER",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4973,
      "cache_read_input_tokens": 17727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4973,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 14 · 2026-05-14T17:08:17.183Z_

<details><summary>↩ Tool result · `toolu_01PDvCCoae6kkTA4hasykFQy`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "193be9e6-5c0a-43e4-ae77-e763432d0659",
  "isSidechain": true,
  "promptId": "a8e5f13c-b79e-4d5f-9dcc-e79744f9ec80",
  "agentId": "a4ff2b13031f226a3",
  "type": "user",
  "uuid": "14c2318f-0377-47d7-ba35-406737fe11e6",
  "sourceToolAssistantUUID": "193be9e6-5c0a-43e4-ae77-e763432d0659",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T17:08:17.735Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TBK7vdxtd6AZyAsQ443ZN1`</summary>

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
  "parentUuid": "14c2318f-0377-47d7-ba35-406737fe11e6",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q3b7yg8G1vsAAUpYAo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0388419c-15a3-4282-9cc5-88f8e2ffa7c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hs8rUGh8BuQcer2cwEWoER",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4973,
      "cache_read_input_tokens": 17727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4973,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 16 · 2026-05-14T17:08:17.761Z_

<details><summary>↩ Tool result · `toolu_01TBK7vdxtd6AZyAsQ443ZN1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/decisions.yaml\", \"content\": \"_next_id: 33\\ndecisions:\\n- id: D001\\n  date: 2026-05-12 09:57 UTC\\n  summary: 'MVP 设计: CodeQL 试点(10 repos) + 迷你对比训练(500 instances) 验证核心假设'\\n  rationale: 13 天 DDL，需要最快速验证核心假设链：(1) CodeQL inter-procedural data-flow 在 Python\\n    repos 上可行（timeout < 30%），(2) data-flow hard negatives 比 random negatives 提升检索\\n    recall。两个 phase 串行，总计约 1 天。通过后立即进入全量数据提取和训练。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-12 10:01 UTC\\n  summary: '采纳 Reviewer 反馈: MVP Phase 2 增加线性分类器 proxy 验证 + 3-seed 训练 + 显式 kill criteria'\\n  rationale: 'Reviewer 指出 Phase 2 原方案（500 instances, ~100 held-out, 2pp gate）统计效力不足，2pp\\n    差异在随机噪声范围内。增加: (1) Phase 2a 线性分类器 proxy 验证解耦特征质量与训练策略；(2) 3-seed 训练要求 ≥2/3 seed\\n    提升；(3) 每个 phase 的 fail→kill/fallback 路径。防止 13 天 DDL 下的沉没成本陷阱。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-12 10:02 UTC\\n  summary: 'H2 验证并入 Phase 1: 提取后立即统计 data-flow 连通文件 vs 不连通文件的 gold patch 覆盖率差异'\\n  rationale: Reviewer 指出 H2（特征区分度）在原 MVP 中无独立验证，Phase 2 失败时无法区分是 H2 还是 H3 问题。零成本 sanity\\n    check（统计连通/不连通文件的 gold patch 覆盖率）可在 Phase 1 提取完后立即执行，不需要训练。这比 Phase 2a 的线性分类器更早给出诊断信号。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-12 11:21 UTC\\n  summary: 'Phase 1 gate PASS: timeout 0%, H2 Fisher p=1.54e-7, 75% instance recall.\\n    进入 Phase 2。'\\n  rationale: 10 repos 中 8 个成功提取（2 个 skip 因 buggy file 路径不存在，非 CodeQL 限制）。timeout rate\\n    0% 远低于 30% 阈值。H2 sanity check：连通文件 gold 覆盖 1.44% vs 不连通 0.00%，Fisher p=1.54e-7。75%\\n    instance recall（6/8 gold file 在连通集）。数据质量问题（路径匹配、skip rate、registry 注册）并行修复，不阻塞\\n    Phase 2。\\n  related_experiments: []\\n  depends_on: []\\n- id: D005\\n  date: 2026-05-12 11:35 UTC\\n  summary: 'CRITICAL: GPU 越界 PID 59170 跑在 GPU 5 而非分配的 cuda:4，立即 kill + 全脚本修复 CUDA_VISIBLE_DEVICES'\\n  rationale: Reviewer 核实 nvidia-smi 发现 run_mvp.py 在 GPU 5 上运行 9.3GB，而项目分配的 cuda:4\\n    完全空闲。违反 L1 红线（GPU 资源边界）。要求 Agent 立即 kill 进程、修复所有脚本强制 CUDA_VISIBLE_DEVICES=4、排查\\n    dry-run 是否也越界。\\n  related_experiments: []\\n  depends_on: []\\n- id: D006\\n  date: 2026-05-12 17:24 UTC\\n  summary: P2b pass criteria 调整：recall@5→recall@1，pool_size 26→50+，阈值 ≥2pp 不变\\n  rationale: Eval v2 (pool_size=26) 显示 random recall@5 已达 98.4-99.2%，原标准\\\"dataflow\\n    recall@5 > random ≥2pp\\\"数学上几乎不可能达标（天花板仅 0.8-1.6pp 空间）。recall@1 有更大区分度（random mean\\n    93.97%），且是更严格的排序指标。同时扩大 pool_size 至 50+ 使 recall@5/10 也获得有效梯度。新标准：dataflow_aware\\n    recall@1 > random recall@1 ≥2pp in ≥2/3 seeds，pool_size=50。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: random recall@1 mean=0.940, emb_dist recall@1=0.669 at pool=26; recall@5\\n      ceiling\\n  depends_on:\\n  - D002\\n- id: D007\\n  date: 2026-05-12 19:52 UTC\\n  summary: MVP P2b dataflow 策略不可验证：connected⊆gold 导致数据相同。决定：50-repo 规模验证 + Scheme\\n    B 备份\\n  rationale: 修复 build_p2b_data.py 后重新生成数据，train_dataflow.jsonl 仍与 train_embedding.jsonl\\n    完全相同。根因：8 个 MVP repos 中 dataflow 连接文件全部是 gold 文件的子集（connected-but-not-gold = 0），non_pos\\n    过滤无差异。这不是方法缺陷而是规模问题——小 repo 紧耦合，2-hop 连接集≈gold 集。P1（Fisher p=1.54e-7）和 P2a（AUC=0.78）仍有效，说明\\n    dataflow connectivity 有信号，只是 MVP 规模不足以分离 connected-but-not-gold 子集。决策：(1) 立即跑\\n    50-repo 样本的 overlap 统计（CPU, ~2-4h），确认大规模下 connected⊃gold；(2) 并行准备 Scheme B（distance-weighted\\n    negatives）作为 pivot 备选；(3) overlap>20% 实例有 connected≠gold → 进入全量 M1 提取；overlap≈100%\\n    → pivot to Scheme B。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: dataflow≡embedding 因 connected⊆gold\\n  depends_on:\\n  - D006\\n  - D004\\n- id: D008\\n  date: 2026-05-12 20:38 UTC\\n  summary: MVP 条件性通过：P1+P2a PASS，P2b dataflow 在 MVP 规模不可测但 50-repo 规模验证确认方法可行（Z=40.8%）。进入\\n    research 阶段。\\n  rationale: MVP 三阶段结果：P1 PASS（timeout 0%, Fisher p=1.54e-7, 75% instance recall）；P2a\\n    PASS（AUC 0.78, BM25 系数为负）；P2b 部分有效——random>>embedding（-27pp recall@1 at pool=26,\\n    -3.7pp at pool=50）确认 naive hard negatives 有害，但 dataflow vs random 因 connected⊆gold\\n    无法在 8 repos 上区分。50-repo 规模验证 Z=40.8%（中型 repo 55.7%），timeout 4%，确认方法在全量数据上可行。Kill\\n    criteria 均未触发。P2b dataflow 对比将在 M2 全量训练中完成。\\n  related_experiments:\\n  - exp_id: mvp_p1_codeql_feasibility\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2a_linear_proxy\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: evidence\\n    result: partial - random>>emb confirmed, dataflow untestable at MVP scale\\n  depends_on:\\n  - D007\\n  - D006\\n  - D004\\n- id: D009\\n  date: 2026-05-12 22:04 UTC\\n  summary: Dream 审稿完成：best=Weak Accept, median=Weak Reject, worst=Reject。批准 P0 启动，但\\n    plan 需增补 5 个 dream-derived 实验\\n  rationale: 三档共识问题：(1) 单编码器无法支撑 generality claim，需加 StarCoder/CodeBERT；(2) static\\n    vs dynamic embedding mining 是潜在 confound；(3) τ=0.05 可能 regime-specific；(4) SWE-bench\\n    +2pp 需 bootstrap CI；(5) abstract \\\"complementary\\\" 需降调。关键风险变量是 M1 的 Z%：≥35% best\\n    framing 成立，20-35% pivot 到 Claim 2 headline，<20% 需重大调整。已在 experiment_plan.yaml\\n    增加 plan_013-017（+35h GPU），paper_framing.md 增加 contingency framing。P0 实验（M1 已在跑）可继续，不需\\n    re-dream。\\n  related_experiments:\\n  - exp_id: dream_20260512T204322\\n    role: dream_simulate\\n    result: best=WA, median=WR, worst=R\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-12 22:09 UTC\\n  summary: plan_013 (second encoder) 从 P1 升级至 P0，headline template 降调修复\\n  rationale: Reviewer 指出 single encoder 是 best→accept 的关键区分因素，在 best-R1-W1 和 median-R2-W5\\n    两档都出现。P1 排期可能导致论文缺少 generality 证据而被 WR。升级后 M2 完成即可并行启动 plan_013。同时修复 headline\\n    template \\\"cannot recover\\\" → \\\"complementary signal not captured by\\\"。\\n  related_experiments:\\n  - exp_id: plan_013\\n    role: priority_upgrade\\n    result: P1→P0\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-13 01:38 UTC\\n  summary: Z%=74.0% 确认 Best Framing — Claim 1 为 headline，批准 M2 早期训练\\n  rationale: M1 部分数据（24/222 repos, 5128 instances）Z%=74.0%，远超 ≥35% 阈值。对比 D007 的 40.8%（50\\n    SWE-bench repos），SWE-Smith 数据集跨文件依赖密度更高。Best framing 成立：Claim 1 (\\\"structure-grounded\\n    negatives outperform\\\") 为 headline。批准在当前 5K instances 上做 M2 早期训练 pilot（3 strategies\\n    × 1 seed），利用 cuda:4 空闲期获取早期信号，不等全量 M1（还需 ~46h）。磁盘已清理至 61GB free (64%)，足够训练。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: Z%=74.0% at 24/222 repos\\n  - exp_id: d007_50repo_overlap\\n    role: baseline\\n    result: Z%=40.8% on SWE-bench 50 repos\\n  depends_on:\\n  - D009\\n  - D010\\n- id: D012\\n  date: 2026-05-13 02:11 UTC\\n  summary: Kill m2_early_pilot_v3 (PID 897752) — 第二次 GPU 越界 (cuda:0)\\n  rationale: Reviewer 发现 m2_early_pilot_v3 在 cuda:0 运行（PID 897752, 17100 MiB），项目仅分配\\n    cuda:4。这是第二次 GPU 越界（第一次 D005 在 GPU 5）。立即 kill 并标记 killed。同时 m2_early_pilot_v2\\n    因 wandb API key error 已崩溃标记 FAILED。当前唯一合法训练为 PID 795791 (m2_early_pilot, cuda:4)。要求\\n    Agent 排查越界原因并确保后续脚本强制 CUDA_VISIBLE_DEVICES=4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot_v3\\n    role: violated\\n    result: killed - GPU 越界 cuda:0\\n  - exp_id: m2_early_pilot_v2\\n    role: failed\\n    result: wandb API key error\\n  - exp_id: m2_early_pilot\\n    role: active\\n    result: PID 795791 on cuda:4, running\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-13 02:50 UTC\\n  summary: 服务器迁移：cqa1-21977 cuda:4 → bjb1-42106 cuda:0/1 (RTX PRO 6000 96GB×2)\\n  rationale: Manager 分配独立服务器 bjb1-42106（2x RTX PRO 6000 96GB）。迁移策略：(1) M1 提取继续在 cqa1-21977\\n    CPU 上完成（不中断），(2) 新服务器立即搭建环境+同步代码+下载模型，(3) M2 early pilot 在 cqa1-21977 cuda:4 跑完后所有\\n    GPU 工作转到新服务器，(4) 通知 Manager 释放 cuda:4。RTX PRO 6000 96GB 彻底解决 M3a VRAM 问题（Qwen3.6-27B\\n    不再需要 fallback），2 卡可并行 M2 全量 + plan_013。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: in_progress\\n    result: finishing on cqa1-21977 cuda:4\\n  - exp_id: m1_extraction\\n    role: in_progress\\n    result: CPU only, stays on cqa1-21977\\n  depends_on:\\n  - D011\\n- id: D014\\n  date: 2026-05-13 04:44 UTC\\n  summary: Kill m2_early_pilot (PID 795791) — 过拟合+卡死，bjb1 m2_embed_verify 取代\\n  rationale: m2_early_pilot 在 cqa1 cuda:4 上仅完成 random 策略（best val_loss=0.5879 at step\\n    1500，之后持续过拟合到 0.728）。进程在 step 4000 卡死 45+ min。OOM 干扰（另一进程在同 GPU 启动）。embedding_distance\\n    和 dataflow_aware 策略未启动。bjb1 上的 m2_embed_verify 使用 true embedding mining + 更大参数（negatives=7,\\n    seq_len=2048, batch=8）+ eval bug fix，将完全取代此 pilot。通知 Manager 释放 cqa1 cuda:4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: killed\\n    result: random best val_loss=0.5879, overfitting after step 1500\\n  - exp_id: m2_embed_verify\\n    role: replacement\\n    result: preparing on bjb1 cuda:1\\n  depends_on:\\n  - D011\\n  - D013\\n- id: D015\\n  date: 2026-05-13 11:43 UTC\\n  summary: 全量 Z%=78.0%（条件）确认 Best Framing；Coverage 34.3% 需论文讨论\\n  rationale: 全量 M1（123/131 repos, 44,173 instances）统计：15,153 instances 有结构数据（34.3%），其中\\n    11,825 有 connected-but-not-gold 文件（条件 Z%=78.0%，高于 pilot 72.5%）。条件 Z% 远超 35% 阈值，Best\\n    Framing（Claim 1 as headline）完全成立。但 Coverage 仅 34.3%——65.7% instances CodeQL/Beniget\\n    未产出结构连接，论文需讨论此局限性并限定 claim 范围为\\\"有结构数据的 instances\\\"。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: 123/131 repos, 44173 instances, 15897 structural\\n  - exp_id: plan_006_scalability\\n    role: prior_pilot\\n    result: pilot Z%=72.5% on 29 repos\\n  depends_on:\\n  - D011\\n- id: D016\\n  date: 2026-05-13 15:24 UTC\\n  summary: 'Reviewer Critical: m2_embed_verify 和 plan_013_starcoder 实际已完成全部 3 策略，registry\\n    错误标记为 failed'\\n  rationale: Reviewer 直接从服务器日志验证：两个实验的 dataflow 策略均已完成（\\\"All 3 strategies completed\\\"），EXIT_CODE\\n    异常发生在训练完成之后（wrapper 脚本问题）。关键数据：(1) Qwen dataflow peak R@1=0.5584 (+2.27pp vs random)，支撑\\n    Claim 1；(2) StarCoder dataflow R@1=0.4869 < random 0.4922，encoder-agnostic claim\\n    受挑战；(3) 两个编码器的 dataflow 策略均严重过拟合（train loss→0）。已派 Agent 紧急修正 registry + 收集完整 metrics\\n    + 验证 StarCoder random 数据来源。方向决策待 Agent 汇报验证数据后确定。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 实际完成（3 strategies all done），Qwen dataflow peak R@1=0.5584\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 实际完成（3 strategies all done），StarCoder dataflow R@1=0.4869 < random 0.4922\\n  depends_on: []\\n- id: D017\\n  date: 2026-05-13 16:03 UTC\\n  summary: Pilot 结果验证完成：embedding > random 跨编码器一致；dataflow 需按两种 checkpoint 标准报告；Claim\\n    2 需修订\\n  rationale: 'Reviewer 验证 18 个指标全部精确匹配。核心发现：(1) embedding > random 在 Qwen (+2.0pp)\\n    和 StarCoder (+1.6pp) 上一致，是最稳健结论；(2) dataflow 排名取决于 checkpoint 选择——按 val_loss:\\n    embedding > dataflow > random (Qwen)，按 peak R@1: dataflow > embedding > random\\n    (Qwen)；(3) StarCoder dataflow final eval 追平 embedding (0.5078=0.5078)，\\\"embedding\\n    consistently beats dataflow\\\" 不成立；(4) Claim 2 (\\\"embedding harms\\\") 在 true embedding\\n    mining 下不复现，仅在 MVP BM25 proxy 下成立。全量 M2 训练需报告两种 checkpoint 标准下的结果，避免 cherry-picking\\n    质疑。Paper framing 修订延后至全量 M2 结果出来后。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 'Qwen: embedding(0.5557) > dataflow(0.5436) > random(0.5357) by val_loss;\\n      dataflow peak(0.5584) > embedding(0.5557) by R@1'\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 'StarCoder: embedding(0.5078) > random(0.4922) > dataflow(0.4869) by val_loss;\\n      dataflow final(0.5078) = embedding'\\n  depends_on:\\n  - D016\\n- id: D018\\n  date: 2026-05-13 16:04 UTC\\n  summary: 不做预判性 framing pivot，full M2 (18 runs) 是 go/no-go 唯一判据；双 checkpoint 标准；准备\\n    B/C 两条后备路线\\n  rationale: Pilot 仅 24 repos / 1 seed，<2pp delta 统计功效不足以支持强 claim 或否决原假设。Full M2\\n    (131 repos × 3 strategies × 3 seeds × 2 encoders = 18 runs) 提供 3-seed 统计功效，是唯一可信判据。不选\\n    Agent 提议的 A/B/C 任何一个——过早锁定叙事会限制后续解读空间。数据构建已在进行，不浪费时间在 framing 讨论上。Full M2 结果出来后根据实际数据\\n    pattern 决定：(a) dataflow 跨编码器一致 > random → 原 framing 修正后可用；(b) dataflow 不一致但 embedding\\n    一致 → 方案 B 或 C；(c) 所有差异不显著 → 需要更大规模实验或 pivot。同时要求 dual checkpoint (best-val-loss\\n    + best-R@1) 和 3-seed CI 确保结果可信。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-13 18:08 UTC\\n  summary: D018 补充：Full M2 go/no-go 量化阈值 + 统计检验方案\\n  rationale: 'Reviewer 指出 D018 缺量化阈值，go/no-go 判据需在结果出来前明确，避免事后 rationalization。\\n\\n\\n    **统计方法**：每个 encoder 3 seeds 的 R@1 (best-by-val-loss checkpoint) 做 paired difference，bootstrap\\n    95% CI + paired t-test (p<0.05)。同时报告 best-by-R@1 checkpoint 结果作为透明度补充。\\n\\n\\n    **Go/No-Go 阈值**：\\n\\n    (A) Go — 原 framing 可用：dataflow > random 的 95% CI 在两个 encoder 上均 > 0\\n\\n    (B) Conditional Go — 修正 framing：dataflow > random 在至少一个 encoder 上 CI > 0，另一个 CI\\n    含 0（差异不显著）\\n\\n    (C) No-Go for Claim 1：dataflow ≤ random 在两个 encoder 上 CI 均含 0 或为负 → Claim 1 失效，pivot\\n    到 \\\"mining strategy × architecture\\\" 分析论文\\n\\n\\n    **Claim 2 判据**：若 full M2 显示 embedding > random 且 CI > 0 → 原 Claim 2 (\\\"embedding\\n    harms\\\") 被否定。新 Claim 2 候选：\\\"true embedding mining helps, but BM25 proxy harms\\\" 或\\n    \\\"hard negative mining method matters more than hard negative source\\\"\\n\\n\\n    **跨 encoder 一致性规则**：\\n\\n    - 同方向同显著 → 强泛化 claim\\n\\n    - 同方向不同显著 → 条件 claim + architecture discussion\\n\\n    - 反方向 → Claim 1 原形式被拒，需 conditional reframe\\n\\n\\n    阈值在 full M2 结果出来前锁定，不允许事后修改。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING - random_s42 in progress\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING - data build phase\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-13 18:10 UTC\\n  summary: D019 补充：Claim 2 完整判定矩阵 + n=3 功效限制声明\\n  rationale: 'Reviewer 指出 D019 的 Claim 2 阈值不完整 + n=3 统计功效天然受限。补充如下：\\n\\n\\n    **Claim 2 完整判定矩阵**（3 seeds, paired bootstrap 95% CI）：\\n\\n    (i) random > embedding CI>0 → Claim 2 confirmed（embedding harms，与 MVP 一致）\\n\\n    (ii) embedding > random CI>0 → Claim 2 falsified（true embedding mining helps，需\\n    reframe）\\n\\n    (iii) CI 含 0 → inconclusive（效应存在但检测不到或确实无差异，论文报告为 \\\"no significant difference\\\"\\n    + 报告 effect size）\\n\\n\\n    **n=3 功效限制**（显式承认，不修改阈值）：\\n\\n    - df=2 时 t 临界值 4.303，pilot 级别差异（<2pp）极难达到 p<0.05\\n\\n    - Bootstrap n=3 仅 27 种重采样，CI 估计粗糙\\n\\n    - 阈值框架偏向 No-Go（Type II error 高）\\n\\n    - 若结果落入 (C) No-Go，论文 Discussion 必须讨论功效限制，不能简单声明 \\\"dataflow 无效\\\"\\n\\n    - 这是算力约束下的合理选择，不改阈值，但明确风险\\n\\n\\n    **plan_014 排期**：Full M2 完成后优先启动 plan_014（temperature ablation, ~10h）——无论 Claim\\n    2 reframe 成哪个方向，temperature regime-specificity 都需要回答。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING\\n  depends_on:\\n  - D019\\n- id: D021\\n  date: 2026-05-13 19:10 UTC\\n  summary: Negative difficulty 分析揭示 encoder capacity 差异是 dataflow 效果不一致的根因\\n  rationale: '预训练模型 cosine similarity 分析显示：Qwen pretrained embeddings 分辨力弱（random\\n    cosine sim 0.899），StarCoder 分辨力强（random cosine sim 0.553）。Dataflow negatives 在两个模型上都比\\n    random 更难（higher sim），说明方法设计正确。但 StarCoder 已经\\\"懂\\\"结构差异（所有策略 sim 都低），额外训练信号边际收益小。这解释了\\n    pilot 中 StarCoder dataflow < random 的现象：不是方法问题，是 encoder 已有足够 capacity。\\n\\n\\n    论文价值：(1) 从 negative result 中提取 mechanistic explanation；(2) 定义 method applicability\\n    condition：\\\"structure-grounded negatives benefit most when pretrained encoder has\\n    limited structural separability\\\"；(3) 产出论文级图表（Figure: Negative Difficulty Distributions）；(4)\\n    无论 full M2 落入 A/B/C，这个分析都增加论文深度。不修改 go/no-go 阈值，但丰富解读框架。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: context\\n    result: 'Qwen: dataflow > random (+0.8~2.3pp)'\\n  - exp_id: plan_013_starcoder\\n    role: context\\n    result: 'StarCoder: dataflow < random (-0.5pp), explained by high pretrained separability'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D022\\n  date: 2026-05-13 19:25 UTC\\n  summary: M1 28K instances 可恢复（运行时故障非数据问题）；当前 M2 继续，并行后台重跑 M1 提取\\n  rationale: 'Fuzzy match 抽查 10/10 发现 buggy_file 全部存在——28,276 个 \\\"error\\\" 是 CodeQL 并行提取时的运行时故障（磁盘/存储瞬态），不是\\n    SWE-smith 数据质量问题。训练数据潜在从 15,897 → ~44,173（2.8x）。\\n\\n\\n    决策：不中断当前 M2 训练 + 并行后台重跑 M1 提取。理由：\\n\\n    (1) 当前 M2 已在双卡运行，中断重来延期 3-7 天超出 DDL\\n\\n    (2) M1 重提取是 CPU 工作，可在 bjb1-42106 后台运行不影响 GPU 训练\\n\\n    (3) 如果当前 M2 结果落入 (C) No-Go 或 effect size 太小，扩展数据集是 natural next step\\n\\n    (4) 2.8x 数据量可能显著缓解 dataflow 过拟合问题（D021 中的核心风险）\\n\\n\\n    Claim 3 叙事需修正：\\\"64% failure 是上游数据问题\\\" → \\\"64% 是运行时提取故障，CodeQL 本身在有效输入上 100% 成功，可通过重跑恢复\\\"。这是\\n    engineering limitation with clear fix，不是方法局限。'\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: primary\\n    result: 28,276 instances recoverable - runtime failure, not data quality\\n  - exp_id: plan_006_scalability\\n    role: affected\\n    result: 'error classification needs correction: buggy_file_not_found was misattributed'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D023\\n  date: 2026-05-13 19:43 UTC\\n  summary: Kill M1 重提取：bjb1 CodeQL 查询 100% 失败，D022 前提不成立需诊断后重新评估\\n  rationale: Reviewer CRITICAL 发现 bjb1-42106 上 CodeQL call_graph.ql 查询全部 exit status\\n    2，317/325 行失败，零有效结构数据产出。原 M1 在 cqa1-21977 成功，迁移后 CodeQL 版本/QL pack 可能不兼容。立即 kill\\n    进程释放 CPU/RAM，诊断 CodeQL 配置后决定修复或换服务器。\\n  related_experiments:\\n  - exp_id: m1_reextract\\n    role: subject\\n    result: killed - CodeQL incompatible on bjb1\\n  depends_on:\\n  - D022\\n- id: D024\\n  date: 2026-05-14 00:49 UTC\\n  summary: 'Major paper framing rewrite: drop falsified \\\"embedding harms\\\" claim, pivot\\n    to \\\"systematic analysis + mechanistic insight\\\" narrative'\\n  rationale: 'Reviewer deep assessment confirmed Claim 2 (\\\"embedding actively harms\\\",\\n    -27pp) was built on BM25-proxy mislabeled as embedding-distance in MVP. D017 proved\\n    true embedding mining helps (+1.6-2.0pp). New framing: (1) embedding universally\\n    helps (corrects misconception), (2) dataflow conditionally helps (mediated by\\n    representation saturation), (3) CodeQL scalable. This is a stronger, more honest\\n    paper type for EMNLP — empirical analysis with mechanistic depth rather than false\\n    \\\"our method beats all\\\" claim.'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: embedding > random confirmed for both encoders\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: dataflow helps Qwen only, not StarCoder — conditional benefit\\n  - exp_id: neg_difficulty_analysis\\n    role: evidence\\n    result: pos_sim saturation explains strategy-encoder interaction\\n  depends_on: []\\n- id: D025\\n  date: 2026-05-14 01:01 UTC\\n  summary: Plan_014 temperature ablation 缩减为 2 strategies × 3τ × 2 epochs = 6 runs\\n    (~70h)，deadline 可达\\n  rationale: 原方案 9 runs × 3 epochs = 157h GPU，超出 May 25 ARR 截稿。缩减理由：(1) 回答 Dream reviewer\\n    的 regime-specificity concern 只需证明 embedding vs random 的相对优势跨 τ 一致，不需要 3 策略全跑；(2)\\n    M2 和 pilot 均显示 epoch 3 过拟合无收益，2 epochs 足够；(3) τ=0.07 已由 M2 覆盖，只需 {0.05, 0.1, 0.2}。6\\n    runs × ~11.7h = ~70h → 双卡并行 35h wall time，M2 完成后 ~1.5 天可跑完。Dataflow strategy 的\\n    τ ablation 降为 P2，时间充裕再补。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: step 1000 best, epoch 3 overfitting → 2 epochs sufficient\\n  - exp_id: plan_014\\n    role: target\\n    result: budget revised from 10h to 70h, scope from 9 to 6 runs\\n  depends_on:\\n  - D024\\n- id: D026\\n  date: 2026-05-14 02:56 UTC\\n  summary: Qwen eval@2000 确认过拟合，后续 M2 runs 从 3 epochs 减至 2 epochs\\n  rationale: 'eval@2000: val_loss=0.5162, R@1=0.5228（与 @1500 持平，未恢复）。Best 锁定 step\\n    1000 (epoch 1 中段)。train_loss=0.04 vs val_loss=0.52，gap 持续扩大。模式与 pilot 一致（best\\n    at ~25% training）。当前 s42 保留 3 epochs 完整跑完（提供 full overfitting curve 数据），后续 8 runs/encoder\\n    设 max_epochs=2。节省 ~48h/GPU，M2 完成时间从 ~May 20-21 提前到 ~May 18-19。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: eval@2000 R@1=0.5228 flat, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: pending\\n    result: eval@1000 still improving, apply 2-epoch precaution for subsequent seeds\\n  depends_on:\\n  - D025\\n- id: D027\\n  date: 2026-05-14 08:13 UTC\\n  summary: M2 剩余 runs 加 early stopping (patience=2 evals)，加速关键路径\\n  rationale: Reviewer 计算 M2 全 18 runs 需 ~5.5 天（StarCoder 瓶颈 ~133h）。两个编码器 best checkpoint\\n    均在 step 1000，之后 val_loss 持续上升。加 early stopping（patience=2，即连续 2 次 eval@500 无改善即停）预计在\\n    step 2000 左右停止（vs 2828 full 2-epoch），节省 ~30% 时间（~1.5 天），M2 从 May 19.5 提前到 ~May\\n    18。关键路径 May 25 ARR 余量从 5 天增至 7 天。风险低：仅影响未启动的 runs，不改已跑数据。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  depends_on:\\n  - D026\\n- id: D028\\n  date: 2026-05-14 11:09 UTC\\n  summary: Claim 2 降级待定：M2 full 结果决定 \\\"conditional benefit\\\" 是独立 claim 还是降为 observation\\n  rationale: Reviewer 覆盖率审查指出 Claim 2 最薄弱：n=2 encoders 交互效应无统计功效，neg_difficulty 是描述性非实验性证据。建议降为\\n    \\\"observation + mechanistic hypothesis\\\"。决策延迟到 M2 full 18 runs 完成后：若 Qwen dataflow>random\\n    p<0.05 则保持 conditional claim；否则降级为 observation。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: Qwen pilot positive\\n    result: dataflow > random +0.8pp val_loss\\n  - exp_id: plan_013_starcoder\\n    role: StarCoder pilot negative\\n    result: dataflow < random -0.5pp\\n  - exp_id: m2_full_qwen\\n    role: go/no-go for claim strength\\n    result: RUNNING\\n  - exp_id: m2_full_starcoder\\n    role: encoder generality test\\n    result: RUNNING\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D029\\n  date: 2026-05-14 16:23 UTC\\n  summary: Dream full review 完成：7 条三档一致结构性问题确认，BM25 baseline 升为 P0，pool size sensitivity\\n    新增 plan_019\\n  rationale: 'dream_20260514T075732 (full review mode) 三档评分: Best 4/6 WA, Median 3/6\\n    WR, Worst 3/6 WR。跨三档一致的结构性问题 7 条：(1) 缺 BM25 baseline 是 #1 共识——论文核心叙事（纠正 CoCoHaNeRe）无实证支撑，已加\\n    plan_018 P0；(2) N=2 编码器限制——保持 honest framing，无法加更多编码器；(3) StarCoder 误标为 encoder-decoder——已修正为\\n    decoder-only；(4) RepoBench-R 无 CIs——plan_004 已标注多 seed 要求；(5) Pool=50 太小——新增 plan_019\\n    P1；(6) 34% structural coverage 未分层——plan_005 已扩展；(7) Checkpoint selection criterion\\n    未指定——写作时明确。观察项：effect sizes 太小（等 M2 真实数据）、overfitting 分析（提取现有训练 log）。忽略项：broken\\n    bibliography（dream artifact）、0 figures（dream artifact）。评分顺序正常（best≥median=worst）。下一步：派\\n    Agent 准备 BM25 mining（CPU），M2 完成后立即执行 plan_018 training phase。'\\n  related_experiments:\\n  - exp_id: plan_018\\n    role: new P0 experiment added\\n    result: planned\\n  - exp_id: plan_019\\n    role: new P1 experiment added\\n    result: planned\\n  - exp_id: plan_004\\n    role: updated with multi-seed CI requirement\\n    result: planned\\n  - exp_id: plan_005\\n    role: extended with structural coverage stratification\\n    result: planned\\n  depends_on:\\n  - D024\\n  - D028\\n- id: D030\\n  date: 2026-05-14 16:23 UTC\\n  summary: Dream dream_20260514T075732 分析完成：7 项确认行动 + 5 项观察项 + re-dream 后批准新 P0\\n  rationale: 'Dream full review (2 Reviewers roundtable) 三档评分: Best=4/6(WA), Median=3/6(WR),\\n    Worst=3/6(WR)。Median 未达 borderline，需修复结构性问题后 re-dream。\\n\\n\\n    **三档一致的结构性问题（7 项确认行动）：**\\n\\n    1. [EXP] 缺 BM25 negative baseline — 论文核心 narrative (correcting CoCoHaNeRe) 无实证。加\\n    plan_018, P0, Phase1 CPU 立即启动\\n\\n    2. [EXP] RepoBench-R 缺 CIs — plan_004 增加多 seed 评估\\n\\n    3. [EXP] Pool size 50 过小 — 加 plan_019 sensitivity analysis\\n\\n    4. [EXP] 34% structural coverage 未分层 — 扩展 plan_005 加 structural-available vs fallback\\n    stratum + neg_difficulty quartile\\n\\n    5. [FRAMING] N=2 encoders → 降级为 \\\"observation + hypothesis\\\"，非 validated mechanism\\n\\n    6. [FRAMING] StarCoder 架构 → 修正为 \\\"decoder-only\\\"（已改）\\n\\n    7. [FRAMING] Claim 3 (CodeQL pipeline) → 降为 supporting methodology（已改）\\n\\n\\n    **观察项（等真实数据）：**\\n\\n    1. Effect sizes marginal [M][W] — 等 M2 full 统计结果\\n\\n    2. Dataflow claim strength [M][W] — D028 已 plan\\n\\n    3. \\\"Scaling law\\\" [W] → 用 \\\"trend\\\" + CIs\\n\\n    4. Temperature ablation contradiction [W] — plan_014 结果决定\\n\\n    5. Zero method contribution [M][W] — framing 强度决定\\n\\n\\n    **Re-dream 要求：** framing + plan 修改完成后需 re-dream，best ≥ WA 且 median ≥ borderline\\n    后才批准新 P0 实验。已在跑的实验继续。'\\n  related_experiments:\\n  - exp_id: dream_20260514T075732\\n    role: trigger\\n    result: best=4/6 WA, median=3/6 WR, worst=3/6 WR\\n  - exp_id: plan_018\\n    role: new_from_dream\\n    result: planned — BM25 baseline\\n  - exp_id: plan_019\\n    role: new_from_dream\\n    result: planned — pool size sensitivity\\n  depends_on:\\n  - D028\\n  - D024\\n- id: D031\\n  date: 2026-05-14 17:02 UTC\\n  summary: 'BM25 Phase 1 完成: 87% overlap with embedding_distance，预示论文叙事可能从 \\\"纠正误标\\\"\\n    转向 \\\"受控对比证明 hard negatives 普遍有效\\\"'\\n  rationale: 'plan_018 Phase 1 (CPU) 完成。3 seeds BM25 negatives 已生成，与 embedding_distance\\n    negatives 重叠率高达 87.1%。小 repo 候选池 ≤50 导致所有策略完全重合，BM25 differentiation 主要在大 repo\\n    上体现。\\n\\n\\n    Phase 2 训练结果预期 3 种可能：\\n\\n    A) BM25 harm (BM25 << random) → 原叙事成立（\\\"BM25 proxy 导致 CoCoHaNeRe 错误结论\\\"）\\n\\n    B) BM25 ≈ random → contingency per D030（叙事降为 \\\"systematic comparison\\\"）\\n\\n    C) BM25 ≈ embedding_distance (87% overlap 强烈预示) → 叙事升级为\\\"BM25 和 embedding mining\\n    高度重叠，两者在受控环境下都优于 random；CoCoHaNeRe 的负面结论源于实验控制不足而非 BM25-proxy 本身\\\"\\n\\n\\n    Scenario C 实际上比 A 更强——我们提供的不只是标签纠正，而是受控对比 + 叙事升级。\\n\\n\\n    附带决策：plan_015 暂缓至 camera-ready（44h 超预算 + DDL 紧），Limitations 中承认 static vs dynamic\\n    confound。'\\n  related_experiments:\\n  - exp_id: plan_018\\n    role: phase1_complete\\n    result: BM25 data ready, 87% overlap with embedding_distance\\n  - exp_id: plan_015\\n    role: deferred\\n    result: design complete, execution deferred to camera-ready\\n  depends_on:\\n  - D030\\n- id: D032\\n  date: 2026-05-14 17:02 UTC\\n  summary: plan_015 缩减为 1 seed × dynamic_ep (~11h)；BM25 overlap 87% 需分层验证\\n  rationale: 'plan_015 原设计 3 variants × 多 seeds = 44h，DDL May 25 前 GPU 时间不够。缩减为 dynamic_ep\\n    × 1 seed (Qwen s42) ~11h，足以排除 static vs dynamic confound。预期 dynamic ≈ static（<1pp），在\\n    Limitation 段写实验证据。\\n\\n\\n    BM25 Phase 1 完成：BM25 vs embedding overlap 87.1%。但 Agent 指出小 repo (pool ≤50) 导致所有策略\\n    negatives 重合——overlap 被拉高。已派补充分析按 repo 大小分层统计真实差异化程度。Phase 2 训练结果将决定 CoCoHaNeRe\\n    narrative 是否需要 pivot（contingency 已在 paper_framing.md）。'\\n  related_experiments:\\n  - exp_id: plan_015\\n    role: scope_reduction\\n    result: 44h→11h, 1 seed × dynamic_ep only\\n  - exp_id: plan_018\\n    role: phase1_complete\\n    result: BM25 vs embedding overlap 87.1%, 3 seeds done\\n  depends_on:\\n  - D030\\n\", \"total_chars\": 25601, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0388419c-15a3-4282-9cc5-88f8e2ffa7c2",
  "isSidechain": true,
  "promptId": "a8e5f13c-b79e-4d5f-9dcc-e79744f9ec80",
  "agentId": "a4ff2b13031f226a3",
  "type": "user",
  "uuid": "9f1c3c16-4abf-46c3-a106-451dc4ec8061",
  "sourceToolAssistantUUID": "0388419c-15a3-4282-9cc5-88f8e2ffa7c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T17:08:18.182Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YCZ11rHAhzT2WSvGUx1y65`</summary>

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
  "parentUuid": "9f1c3c16-4abf-46c3-a106-451dc4ec8061",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q3b7yg8G1vsAAUpYAo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0a9b1fc-7f6d-4b9e-9623-a02d788c25f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hs8rUGh8BuQcer2cwEWoER",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4973,
      "cache_read_input_tokens": 17727,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4973
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 287,
          "cache_read_input_tokens": 17727,
          "cache_creation_input_tokens": 4973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4973,
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

_source line 18 · 2026-05-14T17:08:18.214Z_

<details><summary>↩ Tool result · `toolu_01YCZ11rHAhzT2WSvGUx1y65`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-12\\n# 说明: 只收录项目文件中已引用的 + 确定存在的知名论文。不确定的信息标注\\\"需验证\\\"。\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline  # StructFuse 的评估基准\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Karthik Narasimhan, Ofir Press\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: building-block  # StructFuse 用其 repo 做数据提取\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n        note: \\\"需验证 venue（可能已投稿会议）\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务，StructFuse 可用于评估。\\\"\\n        note: \\\"需验证年份和 venue\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及代码领域的对比学习\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oğuz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式，是 StructFuse 对比训练的方法论基础。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，是 StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"SimCLR: A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Mining Hard Negatives with Curriculum for Dense Retrieval\\\"\\n        authors: \\\"需验证\\\"\\n        venue: \\\"需验证\\\"\\n        year: \\\"需验证\\\"\\n        relation: background\\n        summary: \\\"课程学习式 hard negative 挖掘，从易到难训练检索器。\\\"\\n        note: \\\"需验证完整信息\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block  # StructFuse 核心组件\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n        note: \\\"需验证作者和 venue\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: EMNLP (Findings)\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: background\\n        summary: \\\"大规模开源代码 LLM，广泛用于代码嵌入的 backbone。\\\"\\n        note: \\\"需验证 venue（可能是 arXiv 或其他）\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Qwen Team (Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block  # StructFuse 用 Qwen2.5-Coder-3B 做检索器\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n        note: \\\"需验证确切标题和年份\\\"\\n\\n      - title: \\\"Contrastive Learning for Source Code with Structural and Functional Properties\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: ACL (Findings)\\n        year: 2022\\n        relation: background\\n        summary: \\\"代码对比学习中利用结构/功能属性构建正负样本对。\\\"\\n        note: \\\"需验证作者和 venue\\\"\\n\\n      - title: \\\"BM25\\\"\\n        authors: \\\"Stephen Robertson, Hugo Zaragoza\\\"\\n        venue: \\\"Foundations and Trends in Information Retrieval\\\"\\n        year: 2009\\n        relation: baseline\\n        summary: \\\"经典稀疏检索方法，StructFuse 的 baseline 之一。Phase 2a 实验发现 BM25 在 bug fixing 定位中可能有误导性（负系数）。\\\"\\n\\n# ==========================================================================\\n# 待补充\\n# ==========================================================================\\n# 以下论文可能相关，待确认后补充：\\n# - FAISS (Johnson et al., 2019) — ANN 检索库，StructFuse 评估可能用到\\n# - Tree-sitter — 增量解析器，与 CodeQL 互补\\n# - Aider / Moatless Tools — SWE-bench 上的其他代码检索方法\\n# - CoSQA (Huang et al., 2021) — 代码搜索 QA 数据集\\n# - DeepSeek-Coder — 另一个可能的 backbone 对比\\n\", \"total_chars\": 9647, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0a9b1fc-7f6d-4b9e-9623-a02d788c25f8",
  "isSidechain": true,
  "promptId": "a8e5f13c-b79e-4d5f-9dcc-e79744f9ec80",
  "agentId": "a4ff2b13031f226a3",
  "type": "user",
  "uuid": "22e45e60-4323-40a2-863b-6bfb8de189c1",
  "sourceToolAssistantUUID": "e0a9b1fc-7f6d-4b9e-9623-a02d788c25f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-14T17:08:21.755Z_

Now let me look at the artifacts directory and any existing draft paper or review materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22e45e60-4323-40a2-863b-6bfb8de189c1",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q3z4MwaPegG5W691cJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e1d8b8b-1781-4428-b6d7-040ae282bd25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7ac85VfvAnakbeNruimTy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18447,
      "cache_read_input_tokens": 22700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18447,
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

_source line 20 · 2026-05-14T17:08:23.631Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Pn2QYmVqvQ2q6eXqLsR8cY`</summary>

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
  "parentUuid": "7e1d8b8b-1781-4428-b6d7-040ae282bd25",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q3z4MwaPegG5W691cJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e40f85d6-f68e-4a63-9810-ca53fa228ff4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7ac85VfvAnakbeNruimTy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18447,
      "cache_read_input_tokens": 22700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18447,
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

_source line 21 · 2026-05-14T17:08:23.652Z_

<details><summary>↩ Tool result · `toolu_01Pn2QYmVqvQ2q6eXqLsR8cY`</summary>

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
  "parentUuid": "e40f85d6-f68e-4a63-9810-ca53fa228ff4",
  "isSidechain": true,
  "promptId": "a8e5f13c-b79e-4d5f-9dcc-e79744f9ec80",
  "agentId": "a4ff2b13031f226a3",
  "type": "user",
  "uuid": "f320225b-59fa-45fd-b92b-fc6396abef57",
  "sourceToolAssistantUUID": "e40f85d6-f68e-4a63-9810-ca53fa228ff4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T17:08:24.565Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01WJ1LYBjxDV8KK7pG62oYVD`</summary>

```json
{
  "pattern": "**/dream_reports/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f320225b-59fa-45fd-b92b-fc6396abef57",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q3z4MwaPegG5W691cJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e5386e1-5210-40b6-9418-ca3e227e99a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7ac85VfvAnakbeNruimTy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18447,
      "cache_read_input_tokens": 22700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18447,
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

_source line 23 · 2026-05-14T17:08:24.579Z_

<details><summary>↩ Tool result · `toolu_01WJ1LYBjxDV8KK7pG62oYVD`</summary>

```text
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
artifacts/dream_reports/dream_20260512T204322/meta.yaml
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
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e5386e1-5210-40b6-9418-ca3e227e99a6",
  "isSidechain": true,
  "promptId": "a8e5f13c-b79e-4d5f-9dcc-e79744f9ec80",
  "agentId": "a4ff2b13031f226a3",
  "type": "user",
  "uuid": "5d7c6992-62e3-413b-88fc-56de493ca55c",
  "sourceToolAssistantUUID": "5e5386e1-5210-40b6-9418-ca3e227e99a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T17:08:25.257Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CptnTd3YbBWK2S6y8HKwqc`</summary>

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
  "parentUuid": "5d7c6992-62e3-413b-88fc-56de493ca55c",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q3z4MwaPegG5W691cJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58114317-ade4-42fd-8cf7-5a3543fd02c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7ac85VfvAnakbeNruimTy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18447,
      "cache_read_input_tokens": 22700,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18447
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 22700,
          "cache_creation_input_tokens": 18447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18447,
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

_source line 25 · 2026-05-14T17:08:25.267Z_

<details><summary>↩ Tool result · `toolu_01CptnTd3YbBWK2S6y8HKwqc`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58114317-ade4-42fd-8cf7-5a3543fd02c4",
  "isSidechain": true,
  "promptId": "a8e5f13c-b79e-4d5f-9dcc-e79744f9ec80",
  "agentId": "a4ff2b13031f226a3",
  "type": "user",
  "uuid": "18c2a66f-c6cd-451b-82af-1297c4d7bea5",
  "sourceToolAssistantUUID": "58114317-ade4-42fd-8cf7-5a3543fd02c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-14T17:08:28.517Z_

Let me read the latest dream paper (best tier) and its review context to understand the full paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18c2a66f-c6cd-451b-82af-1297c4d7bea5",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q4WAMbJ38xBEqbAvco",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6eb42cf7-ba5c-43d1-adb2-66cc9badee40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Py1Z3wbNC5jfDEEMvvk1ww",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2915,
      "cache_read_input_tokens": 41147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2915,
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

_source line 27 · 2026-05-14T17:08:30.111Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CCjpXJTHhwJrTi5YLE5VVc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6eb42cf7-ba5c-43d1-adb2-66cc9badee40",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q4WAMbJ38xBEqbAvco",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1399a5e-ed4e-4ccd-a1e9-52fb4fcce8e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Py1Z3wbNC5jfDEEMvvk1ww",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2915,
      "cache_read_input_tokens": 41147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2915,
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

_source line 28 · 2026-05-14T17:08:30.373Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SbgyW1qHrNSeTVYpZcyRWL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1399a5e-ed4e-4ccd-a1e9-52fb4fcce8e0",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q4WAMbJ38xBEqbAvco",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d7b087c-5c26-4000-81d6-ccf3791eda8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Py1Z3wbNC5jfDEEMvvk1ww",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2915,
      "cache_read_input_tokens": 41147,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2915
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 41147,
          "cache_creation_input_tokens": 2915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2915,
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

_source line 29 · 2026-05-14T17:08:30.475Z_

<details><summary>↩ Tool result · `toolu_01CCjpXJTHhwJrTi5YLE5VVc`</summary>

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
201	StarCoder & BM25 & 43.3 & [42.3, 44.3] & $-$2.7 \\
202	StarCoder & random & 46.0 & [45.1, 46.9] & --- \\
203	StarCoder & dataflow & 45.8 & [44.8, 46.8] & $-$0.2 \\
204	StarCoder & embedding & 47.5 & [46.6, 48.4] & +1.5 \\
205	\bottomrule
206	\end{tabular}
207	\end{table}
208	
209	BM25 negatives harm performance for both encoders ($-$2.5pp Qwen, $-$2.7pp StarCoder vs random).
210	BM25 selects lexically similar files that share function names, variable names, and import patterns with the query.
211	These are precisely the signals that contrastive learning should leverage for discrimination; training the encoder to ignore them degrades retrieval.
212	
213	True embedding-distance mining improves both encoders (+2.0pp Qwen, +1.5pp StarCoder), selecting files that are semantically similar in the pretrained embedding space but not relevant to the query.
214	This forces the encoder to learn finer-grained semantic distinctions.
215	
216	Dataflow negatives benefit Qwen (+1.0pp, CI lower bound $>$ 0) but not StarCoder ($-$0.2pp, CI includes zero).
217	Section~\ref{sec:stratified} provides mechanistic explanation for this interaction.
218	
219	%------------------------------------------------------------------------------
220	\subsection{SWE-bench Lite End-to-End Evaluation}
221	\label{sec:swebench}
222	%------------------------------------------------------------------------------
223	
224	\begin{table}[h]
225	\centering
226	\caption{SWE-bench Lite resolve rate (300 instances, Qwen3.6-27B agent, top-5 retrieval).}
227	\label{tab:swebench}
228	\begin{tabular}{lcccc}
229	\toprule
230	\textbf{Strategy} & \textbf{Resolved} & \textbf{Total} & \textbf{Rate (\%)} & \textbf{$\Delta$ vs Random (pp)} \\
231	\midrule
232	random & 66 & 300 & 22.0 & --- \\
233	embedding & 73 & 300 & 24.3 & +2.3 \\
234	dataflow & 76 & 300 & 25.3 & +3.3 \\
235	\bottomrule
236	\end{tabular}
237	\end{table}
238	
239	Retrieval quality improvements amplify at the downstream task level.
240	Embedding mining yields +2.5pp resolve rate ($p = 0.018$, 95\% CI [+0.7, +4.3]), and dataflow yields +3.2pp ($p = 0.008$, CI [+1.0, +5.5]) over random (Table~\ref{tab:swebench_bootstrap}).
241	The difference between dataflow and embedding is +0.7pp but not significant ($p = 0.134$, CI [$-$1.5, +2.9]).
242	
243	\begin{table}[h]
244	\centering
245	\caption{Bootstrap significance tests for SWE-bench Lite (10K resamples).}
246	\label{tab:swebench_bootstrap}
247	\begin{tabular}{lccc}
248	\toprule
249	\textbf{Comparison} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} & \textbf{$p$-value} \\
250	\midrule
251	embedding $-$ random & +2.5 & [+0.7, +4.3] & 0.018 \\
252	dataflow $-$ random & +3.2 & [+1.0, +5.5] & 0.008 \\
253	dataflow $-$ embedding & +0.7 & [$-$1.5, +2.9] & 0.134 \\
254	\bottomrule
255	\end{tabular}
256	\end{table}
257	
258	\paragraph{Breakdown by Patch Complexity.}
259	Multi-file patches (37\% of instances) are the primary source of dataflow advantage: dataflow achieves +5.4pp over random on multi-file patches (17.1\% vs 11.7\%) compared to +2.2pp on single-file patches (30.2\% vs 28.0\%).
260	This is consistent with the mechanism: dataflow negatives train the retriever to understand cross-module dependencies, which matters most when the gold patch spans multiple files.
261	
262	\begin{table}[h]
263	\centering
264	\caption{SWE-bench resolve rate by patch complexity.}
265	\label{tab:swebench_complexity}
266	\begin{tabular}{lcccc}
267	\toprule
268	\textbf{Patch Type} & \textbf{N} & \textbf{random (\%)} & \textbf{embedding (\%)} & \textbf{dataflow (\%)} \\
269	\midrule
270	single-file & 189 & 28.0 & 30.7 & 30.2 \\
271	multi-file & 111 & 11.7 & 14.4 & 17.1 \\
272	\bottomrule
273	\end{tabular}
274	\end{table}
275	
276	%------------------------------------------------------------------------------
277	\subsection{RepoBench-R Cross-File Retrieval}
278	\label{sec:repobench}
279	%------------------------------------------------------------------------------
280	
281	Table~\ref{tab:repobench} shows results on RepoBench-R test\_hard (pool $\approx$ 18).
282	Embedding mining significantly improves R@1 for both encoders (+2.1pp Qwen, +1.5pp StarCoder), confirming cross-benchmark generalization.
283	Dataflow provides +1.2pp for Qwen (CI marginally excludes zero) but is ineffective for StarCoder ($-$0.2pp, CI includes zero)---the same encoder-strategy interaction observed on SWE-smith.
284	
285	\begin{table}[h]
286	\centering
287	\caption{RepoBench-R test\_hard results (pool $\approx$ 18, 9-seed mean $\pm$ 95\% CI).}
288	\label{tab:repobench}
289	\begin{tabular}{llccc}
290	\toprule
291	\textbf{Encoder} & \textbf{Strategy} & \textbf{R@1 (\%)} & \textbf{95\% CI} & \textbf{$\Delta$ vs Random (pp)} \\
292	\midrule
293	Qwen & random & 62.1 & [61.4, 62.8] & --- \\
294	Qwen & embedding & 64.2 & [63.4, 65.0] & +2.1 \\
295	Qwen & dataflow & 63.3 & [62.4, 64.2] & +1.2 \\
296	\midrule
297	StarCoder & random & 57.4 & [56.6, 58.2] & --- \\
298	StarCoder & embedding & 58.9 & [58.0, 59.8] & +1.5 \\
299	StarCoder & dataflow & 57.2 & [56.2, 58.2] & $-$0.2 \\
300	\bottomrule
301	\end{tabular}
302	\end{table}
303	
304	On test\_easy (pool $\approx$ 6), deltas are compressed due to ceiling effects: Qwen embedding +1.2pp (84.3\% $\to$ 85.5\%), StarCoder embedding +1.0pp (81.2\% $\to$ 82.2\%).
305	This is expected---smaller pools leave fewer distractors for mining quality to differentiate.
306	
307	%------------------------------------------------------------------------------
308	\subsection{Stratified Analysis}
309	\label{sec:stratified}
310	%------------------------------------------------------------------------------
311	
312	\paragraph{Structural Data Availability.}
313	Table~\ref{tab:stratified_structural} decomposes dataflow performance by whether structural data was available for each instance.
314	On the 34\% of instances with dataflow connectivity, the dataflow advantage is +2.8pp (Qwen)---substantially larger than the pooled +1.0pp.
315	On the 66\% fallback stratum where dataflow degrades to embedding or random selection, the advantage is +0.1pp (effectively zero).
316	This decomposition directly addresses the concern that 34\% coverage dilutes the signal: the true per-instance effect is +2.8pp, not +1.0pp.
317	
318	\begin{table}[h]
319	\centering
320	\caption{Stratified R@1 delta by structural data availability (Qwen encoder).}
321	\label{tab:stratified_structural}
322	\begin{tabular}{lccccc}
323	\toprule
324	\textbf{Stratum} & \textbf{N} & \textbf{random} & \textbf{embedding} & \textbf{dataflow} & \textbf{df$-$rand (pp)} \\
325	\midrule
326	With dataflow (34\%) & $\sim$5.2K & 53.1 & 55.4 & 55.9 & +2.8 \\
327	Fallback (66\%) & $\sim$10K & 55.2 & 57.3 & 55.3 & +0.1 \\
328	\midrule
329	Overall & $\sim$15.2K & 54.5 & 56.5 & 55.5 & +1.0 \\
330	\bottomrule
331	\end{tabular}
332	\end{table}
333	
334	\paragraph{Negative Difficulty Quartiles.}
335	Table~\ref{tab:neg_difficulty} presents the strongest mechanistic evidence.
336	We partition instances by negative difficulty (margin between positive and hardest negative similarity).
337	The benefit of mining strategies scales monotonically with difficulty: Q4 (hardest, margin 0.008) shows +3.2pp embedding delta, while Q1 (easiest, margin 0.142) shows only +0.8pp.
338	This confirms the representation saturation hypothesis: when random negatives are already easy to distinguish (large margin), better mining adds little; when the margin is thin, mining quality is critical.
339	
340	\begin{table}[h]
341	\centering
342	\caption{R@1 delta by negative difficulty quartile (Qwen encoder).}
343	\label{tab:neg_difficulty}
344	\begin{tabular}{lccc}
345	\toprule
346	\textbf{Quartile} & \textbf{Margin (mean)} & \textbf{emb$-$rand (pp)} & \textbf{df$-$rand (pp)} \\
347	\midrule
348	Q1 (easiest) & 0.142 & +0.8 & +0.3 \\
349	Q2 & 0.078 & +1.5 & +0.7 \\
350	Q3 & 0.031 & +2.4 & +1.2 \\
351	Q4 (hardest) & 0.008 & +3.2 & +2.1 \\
352	\bottomrule
353	\end{tabular}
354	\end{table}
355	
356	\paragraph{Repo Size and Pool Size Strata.}
357	Embedding delta is inversely related to repository size: small repos ($<$50 files) show +2.8pp, while extra-large repos ($>$500 files) show +1.6pp.
358	Pool size strata show a complementary pattern: embedding delta increases from +1.0pp (pool $<$ 20) to +2.5pp (pool $>$ 50), as larger pools provide more distractors where mining quality matters.
359	
360	\paragraph{Query--Positive Similarity.}
361	When query-positive similarity is high ($>$0.95), embedding delta is largest (+2.6pp) and dataflow delta is also substantial (+1.8pp).
362	At low similarity ($<$0.85), both deltas shrink (+1.2pp embedding, +0.2pp dataflow).
363	High-similarity instances are precisely those where the retriever struggles to separate the positive from near-duplicates, making negative quality most impactful.
364	
365	%------------------------------------------------------------------------------
366	\subsection{Ablation Studies}
367	\label{sec:ablations}
368	%------------------------------------------------------------------------------
369	
370	\subsubsection{Temperature Ablation}
371	\label{sec:temp_ablation}
372	
373	\begin{table}[h]
374	\centering
375	\caption{Temperature ablation (R@1 \%). Strategy rankings are preserved across all three temperatures.}
376	\label{tab:temperature}
377	\begin{tabular}{clcccc}
378	\toprule
379	$\tau$ & \textbf{Encoder} & \textbf{random} & \textbf{embedding} & \textbf{dataflow} & \textbf{emb$-$rand (pp)} \\
380	\midrule
381	0.05 & Qwen & 55.8 & 57.7 & 56.9 & +1.9 \\
382	0.05 & StarCoder & 47.0 & 48.5 & 46.7 & +1.5 \\
383	0.10 & Qwen & 54.5 & 56.5 & 55.5 & +2.0 \\
384	0.10 & StarCoder & 46.0 & 47.5 & 45.8 & +1.5 \\
385	0.20 & Qwen & 53.0 & 54.6 & 53.8 & +1.6 \\
386	0.20 & StarCoder & 44.8 & 46.1 & 44.7 & +1.3 \\
387	\bottomrule
388	\end{tabular}
389	\end{table}
390	
391	Strategy rankings (embedding $>$ dataflow $>$ random for Qwen; embedding $>$ random $\approx$ dataflow for StarCoder) are preserved across all three temperatures (Table~\ref{tab:temperature}).
392	$\tau = 0.05$ achieves the highest absolute performance due to sharper gradient signals.
393	$\tau = 0.20$ compresses deltas (1.6pp vs 2.0pp) but does not reverse rankings, confirming findings are not temperature-regime-specific.
394	We use $\tau = 0.1$ as the default, following literature convention.
395	
396	\subsubsection{Call-Graph Hop Depth Ablation}
397	\label{sec:hop_ablation}
398	
399	\begin{table}[h]
400	\centering
401	\caption{Hop depth ablation for dataflow negatives (Qwen encoder).}
402	\label{tab:hop_depth}
403	\begin{tabular}{ccccc}
404	\toprule
405	\textbf{Hops} & \textbf{Coverage (\%)} & \textbf{Neg/query} & \textbf{R@1 (\%)} & \textbf{$\Delta$ vs 2-hop (pp)} \\
406	\midrule
407	1 & 12.4 & 18.2 & 54.8 & $-$0.7 \\
408	2 & 34.3 & 31.7 & 55.5 & --- \\
409	3 & 58.6 & 42.1 & 55.1 & $-$0.4 \\
410	\bottomrule
411	\end{tabular}
412	\end{table}
413	
414	2-hop call-graph bounding is optimal (Table~\ref{tab:hop_depth}).
415	1-hop is too conservative: only 12.4\% coverage means most instances lack sufficient connected nodes to define meaningful ``disconnected'' negatives.
416	3-hop is too permissive: 58.6\% coverage narrows the disconnected set excessively, excluding structurally related files that would serve as good negatives.
417	2-hop captures direct callers/callees and their immediate neighbors, providing a principled boundary at 34.3\% coverage.
418	
419	\subsubsection{Training Data Size Scaling}
420	\label{sec:data_scaling}
421	
422	\begin{table}[h]
423	\centering
424	\caption{Data size scaling (Qwen encoder). Strategy rankings and monotonic improvement are stable across scales.}
425	\label{tab:data_scaling}
426	\begin{tabular}{lcccccc}
427	\toprule
428	\textbf{Size} & \textbf{random} & \textbf{embedding} & \textbf{dataflow} & \textbf{emb$-$rand (pp)} & $\sigma$ \textbf{seeds} \\
429	\midrule
430	1K & 51.0 & 52.2 & 51.5 & +1.2 & 1.5 \\
431	3K & 53.2 & 55.0 & 54.1 & +1.8 & 1.0 \\
432	5K & 54.5 & 56.5 & 55.5 & +2.0 & 0.8 \\
433	\bottomrule
434	\end{tabular}
435	\end{table}
436	
437	Strategy ranking (embedding $>$ dataflow $>$ random) is preserved across 1K, 3K, and 5K training instances (Table~\ref{tab:data_scaling}).
438	The embedding--random delta grows from +1.2pp at 1K to +2.0pp at 5K, with no sign of diminishing returns.
439	Seed variance decreases from $\sigma = 1.5$ at 1K to $\sigma = 0.8$ at 5K as larger datasets reduce sampling noise.
440	
441	\subsubsection{Fusion Head Ablation}
442	\label{sec:fusion_ablation}
443	
444	\begin{table}[h]
445	\centering
446	\caption{Fusion head ablation: training-time mining vs inference-time feature injection.}
447	\label{tab:fusion}
448	\begin{tabular}{lcc}
449	\toprule
450	\textbf{Configuration} & \textbf{Qwen R@1 (\%)} & \textbf{StarCoder R@1 (\%)} \\
451	\midrule
452	embedding-only (ours) & 56.5 & 47.5 \\
453	structural-features-only & 49.8 & 42.1 \\
454	combined fusion & 56.1 & 47.2 \\
455	\bottomrule
456	\end{tabular}
457	\end{table}
458	
459	Table~\ref{tab:fusion} isolates the value of training-time mining versus inference-time structural feature injection.
460	Embedding-only (our approach: mine negatives during training, no structural features at inference) performs best or ties with combined fusion.
461	Structural-features-only (no mining, inject CodeQL connectivity features at inference) is far worse ($-$6.7pp Qwen).
462	Combined fusion slightly underperforms embedding-only ($-$0.4pp) because inference-time structural features introduce noise from the 66\% of instances without CodeQL coverage.
463	The core value of StructFuse is in the \emph{mining strategy}, not in feature engineering.
464	
465	\subsubsection{Pool Size Sensitivity}
466	\label{sec:pool_sensitivity}
467	
468	\begin{table}[h]
469	\centering
470	\caption{Pool size sensitivity (R@1 \%). Strategy rankings are 100\% stable across pool sizes spanning an order of magnitude.}
471	\label{tab:pool_size}
472	\begin{tabular}{clccccc}
473	\toprule
474	\textbf{Pool} & \textbf{Encoder} & \textbf{random} & \textbf{embedding} & \textbf{dataflow} & \textbf{emb$-$rand (pp)} & \textbf{Ranking} \\
475	\midrule
476	50 & Qwen & 54.5 & 56.5 & 55.5 & +2.0 & E$>$D$>$R \\
477	100 & Qwen & 42.8 & 44.7 & 43.8 & +1.9 & E$>$D$>$R \\
478	200 & Qwen & 34.2 & 35.9 & 35.1 & +1.7 & E$>$D$>$R \\
479	500 & Qwen & 26.1 & 27.6 & 26.9 & +1.5 & E$>$D$>$R \\
480	\midrule
481	50 & StarCoder & 46.0 & 47.5 & 45.8 & +1.5 & E$>$R$>$D \\
482	100 & StarCoder & 35.8 & 37.2 & 35.7 & +1.4 & E$>$R$>$D \\
483	200 & StarCoder & 28.2 & 29.5 & 28.1 & +1.3 & E$>$R$\approx$D \\
484	500 & StarCoder & 21.4 & 22.5 & 21.3 & +1.1 & E$>$R$\approx$D \\
485	\bottomrule
486	\end{tabular}
487	\end{table}
488	
489	Strategy rankings are 100\% stable across pool sizes from 50 to 500 (Table~\ref{tab:pool_size}).
490	Absolute R@1 drops as expected with larger pools, and the embedding--random delta degrades gracefully from 2.0pp to 1.5pp (Qwen) and 1.5pp to 1.1pp (StarCoder) at approximately $-$0.15pp per pool-size doubling.
491	The delta does not collapse, confirming the mining strategy's value is not an artifact of small pool sizes.
492	
493	\subsubsection{Dynamic vs Static Embedding Mining}
494	\label{sec:dynamic_mining}
495	
496	\begin{table}[h]
497	\centering
498	\caption{Static vs dynamic embedding mining. Static mining (one-time, from pretrained) is sufficient.}
499	\label{tab:dynamic}
500	\begin{tabular}{lcccc}
501	\toprule
502	\textbf{Encoder} & \textbf{Static R@1 (\%)} & \textbf{Dynamic R@1 (\%)} & \textbf{$\Delta$ (pp)} & $p$\textbf{-value} \\
503	\midrule
504	Qwen & 56.5 & 56.8 & +0.3 & 0.41 \\
505	StarCoder & 47.5 & 47.7 & +0.2 & 0.53 \\
506	\bottomrule
507	\end{tabular}
508	\end{table}
509	
510	Dynamic mining (re-computing negatives each epoch using the current encoder) provides negligible improvement over static mining (+0.3pp Qwen, +0.2pp StarCoder, both non-significant; Table~\ref{tab:dynamic}).
511	LoRA rank-16 fine-tuning changes the embedding space only slightly, so pretrained nearest neighbors remain valid throughout training.
512	This rules out the curriculum-effect confound and simplifies the practical recommendation: mine once from the pretrained checkpoint.
513	
514	\subsubsection{Weighted vs Binary Dataflow Negatives}
515	\label{sec:weighted}
516	
517	\begin{table}[h]
518	\centering
519	\caption{Weighted (by hop distance) vs binary dataflow negatives. Binary is sufficient.}
520	\label{tab:weighted}
521	\begin{tabular}{lccc}
522	\toprule
523	\textbf{Method} & \textbf{Qwen R@1 (\%)} & \textbf{StarCoder R@1 (\%)} & \textbf{$\Delta$ vs Binary (pp)} \\
524	\midrule
525	Binary (default) & 55.5 & 45.8 & --- \\
526	Distance-weighted & 55.8 & 45.9 & +0.3 / +0.1 \\
527	\bottomrule
528	\end{tabular}
529	\end{table}
530	
531	Weighting dataflow negatives by hop distance (farther = higher sampling probability) provides no significant improvement over binary connected/disconnected classification (+0.3pp Qwen, +0.1pp StarCoder; Table~\ref{tab:weighted}).
532	The binary signal---``on the call chain or not''---captures the essential structural distinction.
533	Further distance-based refinement adds complexity without benefit.
534	
535	%------------------------------------------------------------------------------
536	\subsection{Failure Analysis}
537	\label{sec:failure}
538	%------------------------------------------------------------------------------
539	
540	We manually analyzed 50 failure cases from the random retriever on SWE-bench Lite (Table~\ref{tab:failure}).
541	44\% (22/50) are retrieval failures (wrong files retrieved), of which 64\% (14/22) involve cross-module dependencies where the gold file is a caller/callee of a retrieved-but-wrong file.
542	These are precisely the cases dataflow training targets.
543	30\% (15/50) are retrieval successes where the agent fails to generate correct patches, establishing a ceiling: even with perfect retrieval, $\sim$85\% is the maximum achievable resolve rate given agent limitations.
544	
545	\begin{table}[h]
546	\centering
547	\caption{Failure category breakdown (50 random-retriever failures from SWE-bench Lite).}
548	\label{tab:failure}
549	\begin{tabular}{lccc}
550	\toprule
551	\textbf{Category} & \textbf{Count} & \textbf{\% of 50} & \textbf{Dataflow Could Help?} \\
552	\midrule
553	Retrieval: wrong files & 22 & 44\% & 14/22 (64\%) \\
554	Retrieval OK, agent fail & 15 & 30\% & N/A \\
555	Context window limit & 7 & 14\% & 5/7 partially \\
556	Test env issue & 4 & 8\% & No \\
557	Ambiguous issue & 2 & 4\% & No \\
558	\bottomrule
559	\end{tabular}
560	\end{table}
561	
562	\paragraph{Illustrative Example.}
563	Consider a Django issue about \texttt{QuerySet.filter()} returning wrong results with nested Q objects.
564	The random retriever ranks \texttt{django/db/models/query.py} first (text match on ``filter''), but the bug resides in \texttt{django/db/models/sql/query.py} (the downstream SQL builder invoked by \texttt{filter}).
565	The dataflow-trained retriever correctly ranks the SQL builder file higher, having learned that structurally connected files along the call chain are more likely to co-occur in patches.
566	
567	%==============================================================================
568	\section{Discussion}
569	\label{sec:discussion}
570	%==============================================================================
571	
572	\paragraph{Why Does the Encoder--Strategy Interaction Exist?}
573	Qwen2.5-Coder-3B exhibits representation saturation (mean pos\_sim = 0.9855), compressing positive and negative embeddings into a narrow similarity band.
574	Random negatives are trivially separable and provide weak gradient signal.
575	Embedding mining selects negatives that are genuinely close in this compressed space, providing the difficulty gradient the encoder needs.
576	Dataflow negatives add an orthogonal structural dimension that further assists discrimination.
577	
578	StarCoder2-3B has healthier separation (mean pos\_sim = 0.7985).
579	Random negatives already provide moderate difficulty, and embedding mining further refines the boundary.
580	Dataflow negatives offer no additional benefit because the embedding space is not saturated---the encoder can already separate structural from textual similarity using learned features alone.
581	
582	\paragraph{Relationship to Inference-Time Graph Methods.}
583	StructFuse operates at training time, distilling structural knowledge into encoder representations via negative mining.
584	Inference-time graph methods (CodexGraph, LocAgent, RANGER, ARISE, and others; Table~\ref{tab:lit_comparison}) navigate or re-rank over code graphs at inference time.
585	The two approaches are complementary: StructFuse produces a better base retriever that graph-based methods can navigate over.
586	We do not claim superiority over these methods, as they solve different problems and operate under different computational budgets.
587	
588	\begin{table}[h]
589	\centering
590	\caption{Comparison with inference-time graph methods. StructFuse is the only method that leverages structural signal at training time without inference-time overhead.}
591	\label{tab:lit_comparison}
592	\begin{tabular}{llll}
593	\toprule
594	\textbf{Method} & \textbf{Graph Stage} & \textbf{Graph Type} & \textbf{Complementary?} \\
595	\midrule
596	StructFuse (ours) & Training & Dataflow (CodeQL) & --- \\
597	CodexGraph & Inference & Code graph DB & Yes \\
598	LocAgent & Inference & Repo structure & Yes \\
599	RANGER & Inference & Call graph & Yes \\
600	ARISE & Inference & Intra-proc dataflow & Partially \\
601	\bottomrule
602	\end{tabular}
603	\end{table}
604	
605	\paragraph{Practical Recommendations.}
606	Based on our findings: (1) Always use true embedding-distance mining over random negatives---the improvement is consistent across encoders, benchmarks, temperatures, pool sizes, and data scales. (2) Never use BM25 negatives for code retrieval contrastive training. (3) Consider dataflow negatives when encoder representations are saturated (check pos\_sim distribution); static mining suffices. (4) Binary structural signal is sufficient; weighted variants add complexity without benefit.
607	
608	\paragraph{Limitations.}
609	Our study is limited to two 3B-parameter decoder-only code encoders; generalization to encoder-only architectures (e.g., CodeBERT) and larger models remains to be verified.
610	CodeQL structural extraction achieves 34\% coverage, limiting the effective reach of dataflow negatives.
611	SWE-bench Lite evaluation uses 300 instances with a single agent model, providing limited statistical power for pairwise comparisons between mining strategies.
612	
613	%==============================================================================
614	\section{Conclusion}
615	\label{sec:conclusion}
616	%==============================================================================
617	
618	We presented a systematic study of hard negative mining strategies for contrastive code retrieval.
619	Our controlled comparison of four strategies---BM25, random, dataflow, and embedding-distance---across two encoders, three benchmarks, and extensive ablations establishes three findings:
620	(1)~True embedding-distance mining consistently improves code retrieval, correcting the prior misconception that embedding negatives are harmful (the reported harm stems from BM25-proxy negatives).
621	(2)~Structure-grounded dataflow negatives provide conditional benefit when encoder representations are saturated, with the true per-instance effect (+2.8pp) masked by coverage-driven dilution in pooled results.
622	(3)~Negative difficulty quartile analysis provides mechanistic explanation: harder instances benefit more from better negatives (Q4: +3.2pp vs Q1: +0.8pp), linking mining strategy effectiveness to representation geometry.
623	
624	These findings transfer to downstream tasks (SWE-bench Lite: +2.5pp embedding, +3.2pp dataflow resolve rate) and are robust across temperatures, pool sizes, data scales, and a second benchmark (RepoBench-R).
625	Strategy rankings never reverse across any experimental condition tested.
626	
627	\bibliographystyle{plainnat}
628	
629	\end{document}
630	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1399a5e-ed4e-4ccd-a1e9-52fb4fcce8e0",
  "isSidechain": true,
  "promptId": "a8e5f13c-b79e-4d5f-9dcc-e79744f9ec80",
  "agentId": "a4ff2b13031f226a3",
  "type": "user",
  "uuid": "7f9bc187-7ca0-45ab-8167-10940419af43",
  "sourceToolAssistantUUID": "a1399a5e-ed4e-4ccd-a1e9-52fb4fcce8e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T17:08:30.656Z_

<details><summary>↩ Tool result · `toolu_01SbgyW1qHrNSeTVYpZcyRWL`</summary>

```text
1	narrative_guidance: '全 18 runs（9 seeds × 2 encoders × 3 strategies）完整复现 pilot pattern。
2	  Embedding mining 在两个 encoder 上均显著优于 random（Qwen +2.0pp, StarCoder +1.5pp, 95% CI
3	  下界 > 0）。 Dataflow 在 Qwen 上条件性获益（+1.0pp, CI 下界 > 0），StarCoder 上无显著差异（-0.2pp, CI 含零）。
4	  BM25 baseline 实证关闭 CoCoHaNeRe 论证（BM25 vs random: Qwen -2.5pp, StarCoder -2.7pp）。
5	  SWE-bench Lite downstream +2.5pp embedding, +3.2pp dataflow resolve rate delta。
6	  三条 claim 原样成立，EMNLP Main 强投 framing 无需调整。 M2 full anchors — Qwen random R@1=0.545,
7	  embedding=0.565, dataflow=0.555; StarCoder random R@1=0.460, embedding=0.475, dataflow=0.458。
8	
9	  '
10	imagined_experiments:
11	- name: SWE-bench Lite End-to-End Evaluation
12	  plan_id: plan_003
13	  description: '3 strategies × best Qwen checkpoint, Qwen3.6-27B agent, 300 SWE-bench
14	    Lite instances. Retriever 提供 top-k context files，agent 生成 patch，评估 resolve rate。
15	
16	    '
17	  expected_results:
18	    random_resolve_rate: 0.22
19	    random_resolved_count: 66
20	    embedding_resolve_rate: 0.245
21	    embedding_resolved_count: 73
22	    dataflow_resolve_rate: 0.252
23	    dataflow_resolved_count: 76
24	    embedding_minus_random_pp: 2.5
25	    dataflow_minus_random_pp: 3.2
26	    dataflow_minus_embedding_pp: 0.7
27	    total_instances: 300
28	    retriever_top_k: 5
29	    agent_model: Qwen3.6-27B
30	  result_rationale: 'Embedding retriever 在 SWE-bench 上提升 +2.5pp，因为 bug-fix patch 通常涉及与
31	    issue 描述 语义相似但非完全匹配的文件——embedding mining 训练使 retriever 更擅长区分"近似但无关" 与"近似且相关"的文件。Dataflow
32	    额外提升 +0.7pp（总 +3.2pp vs random）因为 SWE-bench patch 经常跨函数/跨模块（约 40% 涉及 caller-callee
33	    关系），dataflow negatives 训练使 retriever 理解"调用链上的文件更可能共同出现在 patch 中"。Delta 幅度从 retrieval
34	    R@1 的 +2.0/+1.0pp 放大到下游 resolve rate 的 +2.5/+3.2pp，符合检索质量在端到端任务中 的杠杆效应——正确检索一个关键文件可以使原本完全失败的
35	    patch 变为可解决。 效果幅度在 swebench_resolve_rate_delta_pp [1.5, 4.0] 范围内。
36	
37	    '
38	  tables:
39	  - name: 'Table 4: SWE-bench Lite Resolve Rate'
40	    columns:
41	    - Strategy
42	    - Resolved
43	    - Total
44	    - Rate (%)
45	    - Δ vs Random (pp)
46	    rows:
47	    - - random
48	      - 66
49	      - 300
50	      - 22.0
51	      - —
52	    - - embedding
53	      - 73
54	      - 300
55	      - 24.3
56	      - '+2.3'
57	    - - dataflow
58	      - 76
59	      - 300
60	      - 25.3
61	      - '+3.3'
62	  - name: 'Table 4b: SWE-bench by Patch Complexity'
63	    columns:
64	    - Patch Type
65	    - N
66	    - random (%)
67	    - embedding (%)
68	    - dataflow (%)
69	    rows:
70	    - - single-file
71	      - 189
72	      - 28.0
73	      - 30.7
74	      - 30.2
75	    - - multi-file
76	      - 111
77	      - 11.7
78	      - 14.4
79	      - 17.1
80	  figures_description:
81	  - 'Fig 5: SWE-bench resolve rate bar chart (3 strategies) with bootstrap 95% CI
82	    whiskers'
83	  - 'Fig 5b: Scatter plot — retrieval R@1 rank vs resolve rate per instance, colored
84	    by strategy'
85	  analysis: 'Multi-file patches（占 37%）是 dataflow 拉开差距的主要来源：dataflow 在 multi-file 上
86	    +5.4pp vs random，远大于 single-file 的 +2.2pp。这与 Claim 2 一致——dataflow negatives 使
87	    retriever 更好地理解跨模块依赖。Embedding vs random 在 multi-file 上也有 +2.7pp，说明更难的 negatives
88	    普遍有益。总体 resolve rate 22-25% 与 SweRank/SWE-Fixer 文献报告的 retriever-only baseline
89	    一致。
90	
91	    '
92	- name: RepoBench-R Cross-File Retrieval with Multi-Seed CIs
93	  plan_id: plan_004
94	  description: 'RepoBench-R test_easy (pool ~6) 和 test_hard (pool ~18) 上评估 9 seeds
95	    × 3 strategies × 2 encoders，报告 R@1 均值 + 95% bootstrap CI。
96	
97	    '
98	  expected_results:
99	    qwen_test_hard:
100	      random_R1_mean: 0.621
101	      random_R1_ci:
102	      - 0.614
103	      - 0.628
104	      embedding_R1_mean: 0.642
105	      embedding_R1_ci:
106	      - 0.634
107	      - 0.65
108	      dataflow_R1_mean: 0.633
109	      dataflow_R1_ci:
110	      - 0.624
111	      - 0.642
112	      embedding_minus_random_pp: 2.1
113	      dataflow_minus_random_pp: 1.2
114	    qwen_test_easy:
115	      random_R1_mean: 0.843
116	      embedding_R1_mean: 0.855
117	      dataflow_R1_mean: 0.85
118	      embedding_minus_random_pp: 1.2
119	    starcoder_test_hard:
120	      random_R1_mean: 0.574
121	      random_R1_ci:
122	      - 0.566
123	      - 0.582
124	      embedding_R1_mean: 0.589
125	      embedding_R1_ci:
126	      - 0.58
127	      - 0.598
128	      dataflow_R1_mean: 0.572
129	      dataflow_R1_ci:
130	      - 0.562
131	      - 0.582
132	      embedding_minus_random_pp: 1.5
133	      dataflow_minus_random_pp: -0.2
134	    starcoder_test_easy:
135	      random_R1_mean: 0.812
136	      embedding_R1_mean: 0.822
137	      dataflow_R1_mean: 0.81
138	    repobench_R1_delta_pp_embedding_avg: 1.8
139	    bootstrap_CI_width_R1_pp_avg: 1.2
140	  result_rationale: 'RepoBench-R 是 cross-file completion 任务，pool 更小（6-18），绝对 R@1 更高。
141	    Embedding mining 在两个 encoder 上均显著提升 test_hard R@1（Qwen +2.1pp, StarCoder +1.5pp），
142	    因为 pool=18 仍有足够 distractors 使 mining 质量差异体现。Test_easy pool=6 接近 ceiling，delta
143	    被压缩但方向一致。Dataflow 在 Qwen test_hard 上 +1.2pp 但 CI 刚好 排除零，StarCoder 上无效（-0.2pp，CI
144	    含零）——与 SWE-smith 上的 encoder-strategy interaction 完全一致，说明 pattern 跨 benchmark 稳定。CI
145	    宽度 ~1.2pp 在 bootstrap_CI_width_R1_pp [0.5, 2.0] 范围内，9 seeds 提供足够统计功效。
146	
147	    '
148	  tables:
149	  - name: 'Table 5: RepoBench-R Results (test_hard, pool≈18)'
150	    columns:
151	    - Encoder
152	    - Strategy
153	    - R@1 (%)
154	    - 95% CI
155	    - Δ vs Random (pp)
156	    rows:
157	    - - Qwen
158	      - random
159	      - 62.1
160	      - '[61.4, 62.8]'
161	      - —
162	    - - Qwen
163	      - embedding
164	      - 64.2
165	      - '[63.4, 65.0]'
166	      - '+2.1'
167	    - - Qwen
168	      - dataflow
169	      - 63.3
170	      - '[62.4, 64.2]'
171	      - '+1.2'
172	    - - StarCoder
173	      - random
174	      - 57.4
175	      - '[56.6, 58.2]'
176	      - —
177	    - - StarCoder
178	      - embedding
179	      - 58.9
180	      - '[58.0, 59.8]'
181	      - '+1.5'
182	    - - StarCoder
183	      - dataflow
184	      - 57.2
185	      - '[56.2, 58.2]'
186	      - −0.2
187	  figures_description:
188	  - 'Fig 6: RepoBench-R R@1 grouped bar chart (2 encoders × 3 strategies) with CI
189	    whiskers, test_easy vs test_hard side by side'
190	  analysis: 'Cross-benchmark 一致性是 best tier 的关键证据：embedding mining 在 SWE-smith 和 RepoBench-R
191	    上均显著提升两个 encoder，dataflow 条件性获益仅限 Qwen。这排除了 "结果仅限单一 benchmark" 的 reviewer concern。Test_easy
192	    上 delta 被压缩（pool=6 ceiling effect）是预期行为，反向验证了 pool size 对绝对效果幅度的调节作用。
193	
194	    '
195	- name: Stratified Analysis with Structural Coverage & Neg Difficulty Quartiles
196	  plan_id: plan_005
197	  description: '5 层分层分析：repo size / pool size / query-positive similarity / structural
198	    data availability (34% vs 66%) / neg_difficulty quartile。使用 M2 best checkpoints
199	    在 SWE-smith validation 上重新评估。
200	
201	    '
202	  expected_results:
203	    stratum_structural_available:
204	      with_dataflow_34pct:
205	        qwen_dataflow_minus_random_pp: 2.8
206	        qwen_dataflow_minus_embedding_pp: 1.3
207	        starcoder_dataflow_minus_random_pp: 0.1
208	        n_instances: ~5200
209	      fallback_66pct:
210	        qwen_dataflow_minus_random_pp: 0.1
211	        qwen_dataflow_minus_embedding_pp: -0.2
212	        starcoder_dataflow_minus_random_pp: -0.3
213	        n_instances: ~10000
214	    stratum_neg_difficulty_quartile:
215	      Q1_easiest:
216	        qwen_embedding_minus_random_pp: 0.8
217	        qwen_dataflow_minus_random_pp: 0.3
218	      Q2:
219	        qwen_embedding_minus_random_pp: 1.5
220	        qwen_dataflow_minus_random_pp: 0.7
221	      Q3:
222	        qwen_embedding_minus_random_pp: 2.4
223	        qwen_dataflow_minus_random_pp: 1.2
224	      Q4_hardest:
225	        qwen_embedding_minus_random_pp: 3.2
226	        qwen_dataflow_minus_random_pp: 2.1
227	    stratum_repo_size:
228	      small_lt50:
229	        embedding_delta_pp: 2.8
230	        n: ~500
231	      medium_50_200:
232	        embedding_delta_pp: 2.2
233	        n: ~4100
234	      large_200_500:
235	        embedding_delta_pp: 1.8
236	        n: ~5500
237	      xlarge_500plus:
238	        embedding_delta_pp: 1.6
239	        n: ~5100
240	    stratum_pool_size:
241	      pool_lt20:
242	        embedding_delta_pp: 1.0
243	        dataflow_delta_pp: 0.3
244	      pool_20_50:
245	        embedding_delta_pp: 2.1
246	        dataflow_delta_pp: 1.0
247	      pool_gt50:
248	        embedding_delta_pp: 2.5
249	        dataflow_delta_pp: 1.4
250	    stratum_query_pos_sim:
251	      high_sim_gt095:
252	        embedding_delta_pp: 2.6
253	        dataflow_delta_pp: 1.8
254	      medium_sim_085_095:
255	        embedding_delta_pp: 1.9
256	        dataflow_delta_pp: 0.8
257	      low_sim_lt085:
258	        embedding_delta_pp: 1.2
259	        dataflow_delta_pp: 0.2
260	  result_rationale: 'Structural-available stratum（34%）上 dataflow 优势放大到 +2.8pp（Qwen），因为这些
261	    instance 实际接收了 dataflow-disconnected negatives——真实训练信号未被 fallback 稀释。 Fallback
262	    stratum（66%）上 dataflow ≈ embedding（±0.2pp），因为 fallback 时 dataflow 策略退化为 embedding
263	    或 random 选择，无结构信号注入。这一分解直接回应 reviewer 关于 "34% coverage 稀释 signal" 的 concern——真实
264	    per-instance 效果是 +2.8pp 而非 pooled +1.0pp。Neg_difficulty Q4（最难 quartile）上 delta
265	    最大（embedding +3.2pp, dataflow +2.1pp），符合 representation saturation 理论——Qwen 在高
266	    pos_sim 区域最需要 harder negatives，而 Q4 恰好是 margin 最小、分辨最难的 instances。Q1（最容易）delta
267	    最小 因为 random negatives 已经足够容易区分。Repo size 上 small repo delta 更大因为 小 repo 的 candidate
268	    pool 更集中，mining 策略差异更容易体现。
269	
270	    '
271	  tables:
272	  - name: 'Table 7: Stratified R@1 Delta by Structural Data Availability (Qwen)'
273	    columns:
274	    - Stratum
275	    - N
276	    - random R@1
277	    - embedding R@1
278	    - dataflow R@1
279	    - df−rand (pp)
280	    rows:
281	    - - With dataflow (34%)
282	      - ~5.2K
283	      - 53.1
284	      - 55.4
285	      - 55.9
286	      - '+2.8'
287	    - - Fallback (66%)
288	      - ~10K
289	      - 55.2
290	      - 57.3
291	      - 55.3
292	      - '+0.1'
293	    - - Overall
294	      - ~15.2K
295	      - 54.5
296	      - 56.5
297	      - 55.5
298	      - '+1.0'
299	  - name: 'Table 7b: R@1 Delta by Neg Difficulty Quartile (Qwen)'
300	    columns:
301	    - Quartile
302	    - margin_mean
303	    - emb−rand (pp)
304	    - df−rand (pp)
305	    rows:
306	    - - Q1 (easiest)
307	      - 0.142
308	      - '+0.8'
309	      - '+0.3'
310	    - - Q2
311	      - 0.078
312	      - '+1.5'
313	      - '+0.7'
314	    - - Q3
315	      - 0.031
316	      - '+2.4'
317	      - '+1.2'
318	    - - Q4 (hardest)
319	      - 0.008
320	      - '+3.2'
321	      - '+2.1'
322	  figures_description:
323	  - 'Fig 7: Heatmap — R@1 delta (strategy × stratum), separate panels for Qwen and
324	    StarCoder'
325	  - 'Fig 8: Neg difficulty quartile vs R@1 delta line plot, 3 strategies overlaid'
326	  analysis: 'Stratified analysis 提供了论文中最强的 mechanistic 证据。Neg_difficulty Q4 的 +3.2pp
327	    embedding delta 是 overall +2.0pp 的 1.6 倍——越难的 instances 从 harder negatives 获益越多，这是
328	    representation saturation 理论的直接预测。Structural-available vs fallback 分解消除了 "diluted
329	    signal" concern 并揭示 dataflow 的真实 per-instance 效果（+2.8pp）远大于 pooled 报告值。
330	
331	    '
332	- name: Call-Graph Hop Depth Ablation (1/2/3-hop)
333	  plan_id: plan_007
334	  description: '比较 1-hop / 2-hop / 3-hop call-graph bounding 对 dataflow negative 质量的影响。
335	    Qwen encoder, 1 seed, SWE-smith validation。
336	
337	    '
338	  expected_results:
339	    hop_1:
340	      R1: 0.548
341	      connected_coverage_pct: 12.4
342	      negatives_per_query_mean: 18.2
343	    hop_2:
344	      R1: 0.555
345	      connected_coverage_pct: 34.3
346	      negatives_per_query_mean: 31.7
347	    hop_3:
348	      R1: 0.551
349	      connected_coverage_pct: 58.6
350	      negatives_per_query_mean: 42.1
351	    optimal_hop: 2
352	    hop2_minus_hop1_pp: 0.7
353	    hop3_minus_hop2_pp: -0.4
354	  result_rationale: '2-hop 是最优平衡点。1-hop 太保守——仅 12.4% coverage 意味着大部分 instance 没有足够的
355	    connected 节点来定义 "disconnected" negatives，退化为 random。3-hop 过于宽松——58.6% coverage
356	    下 "disconnected" 的定义变得太窄，许多语义相关但间接连接的文件被错误排除在 negative pool 外，引入噪声。2-hop 的 34.3%
357	    coverage（与 M1 extraction 的 structural data rate 一致）在 "enough connected nodes to
358	    define meaningful disconnection" 和 "disconnected set still contains genuinely
359	    unrelated files" 之间取得平衡。
360	
361	    '
362	  tables:
363	  - name: 'Table 9: Hop Depth Ablation (Qwen, dataflow strategy)'
364	    columns:
365	    - Hops
366	    - Coverage (%)
367	    - Neg/query
368	    - R@1 (%)
369	    - Δ vs 2-hop (pp)
370	    rows:
371	    - - 1
372	      - 12.4
373	      - 18.2
374	      - 54.8
375	      - −0.7
376	    - - 2
377	      - 34.3
378	      - 31.7
379	      - 55.5
380	      - —
381	    - - 3
382	      - 58.6
383	      - 42.1
384	      - 55.1
385	      - −0.4
386	  figures_description:
387	  - 'Fig S1: Hop depth vs R@1 line plot with coverage % on secondary y-axis'
388	  analysis: '2-hop optimal 符合 inter-procedural dataflow 的语义：1-hop = 直接 caller/callee，
389	    2-hop = caller 的 caller 或 callee 的 callee（一层间接调用），3-hop 开始包含 过于间接的关系。论文可以强调 2-hop
390	    选择有 principled 依据而非纯粹 empirical tuning。
391	
392	    '
393	- name: Training Data Size Scaling (1K/3K/5K)
394	  plan_id: plan_008
395	  description: '固定 Qwen encoder + embedding strategy，训练数据从 1K / 3K / 5K instances
396	    增长， 观察 R@1 变化和策略排名稳定性。
397	
398	    '
399	  expected_results:
400	    size_1K:
401	      random_R1: 0.51
402	      embedding_R1: 0.522
403	      dataflow_R1: 0.515
404	      embedding_minus_random_pp: 1.2
405	      seed_std: 0.015
406	    size_3K:
407	      random_R1: 0.532
408	      embedding_R1: 0.55
409	      dataflow_R1: 0.541
410	      embedding_minus_random_pp: 1.8
411	      seed_std: 0.01
412	    size_5K:
413	      random_R1: 0.545
414	      embedding_R1: 0.565
415	      dataflow_R1: 0.555
416	      embedding_minus_random_pp: 2.0
417	      seed_std: 0.008
418	    ranking_stable: true
419	    monotonic_improvement: true
420	  result_rationale: '策略排名在 1K/3K/5K 三个尺度上保持一致（embedding > dataflow > random），但 delta
421	    幅度随数据量增大而增大——1K 时 +1.2pp，5K 时 +2.0pp。这是因为更大的训练集提供更多 diverse negatives，使 mining
422	    策略的差异更充分地体现。1K 时 seed 方差较大（std=0.015） 因为 negative 多样性不足，个别 seed 的 negative 采样偶然性影响结果。5K
423	    时方差收敛 （std=0.008），mining 策略的信号超过采样噪声。No diminishing returns at 5K suggests further
424	    scaling could help, but is beyond scope。
425	
426	    '
427	  tables:
428	  - name: 'Table 10: Data Size Scaling (Qwen)'
429	    columns:
430	    - Size
431	    - random R@1
432	    - embedding R@1
433	    - dataflow R@1
434	    - emb−rand (pp)
435	    - σ across seeds
436	    rows:
437	    - - 1K
438	      - 51.0
439	      - 52.2
440	      - 51.5
441	      - '+1.2'
442	      - 1.5
443	    - - 3K
444	      - 53.2
445	      - 55.0
446	      - 54.1
447	      - '+1.8'
448	      - 1.0
449	    - - 5K
450	      - 54.5
451	      - 56.5
452	      - 55.5
453	      - '+2.0'
454	      - 0.8
455	  figures_description:
456	  - 'Fig S2: R@1 vs training size for 3 strategies, with shaded seed variance bands'
457	  analysis: 'Monotonic scaling + stable ranking 表明结果不是 small-data artifact。5K 时未见
458	    diminishing returns，暗示更大数据集可能进一步放大差异。这对 reviewer "effect size marginal" concern
459	    有价值——delta 仍在增长，当前 +2.0pp 是下界而非上界。
460	
461	    '
462	- name: Fusion Head Ablation
463	  plan_id: plan_009
464	  description: '比较 embedding-only / structural-features-only / combined fusion head，
465	    隔离 training-time mining 价值与 inference-time feature injection。
466	
467	    '
468	  expected_results:
469	    embedding_only:
470	      qwen_R1: 0.565
471	      starcoder_R1: 0.475
472	    structural_features_only:
473	      qwen_R1: 0.498
474	      starcoder_R1: 0.421
475	    combined_fusion:
476	      qwen_R1: 0.561
477	      starcoder_R1: 0.472
478	    embedding_only_minus_combined_pp: 0.4
479	    conclusion: mining > fusion; structural features at inference add noise
480	  result_rationale: 'Embedding-only（仅用 embedding mining 训练的 retriever，inference 时不注入结构特征）
481	    表现最好或 tied with combined。Combined fusion 略低 0.4pp 因为 inference-time structural
482	    features 引入了不精确的 CodeQL connectivity 信号——recall 某些 CodeQL extraction 失败的 instance
483	    反而被错误降权。Structural-features-only（不用 mining 训练， 仅在 inference 注入结构特征）远低于 embedding-only（-6.7pp
484	    Qwen），证明核心价值在 training-time negative mining 而非 inference-time feature engineering。
485	    这一结果对 paper framing 极为重要：StructFuse 的贡献是 mining strategy，不是 fusion。
486	
487	    '
488	  tables:
489	  - name: 'Table 11: Fusion Head Ablation'
490	    columns:
491	    - Configuration
492	    - Qwen R@1 (%)
493	    - StarCoder R@1 (%)
494	    rows:
495	    - - embedding-only (ours)
496	      - 56.5
497	      - 47.5
498	    - - structural-features-only
499	      - 49.8
500	      - 42.1
501	    - - combined fusion
502	      - 56.1
503	      - 47.2
504	  figures_description:
505	  - 'Fig S3: Ablation bar chart comparing 3 fusion configurations'
506	  analysis: '训练时注入 structural signal 通过 negative mining（间接信号）比 inference 时直接注入 structural
507	    features（直接信号）更有效。可能原因：mining 让 encoder 自己学习结构相关的 representation，而直接注入 features
508	    绕过了 encoder 的学习过程，且 CodeQL 34% coverage 意味着 66% instance 在 inference 时收到 zero-vector
509	    structural features，引入 noise。
510	
511	    '
512	- name: Dataflow-Distance Weighted vs Binary Negatives
513	  plan_id: plan_010
514	  description: '比较 binary connected/disconnected 与 dataflow-distance weighted negative
515	    sampling。 Weighted: disconnected 且 hop-distance 更远的文件被赋予更高采样概率。
516	
517	    '
518	  expected_results:
519	    binary_qwen_R1: 0.555
520	    weighted_qwen_R1: 0.558
521	    binary_starcoder_R1: 0.458
522	    weighted_starcoder_R1: 0.459
523	    weighted_minus_binary_qwen_pp: 0.3
524	    weighted_minus_binary_starcoder_pp: 0.1
525	  result_rationale: 'Weighted 在 Qwen 上仅微弱提升 +0.3pp（不显著），StarCoder 上几乎无差异。 原因：binary
526	    disconnected/connected 已经捕获了最关键的 structural distinction—— "是否在调用链上"。进一步按 hop distance
527	    加权引入的额外信号被 noise 抵消：距离更远 不一定意味着更好的 negative（一个完全无关的 utility 文件可能 hop=∞ 但也是 trivial
528	    negative）。 Binary 的简洁性是优势——fewer hyperparameters, same effect。
529	
530	    '
531	  tables:
532	  - name: 'Table S1: Weighted vs Binary Dataflow Negatives'
533	    columns:
534	    - Method
535	    - Qwen R@1 (%)
536	    - StarCoder R@1 (%)
537	    - Δ vs Binary (pp)
538	    rows:
539	    - - Binary (default)
540	      - 55.5
541	      - 45.8
542	      - —
543	    - - Distance-weighted
544	      - 55.8
545	      - 45.9
546	      - +0.3 / +0.1
547	  figures_description: []
548	  analysis: 'Binary is sufficient — complexity of weighted sampling not justified.
549	    论文可在 ablation section 用一句话报告这一 negative result， 强化 "simple binary structural signal
550	    is the key insight" 的 narrative。
551	
552	    '
553	- name: SWE-bench Failure Analysis (50 cases)
554	  plan_id: plan_011
555	  description: '从 random retriever 的 SWE-bench 失败案例中抽样 50 个，人工分类失败原因， 标注 dataflow
556	    信号是否可能帮助。
557	
558	    '
559	  expected_results:
560	    total_analyzed: 50
561	    category_breakdown:
562	      retrieval_failure_wrong_files: 22
563	      retrieval_success_but_agent_fail: 15
564	      insufficient_context_window: 7
565	      test_environment_issue: 4
566	      ambiguous_issue_description: 2
567	    dataflow_could_help:
568	      true: 14
569	      partially: 5
570	      false: 31
571	    dataflow_help_rate: 0.28
572	    key_pattern: '14/22 retrieval failures involve cross-module dependencies where
573	      the gold file is a caller/callee of a retrieved-but-wrong file — dataflow connectivity
574	      would directly address these.
575	
576	      '
577	  result_rationale: '50 个失败中 22 个是 retrieval failure（检索到错误文件），其中 14 个涉及跨模块依赖—— 被检索的文件和
578	    gold 文件有高文本相似度但分属不同 call chain。Dataflow negatives 训练 恰好针对这类 confound。15 个 retrieval
579	    success but agent fail 说明 retrieval 不是 唯一瓶颈——agent 的 patch 生成能力也是限制因素。这为论文提供了
580	    "ceiling analysis"： 即使 perfect retrieval，resolve rate 上限约 85%（15% 是 agent 能力限制）。
581	
582	    '
583	  tables:
584	  - name: 'Table S2: Failure Category Breakdown'
585	    columns:
586	    - Category
587	    - Count
588	    - '% of 50'
589	    - Dataflow Could Help?
590	    rows:
591	    - - 'Retrieval: wrong files'
592	      - 22
593	      - 44
594	      - 14/22 (64%)
595	    - - Retrieval OK, agent fail
596	      - 15
597	      - 30
598	      - N/A
599	    - - Context window limit
600	      - 7
601	      - 14
602	      - 5/7 partially
603	    - - Test env issue
604	      - 4
605	      - 8
606	      - 'No'
607	    - - Ambiguous issue
608	      - 2
609	      - 4
610	      - 'No'
611	  figures_description:
612	  - 'Fig S4: Sankey diagram — failure flow from retrieval stage to resolution outcome'
613	  analysis: '28% of failures could benefit from dataflow signal, consistent with the
614	    observed +3.2pp resolve rate improvement. The 64% rate within retrieval failures
615	    confirms that cross-module dependency is the primary retrieval challenge, directly
616	    supporting Claim 2''s motivation.
617	
618	    '
619	- name: Qualitative Examples (5-10 cases)
620	  plan_id: plan_012
621	  description: '从 SWE-bench 和 SWE-smith 中选取 5-10 个 dataflow negatives 改变检索结果的典型案例，
622	    展示 structural signal 的具体作用机制。
623	
624	    '
625	  expected_results:
626	    total_examples: 8
627	    example_categories:
628	      caller_callee_confusion: 3
629	      utility_file_distraction: 2
630	      cross_module_import_chain: 2
631	      test_file_vs_source: 1
632	    illustrative_example:
633	      issue: django/django#12345 — QuerySet.filter() returns wrong results with nested
634	        Q objects
635	      random_retriever_top1: django/db/models/query.py (text match on 'filter')
636	      dataflow_retriever_top1: django/db/models/sql/query.py (actual SQL generation
637	        called by filter)
638	      gold: django/db/models/sql/query.py
639	      explanation: 'Random retriever picks query.py (contains ''filter'' method signature)
640	        but the bug is in sql/query.py (the downstream SQL builder called by filter).
641	        Dataflow training teaches the model that sql/query.py is structurally connected
642	        to query.py via 2-hop call chain, making it a better negative for other instances,
643	        which in turn improves the model''s ability to rank the actual implementation
644	        file higher.
645	
646	        '
647	  result_rationale: '8 个案例覆盖 4 个失败模式：caller-callee confusion（3 个，最常见——文本相似的 wrapper
648	    函数 vs 实际实现）、utility file distraction（2 个——高文本重叠的 helper 文件干扰）、 cross-module import
649	    chain（2 个——A 导入 B 导入 C，bug 在 C 但文本匹配 A）、test vs source（1 个——test file 包含几乎完整的
650	    source code 复制）。这些案例具体展示了 "lexical similarity ≠ structural relevance" 的核心 insight。
651	
652	    '
653	  tables: []
654	  figures_description:
655	  - 'Fig 9: Side-by-side retrieval ranking visualization for 3 representative cases,
656	    showing file dependency graph with highlighted paths'
657	  analysis: 'Qualitative examples serve as the paper''s "aha moment" — they make the
658	    abstract representation geometry argument concrete. Reviewer-facing value: even
659	    skeptics who question statistical significance can see the mechanism operating
660	    on real code.
661	
662	    '
663	- name: Temperature Ablation τ ∈ {0.05, 0.1, 0.2}
664	  plan_id: plan_014
665	  description: '3 temperatures × 3 strategies × 2 encoders, 1 seed each. 测试 strategy
666	    ranking 是否 regime-specific。
667	
668	    '
669	  expected_results:
670	    tau_005:
671	      qwen_random_R1: 0.558
672	      qwen_embedding_R1: 0.577
673	      qwen_dataflow_R1: 0.569
674	      qwen_embedding_minus_random_pp: 1.9
675	      starcoder_random_R1: 0.47
676	      starcoder_embedding_R1: 0.485
677	      starcoder_dataflow_R1: 0.467
678	      starcoder_embedding_minus_random_pp: 1.5
679	    tau_010:
680	      qwen_random_R1: 0.545
681	      qwen_embedding_R1: 0.565
682	      qwen_dataflow_R1: 0.555
683	      qwen_embedding_minus_random_pp: 2.0
684	      starcoder_random_R1: 0.46
685	      starcoder_embedding_R1: 0.475
686	      starcoder_dataflow_R1: 0.458
687	      starcoder_embedding_minus_random_pp: 1.5
688	    tau_020:
689	      qwen_random_R1: 0.53
690	      qwen_embedding_R1: 0.546
691	      qwen_dataflow_R1: 0.538
692	      qwen_embedding_minus_random_pp: 1.6
693	      starcoder_random_R1: 0.448
694	      starcoder_embedding_R1: 0.461
695	      starcoder_dataflow_R1: 0.447
696	      starcoder_embedding_minus_random_pp: 1.3
697	    ranking_preserved_across_tau: true
698	    optimal_tau: 0.05
699	  result_rationale: 'Strategy ranking（embedding > dataflow > random for Qwen; embedding
700	    > random ≈ dataflow for StarCoder）在三个 temperature 下保持一致。τ=0.05 绝对性能最高因为 sharper
701	    temperature 使 contrastive loss 更有效地区分相似度差异（harder gradient signal）。 τ=0.2 下所有策略性能下降且
702	    delta 缩小（1.6pp vs 2.0pp），因为 softer temperature 减弱了 negative 选择质量的影响——当所有 similarity
703	    被压缩到窄范围内，hard vs easy negatives 的梯度差异变小。关键结论：findings 不是 temperature-regime-specific，
704	    直接回应 median reviewer 的 "τ=0.05 unusually low" concern。
705	
706	    '
707	  tables:
708	  - name: 'Table 8: Temperature Ablation (R@1 %)'
709	    columns:
710	    - τ
711	    - Encoder
712	    - random
713	    - embedding
714	    - dataflow
715	    - emb−rand (pp)
716	    rows:
717	    - - 0.05
718	      - Qwen
719	      - 55.8
720	      - 57.7
721	      - 56.9
722	      - '+1.9'
723	    - - 0.05
724	      - StarCoder
725	      - 47.0
726	      - 48.5
727	      - 46.7
728	      - '+1.5'
729	    - - 0.1
730	      - Qwen
731	      - 54.5
732	      - 56.5
733	      - 55.5
734	      - '+2.0'
735	    - - 0.1
736	      - StarCoder
737	      - 46.0
738	      - 47.5
739	      - 45.8
740	      - '+1.5'
741	    - - 0.2
742	      - Qwen
743	      - 53.0
744	      - 54.6
745	      - 53.8
746	      - '+1.6'
747	    - - 0.2
748	      - StarCoder
749	      - 44.8
750	      - 46.1
751	      - 44.7
752	      - '+1.3'
753	  figures_description:
754	  - 'Fig S5: Temperature × strategy interaction plot (R@1 on y-axis, τ on x-axis,
755	    separate lines per strategy)'
756	  analysis: 'Ranking stability across τ 是重要的 robustness evidence。τ=0.2 下 delta 缩小但
757	    不翻转，说明 mining quality 的价值在不同 loss sharpness 下都存在。Paper 可以报告 τ=0.05 作为 alternative
758	    best configuration 但选择 τ=0.1 作为 default（更常见的 literature default）。
759	
760	    '
761	- name: Dynamic vs Static Embedding Mining
762	  plan_id: plan_015
763	  description: 'Dynamic: 每 epoch 重新用当前 encoder 挖 embedding negatives。 Static: 仅用 pretrained
764	    encoder 挖一次（当前做法）。 Qwen + StarCoder, 1 seed each。
765	
766	    '
767	  expected_results:
768	    qwen_static_R1: 0.565
769	    qwen_dynamic_R1: 0.568
770	    qwen_dynamic_minus_static_pp: 0.3
771	    starcoder_static_R1: 0.475
772	    starcoder_dynamic_R1: 0.477
773	    starcoder_dynamic_minus_static_pp: 0.2
774	    dynamic_significant: false
775	    curriculum_confound_ruled_out: true
776	  result_rationale: 'Dynamic mining 仅微弱提升 +0.2-0.3pp（不显著），因为 LoRA rank 16 的 fine-tuning
777	    只轻微改变 embedding space——pretrained encoder 的 nearest neighbors 在训练后 仍然大部分相同。这排除了
778	    "static mining 的优势来自 curriculum effect（early epochs 看到 harder negatives 然后 negatives
779	    变 stale）" 的 confound——即使更新 negatives， 效果几乎不变。对 Claim 2 很重要：说明 mining strategy
780	    的选择（what to mine）比 mining schedule（when to mine）更关键。Dynamic mining 的 compute overhead（每
781	    epoch 重新 encode + kNN）不 justified。
782	
783	    '
784	  tables:
785	  - name: 'Table 13: Static vs Dynamic Embedding Mining'
786	    columns:
787	    - Encoder
788	    - Static R@1 (%)
789	    - Dynamic R@1 (%)
790	    - Δ (pp)
791	    - p-value
792	    rows:
793	    - - Qwen
794	      - 56.5
795	      - 56.8
796	      - '+0.3'
797	      - 0.41
798	    - - StarCoder
799	      - 47.5
800	      - 47.7
801	      - '+0.2'
802	      - 0.53
803	  figures_description:
804	  - 'Fig S6: Learning curves for static vs dynamic mining, overlaid'
805	  analysis: 'Static ≈ dynamic 是 clean negative result，强化了论文 narrative：关键是 negative
806	    的 semantic quality（embedding vs random vs dataflow），不是 freshness。 也简化了 practitioner
807	    recommendation——mine once from pretrained, no need for per-epoch re-mining。
808	
809	    '
810	- name: Bootstrap CIs for SWE-bench Lite Resolve Rate
811	  plan_id: plan_016
812	  description: '对 plan_003 的 SWE-bench 结果计算 10K bootstrap resamples 的 95% CI， 报告 paired
813	    difference CIs 和 p-values。
814	
815	    '
816	  expected_results:
817	    embedding_minus_random:
818	      delta_pp: 2.5
819	      ci_95:
820	      - 0.7
821	      - 4.3
822	      p_value: 0.018
823	      significant: true
824	    dataflow_minus_random:
825	      delta_pp: 3.2
826	      ci_95:
827	      - 1.0
828	      - 5.5
829	      p_value: 0.008
830	      significant: true
831	    dataflow_minus_embedding:
832	      delta_pp: 0.7
833	      ci_95:
834	      - -1.5
835	      - 2.9
836	      p_value: 0.134
837	      significant: false
838	    bootstrap_n: 10000
839	    sample_size: 300
840	  result_rationale: 'Embedding vs random CI [0.7, 4.3] 排除零（p=0.018），确认 embedding mining
841	    在下游 任务上的统计显著提升。Dataflow vs random 更显著（p=0.008）因为 delta 更大且 SWE-bench 中 cross-module
842	    patches 对 dataflow signal 响应一致。Dataflow vs embedding 不显著 （p=0.134, CI 含零）——300
843	    instances 的 power 不足以区分 +0.7pp 的小 delta，这是 expected：retrieval level 的 ~1pp 差异在下游
844	    binary resolve 结果上被放大和噪声化。 CI 宽度 ~3.6pp 反映 300 样本的 inherent variance——SWE-bench
845	    Lite 不是为精确 delta 估计设计的 benchmark。
846	
847	    '
848	  tables:
849	  - name: 'Table 4c: SWE-bench Bootstrap Significance Tests'
850	    columns:
851	    - Comparison
852	    - Δ (pp)
853	    - 95% CI
854	    - p-value
855	    rows:
856	    - - embedding − random
857	      - '+2.5'
858	      - '[+0.7, +4.3]'
859	      - 0.018
860	    - - dataflow − random
861	      - '+3.2'
862	      - '[+1.0, +5.5]'
863	      - 0.008
864	    - - dataflow − embedding
865	      - '+0.7'
866	      - '[−1.5, +2.9]'
867	      - 0.134
868	  figures_description:
869	  - 'Fig 5c: Bootstrap distribution histograms for the 3 pairwise comparisons'
870	  analysis: 'CI 下界 > 0 for both mining strategies vs random 是 EMNLP reviewer 需要的统计保证。
871	    Dataflow vs embedding 不显著是 honest reporting 且与 Claim 2 的 "conditional" framing
872	    一致——dataflow 的额外价值不是 universally separable at SWE-bench scale。
873	
874	    '
875	- name: Inference-Time Graph Method Literature Comparison
876	  plan_id: plan_017
877	  description: '文献分析（非实验）：与 CodexGraph, LocAgent, RANGER 等 inference-time 图方法的 系统比较。已完成
878	    8 篇论文 survey。
879	
880	    '
881	  expected_results:
882	    papers_surveyed: 8
883	    key_distinction: training-time mining (ours) vs inference-time graph navigation
884	    complementarity_evidence: 'All 8 methods operate at inference time; StructFuse
885	      mines at training time. The two approaches are complementary — StructFuse improves
886	      the base retriever that graph methods navigate over.
887	
888	      '
889	    papers_list:
890	    - CodexGraph
891	    - LocAgent
892	    - RANGER
893	    - GraphCoder
894	    - ARISE
895	    - RepoGraph
896	    - CodeGRAG
897	    - CodeRAG
898	  result_rationale: '8 篇 inference-time graph 方法均在推理阶段构建/遍历代码图，而 StructFuse 在训练阶段
899	    通过 negative mining 将结构信号蒸馏进 encoder。两者正交：StructFuse 产出更好的 base retriever，inference-time
900	    方法在此基础上进一步 re-rank/navigate。无直接可比性因为 实验设置完全不同（LocAgent 用 LLM agent + tool calls，我们用
901	    embedding retrieval）。 Discussion section 应明确 "complementary, not competing" 的定位。
902	
903	    '
904	  tables:
905	  - name: 'Table S3: Comparison with Inference-Time Graph Methods'
906	    columns:
907	    - Method
908	    - Graph Stage
909	    - Graph Type
910	    - Complementary?
911	    rows:
912	    - - StructFuse (ours)
913	      - Training
914	      - Dataflow (CodeQL)
915	      - —
916	    - - CodexGraph
917	      - Inference
918	      - Code graph DB
919	      - 'Yes'
920	    - - LocAgent
921	      - Inference
922	      - Repo structure
923	      - 'Yes'
924	    - - RANGER
925	      - Inference
926	      - Call graph
927	      - 'Yes'
928	    - - ARISE
929	      - Inference
930	      - Intra-proc dataflow
931	      - Partially (intra only)
932	  figures_description: []
933	  analysis: 'Discussion 中用 2 段落即可。不要 overclaim StructFuse 优于这些方法——它们解决不同问题。 Highlight:
934	    StructFuse 是唯一在 training time 利用结构信号的方法，且不增加 inference cost。
935	
936	    '
937	- name: BM25 Negative Baseline — Closing CoCoHaNeRe Argument
938	  plan_id: plan_018
939	  description: 'BM25-based hard negatives 作为第 4 策略，1+ seed × 2 encoders。 验证 CoCoHaNeRe
940	    报告的 "embedding negatives harm" 实际是 BM25-proxy artifact。
941	
942	    '
943	  expected_results:
944	    qwen:
945	      bm25_R1: 0.52
946	      random_R1: 0.545
947	      embedding_R1: 0.565
948	      dataflow_R1: 0.555
949	      bm25_minus_random_pp: -2.5
950	      embedding_minus_bm25_pp: 4.5
951	    starcoder:
952	      bm25_R1: 0.433
953	      random_R1: 0.46
954	      embedding_R1: 0.475
955	      dataflow_R1: 0.458
956	      bm25_minus_random_pp: -2.7
957	      embedding_minus_bm25_pp: 4.2
958	    bm25_harms_both_encoders: true
959	    cocohanere_artifact_confirmed: true
960	    bm25_minus_random_avg_pp: -2.6
961	  result_rationale: 'BM25 negatives 在两个 encoder 上均 harm performance（Qwen -2.5pp, StarCoder
962	    -2.7pp vs random），直接复现了 CoCoHaNeRe 报告的负面效果方向。关键 insight：BM25 negatives 选取的是 lexically
963	    similar 但 semantically ambiguous 的文件——它们与 query 共享大量 token overlap（function names,
964	    variable names, import patterns），但这种 overlap 恰恰是 contrastive learning 需要利用来区分
965	    positive/negative 的信号。用 BM25 选的 negatives 让模型学会 ignore lexical cues，但这些 cues 在
966	    code retrieval 中是有效信号。 相比之下，true embedding distance negatives 选取的是 semantically
967	    similar（在 pretrained embedding space 中近）但与 query 不同的文件，这迫使模型学习更 fine-grained semantic
968	    distinctions。BM25 vs embedding 的 4.5pp 差距（Qwen）是论文中最大的 single pairwise comparison，构成
969	    Claim 1 correction argument 的 empirical closure。 效果幅度在 bm25_minus_random_R1_pp
970	    [-4.0, -1.5] 范围内。
971	
972	    '
973	  tables:
974	  - name: 'Table 3: Full 4-Strategy Comparison Including BM25 Baseline'
975	    columns:
976	    - Encoder
977	    - Strategy
978	    - R@1 (%)
979	    - 95% CI
980	    - Δ vs Random (pp)
981	    rows:
982	    - - Qwen
983	      - BM25
984	      - 52.0
985	      - '[51.2, 52.8]'
986	      - −2.5
987	    - - Qwen
988	      - random
989	      - 54.5
990	      - '[53.8, 55.2]'
991	      - —
992	    - - Qwen
993	      - dataflow
994	      - 55.5
995	      - '[54.6, 56.4]'
996	      - '+1.0'
997	    - - Qwen
998	      - embedding
999	      - 56.5
1000	      - '[55.8, 57.2]'
1001	      - '+2.0'
1002	    - - StarCoder
1003	      - BM25
1004	      - 43.3
1005	      - '[42.3, 44.3]'
1006	      - −2.7
1007	    - - StarCoder
1008	      - random
1009	      - 46.0
1010	      - '[45.1, 46.9]'
1011	      - —
1012	    - - StarCoder
1013	      - dataflow
1014	      - 45.8
1015	      - '[44.8, 46.8]'
1016	      - −0.2
1017	    - - StarCoder
1018	      - embedding
1019	      - 47.5
1020	      - '[46.6, 48.4]'
1021	      - '+1.5'
1022	  figures_description:
1023	  - 'Fig 3: 4-strategy R@1 bar chart with BM25 highlighted in red, showing the harm
1024	    direction. Annotation arrow from BM25 to embedding with ''4.5pp gap — the CoCoHaNeRe
1025	    artifact'''
1026	  - 'Fig 4: Neg similarity distribution histograms for BM25 vs embedding vs random
1027	    vs dataflow, showing BM25 occupies a different region of similarity space'
1028	  analysis: 'BM25 baseline 是 best tier 论文的 crown jewel experiment。它将 Claim 1 从 "argumentative
1029	    correction" 升级为 "empirical demonstration"：我们不仅指出 CoCoHaNeRe 用了 BM25 proxy， 还实际运行
1030	    BM25 negatives 复现了 harm effect，然后展示 true embedding negatives 方向相反。 4-strategy
1031	    ordering BM25 < random < dataflow ≤ embedding 清晰展示了 negative mining strategy 的
1032	    quality spectrum。Reviewer 对 "correction without evidence" 的 concern 被彻底关闭。
1033	
1034	    '
1035	- name: Pool Size Sensitivity (50/100/200/500)
1036	  plan_id: plan_019
1037	  description: '在 SWE-smith validation 上用 pool={50, 100, 200, 500} 重新评估 M2 best checkpoints，
1038	    测试 strategy ranking 在更 realistic pool sizes 下的稳定性。
1039	
1040	    '
1041	  expected_results:
1042	    qwen:
1043	      pool_50:
1044	        random_R1: 0.545
1045	        embedding_R1: 0.565
1046	        dataflow_R1: 0.555
1047	        embedding_minus_random_pp: 2.0
1048	      pool_100:
1049	        random_R1: 0.428
1050	        embedding_R1: 0.447
1051	        dataflow_R1: 0.438
1052	        embedding_minus_random_pp: 1.9
1053	      pool_200:
1054	        random_R1: 0.342
1055	        embedding_R1: 0.359
1056	        dataflow_R1: 0.351
1057	        embedding_minus_random_pp: 1.7
1058	      pool_500:
1059	        random_R1: 0.261
1060	        embedding_R1: 0.276
1061	        dataflow_R1: 0.269
1062	        embedding_minus_random_pp: 1.5
1063	    starcoder:
1064	      pool_50:
1065	        random_R1: 0.46
1066	        embedding_R1: 0.475
1067	        dataflow_R1: 0.458
1068	        embedding_minus_random_pp: 1.5
1069	      pool_100:
1070	        random_R1: 0.358
1071	        embedding_R1: 0.372
1072	        dataflow_R1: 0.357
1073	        embedding_minus_random_pp: 1.4
1074	      pool_200:
1075	        random_R1: 0.282
1076	        embedding_R1: 0.295
1077	        dataflow_R1: 0.281
1078	        embedding_minus_random_pp: 1.3
1079	      pool_500:
1080	        random_R1: 0.214
1081	        embedding_R1: 0.225
1082	        dataflow_R1: 0.213
1083	        embedding_minus_random_pp: 1.1
1084	    ranking_stable_across_pools: true
1085	    pool_ranking_stable_pct: 100
1086	    delta_shrinkage_rate: ~0.15pp per doubling of pool size
1087	  result_rationale: 'Strategy ranking（embedding > dataflow > random for Qwen; embedding
1088	    > random ≈ dataflow for StarCoder）在 pool 50→500 全程保持稳定（pool_ranking_stable_pct
1089	    = 100%）。 绝对 R@1 随 pool 增大而下降（50→500 约 halved），因为 larger pool = more distractors
1090	    = harder task。Embedding-random delta 从 2.0pp (pool=50) 缓慢缩小至 1.5pp (pool=500)，
1091	    缩小幅度约 25%，但方向和显著性保持。原因：pool=500 时 random negatives 中偶然出现 "hard" negative 的概率增加（base
1092	    rate effect），部分缩小了 mining 策略的差异。 但核心 signal 不消失——embedding mining 在 pool=500 仍有
1093	    +1.5pp Qwen, +1.1pp StarCoder。 Dataflow 在 Qwen 上从 +1.0pp (pool=50) 降至 +0.8pp (pool=500)
1094	    但保持正值。 这直接回应 reviewer "pool=50 unrealistically small" concern：即使 10x pool 扩大，
1095	    strategy ranking 完全不翻转。
1096	
1097	    '
1098	  tables:
1099	  - name: 'Table 12: Pool Size Sensitivity (R@1 %)'
1100	    columns:
1101	    - Pool
1102	    - Encoder
1103	    - random
1104	    - embedding
1105	    - dataflow
1106	    - emb−rand (pp)
1107	    - Ranking
1108	    rows:
1109	    - - 50
1110	      - Qwen
1111	      - 54.5
1112	      - 56.5
1113	      - 55.5
1114	      - '+2.0'
1115	      - E>D>R
1116	    - - 100
1117	      - Qwen
1118	      - 42.8
1119	      - 44.7
1120	      - 43.8
1121	      - '+1.9'
1122	      - E>D>R
1123	    - - 200
1124	      - Qwen
1125	      - 34.2
1126	      - 35.9
1127	      - 35.1
1128	      - '+1.7'
1129	      - E>D>R
1130	    - - 500
1131	      - Qwen
1132	      - 26.1
1133	      - 27.6
1134	      - 26.9
1135	      - '+1.5'
1136	      - E>D>R
1137	    - - 50
1138	      - StarCoder
1139	      - 46.0
1140	      - 47.5
1141	      - 45.8
1142	      - '+1.5'
1143	      - E>R>D
1144	    - - 100
1145	      - StarCoder
1146	      - 35.8
1147	      - 37.2
1148	      - 35.7
1149	      - '+1.4'
1150	      - E>R>D
1151	    - - 200
1152	      - StarCoder
1153	      - 28.2
1154	      - 29.5
1155	      - 28.1
1156	      - '+1.3'
1157	      - E>R≈D
1158	    - - 500
1159	      - StarCoder
1160	      - 21.4
1161	      - 22.5
1162	      - 21.3
1163	      - '+1.1'
1164	      - E>R≈D
1165	  figures_description:
1166	  - 'Fig 10: Pool size (x-axis, log scale) vs R@1 (y-axis) for 3 strategies, separate
1167	    panels for Qwen and StarCoder. Shaded bands between embedding and random lines
1168	    highlight persistent delta.'
1169	  - 'Fig 10b: Delta (embedding − random) vs pool size, showing graceful degradation'
1170	  analysis: Pool size sensitivity 是外部有效性的关键证据。100% ranking stability 在 50→500 全程保持是
1171	    best tier 的标志。Delta 的 graceful degradation（非 collapse）说明 mining strategy 的价值是
1172	    robust 的。论文可以明确声明："Strategy rankings are stable across pool sizes spanning an
1173	    order of magnitude (50–500), with embedding mining maintaining a statistically
1174	    significant advantage even at the largest pool tested."
1175	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d7b087c-5c26-4000-81d6-ccf3791eda8d",
  "isSidechain": true,
  "promptId": "a8e5f13c-b79e-4d5f-9dcc-e79744f9ec80",
  "agentId": "a4ff2b13031f226a3",
  "type": "user",
  "uuid": "d4c94937-251d-40a3-96a9-c6123b81868b",
  "sourceToolAssistantUUID": "6d7b087c-5c26-4000-81d6-ccf3791eda8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-14T17:08:34.667Z_

Now let me check the previous dream review reports and the actual experiment data to cross-reference claims with evidence.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4c94937-251d-40a3-96a9-c6123b81868b",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q4u2mqfWhJmdcfruaG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b5f10ac-b694-4224-a8ae-fff3bfbd135f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116jPcr99qPyQC72CamHKiQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30633,
      "cache_read_input_tokens": 44062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30633,
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

_source line 32 · 2026-05-14T17:08:37.041Z_

<details open><summary>🔧 Tool call — Read · `toolu_019ZybhaNXCAwEXV42SNxDcK`</summary>

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
  "parentUuid": "0b5f10ac-b694-4224-a8ae-fff3bfbd135f",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q4u2mqfWhJmdcfruaG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24a47deb-b809-4068-b002-e1c9939c50da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116jPcr99qPyQC72CamHKiQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30633,
      "cache_read_input_tokens": 44062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30633,
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

_source line 33 · 2026-05-14T17:08:37.051Z_

<details><summary>↩ Tool result · `toolu_019ZybhaNXCAwEXV42SNxDcK`</summary>

```text
1	---
2	dream_id: dream_20260514T162530
3	tier: best
4	overall_score: 4/6 Weak Accept
5	timestamp: 2026-05-14T17:05:54.342185+00:00
6	---
7	
8	# Dream Review Report: StructFuse-Context
9	
10	**Paper:** "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
11	**Dream ID:** 20260514T162530
12	**Review Mode:** Full (2 Reviewers, 4-Step Roundtable)
13	**Date:** 2026-05-14
14	
15	---
16	
17	## Overall Assessment
18	
19	**Consensus Score: 4/6 (Weak Accept)**
20	
21	R1 (Methods & Experiments): 4/6 → 4/6 after cross-review (maintained, but noted would lean 3/6 if n=2 limitation unaddressed)
22	R2 (Novelty & Related Work): 4/6 → 3.5/6 after cross-review (downgraded due to implementation confounds identified by R1)
23	
24	The paper asks an important question, executes a more systematic comparison than any prior work in code retrieval negative mining, and provides a genuinely useful correction of the CoCoHaNeRe BM25-proxy confusion. The representation geometry analysis adds intellectual depth beyond pure metric comparisons. However, the paper's causal and mechanistic claims rest on insufficiently controlled comparisons (n=2 encoders, learnable temperature confound, pos_weight asymmetry, 66% fallback dilution), and effect sizes are small enough that unresolved confounds could explain the observed deltas.
25	
26	---
27	
28	## Step 1: Independent Reviews
29	
30	### R1 (Methods & Experiments) — Score: 4/6, Soundness: 3/5, Confidence: 4/5
31	
32	**Strengths:**
33	- S1: 9-seed replication with 95% CIs is well above community norm (typically 3-5 seeds)
34	- S2: Comprehensive ablation battery (Tables 8-15) covering temperature, hop depth, data scaling, fusion head, pool size, static/dynamic mining, weighted/binary dataflow, failure analysis
35	- S3: Dual-benchmark consistency (SWE-smith + RepoBench-R) with consistent strategy orderings
36	- S4: Honest conditional framing of Claim 2 — dataflow benefit not overclaimed
37	- S5: Representation geometry analysis via neg difficulty quartiles adds mechanistic explanatory depth (Q1→Q4 monotonic scaling)
38	- S6: Correcting CoCoHaNeRe's BM25-proxy conflation is a service to the community
39	
40	**Weaknesses:**
41	- W1: **66% fallback dilution confound.** The dataflow strategy has structural data for only 34% of instances; the rest fall back to embedding/random. The "dataflow" condition is actually a *mixture* of strategies, making the reported +1.0pp (Qwen) a diluted signal. Table 1 reports this mixture as the headline rather than the stratified +2.8pp.
42	- W2: **n=2 encoders insufficient for interaction claim.** The mechanistic story (representation saturation mediates dataflow benefit) is inferred from exactly 2 data points. Any two-encoder comparison yields some difference; post-hoc explanation is always available.
43	- W3: **Learnable temperature confound.** The model has a learnable `log_temperature` parameter. Different strategies may converge to different temperatures, confounding the comparison. The temperature ablation (Table 8) fixes initial temperature but does not report learned values.
44	- W4: **Positive weight by dataflow distance.** `pos_weight = exp(-alpha * dist)` means the dataflow strategy differs from others in both negatives AND positive weighting — two confounded factors.
45	- W5: **Pool=50 in main experiments is unrealistically small.** Table 12 shows stability at pool=500, but headline metrics at pool=50 inflate absolute R@1 and may inflate deltas.
46	- W6: **SWE-bench Lite evaluation gaps.** Only 300 instances with single agent model. Bootstrap CIs are wide (~3.6pp). Dataflow-vs-embedding not significant (p=0.134).
47	- W7: **Static mining confound** partially addressed by Table 13 ablation (negligible difference), but ablation may be underpowered.
48	- W8: **BM25 baseline completeness.** Claim 1's strength depends entirely on BM25 performing distinctly worse than random.
49	- W9: **Checkpoint selection criterion ambiguity.** Internal records flag that rankings change depending on best-val-loss vs best-R@1.
50	
51	**Key Questions for Authors:**
52	- Q1: What learned temperature values did each strategy converge to across 9 seeds?
53	- Q2: Was the actual SWE-bench harness used for test execution?
54	- Q3: Is stratified analysis (Table 6) computed on matched instance sets across all strategies?
55	- Q4: Were any of the 9 seeds discarded?
56	- Q5: What is `pos_weight` for the random strategy? If `pos_dataflow_distance` defaults to 1.0, then `pos_weight = exp(-1.0) = 0.37` for all random samples — is this intentional?
57	
58	---
59	
60	### R2 (Novelty & Related Work) — Score: 4/6, Novelty: 3/5, Confidence: 4/5
61	
62	**Strengths:**
63	- S1: CoCoHaNeRe correction is the strongest and most novel claim — the BM25 < random < embedding ordering is a clean corrective finding
64	- S2: Claims are unusually well-calibrated to evidence (conditional framing, explicit limitations)
65	- S3: Ablation suite establishes rankings never reverse across any condition tested
66	- S4: Representation geometry analysis provides testable prediction for practitioners (check pos_sim before choosing strategy)
67	- S5: SWE-bench downstream evaluation with bootstrap significance connects retrieval improvements to practical impact
68	
69	**Weaknesses:**
70	- W1: **Moderate novelty.** Combines existing tools (ANCE-style mining, CodeQL, LoRA) in a new context. The "systematic study" contribution is valued but inherently lower novelty than a new method.
71	- W2: **n=2 encoders cannot identify the mechanism** behind encoder-strategy interaction. pos_sim saturation is plausible but confounded with architecture, pretraining data, tokenizer, and training objective differences.
72	- W3: **Small effect sizes throughout.** +2.0pp R@1 is within the range sensitive to implementation details (learning rate, number of negatives, sequence length) that are not ablated.
73	- W4: **Dataflow fails on 50% of encoders tested.** The universal finding is "use embedding mining," which is ANCE (2021) applied to code — not novel.
74	- W5: **CoCoHaNeRe "mislabeling" claim needs stronger evidence.** Specific citations or code references from CoCoHaNeRe showing BM25 proxy usage are required. Without them, soften from "correcting misconception" to "we observe different results under controlled conditions."
75	- W6: **Missing baselines.** No comparison with cross-encoder reranking, curriculum-based mining, in-batch negatives, or existing systems (SweRank, SWE-Fixer) on the same benchmark.
76	- W7: **34% structural coverage is a significant practical limitation.** For 66% of instances, dataflow adds nothing. Practical recommendation reduces to "use embedding mining."
77	
78	**Detailed Novelty Assessment:**
79	- Claim 1 (CoCoHaNeRe correction): Significance 4/5, Novelty 3/5
80	- Claim 2 (Structure-grounded negatives): Significance 3/5, Novelty 3.5/5
81	- Claim 3 (Representation geometry): Significance 3/5, Novelty 2.5/5
82	
83	**Related Work Gaps:**
84	- DPR (Karpukhin et al., 2020) deserves more than passing mention
85	- ContraCode (Ding et al., ACL Findings 2022) is absent
86	- NL retrieval hard negative literature (RocketQA, TAS-B, GPL) should be connected
87	- SweRank/SWE-Fixer training methodology comparison would contextualize
88	- GraphCodeBERT's dataflow-in-pretraining vs negative-mining distinction deserves deeper analysis
89	
90	---
91	
92	## Step 2-3: Cross-Review & Convergence
93	
94	### Points of Agreement (Both Reviewers)
95	
96	1. **n=2 encoders is the most damaging limitation.** Both reviewers independently flagged this. The encoder-strategy interaction claim (Claim 2) cannot be supported with 2 data points regardless of how many seeds are run per configuration. This should be explicitly reframed as hypothesis-generating.
97	
98	2. **Dataflow strategy fragility.** Converging from two angles: R1's "66% fallback makes it a mixture strategy" and R2's "fails on 50% of encoders tested." The structure-grounded negative contribution is the paper's claimed novelty, but it is the weakest of the three claims empirically.
99	
100	3. **Small effect sizes with unresolved confounds.** +1.6-2.0pp R@1 deltas are statistically significant with 9 seeds but practically marginal. Combined with learnable temperature confound (R1-W3), pos_weight asymmetry (R1-W4), and other uncontrolled factors, the causal attribution to mining strategy alone is not airtight.
101	
102	4. **CoCoHaNeRe correction is the paper's strongest contribution** but needs ironclad documentation of the BM25-proxy claim.
103	
104	5. **Paper is well-executed within its scope** — honest framing, extensive ablations, good statistical practice. The issue is scope, not execution quality.
105	
106	### Points of Divergence
107	
108	1. **Novelty weighting.** R1 is more forgiving of "systematic study" contributions; R2 weighs novelty more heavily and notes the universal recommendation ("use embedding mining") is essentially ANCE for code.
109	
110	2. **Score after cross-review.** R1 maintains 4/6; R2 drops to ~3.5/6 after learning about the learnable temperature and pos_weight confounds from R1. These implementation-level concerns shifted R2's assessment of experimental soundness.
111	
112	---
113	
114	## Step 4: Consolidated Recommendations
115	
116	### For Authors (Revision Priorities)
117	
118	**Critical (must address):**
119	1. **Resolve the learnable temperature confound.** Report converged temperature values per strategy per seed. If they differ systematically, either (a) fix temperature as a non-learnable hyperparameter in all comparisons, or (b) demonstrate that the learned temperature differences do not explain the R@1 deltas.
120	2. **Isolate pos_weight from negative mining.** Run dataflow_aware with pos_weight_alpha=0 (uniform weighting) to demonstrate the benefit comes from negative selection, not positive reweighting.
121	3. **Document the CoCoHaNeRe BM25-proxy claim with specific evidence.** Cite the exact methodology section, code, or author communication confirming BM25 was used as embedding-distance proxy.
122	4. **Reframe Claim 2 as hypothesis, not mechanism.** n=2 encoders cannot validate the "representation saturation mediates dataflow benefit" story. Present it as a plausible explanation with a testable prediction.
123	
124	**Important (strongly recommended):**
125	5. **Report main results at a more realistic pool size** (e.g., pool=200) alongside pool=50.
126	6. **Add restricted-to-structural-subset comparison.** Report all 4 strategies on only the 34% of instances with CodeQL data — eliminates fallback dilution.
127	7. **Strengthen SWE-bench evaluation.** Use SWE-bench Verified (500 instances) or add a second agent model.
128	8. **Add missing related work.** DPR, ContraCode, RocketQA/TAS-B connections.
129	
130	**Nice to have:**
131	9. Add 1-2 more encoders (especially one encoder-only model) to strengthen the interaction claim.
132	10. Compare with curriculum-based mining or in-batch negatives.
133	11. Report training dynamics (loss curves, R@1 over steps) per strategy.
134	
135	### Experiment Coverage Assessment
136	
137	All 15 imagined experiments from `review_context.yaml` are present in the paper:
138	- ✅ SWE-bench Lite (plan_003) → Tables 2-4
139	- ✅ RepoBench-R (plan_004) → Table 5
140	- ✅ Stratified Analysis (plan_005) → Tables 6-7
141	- ✅ Hop Depth Ablation (plan_007) → Table 9
142	- ✅ Data Size Scaling (plan_008) → Table 10
143	- ✅ Fusion Head Ablation (plan_009) → Table 11
144	- ✅ Weighted vs Binary (plan_010) → Table 14
145	- ✅ Failure Analysis (plan_011) → Table 15
146	- ✅ Qualitative Examples (plan_012) → Django example in §4.7
147	- ✅ Temperature Ablation (plan_014) → Table 8
148	- ✅ Dynamic vs Static (plan_015) → Table 13
149	- ✅ Bootstrap CIs (plan_016) → Table 3
150	- ✅ Literature Comparison (plan_017) → Table 16
151	- ✅ BM25 Baseline (plan_018) → Table 1
152	- ✅ Pool Size Sensitivity (plan_019) → Table 12
153	
154	Coverage: **15/15 (100%)**. The paper is remarkably comprehensive in executing the experimental plan. The issues are not about missing experiments but about uncontrolled confounds within the executed experiments.
155	
156	### Summary Verdict
157	
158	A thorough and honestly-framed empirical study that asks the right question and provides useful findings — particularly the CoCoHaNeRe BM25-proxy correction and the practical recommendation to use true embedding-distance mining. The ablation suite is exemplary. However, the paper's most novel contribution (structure-grounded negatives) is its weakest empirical result, and several implementation confounds (learnable temperature, pos_weight asymmetry) prevent clean causal attribution. The mechanistic claim (Claim 2) is underpowered at n=2 encoders. With targeted revisions addressing the confounds and reframing the interaction claim, this would be a solid empirical contribution to the code retrieval literature.
159	
160	**Final Consensus: 4/6 (Weak Accept) — conditional on addressing the critical revision items above.**
161	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24a47deb-b809-4068-b002-e1c9939c50da",
  "isSidechain": true,
  "promptId": "a8e5f13c-b79e-4d5f-9dcc-e79744f9ec80",
  "agentId": "a4ff2b13031f226a3",
  "type": "user",
  "uuid": "ec95ea90-c48b-42df-abc4-6fd6b54abbc0",
  "sourceToolAssistantUUID": "24a47deb-b809-4068-b002-e1c9939c50da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T17:08:37.765Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PvYUGtBW4CdCTWptomWsax`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/experiment_data.json",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec95ea90-c48b-42df-abc4-6fd6b54abbc0",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q4u2mqfWhJmdcfruaG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29d22f90-430a-4a41-b0bd-1eb4e38bcf60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116jPcr99qPyQC72CamHKiQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30633,
      "cache_read_input_tokens": 44062,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 30633
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 44062,
          "cache_creation_input_tokens": 30633,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 30633,
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

_source line 35 · 2026-05-14T17:08:37.770Z_

<details><summary>↩ Tool result · `toolu_01PvYUGtBW4CdCTWptomWsax`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29d22f90-430a-4a41-b0bd-1eb4e38bcf60",
  "isSidechain": true,
  "promptId": "a8e5f13c-b79e-4d5f-9dcc-e79744f9ec80",
  "agentId": "a4ff2b13031f226a3",
  "type": "user",
  "uuid": "977ba355-79b5-4e22-aa6d-af01af136f16",
  "sourceToolAssistantUUID": "29d22f90-430a-4a41-b0bd-1eb4e38bcf60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-14T17:08:41.240Z_

Now let me also check what the actual real experiment results look like (vs the imagined ones) and look at the previous dream review for comparison.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "977ba355-79b5-4e22-aa6d-af01af136f16",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q5Rd2rug748LzSZtx1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f5d0942-341e-401c-bbe2-1cb1664cfba9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01USVVAfJr3LcoKMppJdKWGA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5701,
      "cache_read_input_tokens": 74695,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5701,
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

_source line 37 · 2026-05-14T17:08:44.547Z_

<details open><summary>🔧 Tool call — Read · `toolu_01228v2B64cKtwYwNL8fCEnd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f5d0942-341e-401c-bbe2-1cb1664cfba9",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q5Rd2rug748LzSZtx1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73cdb2ac-af83-4143-a6db-881cc4c05927",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01USVVAfJr3LcoKMppJdKWGA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5701,
      "cache_read_input_tokens": 74695,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5701,
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

_source line 38 · 2026-05-14T17:08:44.555Z_

<details><summary>↩ Tool result · `toolu_01228v2B64cKtwYwNL8fCEnd`</summary>

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
101	---
102	
103	## Overall Assessment
104	
105	This paper tackles a genuinely important question -- what makes hard negatives work for code retrieval -- with commendable experimental rigor in its design (9 seeds, bootstrap CIs, extensive ablations). The representation saturation insight, if validated on more encoders, could become a useful diagnostic tool for practitioners. However, the paper is undermined by (a) the N=2 encoder limitation that makes the "representation geometry" theory an observation rather than a validated mechanism, (b) missing baselines (BM25) that are critical to the headline narrative, (c) potential discrepancies between reported results and actual experimental maturity, (d) unrealistic pool sizes that limit external validity, and (e) several reporting gaps (no CIs on RepoBench, no stratification by structural coverage, checkpoint criterion unspecified). The paper is above-average in experimental discipline but below the bar for confident acceptance at a top venue in its current form. Addressing the BM25 baseline, the stratified analysis, and the pool size sensitivity would move it toward acceptance.
106	
107	---
108	
109	## Score: 4 / 6 (Weak Accept)
110	
111	The experimental design is sound in principle and the analytical depth is genuine, but critical baselines are missing, the mechanistic theory is underpowered (N=2), and several reporting gaps weaken trust. A revision addressing the major concerns would likely push this to a 5.
112	
113	## Confidence: 4 / 5 (High)
114	
115	I have expertise in contrastive learning, code retrieval, and hard negative mining. I have closely examined the paper's claims against the available evidence, including internal project artifacts. I am confident in my assessment of the methodological strengths and weaknesses.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73cdb2ac-af83-4143-a6db-881cc4c05927",
  "isSidechain": true,
  "promptId": "a8e5f13c-b79e-4d5f-9dcc-e79744f9ec80",
  "agentId": "a4ff2b13031f226a3",
  "type": "user",
  "uuid": "ad9a0874-cb95-4da5-8153-bbdb65e53ac0",
  "sourceToolAssistantUUID": "73cdb2ac-af83-4143-a6db-881cc4c05927",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T17:08:45.110Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017CiZTZibyC2EA3bjEkjDZz`</summary>

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
  "parentUuid": "ad9a0874-cb95-4da5-8153-bbdb65e53ac0",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q5Rd2rug748LzSZtx1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22f270b4-15cd-470a-b01a-43f53d9ecd02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01USVVAfJr3LcoKMppJdKWGA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5701,
      "cache_read_input_tokens": 74695,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5701,
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

_source line 40 · 2026-05-14T17:08:45.134Z_

<details><summary>↩ Tool result · `toolu_017CiZTZibyC2EA3bjEkjDZz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); heavy inference cost |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | Repository-level Graph for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2025) | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (2025) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献\\n\\n- CodexGraph: arXiv:2408.03910, NAACL 2025\\n- LocAgent: arXiv:2503.09089, ACL 2025\\n- RANGER: arXiv:2509.25257, 2025\\n- RepoGraph: arXiv:2410.14684, ICLR 2025\\n- GraphCoder: arXiv:2406.07003, ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, 2025\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\\n---\\n\\n## BM25 Negative Mining 策略洞察 (2026-05-14)\\n\\n**BM25 vs 其他 negative 策略重叠率**：BM25 与 embedding_distance 重叠 87.1%，与 random 重叠 76.2%，与 dataflow_aware 重叠 71.8%。原因：BM25 和 embedding_distance 都倾向选 lexically/semantically similar 的 hard negatives。小 repo（候选池≤50 文件）中所有策略完全重合（median overlap=1.0），BM25 的差异化主要体现在大 repo。\\n\\n**对 paper framing 的影响**：BM25 ≈ embedding_distance >> random 的模式意味着 Phase 2 训练中 BM25 R@1 很可能接近 embedding_distance。这对论文是 positive signal——审稿人要求的 BM25 baseline 不太可能推翻现有结论，反而支持\\\"hard negative 策略趋同\\\"的观察。如果 BM25 ≈ embedding 且都 > random，说明 hard negative mining（无论用哪种方式）是关键改进因素，而非特定策略的选择。\", \"total_chars\": 8650, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22f270b4-15cd-470a-b01a-43f53d9ecd02",
  "isSidechain": true,
  "promptId": "a8e5f13c-b79e-4d5f-9dcc-e79744f9ec80",
  "agentId": "a4ff2b13031f226a3",
  "type": "user",
  "uuid": "bdca1071-42c4-49cb-afc6-c7f4237e1418",
  "sourceToolAssistantUUID": "22f270b4-15cd-470a-b01a-43f53d9ecd02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-14T17:08:50.452Z_

I now have a thorough understanding of the paper, its experimental design, the evidence base, the internal project history, and the previous dream reviews. Let me also check one critical detail -- the discrepancy between the narrative guidance in review_context.yaml and the actual project state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdca1071-42c4-49cb-afc6-c7f4237e1418",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q5y5diVdHTacpLhEPk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "121af56f-0906-47d6-86c3-92067b262faa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNwiyS64WAoT3Shuvk4kJV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6716,
      "cache_read_input_tokens": 80396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6716,
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

_source line 42 · 2026-05-14T17:08:52.822Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NbXoPHZeAWmNVErhGWsdhp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/imagined_experiments.yaml",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "121af56f-0906-47d6-86c3-92067b262faa",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q5y5diVdHTacpLhEPk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "378cd10f-e843-458e-b96c-676dd5a7344e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNwiyS64WAoT3Shuvk4kJV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6716,
      "cache_read_input_tokens": 80396,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6716
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 179,
          "cache_read_input_tokens": 80396,
          "cache_creation_input_tokens": 6716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6716,
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

_source line 43 · 2026-05-14T17:08:52.828Z_

<details><summary>↩ Tool result · `toolu_01NbXoPHZeAWmNVErhGWsdhp`</summary>

```text
1	tier: best
2	narrative_guidance: '全 18 runs（9 seeds × 2 encoders × 3 strategies）完整复现 pilot pattern。
3	  Embedding mining 在两个 encoder 上均显著优于 random（Qwen +2.0pp, StarCoder +1.5pp, 95% CI
4	  下界 > 0）。 Dataflow 在 Qwen 上条件性获益（+1.0pp, CI 下界 > 0），StarCoder 上无显著差异（-0.2pp, CI 含零）。
5	  BM25 baseline 实证关闭 CoCoHaNeRe 论证（BM25 vs random: Qwen -2.5pp, StarCoder -2.7pp）。
6	  SWE-bench Lite downstream +2.5pp embedding, +3.2pp dataflow resolve rate delta。
7	  三条 claim 原样成立，EMNLP Main 强投 framing 无需调整。 M2 full anchors — Qwen random R@1=0.545,
8	  embedding=0.565, dataflow=0.555; StarCoder random R@1=0.460, embedding=0.475, dataflow=0.458。
9	
10	  '
11	imagined_experiments:
12	- name: SWE-bench Lite End-to-End Evaluation
13	  plan_id: plan_003
14	  description: '3 strategies × best Qwen checkpoint, Qwen3.6-27B agent, 300 SWE-bench
15	    Lite instances. Retriever 提供 top-k context files，agent 生成 patch，评估 resolve rate。
16	
17	    '
18	  expected_results:
19	    random_resolve_rate: 0.22
20	    random_resolved_count: 66
21	    embedding_resolve_rate: 0.245
22	    embedding_resolved_count: 73
23	    dataflow_resolve_rate: 0.252
24	    dataflow_resolved_count: 76
25	    embedding_minus_random_pp: 2.5
26	    dataflow_minus_random_pp: 3.2
27	    dataflow_minus_embedding_pp: 0.7
28	    total_instances: 300
29	    retriever_top_k: 5
30	    agent_model: Qwen3.6-27B
31	  result_rationale: 'Embedding retriever 在 SWE-bench 上提升 +2.5pp，因为 bug-fix patch 通常涉及与
32	    issue 描述 语义相似但非完全匹配的文件——embedding mining 训练使 retriever 更擅长区分"近似但无关" 与"近似且相关"的文件。Dataflow
33	    额外提升 +0.7pp（总 +3.2pp vs random）因为 SWE-bench patch 经常跨函数/跨模块（约 40% 涉及 caller-callee
34	    关系），dataflow negatives 训练使 retriever 理解"调用链上的文件更可能共同出现在 patch 中"。Delta 幅度从 retrieval
35	    R@1 的 +2.0/+1.0pp 放大到下游 resolve rate 的 +2.5/+3.2pp，符合检索质量在端到端任务中 的杠杆效应——正确检索一个关键文件可以使原本完全失败的
36	    patch 变为可解决。 效果幅度在 swebench_resolve_rate_delta_pp [1.5, 4.0] 范围内。
37	
38	    '
39	  tables:
40	  - name: 'Table 4: SWE-bench Lite Resolve Rate'
41	    columns:
42	    - Strategy
43	    - Resolved
44	    - Total
45	    - Rate (%)
46	    - Δ vs Random (pp)
47	    rows:
48	    - - random
49	      - 66
50	      - 300
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "378cd10f-e843-458e-b96c-676dd5a7344e",
  "isSidechain": true,
  "promptId": "a8e5f13c-b79e-4d5f-9dcc-e79744f9ec80",
  "agentId": "a4ff2b13031f226a3",
  "type": "user",
  "uuid": "8c44ed45-271a-4209-a630-75e2028618b5",
  "sourceToolAssistantUUID": "378cd10f-e843-458e-b96c-676dd5a7344e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-14T17:08:57.448Z_

I have now reviewed all necessary materials. Let me now construct and submit the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c44ed45-271a-4209-a630-75e2028618b5",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q6XyoKpajbAo2XGhJC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fa936d2-b7a5-43db-ab2f-c8cf3ca8f45b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PH6LGSF8haKDMdfzeYY1Jk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 87112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1291,
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

_source line 45 · 2026-05-14T17:10:52.358Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_018PcuAmVNpuhK3oHzvATHzP`</summary>

```json
{
  "project": "structfuse-context",
  "tier": "best",
  "dream_id": "dream_20260514T162530",
  "overall_score": "4/6 Weak Accept",
  "report": "---\ndream_id: dream_20260514T162530\ntier: best\nreviewer: R1 (Methods and Experiments)\noverall_score: 4/6 Weak Accept\ntimestamp: 2026-05-14\n---\n\n# R1 Review: Methods and Experiments\n\n**Paper**: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n\n---\n\n## 1. Summary\n\nThis paper presents a systematic empirical comparison of four hard negative mining strategies (random, BM25, embedding-distance, dataflow-disconnected) for contrastive code retrieval, evaluated across two 3B-parameter decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with 9 random seeds each. The central findings are: (1) true embedding-distance mining consistently improves R@1 over random (+2.0pp Qwen, +1.5pp StarCoder), correcting a prior finding from CoCoHaNeRe that conflated BM25-proxy negatives with embedding-distance negatives; (2) BM25 negatives harm both encoders, empirically confirming the artifact; (3) dataflow-disconnected negatives provide conditional benefit on Qwen but not StarCoder, with a representation saturation hypothesis offered as explanation. The paper includes an extensive ablation suite (temperature, pool size, data scaling, hop depth, dynamic vs. static mining, fusion head, weighted vs. binary dataflow) and evaluates on SWE-smith validation, RepoBench-R, and SWE-bench Lite.\n\n---\n\n## 2. Strengths\n\n- **S1: Exemplary statistical discipline.** 54 training runs (2 encoders x 3 strategies x 9 seeds) with bootstrap 95% CIs and explicit p-values for all main comparisons is substantially above community standard. The paired bootstrap design for SWE-bench Lite (10K resamples) is appropriate for the binary outcome variable.\n\n- **S2: Comprehensive and purposeful ablation suite.** Each of the 8 ablations addresses a specific methodological concern or potential confound: temperature regime-specificity (Table 8), pool size artifact (Table 12), static vs. dynamic mining curriculum confound (Table 13), hop depth selection (Table 9), data scaling (Table 10), fusion head isolation (Table 11), weighted vs. binary dataflow (Table 14). This is not ablation padding -- each result answers a genuine question. The dynamic mining ablation is particularly valuable: ruling out the curriculum effect (+0.3pp, non-significant) justifies the practical recommendation to mine once from the pretrained checkpoint.\n\n- **S3: Clean experimental control.** The comparison holds all variables constant (data, encoder, LoRA configuration, training schedule, evaluation protocol) except the negative selection strategy. This is the correct experimental design for isolating a single factor's effect.\n\n- **S4: BM25 baseline closes the CoCoHaNeRe correction empirically.** Including BM25 negatives as a fourth strategy (Table 1) transforms the \"correction\" from an argumentative claim into an empirical demonstration. The 4-strategy ordering BM25 < random < dataflow <= embedding, with BM25 harming both encoders (-2.5pp Qwen, -2.7pp StarCoder), is the paper's most clean-cut contribution.\n\n- **S5: Honest conditional framing.** The paper does not overclaim dataflow benefit as universal. The conditional framing (helps Qwen, not StarCoder; helps when representations are saturated) and the stratified decomposition (true per-instance effect +2.8pp on the 34% with structural data, diluted to +1.0pp overall) demonstrate intellectual honesty. Many papers would suppress the StarCoder null or report only the pooled +1.0pp.\n\n- **S6: Multi-benchmark consistency.** Embedding mining improves both encoders on both SWE-smith and RepoBench-R. The encoder-strategy interaction (dataflow helps Qwen, neutral on StarCoder) replicates across benchmarks. This cross-benchmark stability rules out benchmark-specific artifacts.\n\n- **S7: Pool size sensitivity analysis is thorough.** Testing at pool sizes 50, 100, 200, and 500 with 100% ranking stability and graceful delta degradation (-0.15pp per doubling) demonstrates the findings are not artifacts of unrealistically small pools. Embedding mining maintains +1.5pp at pool=500 for Qwen.\n\n- **S8: SWE-bench Lite evaluation connects retrieval to downstream impact.** The +2.5pp embedding (p=0.018) and +3.2pp dataflow (p=0.008) resolve rate improvements, with bootstrap CIs excluding zero, add practical credibility beyond retrieval-only metrics.\n\n---\n\n## 3. Weaknesses\n\n### Major\n\n- **W1: N=2 encoders is fundamentally insufficient for the \"representation saturation mediates strategy effectiveness\" claim.** The mechanistic story -- that pos_sim saturation (0.986 Qwen vs. 0.799 StarCoder) determines whether dataflow negatives help -- rests on exactly two data points. These two encoders differ in pretraining data, pretraining objective (fill-in-the-middle vs. fill-in-the-middle with different ratios), tokenizer, and model family. Any of these confounds could explain the observed interaction. The paper correctly frames Claim 2 as conditional (\"when encoder representations are saturated\"), but the Discussion section (Section 6) presents the saturation mechanism as explanatory rather than merely correlational. With n=2, any post-hoc explanation fits. The neg_difficulty quartile analysis (Table 7b) is descriptive evidence for the saturation hypothesis but is computed on the same two encoders, not an independent validation. This is the paper's most fundamental limitation and limits the mechanistic claim to hypothesis-generating status.\n\n- **W2: The dataflow strategy is a mixture strategy, not a pure structural signal.** Dataflow negatives are available for only 34% of instances; the remaining 66% fall back to embedding-distance or random selection. The headline comparison in Table 1 (dataflow vs. random) therefore compares \"34% structural + 66% fallback\" against \"100% random.\" The stratified analysis (Table 6) decomposes this correctly (+2.8pp on structural-available, +0.1pp on fallback), but this decomposition should be the primary presentation, not a secondary analysis. More critically, the fallback strategy for the 66% is not clearly specified -- is it embedding-distance mining or random? If the former, the \"dataflow\" condition actually contains a substantial embedding-distance component, making the dataflow-vs-embedding comparison in Table 1 confounded: they share 66% of the same negatives.\n\n- **W3: SWE-bench Lite's statistical power is marginal for the reported claims.** With 300 instances, the bootstrap CIs are ~3.6pp wide. The embedding-vs-random comparison (p=0.018) is significant but borderline; the dataflow-vs-embedding comparison (p=0.134) is not. The paper acknowledges this but then reports Table 3 (SWE-bench complexity breakdown) with sub-group analyses (N=189 single-file, N=111 multi-file) that have even less power. The multi-file dataflow advantage (+5.4pp) is presented as evidence for the dataflow mechanism, but with N=111 and no reported CI or p-value for this sub-group, this is anecdotal evidence dressed up as statistical analysis. The paper should either report CIs for each sub-group or refrain from drawing sub-group conclusions.\n\n- **W4: Effect sizes are small enough that uncontrolled implementation details could explain them.** The headline embedding-vs-random delta is +2.0pp (Qwen) and +1.5pp (StarCoder). These are within the range affected by hyperparameter choices not ablated: number of negatives per query (K, which is never specified in the paper), sequence length truncation, learning rate, weight decay, LoRA target modules. The data scaling ablation (Table 10) shows embedding delta growing from +1.2pp (1K) to +2.0pp (5K) -- the delta at 1K (+1.2pp) is comparable to the seed standard deviation (sigma=1.5), meaning individual seed outcomes at 1K would not be significant. The 5K result is more convincing, but the fact that the delta is still growing suggests we are observing the beginning of a trend, not its convergent value. This creates uncertainty about whether the finding is robust or still regime-dependent on data scale.\n\n- **W5: Checkpoint selection criterion is not specified.** The internal project history (D017) reveals that strategy rankings change depending on whether checkpoints are selected by best validation loss or best R@1. Specifically, for Qwen: by val_loss, embedding > dataflow > random; by peak R@1, dataflow > embedding > random. This is a material design choice that affects the headline claims, yet the paper does not state which criterion is used. If val_loss-selected checkpoints are reported (as seems likely from the main results ordering), the paper should acknowledge that R@1-selected checkpoints would produce different rankings and discuss why val_loss selection is preferred.\n\n### Minor\n\n- **W6: The paper claims \"strategy rankings never reverse across any experimental condition tested\" (Conclusion).** This is an overstatement. Table 12 shows StarCoder dataflow ranking changes from E>R>D (pool=50) to E>R~D (pool=200+). While this is not a reversal of the embedding-vs-random ordering, it represents instability in the dataflow ranking. The claim should be narrowed to \"embedding > random never reverses.\"\n\n- **W7: Number of negatives per query (K) is not stated.** Section 3.1 defines the loss with K negatives but never specifies the value used. The review_context mentions pool_size=50 at training time, but it is unclear whether K=49 (all non-positive files in the pool) or some smaller K. This is a basic reproducibility gap.\n\n- **W8: BM25-embedding overlap of 87%.** The memory.md notes reveal that BM25 and embedding-distance negatives overlap by 87.1%. This high overlap means the BM25 harm (-2.5pp) cannot be cleanly attributed to \"BM25 selects lexically similar files that destroy useful token-overlap signals\" (as the paper argues). If 87% of negatives are identical, the 13% difference in negative composition is driving a 4.5pp R@1 difference, which implies those 13% of negatives have outsized influence. This deserves investigation and reporting: what characterizes the non-overlapping 13%? Are they high-lexical-overlap but low-embedding-similarity files?\n\n- **W9: Overfitting patterns are not reported.** Project logs show train_loss dropping to 0.04 while val_loss remains at 0.52, with best checkpoint at step 1000 out of ~4200 steps (epoch 1 midpoint). This severe overfitting (best at 25% of training) is never discussed. Strategy-specific overfitting dynamics could be informative: does dataflow overfit faster (fewer unique negatives due to 34% coverage)? Does embedding overfit slower (higher negative diversity)?\n\n- **W10: The paper name \"StructFuse\" implies a fusion architecture, but the best-performing approach uses no fusion.** Table 11 shows fusion slightly degrades performance (-0.4pp). The name is misleading for an analysis paper whose main recommendation is \"use embedding-distance mining.\"\n\n- **W11: RepoBench-R pool sizes are imprecise.** \"Pool ~18\" and \"pool ~6\" are stated but the exact evaluation protocol is not described. Are these the natural candidate sets from RepoBench-R, or are they constructed to match the SWE-smith protocol?\n\n---\n\n## 4. Questions for Authors\n\n1. **Checkpoint criterion:** Which checkpoint selection criterion (best-val-loss vs. best-R@1) is used for all main results? Given that D017 shows these criteria produce different strategy rankings, please report results under both criteria or justify the chosen one.\n\n2. **Number of negatives K:** What value of K (negatives per query) is used in training? How does varying K interact with the mining strategy comparison?\n\n3. **Dataflow fallback strategy:** For the 66% of instances without structural data, does the dataflow condition fall back to embedding-distance mining or random sampling? If embedding-distance, then the dataflow-vs-embedding comparison in Table 1 is confounded by shared negatives on 66% of instances.\n\n4. **BM25-embedding overlap:** Given the 87.1% overlap between BM25 and embedding negatives reported in your analysis, how do you explain the 4.5pp performance gap? What characterizes the 13% of non-overlapping negatives that apparently drive this difference?\n\n5. **Learned temperature values:** The training configuration includes a learnable log_temperature parameter. Do the converged temperature values differ systematically across strategies? If so, the temperature ablation (Table 8, which fixes initial temperature) does not fully control for this confound.\n\n6. **Positive weighting confound:** Does the dataflow strategy use a different positive weighting scheme (e.g., pos_weight = exp(-alpha * dataflow_distance)) compared to random and embedding strategies? If so, Table 1 conflates two treatment differences (negative selection + positive weighting).\n\n7. **Overfitting dynamics:** Best checkpoints occur at step 1000 (~25% through training). Do different strategies exhibit different overfitting speeds? Is the strategy ranking stable across checkpoints (e.g., at step 500, 1000, 1500, 2000)?\n\n8. **CoCoHaNeRe evidence:** What specific textual or code-level evidence from CoCoHaNeRe supports the claim that they used BM25 as a proxy for embedding-distance? The strength of Claim 1 depends on the precision of this attribution.\n\n---\n\n## 5. Minor Issues\n\n- Table 10 (data scaling): Sigma is reported as a single number per data size, but it should be reported per strategy. If sigma is pooled across strategies, it obscures whether mining quality reduces seed variance (which would be informative).\n- Table 9 (hop depth ablation): Single seed, Qwen only. The optimal hop depth could differ for StarCoder. At minimum, note this limitation.\n- Table 11 (fusion head ablation): No CIs or p-values. Given the small deltas (-0.4pp, -6.7pp), statistical significance should be reported.\n- The SWE-bench Lite evaluation uses only the Qwen retriever, not StarCoder. This asymmetry should be acknowledged in the Limitations section.\n- The failure analysis (Table 15) is based on 50 instances from the random retriever only. A matched analysis comparing failure modes across strategies (which instances does dataflow rescue that embedding does not?) would be more informative.\n- Section 3.3: \"0% timeout rate\" for CodeQL is stated for 5K instances / 131 repos. Clarify whether this refers to individual query timeout or total repo processing timeout.\n- The abstract states \"+2.0pp R@1 Qwen, +1.5pp StarCoder\" for embedding mining, but Table 1 in the body shows these exact numbers. The abstract should reference CIs or state \"statistically significant\" to distinguish from noise.\n\n---\n\n## 6. Overall Assessment\n\n**Score: 4/6 (Weak Accept)**\n\n**Confidence: 4/5 (High)**\n\nThis paper asks a genuinely important question -- what makes hard negatives work for code retrieval -- and answers it with above-average experimental rigor. The 54-run statistical design with bootstrap CIs, the 4-strategy comparison that empirically closes the CoCoHaNeRe BM25-proxy debate, the multi-benchmark consistency, and the extensive ablation suite represent careful, honest empirical work. The CoCoHaNeRe correction (Claim 1) is the paper's strongest and most useful contribution: the BM25 < random < embedding ordering, validated across two encoders and two benchmarks, is a service to the community.\n\nHowever, several issues prevent confident acceptance:\n\n(a) The mechanistic claim about representation saturation (Claim 2) is hypothesis-generating at best with n=2 encoders. The paper should explicitly reframe this as an observation with a testable prediction, not a validated mechanism.\n\n(b) The dataflow strategy's 34% coverage makes it a mixture condition whose headline effect (+1.0pp) is diluted. The stratified decomposition (+2.8pp on structural-available instances) is more honest but raises the question of practical utility: if 66% of instances receive no structural signal, the practical recommendation simplifies to \"use embedding mining.\"\n\n(c) Effect sizes throughout are small (1.0-2.0pp R@1) and within the range sensitive to uncontrolled implementation details (number of negatives K, checkpoint selection criterion, learnable temperature).\n\n(d) Several reporting gaps -- unspecified K, unspecified checkpoint criterion, unreported overfitting dynamics, unreported learned temperatures -- create unnecessary uncertainty about the robustness of the headline numbers.\n\nThe paper is above-average in execution quality and intellectual honesty, but the combination of small effect sizes, limited encoder diversity (n=2), and unresolved confounds places it at the accept/reject boundary. Addressing items (a) through (d) in revision -- particularly the checkpoint criterion transparency, the K specification, and explicit reframing of Claim 2 as hypothesis -- would likely push this to a 5/6.\n\n**What would change my score:**\n- To 5/6: Specify checkpoint criterion and K; report results under both checkpoint criteria; explicitly reframe Claim 2 as hypothesis; add CIs to sub-group analyses.\n- To 3/6: If the learned temperature values differ systematically across strategies (explaining the R@1 deltas as a temperature artifact rather than a mining quality effect) or if the positive weighting confound is confirmed.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fa936d2-b7a5-43db-ab2f-c8cf3ca8f45b",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2q6XyoKpajbAo2XGhJC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebb30e00-0dab-408c-bf1a-bb9e441e1283",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PH6LGSF8haKDMdfzeYY1Jk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 87112,
      "output_tokens": 4419,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1291
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4419,
          "cache_read_input_tokens": 87112,
          "cache_creation_input_tokens": 1291,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1291,
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

_source line 46 · 2026-05-14T17:10:55.807Z_

<details><summary>↩ Tool result · `toolu_018PcuAmVNpuhK3oHzvATHzP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md\", \"dream_id\": \"dream_20260514T162530\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebb30e00-0dab-408c-bf1a-bb9e441e1283",
  "isSidechain": true,
  "promptId": "a8e5f13c-b79e-4d5f-9dcc-e79744f9ec80",
  "agentId": "a4ff2b13031f226a3",
  "type": "user",
  "uuid": "f607b7f2-36ea-46fa-90cd-5474d6bcb11c",
  "sourceToolAssistantUUID": "ebb30e00-0dab-408c-bf1a-bb9e441e1283",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-14T17:11:22.136Z_

Review submitted. Here is a summary of the review:

**Score: 4/6 (Weak Accept), Confidence: 4/5**

**Key strengths identified:**
- Exemplary statistical discipline (54 training runs, 9 seeds, bootstrap CIs)
- BM25 baseline empirically closes the CoCoHaNeRe correction -- the paper's strongest contribution
- Comprehensive and purposeful ablation suite (8 ablations, each answering a specific methodological question)
- Honest conditional framing of dataflow benefit; transparent reporting of null results
- Multi-benchmark consistency (SWE-smith + RepoBench-R)
- Pool size sensitivity analysis (50-500) showing 100% ranking stability

**Key weaknesses identified:**
- N=2 encoders insufficient for the representation saturation mechanism claim (W1, major)
- Dataflow is a mixture strategy (34% structural + 66% fallback), confounding the headline comparison (W2, major)
- SWE-bench Lite underpowered for sub-group analyses reported without CIs (W3, major)
- Effect sizes small enough (1-2pp) that uncontrolled implementation details could explain them (W4, major)
- Checkpoint selection criterion unspecified despite evidence it changes rankings (W5, major)
- BM25-embedding 87% overlap undermines the "lexical signal destruction" explanation (W8, minor)
- Unreported overfitting dynamics, learnable temperature confound, positive weighting confound (W9, questions 5-6)

**Core assessment:** The paper asks the right question and executes with above-average rigor. Claim 1 (CoCoHaNeRe correction) is clean and useful. Claims 2-3 (dataflow conditional benefit, representation saturation mechanism) are underpowered. Addressable in revision.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f607b7f2-36ea-46fa-90cd-5474d6bcb11c",
  "isSidechain": true,
  "agentId": "a4ff2b13031f226a3",
  "requestId": "req_011Cb2qFbdKcDLPC4BAAGAUb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4dcd6c8a-efc9-4c85-a1fb-490906004bec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1a45356f-658c-4c4f-ba94-f04e8cd4eef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SoxLNnoQguYBvcPqYmE6od",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4545,
      "cache_read_input_tokens": 88403,
      "output_tokens": 432,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4545
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 432,
          "cache_read_input_tokens": 88403,
          "cache_creation_input_tokens": 4545,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4545,
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
