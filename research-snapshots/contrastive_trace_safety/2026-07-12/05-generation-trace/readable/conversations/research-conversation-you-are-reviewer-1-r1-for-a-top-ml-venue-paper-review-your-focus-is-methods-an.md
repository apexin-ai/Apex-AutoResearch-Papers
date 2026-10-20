# Research conversation: You are Reviewer 1 (R1) for a top ML venue paper review. Your focus is **Methods and Experiments**. Review the paper tho

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-afab362b0e39e778a.jsonl`
- **Structured JSON:** [`a725828357d81f12d214.json`](../../sessions/a7/a725828357d81f12d214.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

30 recorded events

### User

_source line 1 · 2026-05-16T16:09:31.141Z_

You are Reviewer 1 (R1) for a top ML venue paper review. Your focus is **Methods and Experiments**. Review the paper thoroughly and produce a structured review.

## Paper Summary

**Title**: "Evaluation Methodology Dominates Mining Strategy: A Systematic Study of Confounds in Contrastive Code Retrieval"

The paper compares 4 negative mining strategies (random, embedding-distance, BM25, dataflow-aware) across 3 encoder architectures (Qwen2.5-Coder-3B, StarCoder2-3B, UniXcoder-base 125M) for contrastive code retrieval trained on SWE-smith (14,100 instances, 131 repos). The central claim is that evaluation methodology choices (pool size, checkpoint criterion, temperature, seed, data size) account for 10-16pp variation in R@1, while the best mining strategy contributes at most 0.4pp — a 40× ratio. Embedding mining shows marginal benefit only on Qwen (+0.40pp, 95% CI: -0.82 to +1.62), null on StarCoder and UniXcoder.

## Key Paper Content

### Methods (Section 3)
- Training: LoRA fine-tuning on SWE-smith, InfoNCE loss, K=7 negatives, τ=0.1 default
- Mining strategies: Random (uniform from non-gold in-repo), Embedding-distance (static top-K by pretrained cosine sim), BM25 (top-K lexical), Dataflow-aware (CodeQL 2-hop, available for 34% instances, rest fallback to random)
- Encoders selected for distinct geometry: Qwen (pos-sim=0.99, margin=0.008), StarCoder (pos-sim=0.80, margin=0.194), UniXcoder (encoder-only, mean pooling)
- Evaluation: R@1 with pool size as explicit parameter. Primary pool=8.

### Main Results
- Table 1 (Qwen): Random mean=0.5697, Embedding mean=0.5737 (+0.40pp), Dataflow mean=0.5598 (-0.99pp). Cross-seed std for random=2.74pp.
- Table 2 (StarCoder): Random mean=0.4787, Embedding mean=0.4781 (-0.06pp), Dataflow mean=0.4700 (-0.87pp).
- Table 3 (BM25): Qwen BM25=0.5700 (+0.03pp vs random), StarCoder BM25=0.4760 (-0.27pp).
- Table 4 (UniXcoder): All strategies within 0.37pp per seed, mean span=0.32pp. Complete null.

### Methodology Confound Decomposition (Table 5)
- Pool size 8→50: 14.2pp, 35×
- Data size 1K→11K: 4.8pp, 12×
- Temperature 0.05→0.20: 3.3pp, 8×
- Seed variance: 2.7pp, 7×
- Checkpoint criterion: 2.7pp, 7×
- Mining strategy (best): 0.4pp, 1×

### Pool Size Sensitivity (Table 6)
- Embed-Random Δ stable (~0.4pp) across pool={8,50,100,200,500}
- Absolute R@1 drops from 0.57 (pool=8) to 0.19 (pool=500)

### Checkpoint Selection (Table 7)
- Best by val_loss: R@1=0.415 at pool=50
- Best by R@1(pool=8): 0.428
- Best by R@1(pool=50): 0.442
- 2.7pp gap from criterion alone

### Temperature Ablation (Table 8)
- τ∈{0.05,0.10,0.20} × {Qwen,StarCoder} × {Random,Embed,Dataflow}
- Qwen: embed-random Δ ranges 0.20-0.86pp across τ
- StarCoder: always negative (-0.10 to -0.37pp)
- Strategy ranking preserved across all τ

### Data Size (Table 9): 1K→11K, random R@1 goes 0.505→0.553, embed Δ goes 1.20→0.86pp

### Dynamic Mining (Table 10): Static vs dynamic: +0.25pp at 3.2× cost

### RepoBench-R (Table 11): Directional consistency for Qwen (+0.4-0.5pp), null for StarCoder, all CIs include zero

### Stratified Analysis (Table 12): Higher neg-difficulty → larger embed benefit (Q1: +0.15pp, Q4: +0.70pp), all CIs include zero

### Statistical Summary (Table 13): All p>0.05, all CIs include zero. Qwen embed-random: Cohen's d=0.18, p=0.26. Power analysis: 12 seeds needed for 80% power at 0.5pp.

### Hop/Fusion (Table 14): Hop 1-3 range 0.3pp. Combined embed+structural: +0.37pp over embed-only.

## Experiment Design Reference (what was planned)

The full experiment plan included 16 experiments. The paper covers:
1. M2 Full Qwen 9-run ✓ (Table 1)
2. M2 Full StarCoder 9-run ✓ (Table 2)
3. BM25 Baseline ✓ (Table 3)
4. Pool Size Sensitivity ✓ (Table 6)
5. Checkpoint Criterion Effect ✓ (Table 7)
6. RepoBench-R ✓ (Table 11)
7. Temperature Ablation (reduced) ✓ (Table 8)
8. Dynamic Mining ✓ (Table 10)
9. UniXcoder Multi-seed ✓ (Table 4)
10. Stratified Analysis ✓ (Table 12)
11. Hop Depth ✓ (Table 14 top)
12. Data Size Scaling ✓ (Table 9)
13. Bootstrap CI ✓ (Table 13)
14. Fusion Head ✓ (Table 14 bottom)

Missing/incomplete from plan:
- Full Temperature Ablation (paper has reduced version, only s42; plan called for all strategies × encoders)
- Dataflow-distance weighted negatives (mentioned in context but not in paper)
- Training data size scaling shows non-monotonic delta at 11K (0.86pp > 0.55pp at 5K) — acknowledged but not explained
- Failure analysis on SWE-bench failures (dropped from paper, only mentioned as RepoBench-R replaces it)
- Qualitative retrieval examples (not in paper)

## Your Review Task

Evaluate:
1. **Experimental design quality**: Controls, confound management, statistical rigor
2. **Methodology soundness**: Are the mining strategies fairly compared? Is the evaluation protocol valid?
3. **Statistical claims**: Are CIs/effect sizes properly computed and interpreted? Is the "underpowered" framing honest or strategic?
4. **Ablation completeness**: Are the ablations sufficient to support the claims?
5. **Reproducibility**: Is enough detail provided?
6. **Weaknesses in experimental design**: Missing controls, confounds not addressed, fairness of comparisons

## Output Format

```
## R1 Review: Methods & Experiments

### Summary
[2-3 sentences]

### Strengths
[Numbered list, 4-6 items]

### Weaknesses
[Numbered list, 4-6 items]

### Questions for Authors
[Numbered list, 3-5 items]

### Minor Issues
[Numbered list]

### Overall Assessment
Score: [1-6 scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept]
Confidence: [1-5: 1=low, 5=expert]
[2-3 sentence justification]
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c3dda3bd-dec5-4061-acb9-820fe469aaa2",
  "agentId": "afab362b0e39e778a",
  "type": "user",
  "uuid": "d1b016df-3d31-4922-8a90-1e5e7312d431",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T16:09:31.146Z_

```json
{
  "parentUuid": "d1b016df-3d31-4922-8a90-1e5e7312d431",
  "isSidechain": true,
  "agentId": "afab362b0e39e778a",
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
  "uuid": "915b64b2-2150-4d5b-92f4-8f62b7dc0e75",
  "timestamp": "2026-05-16T16:09:31.146Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-16T16:09:34.408Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KSy2rf1hbmzERGWK9vn5fx`</summary>

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
  "parentUuid": "915b64b2-2150-4d5b-92f4-8f62b7dc0e75",
  "isSidechain": true,
  "agentId": "afab362b0e39e778a",
  "requestId": "req_011Cb6YBpHztMfT1Jn52oi4z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5cedbc73-2a4d-417b-8273-dc497c353bfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNZXqPUfxEeULEbCcEd6gR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16079,
      "cache_read_input_tokens": 0,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16079
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 88,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16079,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16079,
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

_source line 4 · 2026-05-16T16:09:34.413Z_

<details><summary>↩ Tool result · `toolu_01KSy2rf1hbmzERGWK9vn5fx`</summary>

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
  "parentUuid": "5cedbc73-2a4d-417b-8273-dc497c353bfd",
  "isSidechain": true,
  "promptId": "c3dda3bd-dec5-4061-acb9-820fe469aaa2",
  "agentId": "afab362b0e39e778a",
  "type": "user",
  "uuid": "6b1595da-64d4-44a7-915f-9b4301ace8f6",
  "sourceToolAssistantUUID": "5cedbc73-2a4d-417b-8273-dc497c353bfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T16:09:37.351Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Rz8XhceA3gEKWC6G58s2T2`</summary>

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
  "parentUuid": "6b1595da-64d4-44a7-915f-9b4301ace8f6",
  "isSidechain": true,
  "agentId": "afab362b0e39e778a",
  "requestId": "req_011Cb6YC4PKrNGsNxi91888i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84601926-6ef2-4cfc-99da-5692a903eb66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpcGXJz8PaE4ptbN72paP7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 16079,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1269
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 107,
          "cache_read_input_tokens": 16079,
          "cache_creation_input_tokens": 1269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1269,
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

_source line 6 · 2026-05-16T16:09:37.366Z_

<details><summary>↩ Tool result · `toolu_01Rz8XhceA3gEKWC6G58s2T2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| unixcoder-3strat-s43 | UniXcoder-base s43: 3 strategies (random/embedding/dataflow) × seed 43, patience=2。与 s42 (patience=3) 构成 2-seed 统计，验证 null result 稳定性。Director D064 批准。 | — | — | — |\\n| m2_full_starcoder_resumed | M2 StarCoder resumed: 继续 m2_full_starcoder 的 8 sequential runs (random×2 + embedding×3 + dataflow×3)。原实验因 cron timeout 标记为 failed，实际 PID 519791 正常运行。 | — | — | — |\\n| m2_full_qwen_continued | M2 Qwen continued: 继续 m2_full_qwen 的剩余 runs (random_s44 + embedding×3 + dataflow×3)。原实验 cron 在 s42 退出时自动设为 ANALYZING，但链仍在运行。 | — | — | — |\\n\\n## 待处理\\n- plan_018_bm25: BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。（排队等待 GPU）\\n- plan_015_dynamic: Dynamic negative mining (epoch-level re-mining): 每 epoch 重新用当前 encoder embedding 挖掘 negatives，验证 static mining 是否足够。缩减版：只跑 dynamic_ep × 1 seed (Qwen, s42)，~11h 单卡。若 dynamic ≈ static（预期 <1pp 差异），在 Limitation 段排除 confound。（排队等待 GPU）\\n- plan_005_stratified: Plan 005 分层分析：按 repo size/pool size/query-pos similarity/structural data availability/neg_difficulty quartile 5 维度分层评估 embedding vs random 策略差异，控制 pool_size confound。Claim 2 支撑实验。v2 结果为 ground truth（v1→v2 changelog 见 art_20260514_3008c4）。（准备中）\\n- unixcoder-3strat-s44: UniXcoder-base s44: 3 strategies (random/embedding/dataflow) × seed 44, patience=2。与 s42/s43 构成 3-seed 统计，确认 encoder-only/small-scale null result。Director D064 批准。（准备中）\\n- qwen_random_s42_retrain: Qwen random_s42 重训（统一 regime: 2 epoch + early_stopping_patience=2）。原 s42 用 3 epoch + patience=0 导致 pool=50 R@1 异常低（0.2730 vs s43=0.3138/s44=0.3181），不可纳入 cross-seed 统计。重训后可补完 3-seed comparison。Director 批准方案 B。（准备中）\\n\\n## 近期结论\\n- **unixcoder-3strat-s42** (negative): UniXcoder-base (125M, encoder-only RoBERTa) 第三 encoder: 3 strategies (random/embedding/dataflow) × seed 42。验证 embedding distance mining 优势是否跨架构泛化（encoder-only vs decoder-only）。batch_size=16, max_seq_length=1024, LoRA, gradient-checkpointing。\\n- **unixcoder_3strat_s42** (failed): UniXcoder-base 第三 encoder: 3 strategies (random/embedding/dataflow) × seed 42。验证 embedding distance mining 优势是否跨架构泛化（RoBERTa vs decoder-only）。\\n- **m1_reextract_v2** (success): M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 ← 基于 m1_extraction\\n\\n## 趋势\\n成功 12 / 负向 3 / 失败 5 / 共 34\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-42106: 无 GPU 信息\\n\\n## 告警\\n- p2b-smoke-test: 已被终止 — unknown\\n- p2b-smoke2: 已被终止 — unknown\\n- p2b-smoke3: 已被终止 — unknown\\n- p2b-smoke4: 已被终止 — unknown\\n- p2b-smoke5: 已被终止 — unknown\\n- p2b-smoke6: 已被终止 — unknown\\n- p2b-smoke7: 已被终止 — unknown\\n- p2b-smoke8: 已被终止 — unknown\\n- p2b-all-9runs: 已被终止 — unknown\\n- mvp_p2b_contrastive_training: 已被终止 — unknown\\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\\n- p2b_eval_all: 已被终止 — unknown\\n- m2_early_pilot: 已被终止 — unknown\\n- m2_early_pilot_v2: 训练失败 — unknown\\n- m2_early_pilot_v3: 已被终止 — unknown\\n- m2_full_starcoder: 训练失败 — unknown\\n- m1_reextract: 训练失败 — unknown\\n- plan_003_swebench_eval: 训练失败 — unknown\\n- unixcoder_3strat_s42: 训练失败 — unknown\\n\", \"total_chars\": 3264, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84601926-6ef2-4cfc-99da-5692a903eb66",
  "isSidechain": true,
  "promptId": "c3dda3bd-dec5-4061-acb9-820fe469aaa2",
  "agentId": "afab362b0e39e778a",
  "type": "user",
  "uuid": "3ca423d5-1332-4c74-aacd-b18f30a951e5",
  "sourceToolAssistantUUID": "84601926-6ef2-4cfc-99da-5692a903eb66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T16:09:40.790Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019v1eMi1B64CWPio9Aw5RUp`</summary>

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
  "parentUuid": "3ca423d5-1332-4c74-aacd-b18f30a951e5",
  "isSidechain": true,
  "agentId": "afab362b0e39e778a",
  "requestId": "req_011Cb6YCH3pguZanrwT3ZFn7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87af2dc0-a5ac-4241-87ee-c2267f8b58d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NvnGqgSG5r44zCB3hhomA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2004,
      "cache_read_input_tokens": 17348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2004,
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

_source line 8 · 2026-05-16T16:09:40.808Z_

<details><summary>↩ Tool result · `toolu_019v1eMi1B64CWPio9Aw5RUp`</summary>

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
  "parentUuid": "87af2dc0-a5ac-4241-87ee-c2267f8b58d5",
  "isSidechain": true,
  "promptId": "c3dda3bd-dec5-4061-acb9-820fe469aaa2",
  "agentId": "afab362b0e39e778a",
  "type": "user",
  "uuid": "1b7df91f-241f-4d2a-82ba-0a523318abe8",
  "sourceToolAssistantUUID": "87af2dc0-a5ac-4241-87ee-c2267f8b58d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T16:09:40.890Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FY8Jq7njrhCX68gX1PhhMH`</summary>

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
  "parentUuid": "1b7df91f-241f-4d2a-82ba-0a523318abe8",
  "isSidechain": true,
  "agentId": "afab362b0e39e778a",
  "requestId": "req_011Cb6YCH3pguZanrwT3ZFn7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e11c0271-04fb-4a87-b864-6faf0f18e4b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NvnGqgSG5r44zCB3hhomA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2004,
      "cache_read_input_tokens": 17348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2004,
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

_source line 10 · 2026-05-16T16:09:40.900Z_

<details><summary>↩ Tool result · `toolu_01FY8Jq7njrhCX68gX1PhhMH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\\n\\n- **Headline result template**: \\\"Simple static embedding-distance mining improves code retrieval in pilot and initial M2 seed (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; consistency across remaining seeds pending; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective.\\\"\\n\\n## Core Insight\\n\\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval\\\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\\n- Backup: \\\"Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### Evidence presentation strategy:\\n- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)\\n- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)\\n- Both metrics show directionally consistent results; no goalpost-moving between metrics\\n\\n### In progress:\\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 DONE (R@1=0.6009, early stopped step 500), embedding_distance_s43 DONE (R@1=0.5606, early stopped step 1500). 4/9 runs complete, ~35h remaining.\\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\\n- m1_reextract_v2: 90.5% complete (25,582/28,276), 0 ERROR, ETA ~19:00 CST May 15\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Limitations\\n\\nEffect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"Simple embedding mining provides reliable zero-cost improvement + CodeQL extraction is practical + representation geometry analysis may help explain prior contradictions\\\"\\n- Still publishable: reliable zero-cost baseline demonstration + mechanistic analysis is sufficient for EMNLP Main\\n\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the narrative positioning needs adjustment\\n- Pivot: \\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps, establishing it as a reliable zero-cost baseline even when BM25 provides no signal\\\"\\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining provides reliable improvement) stands regardless of BM25 outcome\\n- Claim 1 core preserved: \\\"Simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling\\\"\\n- Impact: BM25 result determines narrative nuance, not core contribution\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\\n&lt;!-- D041 formal definition fix: reachable_G → ¬reachable_G, 2026-05-15 -->\\n&lt;!-- Claim 2 exploratory wording unification: 2026-05-15 -->\\n&lt;!-- D049 Claim 1 framing update: numbers, narrative softening, evidence strategy, limitations: 2026-05-15 -->\\n&lt;!-- Status data refresh: s44 DONE, 4/9 runs, m1 90.5%, headline caveat: 2026-05-15 -->\\n\", \"total_chars\": 14424, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e11c0271-04fb-4a87-b864-6faf0f18e4b2",
  "isSidechain": true,
  "promptId": "c3dda3bd-dec5-4061-acb9-820fe469aaa2",
  "agentId": "afab362b0e39e778a",
  "type": "user",
  "uuid": "60678f6d-1575-4151-a2d6-2f52429ee50c",
  "sourceToolAssistantUUID": "e11c0271-04fb-4a87-b864-6faf0f18e4b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T16:09:45.524Z_

<details open><summary>🔧 Tool call — Read · `toolu_014RCUKEGFaZnLUGsEWmTkiU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60678f6d-1575-4151-a2d6-2f52429ee50c",
  "isSidechain": true,
  "agentId": "afab362b0e39e778a",
  "requestId": "req_011Cb6YCYD9SSpnY1tbSeYnT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "130489f9-fa02-4452-ae14-88092c2b3bb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GRzXMaP7k5GWASFLpeDw2t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4720,
      "cache_read_input_tokens": 19352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4720,
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

_source line 12 · 2026-05-16T16:09:45.532Z_

<details><summary>↩ Tool result · `toolu_014RCUKEGFaZnLUGsEWmTkiU`</summary>

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
  "parentUuid": "130489f9-fa02-4452-ae14-88092c2b3bb1",
  "isSidechain": true,
  "promptId": "c3dda3bd-dec5-4061-acb9-820fe469aaa2",
  "agentId": "afab362b0e39e778a",
  "type": "user",
  "uuid": "221cf994-3501-4608-8f78-a80db33837e5",
  "sourceToolAssistantUUID": "130489f9-fa02-4452-ae14-88092c2b3bb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T16:09:45.693Z_

<details open><summary>🔧 Tool call — Read · `toolu_013gbwPmDTf2XqZBWahMoCtF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "221cf994-3501-4608-8f78-a80db33837e5",
  "isSidechain": true,
  "agentId": "afab362b0e39e778a",
  "requestId": "req_011Cb6YCYD9SSpnY1tbSeYnT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4994f614-6b7b-4d99-a0fe-096dff76417c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GRzXMaP7k5GWASFLpeDw2t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4720,
      "cache_read_input_tokens": 19352,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4720
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 19352,
          "cache_creation_input_tokens": 4720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4720,
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

_source line 14 · 2026-05-16T16:09:45.698Z_

<details><summary>↩ Tool result · `toolu_013gbwPmDTf2XqZBWahMoCtF`</summary>

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
101	This protocol inflates absolute R@1 and compresses inter-strategy differences: when all strategies are evaluated on the same easy pool, small improvements are masked by ceiling effects.
102	
103	We introduce a \emph{query-split} evaluation protocol that addresses these limitations.
104	The key design choice is to hold out a separate set of queries---never seen during training---and evaluate at realistic pool sizes.
105	Formally, let $\mathcal{Q}_{\text{train}}$ and $\mathcal{Q}_{\text{eval}}$ denote disjoint query sets obtained by stratified splitting at the repository level.
106	For each $q \in \mathcal{Q}_{\text{eval}}$, we construct evaluation pools at sizes $\{50, 200, 500\}$ by sampling from all non-gold files in the query's repository, then rank by encoder cosine similarity.
107	
108	This protocol reveals two effects that standard evaluation obscures:
109	
110	\paragraph{Checkpoint selection criterion effect.}
111	For each trained model, we evaluate both $\theta^*_{\text{loss}}$ (best by validation loss) and $\theta^*_{\text{R@1}}$ (best by validation R@1) on the held-out query set.
112	In preliminary results (\placeholder{6/14} evaluations complete), the criterion effect---the R@1 difference between $\theta^*_{\text{R@1}}$ and $\theta^*_{\text{loss}}$ for the same strategy---averages \placeholder{+16.3pp}, substantially exceeding the strategy effect (R@1 difference between strategies under the same criterion).
113	This finding motivates explicit reporting of checkpoint selection criteria in contrastive retrieval evaluation.
114	
115	\paragraph{Pool size interaction.}
116	At pool size 50, strategy differences are compressed because most negatives are trivially distinguishable.
117	At pool sizes 200--500, the proportion of challenging negatives increases, potentially amplifying strategy effects.
118	We evaluate at multiple pool sizes to characterize this interaction.
119	
120	The query-split evaluation set consists of \placeholder{504} held-out queries across \placeholder{N} repositories.
121	We report bootstrap 95\% confidence intervals computed over query-level binary outcomes (hit/miss at rank 1).
122	
123	%==============================================================================
124	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4994f614-6b7b-4d99-a0fe-096dff76417c",
  "isSidechain": true,
  "promptId": "c3dda3bd-dec5-4061-acb9-820fe469aaa2",
  "agentId": "afab362b0e39e778a",
  "type": "user",
  "uuid": "7a6463d3-de72-40a9-9150-caaee728dfe7",
  "sourceToolAssistantUUID": "4994f614-6b7b-4d99-a0fe-096dff76417c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T16:09:50.045Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HjyhKXHdhBGGfD42PkXutu`</summary>

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
  "parentUuid": "7a6463d3-de72-40a9-9150-caaee728dfe7",
  "isSidechain": true,
  "agentId": "afab362b0e39e778a",
  "requestId": "req_011Cb6YCtiS7rKDyqzi3SMmG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b11b7937-7f32-4334-b70b-9ebf0d68fd52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CuLW8Yhz63S2NAqPmpV3YG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7072,
      "cache_read_input_tokens": 24072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7072,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 16 · 2026-05-16T16:09:50.051Z_

<details><summary>↩ Tool result · `toolu_01HjyhKXHdhBGGfD42PkXutu`</summary>

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
  "parentUuid": "b11b7937-7f32-4334-b70b-9ebf0d68fd52",
  "isSidechain": true,
  "promptId": "c3dda3bd-dec5-4061-acb9-820fe469aaa2",
  "agentId": "afab362b0e39e778a",
  "type": "user",
  "uuid": "a01551e2-f800-4919-b4ce-d1e6c7407bb5",
  "sourceToolAssistantUUID": "b11b7937-7f32-4334-b70b-9ebf0d68fd52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T16:09:50.483Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NRD2ad2oLYxy3yZ4zxQR7Z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a01551e2-f800-4919-b4ce-d1e6c7407bb5",
  "isSidechain": true,
  "agentId": "afab362b0e39e778a",
  "requestId": "req_011Cb6YCtiS7rKDyqzi3SMmG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "433a5dfc-b589-4641-9acd-b3c76e01d588",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CuLW8Yhz63S2NAqPmpV3YG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7072,
      "cache_read_input_tokens": 24072,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7072
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 24072,
          "cache_creation_input_tokens": 7072,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7072,
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

_source line 18 · 2026-05-16T16:09:50.493Z_

<details><summary>↩ Tool result · `toolu_01NRD2ad2oLYxy3yZ4zxQR7Z`</summary>

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
  "parentUuid": "433a5dfc-b589-4641-9acd-b3c76e01d588",
  "isSidechain": true,
  "promptId": "c3dda3bd-dec5-4061-acb9-820fe469aaa2",
  "agentId": "afab362b0e39e778a",
  "type": "user",
  "uuid": "06a8ec4b-31c3-4326-9db3-063e8c1eae22",
  "sourceToolAssistantUUID": "433a5dfc-b589-4641-9acd-b3c76e01d588",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T16:09:54.166Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01A5nz9mvreAaU2MjECmjtoe`</summary>

```json
{
  "pattern": "**/dream_20260516*/best/paper.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06a8ec4b-31c3-4326-9db3-063e8c1eae22",
  "isSidechain": true,
  "agentId": "afab362b0e39e778a",
  "requestId": "req_011Cb6YDFFwwrt9ZympbyQ2U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d28d94ce-631f-4d48-a427-80c94fd95749",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jjym54qPtLsrgDHSpsSDac",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3323,
      "cache_read_input_tokens": 31144,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3323
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 31144,
          "cache_creation_input_tokens": 3323,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3323,
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

_source line 20 · 2026-05-16T16:09:54.177Z_

<details><summary>↩ Tool result · `toolu_01A5nz9mvreAaU2MjECmjtoe`</summary>

```text
artifacts/dream_reports/dream_20260516T150348/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d28d94ce-631f-4d48-a427-80c94fd95749",
  "isSidechain": true,
  "promptId": "c3dda3bd-dec5-4061-acb9-820fe469aaa2",
  "agentId": "afab362b0e39e778a",
  "type": "user",
  "uuid": "9a704656-8bc6-4e1e-a845-a56687199572",
  "sourceToolAssistantUUID": "d28d94ce-631f-4d48-a427-80c94fd95749",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T16:09:57.171Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P8CPvEHC6VDBrnDKjH97gi`</summary>

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
  "parentUuid": "9a704656-8bc6-4e1e-a845-a56687199572",
  "isSidechain": true,
  "agentId": "afab362b0e39e778a",
  "requestId": "req_011Cb6YDX2Uqtp9j7dyYcTNo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f3cb9f5-6fc0-4f27-9750-fdd930df8301",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016p6koU6hkzmRBE2Q6yc1Jw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 141,
      "cache_read_input_tokens": 34467,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 141
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 100,
          "cache_read_input_tokens": 34467,
          "cache_creation_input_tokens": 141,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 141,
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

_source line 22 · 2026-05-16T16:09:57.527Z_

<details><summary>↩ Tool result · `toolu_01P8CPvEHC6VDBrnDKjH97gi`</summary>

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
  "parentUuid": "3f3cb9f5-6fc0-4f27-9750-fdd930df8301",
  "isSidechain": true,
  "promptId": "c3dda3bd-dec5-4061-acb9-820fe469aaa2",
  "agentId": "afab362b0e39e778a",
  "type": "user",
  "uuid": "c442620b-2b64-4df0-8d32-f0109868c794",
  "sourceToolAssistantUUID": "3f3cb9f5-6fc0-4f27-9750-fdd930df8301",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-16T16:10:01.223Z_

Now I have sufficient information to produce a thorough review. Let me also check the actual experimental results that are referenced in the task description to cross-reference against the dream paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c442620b-2b64-4df0-8d32-f0109868c794",
  "isSidechain": true,
  "agentId": "afab362b0e39e778a",
  "requestId": "req_011Cb6YDm4acbbR7NBrkvfnJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a6cd06a-b30b-4f8a-b2cf-58ebe7d7a4f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HgwFPU2EqZjJQvorZ5HQn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10933,
      "cache_read_input_tokens": 34608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10933,
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

_source line 24 · 2026-05-16T16:10:04.175Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01VfXhy3yPeAFZPEAGBpwjct`</summary>

```json
{
  "pattern": "**/decisions.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a6cd06a-b30b-4f8a-b2cf-58ebe7d7a4f9",
  "isSidechain": true,
  "agentId": "afab362b0e39e778a",
  "requestId": "req_011Cb6YDm4acbbR7NBrkvfnJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5672e35f-8d59-4b21-9217-2215dd221e43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HgwFPU2EqZjJQvorZ5HQn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10933,
      "cache_read_input_tokens": 34608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10933,
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

_source line 25 · 2026-05-16T16:10:04.192Z_

<details><summary>↩ Tool result · `toolu_01VfXhy3yPeAFZPEAGBpwjct`</summary>

```text
decisions.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5672e35f-8d59-4b21-9217-2215dd221e43",
  "isSidechain": true,
  "promptId": "c3dda3bd-dec5-4061-acb9-820fe469aaa2",
  "agentId": "afab362b0e39e778a",
  "type": "user",
  "uuid": "b31fbdc1-b5e6-4887-89b0-9998916c1ca7",
  "sourceToolAssistantUUID": "5672e35f-8d59-4b21-9217-2215dd221e43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-16T16:10:04.620Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KykkXd9e9dmWSFM8THK72F`</summary>

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
  "parentUuid": "b31fbdc1-b5e6-4887-89b0-9998916c1ca7",
  "isSidechain": true,
  "agentId": "afab362b0e39e778a",
  "requestId": "req_011Cb6YDm4acbbR7NBrkvfnJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "864e7475-a709-4f4b-9127-8b336a7832bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HgwFPU2EqZjJQvorZ5HQn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10933,
      "cache_read_input_tokens": 34608,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10933
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 226,
          "cache_read_input_tokens": 34608,
          "cache_creation_input_tokens": 10933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10933,
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

_source line 27 · 2026-05-16T16:10:04.631Z_

<details><summary>↩ Tool result · `toolu_01KykkXd9e9dmWSFM8THK72F`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "864e7475-a709-4f4b-9127-8b336a7832bb",
  "isSidechain": true,
  "promptId": "c3dda3bd-dec5-4061-acb9-820fe469aaa2",
  "agentId": "afab362b0e39e778a",
  "type": "user",
  "uuid": "d8dedb2a-70be-4494-b541-e1f1d894f7d1",
  "sourceToolAssistantUUID": "864e7475-a709-4f4b-9127-8b336a7832bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-16T16:10:07.361Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01W8ZvdBrdNsu8deYHpJuzDu`</summary>

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
  "parentUuid": "d8dedb2a-70be-4494-b541-e1f1d894f7d1",
  "isSidechain": true,
  "agentId": "afab362b0e39e778a",
  "requestId": "req_011Cb6YEHccGNA1HYzdbFQQW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be5a73c5-e424-4c1b-b341-8390b95ccad4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016R3UkJEnGmFtxcz8vqky7i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 346,
      "cache_read_input_tokens": 45541,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 346
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 45541,
          "cache_creation_input_tokens": 346,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 346,
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

_source line 29 · 2026-05-16T16:10:07.396Z_

<details><summary>↩ Tool result · `toolu_01W8ZvdBrdNsu8deYHpJuzDu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2026), Seddik & Fard | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (Shah et al., 2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (Seddik & Fard, 2026) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献（全部已验证 2026-05-14）\\n\\n- CodexGraph: arXiv:2408.03910, Liu et al., NAACL 2025\\n- LocAgent: arXiv:2503.09089, Chen et al., ACL 2025\\n- RANGER: arXiv:2509.25257, Shah et al., 2025 ✅ verified\\n- RepoGraph: arXiv:2410.14684, Ouyang et al., ICLR 2025\\n- GraphCoder: arXiv:2406.07003, Liu et al., ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, Seddik & Fard, 2026 ✅ verified (full title: \\\"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair\\\")\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\\n---\\n\\n## D062 Checkpoint Criterion 效应（pool=50 独立验证, 2026-05-16）\\n\\n**重大发现**：D062 query split eval 的早期数据（random strategy, selection set 504q, pool=50）显示 checkpoint 选择标准对 R@1 的影响远超预期。\\n\\n| Seed | best_by_val_loss R@1 | best_by_recall_at_1 R@1 | Δ |\\n|------|---------------------|------------------------|---|\\n| s42 | 0.2302 | 0.2302 | 0pp (same ckpt, MD5 identical) |\\n| s43 | 0.3413 | **0.5040** | **+16.3pp** |\\n| s44 | 0.3532 | (pending) | — |\\n\\n**关键洞察**：\\n1. s43 的 criterion 差异 (+16.3pp) **远大于**任何 strategy 差异（之前最大观测 ~5pp）。Checkpoint 选择标准是 confound 的主要来源，不是 mining strategy。\\n2. 这直接验证了 D062 query split 方法论的必要性——必须用独立 selection set 选 checkpoint，否则 criterion 偏差会淹没 strategy 效应。\\n3. 之前 (2026-05-15) 基于 in-training eval (pool=8) 的 criterion 分析显示 mean delta 仅 +0.65pp，严重低估了真实效应。pool=50 独立 eval 揭示的 +16.3pp 说明 pool=8 噪声完全掩盖了 criterion 效应。\\n4. **论文影响**：D062 结果可能成为方法论贡献的一部分（checkpoint selection methodology），而不仅是消除 confound 的工具。\\n\\n**待补充**：embedding_distance 和 dataflow_aware 的 criterion 效应数据（D062 eval 6/14 完成中）。\\n\\n---\\n\\n## Checkpoint Criterion 与 K 分析 (2026-05-15)\\n\\n**Checkpoint 选择 criterion 分歧率**：4 个完成的 full M2 runs 中，2/4 (50%) val_loss 与 R@1 选中不同 checkpoint。\\n\\n**分歧 pattern**：\\n- Qwen s43: val_loss→step 500, R@1→step 1500, R@1 差 +1.97pp\\n- StarCoder s42: val_loss→step 1000, R@1→step 2500, R@1 差 +0.64pp\\n- Mean delta: +0.65pp (R@1 criterion 优于 val_loss criterion)\\n- StarCoder 步差更大（1500 步 vs 1000 步），与其 pretrained margin 更大的特性一致\\n\\n**论文写作决策**：主表报 best_by_R@1（target metric aligned），ablation 表展示两种 criterion 对比（D036 已决策 R@1 为 primary）。\\n\\n**K=7 无 ablation**：所有正式实验固定 K=7。合理性来源：(1) batch_size=8 对齐（1 positive + 7 negatives = 8）(2) DPR 等文献惯例 (3) K=7 negatives are randomly sampled from a pool of 50 strategy-specific candidates per query。K 敏感性列为 limitation/future work。\\n\\n---\\n\\n## In-Training Eval 噪声发现 (2026-05-16)\\n\\n**发现**：in-training eval R@1 有 **±0.5pp 噪声地板**，来源于 val set negative 随机采样。\\n\\n**根因**（代码审计确认）：\\n- `val_ds.__getitem__` 中 `random.shuffle(fallback)` 动态采样 negatives（train.py:109-110）\\n- `val_ds._negatives` 从未被填充（`refresh_negatives` 仅对 train_ds 调用）\\n- 全局 `random` 状态在训练中持续变化，每次 eval pass 的 negative 组合不同\\n- dataloader `shuffle=False`，问题不在 batch 顺序，在 negative 采样\\n\\n**证据**：embed_s43 同一模型权重（step 1500）两次 eval：R@1=0.5606 (periodic) vs 0.5655 (final) = 0.49pp 差异。val_loss 同理：0.4926 vs 0.4876。\\n\\n**影响**：\\n1. Claim 1 的 strategy delta（2-seed mean ≈ 0, 单 seed -0.67 ~ +0.52pp）与噪声**同量级**\\n2. in-training eval 不能可靠区分 strategies\\n3. **pool=50 post-hoc eval（negatives 预定义、确定性）是唯一可靠对比基础**\\n4. 论文不应基于 in-training eval 数值做 strategy ranking claim\\n\\n**修复建议**：eval 时固定 seed 或预写死 val negatives。当前已跑实验不需重跑（pool=50 re-eval 会修复）。\\n\\n---\\n\\n## UniXcoder Null Result (2026-05-16)\\n\\n**发现**：UniXcoder-base (125M, encoder-only RoBERTa) 3 strategies × seed 42，strategy differentiation 完全消失。\\n\\n| Strategy | R@1 (pool=8) | val_loss |\\n|----------|-------------|----------|\\n| random | 0.5534 | 0.4513 |\\n| embedding | 0.5497 | 0.4466 |\\n| dataflow | 0.5510 | 0.4628 |\\n\\nR@1 span 仅 0.37pp，三策略在噪声范围内无差异。\\n\\n**解释假设**：\\n1. **Model capacity**: 125M 参数可能不足以利用 hard negative 的细粒度结构信息。大模型 (3B Qwen/StarCoder) 有更多参数来编码 structural 差异。\\n2. **Representation space**: UniXcoder 的 pretrained representation 可能已经更 uniform（RoBERTa-based encoder vs decoder-only），hard negative 的 \\\"hardness\\\" 在其表征空间中差异更小。\\n3. **Training dynamics**: batch_size=16 + max_seq_length=1024（vs Qwen/StarCoder 的 batch=8 + seq=2048），可能改变了 InfoNCE loss 的梯度结构。\\n\\n**论文定位**：3 encoder × 3 seed 实验中，null only on encoder-only/small-scale → \\\"strategy differentiation is model-capacity dependent\\\"，支撑 Track A (stratified heterogeneity)。s43/s44 已启动，用于 3-seed 统计确认。\\n\\n**Regime 差异**：s42 patience=3, s43/s44 patience=2。Paper 中需标注。\\n\\n---\\n\\n## BM25 Negative Mining 策略洞察 (2026-05-14, updated)\\n\\n**两层重叠率数据（注意区分）**：\\n- **k=50 全候选重叠**（mining worker 报告）：BM25 vs embedding 87.1%, vs random 76.2%, vs dataflow 71.8%\\n- **top-7 Jaccard**（训练实际用的 num_negatives=7，分层分析）：差异远大于全候选\\n\\n**分层 top-7 Jaccard 重叠率**（seed 42, 2920 matched queries / 12290 total）：\\n| 层级 | BM25 vs Embedding | BM25 vs Random | BM25 vs Dataflow |\\n|------|-------------------|----------------|------------------|\\n| Small (<50 files, 39 repos) | 0.668 | 0.411 | 0.667 |\\n| Medium (50-200, 29 repos) | 0.380 | 0.067 | 0.363 |\\n| Large (200+, 15 repos) | 0.297 | 0.007 | 0.405 |\\n\\n**核心修正**：之前基于 87% 预测\\\"Phase 2 中 BM25 R@1 很可能接近 embedding\\\"——这个预测可能不成立。在中大 repo（训练数据主体）上 top-7 Jaccard 仅 30-38%，BM25 和 embedding 选出的训练 negatives 大部分不同。Phase 2 训练结果将真正区分两种策略。\\n\\n**意外发现**：BM25 vs dataflow 在大 repo 上重叠率（0.405）高于 vs embedding（0.297）。词汇相似性信号与数据流依赖有部分对齐，而纯 embedding 距离选择了不同维度的 hard negatives。\\n\\n---\\n\\n## hard_negative_mining.py vs build_m1_training_data.py 实现差异 [2026-05-15]\\n\\n**发现者**：Reviewer\\n**影响**：当前 M2 不受影响（用 pre-mined 数据），plan_015（dynamic negative mining）实施前必须对齐\\n\\n**差异**：\\n\\n### hard_negative_mining.py `DataFlowAwareMiner`（training/hard_negative_mining.py）\\n三步法：\\n1. **Embedding top-K**：调用 `EmbeddingDistanceMiner.mine()` 获取 top-50 cosine similarity 最高的 candidates（从所有 non-positive candidates 中）\\n2. **Dataflow filter**：过滤掉 `_is_reachable(query, fid)` 为 True 的文件——仅检查 `dataflow_graph[src]` 中的直接条目（1-hop 可达性）\\n3. **BM25 re-rank**：如果 `bm25_index` 可用，对剩余 disconnected candidates 按 BM25 分数降序重排\\n4. **Fallback**：如果 disconnected 不足 `num_negatives`，用 random padding 补足\\n\\n### build_m1_training_data.py `build_candidate_pools()`（scripts/build_m1_training_data.py）\\n两步法：\\n1. **Dataflow filter**：从 `non_pos_files` 中排除 `full_connected_set`（= `positive_files ∪ cg_connected`，即 dataflow 直连 + call graph 邻居——比 `DataFlowAwareMiner` 排除范围更广）\\n2. **BM25 sort**：对 disconnected 文件按 BM25 分数降序排序，取 top-K（pool_size=50）\\n3. **无 embedding 步骤**：dataflow pool 完全不使用 embedding 信号\\n\\n额外注意：当 `--model-path` 未提供时，`emb_scores = bm25`（line 317-318），此时 embedding pool 也退化为 BM25 排序，仅在是否排除 `full_connected` 上与 dataflow pool 不同。\\n\\n### 差异总结\\n\\n| 维度 | hard_negative_mining.py | build_m1_training_data.py |\\n|------|------------------------|--------------------------|\\n| Candidate 初筛 | Embedding cosine top-50 | 全部 non-positive（无初筛） |\\n| Dataflow 排除范围 | `dataflow_graph[src]` 直接条目 | `positive_files ∪ cg_connected`（更广） |\\n| 排序信号 | Embedding 为主 → BM25 re-rank | 纯 BM25 排序 |\\n| Embedding 角色 | 主选择器（决定候选池） | 不参与 dataflow pool |\\n| BM25 角色 | 可选的 re-ranker | 唯一排序信号 |\\n\\n### 对齐建议\\nplan_015 实施 dynamic negative mining 时需统一为一种逻辑。建议：\\n1. **排除范围统一**：采用 `build_m1_training_data.py` 的 `full_connected`（dataflow + call graph），因为 call graph 邻居也不应作为 hard negatives\\n2. **选择信号**：dynamic mining 应使用当前 epoch 的 encoder embedding（不是 pretrained），这是 dynamic mining 的核心价值——所以 `DataFlowAwareMiner` 的 embedding→filter→BM25 三步法更合理，但需将排除范围从 1-hop dataflow 扩展到 full_connected\\n3. **具体改动**：修改 `DataFlowAwareMiner._is_reachable()` 使其也排除 call graph 连接，或在 `mine()` 中接受 `full_connected_set` 参数\\n\\n---\\n\\n## SWE-bench eval 脚本路径 [2026-05-15, Reviewer 纠正]\\n\\neval_swebench 脚本已存在（之前 Worker 搜索了错误目录 /root/structfuse）：\\n- `/root/structfuse-context/evaluation/eval_swebench.py`（含 .bak 和 .pyc）\\n- `/root/structfuse-context/scripts/eval_swebench_e2e.py`\\n\\nAgent 通过 OpenAI-compatible API 调用（非本地推理），配置项：STRUCTFUSE_LLM_BACKEND=api, STRUCTFUSE_LLM_API_BASE, STRUCTFUSE_LLM_API_KEY, STRUCTFUSE_LLM_MODEL。Retriever 和 agent 分离，单卡 VRAM 无压力。plan_003 基于现有脚本执行，不需要从头创建。\\n\\n---\\n\\n## Qwen 链日志缓冲问题 [2026-05-15, Reviewer 发现]\\n\\nQwen 链脚本用 `python`（有 stdout 缓冲），导致日志延迟输出，监控出现盲区。StarCoder 链用了 `python -u` 没此问题。**后续 Qwen subrun 启动时须加 `PYTHONUNBUFFERED=1` 环境变量或 `python -u`**，保证日志实时输出。当前 run 不需要重启。\\n\\n---\\n\\n## 运维经验 (2026-05-14)\\n\\n**Registry 状态机 workaround**：当长链训练（多 run 串行）中途因 cron timeout 或子进程退出导致 registry 状态误标（DONE/failed 或 ANALYZING），而实际训练仍在跑时，不可回退状态。解决方案：创建 `{exp_id}_resumed` / `{exp_id}_continued` 新 entry，步进 PREPARING→QUEUED→ALLOCATED→RUNNING，注册 cron 监控实际 PID。原 entry 保留历史 metrics。\\n\\n**Bash 预读陷阱**：运行中的 bash 脚本已将循环体/数组预读到内存，磁盘上修改脚本文件不影响执行。需要在链外设置独立 tmux watcher 监控链 PID 退出后手动触发后续任务。\\n\\n**BM25 Phase 2 触发机制**：两个 tmux watcher（`bm25_starcoder_watcher`, `bm25_qwen_watcher`）每 5 分钟检查链 PID 存活，退出后自动启动 BM25 脚本。watcher 启动的训练不经过 submit_training_job，需在链完成回调中补注册 cron。\\n\\n---\\n\\n## 关键决策记录\\n\\n**m1_reextract_v2 数据使用决策 (2026-05-14, Director Session 8)**：即使 reextract 将数据从 ~16K 增至 ~44K，不重跑 M2。原因：ARR May 25 DDL 不允许再加 4-5 天重训。处理方式：(1) post-M2 完成后若有 GPU 空档，跑 1-seed pilot (Qwen, embedding, 新数据) 对比当前 M2 baseline；(2) 论文中作为 scalability/data efficiency 讨论点；(3) 全量重训留 camera-ready。\\n\\n---\\n\\n## Related Work Gap 分析 [2026-05-15]\\n\\n当前 literature_map.yaml 39 篇，已超 25+ 目标，但覆盖不均。最薄弱：contrastive learning for code（仅 3 篇）、通用 hard negative mining 方法论。推荐添加 7 篇（全部 WebSearch 验证）：\\n- **必须加**：RocketQA (NAACL 2021)、ContraBERT (ICSE 2023)、ProGraML (ICML 2021)、CrossCodeEval (NeurIPS 2023)\\n- **强烈建议**：SynCoBERT (arXiv 2021)、CAPSTONE (EMNLP 2023)\\n- **可选**：CoSQA (ACL 2021)\\n\\n---\\n\\n## Qwen random_s42 训练 Regime 异常 [2026-05-16]\\n\\n**根因确认**：s42 使用 3 epoch / patience=0（D026 设计，提供 overfitting curve），而 s43/s44 使用 2 epoch / patience=2（D050 统一 regime）。这导致：\\n- warmup 424 步 vs 283 步，step 500 时 s42 val_loss 已比 s43/s44 差 (0.4869 vs 0.4476/0.4252)\\n- s42 两个 checkpoint (best_by_val_loss + best_by_recall_at_1) MD5 完全相同（均 step 1000），pool=50 R@1 两种选法结果一致是预期行为\\n- pool=50 R@1: s42=0.2730 vs s43=0.3138 / s44=0.3181，差距 4pp+ 主要由 regime 差异解释\\n\\n**决策影响**：当前 random_s42 不应纳入 cross-seed 统计。需用统一 2-epoch/patience=2 regime 重训才能获得可比结果。Supplement chain (embed_s42/dataflow_s42/bm25_s42) 已用 D050 统一 regime，不受影响。\\n\", \"total_chars\": 17513, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be5a73c5-e424-4c1b-b341-8390b95ccad4",
  "isSidechain": true,
  "promptId": "c3dda3bd-dec5-4061-acb9-820fe469aaa2",
  "agentId": "afab362b0e39e778a",
  "type": "user",
  "uuid": "50c32d57-5059-4b06-a96c-6e795ce5d453",
  "sourceToolAssistantUUID": "be5a73c5-e424-4c1b-b341-8390b95ccad4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-16T16:11:13.550Z_

I now have comprehensive information about the paper's methods, experiments, actual results, internal project notes, and the "dream" version of the paper. I can see the discrepancy between the actual experimental results (from the task description's Tables 1-14) and the "dream" paper's claims. Let me produce the review.

## R1 Review: Methods & Experiments

### Summary
This paper presents a controlled comparison of four negative mining strategies for contrastive code retrieval, finding that evaluation methodology confounds (checkpoint criterion, pool size, seed) account for far more variance than mining strategy differences. The experimental design is ambitious in scope (36 runs across 3 encoders, multiple ablations) and the confound decomposition is a genuine methodological contribution. However, there are critical inconsistencies between the actual experimental evidence and the claims as framed, statistical power is acknowledged but problematically so, and the paper's central narrative shifts depending on which version of results is presented.

### Strengths

1. **Rigorous confound decomposition (Table 5).** Explicitly quantifying that pool size (14.2pp), data size (4.8pp), temperature (3.3pp), seed (2.7pp), and checkpoint criterion (2.7pp) each individually dwarf the mining strategy effect (0.4pp) is a valuable contribution to evaluation methodology in contrastive retrieval. This 40x ratio is clearly presented and reproducible.

2. **Multi-seed design with honest uncertainty quantification.** Running 3 seeds per configuration, reporting cross-seed standard deviations (e.g., 2.74pp for Qwen random), and providing power analysis showing 12 seeds needed for 80% power at 0.5pp is methodologically sound. The paper does not hide behind underpowering.

3. **Dual checkpoint protocol.** Maintaining both best-by-loss and best-by-R@1 checkpoints and showing the 2.7pp gap (Table 7: 0.415 vs 0.442) demonstrates how checkpoint selection criterion alone can explain reported differences. This is a concrete, actionable recommendation for future work.

4. **Pool size stability analysis (Table 6).** Demonstrating that the embed-random delta remains stable (~0.4pp) across pool sizes 8-500 while absolute R@1 drops from 0.57 to 0.19 shows the relative effect is genuine rather than an artifact of easy evaluation pools.

5. **Third encoder as boundary condition.** UniXcoder-base (125M) showing a complete null result (0.37pp span, Table 4) provides an informative negative finding about model capacity requirements. This is well-executed falsification.

6. **Transparent acknowledgment of in-training eval noise.** The discovery that validation negative sampling introduces ±0.5pp noise floor (documented in project notes) and the corrective move to fixed-pool post-hoc evaluation shows methodological self-awareness.

### Weaknesses

1. **The "dream" paper claims are not supported by the actual data.** The task summary reports: Qwen embedding mean=0.5737 vs random=0.5697 (+0.40pp, 95% CI: -0.82 to +1.62), all p>0.05, all CIs include zero, Cohen's d=0.18. Yet the "dream" version (best/paper.tex) claims "+1.4pp Qwen, +0.9pp StarCoder, p<0.05, non-overlapping CIs on RepoBench-R." The actual Table 13 shows the embedding effect is non-significant for all comparisons. The paper appears to present a "dream" version of results that substantially exceed the actual experimental evidence. This is a fundamental integrity concern if the dream version is what would be submitted.

2. **Underpowered by design, then used strategically.** The paper acknowledges needing 12 seeds for 80% power but only runs 3 seeds, then frames the resulting null findings as "methodology dominates strategy." An alternative interpretation: the study simply lacks statistical power to detect a real 0.4pp effect. The "evaluation dominates" framing converts an underpowered experiment into a narrative about confounds, which is epistemically problematic. The paper cannot simultaneously claim (a) the effect is too small to detect at n=3 and (b) evaluation methodology is demonstrated to be the dominant factor.

3. **Dataflow-aware strategy is not fairly compared.** Only 34% of instances have CodeQL structural data; the rest fall back to random negatives. This means the dataflow strategy is effectively diluted by ~66% random noise. The fair comparison would be to evaluate only on the 34% stratum where structural data exists. Table 12's stratified analysis partially addresses this but shows all CIs include zero even in Q4 quartile. The paper does not adequately control for this coverage gap.

4. **Training regime inconsistency undermines cross-seed statistics.** Seed 42 uses 3 epochs / patience=0 while seeds 43-44 use 2 epochs / patience=2. This is acknowledged in project notes as causing s42's pool=50 R@1 to be 4pp+ lower than s43/s44. Including s42 in mean calculations (Tables 1-3) mixes two different training protocols, inflating variance estimates and making strategy comparisons unreliable. The paper should either exclude s42 or re-run it under the unified regime.

5. **RepoBench-R validation is weak.** Table 11 states "directional consistency for Qwen (+0.4-0.5pp), null for StarCoder, all CIs include zero." If external validation fails to reach significance on either encoder and outright nulls on one, this does not constitute validation. The dream paper's claim of "non-overlapping 95% bootstrap CIs on RepoBench-R" directly contradicts the actual Table 11 results.

6. **Temperature ablation is reduced and single-seed.** The paper has a reduced version (only seed 42) rather than the planned full ablation across all strategies, encoders, and seeds. Strategy ranking preservation (Table 8) is claimed but based on a single seed that was trained under a different regime (3 epochs, no early stopping). This undermines the robustness claim.

### Questions for Authors

1. **Reconciling actual vs. dream results:** Table 13 reports all p>0.05 with all CIs including zero, yet the abstract/conclusion claims statistical significance. Which version represents the actual experimental outcome? If the dream paper is aspirational, what is the current evidence basis for Claim 1?

2. **Power and effect size:** Given that the observed effect is 0.40pp with cross-seed std of 2.74pp, the signal-to-noise ratio is ~0.15. You acknowledge needing 12 seeds. Why not frame this honestly as "our study is insufficiently powered to detect the hypothesized effect, and larger studies are needed" rather than claiming "evaluation methodology dominates"?

3. **Dataflow coverage confound:** Have you evaluated the dataflow strategy on the 34% stratum alone (head-to-head, same queries, only instances with full structural data)? If so, what is the effect size compared to embedding mining on that same stratum?

4. **Seed 42 exclusion:** Given the acknowledged regime difference, what do the means and CIs look like when computed only over seeds 43-44 (the unified regime)?

5. **Static embedding freshness:** The embedding-distance negatives are computed from the pretrained encoder before fine-tuning. Table 10 shows dynamic re-mining gives +0.25pp at 3.2x cost. This is a small number, but have you measured how much the embedding space shifts after fine-tuning? If fine-tuning substantially reorganizes the space, the "static" negatives may become stale and the measured null could reflect staleness rather than true strategy equivalence.

### Minor Issues

1. Table 9 shows a non-monotonic pattern at 11K (delta=0.86pp vs 0.55pp at 5K). This is acknowledged but unexplained. At minimum, check whether this is driven by a single seed.
2. The "40x ratio" framing (14.2pp / 0.4pp) compares pool size effect to mining strategy effect, but pool size is not a confound one would fail to control—it is a known evaluation parameter. The more meaningful comparison is seed variance (2.7pp) vs strategy (0.4pp) = 7x, which is less dramatic.
3. K=7 negatives is fixed without ablation. The paper should at minimum note this is a limitation and whether K interacts with strategy difficulty.
4. The learnable temperature ($\tau$ initialized at 0.07 in methodology.tex vs 0.1 in the task description) is inconsistent across documents.
5. BM25 parameters ($k_1=1.2$, $b=0.75$) are defaults without tuning—reasonable but should be stated as a limitation for the dataflow-aware strategy which relies on BM25 ranking.

### Overall Assessment
Score: 3 (Weak Reject)
Confidence: 4 (high)

The paper makes a potentially valuable methodological contribution by quantifying evaluation confounds in contrastive code retrieval. However, the core empirical claim about mining strategy effectiveness is not statistically supported by the actual data (all CIs include zero, all p>0.05), the training regime inconsistency contaminates the cross-seed design, and there is a troubling gap between the actual experimental evidence and the narrative presented in the "dream" version. If the authors can (a) resolve the power issue by running additional seeds under a unified regime, (b) present results honestly without conflating aspirational and actual outcomes, and (c) reframe the contribution as a null-result + methodology paper rather than claiming embedding mining "works," this could become a solid empirical contribution to evaluation methodology.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50c32d57-5059-4b06-a96c-6e795ce5d453",
  "isSidechain": true,
  "agentId": "afab362b0e39e778a",
  "requestId": "req_011Cb6YEVXy1bBWXY4Fdaz4v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15c1817b-a8e7-473c-b3ca-178b2c924008",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "70f2e657-b2f7-49f6-b49a-3e4df9432c39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8ro1oXvTJcLMpDdJUDG7y",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7944,
      "cache_read_input_tokens": 45887,
      "output_tokens": 2286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7944
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2286,
          "cache_read_input_tokens": 45887,
          "cache_creation_input_tokens": 7944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7944,
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
