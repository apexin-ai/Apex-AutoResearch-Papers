# cron hook eval supp reconvla k2 spatial s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/cron_hook_eval-supp-reconvla-k2-spatial-s42.jsonl`
- **Structured JSON:** [`d69919bbddcd8abe19f6.json`](../../sessions/d6/d69919bbddcd8abe19f6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

14 recorded events

### User

_source line 1 · 2026-05-24T00:55:32.324015+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #26。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单按服务器：bjb1-32546 cuda:0-5, bjb2-28827 cuda:0-5, cqa1-32758 cuda:0-5, bjb1-18228（precompute 专用）, bjb2-40593（precompute 专用）
- SmolVLA precompute 数据在 `/root/autodl-tmp/crm_cache_v5/`（960D obs-only 格式），**不是** π0.5 数据
- CRM checkpoint 路径：SmolVLA 3-suite = `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt`；4-suite 正在训练 (`train-crm-unified-4suite-r6`)
- evaluate.py K=2 mean 模式需要 `--mode vla_only --K 2`（不是 reconvla），已修复部署
- Adaptive CRM τ 值必须精确：spatial/goal/long 用 τ=0.25，object 用校正后的 τ（之前 τ=0.074855 是错误值导致 negative）
- π0.5 precompute 是 best-effort 背景任务（D126），不阻塞 SmolVLA 主线

### 2. 🖥️ 基础设施快照
- **bjb1-32546**（6×RTX 4090D）：`/root/acr-vla-conformal-refinement/`，conda base `/root/miniconda3/bin/python`
  - 活跃：train-crm-unified-4suite-r6 (PID 668372, cuda:3)，eval-supp-adapt-tau025-spatial-s44 (PID 742219, cuda:1)，eval-supp-crm-norm005-spatial-s44 (PID 759205, cuda:5)
- **bjb2-28827**（6×GPU）：同路径结构
  - 活跃：eval-supp-goal-adapt-tau025-s42 (cuda:2), eval-supp-k2mean-spatial/object-s42 (cuda:4/1), eval-supp-goal-reconvla-s42 (cuda:3), eval-goal-vla-only-wrapper-s42 (cuda:5), eval-supp-obj-adapt-tau025-s42 (cuda:0)
- **cqa1-32758**（6×RTX 4090D，新增）：同路径结构
  - 活跃：eval-supp-reconvla-spatial-s43 (cuda:1), eval-supp-reconvla-spatial-s44 (cuda:3), eval-supp-k2mean-spatial/object/goal-s43 (cuda:0/2/4), eval-supp-goal-reconvla-s43 (cuda:5)
- **bjb1-18228 / bjb2-40593**：precompute π0.5 专用（precompute-pi05-object/spatial/goal/long-2048-r2 运行中）
- W&B：数据可用（cron 提示 W&B data available）
- 磁盘警告：bjb2-40593 根分区 90%⚠️，cqa1-32758 autodl-pub 96%⚠️

### 3. 📊 当前状态
**刚做完**：session-start 初始化，reconcile crons（21 个），派出 Worker 分析 `eval-supp-reconvla-k2-spatial-s42` 和 `eval-supp-adapt-tau025-spatial-s43` 的日志。

**ANALYZING（待处理）**：
- `eval-supp-reconvla-k2-spatial-s42`：K=2 argmin on Spatial s42，验证 centroid bug 导致 K=2≈K=1（预期 ~78.5%）
- `eval-supp-adapt-tau025-spatial-s43`：Adaptive τ=0.25 Spatial s43，multi-seed 验证（reconcile 刚转 ANALYZING）

**RUNNING（15个）**：全部是 SmolVLA 补充实验矩阵——K=2 mean / Reconvla / Adaptive / CRM-norm005 的多 seed 跑法，覆盖 Spatial/Object/Goal suites。

**等待中**：
- Worker `worker_analyze_eval-supp-reconvla-k2-spatial-s42_20260523T083410` 正在读日志提取 SR，回调后更新 registry + 汇报 Director
- Worker `worker_deploy_bjb2-40593-fix-redeploy-k2mean` 仍在运行
- `train-crm-unified-4suite-r6`（4-suite CRM 训练）完成后才能解锁 Long suite 全套实验

### 4. 📋 待办（条件触发式）
- **Worker 分析回调到达** → 用结果更新 registry（conclusion + metrics），刷新 report.md，汇报 Director（如 K=2 argmin ≈ 78.5% 则 success 确认 CRM 是改进来源）
- **eval-supp-adapt-tau025-spatial-s43 结果就绪** → 与 s42(82.0%) 对比算 multi-seed mean±std，更新 ROADMAP Spatial 行
- **所有 Spatial 3-seed 完成**（s42+s43+s44）→ 计算 VLA-only/Adaptive/CRM/Reconvla/K2mean 各方法的 3-seed mean±std 汇总
- **train-crm-unified-4suite-r6 完成** → 立即铺 Long suite 全套 5 个方法的 eval
- **cqa1-32758 上的 6 个 eval 完成** → 收集 s43 seed 结果，与 s42 对比
- **bjb2-28827 上的 6 个 eval 完成** → 收集 Object/Goal 各方法 s42 结果，更新矩阵
- **π0.5 precompute 完成** → 开始 π0.5 CRM 训练 + eval（best-effort，DDL 前能跑多少跑多少）

### 5. 🎯 战略上下文
- **DDL: CoRL 2026 = 2026-05-29**，≤5 天，所有实验必须在此前完成
- **核心 story**：ACR-VLA = Adaptive Conformal Refinement for frozen flow-matching VLAs。Adaptive CRM τ=0.25 是明星方法（Spatial 82% vs VLA-only 78.5%，仅 19.4% trigger rate）
- **当前瓶颈**：SmolVLA 实验矩阵大量 seed 在跑，Long suite 被 4-suite CRM 训练阻塞
- **关键决策链**：D128(overcorrection 是 magnitude 问题不是方向) → D127(CRM always-correct negative → 3方向并行改进) → D126(π0.5 precompute 降级 best-effort) → D124(放弃第三模型 OFT，锁定 2-model paper)
- **易错点**：
  - Object suite 的 adaptive τ 值与 spatial/goal 不同，之前用错 τ=0.074855 导致 negative
  - K=2 mean 用 `--mode vla_only --K 2`，K=2 argmin 用 `--mode reconvla --K 2`——两个是不同的 baseline，别搞混
  - `eval-supp-goal-crm005-s42` 被标为 success 但实际是 cron 误判（进程还在跑，只完成 ~35%），需要重新评估
  - cqa1-32758 磁盘 96% 使用率，提交新实验前先检查空间

## 可查的历史
前 260 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-24T00:55:42.319170+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-24T00:55:42.319596+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-24T00:55:46.489492+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T00:55:46.939302+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'ANALYZING'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'ANALYZING'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-24T00:55:47.434475+00:00_

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
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T00:55:47.922844+00:00_

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
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
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

_source line 8 · 2026-05-24T00:55:48.090585+00:00_

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
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-24T00:55:53.157693+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-spatial-reconvla-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T00:52:50.566Z\", \"updated_at\": \"2026-05-24T00:53:19.282Z\", \"hypothesis\": \"Reconvla K=10 argmin on Spatial suite seed46. Fifth seed extending Spatial Reconvla coverage. 3-seed mean ~80%. Completes 5-seed variance analysis.\"}, \"eval-supp-spatial-vla-only-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T00:34:46.225Z\", \"updated_at\": \"2026-05-24T00:35:25.376Z\", \"hypothesis\": \"Spatial VLA-only baseline seed46. Fifth seed for Spatial VLA-only variance analysis. 3-seed mean 78.7%±0.3%.\"}, \"eval-supp-long-vla-only-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T00:32:53.028Z\", \"updated_at\": \"2026-05-24T00:33:27.913Z\", \"hypothesis\": \"Long VLA-only baseline seed46. Fifth seed for Long VLA-only variance analysis. 3-seed mean 58.0%±1.5%.\"}, \"eval-supp-spatial-crm-norm005-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T00:22:31.743Z\", \"updated_at\": \"2026-05-24T00:23:19.360Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Spatial suite seed46. Fifth seed for Spatial CRM variance analysis. 3-seed mean ~79.8%.\"}, \"eval-supp-spatial-adapt-tau025-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-23T23:45:59.585Z\", \"updated_at\": \"2026-05-23T23:46:45.330Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed46. Fifth seed extending Spatial Adaptive for variance analysis. 3-seed mean 80.8%±1.1%.\"}, \"eval-supp-spatial-k2mean-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-23T23:41:52.628Z\", \"updated_at\": \"2026-05-23T23:44:39.106Z\", \"hypothesis\": \"K=2 mean baseline on Spatial suite seed46. Fifth seed extending Spatial K2mean coverage for variance analysis.\"}, \"eval-supp-spatial-adapt-tau025-s45-r3\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-23T23:42:31.834Z\", \"updated_at\": \"2026-05-23T23:43:42.064Z\", \"h
…[truncated 2941 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 6668
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T00:56:03.942653+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.6272}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 17003
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-24T01:01:51.864092+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 22, \"results\": [{\"exp_id\": \"precompute-pi05-object-2048-r2\", \"success\": true, \"actions\": [\"Job still running (pid=113456)\"]}, {\"exp_id\": \"precompute-pi05-spatial-2048-r2\", \"success\": true, \"actions\": [\"Job still running (pid=113796)\"]}, {\"exp_id\": \"precompute-pi05-goal-2048-r2\", \"success\": true, \"actions\": [\"Job still running (pid=114159)\"]}, {\"exp_id\": \"precompute-pi05-long-2048-r2\", \"success\": true, \"actions\": [\"Job still running (pid=114507)\"]}, {\"exp_id\": \"eval-supp-long-crm-norm005-s45\", \"success\": true, \"actions\": [\"Stale cron removed (registry status=DONE)\"]}, {\"exp_id\": \"eval-supp-long-reconvla-s45\", \"success\": true, \"actions\": [\"Process gone, no sentinel, no W&B — escalating to agent (miss 2/5)\"]}, {\"exp_id\": \"eval-supp-long-k2mean-s45\", \"success\": true, \"actions\": [\"Job still running (pid=924226)\"]}, {\"exp_id\": \"eval-supp-spatial-adapt-tau025-s45\", \"success\": true, \"actions\": [\"Job still running (pid=502816)\"]}, {\"exp_id\": \"eval-supp-goal-adapt-tau025-s46\", \"success\": true, \"actions\": [\"Job still running (pid=eval-goal-adapt-s46)\"]}, {\"exp_id\": \"eval-supp-goal-crm-norm005-s46\", \"success\": true, \"actions\": [\"Job still running (pid=eval-goal-crm-s46)\"]}, {\"exp_id\": \"eval-supp-goal-reconvla-s46\", \"success\": true, \"actions\": [\"Job still running (pid=eval-supp-goal-reconvla-s46)\"]}, {\"exp_id\": \"eval-supp-goal-k2mean-s46\", \"success\": true, \"actions\": [\"Job still running (pid=eval-goal-k2mean-s46)\"]}, {\"exp_id\": \"eval-supp-goal-vla-only-s46\", \"success\": true, \"actions\": [\"Job still running (pid=eval-supp-goal-vla-only-s46)\"]}, {\"exp_id\": \"eval-supp-reconvla-obj-s45\", \"success\": true, \"actions\": [\"Process gone, no sentinel, no W&B — escalating to agent (miss 1/5)\"]}, {\"exp_id\": \"eval-supp-spatial-k2mean-s45\", \"success\": true, \"actions\": [\"Job still running (p
…[truncated 937 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 364429
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T01:01:51.915125+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"# Handover — 2026-05-24\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval-supp-spatial-reconvla-s46 | Reconvla K=10 argmin on Spatial suite seed46. Fifth seed extending Spatial Reconvla coverage. 3-seed mean ~80%. Completes 5-seed variance analysis. | — | — | — |\\n\\n## 待处理\\n- eval-supp-long-adapt-tau025-s46: Adaptive CRM tau=0.25 on Long suite seed46. Fifth seed for Long Adaptive variance analysis. s42-s45 mean ~59.5%.（等待人工审批）\\n- eval-supp-long-reconvla-s46: Reconvla K=10 argmin on Long suite seed46. Fifth seed for Long Reconvla variance analysis. s42-s45 mean ~57.8%.（等待人工审批）\\n- …另有 99 项\\n\\n## 近期结论\\n- **eval-supp-long-crm-norm005-s45** (success): CRM norm=0.05 always-on on Long suite seed45. Fourth seed for Long CRM validation.\\n\\n## 趋势\\n成功 427 / 负向 72 / 失败 85 / 共 736\\nSR: 0.605 ↑（近 3 次 success）\\nsuccesses: 121 ↑（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-18228: 无 GPU 信息\\nbjb1-32546: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\\nbjb2-28827: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\\nbjb2-40593: 无 GPU 信息\\ncqa1-32758: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\\n\\n## 告警\\n- plan_001-crm-smolvla: 训练失败 — unknown\\n- plan_014-reconvla-baseline: 训练失败 — unknown\\n- eval-smolvla-libero-spatial: 训练失败 — unknown\\n- eval-spatial-reeval-v2: 已被终止 — unknown\\n- precompute-v2-shard0: 已被终止 — unknown\\n- precompute-v2-shard1: 已被终止 — unknown\\n- precompute-v2-shard2: 已被终止 — unknown\\n- eval-spatial-v3-full: 已被终止 — unknown\\n- precompute-v3-shard0: 已被终止 — unknown\\n- precompute-v3-shard1: 已被终止 — unknown\\n- precompute-v3-shard2: 已被终止 — unknown\\n- eval-spatial-v4-full: 已被终止 — unknown\\n- eval-object-v4-full: 已被终止 — unknown\\n- eval-spatial-v5-full: 已被终止 — unknow
…[truncated 5270 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 363992
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-24T01:01:51.915815+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-23 22:41 UTC | 更新原因: Fix Reviewer-flagged range inconsistency (+1.8→+1.9pp to match paper). Update GPU status (4 idle). π0.5 timeline. paper_framing.md D134 note added.\\n\\n> 详见 paper_framing.md（已标注 D134 supersedes D129）\\n\\n## 核心方向\\n**ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs**。CoRL 2026 DDL **2026-05-29**（≤5天）。\\n\\n## 核心叙事 (D134) — 全 4 suites 3-seed 验证 ✅\\n**\\\"Gating correctly modulates intervention intensity — improves where VLA uncertain, preserves where VLA confident\\\"**\\n- Adaptive ≥ CRM on ALL 4 suites (+1.0 to +1.9pp on 3-seed mean) ✅\\n- Trigger_rate > 7%: Adaptive > VLA-only (Spatial +2.1pp, Goal +1.3pp) ✅\\n- Trigger_rate < 5%: Adaptive ≈ VLA-only within noise (Object Δ=+0.1pp, Long Δ=-0.3pp = 0.22σ) ✅\\n- CRM always-on harmful on 2/4 suites (Object -1.2pp, Long -2.2pp) ✅\\n\\n## 跨 suite 完整结果（Table 1 — 3-seed final）\\n| Suite | VLA-only | CRM | Adaptive | Δ(Adapt-VLA) | Δ(Adapt-CRM) |\\n|-------|---------|-----|----------|-------------|--------------|\\n| Spatial | 78.7±0.3(3s) | 79.8±1.3(3s) | 80.8±1.1(3s) | **+2.1pp** | +1.0pp |\\n| Goal | 83.7±1.3(3s) | 83.7±1.8(3s) | 85.0±1.3(3s) | **+1.3pp** | +1.3pp |\\n| Object | 77.7±1.3(5s) | 76.5±2.3(3s) | 77.8±2.1(5s) | +0.1pp | +1.3pp |\\n| Long | 58.0±1.5(3s) | 55.8±1.2(3s) | 57.7±1.5(3s) | -0.3pp | **+1.9pp** |\\n\\n## τ-sweep ablation (D132) ✅ 完成\\n倒 U 型曲线，最优区间 τ∈[0.15, 0.25]。Appendix §B 就绪。\\n\\n## Trigger-rate vs Improvement Figure ✅ 完成\\n4 suite scatter plot。清晰二分模式：trigger>7% = improvement, trigger<5% = baseline preserved。\\n\\n## 论文文本状态\\n- experiments.tex Table 1 + 正文：数值已 Reviewer 验证 PASS ✅\\n- Object CRM \\\"-1.3pp\\\" → \\\"-1.2pp\\\" 已修正（与表值一致）✅\\n- paper_framing.md：D134 header 已更新 ✅\\n\\n## GPU 状态（当前）\\n19/23 在跑 + 4 空闲待部署：\\n
…[truncated 2531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 363825
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-24T01:01:52.389353+00:00_

You've hit your limit · resets 3pm (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-supp-reconvla-k2-spatial-s42"
}
```

</details>

---
