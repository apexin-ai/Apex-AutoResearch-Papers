# cron hook pi05 crm always on long s42 20260528T211535 402700

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 2
- **Tool calls:** 13
- **Original source:** `logs/chats/archive/cron_hook_pi05-crm-always-on-long-s42_20260528T211535_402700.jsonl`
- **Structured JSON:** [`56793b5e4798628c4203.json`](../../sessions/56/56793b5e4798628c4203.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-28T05:11:29.823782+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: pi05-crm-always-on-long-s42
- project: acr-vla-conformal-refinement
- server: cqa1-32758

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-28T05:11:42.803468+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__list_workers",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__list_workers",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-28T05:11:42.854469+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-28T05:11:49.339751+00:00_

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
  "session": "cron:hook:pi05-crm-always-on-long-s42",
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

_source line 5 · 2026-05-28T05:11:49.741395+00:00_

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
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-28T05:11:50.193160+00:00_

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
  "session": "cron:hook:pi05-crm-always-on-long-s42",
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

_source line 7 · 2026-05-28T05:11:50.695036+00:00_

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
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-28T05:11:51.148471+00:00_

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
  "session": "cron:hook:pi05-crm-always-on-long-s42",
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

_source line 9 · 2026-05-28T05:11:53.599548+00:00_

Error: result (1,920,132 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-247e851a/37627c1e-839b-45e7-911a-220ed9506305/tool-results/mcp-agent-ml-research-read_registry-1779945113474.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-247e851a/37627c1e-839b-45e7-911a-220ed9506305/tool-results/mcp-agent-ml-research-read_registry-1779945113474.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-247e851a/37627c1e-839b-45e7-911a-220ed9506305/tool-results/mcp-agent-ml-research-read_registry-1779945113474.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 4259
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-28T05:11:53.650373+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 3908
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-28T05:11:53.651262+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-28T05:11:25Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 1353 个实验 — ANALYZING 1, DEPLOYED 6, DONE 1159, PREPARING 183, QUEUED 4\\n**DONE 分布**: failed 114, killed 217, negative 95, success 733\\n\\n### 💾 磁盘余量\\n- **bjb1-18228**:\\n  - `/init`: 150M/150M 可用（已用 1%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb1-32546**:\\n  - `/autodl-pub`: 1.3T/7.0T 可用（已用 83%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb2-28827**:\\n  - `/autodl-pub`: 4.4T/14T 可用（已用 69%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/439G 可用（已用 5%）\\n- **cqa1-32758**:\\n  - `/autodl-pub`: 486G/7.0T 可用（已用 94%） ⚠️\\n  - `/autodl-pub/data`: 1.5T/4.0T 可用（已用 65%）\\n  - `/usr/bin/nvidia-smi`: 77G/98G 可用（已用 19%）\\n\\n### 🏃 RUNNING\\n_（无）_\\n\\n### 📌 最近完成 (top 5)\\n- `eval-supp-spatial-k2mean-s47` [success] — 2026-05-28T05:02:10\\n- `eval-supp-long-vla-only-s44` [success] — 2026-05-28T05:02:01\\n- `eval-supp-spatial-adapt-tau025-s47` [negative] — 2026-05-28T05:01:48\\n- `eval-supp-long-vla-only-s42` [success] — 2026-05-28T05:01:35\\n- `smolvla-adapt-tau015-object-s44-cqa1` [success] — 2026-05-28T05:01:24\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-28\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| pi05-crm-always-on-long-s42 | Pi05 CRM always-on (τ=0.001) on Long suite s42. Ablation: CRM correction applied every step (trigger_rate=100%) to measure CRM-only contribution without conformal gating. Table 1 data for Pi05 model. | — | — | — |\\n\\n## 待处理\\n- eval-k2-tau035-spatial-s42: K=2
…[truncated 6779 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 3458
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T05:11:53.702883+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-28 01:12 UTC | 更新原因: Long CRM always-on 3-seed 到齐 (43.2%), 4/4 suites harmful 确认, 额外 seeds 验证一致性\\n\\n> 详见 paper_framing.md（D170/D177/D178: K=2 CRM always-on 4/4 harmful + K-matched Table 1）\\n\\n## 核心方向\\n**ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs**。CoRL 2026 DDL **2026-05-28 20:00 北京时间**。\\n\\n## 当前进展\\n- **Table 1 重构**: K-matched 3 列（VLA-only K=1 / K=2 CRM always-on / K=2 Adaptive），消除 K confound\\n- **K=2 CRM always-on 数据**: ✅ 全部 4 suites × 3 seeds 完成，额外 seeds (s45/s46) 确认一致性\\n- **核心发现**: CRM always-on 在 **4/4 suites** 有害（Object -4.7pp, Spatial -1.3pp, Goal -3.7pp, Long -14.8pp）；Adaptive 全面恢复\\n- **叙事**: \\\"CRM 修正是双刃剑，gating 正确决定何时不干预\\\" — Long -14.8pp 是最有力单一证据\\n- **Table 2 (π0.5)**: CRM always-on 实验 cqa1 运行中，VLA-only baseline ✅ 锁定\\n- **Paper Agent**: ✅ 已派单 Table 1 重构 + 叙事 4/4 升级 + 审稿遗留修复\\n- **审稿**: ✅ Round 3 完成，W6(ε confound) 和 W7(K=2 argmin) 已解决\\n\\n## CRM always-on 最终数据（SmolVLA, K=2, n=3）\\n| Suite | VLA-only (K=1) | CRM always-on (K=2) | Adaptive (K=2) | Δ CRM vs VLA | Δ Adaptive vs VLA |\\n|-------|---------------|--------------------|-----------|----|---|\\n| Spatial | 79.3±0.8 | 78.0±1.7 | 80.8±1.1 | -1.3pp | +1.5pp |\\n| Goal | 83.7±1.3 | 80.0±0.5 | 85.0±1.3 | -3.7pp | +1.3pp |\\n| Object | 77.7±1.3 | 73.0±1.8 | 77.8±2.1 | -4.7pp | +0.1pp |\\n| Long | 58.0±1.5 | 43.2±2.3 | 57.7±1.5 | -14.8pp | -0.3pp |\\n\\n## 近期任务\\n- [x] **P0** 收集 Long CRM always-on 3 seeds 结果 → 43.2% (41/45.5/43)\\n- [ ] **P0** Paper Agent 完成 Table 1 重构 + 叙事 4/4 升级\\n- [ ] **P0** 等待用户确认：title 方案 + CoRL 提交/撤回决定\\n- [ ] **P1** Pi05 CRM always-on (cqa1-32758) 运行中 → Table 2\\n- [ ] **P1** Bonus seeds (object-s45/s46, long-s45) 自然完成\\n- [ ] **P2** 最终论文提交 submit_paper_to_review\\n\\n## Claim 策略 (D170/D178 updated)\\n- *
…[truncated 2460 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 3007
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-28T05:11:53.853937+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 2705
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-28T05:12:03.788477+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'pi05-crm-always-on-long-s42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'pi05-crm-always-on-long-s42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T05:12:04.493990+00:00_

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
  "session": "cron:hook:pi05-crm-always-on-long-s42",
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

_source line 16 · 2026-05-28T05:12:06.966479+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1378}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 3178
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-28T05:12:09.927386+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"pi05-crm-always-on-long-s42\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T21:56:13.252Z\", \"updated_at\": \"2026-05-28T05:11:10.953Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark long --seed 42 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:5\"], \"pid\": \"156008\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s42.log\", \"submitted_at\": \"2026-05-27T21:56:10.320Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval-only)\", \"model_name\": \"pi05\", \"seed\": 42, \"data_path\": \"LIBERO long benchmark\", \"data_count\": 200}, \"hypothesis\": \"Pi05 CRM always-on (τ=0.001) on Long suite s42. Ablation: CRM correction applied every step (trigger_rate=100%) to measure CRM-only contribution without conformal gating. Table 1 data for Pi05 model.\", \"reproduce\": {\"finished_at\": \"2026-05-28T05:11:05.760Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-28T05:11:29.007818+00:00\"}]}}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9471}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 5433
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-28T05:12:20.849601+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T05:12:20.900447+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-28T05:12:24.162285+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'pi05-crm-always-on-long-s42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'pi05-crm-always-on-long-s42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-28T05:12:27.276389+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.068}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 3114
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-28T05:12:57.218498+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "analysis:pi05-crm-always-on-long-s42",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务\n分析实验 `pi05-crm-always-on-long-s42` 的结果。\n\n## 实验信息\n- **exp_id**: pi05-crm-always-on-long-s42\n- **server**: cqa1-32758\n- **log_path**: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s42.log\n- **command**: `python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark long --seed 42 --n_rollouts 20`\n- **hypothesis**: Pi05 CRM always-on (τ=0.001) on Long suite s42. Ablation: CRM correction applied every step (trigger_rate=100%) to measure CRM-only contribution without conformal gating. Table 2 data for Pi05 model.\n- **status**: ANALYZING (进程已正常退出)\n\n## 步骤\n\n1. **SSH 读取日志**：连接 cqa1-32758，读取 `~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s42.log` 的最后 100 行，提取：\n   - 总体 success rate (%)\n   - 各 task 的 success rate\n   - trigger_rate / correction 相关统计\n   - 是否有 error/warning\n\n2. **查 W&B**：用 `fetch_wandb_metrics` 查询 run（run name 可能是 `pi05-crm-always-on-long-s42` 或类似），metrics: `[\"success_rate\", \"avg_success_rate\", \"trigger_rate\", \"mean_correction_norm\"]`。如果不确定 run_id，先搜索。\n\n3. **对比 baseline**：查 registry 中以下实验的 metrics，用于对比：\n   - `pi05-vla-only-long-*` (Pi05 VLA-only Long baseline)\n   - 其他 `pi05-crm-always-on-*` 实验（Object/Spatial/Goal suites）\n\n4. **输出**：用 `update_registry` 更新实验：\n   - 设置 `conclusion`: 根据结果判断（如果 success rate 低于 VLA-only baseline → negative；如果高于 → success）\n   - 设置 `metrics`: 包含 success_rate 和其他关键指标\n   - 设置 `status`: DONE\n   \n   注意：CRM always-on 预期是 harmful（低于 VLA-only），如果确认 harmful 则 conclusion=success（因为 hypothesis 是验证 CRM always-on 的负面影响）。\n\n5. **汇总报告**：返回：\n   - Pi05 CRM always-on Long s42 的 success rate\n   - 与 Pi05 VLA-only Long baseline 的对比 (Δ)\n   - 与其他 Pi05 suites CRM always-on 的一致性\n   - 对 Table 2 的影响\n\n关键：这是 Table 2 (跨模型泛化) 的数据点。SmolVLA 上 CRM always-on 4/4 suites harmful，Pi05 如果也 harmful 则支持 MC1 (cross-VLA generalization)。\n",
  "tool_groups": "['ssh', 'wandb', 'registry']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analysis:pi05-crm-always-on-long-s42",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务\n分析实验 `pi05-crm-always-on-long-s42` 的结果。\n\n## 实验信息\n- **exp_id**: pi05-crm-always-on-long-s42\n- **server**: cqa1-32758\n- **log_path**: ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s42.log\n- **command**: `python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark long --seed 42 --n_rollouts 20`\n- **hypothesis**: Pi05 CRM always-on (τ=0.001) on Long suite s42. Ablation: CRM correction applied every step (trigger_rate=100%) to measure CRM-only contribution without conformal gating. Table 2 data for Pi05 model.\n- **status**: ANALYZING (进程已正常退出)\n\n## 步骤\n\n1. **SSH 读取日志**：连接 cqa1-32758，读取 `~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s42.log` 的最后 100 行，提取：\n   - 总体 success rate (%)\n   - 各 task 的 success rate\n   - trigger_rate / correction 相关统计\n   - 是否有 error/warning\n\n2. **查 W&B**：用 `fetch_wandb_metrics` 查询 run（run name 可能是 `pi05-crm-always-on-long-s42` 或类似），metrics: `[\"success_rate\", \"avg_success_rate\", \"trigger_rate\", \"mean_correction_norm\"]`。如果不确定 run_id，先搜索。\n\n3. **对比 baseline**：查 registry 中以下实验的 metrics，用于对比：\n   - `pi05-vla-only-long-*` (Pi05 VLA-only Long baseline)\n   - 其他 `pi05-crm-always-on-*` 实验（Object/Spatial/Goal suites）\n\n4. **输出**：用 `update_registry` 更新实验：\n   - 设置 `conclusion`: 根据结果判断（如果 success rate 低于 VLA-only baseline → negative；如果高于 → success）\n   - 设置 `metrics`: 包含 success_rate 和其他关键指标\n   - 设置 `status`: DONE\n   \n   注意：CRM always-on 预期是 harmful（低于 VLA-only），如果确认 harmful 则 conclusion=success（因为 hypothesis 是验证 CRM always-on 的负面影响）。\n\n5. **汇总报告**：返回：\n   - Pi05 CRM always-on Long s42 的 success rate\n   - 与 Pi05 VLA-only Long baseline 的对比 (Δ)\n   - 与其他 Pi05 suites CRM always-on 的一致性\n   - 对 Table 2 的影响\n\n关键：这是 Table 2 (跨模型泛化) 的数据点。SmolVLA 上 CRM always-on 4/4 suites harmful，Pi05 如果也 harmful 则支持 MC1 (cross-VLA generalization)。\n",
    "tool_groups": "['ssh', 'wandb', 'registry']"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-28T05:13:01.467649+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_pi05-crm-always-on-long-s42_20260528T051257\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analysis_pi05-crm-always-on-long-s42_20260528T051257.log\", \"setup_data\": {}, \"message\": \"Worker worker_analysis_pi05-crm-always-on-long-s42_20260528T051257 started. Use get_worker_status('worker_analysis_pi05-crm-always-on-long-s42_20260528T051257') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 4249
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-28T05:13:01.611304+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | python3 -c \"\nimport sys, yaml\ndata = yaml.safe_load(sys.stdin)\nexps = data.get('experiments', {})\npi05_exps = {k: v for k, v in exps.items() if 'pi05' in k}\nfor k, v in sorted(pi05_exps.items()):\n    status = v.get('status', '?')\n    conclusion = v.get('conclusion', '')\n    metrics = v.get('metrics', {})\n    sr = metrics.get('success_rate', metrics.get('avg_success_rate', ''))\n    hyp = (v.get('hypothesis', '') or '')[:80]\n    print(f'{k}: {status}/{conclusion} sr={sr} | {hyp}')\n\" 2>/dev/null",
  "description": "Extract Pi05 experiments from registry",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | python3 -c \"\nimport sys, yaml\ndata = yaml.safe_load(sys.stdin)\nexps = data.get('experiments', {})\npi05_exps = {k: v for k, v in exps.items() if 'pi05' in k}\nfor k, v in sorted(pi05_exps.items()):\n    status = v.get('status', '?')\n    conclusion = v.get('conclusion', '')\n    metrics = v.get('metrics', {})\n    sr = metrics.get('success_rate', metrics.get('avg_success_rate', ''))\n    hyp = (v.get('hypothesis', '') or '')[:80]\n    print(f'{k}: {status}/{conclusion} sr={sr} | {hyp}')\n\" 2>/dev/null",
    "description": "Extract Pi05 experiments from registry",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-28T05:13:06.141714+00:00_

&lt;persisted-output>
Output too large (35.4KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-247e851a/37627c1e-839b-45e7-911a-220ed9506305/tool-results/bgu43ksyq.txt

Preview (first 2KB):
crm-train-pi05-object: DONE/killed sr= | CRM projection trained on π0.5 precomputed features (49700 object samples, K=10)
crm-train-pi05-object-full: DONE/success sr= | CRM projection trained on π0.5 full precomputed features (69303 object samples, 
crm-train-pi05-spatial: DONE/killed sr= | CRM projection trained on π0.5 precomputed features (38500 spatial samples, K=10
crm-train-pi05-spatial-full: DONE/success sr= | CRM projection trained on π0.5 full precomputed features (~60250 spatial samples
crm-train-pi05-spatial-v2: DONE/success sr= | CRM projection trained on π0.5 full precomputed features (60250 spatial samples,
eval-pi05-adaptive-goal-s42: DONE/failed sr=0 | π0.5 Adaptive (τ=0.25, K=2 hardcoded) 在 Goal benchmark 上通过 conformal gating 选择性修
eval-pi05-adaptive-goal-s42-dryrun: DONE/success sr= | π0.5 Adaptive (τ=0.25, K=2) Goal dry-run — 验证 OOM fix 后 VRAM 稳定性和 trigger_rate 合
eval-pi05-adaptive-goal-s42-full: PREPARING/ sr= | 
eval-pi05-adaptive-goal-s43: DONE/killed sr= | π0.5 Adaptive CRM (τ=0.25) Goal s43。跨模型验证：VLA-only baseline SR=0.97。测试 gating 在 
eval-pi05-adaptive-goal-s44: DONE/killed sr= | 
eval-pi05-adaptive-object-s42: DONE/killed sr= | π0.5 Adaptive CRM (τ=0.25) Object s42。跨模型验证 Object suite。
eval-pi05-adaptive-object-s43: DONE/killed sr= | π0.5 Adaptive CRM (τ=0.25) Object s43。跨模型验证 Object suite seed 43。
eval-pi05-adaptive-object-s44: DONE/killed sr= | 
eval-pi05-adaptive-spatial-s42: DONE/failed sr= | π0.5 Adaptive CRM (K=2, τ=0.25) on Spatial s42. 跨模型验证：π0.5 是否也能从 uncertainty gat
eval-pi05-adaptive-spatial-s42-r2: DONE/killed sr= | π0.5 Adaptive CRM (K=2, τ=0.25) on LIBERO-Spatial s42. Retry of failed s42 run: 
eval-pi05-baseline-object-see
…[truncated 263 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "Bash",
  "elapsed_ms": 4530
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-28T05:13:22.546001+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | python3 -c \"\nimport sys, yaml\ndata = yaml.safe_load(sys.stdin)\nexps = data.get('experiments', {})\n\n# Filter for Pi05 CRM always-on and VLA-only experiments\nfor pattern in ['pi05-crm-always-on', 'pi05-vla-only']:\n    print(f'\\n=== {pattern} ===')\n    for k, v in sorted(exps.items()):\n        if pattern in k:\n            status = v.get('status', '?')\n            conclusion = v.get('conclusion', '')\n            metrics = v.get('metrics', {})\n            sr = metrics.get('success_rate', metrics.get('avg_success_rate', ''))\n            hyp = (v.get('hypothesis', '') or '')[:100]\n            print(f'{k}: {status}/{conclusion} sr={sr} | {hyp}')\n\" 2>/dev/null",
  "description": "Filter Pi05 CRM always-on and VLA-only experiments",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | python3 -c \"\nimport sys, yaml\ndata = yaml.safe_load(sys.stdin)\nexps = data.get('experiments', {})\n\n# Filter for Pi05 CRM always-on and VLA-only experiments\nfor pattern in ['pi05-crm-always-on', 'pi05-vla-only']:\n    print(f'\\n=== {pattern} ===')\n    for k, v in sorted(exps.items()):\n        if pattern in k:\n            status = v.get('status', '?')\n            conclusion = v.get('conclusion', '')\n            metrics = v.get('metrics', {})\n            sr = metrics.get('success_rate', metrics.get('avg_success_rate', ''))\n            hyp = (v.get('hypothesis', '') or '')[:100]\n            print(f'{k}: {status}/{conclusion} sr={sr} | {hyp}')\n\" 2>/dev/null",
    "description": "Filter Pi05 CRM always-on and VLA-only experiments",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-28T05:13:25.811535+00:00_

=== pi05-crm-always-on ===
pi05-crm-always-on-goal-s42: DONE/success sr=81.5 | Pi05 CRM always-on (τ=0.001) on Goal suite s42. Ablation: CRM correction applied every step (trigger
pi05-crm-always-on-goal-s43: PREPARING/ sr= | Pi05 CRM always-on (τ=0.001) on Goal suite s43. Second seed for Table 2 Goal row, measuring CRM-only
pi05-crm-always-on-goal-s44: PREPARING/ sr= | Pi05 CRM always-on (τ=0.001) on Goal suite s44. Third seed for Table 2 Goal row.
pi05-crm-always-on-long-s42: ANALYZING/ sr= | Pi05 CRM always-on (τ=0.001) on Long suite s42. Ablation: CRM correction applied every step (trigger
pi05-crm-always-on-long-s43: PREPARING/ sr= | Pi05 CRM always-on (τ=0.001) on Long suite s43. Second seed for Table 2 Long row, measuring CRM-only
pi05-crm-always-on-long-s44: PREPARING/ sr= | Pi05 CRM always-on (τ=0.001) on Long suite s44. Third seed for Table 2 Long row.
pi05-crm-always-on-object-s42: DONE/success sr=90.5 | Pi05 CRM always-on (τ=0.001) on Object suite s42. Ablation: CRM correction applied every step (trigg
pi05-crm-always-on-object-s43: DONE/success sr=92 | Pi05 CRM always-on (τ=0.001) on Object suite s43. Ablation: CRM correction applied every step (trigg
pi05-crm-always-on-object-s44: PREPARING/ sr= | Pi05 CRM always-on (τ=0.001) on Object suite s44. Third seed for Table 2 Object row.
pi05-crm-always-on-spatial-s42: DONE/success sr=96 | Pi05 CRM always-on (τ=0.001) on Spatial suite s42. Ablation: CRM correction applied every step (trig
pi05-crm-always-on-spatial-s43: PREPARING/ sr= | Pi05 CRM always-on (τ=0.001) on Spatial suite s43. Second seed for Table 2 Spatial row.
pi05-crm-always-on-spatial-s44: PREPARING/ sr= | Pi05 CRM always-on (τ=0.001) on Spatial suite s44. Third seed for Table 2 Spatial row.

=== pi05-vla-only ===
eval-pi05-vla-only-goal-s42: DONE/success sr= | π0.5 VLA-only baseline on LIBERO-Goal (seed 42, 20 rollouts). Establishes pi0.5 goal-conditioned bas
eval-pi05-vla-only-goal-s42-paired: DONE/success sr=0.98 | π0.5 VLA-only baseline Goa
…[truncated 11438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "tool": "Bash",
  "elapsed_ms": 3265
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-28T05:13:55.468299+00:00_

Worker 已派发分析 `pi05-crm-always-on-long-s42`。

已有的 Pi05 CRM always-on 数据（单 seed s42）：
- Object: 90.5%（VLA-only ~96.5-99% → harmful）
- Spatial: 96%（VLA-only ~98% → harmful）
- Goal: 81.5%（VLA-only ~97.5% → harmful）
- **Long: 待分析**（VLA-only ~94-95%）

等待 Worker 完成后汇报 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:pi05-crm-always-on-long-s42"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 29 · 2026-05-28T21:14:34.510830+00:00_

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
  "session": "cron:hook:pi05-crm-always-on-long-s42",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-28T21:15:35.398065+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：bjb1-18228, bjb1-32546, bjb2-28827, cqa1-32758 共 22 张卡
- cqa1-32758 磁盘 /autodl-pub 已用 94% ⚠️，提交新实验前必须检查磁盘
- Pi05 实验必须在 4090 服务器（cqa1-32758）上跑，因为 Pi05 模型权重只在该服务器部署
- Table 2 只做 degradation-only 两列（VLA-only + CRM always-on），不做 Adaptive 列（D181 决策）
- westd-49937 服务器数据已确认系统性偏低 4-5pp（D174/D175），该服务器的 paired 数据仅作参考，Table 用 4090 服务器数据
- CoRL 2026 DDL **2026-05-28 20:00 北京时间**——今天截稿

### 2. 🖥️ 基础设施快照
- **cqa1-32758**（Pi05 主力）: 工作目录 `/root/autodl-tmp/acr-vla-conformal-refinement/`，conda base（`/root/miniconda3/bin/python`），6× GPU
- **bjb1-32546 / bjb2-28827**（SmolVLA 主力）: 同上结构，各 6× GPU
- **bjb1-18228**: 6× GPU，部分 Pi05 VLA-only baseline 在此跑过
- Pi05 模型路径: cqa1 上 `/root/autodl-tmp/` 下（具体路径需 SSH 确认）
- SmolVLA CRM checkpoint: 各服务器 `/root/autodl-tmp/acr-vla-conformal-refinement/checkpoints/`
- W&B project: 通过 project config 获取，metrics 包括 success_rate, trigger_rate, mean_correction_norm
- 活跃进程: **无**（所有 RUNNING 实验已完成或转 ANALYZING）
- 活跃 Worker: **无**（刚 spawn 了 `worker_analysis_pi05-crm-always-on-long-s42_20260528T051257`，可能还在跑）

### 3. 📊 当前状态
**刚做完**: Session 初始化（reconcile crons + read registry + read report/roadmap），spawn Worker 分析 `pi05-crm-always-on-long-s42` 结果。

**pi05-crm-always-on-long-s42 关键信息**:
- 状态: ANALYZING，进程正常退出，W&B 数据可用
- 命令: `python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark long --seed 42 --n_rollouts 20`
- 对比 baseline: Pi05 VLA-only Long s42 = 94%（4090 服务器）/ 98%（westd）
- 预期: CRM always-on harmful（SmolVLA Long -14.8pp）

**已完成的 Pi05 CRM always-on 数据**:
| Suite | s42 | s43 | s44 | VLA-only baseline (4090, 3-seed mean) |
|-------|-----|-----|-----|--------------------------------------|
| Object | 90.5% | 92% | PREPARING | ~99.3% → Δ≈-8pp |
| Spatial | 96% | PREPARING | PREPARING | ~98% → Δ≈-2pp |
| Goal | 81.5% | PREPARING | PREPARING | ~97.5% → Δ≈-16pp |
| Long | ANALYZING | PREPARING | PREPARING | ~95% → 待确认 |

**PREPARING 实验** (12 个 Pi05 CRM always-on s43/s44): 等 GPU 和 DDL 前排期，但 DDL 就是今天。

**等待中**:
- Worker `worker_analysis_pi05-crm-always-on-long-s42` 回调 → 需要处理结果、更新 registry、汇报 Director
- Paper Agent 可能还在完成 Table 1 重构 + 叙事升级（上次 report 提到已派单）

### 4. 📋 待办（条件触发式）
- Worker 分析回调到达 → 读取 Long s42 success rate → update_registry(conclusion, metrics, status=DONE) → 汇报 Director Table 2 Long 数据点
- Long s42 success rate 显著低于 94% baseline → conclusion=success（CRM harmful 确认），Pi05 跨模型一致性 MC1 强化
- Long s42 接近或高于 baseline → 异常，需要与 SmolVLA Long -14.8pp 对比分析，汇报 Director
- Pi05 4 suites 单 seed 数据齐全后 → 汇报 Director Table 2 完整 single-seed 数据，建议是否用单 seed 提交（DDL 今天）
- DDL 前 Paper Agent 完成 → 最终论文审查 + 提交流程

### 5. 🎯 战略上下文
- **核心叙事**: "CRM 修正是双刃剑，gating 正确决定何时不干预"。CRM always-on 4/4 suites harmful 是论文最有力证据。
- **Table 2 策略 (D181)**: 只做 degradation-only 两列（VLA-only + CRM always-on），不做 Adaptive 列。目的是跨模型验证 MC1（CRM 无选择地施加 = harmful）。
- **Pi05 数据现状**: Object/Spatial/Goal/Long 各只有 s42 一个 seed 完成（Long 还在 ANALYZING）。s43/s44 全部 PREPARING。DDL 今天，大概率 Table 2 只能用单 seed 数据。
- **易错点**: 
  - Pi05 VLA-only baseline 有多个版本（r3/r4/paired/westd），Table 2 应用 4090 服务器的 r4 版本数据（D173/D175 决策）
  - 不要把 westd 服务器数据和 4090 服务器数据混用（LIBERO assets 版本差异导致 4-5pp 偏差）
  - Pi05 CRM always-on 的 conclusion 应该是 success（因为 hypothesis 是验证 harmful effect，harmful 确认 = hypothesis 成立）
- **决策链**: D177（Table 1 K-matched 3列）→ D178（Long -14.8pp 最有力证据）→ D179（Title 锁定）→ D180（Table 2 叙事）→ D181（Table 2 degradation-only）
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:pi05-crm-always-on-long-s42"
}
```

</details>

---
