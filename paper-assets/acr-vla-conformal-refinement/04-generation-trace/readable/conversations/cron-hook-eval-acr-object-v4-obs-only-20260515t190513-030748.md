# cron hook eval acr object v4 obs only 20260515T190513 030748

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 2
- **Tool calls:** 12
- **Original source:** `logs/chats/archive/cron_hook_eval-acr-object-v4-obs-only_20260515T190513_030748.jsonl`
- **Structured JSON:** [`132d70a582de044f5ba5.json`](../../sessions/13/132d70a582de044f5ba5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-15T15:59:34.504603+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: eval-acr-object-v4-obs-only
- project: acr-vla-conformal-refinement
- server: bjb1-32546

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-15T15:59:47.356197+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__read_experiment_plan_with_status",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__read_experiment_plan_with_status",
    "max_results": "15"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-15T15:59:47.356770+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T15:59:52.777184+00:00_

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
  "session": "cron:hook:eval-acr-object-v4-obs-only",
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

_source line 5 · 2026-05-15T15:59:52.827820+00:00_

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
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T15:59:53.383895+00:00_

Error: result (146,084 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-22463a65/2fac8582-c7b0-41f6-925f-df851d718b62/tool-results/mcp-agent-ml-research-read_registry-1778860793350.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-22463a65/2fac8582-c7b0-41f6-925f-df851d718b62/tool-results/mcp-agent-ml-research-read_registry-1778860793350.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 606
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T15:59:53.936299+00:00_

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
  "session": "cron:hook:eval-acr-object-v4-obs-only",
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

_source line 8 · 2026-05-15T15:59:54.488788+00:00_

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
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T15:59:54.890638+00:00_

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
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "status": "running"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T15:59:55.041685+00:00_

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
  "session": "cron:hook:eval-acr-object-v4-obs-only",
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

_source line 11 · 2026-05-15T16:00:26.476399+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 15, \"results\": [{\"exp_id\": \"eval-reconvla-object\", \"success\": true, \"actions\": [\"Job still running (pid=9659)\"]}, {\"exp_id\": \"eval-mag-perdof-norm003\", \"success\": true, \"actions\": [\"Job still running (pid=13185)\"]}, {\"exp_id\": \"eval-mag-perdof-norm005\", \"success\": true, \"actions\": [\"Job still running (pid=13456)\"]}, {\"exp_id\": \"eval-mag-perdof-norm02\", \"success\": true, \"actions\": [\"Job still running (pid=13728)\"]}, {\"exp_id\": \"eval-mag-perdof-norm03\", \"success\": true, \"actions\": [\"Job still running (pid=14260)\"]}, {\"exp_id\": \"eval-mag-obsonly-norm005\", \"success\": true, \"actions\": [\"Sentinel EXIT_CODE=0 → Registry → ANALYZING\", \"Cron deleted\"]}, {\"exp_id\": \"eval-mag-obsonly-norm02\", \"success\": true, \"actions\": [\"Job still running (pid=15190)\"]}, {\"exp_id\": \"eval-vla-mean-object\", \"success\": true, \"actions\": [\"Job still running (pid=18808)\"]}, {\"exp_id\": \"eval-acr-object-v4-scalar\", \"success\": true, \"actions\": [\"Job still running (pid=14003)\"]}, {\"exp_id\": \"eval-acr-object-obs-only-norm02\", \"success\": true, \"actions\": [\"Job still running (pid=44270)\"]}, {\"exp_id\": \"eval-mag-obsonly-norm003-b2\", \"success\": true, \"actions\": [\"Job still running (pid=227434)\"]}, {\"exp_id\": \"eval-mag-obsonly-norm03-r2\", \"success\": true, \"actions\": [\"Job still running (pid=325264)\"]}, {\"exp_id\": \"eval-obs-only-object-seed43\", \"success\": true, \"actions\": [\"Job still running (pid=356490)\"]}, {\"exp_id\": \"eval-argmin-object-seed43\", \"success\": true, \"actions\": [\"Job still running (pid=356696)\"]}, {\"exp_id\": \"eval-perdof-object-seed43\", \"success\": true, \"actions\": [\"Job still running (pid=365925)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 33648
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T16:00:26.477220+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-15T16:00:04Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 103 个实验 — ANALYZING 2, DONE 68, PREPARING 18, RUNNING 15\\n**DONE 分布**: failed 15, killed 28, success 25\\n\\n### GPU 占用\\n- **实际运行**: 15 张 — bjb1-32546:cuda:0(eval-reconvla-object), bjb1-32546:cuda:3(eval-acr-object-v4-scalar), bjb2-28827:bjb2-28827:cuda:0(eval-mag-perdof-norm003), bjb2-28827:bjb2-28827:cuda:1(eval-mag-perdof-norm005), bjb2-28827:bjb2-28827:cuda:2(eval-mag-perdof-norm02), bjb2-28827:bjb2-28827:cuda:3(eval-mag-perdof-norm03), bjb2-28827:bjb2-28827:cuda:5(eval-mag-obsonly-norm02), bjb1-32546:bjb1-32546:cuda:5(eval-vla-mean-object), bjb2-40593:cuda:0(eval-mag-obsonly-norm003-b2), bjb1-32546:cuda:4(eval-acr-object-obs-only-norm02), bjb1-18228:cuda:0(eval-mag-obsonly-norm03-r2), bjb1-18228:cuda:2(eval-obs-only-object-seed43), bjb1-18228:cuda:3(eval-argmin-object-seed43), bjb1-18228:cuda:1(eval-perdof-object-seed43), bjb1-32546:cuda:1(eval-vla-mean-object-seed43)\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `eval-reconvla-object` | bjb1-32546 | cuda:0 | 9659 | `~/runs/acr-vla-conformal-refinement/eval-reconvla-object.log` |\\n| `eval-acr-object-v4-scalar` | bjb1-32546 | cuda:3 | 14003 | `…/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log` |\\n| `eval-mag-perdof-norm003` | bjb2-28827 | bjb2-28827:cuda:0 | 13185 | `—` |\\n| `eval-mag-perdof-norm005` | bjb2-28827 | bjb2-28827:cuda:1 | 13456 | `—` |\\n| `eval-mag-perdof-norm02` | bjb2-28827 | bjb2-28827:cuda:2 | 13728 | `—` |\\n| `eval-mag-perdof-norm03` | bjb2-28827 | bjb2-28827:cuda:3 | 14260 | `—` |\\n| `eval-mag-obsonly-norm02` | bjb2-28827 | bjb2-28827:cuda:5 | 15190 | `—` |\\n| `eval-vla-mean-object` | bjb1-
…[truncated 6614 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 32540
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T16:00:26.528620+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-15 13:45 UTC | 更新原因: 修正 magnitude sweep 表 — perdof norm=0.03 和 norm=0.3 数据与 registry 同步\\n\\n> 最后更新: 2026-05-15 13:25 UTC | 更新原因: scalar-r2 完成锁定 spatial, object 6/10 中期数据, D032 magnitude narrative 修正, seed=43 三方部署确认\\n\\n## 核心方向\\nobs_only CRM（基于观测特征的 learned correction）是唯一存活路径。Per-DOF conformal claim 已死。论文 story：obs_only CRM 对 correction magnitude 鲁棒，perdof 在高 norm 下崩塌。详见 paper_framing.md。\\n\\n## 投稿目标\\n**CoRL 2026**（abstract DDL ~May 26, full paper DDL ~Jun 2）。剩余 ~11 天。\\n\\n## 当前进展\\n- **阶段**: Phase 2d — Object benchmark + seed=43 doubling 决定项目存亡\\n- **MVP**: PASS\\n- **Spatial LOCKED ✅**: 全部 CRM 变体确认 dead（argmin 34%, perdof 35%, obs_only 35%, scalar 32%）\\n- **Object 6/10 tasks**: obs_only 0.1: 13.3% vs argmin 6.7% (+6.6pp)；obs_only 0.2: 18.0% vs argmin ~8% (+~10pp)\\n- **Magnitude sweep 6-7/10 tasks**: obs_only 在所有 norm 下 > perdof，优势随 norm 增大急剧扩大（D032）\\n- **D031 seed=43 三方对比已部署**: obs_only / argmin / perdof 均在 bjb1-18228 运行中\\n\\n## Spatial 最终结果（LOCKED ✅）\\n\\n| 方法 | 10-task SR | vs argmin |\\n|------|-----------|-----------|\\n| argmin K=10 | 34% | baseline |\\n| perdof 0.1 | 35% | +1pp |\\n| obs_only 0.1 | 35% | +1pp |\\n| scalar 0.1 | 32% | -2pp |\\n| VLA-only K=1 | 30% | -4pp |\\n| VLA-mean K=10 | 32% | -2pp |\\n\\n## Object 中期快照（6/10 tasks, seed=42）\\n\\n| 方法 | SR | vs argmin |\\n|------|-----|-----------|\\n| obs_only 0.1 | 13.3% | +6.6pp |\\n| obs_only 0.2 | 18.0% (5t) | +11.3pp |\\n| vla_mean | 10.0% | +3.3pp |\\n| perdof 0.1 | 8.3% | +1.6pp |\\n| argmin | 6.7% | baseline |\\n| scalar 0.1 | 3.3% | -3.4pp |\\n\\n## Magnitude Sweep（4-7/10 tasks, spatial）\\n\\n| norm | obs_only | perdof | gap | 备注 |\\n|------|----------|--------|-----|------|\\n| 0.03 | 55.0% (4t) | 40.0% (7t) | +15pp | 任务数不对等，不可直接比 |\\n| 0.05 | 42.9
…[truncated 2957 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 32039
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T16:00:26.579287+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_research_magnitude-robustness-literature_20260515T155457\", \"task_type\": \"research:magnitude-robustness-literature\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-15T15:54:57.665928+00:00\", \"ended_at\": null}], \"count\": 1}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 31688
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T16:00:26.579651+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"acr-vla-conformal-refinement\", \"section\": \"execution\", \"config\": {\"execution\": {\"account\": \"root\", \"gpu_constraint\": [\"autodl-4090:cuda:0\"], \"gpu_ids\": [\"bjb2-40593:cuda:0\", \"bjb1-18228:cuda:0\", \"bjb1-18228:cuda:1\", \"bjb1-18228:cuda:2\", \"bjb1-18228:cuda:3\", \"bjb1-32546:cuda:0\", \"bjb1-32546:cuda:1\", \"bjb1-32546:cuda:2\", \"bjb1-32546:cuda:3\", \"bjb1-32546:cuda:4\", \"bjb1-32546:cuda:5\", \"bjb2-28827:cuda:0\", \"bjb2-28827:cuda:1\", \"bjb2-28827:cuda:2\", \"bjb2-28827:cuda:3\", \"bjb2-28827:cuda:4\", \"bjb2-28827:cuda:5\"], \"project_path\": \"/root/acr-vla-conformal-refinement\", \"servers\": [\"bjb2-40593\", \"bjb1-18228\", {\"account\": \"root\", \"server\": \"bjb1-32546\"}, {\"account\": \"root\", \"server\": \"bjb2-28827\"}]}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 31537
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T16:00:33.456488+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-acr-object-v4-obs-only'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-acr-object-v4-obs-only'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T16:00:33.809124+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2575}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 352
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T16:00:33.909795+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-mag-obsonly-norm005'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-mag-obsonly-norm005'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T16:00:34.161740+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2346}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 251
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T16:00:37.677432+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'ANALYZING'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'ANALYZING'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T16:00:37.928974+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-mag-obsonly-norm005\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:18.917Z\", \"updated_at\": \"2026-05-15T16:00:03.129Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.05 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obs_only_norm005.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-obs_only\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-obs_only\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:4\", \"pid\": 14854, \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"T0_between_plate_ramekin\": \"80%\", \"T1_next_to_ramekin\": \"90%\", \"T2_table_center\": \"0%\", \"T3_on_cookie_box\": \"40%\", \"T4_top_drawer\": \"10%\", \"T5_on_ramekin\": \"0%\", \"T6_next_to_cookie_box\": \"80%\"}, \"running_avg_7task\": \"42.9%\", \"snapshot_time\": \"2026-05-15T09:00:00Z\", \"server\": \"bjb2-28827\", \"process_status\": \"alive\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:00:02.717Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:00:09.569232+00:00\"}]}}, \"eval-acr-object-v4-obs-only\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:53:41.689Z\", \"updated_at\": \"2026-05-15T15:59:32.240Z\", \"hypothesis\": \"D021: obs_only CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation — obs-only leads spatial at 57.5%.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOM
…[truncated 1335 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 251
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T16:01:13.048819+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "analysis:eval-acr-object-v4-obs-only",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务\nSSH 到 bjb1-32546 读取实验 eval-acr-object-v4-obs-only 的最终结果。\n\n## 背景\n这是 obs_only CRM v3-norm (max_correction_norm=0.1) 在 LIBERO object benchmark 上的 10-task 评测。进程已正常退出，状态为 ANALYZING。\n\n这是项目存亡级实验——如果 obs_only 在 object 上维持 +6pp+ 优于 argmin 的优势，项目存活；否则 dead。\n\n## 具体步骤\n\n1. SSH 到 bjb1-32546（用户 root），读取日志文件：\n   ```\n   cat ~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log | tail -200\n   ```\n\n2. 尝试读取 JSON 结果文件（如果存在）：\n   ```\n   cat /root/acr-vla-conformal-refinement/logs/eval_acr_object_v4_obs_only*.json 2>/dev/null || echo \"NO_JSON\"\n   ls -la /root/acr-vla-conformal-refinement/logs/ | grep -i \"obs.only\" | grep -i object\n   ```\n\n3. 从日志中提取每个 task 的成功率（10 个 task 各自的 SR%）和总体平均 SR。\n\n4. 用 update_registry 更新实验：\n   - metrics: 包含所有 10 个 task 的 SR 和总体平均\n   - conclusion: 根据结果判断（如果 obs_only 10-task SR 显著高于 argmin baseline 6.7%，则 success；否则 negative）\n   - status: DONE\n   - 设置 checkpoint_path 和 log_path\n\n5. 对比 baseline（从 registry 中 eval-argmin-only-object 获取）：\n   - argmin object 10-task = ?（需要查 registry）\n   - 计算 obs_only vs argmin 差值\n\n## 已知 6/10 中间结果\nalphabet_soup: 0%, cream_cheese: 10%, salad_dressing: 20%, bbq_sauce: 40%, ketchup: 10%, tomato_sauce: 0%\n6-task avg: 13.3%\n\n## 输出\n将完整的 10-task 结果表格和分析写入产出，包括：\n- 每个 task 的 SR\n- 10-task 平均 SR\n- vs argmin baseline 的差值\n- 结论判定",
  "tool_groups": "['ssh', 'registry']",
  "context": "项目: acr-vla-conformal-refinement\n服务器: bjb1-32546 (root@)\n实验 ID: eval-acr-object-v4-obs-only\n日志路径: ~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log\n项目路径: /root/acr-vla-conformal-refinement\nObject benchmark argmin baseline (6/10 snapshot): 6.7% SR"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analysis:eval-acr-object-v4-obs-only",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务\nSSH 到 bjb1-32546 读取实验 eval-acr-object-v4-obs-only 的最终结果。\n\n## 背景\n这是 obs_only CRM v3-norm (max_correction_norm=0.1) 在 LIBERO object benchmark 上的 10-task 评测。进程已正常退出，状态为 ANALYZING。\n\n这是项目存亡级实验——如果 obs_only 在 object 上维持 +6pp+ 优于 argmin 的优势，项目存活；否则 dead。\n\n## 具体步骤\n\n1. SSH 到 bjb1-32546（用户 root），读取日志文件：\n   ```\n   cat ~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log | tail -200\n   ```\n\n2. 尝试读取 JSON 结果文件（如果存在）：\n   ```\n   cat /root/acr-vla-conformal-refinement/logs/eval_acr_object_v4_obs_only*.json 2>/dev/null || echo \"NO_JSON\"\n   ls -la /root/acr-vla-conformal-refinement/logs/ | grep -i \"obs.only\" | grep -i object\n   ```\n\n3. 从日志中提取每个 task 的成功率（10 个 task 各自的 SR%）和总体平均 SR。\n\n4. 用 update_registry 更新实验：\n   - metrics: 包含所有 10 个 task 的 SR 和总体平均\n   - conclusion: 根据结果判断（如果 obs_only 10-task SR 显著高于 argmin baseline 6.7%，则 success；否则 negative）\n   - status: DONE\n   - 设置 checkpoint_path 和 log_path\n\n5. 对比 baseline（从 registry 中 eval-argmin-only-object 获取）：\n   - argmin object 10-task = ?（需要查 registry）\n   - 计算 obs_only vs argmin 差值\n\n## 已知 6/10 中间结果\nalphabet_soup: 0%, cream_cheese: 10%, salad_dressing: 20%, bbq_sauce: 40%, ketchup: 10%, tomato_sauce: 0%\n6-task avg: 13.3%\n\n## 输出\n将完整的 10-task 结果表格和分析写入产出，包括：\n- 每个 task 的 SR\n- 10-task 平均 SR\n- vs argmin baseline 的差值\n- 结论判定",
    "tool_groups": "['ssh', 'registry']",
    "context": "项目: acr-vla-conformal-refinement\n服务器: bjb1-32546 (root@)\n实验 ID: eval-acr-object-v4-obs-only\n日志路径: ~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log\n项目路径: /root/acr-vla-conformal-refinement\nObject benchmark argmin baseline (6/10 snapshot): 6.7% SR"
  }
}
````

</details>

---

### Tool result

_source line 23 · 2026-05-15T16:01:23.424500+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_eval-acr-object-v4-obs-only_20260515T160113\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analysis_eval-acr-object-v4-obs-only_20260515T160113.log\", \"setup_data\": {}, \"message\": \"Worker worker_analysis_eval-acr-object-v4-obs-only_20260515T160113 started. Use get_worker_status('worker_analysis_eval-acr-object-v4-obs-only_20260515T160113') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 10375
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T16:01:24.581783+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "analysis:eval-mag-obsonly-norm005",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务\nSSH 到 bjb2-28827 读取实验 eval-mag-obsonly-norm005 的最终结果。\n\n## 背景\n这是 obs_only CRM v3-norm (max_correction_norm=0.05) 在 LIBERO spatial benchmark 上的 magnitude sweep 评测。进程已正常退出，状态为 ANALYZING。\n\n## 具体步骤\n\n1. SSH 到 bjb2-28827（用户 root），查找并读取日志/结果文件：\n   ```\n   ls -la ~/runs/acr-vla-conformal-refinement/ | grep -i \"mag.*obs.*norm005\\|obsonly.*norm005\"\n   ls -la /root/acr-vla-conformal-refinement/logs/ | grep -i \"obs.*only.*norm.*005\\|mag.*obs\"\n   ```\n\n2. 读取日志文件（尝试多个可能路径）：\n   ```\n   cat /root/acr-vla-conformal-refinement/logs/eval_mag_obs_only_norm005*.json 2>/dev/null || echo \"NO_JSON\"\n   # 也检查 tmux 日志\n   tail -200 ~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm005.log 2>/dev/null || echo \"NO_RUN_LOG\"\n   ```\n\n3. 从日志中提取每个 task 的成功率（10 个 task 各自的 SR%）和总体平均 SR。\n\n4. 用 update_registry 更新实验：\n   - metrics: 包含所有 10 个 task 的 SR 和总体平均\n   - conclusion: success（magnitude sweep data point）\n   - status: DONE\n   - 设置 log_path 和 checkpoint_path\n\n## 已知 7/10 中间结果\nT0_between_plate_ramekin: 80%, T1_next_to_ramekin: 90%, T2_table_center: 0%, T3_on_cookie_box: 40%, T4_top_drawer: 10%, T5_on_ramekin: 0%, T6_next_to_cookie_box: 80%\n7-task avg: 42.9%\n\n## Magnitude sweep 背景\n其他 norm 值的 obs_only 结果（spatial）:\n- norm=0.03: obs_only 55.0% (4t) vs perdof 40.0% (7t)\n- norm=0.05: 42.9% (7t) ← 这个实验，需要 10-task 最终值\n- norm=0.2: 45.7% (7t)\n- norm=0.3: 46.0% (5t)\n\n## 输出\n完整 10-task 结果表格 + 最终 SR + 与其他 norm 的对比",
  "tool_groups": "['ssh', 'registry']",
  "context": "项目: acr-vla-conformal-refinement\n服务器: bjb2-28827 (root@)\n实验 ID: eval-mag-obsonly-norm005\n项目路径: /root/acr-vla-conformal-refinement\n评测命令: python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.05 --n_rollouts 10 --K 10"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analysis:eval-mag-obsonly-norm005",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务\nSSH 到 bjb2-28827 读取实验 eval-mag-obsonly-norm005 的最终结果。\n\n## 背景\n这是 obs_only CRM v3-norm (max_correction_norm=0.05) 在 LIBERO spatial benchmark 上的 magnitude sweep 评测。进程已正常退出，状态为 ANALYZING。\n\n## 具体步骤\n\n1. SSH 到 bjb2-28827（用户 root），查找并读取日志/结果文件：\n   ```\n   ls -la ~/runs/acr-vla-conformal-refinement/ | grep -i \"mag.*obs.*norm005\\|obsonly.*norm005\"\n   ls -la /root/acr-vla-conformal-refinement/logs/ | grep -i \"obs.*only.*norm.*005\\|mag.*obs\"\n   ```\n\n2. 读取日志文件（尝试多个可能路径）：\n   ```\n   cat /root/acr-vla-conformal-refinement/logs/eval_mag_obs_only_norm005*.json 2>/dev/null || echo \"NO_JSON\"\n   # 也检查 tmux 日志\n   tail -200 ~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm005.log 2>/dev/null || echo \"NO_RUN_LOG\"\n   ```\n\n3. 从日志中提取每个 task 的成功率（10 个 task 各自的 SR%）和总体平均 SR。\n\n4. 用 update_registry 更新实验：\n   - metrics: 包含所有 10 个 task 的 SR 和总体平均\n   - conclusion: success（magnitude sweep data point）\n   - status: DONE\n   - 设置 log_path 和 checkpoint_path\n\n## 已知 7/10 中间结果\nT0_between_plate_ramekin: 80%, T1_next_to_ramekin: 90%, T2_table_center: 0%, T3_on_cookie_box: 40%, T4_top_drawer: 10%, T5_on_ramekin: 0%, T6_next_to_cookie_box: 80%\n7-task avg: 42.9%\n\n## Magnitude sweep 背景\n其他 norm 值的 obs_only 结果（spatial）:\n- norm=0.03: obs_only 55.0% (4t) vs perdof 40.0% (7t)\n- norm=0.05: 42.9% (7t) ← 这个实验，需要 10-task 最终值\n- norm=0.2: 45.7% (7t)\n- norm=0.3: 46.0% (5t)\n\n## 输出\n完整 10-task 结果表格 + 最终 SR + 与其他 norm 的对比",
    "tool_groups": "['ssh', 'registry']",
    "context": "项目: acr-vla-conformal-refinement\n服务器: bjb2-28827 (root@)\n实验 ID: eval-mag-obsonly-norm005\n项目路径: /root/acr-vla-conformal-refinement\n评测命令: python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.05 --n_rollouts 10 --K 10"
  }
}
````

</details>

---

### Tool result

_source line 25 · 2026-05-15T16:01:26.943283+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_eval-mag-obsonly-norm005_20260515T160124\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analysis_eval-mag-obsonly-norm005_20260515T160124.log\", \"setup_data\": {}, \"message\": \"Worker worker_analysis_eval-mag-obsonly-norm005_20260515T160124 started. Use get_worker_status('worker_analysis_eval-mag-obsonly-norm005_20260515T160124') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 2361
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-15T16:01:45.041762+00:00_

两个分析 Worker 已派出：
- `eval-acr-object-v4-obs-only`（object obs_only 10-task 最终结果，项目存亡级）→ bjb1-32546
- `eval-mag-obsonly-norm005`（spatial magnitude sweep norm=0.05）→ bjb2-28827

同时注意到两个 GPU 已释放：bjb1-32546:cuda:2 和 bjb2-28827:cuda:4。待分析结果出来后决定下一步实验分配，并向 Director 汇报。

等待 Worker 回调。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-acr-object-v4-obs-only"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 27 · 2026-05-15T19:04:20.026392+00:00_

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
  "session": "cron:hook:eval-acr-object-v4-obs-only",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-15T19:05:13.028999+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb2-40593:cuda:0, bjb1-18228:cuda:0-3, bjb1-32546:cuda:0-5, bjb2-28827:cuda:0-5（共 17 张）。白名单外的 GPU 即使 Director 指令也必须 push back
- bjb1-32546 用 conda 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，没有 .venv
- submit 命令必须自带环境激活，GPU 编号从 0 开始（框架注入 CUDA_VISIBLE_DEVICES）
- obs_only 是唯一存活路径，perdof claim 已死。不要在 perdof 方向投新实验
- CoRL 2026 DDL: abstract ~May 26, full paper ~Jun 2，剩余 ~11 天

### 2. 🖥️ 基础设施快照
- **bjb1-32546**（6×4090）：工作目录 /root/acr-vla-conformal-refinement，Python /root/miniconda3/bin/python，conda base
  - 模型：/root/autodl-tmp/models/smolvla_libero/，CRM checkpoint: /root/autodl-tmp/checkpoints/crm_v3_norm/{obs_only,perdof,scalar_unc}/crm_best.pt
  - 日志：~/runs/acr-vla-conformal-refinement/
- **bjb1-18228**（4×4090）：同结构，4 卡满载跑 seed=43 三方对比 + mag sweep
- **bjb2-28827**（6×4090）：magnitude sweep 6-way（perdof 4 卡 + obsonly 2 卡）
- **bjb2-40593**（1×4090D）：obsonly-norm003-b2
- HF cache: /root/autodl-tmp/.hf_cache（所有服务器）
- W&B: 配置在项目 config 中，entity/project 自动读取

### 3. 📊 当前状态
**刚发生**：收到 cron 回调，eval-acr-object-v4-obs-only 和 eval-mag-obsonly-norm005 两个实验完成转 ANALYZING。已派出两个分析 Worker：
- `worker_analysis_eval-acr-object-v4-obs-only_20260515T160113`（SSH bjb1-32546 读最终 10-task 结果）
- `worker_analysis_eval-mag-obsonly-norm005_20260515T160124`（SSH bjb2-28827 读最终 10-task 结果）

**这两个 Worker 的回调尚未返回，下一个"你"会收到 [WORKER DONE] 消息，必须处理。**

**RUNNING 实验（14 个）**：
| 实验 | 服务器 | GPU | 摘要 |
|------|--------|-----|------|
| eval-reconvla-object | bjb1-32546 | cuda:0 | reconvla baseline on object |
| eval-acr-object-v4-scalar | bjb1-32546 | cuda:3 | scalar CRM on object |
| eval-vla-mean-object | bjb1-32546 | cuda:5 | VLA-mean baseline on object |
| eval-vla-mean-object-seed43 | bjb1-32546 | cuda:1 | VLA-mean seed=43 |
| eval-acr-object-obs-only-norm02 | bjb1-32546 | cuda:4 | obs_only norm=0.2 on object |
| eval-mag-perdof-norm003/005/02/03 | bjb2-28827 | cuda:0-3 | perdof magnitude sweep spatial |
| eval-mag-obsonly-norm02 | bjb2-28827 | cuda:5 | obsonly norm=0.2 spatial sweep |
| eval-mag-obsonly-norm003-b2 | bjb2-40593 | cuda:0 | obsonly norm=0.03 spatial retry |
| eval-mag-obsonly-norm03-r2 | bjb1-18228 | cuda:0 | obsonly norm=0.3 spatial retry |
| eval-obs-only-object-seed43 | bjb1-18228 | cuda:2 | 🔑 seed=43 obs_only object |
| eval-argmin-object-seed43 | bjb1-18228 | cuda:3 | 🔑 seed=43 argmin object |
| eval-perdof-object-seed43 | bjb1-18228 | cuda:1 | 🔑 seed=43 perdof object |

**另有 1 个 running Worker**：`worker_research_magnitude-robustness-literature_20260515T155457`（文献调研）

### 4. 📋 待办（条件触发式）
- **Worker 分析回调到达** → 读结果，update_registry(status=DONE)，更新 report.md，向 Director 汇报。eval-acr-object-v4-obs-only 是项目存亡级：10-task obs_only SR vs argmin 6.7% 的差值决定项目生死
- **eval-acr-object-v4-obs-only 10-task SR ≥ 12%**（维持 +5pp+ vs argmin）→ success，项目存活，等 seed=43 三方确认后做 Fisher exact test
- **eval-acr-object-v4-obs-only 10-task SR < 10%**（优势消失）→ negative，触发 red-section Framing 提案，项目可能 dead
- **seed=43 三方完成**（obs_only/argmin/perdof on object）→ 立即做 Fisher exact test + bootstrap CI，这是 CoRL 投稿的统计基础
- **magnitude sweep 全部完成** → 汇总 norm sensitivity curve，obs_only 鲁棒性 vs perdof 崩塌是论文核心 story
- **所有 object eval 完成** → 更新 paper_framing.md，启动 CoRL 初稿写作
- **文献调研 Worker 回调** → 整合 magnitude robustness 相关文献到 literature_map.yaml

### 5. 🎯 战略上下文
- **核心结论链**：D025 推翻了 perdof 52.5% 的虚高数据 → D027 matched-task 分析确认 perdof≈argmin → D028 argmin locked 34% → D029 perdof locked 35% → D030 spatial ALL CRM dead → D031 统计显著性方案（seed=43 doubling）→ D032 magnitude sweep narrative（obs_only 鲁棒，perdof 高 norm 崩塌）
- **项目存活唯一路径**：Object obs_only +6pp+ 维持 + seed=43 复现 → p < 0.05。Spatial 已确认全部 CRM 无效（inc obs_only）
- **论文 story**：obs_only CRM 对 correction magnitude 鲁棒，perdof 在高 norm 下崩塌；object 域 obs_only 显著优于 argmin/perdof
- **最容易判断错的事**：(1) 不要用 6/10 中期快照数据作为最终结果——必须等 Worker 读回 10-task 完整数据；(2) spatial 上所有 CRM 变体都和 argmin 差不多（±1pp），这不是 bug 是事实，不要试图"修复"；(3) eval-acr-object-v4-obs-only 的 6/10 中期 13.3% 看起来不错但 T7-T10 可能全是难 task 导致下降——等完整数据再下结论
- **resource-saturation skill 要求**：向 Director 汇报时必须开头带 `[资源] GPU 分配 N / 实际跑 M | Worker 池 K` 行
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-acr-object-v4-obs-only"
}
```

</details>

---
