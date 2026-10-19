# cron hook eval mag obsonly norm03 b2 20260515T101504 914236

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 2
- **Tool calls:** 16
- **Original source:** `logs/chats/archive/cron_hook_eval-mag-obsonly-norm03-b2_20260515T101504_914236.jsonl`
- **Structured JSON:** [`6eaee67a292f1c869004.json`](../../sessions/6e/6eaee67a292f1c869004.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-15T07:10:40.112437+00:00_

[CRON] 实验进程异常退出（失败），需要你诊断原因。
详情: Process exited without valid W&B metrics

- exp_id: eval-mag-obsonly-norm03-b2
- project: acr-vla-conformal-refinement
- server: bjb1-18228
- log_path: logs/eval_mag_obsonly_norm03.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-15T07:10:54.689807+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__get_worker_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__get_worker_status",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-15T07:10:54.740368+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T07:11:01.818955+00:00_

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
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
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

_source line 5 · 2026-05-15T07:11:02.270478+00:00_

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
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T07:11:02.773645+00:00_

Error: result (128,966 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-f4d6c40d/bd11dcaf-49d0-4eba-b739-951cae2a0f3f/tool-results/mcp-agent-ml-research-read_registry-1778829062419.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-f4d6c40d/bd11dcaf-49d0-4eba-b739-951cae2a0f3f/tool-results/mcp-agent-ml-research-read_registry-1778829062419.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 954
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T07:11:02.774046+00:00_

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
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
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

_source line 8 · 2026-05-15T07:11:02.876808+00:00_

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
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T07:11:28.390199+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 17, \"results\": [{\"exp_id\": \"eval-reconvla-object\", \"success\": true, \"actions\": [\"Job still running (pid=9659)\"]}, {\"exp_id\": \"eval-acr-object-v4-perdof\", \"success\": true, \"actions\": [\"Job still running (pid=11116)\"]}, {\"exp_id\": \"eval-acr-object-v4-obs-only\", \"success\": true, \"actions\": [\"Job still running (pid=13806)\"]}, {\"exp_id\": \"eval-mag-perdof-norm003\", \"success\": true, \"actions\": [\"Job still running (pid=13185)\"]}, {\"exp_id\": \"eval-mag-perdof-norm005\", \"success\": true, \"actions\": [\"Job still running (pid=13456)\"]}, {\"exp_id\": \"eval-mag-perdof-norm02\", \"success\": true, \"actions\": [\"Job still running (pid=13728)\"]}, {\"exp_id\": \"eval-mag-perdof-norm03\", \"success\": true, \"actions\": [\"Job still running (pid=14260)\"]}, {\"exp_id\": \"eval-mag-obsonly-norm005\", \"success\": true, \"actions\": [\"Job still running (pid=14854)\"]}, {\"exp_id\": \"eval-mag-obsonly-norm02\", \"success\": true, \"actions\": [\"Job still running (pid=15190)\"]}, {\"exp_id\": \"eval-vla-mean-object\", \"success\": true, \"actions\": [\"Job still running (pid=18808)\"]}, {\"exp_id\": \"eval-acr-object-v4-scalar\", \"success\": true, \"actions\": [\"Job still running (pid=14003)\"]}, {\"exp_id\": \"eval-acr-spatial-v4-scalar-r2\", \"success\": true, \"actions\": [\"Job still running (pid=311881)\"]}, {\"exp_id\": \"eval-acr-spatial-v4-small-r2\", \"success\": true, \"actions\": [\"Job still running (pid=312150)\"]}, {\"exp_id\": \"eval-acr-spatial-v4-obs-only-r3\", \"success\": true, \"actions\": [\"Job still running (pid=312420)\"]}, {\"exp_id\": \"eval-acr-object-obs-only-norm02\", \"success\": true, \"actions\": [\"Job still running (pid=44270)\"]}, {\"exp_id\": \"eval-mag-obsonly-norm003-b2\", \"success\": true, \"actions\": [\"Job still running (pid=227434)\"]}, {\"exp_id\": \"eval-mag-obsonly-norm03-r2\", \"success\": true, \"actions\": [\"Skipped (created 
…[truncated 68 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 26119
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T07:11:28.390759+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval-mag-obsonly-norm03-r2 | Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127 fix). Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness. | — | — | — |\\n| eval-acr-spatial-v4-obs-only-r3 | Restart from T6. obs_only CRM v3-norm with max_correction_norm=0.1 on spatial. If obs_only >= perdof, conformal features need restructuring. | — | — | — |\\n| eval-acr-spatial-v4-small-r2 | Restart from T7. ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on spatial. Full per-DOF uncertainty pipeline. | — | — | — |\\n\\n## 待处理\\n- eval-mag-obsonly-norm-0p3-r3（准备中）\\n- eval-mag-obsonly-norm-0.3-r3: Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness over perdof.（准备中）\\n- eval-mag-obsonly-norm03-b2: Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127). Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade, strong evidence for obs_only robustness.（准备中）\\n- eval-mag-obsonly-norm03: Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness.（准备中）\\n- eval-acr-object-v4-default: Ablation: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Tests whether m
…[truncated 3032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 25616
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T07:11:28.391143+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-15 05:36 UTC | 更新原因: Reviewer CRITICAL: bjb2-40593 ghost process blocking obs_only norm=0.03; object eval perdof 0% warning; updated task status\\n\\n## 核心方向\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\\n\\n## 投稿目标\\n**CoRL 2026**（abstract DDL ~May 26, full paper DDL ~Jun 2）。剩余 ~11 天。\\n\\n## 当前进展\\n- **阶段**: Phase 2c — Spatial 四路重启中 + Object 6-way + Magnitude sweep\\n- **MVP**: PASS\\n- **Claims 2+3 已放弃** (D022, D023): CoRL 聚焦单 Claim (CRM correction)\\n- **D027 CRITICAL**: Reviewer matched-task analysis — perdof = argmin = 42.9% on T0-T6（**0pp delta**）。Kill criteria TRIGGERED on spatial.\\n- **obs_only on T0-T5**: 40% vs perdof/argmin 35%（+5pp）— obs_only CRM 可能仍有效\\n- **Baselines 锁定**: spatial 30% (K=1), VLA-mean 31% (K=10), **argmin K=10: 34% (完整 10-task)**, object 12% (K=1), 12% (VLA-mean-object partial)\\n\\n## Per-Task Data (Spatial, kill 前最完整快照)\\n\\n| Task | argmin | perdof | obs_only | scalar |\\n|------|--------|--------|----------|--------|\\n| T0 | 60% | 60% | 90% | 60% |\\n| T1 | 100% | 100% | 100% | 100% |\\n| T2 | 0% | 10% | 0% | 10% |\\n| T3 | 30% | 40% | 40% | — |\\n| T4 | 10% | 0% | 10% | — |\\n| T5 | 10% | 0% | 0% | — |\\n| T6 | 90% | 90% | 90% (r3) | — |\\n| T7 | 0% | 10% (r2) | running | — |\\n| T8 | 30% | — | — | — |\\n| T9 | 10% (r2) | — | — | — |\\n\\nMatched T0-T5: obs_only 40% > perdof = argmin = 35%\\n\\n## Spatial Eval — bjb1-18228（四路重启 RUNNING）\\n\\n| GPU | 实验 | 重启 Offset | 剩余 Tasks | 预计时间 |\\n|-----|------|------------|-----------|---------|\\n| cuda:0 | argmin-r2 | T9 | 0 | ✅ DONE (34%, 34/100) |\\n| cuda:1 | scalar-r2 | T3 | 7 | ~3h |\\n| cuda:2 | perdof-r2 | T7 | 3 | ~1.5h |\\n| cuda:3 | obs-onl
…[truncated 4791 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 25514
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T07:11:34.768047+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-mag-obsonly-norm03-b2'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-mag-obsonly-norm03-b2'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T07:11:36.675108+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3617}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1907
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T07:11:36.675542+00:00_

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
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/on-experiment-failed.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T07:11:36.977134+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_f4d6c40d.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T07:11:37.078516+00:00_

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
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T07:11:37.079208+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_f4d6c40d.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T07:11:42.778507+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'DONE'}",
  "fields": "['*']",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'DONE'}",
    "fields": "['*']",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T07:11:43.031108+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-argmin-only-spatial-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:03.322Z\", \"updated_at\": \"2026-05-15T06:39:37.926Z\", \"hypothesis\": \"Restart from T9. ReconVLA baseline (scalar Euclidean argmin, K=10) on spatial. Isolate argmin base action selection from CRM correction.\", \"parent\": \"eval-argmin-only-spatial\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --start_task 9\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 311609, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial-r2.log\", \"submitted_at\": \"2026-05-15T05:14:30.112Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 10, \"model_name\": \"ReconVLA argmin K=10 (restart from T9)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial task 9 only\", \"checkpoint_source\": \"N/A (reconvla mode, no CRM)\", \"wall_clock_seconds\": 5107.8, \"gpu_hours\": 1.42}, \"reproduce\": {\"finished_at\": \"2026-05-15T06:35:00.746Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:35:02.954210+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_trials\": 100, \"per_task\": {\"T0_between_plate_and_ramekin\": 0.6, \"T1_next_to_ramekin\": 1, \"T2_from_table_center\": 0, \"T3_on_cookie_box\": 0.3, \"T4_in_top_drawer\": 0.1, \"T5_on_ramekin\": 0.1, \"T6_next_to_cookie_box\": 0.9, \"T7_on_stove\": 0, \"T8_next_to_plate\": 0.3, \"T9_on_wooden_cabinet\": 0.1}, \"note\": \"T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result.\"}, \"conclusion\": \"success\", \"notes\": \"10-task complete. T9 (wooden_cabinet) = 10%. Overall 34% (34/100). T0-T8 from original run, T9 from r2 restart.
…[truncated 7612 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 252
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T07:11:43.031808+00:00_

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
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/on-experiment-failed.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T07:11:43.082444+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T07:11:58.804641+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | grep -A 30 \"eval-mag-obsonly-norm03-b2\"",
  "description": "Search registry for eval-mag-obsonly-norm03-b2 experiment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | grep -A 30 \"eval-mag-obsonly-norm03-b2\"",
    "description": "Search registry for eval-mag-obsonly-norm03-b2 experiment"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T07:11:58.958530+00:00_

  eval-mag-obsonly-norm03-b2:
    status: PREPARING
    retry_count: 0
    created_at: '2026-05-15T07:05:41.192Z'
    updated_at: '2026-05-15T07:10:37.800Z'
    hypothesis: 'Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Retry
      of eval-mag-obsonly-norm03 (EXIT_CODE=127). Fills obs_only norm=0.3 gap. perdof
      norm=0.3 shows T1 drop to 50% — if obs_only doesn''t degrade, strong evidence
      for obs_only robustness.'
    parent: eval-mag-obsonly-norm03
    spec:
      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
        base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py
        --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint
        /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm
        0.3 --output_file logs/eval_mag_obsonly_norm03.json"
      server: bjb1-18228
      gpu:
      - cuda:0
      pid: '328010'
      log_path: ~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b2.log
      submitted_at: '2026-05-15T07:05:55.705Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
    conclusion: failed
    notes: 'Killed: duplicate of eval-mag-obsonly-norm03-r2 on same cuda:0. r2 had
      15min more progress. Both wrote same output_file, causing potential corruption.'
    reproduce:
      finished_at: '2026-05-15T07:10:36.759Z'
    failure_reason: EXIT_CODE=143 (SIGTERM — graceful kill)
    extra:
      hook_events:
      - event: on_failed
        action: agent
        ts: '2026-05-15T07:10:39.645469+00:00'
  eval-mag-obsonly-norm-0.3-r3:
    status: PREPARING
    retry_count: 0
    created_at: '2026-05-15T07:10:44.647Z'
    updated_at: '2026-05-15T07:10:50.786Z'
    hypothesis: 'Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3
      on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn''t degrade
      at same norm, strong evidence for 
…[truncated 310 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "Bash",
  "elapsed_ms": 153
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T07:12:08.664796+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | grep -A 25 \"eval-mag-obsonly-norm03-r2:\"",
  "description": "Check eval-mag-obsonly-norm03-r2 registry entry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | grep -A 25 \"eval-mag-obsonly-norm03-r2:\"",
    "description": "Check eval-mag-obsonly-norm03-r2 registry entry"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T07:12:08.765808+00:00_

  eval-mag-obsonly-norm03-r2:
    status: RUNNING
    retry_count: 0
    created_at: '2026-05-15T06:49:38.786Z'
    updated_at: '2026-05-15T07:10:07.073Z'
    hypothesis: 'Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127 fix). Magnitude sweep:
      obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof
      norm=0.3 shows T1 drop to 50% — if obs_only doesn''t degrade at same norm, strong
      evidence for obs_only robustness.'
    parent: eval-mag-obsonly-norm03
    spec:
      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
        base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py
        --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint
        /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm
        0.3 --output_file logs/eval_mag_obsonly_norm03.json"
      server: bjb1-18228
      gpu:
      - cuda:0
      pid: 325264
      log_path: ~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-r2.log
      submitted_at: '2026-05-15T06:50:02.511Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
      data_path: LIBERO spatial benchmark

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T07:12:19.839511+00:00_

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
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
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

_source line 27 · 2026-05-15T07:12:20.392278+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 552
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T07:12:20.442836+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__load_project_config",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__load_project_config",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T07:12:20.543560+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T07:12:23.304774+00:00_

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
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
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

_source line 31 · 2026-05-15T07:12:23.355415+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"acr-vla-conformal-refinement\", \"section\": \"execution\", \"config\": {\"execution\": {\"account\": \"root\", \"gpu_constraint\": [\"autodl-4090:cuda:0\"], \"gpu_ids\": [\"bjb2-40593:cuda:0\", \"bjb1-18228:cuda:0\", \"bjb1-18228:cuda:1\", \"bjb1-18228:cuda:2\", \"bjb1-18228:cuda:3\", \"bjb1-32546:cuda:0\", \"bjb1-32546:cuda:1\", \"bjb1-32546:cuda:2\", \"bjb1-32546:cuda:3\", \"bjb1-32546:cuda:4\", \"bjb1-32546:cuda:5\", \"bjb2-28827:cuda:0\", \"bjb2-28827:cuda:1\", \"bjb2-28827:cuda:2\", \"bjb2-28827:cuda:3\", \"bjb2-28827:cuda:4\", \"bjb2-28827:cuda:5\"], \"project_path\": \"/root/acr-vla-conformal-refinement\", \"servers\": [\"bjb2-40593\", \"bjb1-18228\", {\"account\": \"root\", \"server\": \"bjb1-32546\"}, {\"account\": \"root\", \"server\": \"bjb2-28827\"}]}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T07:12:42.362419+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-mag-obsonly-norm03-b2",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-mag-obsonly-norm03-b2",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T07:12:42.613761+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → DONE. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.2135}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 251
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-15T07:13:19.389348+00:00_

诊断完成。

**结论**：这是一个 stale cron 回调，无需进一步处理。

- `eval-mag-obsonly-norm03-b2`（norm=0.3, bjb1-18228 cuda:0, pid=328010）是之前被诊断为重复实验后故意 SIGTERM kill 的。Registry 已正确记录 conclusion=failed, failure_reason=EXIT_CODE=143。
- 替代实验 `eval-mag-obsonly-norm03-r2` 已在 bjb1-18228 cuda:0 上运行中（pid=325264），cron 监控正常。
- status 字段卡在 PREPARING（状态机不允许 PREPARING→DONE），但 conclusion/failure_reason/notes 齐全，不影响操作。

**资源状态**：
- 17 GPU 分配，reconcile 显示 17 个 cron 活跃（含这个已完成的 stale 条目）
- bjb1-18228: 4/4 GPU 运行中（scalar-r2, small-r2/perdof-r2, obs-only-r3, norm03-r2）
- bjb1-32546: 6/6 GPU 运行中（object eval 6-way）
- bjb2-28827: 6/6 GPU 运行中（magnitude sweep）
- bjb2-40593: 1/1 GPU 运行中（obs_only norm=0.03, pid=227434）
- Worker 池: 0（全部 GPU 已满载，无待调度任务）

无需向 Director 汇报此回调——已知的重复 kill，替代实验正在运行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 35 · 2026-05-15T10:14:07.962685+00:00_

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
  "session": "cron:hook:eval-mag-obsonly-norm03-b2",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-15T10:15:04.912320+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单严格按 `execution.gpu_ids` 执行：bjb2-40593:cuda:0, bjb1-18228:cuda:0-3, bjb1-32546:cuda:0-5, bjb2-28827:cuda:0-5（共 17 张）
- bjb2-40593 是单卡机（RTX 4090 D），只有 cuda:0，不要尝试 cuda:1+
- eval 脚本 GPU 编号始终用 `--gpu 0`（框架自动映射物理 GPU）
- obs_only norm=0.3 实验（eval-mag-obsonly-norm03 系列）已经产生 3 个重复条目（norm03, norm03-b2, norm-0.3-r3, norm-0p3-r3），当前有效的是 `eval-mag-obsonly-norm03-r2`（bjb1-18228 cuda:0），不要再创建新的
- submit_training_job 的 command 必须自带环境激活：`bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && ..."`
- output_file 路径不同实验必须不同，之前 norm03-b2 和 norm03-r2 共用 `logs/eval_mag_obsonly_norm03.json` 导致潜在数据污染

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (4× RTX 4090): 工作目录 `/root/acr-vla-conformal-refinement`, Python `/root/miniconda3/bin/python`, conda base
  - 模型: `/root/autodl-tmp/models/smolvla_libero/`, CRM checkpoints: `/root/autodl-tmp/checkpoints/crm_v3_norm/{perdof,obs_only,scalar_unc}/crm_best.pt`
  - 数据: `/root/autodl-tmp/libero_data/`
  - 活跃进程: eval-acr-spatial-v4-scalar-r2 (PID 311881, cuda:1), eval-acr-spatial-v4-small-r2 (PID 312150, cuda:2), eval-acr-spatial-v4-obs-only-r3 (PID 312420, cuda:3), eval-mag-obsonly-norm03-r2 (PID 325264, cuda:0)
- **bjb1-32546** (6× RTX 4090): 同上路径结构
  - 活跃: eval-reconvla-object (PID 9659, cuda:0), eval-acr-object-v4-perdof (PID 11116, cuda:1), eval-acr-object-v4-obs-only (PID 13806, cuda:2), eval-acr-object-v4-scalar (PID 14003, cuda:3), eval-acr-object-obs-only-norm02 (PID 44270, cuda:4), eval-vla-mean-object (PID 18808, cuda:5)
- **bjb2-28827** (6× RTX 4090): magnitude sweep
  - 活跃: eval-mag-perdof-norm003 (PID 13185), norm005 (PID 13456), norm02 (PID 13728), norm03 (PID 14260), eval-mag-obsonly-norm005 (PID 14854), norm02 (PID 15190)
- **bjb2-40593** (1× RTX 4090 D): eval-mag-obsonly-norm003-b2 (PID 227434, cuda:0) — 这是 obs_only norm=0.03 实验，reconcile 确认仍在运行
- HF cache: `/root/autodl-tmp/.hf_cache`（所有服务器）

### 3. 📊 当前状态
刚处理 eval-mag-obsonly-norm03-b2 的失败 cron 回调——这是 stale 回调，该实验之前已被诊断为重复并 SIGTERM kill，registry 已正确标记 conclusion=failed。替代实验 eval-mag-obsonly-norm03-r2 正在 bjb1-18228 cuda:0 运行中。

**RUNNING 实验（17 crons 活跃，16 GPU 满载 + 1 cron 刚创建跳过）**:
- bjb1-18228: spatial 四路重启（scalar-r2 T3起/perdof-r2 T7起/obs-only-r3 T6起 + obs_only norm=0.3 sweep）
- bjb1-32546: object 6-way eval（reconvla/perdof/obs-only/scalar/obs-only-norm02/vla-mean）
- bjb2-28827: magnitude sweep 6路（perdof 4个norm + obs_only 2个norm）
- bjb2-40593: obs_only norm=0.03（恢复运行中）

**registry 异常**: eval-mag-obsonly-norm03-b2 status=PREPARING 但 conclusion=failed，状态机不允许 PREPARING→DONE 直接跳转，需要手动修 registry.yaml 或忽略（不影响运行）

**Worker 池: 0 running**（所有工作都是 cron 监控的 GPU 实验，无 CPU 任务在跑）

### 4. 📋 待办（条件触发式）
- bjb1-18228 任一 spatial 实验完成 cron 回调 → 按 on-experiment-done 流程：更新 registry metrics、更新 report.md、检查 matched-task comparison（obs_only vs perdof vs argmin vs scalar 全 10-task）
- bjb1-18228 全部 4 路 spatial 完成 → 最终 matched 10-task 对比表，裁决 per-DOF claim 是否彻底死亡
- bjb1-32546 object eval 完成 → cross-benchmark validation，如果 perdof 持续 0% 则 per-DOF claim 跨 benchmark 也死
- bjb2-28827 magnitude sweep 全部完成 → 画 norm 敏感性曲线（obs_only vs perdof at each norm），裁决 obs_only 是否稳定优于 perdof
- bjb2-40593 obs_only norm=0.03 完成 → 补全 obs_only norm curve 最低点
- 全部实验完成 → 最终 framing 裁决（obs_only narrative 还是项目 dead），更新 paper_framing.md，启动 Paper Agent 写 CoRL 初稿
- 任何实验 conclusion=negative → 按 red-section skill 产 Framing 调整提案，禁止默跑下一个

### 5. 🎯 战略上下文
- **D027 CRITICAL**: per-DOF (perdof) CRM 在 spatial matched-task 上与 argmin 0pp 差异（均 42.9%/35%），kill criteria 已触发。per-DOF claim 在 spatial 上实质死亡。
- **obs_only 是项目存活的唯一希望**: obs_only T0-T5 40% > perdof/argmin 35%（+5pp），magnitude sweep 初步显示 obs_only >= perdof at every tested norm。如果全 10-task + 全 norm 确认 obs_only 稳定优于 perdof/argmin → 论文转向 "learned correction with observation-only features"。
- **Object benchmark 风险极高**: perdof 前 2 tasks 均 0%（VLA-only K=1 baseline 有 10%），per-DOF 在 object 上可能比 baseline 还差。
- **CoRL DDL**: abstract ~May 26（11天），full paper ~Jun 2（18天）。
- **易错点**:
  - 不要把部分 task 的 SR 直接与全 10-task SR 对比（matched-task comparison 必须用相同 task 子集）
  - eval-mag-obsonly-norm03 系列有多个重复条目，只有 r2 是有效的
  - bjb2-40593 的 norm003-b2 (PID 227434) 是 norm=0.03 实验（不是 norm=0.3），别和 bjb1-18228 的 norm03-r2 (norm=0.3) 搞混
  - registry 状态机严格限制跳转，PREPARING 不能直接到 DONE，某些历史条目状态不一致需容忍
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-mag-obsonly-norm03-b2"
}
```

</details>

---
