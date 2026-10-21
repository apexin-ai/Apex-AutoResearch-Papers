# cron hook eval adaptive k spatial p50 seed44 r2 20260521T024609 437958

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 85
- **Recorded user turns:** 2
- **Tool calls:** 41
- **Original source:** `logs/chats/archive/cron_hook_eval-adaptive-k-spatial-p50-seed44-r2_20260521T024609_437958.jsonl`
- **Structured JSON:** [`57c9efa7c53cbce54fb7.json`](../../sessions/57/57c9efa7c53cbce54fb7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

37 recorded events

### User

_source line 1 · 2026-05-20T09:50:53.580437+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: eval-adaptive-k-spatial-p50-seed44-r2
- project: acr-vla-conformal-refinement
- server: bjb2-28827
- log_path: ~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed44-r2.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-20T09:51:07.602343+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__send_progress,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__get_worker_status",
  "max_results": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__send_progress,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__get_worker_status",
    "max_results": "12"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-20T09:51:07.602677+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T09:51:10.964947+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T09:51:11.467837+00:00_

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
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T09:51:12.069752+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "report.md"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T09:51:12.493538+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T09:51:12.754697+00:00_

Error: result (650,299 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-6c64b20e/7317285c-edfe-4eee-8006-151111062abb/tool-results/mcp-agent-ml-research-read_registry-1779270672594.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-6c64b20e/7317285c-edfe-4eee-8006-151111062abb/tool-results/mcp-agent-ml-research-read_registry-1779270672594.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1789
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T09:51:12.755235+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "status": "running"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T09:51:18.562897+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 1, \"results\": [{\"exp_id\": \"eval-adaptive-k-spatial-p50-seed42\", \"success\": true, \"actions\": [\"Job still running (pid=681823)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 7095
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T09:51:18.619910+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-20T09:50:50Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 430 个实验 — ANALYZING 1, DEPLOYED 4, DONE 380, PREPARING 32, QUEUED 12, RUNNING 1\\n**DONE 分布**: failed 47, killed 85, negative 32, success 216\\n\\n### GPU 占用\\n- **实际运行**: 1 张 — bjb2-40593:cuda:0(eval-adaptive-k-spatial-p50-seed42)\\n\\n### 💾 磁盘余量\\n- **bjb2-40593**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 46G/437G 可用（已用 90%） ⚠️\\n- **bjb1-18228**:\\n  - `/autodl-pub`: 992G/7.0T 可用（已用 87%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb1-32546**:\\n  - `/autodl-pub`: 904G/7.0T 可用（已用 88%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb2-28827**:\\n  - `/autodl-pub`: 4.5T/14T 可用（已用 69%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/439G 可用（已用 5%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `eval-adaptive-k-spatial-p50-seed42` | bjb2-40593 | cuda:0 | 681823 | `—` |\\n\\n### 📌 最近完成 (top 5)\\n- `eval-adaptive-k-p75-seed42` [success] — 2026-05-20T09:46:30\\n- `eval-adaptive-k-p75-seed43` [success] — 2026-05-20T09:46:26\\n- `eval-adaptive-k-p50-seed42` [success] — 2026-05-20T09:46:22\\n- `eval-adaptive-k-p50-seed43` [success] — 2026-05-20T09:46:19\\n- `eval-random-selection-object-seed42` [success] — 2026-05-20T09:26:47\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval-adaptive-k-spatial-p50-seed42 | Adaptive K with τ=P
…[truncated 7083 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6550
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T09:51:18.625714+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-20 06:17 UTC | 更新原因: Fix Long OOD data to match D081, update RUNNING section per Reviewer observation\\n\\n> 详见 paper_framing.md（D077: Adaptive K 升级为核心贡献）\\n\\n## 核心方向\\n**Adaptive inference-time compute for frozen VLAs** — K=2 L2 distance 作为不确定性信号，自适应决定每步推理次数。CRM correction>selection 分析作为支撑。\\n\\n## 投稿目标\\n**CoRL 2026** DDL **2026-05-29**。剩余 ~9 天。\\n\\n## D077 方向转换（用户硬要求）\\n- Adaptive K = 论文**核心贡献**（方法）\\n- K=10 分析降为 supporting evidence\\n\\n## 信号候选 (CLOSED)\\n| 信号 | ρ vs K10_var | 结论 |\\n|------|-------------|------|\\n| **K=2 L2 distance** | **0.9979** | **✅ GO — 唯一可用信号** |\\n| CRM correction magnitude | 0.1523 | ❌ NO-GO (D079) |\\n| FMVD | 0.0825 | ❌ NO-GO |\\n\\n## Adaptive K Sweep (Object) — 12/12 DONE ✅\\n| 阈值 | seeds | SR (mean) | avg_K | fast_path% | vs K=10 |\\n|------|-------|-----------|-------|-----------|---------|\\n| P90 | 3/3 ✅ | 13.3% | ~2.6 | ~93% | 74% |\\n| P75 | 3/3 ✅ | 13.7% | ~3.1 | ~87% | 79% |\\n| **P50** | **3/3 ✅** | **15.3%** | **~3.8** | **~77%** | **~91%** |\\n| P25 | 3/3 ✅ | 14.3% | ~4.8 | ~65% | ~85% |\\n\\n**P50 = Pareto 最优 (D078)**。\\n\\n## RUNNING 实验\\n- bjb2-40593: Spatial Adaptive K P50 seed42 (rollout 中)\\n- bjb1-18228: Long VLA-only seed54, Long CRM seed53, Spatial VLA-only seed53\\n- bjb1-32546: Long CRM seed54, Spatial VLA-only seed54\\n- 更多部署中（Agent 处理综合指令）\\n\\n## 待部署\\n1. **Spatial Adaptive K P50 seed43, seed44**\\n2. **Random Selection baseline seed42, seed44** (plan_600)\\n3. **CRM Object K=10 norm02 seed42** (Table 1 n=6→n=7)\\n4. **fig3_kvalue 重新生成**\\n\\n## 论文 CRITICAL 待解决\\n1. **evaluate.py 推理模式确认** — Agent P0\\n2. **Spatial CRM K=10 n=8 溯源** — registry 只有 n=7, Agent 调查中\\n3. **OOD Long/Goal 数据全量更新** — Paper Agent 处理中\\n4. **P25 n=3 更新** — Paper Agent 处理中\\n\\n## 核心实验结果 (LOCKED,
…[truncated 2536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 6132
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T09:51:18.788574+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_gpu-scan_bjb1-18228_20260520T095114\", \"task_type\": \"gpu-scan:bjb1-18228\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-20T09:51:14.484850+00:00\", \"ended_at\": null}], \"count\": 1}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 6033
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T09:51:23.894674+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-adaptive-k-spatial-p50-seed44-r2'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-adaptive-k-spatial-p50-seed44-r2'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T09:51:24.327797+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-adaptive-k-spatial-p50-seed42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-adaptive-k-spatial-p50-seed42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T09:51:26.087610+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.1676}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2192
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T09:51:27.595877+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.4666}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 3268
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T09:51:32.522468+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "eval-adaptive-k-spatial-p50-seed44",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "eval-adaptive-k-spatial-p50-seed44",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T09:51:32.673527+00:00_

Found 33 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/cron_hook_eval-adaptive-k-spatial-p50-seed44-r2.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a_reviewer.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/checkpoints/eval-adaptive-k-spatial-p50-seed44-r2_ANALYZING_20260520T095044.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/feishu_group_oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_harvest_eval-random-selection-object-seed42_20260520T092524.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/cron_hook_eval-adaptive-k-spatial-p50-seed43-r2.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/cron_hook_eval-obs-only-object-norm02-seed42.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/cron_hook_eval-random-selection-object-seed42.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_ssh_deploy-bjb2-28827-remaining_20260520T084702.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/cron_hook_eval-random-selection-object-seed44.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conform
…[truncated 3113 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T09:51:36.111947+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "eval-adaptive-k-spatial-p50-seed44-r2",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "output_mode": "content",
  "-A": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "eval-adaptive-k-spatial-p50-seed44-r2",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "output_mode": "content",
    "-A": "30"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T09:51:36.162590+00:00_

15737:  eval-adaptive-k-spatial-p50-seed44-r2:
15738-    status: ANALYZING
15739-    retry_count: 0
15740-    created_at: '2026-05-20T06:42:09.659Z'
15741-    updated_at: '2026-05-20T09:50:43.968Z'
15742-    hypothesis: K=2 L2 divergence-based adaptive K allocation (P50 threshold τ=0.074855)
15743-      transfers from Object to Spatial benchmark, achieving comparable SR to fixed
15744-      K=10 with ~62% compute savings. Cross-benchmark validation of adaptive K as
15745-      core method.
15746-    parent: eval-adaptive-k-spatial-p50-seed44
15747-    spec:
15748-      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
15749-        base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache
15750-        HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py
15751-        --mode adaptive_k --adaptive_threshold 0.074855 --k_full 10 --benchmark spatial
15752-        --seed 44 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt
15753-        --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p50_seed44.json"
15754-      server: bjb2-28827
15755-      gpu:
15756-      - cuda:0
15757-      pid: '249543'
15758:      log_path: ~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed44-r2.log
15759-      submitted_at: '2026-05-20T07:08:05.277Z'
15760-      submitted_via: submit_training_job
15761-      backend: tmux
15762-      account: root
15763-    server: bjb2-28827
15764-    gpu: cuda:0
15765-    account: root
15766-    reproduce:
15767-      server: bjb2-28827
15768-      gpu: cuda:0
15769-      started_at: '2026-05-20T07:08:00.822Z'
15770-      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
15771-        base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache
15772-        HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py

…[truncated 1682 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T09:51:43.492220+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "eval-adaptive-k-spatial-p50-seed43-r2",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "output_mode": "content",
  "-A": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "eval-adaptive-k-spatial-p50-seed43-r2",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "output_mode": "content",
    "-A": "40"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T09:51:43.643685+00:00_

15678:  eval-adaptive-k-spatial-p50-seed43-r2:
15679-    status: DONE
15680-    retry_count: 0
15681-    created_at: '2026-05-20T06:42:06.832Z'
15682-    updated_at: '2026-05-20T09:26:09.877Z'
15683-    hypothesis: K=2 L2 divergence-based adaptive K allocation (P50 threshold τ=0.074855)
15684-      transfers from Object to Spatial benchmark, achieving comparable SR to fixed
15685-      K=10 with ~62% compute savings. Cross-benchmark validation of adaptive K as
15686-      core method.
15687-    parent: eval-adaptive-k-spatial-p50-seed43
15688-    spec:
15689-      checkpoint_path: N/A (eval only)
15690:      log_path: ~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43-r2.log
15691-    server: bjb1-32546
15692-    gpu: cuda:0
15693-    account: root
15694-    reproduce:
15695-      server: bjb1-32546
15696-      gpu: cuda:0
15697-      started_at: '2026-05-20T07:07:47.040Z'
15698-      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
15699-        base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache
15700-        HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py
15701-        --mode adaptive_k --adaptive_threshold 0.074855 --k_full 10 --benchmark spatial
15702-        --seed 43 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt
15703-        --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p50_seed43.json"
15704-      finished_at: '2026-05-20T09:14:06.027Z'
15705-      training_hours: 2.11
15706-    pid: '303834'
15707:    log_path: ~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed43-r2.log
15708-    extra:
15709-      hook_events:
15710-      - event: on_complete
15711-        action: agent
15712-        ts: '2026-05-20T09:14:15.835758+00:00'
15713-    metrics:
15714-      overall_success_rate: 0.33
15715-      per_task_sr:
15716-        between_plate_and_ramekin: 0.8
157
…[truncated 1227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T09:51:43.945048+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "eval-adaptive-k-spatial-p50-seed42:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "output_mode": "content",
  "-A": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "eval-adaptive-k-spatial-p50-seed42:",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "output_mode": "content",
    "-A": "40"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T09:51:43.995776+00:00_

15497:  eval-adaptive-k-spatial-p50-seed42:
15498-    status: RUNNING
15499-    retry_count: 1
15500-    created_at: '2026-05-20T06:01:50.026Z'
15501-    updated_at: '2026-05-20T07:57:07.905Z'
15502-    hypothesis: Adaptive K with τ=P50 (0.074855, Object-calibrated) on LIBERO-Spatial
15503-      seed42. 验证 Adaptive K 方法在第二个 benchmark 上的泛化：使用 Object 上校准的阈值直接应用到 Spatial（无
15504-      per-benchmark tuning）。如果 SR 接近 CRM K=10 (34.3%) 且 fast_path >50%，则证明方法跨 benchmark
15505-      通用。
15506-    notes: 'PID 681823 在 bjb2-40593:cuda:0 运行中 (State: R, 210 threads, 6483 MiB GPU)。旧
15507-      cron 检测旧 PID 675831 死亡后误标 DONE/failed，已恢复 RUNNING。第三次 cron 误报。'
15508-    reproduce:
15509-      finished_at: '2026-05-20T07:29:54.160Z'
15510-    failure_reason: ''
15511-    completed_at: '2026-05-20T07:29:59.173Z'
15512-    extra:
15513-      hook_events:
15514-      - event: on_failed
15515-        action: agent
15516-        ts: '2026-05-20T07:30:08.474411+00:00'
15517-      previous_failure:
15518-        conclusion: failed
15519-        notes: '旧PID 675831被kill后，新PID 681823已于cuda:0重新启动，运行正常(11min+)。旧cron检测到675831死亡触发误报回调。已完成3/10
15520-          tasks，SR: 70%/100%/0%，第4个task进行中。'
15521-    spec:
15522-      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
15523-        base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache
15524-        HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py
15525-        --mode adaptive_k --adaptive_threshold 0.074855 --k_full 10 --benchmark spatial
15526-        --seed 42 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt
15527-        --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p50_seed42.json"
15528-      server: bjb2-40593
15529-      gpu:
15530-      - cuda:0
15531-      pid: '681823'
15532-      data_path: LIBERO-Spatial
15533-      data_count: '100'
15534-      model_name: SmolVLA+Adaptive
…[truncated 94 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T09:52:01.938414+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "harvest:eval-adaptive-k-spatial-p50-seed44-r2",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务\nSSH 到 bjb2-28827 读取实验 eval-adaptive-k-spatial-p50-seed44-r2 的结果。\n\n## 步骤\n\n1. SSH 读取日志末尾（最后 100 行）:\n   ```\n   服务器: bjb2-28827\n   日志: ~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed44-r2.log\n   ```\n\n2. SSH 读取输出 JSON 文件:\n   ```\n   路径: /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p50_seed44.json\n   ```\n\n3. 从 JSON 文件提取以下指标:\n   - overall_success_rate (或 success_rate)\n   - per_task_sr (每个 task 的 success rate)\n   - avg_k (平均 K 值)\n   - fast_path_ratio (fast path 比例)\n   - adaptive_trigger_rate (触发完整推理比例)\n   - mean_l2_distance\n   - total_steps, fast_steps, full_steps\n   - threshold\n   - total_rollouts\n\n4. 用 update_registry 更新实验:\n   - field=\"metrics\", value=上面提取的 metrics dict\n   - field=\"conclusion\", value=\"success\" 或 \"negative\"（SR > 0 且方法正常工作即 success）\n   - field=\"status\", value=\"DONE\"\n   - 设 spec.checkpoint_path = \"N/A (eval only)\"\n\n**判断 conclusion**:\n- Spatial CRM K=10 baseline SR ≈ 34.3%\n- 如果 Adaptive K SR 合理（>20%），且 avg_k < 10（有 fast path），则 conclusion=success\n- 如果完全 crash 或 SR=0，则 conclusion=failed\n\n同系列参考: seed43-r2 结果 — SR=33%, avg_k=6.33, fast_path_ratio=0.458\n\n5. 汇报提取到的完整 metrics。",
  "tool_groups": "['ssh', 'registry']"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "harvest:eval-adaptive-k-spatial-p50-seed44-r2",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务\nSSH 到 bjb2-28827 读取实验 eval-adaptive-k-spatial-p50-seed44-r2 的结果。\n\n## 步骤\n\n1. SSH 读取日志末尾（最后 100 行）:\n   ```\n   服务器: bjb2-28827\n   日志: ~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed44-r2.log\n   ```\n\n2. SSH 读取输出 JSON 文件:\n   ```\n   路径: /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p50_seed44.json\n   ```\n\n3. 从 JSON 文件提取以下指标:\n   - overall_success_rate (或 success_rate)\n   - per_task_sr (每个 task 的 success rate)\n   - avg_k (平均 K 值)\n   - fast_path_ratio (fast path 比例)\n   - adaptive_trigger_rate (触发完整推理比例)\n   - mean_l2_distance\n   - total_steps, fast_steps, full_steps\n   - threshold\n   - total_rollouts\n\n4. 用 update_registry 更新实验:\n   - field=\"metrics\", value=上面提取的 metrics dict\n   - field=\"conclusion\", value=\"success\" 或 \"negative\"（SR > 0 且方法正常工作即 success）\n   - field=\"status\", value=\"DONE\"\n   - 设 spec.checkpoint_path = \"N/A (eval only)\"\n\n**判断 conclusion**:\n- Spatial CRM K=10 baseline SR ≈ 34.3%\n- 如果 Adaptive K SR 合理（>20%），且 avg_k < 10（有 fast path），则 conclusion=success\n- 如果完全 crash 或 SR=0，则 conclusion=failed\n\n同系列参考: seed43-r2 结果 — SR=33%, avg_k=6.33, fast_path_ratio=0.458\n\n5. 汇报提取到的完整 metrics。",
    "tool_groups": "['ssh', 'registry']"
  }
}
````

</details>

---

### Tool call

_source line 27 · 2026-05-20T09:52:02.440772+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T09:52:05.006047+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_harvest_eval-adaptive-k-spatial-p50-seed44-r2_20260520T095202\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_harvest_eval-adaptive-k-spatial-p50-seed44-r2_20260520T095202.log\", \"setup_data\": {}, \"message\": \"Worker worker_harvest_eval-adaptive-k-spatial-p50-seed44-r2_20260520T095202 started. Use get_worker_status('worker_harvest_eval-adaptive-k-spatial-p50-seed44-r2_20260520T095202') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 3067
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T09:52:05.006529+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_6c64b20e.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "elapsed_ms": 2565
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T09:52:08.275756+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T09:52:08.326415+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T09:52:10.736522+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation*",
  "path": "/home/ubuntu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation*",
    "path": "/home/ubuntu"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-20T09:52:10.988165+00:00_

/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T09:52:13.345442+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T09:52:13.345941+00:00_

1	---
2	name: resource-saturation
3	description: "当你准备向 Director 汇报前、收到 cron/worker 回调、审批通过准备开跑、怀疑 Worker 池不够饱和时,立即使用本 skill。四部分:A) GPU 分配率(分配了没跑=失职) B) GPU 效率 C) 非 GPU 任务并行(Worker 池<2=失职) D) 汇报必须带 [资源] 行。"
4	always: false
5	roles:
6	  - director
7	  - agent
8	---
9	
10	# 资源饱和度自检（硬约束）
11	
12	## A. GPU 分配率检查
13	
14	调 `get_project_resource_usage(project)` 看:
15	- 已分配给本项目的 GPU 总数和具体卡号
16	- 实际在跑任务的 GPU 数和具体卡号（交叉 registry RUNNING + nvidia-smi 进程）
17	- 分配了但没跑的 GPU 清单 ⚠️
18	
19	任何"分配了但没跑"的 GPU = 失职。必须立即:
20	- 派 Worker 铺 dry-run / 下一批实验代码准备
21	- 铺 ablation（从 experiment-matrix 空白格子里挑）
22	- 确实无实验可铺 → 向 Director 汇报"暂无可铺实验"+ 建议下一步方向(扩 ablation 维度 / 加 baseline / 加 benchmark)。**不要建议归还 GPU**——项目级 GPU 归还只在归档时由 `archive_project` 自动触发, 不是 Director 中途的动作
23	
24	**单实验不占多卡**: 分配 4 卡但实验只用 1 卡 → 另 3 卡必须并行跑其他实验,不能空占。
25	
26	## B. GPU 效率检查
27	
28	调 `get_gpu_health(server)`:
29	- 空闲 GPU（util < 10% 持续 > 5 min）→ 立即铺任务
30	- 低利用率（util < 50% 持续 > 15 min）→ spawn_worker 诊断（batch / IO / 同步）
31	- OOM 风险（显存 > 90% 持续 10 min）→ 主动降 batch / 调优
32	
33	## C. 非 GPU 任务并行
34	
35	GPU 在跑 ≠ 你空闲。以下 CPU / 网络任务**必须**派独立 Worker 并行:
36	- 下一批实验的数据集下载 / 预处理 / fingerprint
37	- 下一批实验的代码准备 / dry-run / 环境配置
38	- 论文文献调研 / related work 检索
39	- 已完成实验的 log 深度分析 / metric 聚合
40	- 论文章节起草
41	- 代码 review / refactor
42	
43	**硬约束**: 任一时刻 Worker 池 < 2 个 = 失职（除非真的全部下游阻塞在等 GPU,这时应当向 Director 申请扩 GPU）。
44	
45	## D. 汇报格式
46	
47	向 Director 汇报时开头必须带资源声明行:
48	
49	    [资源] GPU 分配 N / 实际在跑 M | Worker 池 K (其中 GPU 任务 A / CPU 任务 B)
50	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T09:52:22.689498+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'QUEUED'}",
  "fields": "['exp_id', 'status', 'hypothesis', 'server', 'gpu']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'QUEUED'}",
    "fields": "['exp_id', 'status', 'hypothesis', 'server', 'gpu']"
  }
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-20T10:10:54.010051+00:00_

Worker 已派出去读取 seed44-r2 结果。同时检查 QUEUED 实验队列，了解下一步部署需求。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2"
}
```

</details>

---

## Round 2

48 recorded events

### User

_source line 38 · 2026-05-21T02:43:23.232461+00:00_

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
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T02:43:49.615487+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/",
  "description": "List project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/",
    "description": "List project directory"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T02:43:50.420121+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
_last_visual_review.json
artifacts
checkpoints
decisions.lock
decisions.yaml
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.lock
experiment_plan.yaml
literature_map.yaml
logs
memory.md
mistakes.lock
mistakes.yaml
paper
paper_framing.md
paper_provenance.lock
paper_provenance.yaml
registry.lock
registry.yaml
report.md
scripts
src
study_status.lock
task_context
writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Bash",
  "elapsed_ms": 804
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T02:43:50.574514+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ 2>/dev/null || echo \"NO_ARTIFACTS_DIR\"",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ 2>/dev/null || echo \"NO_ARTIFACTS_DIR\"",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T02:43:50.675421+00:00_

__pycache__
_project
ablation_eval_commands.md
adaptive_k_design.md
analysis
analysis_magnitude_sweep.py
analysis_object_benchmark.py
analysis_spatial_final.py
argmin_seed44_r2_results.json
batched_inference_feasibility_report.md
benchmark_data_audit.md
benchmark_survey.md
citation_attribution_audit.md
citation_audit_report.md
competitive_analysis_20260515.md
competitor_analysis.md
conclusion_draft.md
contribution_list.md
corl_paper_outline.md
correction_degradation_literature.md
crm-train-v2-k5
crm_bug_audit.md
crm_k1_model.py
diag-eval-v6-batch-failure.md
diag_bjb1_18228.md
diag_bjb2_28827.md
diag_plan_a_spatial_seed42_43.md
diagnose-eval-adaptive-k-spatial-p50-seed44.md
diagnose-norm02-seed44-r2.md
diagnose-random-selection-seed46-r2.md
diagnose_bjb1_18228_failure.md
diagnose_bjb1_32546_batch_failure.md
diagnose_crm_long_seed45.md
diagnose_default_seed46.md
diagnose_failed_evals_20260521.md
diagnose_spatial_k5_seed44_r2.md
diagnosis-eval-obs-only-object-norm003-seed43.md
diagnosis_random_k5_seed44_r2.md
dream_reports
eval-acr-object-v4-obs-only
eval-acr-object-v4-scalar
eval-argmin-object-seed44-r2
eval-mag-perdof-norm03
eval-obs-only-goal-norm02-seed52.json
eval-obs-only-object-default-seed45
eval-obs-only-object-norm01-seed45-r2
eval-obs-only-object-norm02-seed44-r2
eval-obs-only-object-norm02-seed46
eval-obs-only-object-norm03-seed44
eval-openvla-object-vla-only-seed42
eval-openvla-object-vla-only-seed42-v2
eval-random-selection-object-k5-seed44-r2
eval-reconvla-spatial-v1-diag.md
eval-vla-mean-object-seed44
experiment_progress_20260515.md
experiments_draft.md
fallback_narrative_draft.md
fig_magnitude_curve.py
figures
fisher_analysis.py
fix_plan_code_sketch.md
gpu_health_snapshot_20260515.md
introduction_draft.md
k_value_curve_data.json
latency-profile-n1000
latency_breakdown.json
lerobot-pipeline-alignment.md
libero-smolvla-env-report.md
literature_gap_report.md
magnitude_curve.pdf
magnitude_curve.png
magnitude_curve_data.json
magnitude_curve_data.md
magnitud
…[truncated 1335 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T02:43:54.994352+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T02:43:55.297141+00:00_

1	baseline: null
2	experiments:
3	  mvp-point-reaching:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-13T01:22:10.415Z'
7	    updated_at: '2026-05-17T03:13:35.534Z'
8	    spec:
9	      hypothesis: Per-DOF uncertainty features carry more actionable information than
10	        scalar uncertainty summaries, enabling dimension-selective correction
11	      description: '3D point-reaching MVP: 3 MLP variants (scalar/per-DOF/no uncertainty)
12	        x 6 groups (3 anisotropy ratios x 2 uncertainty sources)'
13	      server: bjb2-40593
14	      gpu: cuda:0
15	      data_count: 20000
16	      model_name: CorrectionMLP(2-layer, 64-hidden)
17	      seed: 42
18	      command: python -u run_mvp.py
19	      data_path: synthetic (generated in-script)
20	      checkpoint_path: /root/acr-vla-conformal-refinement/mvp/
21	      log_path: /root/acr-vla-conformal-refinement/mvp/mvp_results.log
22	    conclusion: success
23	    completed_at: '2026-05-13T01:44:00.055Z'
24	    metrics:
25	      group1_oracle:
26	        A_scalar:
27	          mse_x: 0.180218
28	          mse_y: 0.02497
29	          mse_z: 0.024232
30	          total: 0.076473
31	        B_perDOF:
32	          mse_x: 0.172652
33	          mse_y: 0.015544
34	          mse_z: 0.01561
35	          total: 0.067935
36	        C_none:
37	          mse_x: 0.22706
38	          mse_y: 0.025542
39	          mse_z: 0.024753
40	          total: 0.092451
41	      group2_oracle:
42	        A_scalar:
43	          mse_x: 0.064642
44	          mse_y: 0.023836
45	          mse_z: 0.022967
46	          total: 0.037148
47	        B_perDOF:
48	          mse_x: 0.053403
49	          mse_y: 0.015695
50	          mse_z: 0.01573
51	          total: 0.028276
52	        C_none:
53	          mse_x: 0.084178
54	          mse_y: 0.025427
55	          mse_z: 0.024798
56	          total: 0.044801
57	      group3_oracle:
58	        A_scalar:
59	          mse_x: 0.042948
60	          mse_y: 0.023218
61	          mse_z: 0.022365
62	   
…[truncated 5314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T02:43:55.298363+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T02:43:56.052227+00:00_

1	&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-21T02:36:32Z; do not edit — regenerated by auto_build_report_facts) -->
2	## 📊 当前状态（auto-derived from registry）
3	
4	**总计**: 541 个实验 — ANALYZING 1, DEPLOYED 5, DONE 482, PREPARING 34, RUNNING 19
5	**DONE 分布**: failed 54, killed 90, negative 38, success 300
6	
7	### GPU 占用
8	- **实际运行**: 19 张 — bjb2-28827:cuda:2(eval-obs-only-object-norm003-seed56), bjb1-32546:cuda:0(eval-obs-only-object-norm003-seed64), bjb1-32546:cuda:1(eval-obs-only-object-norm003-seed65), bjb1-32546:cuda:3(eval-obs-only-object-norm01-seed64), bjb1-32546:cuda:4(eval-obs-only-object-norm01-seed65), bjb1-32546:cuda:5(eval-obs-only-object-norm005-seed64), bjb1-32546:cuda:0(eval-obs-only-object-norm01-seed51-r3), bjb1-32546:cuda:1(eval-obs-only-object-norm01-seed52-r3), bjb1-32546:cuda:3(eval-obs-only-object-norm003-seed62-r2), bjb1-32546:cuda:4(eval-obs-only-object-norm003-seed63-r2), bjb2-28827:cuda:0(eval-obs-only-object-norm01-seed71), bjb2-28827:cuda:1(eval-obs-only-object-norm005-seed72), bjb2-28827:cuda:2(eval-obs-only-object-norm003-seed73), bjb2-28827:cuda:3(eval-obs-only-object-norm01-seed74), bjb2-28827:cuda:4(eval-obs-only-object-norm005-seed75), bjb1-18228:cuda:0(eval-obs-only-object-norm003-seed66), bjb1-18228:cuda:2(eval-obs-only-object-norm005-seed66), bjb1-18228:cuda:3(eval-obs-only-object-norm01-seed66), bjb2-40593:cuda:0(eval-pi05-baseline-object-seed42)
9	
10	### 💾 磁盘余量
11	- **bjb2-40593**:
12	  - `/init`: 150M/150M 可用（已用 0%）
13	  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）
14	  - `/usr/bin/nvidia-smi`: 46G/437G 可用（已用 89%）
15	- **bjb1-18228**:
16	  - `/autodl-pub`: 588G/7.0T 可用（已用 92%） ⚠️
17	  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）
18	  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）
19	- **bjb1-32546**:
20	  - `/autodl-pub`: 888G/7.0T 可用（已用 88%）
21	  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）
22	  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）
23	- **bjb2-28827**:
24	  - `/autodl-pub`: 4.4T/14T 可用（已用 69%）
25	  - `/autodl-pub/data`: 5.7T/10T 可用（
…[truncated 4787 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T02:43:56.204467+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T02:43:56.205166+00:00_

1	# acr-vla-conformal-refinement — Research Dashboard
2	
3	> 最后更新: 2026-05-21 00:48 UTC | 更新原因: D092-D095 updates: Plan A LOCKED, OpenVLA CRM CLOSED, π0.5/π added, GPU state corrected
4	
5	> 详见 paper_framing.md（D077: Adaptive K 核心, D088→D090→D092: Plan A GO）
6	
7	## 核心方向
8	**Adaptive inference-time compute for frozen VLAs** — K=2 L2 distance 作为不确定性信号，自适应决定推理策略（直出 vs CRM correction）。CRM correction>selection 分析作为支撑。
9	
10	## 投稿目标
11	**CoRL 2026** DDL **2026-05-29**。剩余 **8 天**。
12	
13	## 方法路径（D088→D092 最终）
14	- ❌ B (Learned Uncertainty Head): NO-GO, mean 12.0% < VLA-only (D090)
15	- ✅ **A (Plan A: K=2 Conformal + Selective CRM)**: Object 18.3%±2.1%, Spatial 35.0%±1.0% — **GO (D092/D094)**
16	- ⏳ C (Action Distribution Geometry): 不再需要，Plan A 已成功
17	
18	## Plan A 核心结果
19	| Benchmark | Plan A (K=2) | K=10 CRM | Δ vs K=10 | Compute |
20	|-----------|-------------|----------|-----------|---------|
21	| Object    | 18.3%±2.1%  | 16.8%    | +1.5pp    | 80% less (K=2 vs K=10) |
22	| Spatial   | 35.0%±1.0%  | 34.5%    | +0.5pp    | 80% less |
23	
24	Pipeline: K=2 batched forward → d₂=‖a₁-a₂‖₂ → if d₂>τ: argmin-to-centroid + CRM; if d₂≤τ: direct output。
25	⚠️ Threshold calibration: flatten-L2 (30D) vs per-step-mean-L2 (7D×5) 差异 ~2.77×，当前 τ 在 Plan A scale 上 trigger rate 84%。待决：强调 K=2 效率 vs recalibrate Pareto sweep。
26	
27	## OpenVLA 实验线
28	- ✅ plan_801: OpenVLA v2 baseline SR=69%
29	- ✅ plan_802 train: CRM 训练完成 (val_loss=0.077260)
30	- ❌ **D093: OpenVLA CRM eval 0%** — near-deterministic (T=0.5, 8/10 identical actions)，applicability boundary，CLOSED
31	
32	## π0.5/π 实验线（D095，用户硬要求）
33	- 🔄 Phase 1: WebSearch + 下载模型（Agent 队列中）
34	- ⏳ Phase 2: env setup + baseline eval
35	- ⏳ Phase 3: 检查 action diversity → if stochastic: CRM pipeline
36	- 目的：第二/三个 VLA backbone（flow-matching），解决 M1 (narrow scope) + R2-W1-new (low absolute perf)
37	
38	## Norm Sweep 状态（plan_200/500）
39	| ε    | n seeds | mean SR | 状态 |
40	|------|---------|---------|------|
41	| 0.03 | ~6      | 15.5%   | seeds running
…[truncated 2883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T02:44:02.530068+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T02:44:02.983050+00:00_

1	# Project Memory
2	
3	## 失败模式记录
4	
5	- [失败模式] Cron false positive：eval 脚本不写 W&B 也不写 sentinel file，进程正常退出后 cron 5 次检测找不到标记 → 自动标记为 failed。受影响：eval-vla-only-long-seed46, eval-vla-only-goal-seed46。修复方案：tail 日志确认实际完成 → 手动修正 conclusion=success + 补录 metrics。预防：eval 实验应检查 output JSON 是否存在作为 sentinel。
6	
7	- [失败模式] Cron false positive（2026-05-20）：**eval-adaptive-k-spatial-p50-seed42** 被 cron 误判为 failed（"process dead 5× with no sentinel/W&B"）。实际情况：原 PID 675831 被 deploy worker kill 后，重启为 PID 681823。重启后进程正常运行，但 cron 监控未追踪到新 PID，5 次检测均未发现 sentinel → 自动标记 failed。诊断时（2026-05-20）PID 681823 仍在运行（状态 Rl+，已运行 17h36m），已完成 3/10 tasks（SR: 70%/100%/0%），第 4 个 task 进行中（rollout 5, 1/5 success）。GPU 使用 5972/24564 MiB，日志无错误。**无需重新提交，等待自然完成后手动修正 conclusion。**
8	
9	- [失败模式] SIGHUP false failure（2026-05-20）：bjb2-28827 上多个实验 EXIT_CODE=129 (SIGHUP) 被标记 failed，实际全部完成。**已确认受影响：P75-seed44, P90-seed42, P25-seed44**。SIGHUP 发生在进程写完结果 JSON 之后（tmux session 断开或 SSH 连接清理）。**诊断方法：tail 日志看 "Results saved to" + "Overall success rate" 行 → 手动修正 conclusion=success 并补录 metrics。**
10	
11	- [失败模式] Cron 日志路径不匹配（2026-05-20）：**eval-obs-only-goal-norm02-seed51** (bjb1-32546) 被 cron 误判 dead。根因：实验日志写入 `/root/acr-vla-conformal-refinement/logs/`（项目目录下），但 cron 监控在 `~/runs/acr-vla-conformal-refinement/` 下找日志 → 找不到 → 5 次检测均无 sentinel → auto-resolved failed。**教训：submit_training_job 的 log_path 必须与实际 tee 输出路径一致。部分实验用 `tee logs/xxx.log`（相对于 cd 后的项目目录），另一部分用 `~/runs/` 绝对路径，两套路径并存导致 cron 误判。**
12	
13	- [失败模式] Cron false positive 批量（2026-05-20 诊断）：bjb1-32546 上 **eval-perdof-object-norm02-seed50** (PID 542405) 和 **eval-obs-only-object-norm02-seed51** (PID 542894) 被 cron 报告 "process gone, no sentinel, no W&B"。实际两者均已**正常完成**，output JSON 已写入。bjb1-18228 上 **eval-obs-only-object-norm005-seed44** 同样正常完成但被标记 failed。根因同上：eval 脚本不写 sentinel/W&B，进程正常退出后 cron 无法确认完成状态。结果：perdof-norm02-seed50 SR=10.0%, obs_only-norm02-seed51 SR=17.0%, obs_only-norm005-seed44 SR=12.0%。**均无需重跑，需手动修正 conclusion=success 并补录 metrics。**
14	
15	- [失败模式] python PATH 不存在（
…[truncated 5201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-21T02:44:03.485217+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md",
  "offset": "87",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md",
    "offset": "87",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T02:44:03.887087+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (87). The file has 87 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T02:44:03.887470+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-21T02:44:03.938689+00:00_

1	# Paper Framing — acr-vla-conformal-refinement
2	
3	> Last updated: 2026-05-20 ~20:30 UTC | D090: D088 NO-GO → Plan A fallback, OpenVLA v2=69% (D087), VLA-only n=8, Adaptive K P50 结果, norm range 修正
4	
5	## Target Venue
6	- **CoRL 2026** (DDL **2026-05-29** per ROADMAP; ⚠️ previously said ~Jun 2 — need user confirmation)
7	- Framing: Analysis paper — inference-time correction dissection + mechanism insights (D065 reframe)
8	- Title: "Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs"
9	
10	## Core Insight (D065 revised)
11	Learned correction is the active mechanism that improves frozen VLA policies, but multi-sampling is an enabling condition: it provides a centered starting point within the CRM's bounded correction radius. Neither works alone — K=1 correction performs below baseline (10.3% vs 11.0%), and selection without correction matches baseline. The improvement (+5.8pp, 16.8% vs 11.0%, K=10 n=7 excl. seed42 per D084; K=5: 15.5%) emerges from correction operating on a multi-sample-centered input. Batched inference (D067) eliminates K as a latency factor (~170ms for all K on RTX 4090). The conditioning-magnitude interaction determines success vs catastrophic failure: observation features yield robust corrections (13.4-16.8% across all ε), while conformal per-DOF features cause progressive collapse (14%→0%). This pipeline requires stochastic VLA action diversity as a prerequisite. **D069 boundary**: CRM correction is task-specific — on held-out tasks (LTO), CRM actively degrades VLA (2% vs 14%), revealing that correction quality is bounded by calibration data coverage. Cross-benchmark results (Spatial K=10: 34.5%±1.5%, n=9) are in-distribution (CRM trained on all 20 tasks). **Adaptive K (D076)**: P50 threshold achieves 15.3% at avg_K=3.8 (~91% of fixed K=10). **OpenVLA (D087)**: v2 baseline 69%, CRM training complete (plan_802).
12	
13	## Headline Metrics
14	- **K=5 CRM obs_only (PRIMARY, D066)**: 16.0%±2.2% (n=7, seeds 42-48
…[truncated 7443 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-21T02:44:13.418817+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md",
  "offset": "100",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md",
    "offset": "100",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-21T02:44:13.879212+00:00_

100	## 全 Benchmark 统计摘要 (v2, 2026-05-20, 含新增数据)
101	
102	### 1. LIBERO-Object — **Strong improvement**
103	
104	| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |
105	|--------|---|----------|----------|-----------|-----|
106	| **CRM norm02 K=10 (主配置)** | **6** | **16.8%±1.8%** | **+6.0pp** | **0.000095** | **\*\*\*** |
107	| CRM norm01 (补充) | 6 | 17.5%±1.0% | +6.6pp | <0.001 | *** |
108	| CRM norm02 K=5 (补充) | 7 | 16.0%±2.2% | +5.1pp | 0.000312 | *** |
109	| Adaptive-K (all) | 12 | 14.2%±1.5% | +3.3pp | 0.000098 | *** |
110	| Argmin K=10 | 5 | 12.4%±2.9% | +1.5pp | 0.317 | n.s. |
111	| **VLA-only** | **8** | **10.9%±1.4%** | — | — | — |
112	
113	### 2. LIBERO-Spatial — **Strong improvement**
114	
115	| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |
116	|--------|---|----------|----------|-----------|-----|
117	| CRM obs_only (K=10) | 7 | 34.6%±1.4% | **+5.0pp** | 0.000007 | *** |
118	| **VLA-only** | **9** | **29.6%±1.1%** | — | — | — |
119	
120	### 3. LIBERO-Goal (OOD) — **Neutral**
121	
122	| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |
123	|--------|---|----------|----------|-----------|-----|
124	| CRM obs_only | 7 | 67.7%±3.3% | -1.0pp | ~0.7 | n.s. |
125	| **VLA-only** | **6** | **68.7%±3.9%** | — | — | — |
126	
127	### 4. LIBERO-Long (OOD) — **⚠️ Borderline**
128	
129	| Method | n | Mean±Std | vs VLA Δ | p (Welch) | Sig |
130	|--------|---|----------|----------|-----------|-----|
131	| CRM obs_only | 7 | 17.0%±2.0% | **+2.2pp** | 0.049 | * |
132	| **VLA-only** | **11** | **14.8%±2.2%** | — | — | — |
133	
134	**⚠️ Long MW-U p=0.061 (n.s.)。t检验 p=0.049 刚好卡在 0.05 边缘。论文需 cautious wording。**
135	
136	### 效果总结
137	
138	| Benchmark | Δ (pp) | p-value | 判定 |
139	|-----------|--------|---------|------|
140	| **Object** | +6.0 | <0.001 | Strong (主配置 norm02) |
141	| **Spatial** | +5.0 | <0.001 | Strong |
142	| **Long** | +2.2 | 0.049 | ⚠️ Borderline (OOD, MW-U n.s.) |
143	| **Goal** | -1.0 | ~0.7 | Neutral (OOD) |
144	
145	**注意**: Argmin K=10 seed43=17
…[truncated 777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "elapsed_ms": 460
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-21T02:44:16.327496+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-21T02:44:16.383177+00:00_

1	_next_id: 97
2	decisions:
3	- id: D001
4	  date: 2026-05-13 01:03 UTC
5	  summary: MVP 方案确定：3D Point-Reaching Motivating Experiment 验证 per-DOF conformal 特征的信息优势
6	  rationale: IDEA_BRIEF 已设计了完美的 go/no-go gate：用合成数据的 3D reaching task 对比 per-DOF vs
7	    标量 vs 无不确定性三种 conditioning，直接测试核心假设。成本极低（<0.5 GPU-hours），无需 VLA 基础设施，失败则提前止损。Pass
8	    标准明确：B 在非扰动轴 MSE 比 A 低 >10%。
9	  related_experiments: []
10	  depends_on: []
11	- id: D002
12	  date: 2026-05-13 01:06 UTC
13	  summary: 采纳 Reviewer 建议完善 MVP：增加 B vs C 对比（>5% MSE）、K=10 estimated uncertainty variant、2:1/1.5:1
14	    各向异性 sweep
15	  rationale: Reviewer 正确指出 (1) 缺少 B vs C 对比会遗漏"观测特征已足够"的可能性，这直接关系核心 claim；(2) oracle
16	    uncertainty 与实际 pipeline 存在 gap，K=10 variant 几乎零成本可验证；(3) 5:1 比率过极端，需测试更温和情况。三项改进均不增加显著成本。
17	  related_experiments: []
18	  depends_on:
19	  - D001
20	- id: D003
21	  date: 2026-05-13 01:47 UTC
22	  summary: MVP 通过，GO — 进入 research 阶段
23	  rationale: 全部 3 条 pass 标准满足且 margin 很大：per-DOF (B) 在非扰动轴 MSE 比标量 (A) 低 22-38%，比无
24	    uncertainty (C) 低 15-39%。K=10 estimated 和弱各向异性(1.5:1)下均成立。核心假设"per-DOF conformal
25	    特征携带更多可操作信息"得到验证。关注风险：oracle→K=10 衰减 ~15pp，真实 7-DOF 场景待验证。
26	  related_experiments:
27	  - exp_id: mvp-point-reaching
28	    role: MVP gate
29	    result: PASS — all 6 conditions met criteria
30	  depends_on:
31	  - D001
32	  - D002
33	- id: D004
34	  date: 2026-05-13 02:59 UTC
35	  summary: Horizon 策略：截取 chunk 前 H_eff=5 步，action_dim=6。CGS 输出 40D。
36	  rationale: SmolVLA chunk_size=50 远超原假设 H=5。receding-horizon 执行语义下只需关注近期 action 的
37	    uncertainty，远期 step 对当前校正无意义。H_eff=5 保持与 IDEA_BRIEF 设计一致，CGS 40D 可控（per-DOF std
38	    30 + radius 5 + volume 5），p/n=6/10=0.6 优于原假设 0.7。H_eff=10 留作 ablation。action_dim=6
39	    使 Ledoit-Wolf 更稳定。
40	  related_experiments: []
41	  depends_on:
42	  - D003
43	- id: D005
44	  date: 2026-05-13 03:00 UTC
45	  summary: 不等 Dream 重新提交，直接启动 P0 实验。Dream zombie 占槽，Reviewer 已两轮审核通过 framing/plan。
46	  rationale: Dream dream_20260513T015051 崩溃在 review 阶段（imagine+write 
…[truncated 1669 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "elapsed_ms": 55
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-21T02:44:22.167000+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
  "offset": "600",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
    "offset": "600",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-21T02:44:22.670210+00:00_

600	  - D030
601	  - D031
602	  - D032
603	- id: D034
604	  date: 2026-05-15 20:25 UTC
605	  summary: ReconVLA 重新定位：从"直接竞品(selection-only)"改为"同领域不同路线(UQ+OOD检测)"
606	  rationale: '引用审计确认 ReconVLA 使用 CQR 单流不确定性量化 + SMD OOD 检测，不做多样本选择。之前将其描述为"sample
607	    selection"是错误的。重新定位：ReconVLA="何时不信任"(UQ+OOD)，ACR-VLA="如何改进执行"(selection+correction)。这减少了直接竞争，使
608	    ACR-VLA 的 multi-sample conformal selection + correction 更具独创性。paper_framing.md
609	    Story Spine/Competitive Landscape/Reviewer Concern #7 已更新。Paper Agent 已收到 .tex
610	    修正指令。'
611	  related_experiments: []
612	  depends_on: []
613	- id: D035
614	  date: 2026-05-16 00:49 UTC
615	  summary: 'D035: Kill criterion 触发 (pooled Δ=1pp, p=0.89) + seed43 CRM 零效果异常，暂缓方向决策等排查结论'
616	  rationale: obs_only vs argmin pooled Fisher p=0.89, Δ=1.0pp, kill criterion (|Δ|<3pp)
617	    触发。更严重的是 Reviewer 发现 seed43 obs_only 与 VLA-only 100/100 rollout 完全一致(p<7e-6)，CRM
618	    校正可能未生效。如果是 bug 则 seed43 数据无效需重跑；如果是方法问题则需根本性 reframe。在排查结论出来前暂缓所有方向性决策。
619	  related_experiments:
620	  - exp_id: eval-obs-only-object-seed43
621	    role: primary
622	    result: 12/100=12%, identical to VLA-only
623	  - exp_id: eval-argmin-object-seed43
624	    role: primary
625	    result: 17/100=17%
626	  - exp_id: eval-acr-object-v4-obs-only
627	    role: baseline_seed42
628	    result: 19/100=19%
629	  depends_on:
630	  - D033
631	  - D031
632	- id: D036
633	  date: 2026-05-16 01:20 UTC
634	  summary: 暂停新 baseline 实验，P0 调查 seed43 CRM 零纠正根因
635	  rationale: Reviewer 发现 obs_only seed43 与 vla_only seed43 逐 rollout 完全一致（100/100），CRM
636	    纠正量为零。ε=0.1 pooled Fisher p=0.44，Claim 1 不成立。在确定是代码 bug 还是 CRM 本身不稳定之前，不应投入 GPU
637	    跑新 baseline（如 argmin seed=44），因为如果是 bug 则现有 seed43 数据全部作废需要重跑。等根因 + ε=0.2 seed43
638	    结果再决定 framing。
639	  related_experiments:
640	  - exp_id: eval-obs-only-object-seed43
641	    role: trigger
642	    result: 12% SR, identical to vla_only
643	  - exp_id: eval-argmin-object-seed43
644	    role: baseline
645	    result: 17% SR
646	  
…[truncated 6478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-21T02:44:22.971734+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"^  - id:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
  "description": "Count decisions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"^  - id:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
    "description": "Count decisions"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-21T02:44:23.175619+00:00_

0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Bash",
  "elapsed_ms": 203
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-21T02:44:31.227484+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"^- id:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
  "description": "Count decisions correctly"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"^- id:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
    "description": "Count decisions correctly"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-21T02:44:31.680724+00:00_

96

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Bash",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-21T02:44:31.831753+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
  "offset": "1400",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
    "offset": "1400",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-21T02:44:31.934224+00:00_

1400	- id: D074
1401	  date: 2026-05-19 16:56 UTC
1402	  summary: 'D074: Adaptive K go/no-go 时间线——FMVD Phase 1 今天出结果，5/22 前完成全 pipeline 或切换信号源'
1403	  rationale: Reviewer 指出 D072 pivot 风险：FMVD 未验证就改了论文方向。设定硬时间线：(1) FMVD Phase 1 今天
1404	    (5/19) 出结果（仅 1 GPU-hour），ρ>0.3 go; (2) 如果 go，Phase 2/3 在 5/21 前完成; (3) 如果 FMVD
1405	    fail，不回退到 analysis paper（用户硬要求 adaptive K），而是立即尝试备选信号（K=2 L2 距离、action variance）;
1406	    (4) 5/22 是锁定 framing 的硬截止——无论什么信号，adaptive K eval 必须完成; (5) 5/22-27 paper writing。用户不接受固定
1407	    K 的 analysis paper，fallback 是换信号源不是换方向。
1408	  related_experiments:
1409	  - exp_id: calibrate-fmvd-phase1
1410	    role: go/no-go gate
1411	    result: running on bjb2-28827 GPU5
1412	  depends_on:
1413	  - D072
1414	- id: D075
1415	  date: 2026-05-19 19:04 UTC
1416	  summary: 'D075: FMVD Phase 1 NO-GO (ρ=0.0825)——立即测试 K=2 L2 距离作为替代信号，用现有数据后分析'
1417	  rationale: FMVD (flow velocity dispersion) 与 K=10 action variance 的 Spearman ρ=0.0825，远低于
1418	    0.3 门槛。SmolVLA K=10 action variance 本身极小 (mean=0.005)，FMVD 无法区分微小差异。Adaptive K
1419	    的零成本信号路线失败。立即测试 K=2 L2 距离：从 FMVD 校准数据中取 2/10 samples 计算 L2，检查与 K=10 variance 的相关性。这是零
1420	    GPU 成本的后分析，可在分钟内出结果。若 K=2 也失败，需要重新审视 adaptive K 方向——batched inference 已消除 K 的延迟差异
1421	    (170ms for all K)，可能需要从 step-level adaptive 转向其他方向。
1422	  related_experiments:
1423	  - exp_id: fmvd-calibration-phase1
1424	    role: primary
1425	    result: 'NO-GO: ρ=0.0825'
1426	  depends_on:
1427	  - D072
1428	  - D074
1429	- id: D076
1430	  date: 2026-05-19 22:39 UTC
1431	  summary: 'D076: K=2 L2 GO (ρ=0.9979) — 启动 Phase 2 adaptive K threshold sweep + pipeline
1432	    实现'
1433	  rationale: K=2 L2 pairwise distance 与 K=10 variance 的 Spearman ρ=0.9979（近乎完美），2
1434	    次推理即可替代 10 次推理的不确定性估计。FMVD 确认无关（ρ=0.09）。Adaptive K 架构：默认 K=2（batched，延迟=K=1）→
1435	    L2 > τ 时扩展到 K=10 + CRM 校正 → L2 ≤ τ 时直接用 K=2 argmin。Phase 2：实现 adaptive pipeline
1436	    + threshold sweep（τ = P25/P50/P75/P90）× 3 seeds on Object → 找 SR vs avg_K Pareto
1437	    最优。Phase
…[truncated 6791 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-21T02:44:37.270518+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
  "offset": "1600",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
    "offset": "1600",
    "limit": "250"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-21T02:44:37.324549+00:00_

1600	  rationale: Spatial sweep 数据显示：(1) 所有阈值 SR 保留率 >91%，L2 probe 在 OOD 上仍准确识别 hard steps；(2)
1601	    但效率退化明显（P50 compute 38%→64%）。Pareto 最优点 benchmark-dependent（Object=P50, Spatial=P75）。Framing
1602	    选择：论文默认 P50（ID-calibrated），展示跨 benchmark SR 保留的鲁棒性，efficiency 退化作为 Discussion
1603	    分析点——"方法自动为更难任务分配更多计算"。不建议 per-benchmark tuning 作为默认（会削弱 single-threshold 简洁性
1604	    claim）。Abstract 不写死 "38% compute"，改为报告两个 benchmark 范围。Supplementary 放完整 Spatial
1605	    sweep 表。
1606	  related_experiments:
1607	  - exp_id: eval-adaptive-k-spatial-p50-seed43
1608	    role: evidence
1609	    result: SR=33%, avg_K=6.33, compute=63.7%
1610	  - exp_id: eval-adaptive-k-spatial-p50-seed44
1611	    role: evidence
1612	    result: SR=33%, avg_K=6.40, compute=64%
1613	  - exp_id: eval-adaptive-k-spatial-p75-seed42
1614	    role: evidence
1615	    result: SR=31%, avg_K=5.02, compute=50.3%
1616	  - exp_id: eval-adaptive-k-spatial-p75-seed43
1617	    role: evidence
1618	    result: SR=34%, avg_K=5.03, compute=50.3%
1619	  - exp_id: eval-adaptive-k-spatial-p25-seed42
1620	    role: evidence
1621	    result: SR=33%, avg_K=7.65, compute=76.3%
1622	  - exp_id: eval-adaptive-k-spatial-p25-seed43
1623	    role: evidence
1624	    result: SR=30%, avg_K=7.60, compute=76.3%
1625	  depends_on:
1626	  - D078
1627	  - D077
1628	- id: D086
1629	  date: 2026-05-20 12:29 UTC
1630	  summary: 'D086: OpenVLA 0% SR 确认为 applicability boundary negative result，取消 plan_802/803'
1631	  rationale: OpenVLA (tokenized VLA) 在 LIBERO Object 上 baseline=0%，CRM 无法校正完全不工作的
1632	    policy。这与论文已有的 applicability boundary claim 一致（tokenized VLA 不适用 flow-matching
1633	    的 CRM 方法）。plan_802(OpenVLA+CRM) 和 plan_803(OpenVLA magnitude) 的预期结果也是 0% 或接近 0%，花
1634	    54 GPU-hours 验证已知结论不值得。OpenVLA 0% 数据作为 Appendix negative result 呈现。
1635	  related_experiments:
1636	  - exp_id: eval-openvla-object-vla-only-seed42
1637	    role: evidence
1638	    result: SR=0%, confirms tokenized VLA boundary
1639	  depends_on:
1640	  - D077
164
…[truncated 8481 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "elapsed_ms": 54
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-21T02:44:51.997828+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"status: RUNNING\\|status: PREPARING\\|status: ANALYZING\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -60",
  "description": "Find RUNNING/PREPARING/ANALYZING experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"status: RUNNING\\|status: PREPARING\\|status: ANALYZING\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -60",
    "description": "Find RUNNING/PREPARING/ANALYZING experiments"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-21T02:44:52.390952+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md",
  "offset": "150",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md",
    "offset": "150",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-21T02:44:52.506014+00:00_

150	|------|--------|------|-----------|------|------|----|-----------|
151	| eval-perdof-object-norm02-seed50 | bjb1-32546 | crm_perdof | object | 0.2 | 50 | 10.0% | 05-21 03:22 |
152	| eval-obs-only-object-norm02-seed51 | bjb1-32546 | crm_obs_only | object | 0.2 | 51 | 17.0% | 05-21 03:20 |
153	| eval-obs-only-object-norm005-seed44 | bjb1-18228 | crm_obs_only | object | 0.05 | 44 | 12.0% | 05-21 03:16 |
154	| eval-obs-only-object-norm01-seed48 | bjb1-18228 | crm_obs_only | object | 0.1 | 48 | **仍在运行** | — |
155	
156	**norm01-seed48**: PID 507385, 状态 Rl+, 运行 55m55s, GPU1 3408MiB/29%利用率, 已完成 5/10 tasks。预计再需约 1 小时完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "elapsed_ms": 115
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-21T02:44:52.564211+00:00_

7887:    status: PREPARING
12217:    status: PREPARING
12241:    status: PREPARING
13901:    status: ANALYZING
14355:    status: PREPARING
14640:    status: PREPARING
14761:    status: PREPARING
14771:    status: PREPARING
14797:    status: PREPARING
14818:    status: PREPARING
14836:    status: PREPARING
14861:    status: PREPARING
14887:    status: PREPARING
14939:    status: PREPARING
14960:    status: PREPARING
14980:    status: PREPARING
15006:    status: PREPARING
15072:    status: PREPARING
15098:    status: PREPARING
15221:    status: PREPARING
15382:    status: PREPARING
15442:    status: PREPARING
15463:    status: PREPARING
15483:    status: PREPARING
15502:    status: PREPARING
15521:    status: PREPARING
15540:    status: PREPARING
15559:    status: PREPARING
15578:    status: PREPARING
15596:    status: PREPARING
15614:    status: PREPARING
15633:    status: PREPARING
15651:    status: PREPARING
17421:    status: PREPARING
17739:    status: PREPARING
18950:    status: PREPARING
19644:    status: RUNNING
19665:    status: RUNNING
19686:    status: RUNNING
19707:    status: RUNNING
19728:    status: RUNNING
19782:    status: RUNNING
19806:    status: RUNNING
19830:    status: RUNNING
19854:    status: RUNNING
20024:    status: RUNNING
20045:    status: RUNNING
20066:    status: RUNNING
20087:    status: RUNNING
20108:    status: RUNNING
20129:    status: RUNNING
20149:    status: RUNNING
20169:    status: RUNNING
20188:    status: RUNNING

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Bash",
  "elapsed_ms": 566
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-21T02:45:00.271654+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B2 \"status: RUNNING\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | grep \"eval-pi05\\|pi0\" ",
  "description": "Check pi0.5 experiments in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B2 \"status: RUNNING\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | grep \"eval-pi05\\|pi0\" ",
    "description": "Check pi0.5 experiments in registry"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-21T02:45:00.783251+00:00_

  eval-pi05-baseline-object-seed42:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Bash",
  "elapsed_ms": 511
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-21T02:45:00.895701+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "offset": "20020",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "offset": "20020",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-21T02:45:01.001767+00:00_

20020	      log_path: /root/autodl-tmp/logs/norm003_seed64.log
20021	    conclusion: killed
20022	    completed_at: '2026-05-21T00:54:21.580Z'
20023	  eval-obs-only-object-norm01-seed71:
20024	    status: RUNNING
20025	    retry_count: 0
20026	    created_at: '2026-05-21T00:55:00.000Z'
20027	    updated_at: '2026-05-21T00:55:00.000Z'
20028	    hypothesis: CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed71. Norm sweep filling
20029	      ε=0.1 gap.
20030	    spec:
20031	      command: python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed
20032	        71 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt
20033	        --max_correction_norm 0.1 --output_file logs/norm01_seed71.json
20034	      server: bjb2-28827
20035	      gpu:
20036	      - cuda:0
20037	      pid: '922504'
20038	      seed: 71
20039	      model_name: CRM_obs_only
20040	      data_path: LIBERO-Object
20041	      data_count: 100
20042	      checkpoint_path: /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt
20043	      log_path: /root/autodl-tmp/logs/norm01_seed71.log
20044	  eval-obs-only-object-norm005-seed72:
20045	    status: RUNNING
20046	    retry_count: 0
20047	    created_at: '2026-05-21T00:55:00.000Z'
20048	    updated_at: '2026-05-21T00:55:00.000Z'
20049	    hypothesis: CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed72. Norm sweep seed
20050	      balance.
20051	    spec:
20052	      command: python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed
20053	        72 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt
20054	        --max_correction_norm 0.05 --output_file logs/norm005_seed72.json
20055	      server: bjb2-28827
20056	      gpu:
20057	      - cuda:1
20058	      pid: '922712'
20059	      seed: 72
20060	      model_name: CRM_obs_only
20061	      data_path: LIBERO-Object
20062	      data_count: 100
20063	      checkpoint_path: /root/auto
…[truncated 308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Read",
  "elapsed_ms": 106
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-21T02:45:06.784421+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A15 \"eval-pi05-baseline\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "description": "Check pi0.5 baseline experiment details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A15 \"eval-pi05-baseline\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "description": "Check pi0.5 baseline experiment details"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-21T02:45:07.359597+00:00_

  eval-pi05-baseline-object-seed42:
    status: RUNNING
    retry_count: 0
    created_at: '2026-05-21T01:50:00.000Z'
    updated_at: '2026-05-21T01:50:00.000Z'
    hypothesis: π0.5 VLA-only baseline on LIBERO-Object seed42 — establishes reference
      success rate for flow-matching VLA, tests CRM applicability to second VLA backbone
    server: bjb2-40593
    gpu: cuda:0
    pid: 802634
    seed: 42
    spec:
      command: CUDA_VISIBLE_DEVICES=0 python3 evaluate.py --model pi05 --pi05_path
        /root/autodl-tmp/models/pi05_libero_finetuned --mode vla_only --benchmark
        object --seed 42
      server: bjb2-40593

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Bash",
  "elapsed_ms": 575
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-21T02:45:07.467453+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"DEPLOYED\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -10",
  "description": "Find DEPLOYED experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"DEPLOYED\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -10",
    "description": "Find DEPLOYED experiments"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-21T02:45:07.971551+00:00_

4431:    status: DEPLOYED
6944:    status: DEPLOYED
9063:    status: DEPLOYED
9090:    status: DEPLOYED
9406:    status: DEPLOYED

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Bash",
  "elapsed_ms": 504
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-21T02:45:11.440448+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B2 \"status: DEPLOYED\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "description": "Get DEPLOYED experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B2 \"status: DEPLOYED\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "description": "Get DEPLOYED experiment IDs"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-21T02:45:11.962786+00:00_

      obs_only 接近（两者都受限于低 norm 纠正量）。magnitude curve 低端数据点。
  eval-mag-perdof-norm03-object:
    status: DEPLOYED
--
    completed_at: '2026-05-17T10:19:28.338Z'
  eval-obs-only-object-norm01-seed46-r2:
    status: DEPLOYED
--
    completed_at: '2026-05-18T15:18:13.193Z'
  eval-obs-only-object-norm01-seed42:
    status: DEPLOYED
--
      total_rollouts: 100
  eval-perdof-object-norm01-seed42:
    status: DEPLOYED
--
    completed_at: '2026-05-18T21:05:50.448Z'
  eval-obs-only-object-norm005-seed45:
    status: DEPLOYED

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Bash",
  "elapsed_ms": 522
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-21T02:45:12.128883+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B2 \"status: ANALYZING\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "description": "Get ANALYZING experiment ID"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B2 \"status: ANALYZING\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "description": "Get ANALYZING experiment ID"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-21T02:45:12.519037+00:00_

    completed_at: '2026-05-19T22:12:05.406Z'
  eval-vla-only-object-seed49:
    status: ANALYZING

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2",
  "tool": "Bash",
  "elapsed_ms": 390
}
```

</details>

---

### Assistant

_source line 85 · 2026-05-21T02:46:09.406216+00:00_

Now I have enough context. Let me write the handoff.

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- **GPU 白名单**：必须查 `get_project_status` 的 `execution.gpu_ids`，只能用白名单内的 GPU。即使 Director 指定白名单外的 GPU 也必须 push back
- **服务器 Python 路径**：bjb1-32546 和 bjb1-18228 用 conda（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），不要假设 `python` 在 PATH 中。bjb2-28827/bjb2-40593 用 `python3`
- **CoRL DDL 2026-05-29**：剩余 8 天。Plan A LOCKED（Object 18.3%±2.1%, Spatial 35.0%±1.0%），不要动 LOCKED 数据
- **OpenVLA CRM 线已 CLOSED (D093)**：0% SR，near-deterministic，不要再投入 GPU
- **Cron false positive 是系统性问题**：eval 脚本不写 sentinel/W&B → cron 5× 检测无标记 → 误判 failed。**不要盲信 cron 的 failed 标记**，必须 tail 日志 + 检查 output JSON 确认实际状态
- **Table 1 只用 norm02 数据**：seed42 的 norm02 结果 (20%) 不纳入主分析 (D084)，保持 n=6 (16.8%±1.8%)
- **submit_training_job 命令必须自带环境激活前缀**：不能裸 `python`

### 2. 🖥️ 基础设施快照
- **4 台服务器**：
  - `bjb2-40593`：cuda:0 跑 π0.5 baseline (PID 802634)。工作目录 `/root/acr-vla-conformal-refinement/`。磁盘根分区 89% ⚠️ 仅 46GB 可用
  - `bjb1-32546`：6 GPU。conda 环境。工作目录 `/root/acr-vla-conformal-refinement/`。磁盘 400GB 可用 (4%)
  - `bjb1-18228`：3 GPU 活跃 (cuda:0/2/3)。conda 环境。磁盘根分区 92% ⚠️
  - `bjb2-28827`：5 GPU 活跃 (cuda:0-4)。工作目录 `/root/acr-vla-conformal-refinement/`。磁盘 399GB 可用 (5%)
- **模型路径**：CRM checkpoint `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`；SmolVLA 各服务器已部署
- **π0.5 模型**：`/root/autodl-tmp/models/pi05_libero_finetuned`（bjb2-40593）
- **代码**：`src/evaluate.py`（注意 `src/` 前缀），`src/train_crm.py`
- **活跃进程**：19 RUNNING（见 report.md 表），含 norm sweep seeds (64-75) + seed66 (bjb1-18228) + π0.5 baseline

### 3. 📊 当前状态
- **刚完成**：D092 Plan A Object GO (18.3%±2.1%)，D094 Plan A Spatial GO (35.0%±1.0%)，D093 OpenVLA CRM CLOSED (0%)，D095/D096 π0.5 实验线启动
- **RUNNING (19)**：
  - Norm sweep 补种：bjb1-32546 上 10 个（norm003/norm01/norm005 seeds 51-65），bjb2-28827 上 5 个（seeds 71-75），bjb1-18228 上 3 个（seed66 × 3 norms）
  - **π0.5 baseline**：bjb2-40593 cuda:0 (PID 802634)，结果决定是否启动 CRM pipeline
- **ANALYZING (1)**：eval-vla-only-object-seed49
- **PREPARING (34)**：大量 norm sweep 补种队列
- **DEPLOYED (5)**：历史遗留，未清理
- **等待中**：
  - π0.5 baseline 结果 → 若 SR > 30% 且 stochastic → 启动 CRM precompute + train + Plan A eval
  - norm sweep seeds 完成 → 更新 Figure 2 magnitude curve
  - seed66 × 3 进程（bjb1-18228）被 cron 误标 failed，实际仍在跑

### 4. 📋 待办（条件触发式）
- **π0.5 baseline 完成** → 检查 SR + action diversity → SR > 30% 且 stochastic → spawn Worker 做 CRM 适配（projection layer 2048D→960D）+ precompute + train + Plan A eval
- **π0.5 baseline SR < 30% 或 near-deterministic** → 向 Director 汇报 boundary，关闭实验线
- **seed66 (bjb1-18228) 3 个进程完成** → 手动修正 conclusion=success，从 output JSON 补录 metrics
- **norm sweep 全部完成** → 生成 Figure 2 magnitude curve（ε vs SR 多 seed），更新论文
- **eval-vla-only-object-seed49 ANALYZING** → 需要 Worker 读结果 → 更新 registry
- **所有 eval 数据收齐** → Paper Agent 开始写论文各章节（P0 任务）
- **DDL 前 3 天 (~5/26)** → 论文必须完成初稿，送 Reviewer

### 5. 🎯 战略上下文
- **核心决策链**：D043 Narrative B (mechanism insight) → D077 Adaptive K 升级为核心 → D088 Learned Head NO-GO → D090 fallback Plan A → D092 Plan A GO → D095/D096 π0.5 新线
- **论文 story**："Correction Over Selection" — 分析论文，correction 是主动机制，multi-sampling 是 enabling condition，Adaptive K (K=2 L2 probe) 实现高效推理
- **Plan A 是论文核心方法**：K=2 batched forward → L2 distance → if high: argmin + CRM → 80% compute reduction vs K=10，SR 持平或更高
- **π0.5 是最后的 scope 扩展机会**：解决 M1 (narrow scope) + R2-W1-new (low absolute perf)。若 π0.5 CRM 有效，论文从 "single weak VLA" 升级为 "works across VLA families"
- **易错点**：
  - 不要把 norm01 和 norm02 数据混用（Table 1 数据混淆事故 D080）
  - 不要信 cron 的 failed 标记——必须实际检查日志和 JSON
  - Adaptive K trigger_rate 在 Plan A scale 上约 84%（Object）/ 98%（Spatial），τ 校准问题 acknowledged 但未解决（D094）
  - FMVD (ρ=0.08) 和 CRM magnitude (ρ=0.15) 都是 dead ends，不要重试
  - bjb2-40593 磁盘 89%，提交新实验前必须检查空间
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed44-r2"
}
```

</details>

---
