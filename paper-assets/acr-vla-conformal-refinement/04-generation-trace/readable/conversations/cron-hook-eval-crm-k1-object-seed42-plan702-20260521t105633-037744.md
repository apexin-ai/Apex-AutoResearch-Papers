# cron hook eval crm k1 object seed42 plan702 20260521T105633 037744

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 3
- **Tool calls:** 11
- **Original source:** `logs/chats/archive/cron_hook_eval-crm-k1-object-seed42-plan702_20260521T105633_037744.jsonl`
- **Structured JSON:** [`742dd1a0a8e7445d62ec.json`](../../sessions/74/742dd1a0a8e7445d62ec.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-20T14:28:37.992154+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: eval-crm-k1-object-seed42-plan702
- project: acr-vla-conformal-refinement
- server: bjb2-28827
- log_path: ~/runs/acr-vla-conformal-refinement/eval-crm-k1-object-seed42-plan702.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-20T14:28:55.356860+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__save_project_file",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__save_project_file",
    "max_results": "11"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-20T14:28:55.412779+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "tool": "ToolSearch",
  "elapsed_ms": 55
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T14:28:59.227624+00:00_

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
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
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

_source line 5 · 2026-05-20T14:28:59.228076+00:00_

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
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T14:29:00.191522+00:00_

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
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
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

_source line 7 · 2026-05-20T14:29:00.302592+00:00_

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
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T14:29:01.623984+00:00_

Error: result (701,641 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-131a8faa/cd6987f2-22f4-415e-b1cc-6178a8a33f57/tool-results/mcp-agent-ml-research-read_registry-1779287341446.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-131a8faa/cd6987f2-22f4-415e-b1cc-6178a8a33f57/tool-results/mcp-agent-ml-research-read_registry-1779287341446.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2396
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T14:29:54.868509+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 8, \"results\": [{\"exp_id\": \"eval-perdof-object-norm02-seed49\", \"success\": true, \"actions\": [\"Job still running (pid=450375)\"]}, {\"exp_id\": \"eval-adaptive-k-spatial-p90-seed44\", \"success\": true, \"actions\": [\"Job still running (pid=384503)\"]}, {\"exp_id\": \"eval-random-selection-spatial-seed42-r2\", \"success\": true, \"actions\": [\"Job still running (pid=384777)\"]}, {\"exp_id\": \"eval-obs-only-spatial-norm02-seed48\", \"success\": true, \"actions\": [\"Job still running (pid=385308)\"]}, {\"exp_id\": \"eval-vla-only-spatial-seed48\", \"success\": true, \"actions\": [\"Job still running (pid=385902)\"]}, {\"exp_id\": \"eval-obs-only-spatial-norm02-seed49\", \"success\": true, \"actions\": [\"Job still running (pid=357304)\"]}, {\"exp_id\": \"eval-crm-k1-object-seed43-plan702\", \"success\": true, \"actions\": [\"Skipped (created 84s ago < interval 120s)\"]}, {\"exp_id\": \"eval-crm-k1-object-seed44-plan702\", \"success\": true, \"actions\": [\"Skipped (created 83s ago < interval 120s)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 55640
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T14:29:54.921231+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-20T14:29:31Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 458 个实验 — ANALYZING 4, DEPLOYED 4, DONE 408, PREPARING 37, RUNNING 5\\n**DONE 分布**: failed 47, killed 82, negative 33, success 246\\n\\n### GPU 占用\\n- **实际运行**: 5 张 — bjb1-18228:cuda:0(eval-adaptive-k-spatial-p90-seed44), bjb1-18228:cuda:1(eval-random-selection-spatial-seed42-r2), bjb2-28827:cuda:2(eval-obs-only-spatial-norm02-seed49), bjb2-28827:cuda:3(openvla-precompute-k1), bjb1-32546:cuda:2(eval-perdof-object-norm02-seed49)\\n\\n### 💾 磁盘余量\\n- **bjb2-40593**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 46G/437G 可用（已用 89%）\\n- **bjb1-18228**:\\n  - `/autodl-pub`: 791G/7.0T 可用（已用 89%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb1-32546**:\\n  - `/autodl-pub`: 890G/7.0T 可用（已用 88%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb2-28827**:\\n  - `/autodl-pub`: 4.5T/14T 可用（已用 69%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/439G 可用（已用 5%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `eval-adaptive-k-spatial-p90-seed44` | bjb1-18228 | cuda:0 | 384493 | `…conformal-refinement/eval-adaptive-k-spatial-p90-seed44.log` |\\n| `eval-random-selection-spatial-seed42-r2` | bjb1-18228 | cuda:1 | 384767 | `…rmal-refinement/eval-random-selection-spatial-seed42-r2.log` |\\n| `eval-obs-only-spatial-norm02-seed49` | bjb2-28827 | cuda:2 | 357291 | `…onformal-refinement/eval-obs-only-spatial-norm02-seed49.log` |\\n| `openvla-precompute-k1` | bjb2-28827 | cuda:3 | 365142 | `…runs/acr-vla-
…[truncated 7775 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 54729
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T14:29:54.921856+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-20 06:17 UTC | 更新原因: Fix Long OOD data to match D081, update RUNNING section per Reviewer observation\\n\\n> 详见 paper_framing.md（D077: Adaptive K 升级为核心贡献）\\n\\n## 核心方向\\n**Adaptive inference-time compute for frozen VLAs** — K=2 L2 distance 作为不确定性信号，自适应决定每步推理次数。CRM correction>selection 分析作为支撑。\\n\\n## 投稿目标\\n**CoRL 2026** DDL **2026-05-29**。剩余 ~9 天。\\n\\n## D077 方向转换（用户硬要求）\\n- Adaptive K = 论文**核心贡献**（方法）\\n- K=10 分析降为 supporting evidence\\n\\n## 信号候选 (CLOSED)\\n| 信号 | ρ vs K10_var | 结论 |\\n|------|-------------|------|\\n| **K=2 L2 distance** | **0.9979** | **✅ GO — 唯一可用信号** |\\n| CRM correction magnitude | 0.1523 | ❌ NO-GO (D079) |\\n| FMVD | 0.0825 | ❌ NO-GO |\\n\\n## Adaptive K Sweep (Object) — 12/12 DONE ✅\\n| 阈值 | seeds | SR (mean) | avg_K | fast_path% | vs K=10 |\\n|------|-------|-----------|-------|-----------|---------|\\n| P90 | 3/3 ✅ | 13.3% | ~2.6 | ~93% | 74% |\\n| P75 | 3/3 ✅ | 13.7% | ~3.1 | ~87% | 79% |\\n| **P50** | **3/3 ✅** | **15.3%** | **~3.8** | **~77%** | **~91%** |\\n| P25 | 3/3 ✅ | 14.3% | ~4.8 | ~65% | ~85% |\\n\\n**P50 = Pareto 最优 (D078)**。\\n\\n## RUNNING 实验\\n- bjb2-40593: Spatial Adaptive K P50 seed42 (rollout 中)\\n- bjb1-18228: Long VLA-only seed54, Long CRM seed53, Spatial VLA-only seed53\\n- bjb1-32546: Long CRM seed54, Spatial VLA-only seed54\\n- 更多部署中（Agent 处理综合指令）\\n\\n## 待部署\\n1. **Spatial Adaptive K P50 seed43, seed44**\\n2. **Random Selection baseline seed42, seed44** (plan_600)\\n3. **CRM Object K=10 norm02 seed42** (Table 1 n=6→n=7)\\n4. **fig3_kvalue 重新生成**\\n\\n## 论文 CRITICAL 待解决\\n1. **evaluate.py 推理模式确认** — Agent P0\\n2. **Spatial CRM K=10 n=8 溯源** — registry 只有 n=7, Agent 调查中\\n3. **OOD Long/Goal 数据全量更新** — Paper Agent 处理中\\n4. **P25 n=3 更新** — Paper Agent 处理中\\n\\n## 核心实验结果 (LOCKED,
…[truncated 2698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 54619
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T14:30:01.009969+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-crm-k1-object-seed42-plan702'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-crm-k1-object-seed42-plan702'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T14:30:02.019426+00:00_

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
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
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

_source line 14 · 2026-05-20T14:30:02.725390+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "memory.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "memory.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T14:30:03.132379+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0393}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2122
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T14:30:06.500732+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-crm-k1-object-seed44-plan702\": {\"status\": \"ANALYZING\", \"conclusion\": \"\", \"failure_reason\": \"\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:50:04.763Z\", \"updated_at\": \"2026-05-20T14:29:16.043Z\", \"hypothesis\": \"K=1 CRM (ACCG) on LIBERO-Object seed44 for plan_702. Single VLA forward + CRM correction.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 44 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2 --output_file logs/eval_crm_k1_object_seed44_plan702.json 2>&1 | tee logs/eval-crm-k1-object-seed44-plan702.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"381573\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-k1-object-seed44-plan702.log\", \"submitted_at\": \"2026-05-20T13:50:39.297Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T14:29:12.945Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T14:29:37.626962+00:00\"}]}}, \"eval-crm-k1-object-seed43-plan702\": {\"status\": \"ANALYZING\", \"conclusion\": \"\", \"failure_reason\": \"\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:50:02.848Z\", \"updated_at\": \"2026-05-20T14:28:50.245Z\", \"hypothesis\": \"K=1 CRM (ACCG) on LIBERO-Object seed43 for plan_702. Single VLA forward + CRM correction.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFF
…[truncated 3537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 4481
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T14:30:06.553747+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\", \"content\": \"# Project Memory\\n\\n## 失败模式记录\\n\\n- [失败模式] Cron false positive：eval 脚本不写 W&B 也不写 sentinel file，进程正常退出后 cron 5 次检测找不到标记 → 自动标记为 failed。受影响：eval-vla-only-long-seed46, eval-vla-only-goal-seed46。修复方案：tail 日志确认实际完成 → 手动修正 conclusion=success + 补录 metrics。预防：eval 实验应检查 output JSON 是否存在作为 sentinel。\\n\\n- [失败模式] Cron false positive（2026-05-20）：**eval-adaptive-k-spatial-p50-seed42** 被 cron 误判为 failed（\\\"process dead 5× with no sentinel/W&B\\\"）。实际情况：原 PID 675831 被 deploy worker kill 后，重启为 PID 681823。重启后进程正常运行，但 cron 监控未追踪到新 PID，5 次检测均未发现 sentinel → 自动标记 failed。诊断时（2026-05-20）PID 681823 仍在运行（状态 Rl+，已运行 17h36m），已完成 3/10 tasks（SR: 70%/100%/0%），第 4 个 task 进行中（rollout 5, 1/5 success）。GPU 使用 5972/24564 MiB，日志无错误。**无需重新提交，等待自然完成后手动修正 conclusion。**\\n\\n- [失败模式] SIGHUP false failure（2026-05-20）：bjb2-28827 上多个实验 EXIT_CODE=129 (SIGHUP) 被标记 failed，实际全部完成。**已确认受影响：P75-seed44, P90-seed42, P25-seed44**。SIGHUP 发生在进程写完结果 JSON 之后（tmux session 断开或 SSH 连接清理）。**诊断方法：tail 日志看 \\\"Results saved to\\\" + \\\"Overall success rate\\\" 行 → 手动修正 conclusion=success 并补录 metrics。**\\n\\n- [失败模式] Cron 日志路径不匹配（2026-05-20）：**eval-obs-only-goal-norm02-seed51** (bjb1-32546) 被 cron 误判 dead。根因：实验日志写入 `/root/acr-vla-conformal-refinement/logs/`（项目目录下），但 cron 监控在 `~/runs/acr-vla-conformal-refinement/` 下找日志 → 找不到 → 5 次检测均无 sentinel → auto-resolved failed。**教训：submit_training_job 的 log_path 必须与实际 tee 输出路径一致。部分实验用 `tee logs/xxx.log`（相对于 cd 后的项目目录），另一部分用 `~/runs/` 绝对路径，两套路径并存导致 cron 误判。**\\n\\n- [失败模式] FMVD 信号无效：ρ=0.0825 NO-GO。根因：denoising 空间统计量不映射到 action uncertainty。\\n\\n- [失败模式] CRM correction magnitude 信号无效（2026-05-20）：ρ(K1_corr_mag, K10_var) = 0.1523 NO-GO。**根因：CRM correction magnitude 是常数 (~0.1205)，P25=P50=P75=P90 几乎相同。** CRM 对所有输入产出相同大小的修正向量——修正方向变化但幅度不变。推测因 max_correction_norm=0.2 的 clipping 使得大部分 correction 被截断到相同 norm。K=2 argmin 版本同样无效 (ρ
…[truncated 5391 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 3828
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T14:30:24.651693+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_experiment_plan_with_status,mcp__agent-ml-research__get_project_resource_usage",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_experiment_plan_with_status,mcp__agent-ml-research__get_project_resource_usage",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T14:30:24.702315+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T14:30:27.596547+00:00_

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
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T14:30:44.089084+00:00_

{"result":"{\"success\": true, \"data\": {\"allocated_gpus\": [], \"actually_running_gpus\": [{\"server\": \"bjb1-18228\", \"gpu_id\": \"cuda:0\", \"exp_id\": \"eval-adaptive-k-spatial-p90-seed44\"}, {\"server\": \"bjb1-18228\", \"gpu_id\": \"cuda:1\", \"exp_id\": \"eval-random-selection-spatial-seed42-r2\"}, {\"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:2\", \"exp_id\": \"eval-obs-only-spatial-norm02-seed49\"}, {\"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:3\", \"exp_id\": \"openvla-precompute-k1\"}, {\"server\": \"bjb1-32546\", \"gpu_id\": \"cuda:2\", \"exp_id\": \"eval-perdof-object-norm02-seed49\"}], \"allocated_but_idle\": [], \"registered_but_hw_idle\": [], \"unregistered_but_hw_active\": [], \"running_experiments\": [{\"exp_id\": \"eval-adaptive-k-spatial-p90-seed44\", \"gpus\": [\"cuda:0\"], \"util_avg\": null}, {\"exp_id\": \"eval-random-selection-spatial-seed42-r2\", \"gpus\": [\"cuda:1\"], \"util_avg\": null}, {\"exp_id\": \"eval-obs-only-spatial-norm02-seed49\", \"gpus\": [\"cuda:2\"], \"util_avg\": null}, {\"exp_id\": \"openvla-precompute-k1\", \"gpus\": [\"cuda:3\"], \"util_avg\": null}, {\"exp_id\": \"eval-perdof-object-norm02-seed49\", \"gpus\": [\"cuda:2\"], \"util_avg\": null}], \"worker_pool\": {\"total\": 2, \"gpu_tasks\": 0, \"cpu_tasks\": 2, \"details\": [{\"worker_id\": \"worker_bugfix_plan702-unc-dim-redeploy_20260520T142039\", \"task\": \"bugfix:plan702-unc-dim-redeploy\"}, {\"worker_id\": \"worker_deploy_bjb2-28827-cuda4-fill_20260520T142830\", \"task\": \"deploy:bjb2-28827-cuda4-fill\"}]}, \"summary\": \"分配 0 张, 实际跑 5 张 | Worker 2 (GPU 0 / CPU 2)\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "elapsed_ms": 16492
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T14:30:44.341709+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "analyze:crm-k1-object-plan702",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务：分析 4 个 ANALYZING 状态的实验日志，提取 metrics\n\n你需要 SSH 到服务器读取实验日志，提取成功率和关键指标。\n\n### 实验列表\n\n**服务器 bjb2-28827 上的 4 个实验：**\n\n1. **eval-crm-k1-object-seed42-plan702** — K=1 CRM (ACCG) on LIBERO-Object seed42\n   - 日志: `~/runs/acr-vla-conformal-refinement/eval-crm-k1-object-seed42-plan702.log`\n   - JSON: `/root/acr-vla-conformal-refinement/logs/eval_crm_k1_object_seed42_plan702.json`\n\n2. **eval-crm-k1-object-seed43-plan702** — K=1 CRM (ACCG) on LIBERO-Object seed43\n   - 日志: `~/runs/acr-vla-conformal-refinement/eval-crm-k1-object-seed43-plan702.log`\n   - JSON: `/root/acr-vla-conformal-refinement/logs/eval_crm_k1_object_seed43_plan702.json`\n\n3. **eval-crm-k1-object-seed44-plan702** — K=1 CRM (ACCG) on LIBERO-Object seed44\n   - 日志: `~/runs/acr-vla-conformal-refinement/eval-crm-k1-object-seed44-plan702.log`\n   - JSON: `/root/acr-vla-conformal-refinement/logs/eval_crm_k1_object_seed44_plan702.json`\n\n4. **eval-obs-only-spatial-norm02-seed42** — CRM obs_only K=10 norm02 on LIBERO-Spatial seed42\n   - 日志: `logs/eval-obs-only-spatial-norm02-seed42.log` (在 /root/acr-vla-conformal-refinement/ 下)\n   - 可能也在 `~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-norm02-seed42.log`\n\n### 对每个实验，提取以下信息：\n\n1. **Overall Success Rate (SR)** — 例如 \"Overall success rate: 16/100 = 16.00%\"\n2. **Per-task breakdown** — 每个 task 的 success rate\n3. **是否正常完成** — 看日志最后几行有无 \"Results saved to\" 或 \"Overall success rate\"\n4. **如果有 JSON 输出文件**，读取其中的 metrics\n\n### 上下文\n\n- K=1 CRM 实验的 baseline 是 K=1 VLA-only = 10.8% (Object)\n- K=10 CRM obs_only Object = 16.8% (norm02, n=6)\n- Spatial CRM K=10 obs_only = 34.6% (n=7), VLA-only Spatial = 29.6%\n- eval-obs-only-spatial-norm02-seed42 是 Spatial CRM K=10 的第 8 个 seed\n\n### 输出格式\n\n对每个实验，报告：\n```\nexp_id: xxx\nSR: XX%\nper_task: [task1=X/10, task2=X/10, ...]\nconclusion: success / negative / failed\n备注: ...\n```\n\n最后汇总 K=1 CRM Object 三个 seeds 的均值和标准差。",
  "tool_groups": "['ssh']"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analyze:crm-k1-object-plan702",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务：分析 4 个 ANALYZING 状态的实验日志，提取 metrics\n\n你需要 SSH 到服务器读取实验日志，提取成功率和关键指标。\n\n### 实验列表\n\n**服务器 bjb2-28827 上的 4 个实验：**\n\n1. **eval-crm-k1-object-seed42-plan702** — K=1 CRM (ACCG) on LIBERO-Object seed42\n   - 日志: `~/runs/acr-vla-conformal-refinement/eval-crm-k1-object-seed42-plan702.log`\n   - JSON: `/root/acr-vla-conformal-refinement/logs/eval_crm_k1_object_seed42_plan702.json`\n\n2. **eval-crm-k1-object-seed43-plan702** — K=1 CRM (ACCG) on LIBERO-Object seed43\n   - 日志: `~/runs/acr-vla-conformal-refinement/eval-crm-k1-object-seed43-plan702.log`\n   - JSON: `/root/acr-vla-conformal-refinement/logs/eval_crm_k1_object_seed43_plan702.json`\n\n3. **eval-crm-k1-object-seed44-plan702** — K=1 CRM (ACCG) on LIBERO-Object seed44\n   - 日志: `~/runs/acr-vla-conformal-refinement/eval-crm-k1-object-seed44-plan702.log`\n   - JSON: `/root/acr-vla-conformal-refinement/logs/eval_crm_k1_object_seed44_plan702.json`\n\n4. **eval-obs-only-spatial-norm02-seed42** — CRM obs_only K=10 norm02 on LIBERO-Spatial seed42\n   - 日志: `logs/eval-obs-only-spatial-norm02-seed42.log` (在 /root/acr-vla-conformal-refinement/ 下)\n   - 可能也在 `~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-norm02-seed42.log`\n\n### 对每个实验，提取以下信息：\n\n1. **Overall Success Rate (SR)** — 例如 \"Overall success rate: 16/100 = 16.00%\"\n2. **Per-task breakdown** — 每个 task 的 success rate\n3. **是否正常完成** — 看日志最后几行有无 \"Results saved to\" 或 \"Overall success rate\"\n4. **如果有 JSON 输出文件**，读取其中的 metrics\n\n### 上下文\n\n- K=1 CRM 实验的 baseline 是 K=1 VLA-only = 10.8% (Object)\n- K=10 CRM obs_only Object = 16.8% (norm02, n=6)\n- Spatial CRM K=10 obs_only = 34.6% (n=7), VLA-only Spatial = 29.6%\n- eval-obs-only-spatial-norm02-seed42 是 Spatial CRM K=10 的第 8 个 seed\n\n### 输出格式\n\n对每个实验，报告：\n```\nexp_id: xxx\nSR: XX%\nper_task: [task1=X/10, task2=X/10, ...]\nconclusion: success / negative / failed\n备注: ...\n```\n\n最后汇总 K=1 CRM Object 三个 seeds 的均值和标准差。",
    "tool_groups": "['ssh']"
  }
}
````

</details>

---

### Tool result

_source line 23 · 2026-05-20T14:30:48.058158+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analyze_crm-k1-object-plan702_20260520T143045\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_crm-k1-object-plan702_20260520T143045.log\", \"setup_data\": {}, \"message\": \"Worker worker_analyze_crm-k1-object-plan702_20260520T143045 started. Use get_worker_status('worker_analyze_crm-k1-object-plan702_20260520T143045') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 3716
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-20T14:31:06.902379+00:00_

已派 Worker (analyze:crm-k1-object-plan702) 到 bjb2-28827 读取 4 个 ANALYZING 实验的日志：
- 3× K=1 CRM Object (seed42/43/44) — plan_702
- 1× CRM obs_only Spatial norm02 seed42（滞留 2h+）

Worker 完成后我会更新 registry、刷新 report.md、汇报 Director。

当前资源状态：5 张 GPU RUNNING（bjb1-18228×2, bjb2-28827×2, bjb1-32546×1），3 个 Worker 在跑（含本次分析 Worker）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 25 · 2026-05-20T16:45:43.058476+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: eval-crm-k1-object-seed42-plan702
- project: acr-vla-conformal-refinement
- server: bjb2-28827

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "source": "cron:hook"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-20T16:45:59.227314+00:00_

重复回调——eval-crm-k1-object-seed42-plan702 已在处理中。Worker `worker_analyze_crm-k1-object-plan702_20260520T143045` 正在读取该实验及其他 3 个 ANALYZING 实验的日志。等 Worker 回调后统一更新 registry 和汇报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702"
}
```

</details>

---

## Round 3

2 recorded events

### User

_source line 27 · 2026-05-21T10:54:59.755892+00:00_

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
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-21T10:56:33.035973+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- `evaluate.py` 在 `src/` 子目录下，命令必须是 `python -u src/evaluate.py`（多次因 `python evaluate.py` 导致 EXIT_CODE=2）
- CRM K=1 checkpoint: `/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt`；K=10 checkpoint: `/root/autodl-tmp/checkpoints/crm_best.pt`（不要搞混）
- `submit_training_job` 的 log_path 必须与实际 `tee` 输出路径一致（`~/runs/` vs `logs/` 不匹配会导致 cron 误判 failed）
- `get_project_resource_usage` 显示 allocated_gpus=0，GPU 分配信息不可靠，实际使用 5 张。以 reconcile_crons 和 report.md 为准
- SIGHUP (EXIT_CODE=129) 不等于 failed——tail 日志看 "Results saved to" 行确认实际完成状态

### 2. 🖥️ 基础设施快照
- **服务器**: bjb1-18228 (RTX 4090×?), bjb1-32546 (4090×6), bjb2-28827 (4090×6), bjb2-40593
- **工作目录**: `/root/acr-vla-conformal-refinement`
- **Python**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，pip/python 在 `/root/miniconda3/bin/`
- **HF cache**: `HF_HOME=/root/autodl-tmp/.hf_cache`，eval 时加 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`
- **MUJOCO**: `MUJOCO_GL=egl`（必须，否则 headless 渲染失败）
- **活跃进程**:
  - bjb1-18228: cuda:0 eval-adaptive-k-spatial-p90-seed44 (pid=384503), cuda:1 eval-random-selection-spatial-seed42-r2 (pid=384777)
  - bjb2-28827: cuda:2 eval-obs-only-spatial-norm02-seed49 (pid=357304), cuda:3 openvla-precompute-k1 (pid=365142)
  - bjb1-32546: cuda:2 eval-perdof-object-norm02-seed49 (pid=450375)
  - bjb1-18228 还有: eval-obs-only-spatial-norm02-seed48 (pid=385308), eval-vla-only-spatial-seed48 (pid=385902)

### 3. 📊 当前状态
**刚做完**: 收到 eval-crm-k1-object-seed42-plan702 的 CRON 回调。发现 3 个 K=1 CRM Object seeds (42/43/44) + 1 个 Spatial seed42 共 4 个实验都在 ANALYZING。已 spawn `worker_analyze_crm-k1-object-plan702_20260520T143045` 去 SSH 读日志提取 metrics，**尚未回调**。

**ANALYZING (4)**:
- eval-crm-k1-object-seed42-plan702 — K=1 CRM ACCG Object seed42 (vs VLA-only K=1 baseline 10.8%)
- eval-crm-k1-object-seed43-plan702 — 同上 seed43
- eval-crm-k1-object-seed44-plan702 — 同上 seed44
- eval-obs-only-spatial-norm02-seed42 — CRM K=10 obs_only Spatial seed42（已等 2h+ 未处理）

**RUNNING (5-7)**: 见上方基础设施快照活跃进程列表

**活跃 Workers (3)**:
- worker_analyze_crm-k1-object-plan702 — 正在读日志（等回调）
- worker_bugfix_plan702-unc-dim-redeploy — 修复 plan702 相关 bug
- worker_deploy_bjb2-28827-cuda4-fill — 部署新实验到 bjb2-28827 cuda:4

### 4. 📋 待办（条件触发式）
- **worker_analyze 回调到达** → 用返回的 SR 数据 update_registry(conclusion=success/negative) 4 个实验 → 刷新 report.md → 汇报 Director（K=1 CRM vs K=1 VLA-only 10.8% 对比 + Spatial seed42 是否改变 n=7→n=8 均值）
- **K=1 CRM SR ≈ VLA-only (10.8%)** → negative，说明 CRM correction 在 K=1 下无显著提升，K>1 采样是 CRM 收益的前提。写入 memory.md 作为论文 discussion 素材
- **K=1 CRM SR > 12%** → success，CRM 即使 K=1 也有独立贡献，强化 "correction > selection" narrative
- **eval-adaptive-k-spatial-p90-seed44 完成** → Spatial P90 sweep 3/3 done → 更新 memory.md Adaptive K Cross-Benchmark 表
- **eval-random-selection-spatial-seed42-r2 完成** → Random Selection baseline Spatial 数据点 → plan_600 进度
- **eval-perdof-object-norm02-seed49 完成** → perdof magnitude curve 补充 seed
- **openvla-precompute-k1 完成** → OpenVLA K=1 预计算就绪 → 可提交 OpenVLA eval 实验

### 5. 🎯 战略上下文
**投稿**: CoRL 2026，DDL **2026-05-29**，剩 ~9 天。

**核心方向** (D077): Adaptive K 是论文核心贡献。K=2 L2 distance 作为不确定性信号（ρ=0.9979），P50 阈值 Pareto 最优（Object 15.3%, avg_K=3.8, 省 62% compute）。K=10 分析降为 supporting evidence。

**关键决策链**:
- D078: P50 = Pareto 最优
- D079: CRM magnitude NO-GO (ρ=0.15，常数信号)
- D080: Table 1 修正为 norm02-only n=6 (16.8±1.8%)
- D081: Long OOD 降级 cautious wording (MW-U p=0.061 n.s.)
- D082: evaluate.py 确认 batched inference
- D083: Spatial CRM K=10 修正为 clean n=8 (34.4±1.5%)
- D085: 跨 benchmark 阈值迁移 framing
- D087: 撤回 D086，恢复 OpenVLA 实验线

**易错点**:
1. Spatial CRM 数据曾有 n=7 vs n=8 溯源问题（D083），更新数据时必须核对具体 seed 列表
2. Table 1 曾出现 norm01+norm02 混合（D080 教训），provenance 必须引用具体 registry_id
3. eval-adaptive-k-spatial-p50-seed42 曾被 cron 误判 failed（PID 变更），现在可能已自然完成需要人工检查
4. Random Selection baseline 之前 seed43=9%, seed45=10% 实际已完成但标记 failed，需 tail 日志确认
5. K=1 CRM 实验 (plan_702) 的核心价值是回答 "CRM 在 K=1 下是否有独立贡献"——如果有，强化 correction narrative；如果没有，说明多样性采样是前提条件
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-crm-k1-object-seed42-plan702"
}
```

</details>

---
