# cron hook eval plan 014 sft no evidence 20260515T213304 190662

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 2
- **Tool calls:** 14
- **Original source:** `logs/chats/archive/cron_hook_eval_plan_014_sft_no_evidence_20260515T213304_190662.jsonl`
- **Structured JSON:** [`ad5e065b9540e200a3a2.json`](../../sessions/ad/ad5e065b9540e200a3a2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

30 recorded events

### User

_source line 1 · 2026-05-15T18:29:37.809899+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: eval_plan_014_sft_no_evidence
- project: faith-evidence-ie
- server: rtx5090-4x
- log_path: ~/runs/faith-evidence-ie/eval_plan_014_sft_no_evidence.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-15T18:29:50.012166+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_experiment_plan_with_status,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__compute_coverage_matrix,mcp__agent-ml-research__get_worker_status",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_experiment_plan_with_status,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__compute_coverage_matrix,mcp__agent-ml-research__get_worker_status",
    "max_results": "15"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-15T18:29:50.063876+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T18:29:53.367020+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T18:29:53.367512+00:00_

called mcp__agent-ml-research__reconcile_crons

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reconcile_crons</summary>

```json
Arguments not recorded in this source.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T18:29:53.970992+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "report.md"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T18:29:54.528402+00:00_

Error: result (170,154 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie--claude-sessions-agent-d384206e/72980821-fcf3-4320-9ea9-25a5d10f2580/tool-results/mcp-agent-ml-research-read_registry-1778869794088.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie--claude-sessions-agent-d384206e/72980821-fcf3-4320-9ea9-25a5d10f2580/tool-results/mcp-agent-ml-research-read_registry-1778869794088.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1161
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T18:29:54.528922+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 1161
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T18:29:54.532410+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-15T18:29:36Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 68 个实验 — ANALYZING 3, DONE 61, PREPARING 2, QUEUED 1, RUNNING 1\\n**DONE 分布**: failed 10, killed 14, negative 8, success 29\\n\\n### GPU 占用\\n- **分配**: 4 张 — rtx5090-4x:cuda:0, rtx5090-4x:cuda:1, rtx5090-4x:cuda:2, rtx5090-4x:cuda:3\\n- **实际运行**: 1 张 — rtx5090-4x:cuda:3(plan_008_rsft_topk3)\\n- **空闲（分配了没跑）**: rtx5090-4x:cuda:0, rtx5090-4x:cuda:1, rtx5090-4x:cuda:2\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `plan_008_rsft_topk3` | rtx5090-4x | cuda:3 | 234489 | `~/runs/faith-evidence-ie/plan_008_rsft_topk3.log` |\\n\\n### 📌 最近完成 (top 5)\\n- `plan_002_test_eval_s44` [failed] — 2026-05-15T18:20:17\\n- `plan_001_rsft_flat_nli` [success] — 2026-05-15T18:04:14\\n- `eval_plan_001_flat_nli` [success] — 2026-05-15T18:04:13\\n- `eval_grpo_g8_bf16` [success] — 2026-05-15T17:57:46\\n- `plan_015_grpo_g4_bf16_v3` [killed] — 2026-05-15T16:54:54\\n\\n### 🔴 最近失败原因 (top 3)\\n- `plan_002_test_eval_s44`: _(no failure_reason — pre-2026-04-24 entry)_\\n- `plan_015_grpo_g4_bf16_v3`: _(no failure_reason — pre-2026-04-24 entry)_\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| plan_008_rsft_topk3 | — | — | — | — |\\n| eval_plan_014_sft_no_evidence | — | — | — | — |\\n| plan_014_sft_no_evidence | SFT-without-evidence ablation: 训练只输出 relation triples（不含 evidence sentences）的 SFT 模型。量化 joint evidence generation 对 extraction 的代价（当前 rel_f1=0.4057 vs 只抽关系的 LMRC 60.7 的 gap 有多少来自 evidence 负担）。 | — | — | — |\\n\\n## 待处理\\n- plan_001_flat_nli_seed43（排队等待 GPU）\\n- mvp2_eval_rs
…[truncated 2632 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 561
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T18:29:54.532953+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T18:29:54.735843+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\", \"content\": \"# faith-evidence-ie — Research Dashboard\\n\\n> 最后更新: 2026-05-15 17:59 UTC | 更新原因: plan_011 Reviewer PASS — C2+C3 证据链完整，QLoRA confound 已解决，cuda:3 派 plan_008\\n\\n## 核心方向\\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。核心发现：GRPO 在结构化 IE 上的 evidence-extraction decoupling 是 QLoRA 量化噪声导致（非 RL 通病）。RSFT+NLI-based scoring 有效提升证据质量。bf16 GRPO 与 RSFT 持平。论文定位：\\\"task definition + decoupling finding + EDCR metric\\\"。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research + 审稿同步进行\\n- **C2 证据完整**: QLoRA GRPO catastrophic forgetting (rel_f1=0.2167) vs bf16 GRPO 正常 (rel_f1=0.4549) — decoupling 是 QLoRA-specific\\n- **C3 证据完整**: bf16 GRPO ckpt-100 ≈ RSFT (差 0.47pp rel_f1)，两者均 >>SFT baseline (+4.9pp)\\n- **plan_001** flat-NLI RSFT: 训练成功，eval 运行中 (cuda:0)\\n- **plan_012** DPO+CED: eval 运行中 (cuda:2)，Reviewer WARNING 过拟合信号\\n- **plan_014** SFT-without-evidence: eval 运行中 (cuda:1)\\n- **Dream v2**: best=3.0/median=2.5/worst=2.5 → 未达标，结构性问题正在逐一修复\\n\\n## 投稿目标\\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25)\\n\\n## 近期任务\\n- [x] plan_011 bf16 GRPO eval — Reviewer PASS, C2+C3 完整\\n- [ ] plan_001 flat-NLI eval (cuda:0 运行中) → 完成后解锁 plan_002/003\\n- [ ] plan_014 SFT-no-evidence eval (cuda:1 运行中)\\n- [ ] plan_012 DPO+CED eval (cuda:2 运行中)\\n- [ ] plan_008 top_k ablation (cuda:3 刚派)\\n- [ ] plan_009 forgetting dynamics figure (P0，检查 worker 是否已完成)\\n- [ ] plan_002 test set eval (P0，deps plan_001)\\n- [ ] plan_003 EDCR pipeline (P0，deps plan_001)\\n- [ ] Paper Agent: retitle + reframe + related work 扩展 (待核心 eval 收齐)\\n\\n## GPU 分配\\n\\n| GPU | 状态 | 任务 |\\n|-----|------|------|\\n| cuda:0 | 🏃 | eval_plan_001_flat_nli |\\n| cuda:1 | 🏃 | eval_plan_014_sft_no_evidence |\\n| cuda:2 | 🏃 | eval_plan_012_dpo_ced |\\n| cuda:3 | 📋 | plan_008 top_k ablation (刚派) |\\n\\n## GPU 预算\\n- 硬件: 4× RTX 5090 32GB (rtx5090-4x)\\n- Research P0 剩余: ~
…[truncated 2195 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 202
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T18:29:54.789460+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "faith-evidence-ie",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "faith-evidence-ie",
    "status": "running"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T18:29:54.940632+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_eval_plan_012_dpo_ced_20260515T174106\", \"task_type\": \"eval:plan_012_dpo_ced\", \"project\": \"faith-evidence-ie\", \"status\": \"running\", \"started_at\": \"2026-05-15T17:41:06.195558+00:00\", \"ended_at\": null}], \"count\": 1}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T18:29:59.776818+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'exp_id': 'eval_plan_014_sft_no_evidence'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'exp_id': 'eval_plan_014_sft_no_evidence'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T18:30:00.330446+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3876}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 553
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T18:30:00.783689+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'exp_id': 'plan_014_sft_no_evidence'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'exp_id': 'plan_014_sft_no_evidence'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T18:30:00.834448+00:00_

called mcp__agent-ml-research__read_experiment_plan_with_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_experiment_plan_with_status</summary>

```json
{
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__read_experiment_plan_with_status",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T18:30:01.087490+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.323}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 303
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T18:30:01.490939+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": [{\"id\": \"plan_001\", \"claim\": 2, \"description\": \"CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选 RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py 用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。\", \"priority\": \"P0\", \"gpu_budget_hours\": 20, \"deps\": [], \"registry_id\": \"plan_001_rsft_flat_nli\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.6238, \"train_loss_min\": 0.5803, \"mean_token_accuracy\": 0.8528, \"train_runtime_sec\": 2946, \"epochs\": 3, \"total_steps\": 507, \"samples\": 2691}}, {\"id\": \"plan_002\", \"claim\": 1, \"description\": \"Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set 上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。\", \"priority\": \"P0\", \"gpu_budget_hours\": 4, \"deps\": [\"plan_001\"], \"registry_id\": null, \"status\": \"planned\"}, {\"id\": \"plan_003\", \"claim\": 4, \"description\": \"EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing 方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。\", \"priority\": \"P0\", \"gpu_budget_hours\": 2, \"deps\": [\"plan_001\"], \"registry_id\": null, \"status\": \"planned\"}, {\"id\": \"plan_004\", \"claim\": 1, \"description\": \"DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large) 的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。\", \"priority\": \"P0\", \"gpu_budget_hours\": 8, \"deps\": [], \"registry_id\": \"plan_004_dreeam_baseline\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"dev_rel_f1\": 63.57, \"dev_rel_ign_f1\": 61.72, \"dev_evi_f1\": 54.01, \"dev_rel_p\": 66.95, \"dev_rel_r\": 60.51, \"dev_evi_p\": 60.53, \"dev_evi_r\": 48.76}}, {\"id\": \"plan_005\", \"claim\": 1, \"description\": \"CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。\", \"priority\": \"P1\", \"gpu_budget_hours\":
…[truncated 7023 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__read_experiment_plan_with_status",
  "elapsed_ms": 656
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T18:30:13.163785+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/registry.yaml | grep -A 50 \"eval_plan_014_sft_no_evidence\"",
  "description": "Search registry.yaml for eval_plan_014_sft_no_evidence entry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/registry.yaml | grep -A 50 \"eval_plan_014_sft_no_evidence\"",
    "description": "Search registry.yaml for eval_plan_014_sft_no_evidence entry"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T18:30:13.365216+00:00_

  eval_plan_014_sft_no_evidence:
    status: ANALYZING
    retry_count: 0
    created_at: '2026-05-15T17:20:25.574Z'
    updated_at: '2026-05-15T18:29:35.278Z'
    spec:
      command: python -m freige.eval.inference --model_path /root/autodl-tmp/sft_no_evidence_output
        --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred
        --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/sft_no_evidence
        --no-quantize --no_evidence
      server: rtx5090-4x
      gpu:
      - cuda:1
      pid: '230804'
      log_path: ~/runs/faith-evidence-ie/eval_plan_014_sft_no_evidence.log
      submitted_at: '2026-05-15T17:20:44.247Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
      data_path: /root/autodl-tmp/data/docred
      data_count: 985
      model_name: Qwen3-4B (SFT-no-evidence)
      seed: 42
      checkpoint_source: /root/autodl-tmp/sft_no_evidence_output
      eval_data: docred dev (985 docs)
    reproduce:
      finished_at: '2026-05-15T18:29:34.790Z'
    extra:
      hook_events:
      - event: on_complete
        action: agent
        ts: '2026-05-15T18:29:37.278008+00:00'
  plan_008_rsft_topk3:
    status: RUNNING
    retry_count: 0
    created_at: '2026-05-15T18:01:33.773Z'
    updated_at: '2026-05-15T18:04:25.251Z'
    spec:
      command: python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B
        --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered_topk3/rsft_train.jsonl
        --output_dir /root/autodl-tmp/rsft_topk3_output --learning_rate 2e-5 --num_epochs
        3 --per_device_batch_size 1 --gradient_accumulation_steps 16 --lora_rank 64
        --lora_alpha 128 --eval_data_dir /root/autodl-tmp/data/docred --wandb_run_name
        plan_008_rsft_topk3 --seed 42
      server: rtx5090-4x
      gpu:
      - cuda:3
      pid: '234489'
      log_path: ~/runs/faith-e
…[truncated 623 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T18:30:31.177198+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/skills/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T18:30:31.730980+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/agent_d384206e.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T18:30:32.133144+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T18:30:32.385336+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/paper_framing.md\", \"content\": \"# Paper Framing — FREIGE\\n\\n> **状态**: POST-MVP + DREAM v2 完成（D047 分析）\\n> **最后更新**: 2026-05-15\\n> **Dream v1**: best=2.5, median=3.0, worst=2.5 → reframe 完成\\n> **Dream v2**: best=3.0, median=2.5, worst=2.5 → best 提升但 median 下降，未达标。关键路径：plan_011 bf16 GRPO eval + structural fixes → re-dream v3\\n\\n## Target Venue\\n\\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\\n\\n## Core Insight\\n\\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。本文提出 **evidence-grounded DocRE** 作为新任务范式：LLM 同时输出关系三元组和支撑证据句。\\n\\n我们系统性地探索了 online RL (GRPO) 和 offline RL (RSFT) 两条技术路线。关键发现：**GRPO 在结构化 IE 上导致 evidence-extraction decoupling**——evidence 质量持续提升（evi_f1→0.85）但抽取能力 catastrophically forget（rel_f1<0.02），这一现象在 3 种 reward function 下一致出现。RSFT 有效规避此问题。\\n\\nCED (Contrastive Evidence Discrimination) 是一种 NLI-based 候选筛选函数，通过文档内 hard negative 对比评估 evidence 质量。CED 作为 RSFT 的 scoring function 之一进行测试，其相对于 flat-NLI 的优势需要通过充分的统计检验验证。\\n\\n## Story Arc\\n\\n1. **Problem**: LLM DocRE 无证据 → 部署障碍\\n2. **New task**: evidence-grounded DocRE — 同时生成关系和证据\\n3. **Exploration**: 系统性比较 online RL (GRPO) vs offline RL (RSFT)\\n4. **Key finding**: evidence-extraction decoupling — GRPO 下 evidence 和 extraction 被差异化优化，extraction catastrophically forget\\n5. **What works**: RSFT with NLI-based scoring 有效提升 evidence 质量而不牺牲抽取\\n6. **Diagnostic tool**: EDCR 捕捉 Evi-F1 的盲区\\n\\n## Core Claims (reframed after Dream v1)\\n\\n### Claim 1 (Main): Evidence-grounded DocRE 是可行的新能力\\n- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法\\n- RSFT 在 4/4 配置下均超过 SFT baseline（rel_f1 +3.9~6.0pp）\\n- 需要 DREEAM-protocol 对齐的 Evi-F1 对比（D041 在处理中）\\n\\n### Claim 2 (Core finding): GRPO 在结构化 IE 上导致 evidence-extraction decoupling\\n- 3 种 reward × 多个 lr 全线失败\\
…[truncated 4293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 252
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T18:30:32.436355+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "memory.md"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T18:30:32.488115+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"content\": \"# 文献调研：GRPO/RLHF 训练中的\\\"先遗忘后恢复\\\"现象\\n\\n日期：2026-05-14\\n\\n## 背景\\n\\nQwen3-4B + GRPO + QLoRA 4-bit 训练文档级关系抽取，观察到：\\n- Reward 上升但 eval rel_F1 崩塌（ckpt-20: 0.0077 vs SFT baseline 0.406）\\n- lr=5e-5 和 lr=5e-6 下都出现\\n- 存在\\\"先遗忘后缓慢恢复\\\"的 U 型曲线（step-10=0.003 → step-90=0.211），但恢复不足\\n\\n---\\n\\n## 论文 1：Mitigating the Alignment Tax of RLHF\\n\\n- **作者**：Yifei Lin, Yuxin Tan, et al.\\n- **年份/Venue**：2024, EMNLP 2024\\n- **arXiv**：2309.06256\\n\\n### 核心发现\\n- 定义了\\\"alignment tax\\\"：RLHF 对齐后模型遗忘预训练/SFT 阶段习得能力的现象\\n- 发现简单的**模型参数平均**（插值 SFT 和 RLHF 后模型权重）在 alignment-forgetting Pareto 前沿上表现最优\\n- 提出 **Heterogeneous Model Averaging (HMA)**：对不同层使用不同插值比例\\n\\n### 与我们场景的相关性\\n- **直接相关**。GRPO 阶段的 rel_F1 崩塌是 alignment tax 的典型表现\\n- HMA 的层级插值思路可直接应用于 QLoRA adapter 权重（但 GRPO 路线已判死，仅留作参考）\\n\\n---\\n\\n## 论文 2：Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment\\n\\n- **作者**：Lu et al. (Qwen 团队)\\n- **年份/Venue**：2024, arXiv 2405.17931\\n- **开源**：github.com/QwenLM/online_merging_optimizers\\n\\n### 核心发现\\n- 在 RLHF 每个优化步骤中实时合并 RL policy 和 SFT 模型参数\\n- 在 Qwen 和 LLaMA 系列上验证有效\\n\\n### 与我们场景的相关性\\n- 高度相关但 GRPO 路线已判死，仅留作参考\\n\\n---\\n\\n## D031 Pivot: GRPO+QLoRA → RSFT + CED (2026-05-15)\\n\\n### 决策\\nGRPO+QLoRA 方向判死，pivot 到 Rejection Sampling Fine-Tuning (RSFT) + CED scoring。\\n\\n### 核心证据\\n- lr=5e-5 (ced_kl001_r4): best eval rel_f1=0.211 (step-90)，仅 SFT baseline (0.406) 的 52%\\n- lr=5e-6 (lr5e6_r1): 完整轨迹 ckpt-20→100 rel_f1 = 0.008/0.007/0.009/0.012/0.014 — 零恢复\\n- 所有 3 种 reward type (CED/extract-only/flat-NLI) 在 GRPO+QLoRA 下均 collapse\\n\\n### RSFT 技术约束\\n- **--quantize (4-bit) + merge_and_unload 在 RTX 5090 上有 CUBLAS 错误**，RSFT 训练不要用 quantize。bf16 Qwen3-4B 仅 ~8GB，无需量化。\\n- 运行目录必须是 `/root/autodl-tmp/`（freige 不是 pip install 的包，cd 到 freige/ 子目录会导致 import 找到内层空包）\\n\\n---\\n\\n## ⭐ bf16 GRPO 成功 — Forgetting 是 
…[truncated 9987 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T18:31:03.875212+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "analyze:eval_plan_014_sft_no_evidence",
  "project": "faith-evidence-ie",
  "task_prompt": "## 任务\n分析实验 eval_plan_014_sft_no_evidence 的结果并汇总指标。\n\n## 背景\n这是 SFT-without-evidence 模型的 dev set evaluation。该模型只输出 relation triples（不含 evidence sentences），目的是量化 evidence generation 对抽取性能的代价。\n\n对比基线:\n- 标准 SFT (含 evidence): rel_f1=0.4057, evi_f1=0.7979, EDCR=0.7118, pred_count=12234\n- RSFT CED 3-seed mean: rel_f1=0.4596±0.0128\n- LMRC (纯抽取，无 evidence): rel_f1≈0.607\n\n## 执行步骤\n\n1. SSH 到 rtx5090-4x，读取 eval log：\n```bash\ncat ~/runs/faith-evidence-ie/eval_plan_014_sft_no_evidence.log\n```\n\n2. 读取 eval 输出目录中的结果文件：\n```bash\nls -la /root/autodl-tmp/eval_results/sft_no_evidence/\ncat /root/autodl-tmp/eval_results/sft_no_evidence/eval_metrics.json 2>/dev/null\ncat /root/autodl-tmp/eval_results/sft_no_evidence/metrics*.json 2>/dev/null\ncat /root/autodl-tmp/eval_results/sft_no_evidence/*.json 2>/dev/null\n```\n\n3. 如果 log 或 json 中没有完整 metrics，检查 W&B：\n- 查看 log 中是否有 wandb run ID\n- 关键指标: rel_f1, ign_f1, rel_precision, rel_recall, pred_count, format_ok_rate, n_truncated, n_total\n- 注意: 因为 --no_evidence 模式，可能没有 evi_f1 / EDCR（或这些值为 0）\n\n4. 检查 checkpoint 路径确认 eval 用了正确的模型：\n```bash\nls -la /root/autodl-tmp/sft_no_evidence_output/\n```\n\n## 产出\n用 save_project_file 写一个简洁的分析报告到项目临时文件。内容包括：\n- 完整 metrics 表格\n- 与 SFT baseline (含 evidence) 的对比\n- 结论：evidence generation 对 rel_f1 的影响有多大\n\n## 服务器\n- server: rtx5090-4x\n- 用 ssh_read_only 读取所有内容，不需要执行任何修改操作",
  "tool_groups": "['ssh', 'wandb', 'knowledge']"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analyze:eval_plan_014_sft_no_evidence",
    "project": "faith-evidence-ie",
    "task_prompt": "## 任务\n分析实验 eval_plan_014_sft_no_evidence 的结果并汇总指标。\n\n## 背景\n这是 SFT-without-evidence 模型的 dev set evaluation。该模型只输出 relation triples（不含 evidence sentences），目的是量化 evidence generation 对抽取性能的代价。\n\n对比基线:\n- 标准 SFT (含 evidence): rel_f1=0.4057, evi_f1=0.7979, EDCR=0.7118, pred_count=12234\n- RSFT CED 3-seed mean: rel_f1=0.4596±0.0128\n- LMRC (纯抽取，无 evidence): rel_f1≈0.607\n\n## 执行步骤\n\n1. SSH 到 rtx5090-4x，读取 eval log：\n```bash\ncat ~/runs/faith-evidence-ie/eval_plan_014_sft_no_evidence.log\n```\n\n2. 读取 eval 输出目录中的结果文件：\n```bash\nls -la /root/autodl-tmp/eval_results/sft_no_evidence/\ncat /root/autodl-tmp/eval_results/sft_no_evidence/eval_metrics.json 2>/dev/null\ncat /root/autodl-tmp/eval_results/sft_no_evidence/metrics*.json 2>/dev/null\ncat /root/autodl-tmp/eval_results/sft_no_evidence/*.json 2>/dev/null\n```\n\n3. 如果 log 或 json 中没有完整 metrics，检查 W&B：\n- 查看 log 中是否有 wandb run ID\n- 关键指标: rel_f1, ign_f1, rel_precision, rel_recall, pred_count, format_ok_rate, n_truncated, n_total\n- 注意: 因为 --no_evidence 模式，可能没有 evi_f1 / EDCR（或这些值为 0）\n\n4. 检查 checkpoint 路径确认 eval 用了正确的模型：\n```bash\nls -la /root/autodl-tmp/sft_no_evidence_output/\n```\n\n## 产出\n用 save_project_file 写一个简洁的分析报告到项目临时文件。内容包括：\n- 完整 metrics 表格\n- 与 SFT baseline (含 evidence) 的对比\n- 结论：evidence generation 对 rel_f1 的影响有多大\n\n## 服务器\n- server: rtx5090-4x\n- 用 ssh_read_only 读取所有内容，不需要执行任何修改操作",
    "tool_groups": "['ssh', 'wandb', 'knowledge']"
  }
}
````

</details>

---

### Tool result

_source line 29 · 2026-05-15T18:31:06.692140+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analyze_eval_plan_014_sft_no_evidence_20260515T183104\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/logs/workers/worker_analyze_eval_plan_014_sft_no_evidence_20260515T183104.log\", \"setup_data\": {}, \"message\": \"Worker worker_analyze_eval_plan_014_sft_no_evidence_20260515T183104 started. Use get_worker_status('worker_analyze_eval_plan_014_sft_no_evidence_20260515T183104') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 2816
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-15T18:31:23.070893+00:00_

Worker 已派出分析 eval_plan_014 结果。等待 Worker 回调。当前状态:
- cuda:0, cuda:1 空闲
- cuda:2 跑 DPO eval (worker running)
- cuda:3 跑 plan_008 RSFT topk3 训练

Worker 池: 2 个 (分析 eval_014 + DPO eval)，满足最低要求。等 Worker 返回 eval_014 metrics 后更新 registry 并汇报 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval_plan_014_sft_no_evidence"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 31 · 2026-05-15T21:32:14.201464+00:00_

[WRITE HANDOFF] 请立即写你的 handoff。

**格式硬约束**:
- 整条回复**只能**是 &lt;handoff>...&lt;/handoff> 标签包裹
- 禁止在标签外写任何寒暄 / 说明 / 确认（"好的"/"我开始写"/"写完了"等）

**必须覆盖以下 5 个 section（缺一不可，无内容写 N/A）**:

### 1. 🔴 硬约束 / 红线
  本项目特定的不可违反约束（GPU 设备号、服务器名、账号、路径限制等）。
  写本项目特定的，不要抄 CLAUDE.md 通用 L1 红线。
  下一个"你"第一眼看到的就是这里，写错了会被 Director CRITICAL。

### 2. 🖥️ 基础设施快照
  - 服务器名 + 工作目录 + Python 路径 + conda env
  - 模型路径 / 数据集路径 / wandb config / HF cache
  - 活跃进程：PID + tmux session + cron 任务 ID
  写一次就稳定，下一个"你"不用再 SSH 探查。

### 3. 📊 当前状态
  - 你刚做完什么 / 正在做什么
  - registry 里 RUNNING/PREPARING 的实验列表 + 一句话摘要
  - 等待中的 Worker 回调 / Cron / Director 决策

### 4. 📋 待办（条件触发式）
  格式 "条件 X 满足 → 动作 Y"。例如:
  - "Falcon-H1R 下载完成 → sed 修 MODEL_PATH → dry-run → 提交"
  - "pilot_011 出 GC4 结果 → ≥2pp 转架构 narrative，<2pp 写 null-result"

### 5. 🎯 战略上下文
  - 项目核心结论 / 决策链（D001..）
  - 下一个"你"最容易判断错的事 / 容易踩的坑

**写作原则**：
- 第 1 节必须是项目特定的（不是通用 L1 红线）
- 第 2 节让下一轮 BOOT 后能立即开工，避免重新 SSH 探查
- 简洁 > 完整：每节 5-10 行足够，长 handoff 不等于好 handoff

示例格式:
&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:4 / cuda:5（之前两次违规 cuda:0 被 Director CRITICAL）
- submit_training_job 不支持 shell builtin（source/conda activate 全不行）

### 2. 🖥️ 基础设施快照
- 服务器：westd-8x6000，工作目录 /root/autodl-tmp/hybrid_reasoning_phases
- Python：/root/miniconda3/bin/python（绝对路径，不走 conda activate）
- 模型：/root/autodl-tmp/qwen35_4b_direct
- 活跃：pilot_011 (PID 203221, tmux=pilot_011, cuda:4)

### 3. 📊 当前状态
我刚完成 pilot_010 分析，正在等 pilot_011 (Falcon-H1R) CoT 生成完成（6/50）。
registry: pilot_011 RUNNING；其他全 DONE。

### 4. 📋 待办
- pilot_011 cron 回调 → spawn worker 跑 probe + GC4 计算
- GC4 ≥2pp → 转架构 narrative；<2pp → null-result paper outline 已就绪

### 5. 🎯 战略上下文
Falcon-H1R 是最后一个数据点。已知 4B/9B GC4 都 FAIL。
易错：不要把 GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 直接对比。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval_plan_014_sft_no_evidence",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-15T21:33:04.077218+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单: rtx5090-4x 的 cuda:0, cuda:1, cuda:2, cuda:3（共 4 张），不可用其他 GPU
- RTX 5090 必须 `--no-quantize`（QLoRA 4-bit 有 CUBLAS 错误）
- inference.py 必须传完整模型 stack: `--base_model` + `--sft_adapter` + `--model_path`，缺任何一层结果不可用
- 运行目录必须在 `/root/autodl-tmp/`，不能 cd 到 freige/ 子目录（会导致 import 找到内层空包）
- D057: test set eval 已推迟到论文终稿阶段，不要现在跑 plan_002
- D056: CED vs flat-NLI 统计不可区分，CED 不再作为独立贡献，论文方向已收窄为 "task definition + QLoRA decoupling finding + EDCR metric"

### 2. 🖥️ 基础设施快照
- 服务器: rtx5090-4x, 4× RTX 5090 32GB
- 工作目录: `/root/autodl-tmp/`（代码 repo 在此下）
- Python: `/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 激活命令: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型路径:
  - Base: `/root/autodl-tmp/models/Qwen3-4B`
  - SFT adapter: `/root/autodl-tmp/sft_output`
  - SFT-no-evidence: `/root/autodl-tmp/sft_no_evidence_output`
  - RSFT CED: `/root/autodl-tmp/rsft_output` (多 seed 在子目录)
  - RSFT top_k=3: `/root/autodl-tmp/rsft_topk3_output` (训练中)
- 数据: `/root/autodl-tmp/data/docred` (dev 985 docs)
- W&B: entity/project 从 project config 读取
- HF cache: `/root/autodl-tmp/.hf_cache`
- 活跃进程: plan_008_rsft_topk3 (PID 234489, tmux, cuda:3)

### 3. 📊 当前状态
**刚做的**: 收到 eval_plan_014_sft_no_evidence CRON 回调（进程正常退出，ANALYZING），已 spawn Worker `worker_analyze_eval_plan_014_sft_no_evidence_20260515T183104` 去 SSH 读 log 提取 metrics。**Worker 尚未回调，下一个我需要处理这个回调。**

**Registry 状态**:
- `plan_008_rsft_topk3` — RUNNING, cuda:3, PID 234489 — top_k=3 CED RSFT 训练（8037 samples vs 标准 2718）
- `eval_plan_014_sft_no_evidence` — ANALYZING, cuda:1 已释放 — SFT-without-evidence dev eval
- `plan_012_dpo_ced` — ANALYZING — DPO+CED eval，Worker `worker_eval_plan_012_dpo_ced_20260515T174106` 仍在运行
- `plan_014_sft_no_evidence` — ANALYZING — 训练部分已 success，等 eval 结果一起关闭

**空闲 GPU**: cuda:0, cuda:1, cuda:2（cuda:2 eval 可能快完成）

**等待中**:
- Worker 回调: eval_plan_014 分析 worker、plan_012 DPO eval worker
- plan_008 训练完成 cron 回调

### 4. 📋 待办
- eval_plan_014 分析 Worker 回调到达 → 读 metrics → update_registry(eval_plan_014 → DONE) + update_registry(plan_014 → DONE) → 与 SFT baseline 对比（rel_f1 gap 有多少来自 evidence 生成负担）→ 更新 report.md → 汇报 Director
- plan_012 DPO eval Worker 回调到达 → 同上流程，DPO 是 RL spectrum 关键数据点（Dream v2 要求），关注是否有过拟合（ROADMAP 标 WARNING）
- plan_008 cron 回调 → spawn eval worker（用空闲 cuda 跑 full dev eval）
- cuda:0/1/2 空闲 → 检查 experiment_plan 中哪些 P0/P1 可以立即铺（plan_003 EDCR pipeline 是 CPU 任务可立即 spawn；plan_009 forgetting dynamics figure 也是 CPU/数据汇总任务可立即 spawn）
- 如 eval_plan_014 显示 SFT-no-evidence rel_f1 显著 > SFT-with-evidence → evidence generation 负担被量化，直接写入论文 story；如差距不大 → evidence generation 不是 gap 主因，需要其他解释

### 5. 🎯 战略上下文
**项目核心**: FREIGE = evidence-grounded DocRE。论文定位为 analysis paper，核心贡献是 (1) 新任务定义, (2) QLoRA-specific decoupling 发现, (3) EDCR metric。

**关键决策链**:
- D054: GRPO decoupling 从 "RL 通病" 收窄为 "QLoRA-specific"（bf16 GRPO rel_f1=0.4549 正常）
- D056: CED vs flat-NLI 统计不可区分 → CED 降级，不再是独立贡献
- D057: test set eval 推迟到论文终稿

**最容易判断错的事**:
1. **不要以为 GRPO 完全失败**——只有 QLoRA GRPO 崩塌，bf16 GRPO (0.4549) 与 RSFT (0.4596) 接近。论文 claim 是 "QLoRA causes forgetting in GRPO"，不是 "GRPO fails"
2. **plan_015 (bf16 G=4 隔离实验) 已被 killed (D052)**——plan_011 vs mvp2_grpo_ced_kl001_r4 已构成 clean ablation，不需要再跑
3. **eval 用的 evi_f1 是 conditional**（只算 TP triples 的 evidence），与 DREEAM joint protocol 不可直接比
4. **Worker 池当前只有 2 个运行**（plan_012 eval + plan_014 分析），plan_008 有 cron 监控。空闲 GPU 3 张是失职信号——接手后立即检查能铺什么
5. **投稿目标 EMNLP 2026 ARR July (~7/15-25)**，剩 ~2 个月，核心 eval 正在收尾，收齐后进入 paper writing phase
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval_plan_014_sft_no_evidence"
}
```

</details>

---
