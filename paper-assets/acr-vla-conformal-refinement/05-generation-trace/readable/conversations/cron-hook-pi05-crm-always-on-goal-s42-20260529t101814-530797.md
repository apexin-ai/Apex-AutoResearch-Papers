# cron hook pi05 crm always on goal s42 20260529T101814 530797

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 2
- **Tool calls:** 9
- **Original source:** `logs/chats/archive/cron_hook_pi05-crm-always-on-goal-s42_20260529T101814_530797.jsonl`
- **Structured JSON:** [`4cda0d22f661e28b9f0d.json`](../../sessions/4c/4cda0d22f661e28b9f0d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

20 recorded events

### User

_source line 1 · 2026-05-28T18:04:42.282442+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #30。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单（22 张跨 4 台服务器）：bjb1-18228, bjb1-32546, bjb2-28827, cqa1-32758 — 不得用白名单外 GPU
- westd-49937 数据系统性偏低 4-5pp（D174/D175: LIBERO assets 版本差异），该服务器 eval 数据不入主表
- CoRL 2026 DDL **2026-05-28 20:00 北京时间**（今天）— 所有操作围绕论文提交
- Table 1 使用 K-matched 3 列设计（VLA-only K=1 / K=2 CRM always-on / K=2 Adaptive）— 不得回退旧格式
- Pi05 Object CRM 数据不入 Table 2 主表，放 Supplement（D171）

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: SmolVLA tau-sweep 实验（tau040-long, tau045-long）
- **bjb1-32546**: crm-always-on-long-s45（cuda:5, PID 423632）
- **bjb2-28827**: smolvla-tau015-spatial-s42-fix（cuda:4）+ tau-sweep 补充实验（tau015/020/030/035-long）
- **cqa1-32758**: Pi05 CRM always-on 实验 — object-s42 (cuda:1, PID 154994), object-s43 (cuda:0, PID 190565), long-s42 (cuda:5, PID 156008)；goal-s42 刚完成进入 ANALYZING
- cqa1 磁盘 `/autodl-pub` 94% 已用 ⚠️（466GB 可用）
- 代码仓库路径: 各服务器 `~/runs/acr-vla-conformal-refinement/`
- 活跃 cron: 11 个（reconcile 刚确认全部健康）

### 3. 📊 当前状态
**刚做完**: Session 初始化（registry 同步 + cron reconcile + 读 report/ROADMAP）。收到 `pi05-crm-always-on-goal-s42` 完成回调，已派 Worker (`worker_analysis_pi05-crm-always-on-goal-s42_20260528T015252`) SSH 读日志提取 metrics 并更新 registry。

**等待中的回调/Worker**:
- Worker `analysis:pi05-crm-always-on-goal-s42` — 正在分析日志，预期分钟级完成
- RUNNING 实验（11 个 cron 监控中）:
  - `pi05-crm-always-on-object-s42` / `object-s43` / `long-s42` — cqa1-32758, Table 2 数据
  - `crm-always-on-long-s45` — bjb1-32546, SmolVLA bonus seed
  - `smolvla-tau040-long-s42` / `tau045-long-s42` — bjb1-18228, tau-sweep
  - `smolvla-tau015/020/030/035-long-s42` — bjb2-28827, tau-sweep 补充
  - `smolvla-tau015-spatial-s42-fix` — bjb2-28827
- Paper Agent 已派单（Table 1 重构 + 叙事 4/4 升级 + 审稿遗留修复）— 状态未确认

**Pi05 CRM always-on 已完成数据**:
- Spatial s42: sr=96%, tr=100%, baseline ~97-98% → Δ≈-1pp ✅
- Goal s42: ANALYZING（Worker 正在提取）

### 4. 📋 待办（条件触发式）
- Worker `analysis:pi05-crm-always-on-goal-s42` 回调 → 读 metrics, 更新 report.md, 汇报 Director（格式: 事实+对比+Table 2 进度）
- `pi05-crm-always-on-object-s42` cron 回调 → 派 Worker 分析 → 对比 Pi05 VLA-only Object baseline（~99.3%）
- `pi05-crm-always-on-object-s43` cron 回调 → 同上，两个 object seed 齐后算均值
- `pi05-crm-always-on-long-s42` cron 回调 → 派 Worker 分析 → 对比 Pi05 VLA-only Long baseline（~95.0%）
- 全部 Pi05 CRM always-on 4 suite 齐 → 汇报 Director 完整 Table 2 CRM always-on 列数据，确认是否 Pi05 也 4/4 harmful
- `crm-always-on-long-s45` 回调 → SmolVLA bonus seed，更新均值
- tau-sweep 系列回调 → 更新 tau-sweep 数据，Appendix sensitivity analysis
- Paper Agent 完成 → 审查 Table 1/叙事一致性

### 5. 🎯 战略上下文
- **核心结论**: CRM always-on 在 SmolVLA 4/4 suites 有害（Object -4.7pp, Spatial -1.3pp, Goal -3.7pp, Long -14.8pp），Adaptive gating 全面恢复。Pi05 Spatial 也确认 harmful (-1pp)，Goal/Object/Long 数据即将到齐
- **决策链**: D170(Long tau-sweep 非单调) → D171(Pi05 Object CRM 放 Supplement) → D172(matched-seed 统计) → D173(Pi05 VLA-only 验证通过) → D174/D175(westd 偏差隔离) → D176(perdof 不可用) → D177(Table 1 K-matched 3 列) → D178(Long -14.8pp 最有力证据)
- **MC1**: 4/4 harmful + Adaptive 恢复 = 论文核心 claim（gating 正确决定何时不干预）
- **MC2**: Trigger rate ↔ Δ 单调正相关（tau-sweep 数据支撑，Long 非单调需 Appendix 诚实报告 D170）
- **MC3**: Cross-VLA 泛化 = Pi05 Table 2 的作用，正在收集中
- **易错点**: Pi05 VLA-only baseline 有多个版本（r3/r4/v2/paired），Table 2 用 r4 版本（n_rollouts=20 标准化）；不要混用不同版本的 sr
- **DDL 今天 20:00 北京时间** — 所有运行中实验让其自然完成，不再部署新实验

## 可查的历史
前 295 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-28T18:04:56.575500+00:00_

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
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
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

_source line 3 · 2026-05-28T18:04:56.626088+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-28T18:05:00.184807+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'RUNNING'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'RUNNING'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-28T18:05:00.689551+00:00_

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
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-28T18:05:01.191204+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "report.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "report.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-28T18:05:01.443075+00:00_

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
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-28T18:05:03.652690+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.4606}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 3467
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-28T18:05:03.703334+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 3013
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-28T18:05:03.754174+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"# Handover — 2026-05-28\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无运行中实验 — 2026-05-28 全部实验已 kill/cancel）\\n\\n## 待处理\\n（全部 179 项已取消 — 2026-05-28 用户指令全面停机）\\n\\n## 近期结论\\n- **eval-supp-long-adapt-tau025-s44** (negative): Long Adaptive τ=0.25 s44, SR=56%, trigger=4.9%. Below VLA-only baseline (58%). Supplementary seed variance data — 数据已充足。\\n- **pi05-adaptive-goal-s44-backfill** (success): Pi05 Adaptive Conformal on Goal s44. Fills Table 2 gap (only s42/s43 exist). Cross-seed validation for Pi05 Goal adaptive.\\n\\n## 趋势\\n成功 768 / 负向 97 / 失败 130 / 共 1230\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-18228: 1× RTX 4090 空闲（配置说 4 卡但实测仅 1 卡）\\nbjb1-32546: ❌ 连接失败（port 32546 不可达，AutoDL 实例可能已关机/端口变更）\\nbjb2-28827: ❌ 连接失败（port 28827 不可达）\\ncqa1-32758: ❌ 连接失败（port 32758 不可达）\\n\\n## 告警\\n- plan_001-crm-smolvla: 训练失败 — unknown\\n- plan_014-reconvla-baseline: 训练失败 — unknown\\n- eval-smolvla-libero-spatial: 训练失败 — unknown\\n- eval-spatial-reeval-v2: 已被终止 — unknown\\n- precompute-v2-shard0: 已被终止 — unknown\\n- precompute-v2-shard1: 已被终止 — unknown\\n- precompute-v2-shard2: 已被终止 — unknown\\n- eval-spatial-v3-full: 已被终止 — unknown\\n- precompute-v3-shard0: 已被终止 — unknown\\n- precompute-v3-shard1: 已被终止 — unknown\\n- precompute-v3-shard2: 已被终止 — unknown\\n- eval-spatial-v4-full: 已被终止 — unknown\\n- eval-object-v4-full: 已被终止 — unknown\\n- eval-spatial-v5-full: 已被终止 — unknown\\n- crm-train-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v2: 已被终止 — unknown\\n- eval-acr-spatial-v1: 已被终止 — unknown\\n- crm-train-a3-obs-only: 已被终止 — unknown\\n- eval-acr-vla-spatial-v1: 已被终止 — unknown\\n- eval-spatial-v6-full: 已被终止 — unknown\\n- eval-acr-spatial-v2: 已被终止 — unknown\\n- eval-object-v5-full: 已被终止 — unknown\\n- eval-object-v6-full: 已被终止 — unknown\\n- crm-train-a4-s
…[truncated 5000 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 2562
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-28T18:05:03.754724+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-28 09:39 UTC | 更新原因: Paper Agent 确认 Table 1 重构+叙事升级完成，论文就绪待提交，ROADMAP 更新任务完成状态\\n\\n> 详见 paper_framing.md（D170/D177/D178: K=2 CRM always-on 4/4 harmful + K-matched Table 1）\\n\\n## 核心方向\\n**ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs**。CoRL 2026 DDL **2026-05-28 20:00 北京时间**。\\n\\n## 当前进展\\n- **论文就绪**：编译通过，8 页正文 + 6 页（refs 2 + appendix 4），零 critical warning\\n- **Table 1 重构完成**：K-matched 3 列（VLA-only K=1 / K=2 CRM always-on / K=2 Adaptive），4/4 suites harmful 叙事升级 ✅\\n- **Table 3 (Pi05) 完成**：4/4 suites degradation-only（含 Long 94.0→77.0, Δ=-17.0pp），seed-matched ✅\\n- **叙事一致性**：4/4 harmful + gating recovery，全文对齐（Abstract/Intro/Experiments/Conclusion）✅\\n- **贡献**：3 条（OpenVLA 从贡献列表移除，保留 §4.5 + Appendix）✅\\n- **Backfill 修复**：M115 根因定位（手动 update_registry 不创建 cron），已全部改用 submit_training_job\\n- **GPU**：22/22 满载，补充实验持续产出\\n\\n## CRM always-on 最终数据（SmolVLA, K=2, n=3）\\n| Suite | VLA-only (K=1) | CRM always-on (K=2) | Adaptive (K=2) | Δ CRM vs VLA | Δ Adaptive vs VLA |\\n|-------|---------------|--------------------|-----------|----|---|\\n| Spatial | 79.3±0.8 | 78.0±1.7 | 80.8±1.1 | -1.3pp | +1.5pp |\\n| Goal | 83.7±1.3 | 80.0±0.5 | 85.0±1.3 | -3.7pp | +1.3pp |\\n| Object | 77.7±1.3 | 73.0±1.8 | 77.8±2.1 | -4.7pp | +0.1pp |\\n| Long | 58.0±1.5 | 43.2±2.3 | 57.7±1.5 | -14.8pp | -0.3pp |\\n\\n## 近期任务\\n- [x] **P0** 收集 Long CRM always-on 3 seeds → 43.2%\\n- [x] **P0** Paper Agent Table 1 K-matched 重构 + 叙事 4/4 升级 ✅\\n- [ ] **P0** 等待用户确认 title + CoRL 提交决定（contingency: 18:00 BJ 默认提交）\\n- [ ] **P1** Pi05 CRM always-on long s43/s44（bjb1-18228 运行中）→ supplementary\\n- [ ] **P1** Bonus seeds + tau-sweep 补充点（22 GPU 持续跑）→ supplementary / camera-ready\\n- [ ] **P2** 最终论文提交 submit_paper_to_review\\n- [ ] **Reviewer** 最终 claim 强度
…[truncated 2374 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 2311
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-28T18:05:22.833067+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'ANALYZING'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'ANALYZING'}"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-28T18:05:23.688401+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__list_workers,mcp__agent-ml-research__main_agent_post_to_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__list_workers,mcp__agent-ml-research__main_agent_post_to_director",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T18:05:26.203008+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.3447}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 3369
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-28T18:05:26.203440+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "ToolSearch",
  "elapsed_ms": 2515
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-28T18:05:29.865890+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "status": "running",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "status": "running",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-28T18:05:30.067155+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-28T18:05:47.908792+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 0/22 | Worker 0 | 全部服务器已关机\n\n**Session #30 状态汇报**\n\n系统完全空闲：\n- 实验：0 RUNNING / 0 ANALYZING（全部已 kill/cancel）\n- Cron：0 活跃\n- Worker：0 运行中\n- 服务器：bjb1-18228 / bjb1-32546 / bjb2-28827 / cqa1-32758 全部连接失败（实例已关机）\n\n**论文状态**：就绪待提交\n- Table 1 K-matched 3 列 ✅（4/4 suites harmful + Adaptive 恢复）\n- Table 3 Pi05 完成 ✅（4/4 degradation-only）\n- 编译通过，8+6 页，零 critical warning\n- Title: \"Knowing When Not to Correct: Adaptive Test-Time Refinement for Frozen Flow-Matching VLAs\"\n\n**待 Director 决策**：CoRL 2026 提交确认（DDL 今天 20:00 北京时间）。ROADMAP 记录 contingency: 18:00 BJ 默认提交。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 0/22 | Worker 0 | 全部服务器已关机\n\n**Session #30 状态汇报**\n\n系统完全空闲：\n- 实验：0 RUNNING / 0 ANALYZING（全部已 kill/cancel）\n- Cron：0 活跃\n- Worker：0 运行中\n- 服务器：bjb1-18228 / bjb1-32546 / bjb2-28827 / cqa1-32758 全部连接失败（实例已关机）\n\n**论文状态**：就绪待提交\n- Table 1 K-matched 3 列 ✅（4/4 suites harmful + Adaptive 恢复）\n- Table 3 Pi05 完成 ✅（4/4 degradation-only）\n- 编译通过，8+6 页，零 critical warning\n- Title: \"Knowing When Not to Correct: Adaptive Test-Time Refinement for Frozen Flow-Matching VLAs\"\n\n**待 Director 决策**：CoRL 2026 提交确认（DDL 今天 20:00 北京时间）。ROADMAP 记录 contingency: 18:00 BJ 默认提交。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T18:05:51.474440+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 3565
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-28T18:05:57.467900+00:00_

Session #30 初始化完成。系统完全空闲，论文就绪，已向 Director 汇报并等待 CoRL 提交确认。DDL 今天 20:00 北京时间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:pi05-crm-always-on-goal-s42"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 21 · 2026-05-29T10:17:38.146583+00:00_

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
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-29T10:18:14.529121+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单 22 张跨 4 台：bjb1-18228, bjb1-32546, bjb2-28827, cqa1-32758 — 不得用白名单外 GPU
- westd-49937 eval 数据不入主表（D174/D175: LIBERO assets 版本差异导致系统性偏低 4-5pp）
- Table 1 使用 K-matched 3 列设计（VLA-only K=1 / K=2 CRM always-on / K=2 Adaptive）— 不得回退旧格式
- Pi05 Object CRM 数据不入 Table 2 主表，放 Supplement（D171）
- CoRL 2026 DDL **2026-05-28 20:00 北京时间** — 已过或即将过

### 2. 🖥️ 基础设施快照
- **全部 4 台服务器已关机**：bjb1-18228 / bjb1-32546 / bjb2-28827 / cqa1-32758 连接失败
- 代码仓库路径（各服务器）: `~/runs/acr-vla-conformal-refinement/`
- 活跃进程：无（0 PID / 0 tmux / 0 cron）
- 系统完全空闲：0 RUNNING / 0 ANALYZING / 0 Worker / 0 Cron

### 3. 📊 当前状态
Session #30 刚完成初始化。Registry 确认 0 RUNNING / 0 ANALYZING。全部实验已在之前 loop 中 kill/cancel，所有服务器实例已关机。

论文状态：**就绪待提交**
- Table 1 K-matched 3 列 ✅（4/4 suites harmful + Adaptive 恢复）
- Table 3 Pi05 完成 ✅（4/4 degradation-only，含 Long 94.0→77.0 Δ=-17.0pp）
- 编译通过，8+6 页，零 critical warning
- Title: "Knowing When Not to Correct: Adaptive Test-Time Refinement for Frozen Flow-Matching VLAs"
- 总计 1230 实验（成功 768 / 负向 97 / 失败 130）

已向 Director 汇报完整状态，等待提交决策。

### 4. 📋 待办
- Director 确认提交 → 执行 CoRL 提交流程
- Director 要求修改 → 派 Worker 改论文（注意服务器已关机，仅本地编辑可行）
- 如需重新启动实验 → 需先确认服务器实例重启 + 端口更新

### 5. 🎯 战略上下文
- **核心结论**: CRM always-on 在 SmolVLA 4/4 suites 有害（Object -4.7pp, Spatial -1.3pp, Goal -3.7pp, Long -14.8pp），Adaptive gating 全面恢复。Pi05 跨模型验证 4/4 degradation-only
- **决策链**: D170→D178（Long -14.8pp 最有力证据）→ D179（Title 锁定）→ D180-D182（Table 2/3 数据确认）→ D183（OpenVLA 贡献移除）→ D184（Title+提交确认）
- **MC1**: 4/4 harmful + Adaptive 恢复 = 论文核心 claim
- **MC2**: Trigger rate ↔ Δ 单调正相关（Long 非单调需 Appendix 诚实报告 D170）
- **MC3**: Cross-VLA 泛化 = Pi05 Table 3
- **易错点**: Pi05 VLA-only baseline 有多个版本（r3/r4/v2/paired），Table 2/3 用 r4 版本（n_rollouts=20 标准化），不要混用
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:pi05-crm-always-on-goal-s42"
}
```

</details>

---
