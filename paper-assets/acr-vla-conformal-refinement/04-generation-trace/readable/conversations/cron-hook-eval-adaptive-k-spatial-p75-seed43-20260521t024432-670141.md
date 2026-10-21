# cron hook eval adaptive k spatial p75 seed43 20260521T024432 670141

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 2
- **Tool calls:** 15
- **Original source:** `logs/chats/archive/cron_hook_eval-adaptive-k-spatial-p75-seed43_20260521T024432_670141.jsonl`
- **Structured JSON:** [`108a83b892a73389ac66.json`](../../sessions/10/108a83b892a73389ac66.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

32 recorded events

### User

_source line 1 · 2026-05-20T10:32:11.873037+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: eval-adaptive-k-spatial-p75-seed43
- project: acr-vla-conformal-refinement
- server: bjb1-32546
- log_path: ~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p75-seed43.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-20T10:32:25.551410+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__load_project_config",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__load_project_config",
    "max_results": "11"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-20T10:32:25.551918+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T10:32:30.042640+00:00_

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
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
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

_source line 5 · 2026-05-20T10:32:30.490587+00:00_

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
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T10:32:31.009489+00:00_

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
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
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

_source line 7 · 2026-05-20T10:32:31.453251+00:00_

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
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T10:32:31.565940+00:00_

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
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
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

_source line 9 · 2026-05-20T10:32:33.525373+00:00_

Error: result (653,145 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-a25e50e4/1c359730-cf2b-4048-af30-9e5dcd52e270/tool-results/mcp-agent-ml-research-read_registry-1779273153310.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-a25e50e4/1c359730-cf2b-4048-af30-9e5dcd52e270/tool-results/mcp-agent-ml-research-read_registry-1779273153310.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-a25e50e4/1c359730-cf2b-4048-af30-9e5dcd52e270/tool-results/mcp-agent-ml-research-read_registry-1779273153310.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 3482
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T10:32:56.857887+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 6, \"results\": [{\"exp_id\": \"eval-adaptive-k-spatial-p50-seed42\", \"success\": true, \"actions\": [\"Job still running (pid=681823)\"]}, {\"exp_id\": \"eval-adaptive-k-spatial-p25-seed42\", \"success\": true, \"actions\": [\"Job still running (pid=308612)\"]}, {\"exp_id\": \"eval-adaptive-k-spatial-p25-seed43\", \"success\": true, \"actions\": [\"Skipped (created 110s ago < interval 120s)\"]}, {\"exp_id\": \"eval-crm-object-k20-seed43\", \"success\": true, \"actions\": [\"Skipped (created 109s ago < interval 120s)\"]}, {\"exp_id\": \"eval-obs-only-object-norm003-seed43-r2\", \"success\": true, \"actions\": [\"Skipped (created 107s ago < interval 120s)\"]}, {\"exp_id\": \"eval-obs-only-object-norm005-seed44\", \"success\": true, \"actions\": [\"Skipped (created 105s ago < interval 120s)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 26367
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T10:32:56.976177+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-20T10:32:38Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 430 个实验 — ANALYZING 5, DEPLOYED 4, DONE 381, PREPARING 32, QUEUED 3, RUNNING 5\\n**DONE 分布**: failed 47, killed 85, negative 32, success 217\\n\\n### GPU 占用\\n- **实际运行**: 5 张 — bjb1-32546:cuda:5(eval-obs-only-object-norm005-seed44), bjb1-32546:cuda:4(eval-obs-only-object-norm003-seed43-r2), bjb2-40593:cuda:0(eval-adaptive-k-spatial-p50-seed42), bjb1-18228:cuda:2(eval-adaptive-k-spatial-p25-seed42), bjb1-32546:cuda:2(eval-adaptive-k-spatial-p25-seed43)\\n\\n### 💾 磁盘余量\\n- **bjb2-40593**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 46G/437G 可用（已用 90%） ⚠️\\n- **bjb1-18228**:\\n  - `/autodl-pub`: 992G/7.0T 可用（已用 87%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb1-32546**:\\n  - `/autodl-pub`: 904G/7.0T 可用（已用 88%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb2-28827**:\\n  - `/autodl-pub`: 4.5T/14T 可用（已用 69%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/439G 可用（已用 5%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `eval-obs-only-object-norm005-seed44` | bjb1-32546 | cuda:5 | 315473 | `…onformal-refinement/eval-obs-only-object-norm005-seed44.log` |\\n| `eval-obs-only-object-norm003-seed43-r2` | bjb1-32546 | cuda:4 | 314884 | `…ormal-refinement/eval-obs-only-object-norm003-seed43-r2.log` |\\n| `eval-adaptive-k-spatial-p50-seed42` | bjb2-40593 | cuda:0 | 681823 | `—` |\\n| `eval-adaptive-k-spatial-p25-seed42` | bjb1-18228 | cuda:2 | 308612 | `…conformal-refinement/eval-adaptiv
…[truncated 7933 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 25966
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T10:32:57.041377+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-20 06:17 UTC | 更新原因: Fix Long OOD data to match D081, update RUNNING section per Reviewer observation\\n\\n> 详见 paper_framing.md（D077: Adaptive K 升级为核心贡献）\\n\\n## 核心方向\\n**Adaptive inference-time compute for frozen VLAs** — K=2 L2 distance 作为不确定性信号，自适应决定每步推理次数。CRM correction>selection 分析作为支撑。\\n\\n## 投稿目标\\n**CoRL 2026** DDL **2026-05-29**。剩余 ~9 天。\\n\\n## D077 方向转换（用户硬要求）\\n- Adaptive K = 论文**核心贡献**（方法）\\n- K=10 分析降为 supporting evidence\\n\\n## 信号候选 (CLOSED)\\n| 信号 | ρ vs K10_var | 结论 |\\n|------|-------------|------|\\n| **K=2 L2 distance** | **0.9979** | **✅ GO — 唯一可用信号** |\\n| CRM correction magnitude | 0.1523 | ❌ NO-GO (D079) |\\n| FMVD | 0.0825 | ❌ NO-GO |\\n\\n## Adaptive K Sweep (Object) — 12/12 DONE ✅\\n| 阈值 | seeds | SR (mean) | avg_K | fast_path% | vs K=10 |\\n|------|-------|-----------|-------|-----------|---------|\\n| P90 | 3/3 ✅ | 13.3% | ~2.6 | ~93% | 74% |\\n| P75 | 3/3 ✅ | 13.7% | ~3.1 | ~87% | 79% |\\n| **P50** | **3/3 ✅** | **15.3%** | **~3.8** | **~77%** | **~91%** |\\n| P25 | 3/3 ✅ | 14.3% | ~4.8 | ~65% | ~85% |\\n\\n**P50 = Pareto 最优 (D078)**。\\n\\n## RUNNING 实验\\n- bjb2-40593: Spatial Adaptive K P50 seed42 (rollout 中)\\n- bjb1-18228: Long VLA-only seed54, Long CRM seed53, Spatial VLA-only seed53\\n- bjb1-32546: Long CRM seed54, Spatial VLA-only seed54\\n- 更多部署中（Agent 处理综合指令）\\n\\n## 待部署\\n1. **Spatial Adaptive K P50 seed43, seed44**\\n2. **Random Selection baseline seed42, seed44** (plan_600)\\n3. **CRM Object K=10 norm02 seed42** (Table 1 n=6→n=7)\\n4. **fig3_kvalue 重新生成**\\n\\n## 论文 CRITICAL 待解决\\n1. **evaluate.py 推理模式确认** — Agent P0\\n2. **Spatial CRM K=10 n=8 溯源** — registry 只有 n=7, Agent 调查中\\n3. **OOD Long/Goal 数据全量更新** — Paper Agent 处理中\\n4. **P25 n=3 更新** — Paper Agent 处理中\\n\\n## 核心实验结果 (LOCKED,
…[truncated 2536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 25588
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T10:32:57.494552+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_diagnose_eval-adaptive-k-spatial-p50-seed42_20260520T103105\", \"task_type\": \"diagnose:eval-adaptive-k-spatial-p50-seed42\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-20T10:31:06.280640+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_analysis_eval-crm-object-k20-seed42_20260520T103217\", \"task_type\": \"analysis:eval-crm-object-k20-seed42\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-20T10:32:17.959548+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_analyze_eval-adaptive-k-spatial-p75-seed42_20260520T103231\", \"task_type\": \"analyze:eval-adaptive-k-spatial-p75-seed42\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-20T10:32:32.157749+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_analyze_eval-vla-only-long-seed49-r2_20260520T103241\", \"task_type\": \"analyze:eval-vla-only-long-seed49-r2\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-20T10:32:42.426868+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_analyze_eval-crm-object-k20-seed42_20260520T103247\", \"task_type\": \"analyze:eval-crm-object-k20-seed42\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-20T10:32:48.161409+00:00\", \"ended_at\": null}], \"count\": 5}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 25928
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T10:33:05.219278+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-adaptive-k-spatial-p75-seed43'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-adaptive-k-spatial-p75-seed43'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T10:33:06.244685+00:00_

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
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
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

### Tool call

_source line 16 · 2026-05-20T10:33:06.583532+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-adaptive-k-spatial-p75-seed42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-adaptive-k-spatial-p75-seed42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T10:33:09.550150+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.2543}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 4330
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T10:33:12.257794+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-crm-object-k20-seed42\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T08:02:49.893Z\", \"updated_at\": \"2026-05-20T10:33:03.327Z\", \"hypothesis\": \"CRM obs_only K=20 on Object seed42. K-value sweep (plan_601): tests whether increasing from K=10 to K=20 further improves SR, justifying K=10 as compute-efficient choice.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 42 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_K20_seed42.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"309205\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-object-k20-seed42.log\", \"submitted_at\": \"2026-05-20T08:03:32.825Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM obs_only K=20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A (eval only)\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T10:30:44.758Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T10:30:55.113999+00:00\"}]}, \"conclusion\": \"success\"}, \"eval-vla-only-long-seed49-r2\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T08:02:40.709Z\", \"updated_at\": \"2026-05-20T10:32:50.947Z\", \"hypothesis\": \"VLA-only b
…[truncated 6311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 6013
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T10:33:15.844565+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.5833}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 9261
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T10:33:27.467437+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-adaptive-k-p75-seed43'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-adaptive-k-p75-seed43'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T10:33:28.005472+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-adaptive-k-p75-seed42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-adaptive-k-p75-seed42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T10:33:29.059484+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-adaptive-k-spatial-p50-seed42'}",
  "fields": "['metrics', 'conclusion', 'status']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-adaptive-k-spatial-p50-seed42'}",
    "fields": "['metrics', 'conclusion', 'status']"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T10:33:29.879575+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-adaptive-k-spatial-p50-seed44-r2'}",
  "fields": "['metrics', 'conclusion', 'status']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-adaptive-k-spatial-p50-seed44-r2'}",
    "fields": "['metrics', 'conclusion', 'status']"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T10:33:33.492254+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.8844}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 6024
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T10:33:38.345163+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.8473}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 10339
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T10:33:42.192495+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.7642}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 13133
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T10:33:47.438669+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.2106}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 17559
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T10:34:12.098542+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "analyze:eval-adaptive-k-spatial-p75-seed43",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务\n分析已完成的实验 `eval-adaptive-k-spatial-p75-seed43` 的结果。\n\n## 实验信息\n- exp_id: eval-adaptive-k-spatial-p75-seed43\n- server: bjb1-32546\n- log_path: ~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p75-seed43.log\n- 模式: adaptive_k, threshold=P75 (0.098735, Object-calibrated)\n- benchmark: LIBERO-Spatial\n- seed: 43\n- K_full=10, n_rollouts=10\n\n## 操作步骤\n\n1. SSH 到 bjb1-32546，读取 log 文件末尾（tail -100）获取最终结果\n2. 读取 JSON 输出文件：`/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p75_seed43.json`（如果存在）\n3. 提取关键指标：\n   - success_rate (overall)\n   - per_task success rates\n   - avg_K (平均推理次数)\n   - fast_path_ratio (K=2 的比例)\n   - 总 rollout 数\n4. 用 `update_registry` 更新实验：\n   - field=metrics, value=提取到的指标字典\n   - field=conclusion, value=\"success\"（如果正常完成且指标合理）或 \"negative\"/\"failed\"\n   - field=status, value=\"DONE\"\n   - field=log_path, value=实际 log 路径\n   \n## 对比参考（来自 ROADMAP）\n- Object P75: SR mean 13.7%, avg_K ~3.1, fast_path ~87%\n- Spatial K=10 CRM baseline: 34.4±1.5%\n- Spatial P50: ~62% compute savings, comparable SR to K=10\n\n## 注意\n- 用 ssh_read_only 读取 log 和 JSON\n- 只有更新 registry 时用写操作\n- 提取完所有指标后再一次性更新 registry",
  "tool_groups": "['ssh', 'registry']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analyze:eval-adaptive-k-spatial-p75-seed43",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务\n分析已完成的实验 `eval-adaptive-k-spatial-p75-seed43` 的结果。\n\n## 实验信息\n- exp_id: eval-adaptive-k-spatial-p75-seed43\n- server: bjb1-32546\n- log_path: ~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p75-seed43.log\n- 模式: adaptive_k, threshold=P75 (0.098735, Object-calibrated)\n- benchmark: LIBERO-Spatial\n- seed: 43\n- K_full=10, n_rollouts=10\n\n## 操作步骤\n\n1. SSH 到 bjb1-32546，读取 log 文件末尾（tail -100）获取最终结果\n2. 读取 JSON 输出文件：`/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p75_seed43.json`（如果存在）\n3. 提取关键指标：\n   - success_rate (overall)\n   - per_task success rates\n   - avg_K (平均推理次数)\n   - fast_path_ratio (K=2 的比例)\n   - 总 rollout 数\n4. 用 `update_registry` 更新实验：\n   - field=metrics, value=提取到的指标字典\n   - field=conclusion, value=\"success\"（如果正常完成且指标合理）或 \"negative\"/\"failed\"\n   - field=status, value=\"DONE\"\n   - field=log_path, value=实际 log 路径\n   \n## 对比参考（来自 ROADMAP）\n- Object P75: SR mean 13.7%, avg_K ~3.1, fast_path ~87%\n- Spatial K=10 CRM baseline: 34.4±1.5%\n- Spatial P50: ~62% compute savings, comparable SR to K=10\n\n## 注意\n- 用 ssh_read_only 读取 log 和 JSON\n- 只有更新 registry 时用写操作\n- 提取完所有指标后再一次性更新 registry",
    "tool_groups": "['ssh', 'registry']"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T10:34:17.894339+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analyze_eval-adaptive-k-spatial-p75-seed43_20260520T103414\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-adaptive-k-spatial-p75-seed43_20260520T103414.log\", \"setup_data\": {}, \"message\": \"Worker worker_analyze_eval-adaptive-k-spatial-p75-seed43_20260520T103414 started. Use get_worker_status('worker_analyze_eval-adaptive-k-spatial-p75-seed43_20260520T103414') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 5795
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T10:35:05.868600+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "analyze:eval-crm-object-k20-seed43",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务\n分析已完成的实验 `eval-crm-object-k20-seed43` 的结果。\n\n## 实验信息\n- exp_id: eval-crm-object-k20-seed43\n- server: bjb1-32546\n- log_path: ~/runs/acr-vla-conformal-refinement/eval-crm-object-k20-seed43.log\n- 模式: crm_obs_only, K=20\n- benchmark: LIBERO-Object\n- seed: 43\n- n_rollouts=10\n\n## 操作步骤\n\n1. SSH 到 bjb1-32546，读取 log 文件末尾（tail -100）获取最终结果\n2. 读取 JSON 输出文件（可能路径）：`/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_K20_seed43.json`\n3. 提取关键指标：\n   - success_rate (overall)\n   - per_task success rates\n   - 总 rollout 数\n4. 用 `update_registry` 更新实验：\n   - field=metrics, value=提取到的指标字典\n   - field=conclusion, value=\"success\"（如果正常完成且指标合理）\n   - field=status, value=\"DONE\"\n\n## 对比参考\n- Object CRM K=10 (norm02): 16.8±1.8% (n=6)\n- 这个实验测试 K=20 vs K=10 的边际收益\n\n## 注意\n- 用 ssh_read_only 读取 log 和 JSON\n- 只有更新 registry 时用写操作",
  "tool_groups": "['ssh', 'registry']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analyze:eval-crm-object-k20-seed43",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务\n分析已完成的实验 `eval-crm-object-k20-seed43` 的结果。\n\n## 实验信息\n- exp_id: eval-crm-object-k20-seed43\n- server: bjb1-32546\n- log_path: ~/runs/acr-vla-conformal-refinement/eval-crm-object-k20-seed43.log\n- 模式: crm_obs_only, K=20\n- benchmark: LIBERO-Object\n- seed: 43\n- n_rollouts=10\n\n## 操作步骤\n\n1. SSH 到 bjb1-32546，读取 log 文件末尾（tail -100）获取最终结果\n2. 读取 JSON 输出文件（可能路径）：`/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_K20_seed43.json`\n3. 提取关键指标：\n   - success_rate (overall)\n   - per_task success rates\n   - 总 rollout 数\n4. 用 `update_registry` 更新实验：\n   - field=metrics, value=提取到的指标字典\n   - field=conclusion, value=\"success\"（如果正常完成且指标合理）\n   - field=status, value=\"DONE\"\n\n## 对比参考\n- Object CRM K=10 (norm02): 16.8±1.8% (n=6)\n- 这个实验测试 K=20 vs K=10 的边际收益\n\n## 注意\n- 用 ssh_read_only 读取 log 和 JSON\n- 只有更新 registry 时用写操作",
    "tool_groups": "['ssh', 'registry']"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T10:35:09.753543+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analyze_eval-crm-object-k20-seed43_20260520T103506\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-crm-object-k20-seed43_20260520T103506.log\", \"setup_data\": {}, \"message\": \"Worker worker_analyze_eval-crm-object-k20-seed43_20260520T103506 started. Use get_worker_status('worker_analyze_eval-crm-object-k20-seed43_20260520T103506') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 3884
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-20T10:35:20.281567+00:00_

两个分析 Worker 已派发：
- `eval-adaptive-k-spatial-p75-seed43`（本次 cron 回调的目标）
- `eval-crm-object-k20-seed43`（session 初始化发现的 ANALYZING 无 Worker 实验）

当前状态：
- **RUNNING**: 5 个实验（P50-seed42, P25-seed42, P25-seed43, obs-only-norm003-seed43-r2, obs-only-norm005-seed44）
- **ANALYZING**: 5 个实验，均已有 Worker 在处理
- **Worker 池**: 7 个（5 个已有 + 2 个刚派发）

等待 Worker 回调后更新 registry 并汇报 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 33 · 2026-05-21T02:43:25.611307+00:00_

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
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-21T02:44:32.663536+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单必须查 `get_project_status` 的 `execution.gpu_ids`，不可用白名单外的 GPU（即使 Director 指示也必须 push back）
- CRM checkpoint 路径固定：`/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`，max_correction_norm=0.2
- Object CRM K=10 norm02 seed42 (SR=20%) 已被 D084 排除出 Table 1，不可纳入
- Spatial CRM K=10 使用 clean n=8 (34.4±1.5%)，溯源见 D083
- Long OOD 只能用 cautious wording（MW-U p=0.061 n.s.），见 D081
- evaluate.py 使用 batched inference（D082 已确认），延迟表需据此更新

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: 工作目录 `/root/acr-vla-conformal-refinement`，conda base (`/root/miniconda3`)，磁盘 400G/438G 可用(4%)
- **bjb1-32546**: 同上路径和 conda，磁盘 400G/438G 可用(4%)
- **bjb2-40593**: 同上路径和 conda，磁盘 46G/437G 可用(90%) ⚠️ 几乎满
- **bjb2-28827**: 磁盘 399G/439G 可用(5%)
- HF cache: `/root/autodl-tmp/.hf_cache`（所有服务器），HF_HUB_OFFLINE=1 + TRANSFORMERS_OFFLINE=1
- 环境激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 活跃 cron 监控（reconcile 时 6 个）：eval-adaptive-k-spatial-p50-seed42(pid=681823@bjb2-40593), eval-adaptive-k-spatial-p25-seed42(pid=308612@bjb1-18228), eval-adaptive-k-spatial-p25-seed43(@bjb1-32546), eval-crm-object-k20-seed43(@bjb1-32546), eval-obs-only-object-norm003-seed43-r2(@bjb1-32546), eval-obs-only-object-norm005-seed44(@bjb1-32546)

### 3. 📊 当前状态
收到 cron 回调：`eval-adaptive-k-spatial-p75-seed43` 进程退出，状态 ANALYZING。我刚派了两个分析 Worker：
- `worker_analyze_eval-adaptive-k-spatial-p75-seed43_20260520T103414` — SSH 读 log 提取 metrics，更新 registry 到 DONE
- `worker_analyze_eval-crm-object-k20-seed43_20260520T103506` — 同上（该实验也处于 ANALYZING 无 Worker）

**还有 3 个 ANALYZING 实验已有 Worker 在跑**（上一 session 派的）：
- eval-adaptive-k-spatial-p75-seed42 → worker running
- eval-crm-object-k20-seed42 → worker running
- eval-vla-only-long-seed49-r2 → worker running（metrics 已在 registry: SR=0.16）

**RUNNING 实验**（5 个 GPU 在跑）：
- eval-adaptive-k-spatial-p50-seed42 @ bjb2-40593:cuda:0
- eval-adaptive-k-spatial-p25-seed42 @ bjb1-18228:cuda:2
- eval-adaptive-k-spatial-p25-seed43 @ bjb1-32546:cuda:2
- eval-obs-only-object-norm003-seed43-r2 @ bjb1-32546:cuda:4
- eval-obs-only-object-norm005-seed44 @ bjb1-32546:cuda:5

**尚未汇报 Director**——等 Worker 回调拿到 metrics 后需要汇总汇报。

### 4. 📋 待办（条件触发式）
- Worker 回调 P75-seed43 metrics → 合并 P75-seed42 结果 → 计算 Spatial P75 mean±std → 更新 report.md → 汇报 Director（对比 Object P75: 13.7%, Spatial P50 baseline）
- Worker 回调 K20-seed42/seed43 → 计算 K=20 Object mean → 与 K=10 (16.8±1.8%) 对比 → 汇报 Director（K=20 边际收益判断，支撑"K=10 为 compute-efficient 选择"的 claim）
- Worker 回调 VLA-only-long-seed49-r2 → 确认 SR=0.16 写入 DONE → 与已有 Long OOD 数据合并 → 更新 D081 数据
- eval-adaptive-k-spatial-p50-seed42 完成 → 合并 P50 三个 seed → Spatial P50 完整统计 → 这是核心结果（P50=Pareto 最优）
- P25 seed42/seed43 完成 → 补全 Spatial threshold sweep 表
- norm003-seed43-r2 / norm005-seed44 完成 → Figure 2 error bars 补充数据
- 所有 Spatial Adaptive K 完成后 → 更新论文 Table/Figure → 需要 Director 审阅

### 5. 🎯 战略上下文
- **核心方向**：Adaptive inference-time compute for frozen VLAs。K=2 L2 distance 作为不确定性信号（ρ=0.9979 vs K10 variance），自适应决定推理次数。D077 将 Adaptive K 升级为论文核心贡献。
- **投稿目标**：CoRL 2026，DDL 2026-05-29（剩 ~9 天）
- **Object sweep 已完成** 12/12：P50 是 Pareto 最优（SR 15.3%, avg_K ~3.8, fast_path ~77%, vs K=10 ~91%）
- **Spatial cross-benchmark 验证进行中**：P50 已有 seed44-r2 success（~62% compute savings），seed42 还在跑；P75/P25 也在跑。这是证明 Object-calibrated 阈值 transfer 到 Spatial 的关键证据
- **K=20 实验**（plan_601）：测试 K=10→K=20 边际收益，预期收益递减，支撑"K=10 够用"的 claim
- **信号候选已关闭**：只有 K=2 L2 distance 可用（CRM magnitude ρ=0.15 NO-GO, FMVD ρ=0.08 NO-GO）
- **易错点**：bjb2-40593 磁盘几乎满（90%），提交新实验到该服务器前必须先清理
- **易错点**：Registry 的 `filters={"exp_id": "xxx"}` 返回空——exp_id 是 key 不是 field，需用 `filters={"status": "ANALYZING"}` 等 field 过滤后手动匹配
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-adaptive-k-spatial-p75-seed43"
}
```

</details>

---
