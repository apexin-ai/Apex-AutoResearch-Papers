# cron hook eval obs only goal norm02 seed51 20260521T054556 565039

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 2
- **Tool calls:** 17
- **Original source:** `logs/chats/archive/cron_hook_eval-obs-only-goal-norm02-seed51_20260521T054556_565039.jsonl`
- **Structured JSON:** [`a4567b05dfd9234534b4.json`](../../sessions/a4/a4567b05dfd9234534b4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-20T13:29:30.555215+00:00_

[CRON] 实验进程异常退出（失败），需要你诊断原因。
详情: Process exited without valid W&B metrics

- exp_id: eval-obs-only-goal-norm02-seed51
- project: acr-vla-conformal-refinement
- server: bjb1-32546

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-20T13:29:45.048124+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__read_experiment_plan_with_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__read_experiment_plan_with_status",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-20T13:29:45.048579+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T13:29:49.117439+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T13:29:49.117855+00:00_

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
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T13:29:49.622516+00:00_

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
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
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

_source line 7 · 2026-05-20T13:29:50.125468+00:00_

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
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T13:29:50.426550+00:00_

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
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
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

_source line 9 · 2026-05-20T13:29:51.798999+00:00_

Error: result (693,240 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-6273b5e7/c0e2eb67-1e89-44ba-8665-ad4720a83802/tool-results/mcp-agent-ml-research-read_registry-1779283791698.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-6273b5e7/c0e2eb67-1e89-44ba-8665-ad4720a83802/tool-results/mcp-agent-ml-research-read_registry-1779283791698.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2681
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T13:29:56.323692+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 1, \"results\": [{\"exp_id\": \"eval-obs-only-object-norm02-seed43-r3\", \"success\": true, \"actions\": [\"Job still running (pid=401735)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 7205
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T13:29:56.324657+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-20T13:29:44Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 451 个实验 — ANALYZING 1, DEPLOYED 4, DONE 406, PREPARING 39, RUNNING 1\\n**DONE 分布**: failed 50, killed 82, negative 33, success 241\\n\\n### GPU 占用\\n- **实际运行**: 1 张 — bjb1-32546:cuda:2(eval-obs-only-object-norm02-seed43-r3)\\n\\n### 💾 磁盘余量\\n- **bjb2-40593**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 46G/437G 可用（已用 90%） ⚠️\\n- **bjb1-18228**:\\n  - `/autodl-pub`: 816G/7.0T 可用（已用 89%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb1-32546**:\\n  - `/autodl-pub`: 890G/7.0T 可用（已用 88%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb2-28827**:\\n  - `/autodl-pub`: 4.5T/14T 可用（已用 69%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/439G 可用（已用 5%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `eval-obs-only-object-norm02-seed43-r3` | bjb1-32546 | cuda:2 | 401735 | `logs/eval-obs-only-object-norm02-seed43-r3.log` |\\n\\n### 📌 最近完成 (top 5)\\n- `eval-obs-only-goal-norm02-seed51` [failed] — 2026-05-20T13:29:30 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\n- `eval-adaptive-k-spatial-p25-seed44` [failed] — 2026-05-20T13:28:42 — EXIT_CODE=129 (non-zero)\\n- `eval-vla-only-object-seed50` [success] — 2026-05-20T13:27:12\\n- `eval-perdof-object-norm02-seed48` [success] — 2026-05-20T13:26:57\\n- `eval-openvla-object-baseline-seed42` [killed] — 2026-05-20T13:26:22 — EXIT_CODE=124 (timeout — exceeded timeout_hours)\\n\\n### 🔴 最近失败原因 (top 3)\\n- `eval-obs-only-goal-norm02-
…[truncated 7497 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6702
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T13:29:56.330399+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-20 06:17 UTC | 更新原因: Fix Long OOD data to match D081, update RUNNING section per Reviewer observation\\n\\n> 详见 paper_framing.md（D077: Adaptive K 升级为核心贡献）\\n\\n## 核心方向\\n**Adaptive inference-time compute for frozen VLAs** — K=2 L2 distance 作为不确定性信号，自适应决定每步推理次数。CRM correction>selection 分析作为支撑。\\n\\n## 投稿目标\\n**CoRL 2026** DDL **2026-05-29**。剩余 ~9 天。\\n\\n## D077 方向转换（用户硬要求）\\n- Adaptive K = 论文**核心贡献**（方法）\\n- K=10 分析降为 supporting evidence\\n\\n## 信号候选 (CLOSED)\\n| 信号 | ρ vs K10_var | 结论 |\\n|------|-------------|------|\\n| **K=2 L2 distance** | **0.9979** | **✅ GO — 唯一可用信号** |\\n| CRM correction magnitude | 0.1523 | ❌ NO-GO (D079) |\\n| FMVD | 0.0825 | ❌ NO-GO |\\n\\n## Adaptive K Sweep (Object) — 12/12 DONE ✅\\n| 阈值 | seeds | SR (mean) | avg_K | fast_path% | vs K=10 |\\n|------|-------|-----------|-------|-----------|---------|\\n| P90 | 3/3 ✅ | 13.3% | ~2.6 | ~93% | 74% |\\n| P75 | 3/3 ✅ | 13.7% | ~3.1 | ~87% | 79% |\\n| **P50** | **3/3 ✅** | **15.3%** | **~3.8** | **~77%** | **~91%** |\\n| P25 | 3/3 ✅ | 14.3% | ~4.8 | ~65% | ~85% |\\n\\n**P50 = Pareto 最优 (D078)**。\\n\\n## RUNNING 实验\\n- bjb2-40593: Spatial Adaptive K P50 seed42 (rollout 中)\\n- bjb1-18228: Long VLA-only seed54, Long CRM seed53, Spatial VLA-only seed53\\n- bjb1-32546: Long CRM seed54, Spatial VLA-only seed54\\n- 更多部署中（Agent 处理综合指令）\\n\\n## 待部署\\n1. **Spatial Adaptive K P50 seed43, seed44**\\n2. **Random Selection baseline seed42, seed44** (plan_600)\\n3. **CRM Object K=10 norm02 seed42** (Table 1 n=6→n=7)\\n4. **fig3_kvalue 重新生成**\\n\\n## 论文 CRITICAL 待解决\\n1. **evaluate.py 推理模式确认** — Agent P0\\n2. **Spatial CRM K=10 n=8 溯源** — registry 只有 n=7, Agent 调查中\\n3. **OOD Long/Goal 数据全量更新** — Paper Agent 处理中\\n4. **P25 n=3 更新** — Paper Agent 处理中\\n\\n## 核心实验结果 (LOCKED,
…[truncated 2698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 6204
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T13:29:56.431357+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_pipeline_openvla-crm-bjb2-28827_20260520T132403\", \"task_type\": \"pipeline:openvla-crm-bjb2-28827\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-20T13:24:03.620093+00:00\", \"ended_at\": null}], \"count\": 1}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 6004
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T13:30:01.216081+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-obs-only-goal-norm02-seed51'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-obs-only-goal-norm02-seed51'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T13:30:02.169478+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/on-experiment-failed.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/on-experiment-failed.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T13:30:02.471195+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0876}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1255
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T13:30:02.471638+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_6273b5e7.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T13:30:02.471878+00:00_

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
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T13:30:02.522645+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_6273b5e7.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T13:30:07.591223+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'DONE', 'conclusion': 'failed'}",
  "fields": "['*']",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'DONE', 'conclusion': 'failed'}",
    "fields": "['*']",
    "limit": "5"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T13:30:08.545439+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/on-experiment-failed.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/on-experiment-failed.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T13:30:08.916589+00:00_

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
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
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

_source line 23 · 2026-05-20T13:30:09.017791+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-goal-norm02-seed51\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:48:04.411Z\", \"updated_at\": \"2026-05-20T13:29:26.541Z\", \"hypothesis\": \"CRM obs_only K=10 norm02 on LIBERO-Goal seed51. Multi-seed supplement to address R2 seed imbalance concern. CRM should outperform VLA-only baseline on Goal OOD.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 ... python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 51 --n_rollouts 10 --K 10 --crm_checkpoint .../crm_best.pt --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"401661\", \"log_path\": \"logs/eval-obs-only-goal-norm02-seed51.log\", \"submitted_at\": \"2026-05-20T10:51:48.054Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM obs_only (K=10, norm02)\", \"seed\": 51, \"wall_clock_seconds\": 9448.7, \"gpu_hours\": 2.62}, \"reproduce\": {\"finished_at\": \"2026-05-20T13:29:19.616Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T13:29:16.734Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T13:29:36.596426+00:00\"}]}}, \"eval-adaptive-k-spatial-p25-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:44:42.913Z\", \"updated_at\": \"2026-05-20T13:28:42.550Z\", \"hypothesis\": \"Adaptive K with τ=P25 (0.054959, Object-calibrated) on LIBERO-Spatial seed44. Third seed for cross-benchmark P25 threshold sweep. Completes Spatial sweep table (P25/P50/P75/P90 × 3 seeds).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement &&
…[truncated 5989 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1426
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T13:30:09.068527+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "Glob",
  "elapsed_ms": 523
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T13:30:09.068969+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "Glob",
  "elapsed_ms": 152
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T13:30:22.068535+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_project_resource_usage,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_project_resource_usage,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T13:30:22.119215+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T13:30:25.833408+00:00_

called mcp__agent-ml-research__get_project_resource_usage

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_project_resource_usage</summary>

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
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T13:30:25.985712+00:00_

called mcp__agent-ml-research__load_project_config

<details open><summary>🔧 Tool call — mcp__agent-ml-research__load_project_config</summary>

```json
{
  "project_name": "acr-vla-conformal-refinement",
  "section": "execution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "mcp__agent-ml-research__load_project_config",
  "tool_args": {
    "project_name": "acr-vla-conformal-refinement",
    "section": "execution"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T13:30:27.091133+00:00_

{"result":"{\"success\": true, \"data\": {\"allocated_gpus\": [], \"actually_running_gpus\": [{\"server\": \"bjb1-32546\", \"gpu_id\": \"cuda:2\", \"exp_id\": \"eval-obs-only-object-norm02-seed43-r3\"}], \"allocated_but_idle\": [], \"registered_but_hw_idle\": [], \"unregistered_but_hw_active\": [], \"running_experiments\": [{\"exp_id\": \"eval-obs-only-object-norm02-seed43-r3\", \"gpus\": [\"cuda:2\"], \"util_avg\": null}], \"worker_pool\": {\"total\": 1, \"gpu_tasks\": 0, \"cpu_tasks\": 1, \"details\": [{\"worker_id\": \"worker_pipeline_openvla-crm-bjb2-28827_20260520T132403\", \"task\": \"pipeline:openvla-crm-bjb2-28827\"}]}, \"summary\": \"分配 0 张, 实际跑 1 张 | Worker 1 (GPU 0 / CPU 1)\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "elapsed_ms": 1257
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T13:30:27.091540+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"acr-vla-conformal-refinement\", \"section\": \"execution\", \"config\": {\"execution\": {\"account\": \"root\", \"gpu_constraint\": [\"autodl-4090:cuda:0\"], \"gpu_ids\": [\"bjb2-40593:cuda:0\", \"bjb1-18228:cuda:0\", \"bjb1-18228:cuda:1\", \"bjb1-18228:cuda:2\", \"bjb1-18228:cuda:3\", \"bjb1-32546:cuda:0\", \"bjb1-32546:cuda:1\", \"bjb1-32546:cuda:2\", \"bjb1-32546:cuda:3\", \"bjb1-32546:cuda:4\", \"bjb1-32546:cuda:5\", \"bjb2-28827:cuda:0\", \"bjb2-28827:cuda:1\", \"bjb2-28827:cuda:2\", \"bjb2-28827:cuda:3\", \"bjb2-28827:cuda:4\", \"bjb2-28827:cuda:5\"], \"project_path\": \"/root/acr-vla-conformal-refinement\", \"servers\": [\"bjb2-40593\", \"bjb1-18228\", {\"account\": \"root\", \"server\": \"bjb1-32546\"}, {\"account\": \"root\", \"server\": \"bjb2-28827\"}]}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 1105
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T13:30:48.032020+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "diagnose:eval-obs-only-goal-norm02-seed51",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务：诊断实验失败原因\n\n实验 `eval-obs-only-goal-norm02-seed51` 在 bjb1-32546 上失败。\n\n**失败信息**：\n- failure_reason: \"process dead 5× with no sentinel/W&B — auto-resolved as failed\"\n- server: bjb1-32546\n- GPU: cuda:1\n- PID: 401661\n- log_path: logs/eval-obs-only-goal-norm02-seed51.log\n- 运行时长: ~2.6 hours (9448.7s)\n- command: `CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 51 --n_rollouts 10 --K 10 --crm_checkpoint .../crm_best.pt --max_correction_norm 0.2`\n\n**你的任务**：\n1. SSH 到 bjb1-32546 读取日志文件 `/root/acr-vla-conformal-refinement/logs/eval-obs-only-goal-norm02-seed51.log`（用 ssh_read_only 读最后 200 行）\n2. 检查是否有 OOM、segfault、Python traceback、或其他错误信息\n3. 检查 tmux session 是否还存在：`tmux list-sessions 2>/dev/null | grep eval-obs-only-goal-norm02-seed51`\n4. 检查 dmesg 是否有 OOM killer 记录：`dmesg -T 2>/dev/null | tail -50 | grep -i oom`\n5. 检查该 GPU 的当前状态：`nvidia-smi`\n6. 同时检查 `/root/runs/acr-vla-conformal-refinement/eval-obs-only-goal-norm02-seed51.log`（cron 可能把日志重定向到 ~/runs/ 下）\n7. 检查是否有 JSON 输出文件生成（可能部分完成了任务）：`ls -la /root/acr-vla-conformal-refinement/logs/eval*goal*seed51*`\n\n**产出要求**：\n- 明确失败根因（OOM / 进程被 kill / 代码错误 / 服务器问题 / 超时）\n- 如果有部分结果，列出哪些 task 完成了\n- 判断是否可以直接重试（transient failure）还是需要改代码\n- 把诊断结论写在产出的最后一段，清晰标注 `## 诊断结论`\n",
  "tool_groups": "['ssh']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "diagnose:eval-obs-only-goal-norm02-seed51",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务：诊断实验失败原因\n\n实验 `eval-obs-only-goal-norm02-seed51` 在 bjb1-32546 上失败。\n\n**失败信息**：\n- failure_reason: \"process dead 5× with no sentinel/W&B — auto-resolved as failed\"\n- server: bjb1-32546\n- GPU: cuda:1\n- PID: 401661\n- log_path: logs/eval-obs-only-goal-norm02-seed51.log\n- 运行时长: ~2.6 hours (9448.7s)\n- command: `CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 51 --n_rollouts 10 --K 10 --crm_checkpoint .../crm_best.pt --max_correction_norm 0.2`\n\n**你的任务**：\n1. SSH 到 bjb1-32546 读取日志文件 `/root/acr-vla-conformal-refinement/logs/eval-obs-only-goal-norm02-seed51.log`（用 ssh_read_only 读最后 200 行）\n2. 检查是否有 OOM、segfault、Python traceback、或其他错误信息\n3. 检查 tmux session 是否还存在：`tmux list-sessions 2>/dev/null | grep eval-obs-only-goal-norm02-seed51`\n4. 检查 dmesg 是否有 OOM killer 记录：`dmesg -T 2>/dev/null | tail -50 | grep -i oom`\n5. 检查该 GPU 的当前状态：`nvidia-smi`\n6. 同时检查 `/root/runs/acr-vla-conformal-refinement/eval-obs-only-goal-norm02-seed51.log`（cron 可能把日志重定向到 ~/runs/ 下）\n7. 检查是否有 JSON 输出文件生成（可能部分完成了任务）：`ls -la /root/acr-vla-conformal-refinement/logs/eval*goal*seed51*`\n\n**产出要求**：\n- 明确失败根因（OOM / 进程被 kill / 代码错误 / 服务器问题 / 超时）\n- 如果有部分结果，列出哪些 task 完成了\n- 判断是否可以直接重试（transient failure）还是需要改代码\n- 把诊断结论写在产出的最后一段，清晰标注 `## 诊断结论`\n",
    "tool_groups": "['ssh']"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-20T13:30:51.149606+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_diagnose_eval-obs-only-goal-norm02-seed51_20260520T133048\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_diagnose_eval-obs-only-goal-norm02-seed51_20260520T133048.log\", \"setup_data\": {}, \"message\": \"Worker worker_diagnose_eval-obs-only-goal-norm02-seed51_20260520T133048 started. Use get_worker_status('worker_diagnose_eval-obs-only-goal-norm02-seed51_20260520T133048') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 3117
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T13:31:14.827450+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 1/17 | Worker 2 (GPU 0 / CPU 2) | 磁盘: bjb1-32546 400G/438G (4%)\n\n**[实验失败] eval-obs-only-goal-norm02-seed51**\n\n- 服务器: bjb1-32546, cuda:1\n- Hypothesis: CRM obs_only K=10 norm02 on LIBERO-Goal seed51 (multi-seed supplement)\n- 失败原因: process dead 5× with no sentinel/W&B — auto-resolved as failed\n- 运行时长: ~2.6h\n\n已派 Worker SSH 诊断日志，等待根因确认后决定是否重试。\n\n**同时注意**: `eval-adaptive-k-spatial-p25-seed44` 也刚失败 (EXIT_CODE=129, SIGHUP)，bjb2-28827。两个失败实验在不同服务器，可能是独立的 transient failure。\n\n**GPU 饱和度严重不足**: 17 张 GPU 分配，仅 1 张在跑 (eval-obs-only-object-norm02-seed43-r3)。等诊断结果回来后，如果确认是 transient failure，将立即重试失败实验并批量铺设 PREPARING 中的 38 项待处理实验。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 1/17 | Worker 2 (GPU 0 / CPU 2) | 磁盘: bjb1-32546 400G/438G (4%)\n\n**[实验失败] eval-obs-only-goal-norm02-seed51**\n\n- 服务器: bjb1-32546, cuda:1\n- Hypothesis: CRM obs_only K=10 norm02 on LIBERO-Goal seed51 (multi-seed supplement)\n- 失败原因: process dead 5× with no sentinel/W&B — auto-resolved as failed\n- 运行时长: ~2.6h\n\n已派 Worker SSH 诊断日志，等待根因确认后决定是否重试。\n\n**同时注意**: `eval-adaptive-k-spatial-p25-seed44` 也刚失败 (EXIT_CODE=129, SIGHUP)，bjb2-28827。两个失败实验在不同服务器，可能是独立的 transient failure。\n\n**GPU 饱和度严重不足**: 17 张 GPU 分配，仅 1 张在跑 (eval-obs-only-object-norm02-seed43-r3)。等诊断结果回来后，如果确认是 transient failure，将立即重试失败实验并批量铺设 PREPARING 中的 38 项待处理实验。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T13:31:19.152461+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 4325
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-20T13:31:23.258797+00:00_

已派 Worker 诊断 `eval-obs-only-goal-norm02-seed51` 失败原因（bjb1-32546 上 process dead 5× with no sentinel/W&B），并向 Director 汇报。等待 Worker 回调后确认根因再决定重试策略。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 37 · 2026-05-21T05:45:08.606796+00:00_

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
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-21T05:45:56.563391+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单: bjb2-40593:cuda:0, bjb1-18228:cuda:0-3, bjb1-32546:cuda:0-5, bjb2-28827:cuda:0-5（共 17 张）。白名单外的 GPU 即使 Director 指令也必须 push back
- Table 1 CRM Object 只用 norm02 数据（D080），seed42 SR=20% 为 outlier 不纳入（D084）
- Long OOD 结果必须用 cautious wording（MW-U p=0.061 n.s.，D081）
- evaluate.py 使用 batched inference（D082），延迟表和效率分析需基于此
- OpenVLA 实验线已恢复（D087 撤回 D086），v2 baseline SR=69% 可用

### 2. 🖥️ 基础设施快照
- **4 台服务器**，账号均为 root，工作目录 `/root/acr-vla-conformal-refinement`
- Python: `/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 激活方式: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- CRM checkpoint: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`
- HF cache: `/root/autodl-tmp/.hf_cache`（必须设 HF_HOME + HF_HUB_OFFLINE=1 + TRANSFORMERS_OFFLINE=1）
- 环境变量: `MUJOCO_GL=egl`（headless 渲染）
- **活跃进程**: eval-obs-only-object-norm02-seed43-r3 (PID 401735, bjb1-32546:cuda:2, cron 监控中)
- **活跃 Worker**: worker_pipeline_openvla-crm-bjb2-28827（CPU task，OpenVLA pipeline）
- 磁盘: bjb1-32546 400G/438G (4%), bjb1-18228 400G/438G (4%), bjb2-28827 399G/439G (5%), bjb2-40593 46G/437G (90%) ⚠️

### 3. 📊 当前状态
- 刚收到 `eval-obs-only-goal-norm02-seed51` 失败回调（process dead 5×, bjb1-32546:cuda:1）
- 已派诊断 Worker (`worker_diagnose_eval-obs-only-goal-norm02-seed51_20260520T133048`) SSH 查日志，**尚未回调**
- 已向 Director 汇报失败 + GPU 饱和度不足（1/17）
- `eval-adaptive-k-spatial-p25-seed44` 也刚失败（EXIT_CODE=129, bjb2-28827），未单独诊断
- **RUNNING**: eval-obs-only-object-norm02-seed43-r3 (bjb1-32546:cuda:2)
- **PREPARING**: 38-39 项待处理实验（详见 report.md 待处理段）
- **GPU 饱和度极低**: 17 张分配仅 1 张在跑

### 4. 📋 待办
- 诊断 Worker 回调 → 根据根因决定：transient failure 则立即重试 eval-obs-only-goal-norm02-seed51；代码问题则修复后重试
- eval-adaptive-k-spatial-p25-seed44 (EXIT_CODE=129) → 需要单独诊断或直接重试（SIGHUP 通常是 transient）
- eval-obs-only-object-norm02-seed43-r3 完成回调 → 按 on-experiment-done 处理，更新 Table 1 Object CRM seed 数
- **紧急**: GPU 饱和度 1/17 → 诊断完成后立即批量铺设 PREPARING 中的实验（Spatial Adaptive K P50 seeds、Random Selection baseline、CRM Object seed42 补充等）
- OpenVLA pipeline Worker 完成 → 整合 OpenVLA baseline 结果到论文

### 5. 🎯 战略上下文
- **投稿目标**: CoRL 2026, DDL 2026-05-29（剩 ~9 天）
- **核心方向**: Adaptive inference-time compute for frozen VLAs。K=2 L2 distance 是唯一可用不确定性信号（ρ=0.9979），P50 阈值为 Pareto 最优
- **关键决策链**: D078 P50最优 → D079 CRM magnitude NO-GO → D080 Table1 norm02 n=6 → D081 Long OOD cautious → D082 batched inference → D083 Spatial n=8 clean → D084 seed42 outlier 排除 → D085 跨 benchmark 阈值迁移 → D087 OpenVLA 恢复
- **Object CRM K=10**: 16.8±1.8% (n=6) vs VLA 10.9%, p=9.5e-5***（核心 supporting evidence）
- **Spatial Adaptive K sweep 是当前最大空缺**——Object 12/12 done，Spatial 需要 P50/P75/P25/P90 × 3 seeds
- **易错点**: (1) bjb2-40593 磁盘 90% 快满，提交实验前必须检查 (2) 很多实验反复失败是 transient（进程被 kill、OOM），重试通常解决 (3) seed42 Object CRM SR=20% 是 outlier 不纳入 Table 1 (4) submit_training_job 的 command 必须包含完整环境激活链（source conda + cd + 环境变量）
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-obs-only-goal-norm02-seed51"
}
```

</details>

---
