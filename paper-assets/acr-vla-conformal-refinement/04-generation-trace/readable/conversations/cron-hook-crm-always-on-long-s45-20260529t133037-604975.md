# cron hook crm always on long s45 20260529T133037 604975

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 2
- **Tool calls:** 8
- **Original source:** `logs/chats/archive/cron_hook_crm-always-on-long-s45_20260529T133037_604975.jsonl`
- **Structured JSON:** [`884d3179a55c118dadab.json`](../../sessions/88/884d3179a55c118dadab.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

18 recorded events

### User

_source line 1 · 2026-05-28T21:28:33.552176+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #30。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：22 张，分布在 bjb1-18228, bjb1-32546, bjb2-28827, cqa1-32758 四台服务器
- CoRL 2026 DDL **2026-05-28 20:00 北京时间**（今天！），DDL 前不再部署新实验，让运行中的自然完成
- westd-49937 服务器数据系统性偏低 4-5pp（D174/D175），该服务器结果不可用于论文，已隔离
- Table 1 只用 K-matched 3 列（VLA-only K=1 / K=2 CRM always-on / K=2 Adaptive），禁止混 K 对比
- perdof 数据因训练条件差异不可用于论文对比（D176）

### 2. 🖥️ 基础设施快照
- **bjb1-32546**: 工作目录 /root/autodl-tmp/acr-vla-conformal-refinement, 磁盘 83% 已用
- **bjb2-28827**: 同上路径, 磁盘 69% 已用, cuda:4 跑 smolvla-tau015-spatial-s42-fix (PID 20271)
- **cqa1-32758**: 同上路径, 磁盘 94% ⚠️, cuda:5 跑 pi05-crm-always-on-long-s42 (PID 156008)
- CRM checkpoint: /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt（各服务器同路径）
- 4 台 tau-sweep 实验在 bjb2-28827 运行中：smolvla-tau015-long-s42, tau020-long-s42, tau030-long-s42, tau035-long-s42

### 3. 📊 当前状态
**刚收到 cron 回调**: `crm-always-on-long-s45`（bjb1-32546）进程正常退出，已转 ANALYZING。这是 Long CRM always-on 的第 4 个 seed（bonus seed）。已派 Worker `worker_analyze_crm-always-on-long-s45_20260528T032552` 去读日志提取 metrics，**尚未回调**。

**RUNNING 实验**:
| exp_id | server | GPU | 说明 |
|--------|--------|-----|------|
| pi05-crm-always-on-long-s42 | cqa1-32758 | cuda:5 | Pi05 Table 2 Long suite，最后一个 Pi05 数据点 |
| smolvla-tau015-spatial-s42-fix | bjb2-28827 | cuda:4 | Spatial tau-sweep τ=0.15 |
| smolvla-tau015-long-s42 | bjb2-28827 | — | Long tau-sweep τ=0.15 |
| smolvla-tau020-long-s42 | bjb2-28827 | — | Long tau-sweep τ=0.20 |
| smolvla-tau030-long-s42 | bjb2-28827 | — | Long tau-sweep τ=0.30 |
| smolvla-tau035-long-s42 | bjb2-28827 | — | Long tau-sweep τ=0.35 |

**等待中**:
- Worker 回调：analyze:crm-always-on-long-s45 → 收到后更新 registry + 汇报 Director
- 4 项 QUEUED 实验等 GPU（eval-k2-tau035-spatial-s42, eval-k2-tau025-spatial-s42 等）
- Paper Agent 在跑 Table 1 重构 + 叙事 4/4 升级 + 审稿遗留修复

### 4. 📋 待办
- Worker analyze:crm-always-on-long-s45 回调 → 提取 success_rate → update_registry(conclusion=success/negative) → 更新 report.md → 汇报 Director（s45 与已有 s42/s43/s44 对比，4-seed 均值±std）
- pi05-crm-always-on-long-s42 cron 回调 → 同流程分析 → 这是 Pi05 Table 2 Long 的关键数据，完成后 Table 2 Long 列就齐了
- tau-sweep 系列（5 个）陆续完成 → 每个回调后提取 metrics → 汇总成 tau-sweep sensitivity analysis 数据
- Paper Agent 完成回调 → 检查 Table 1 重构质量 → 送审
- DDL 20:00 前：确认所有论文修改完成，等用户/Director 决定提交

### 5. 🎯 战略上下文
- **核心结论**: CRM always-on 在 4/4 suites 有害（Long 最严重 -14.8pp），Adaptive conformal gating 全面恢复。这是论文最强 claim（MC1）
- **Table 1 数据已锁定**: SmolVLA 4 suites × 3 seeds 齐全。Long: VLA-only 58.0±1.5, CRM-always-on 43.2±2.3, Adaptive 57.7±1.5
- **Table 2 (Pi05)**: Object/Spatial/Goal 已完成，Long (cqa1) 是最后一块。D181 确认 Table 2 只展示 degradation（VLA-only + CRM-always-on 两列）
- **易错点**: crm-always-on-long-s45 是 bonus seed 不进入主 Table 1 统计（主统计用 s42/s43/s44），只用于 robustness 验证。如果 s45 数值与已有 3 seeds 差异大，需要汇报 Director 但不改 Table
- **Title 已锁定(D179)**: "Knowing When Not to Correct: Adaptive Test-Time Correction via Conformal Prediction for Vision-Language-Action Models"

## 可查的历史
前 302 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:crm-always-on-long-s45",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-28T21:28:49.752594+00:00_

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
  "session": "cron:hook:crm-always-on-long-s45",
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

_source line 3 · 2026-05-28T21:28:49.803142+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s45",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-28T21:28:57.980439+00:00_

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
  "session": "cron:hook:crm-always-on-long-s45",
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

_source line 5 · 2026-05-28T21:28:58.499457+00:00_

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
  "session": "cron:hook:crm-always-on-long-s45",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-28T21:28:59.058512+00:00_

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
  "session": "cron:hook:crm-always-on-long-s45",
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

_source line 7 · 2026-05-28T21:28:59.164632+00:00_

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
  "session": "cron:hook:crm-always-on-long-s45",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-28T21:29:01.381444+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.3467}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s45",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 3401
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-28T21:29:01.432526+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s45",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 2933
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-28T21:29:01.433234+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"# Handover — 2026-05-28\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无运行中实验 — 2026-05-28 全部实验已 kill/cancel）\\n\\n## 待处理\\n（全部 179 项已取消 — 2026-05-28 用户指令全面停机）\\n\\n## 近期结论\\n- **eval-supp-long-adapt-tau025-s44** (negative): Long Adaptive τ=0.25 s44, SR=56%, trigger=4.9%. Below VLA-only baseline (58%). Supplementary seed variance data — 数据已充足。\\n- **pi05-adaptive-goal-s44-backfill** (success): Pi05 Adaptive Conformal on Goal s44. Fills Table 2 gap (only s42/s43 exist). Cross-seed validation for Pi05 Goal adaptive.\\n\\n## 趋势\\n成功 768 / 负向 97 / 失败 130 / 共 1230\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-18228: 1× RTX 4090 空闲（配置说 4 卡但实测仅 1 卡）\\nbjb1-32546: ❌ 连接失败（port 32546 不可达，AutoDL 实例可能已关机/端口变更）\\nbjb2-28827: ❌ 连接失败（port 28827 不可达）\\ncqa1-32758: ❌ 连接失败（port 32758 不可达）\\n\\n## 告警\\n- plan_001-crm-smolvla: 训练失败 — unknown\\n- plan_014-reconvla-baseline: 训练失败 — unknown\\n- eval-smolvla-libero-spatial: 训练失败 — unknown\\n- eval-spatial-reeval-v2: 已被终止 — unknown\\n- precompute-v2-shard0: 已被终止 — unknown\\n- precompute-v2-shard1: 已被终止 — unknown\\n- precompute-v2-shard2: 已被终止 — unknown\\n- eval-spatial-v3-full: 已被终止 — unknown\\n- precompute-v3-shard0: 已被终止 — unknown\\n- precompute-v3-shard1: 已被终止 — unknown\\n- precompute-v3-shard2: 已被终止 — unknown\\n- eval-spatial-v4-full: 已被终止 — unknown\\n- eval-object-v4-full: 已被终止 — unknown\\n- eval-spatial-v5-full: 已被终止 — unknown\\n- crm-train-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v2: 已被终止 — unknown\\n- eval-acr-spatial-v1: 已被终止 — unknown\\n- crm-train-a3-obs-only: 已被终止 — unknown\\n- eval-acr-vla-spatial-v1: 已被终止 — unknown\\n- eval-spatial-v6-full: 已被终止 — unknown\\n- eval-acr-spatial-v2: 已被终止 — unknown\\n- eval-object-v5-full: 已被终止 — unknown\\n- eval-object-v6-full: 已被终止 — unknown\\n- crm-train-a4-s
…[truncated 5000 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s45",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 2374
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-28T21:29:01.433782+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-28 09:39 UTC | 更新原因: Paper Agent 确认 Table 1 重构+叙事升级完成，论文就绪待提交，ROADMAP 更新任务完成状态\\n\\n> 详见 paper_framing.md（D170/D177/D178: K=2 CRM always-on 4/4 harmful + K-matched Table 1）\\n\\n## 核心方向\\n**ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs**。CoRL 2026 DDL **2026-05-28 20:00 北京时间**。\\n\\n## 当前进展\\n- **论文就绪**：编译通过，8 页正文 + 6 页（refs 2 + appendix 4），零 critical warning\\n- **Table 1 重构完成**：K-matched 3 列（VLA-only K=1 / K=2 CRM always-on / K=2 Adaptive），4/4 suites harmful 叙事升级 ✅\\n- **Table 3 (Pi05) 完成**：4/4 suites degradation-only（含 Long 94.0→77.0, Δ=-17.0pp），seed-matched ✅\\n- **叙事一致性**：4/4 harmful + gating recovery，全文对齐（Abstract/Intro/Experiments/Conclusion）✅\\n- **贡献**：3 条（OpenVLA 从贡献列表移除，保留 §4.5 + Appendix）✅\\n- **Backfill 修复**：M115 根因定位（手动 update_registry 不创建 cron），已全部改用 submit_training_job\\n- **GPU**：22/22 满载，补充实验持续产出\\n\\n## CRM always-on 最终数据（SmolVLA, K=2, n=3）\\n| Suite | VLA-only (K=1) | CRM always-on (K=2) | Adaptive (K=2) | Δ CRM vs VLA | Δ Adaptive vs VLA |\\n|-------|---------------|--------------------|-----------|----|---|\\n| Spatial | 79.3±0.8 | 78.0±1.7 | 80.8±1.1 | -1.3pp | +1.5pp |\\n| Goal | 83.7±1.3 | 80.0±0.5 | 85.0±1.3 | -3.7pp | +1.3pp |\\n| Object | 77.7±1.3 | 73.0±1.8 | 77.8±2.1 | -4.7pp | +0.1pp |\\n| Long | 58.0±1.5 | 43.2±2.3 | 57.7±1.5 | -14.8pp | -0.3pp |\\n\\n## 近期任务\\n- [x] **P0** 收集 Long CRM always-on 3 seeds → 43.2%\\n- [x] **P0** Paper Agent Table 1 K-matched 重构 + 叙事 4/4 升级 ✅\\n- [ ] **P0** 等待用户确认 title + CoRL 提交决定（contingency: 18:00 BJ 默认提交）\\n- [ ] **P1** Pi05 CRM always-on long s43/s44（bjb1-18228 运行中）→ supplementary\\n- [ ] **P1** Bonus seeds + tau-sweep 补充点（22 GPU 持续跑）→ supplementary / camera-ready\\n- [ ] **P2** 最终论文提交 submit_paper_to_review\\n- [ ] **Reviewer** 最终 claim 强度
…[truncated 2374 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s45",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 2269
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-28T21:29:20.907794+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__list_workers",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:crm-always-on-long-s45",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__list_workers",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-28T21:29:20.958360+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s45",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-28T21:29:23.719306+00:00_

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
  "session": "cron:hook:crm-always-on-long-s45",
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

_source line 15 · 2026-05-28T21:29:23.921133+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s45",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-28T21:29:35.627442+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 0/22 | Worker 0 | 磁盘: 3/4 服务器不可达，bjb1-18228 可达但空闲\n\n**Session #30 启动状态汇报**\n\n项目完全空闲：\n- 0 RUNNING 实验，0 活跃 Worker，0 活跃 Cron\n- bjb1-32546 / bjb2-28827 / cqa1-32758 连接失败（AutoDL 实例可能已关机或端口变更）\n- 仅 bjb1-18228 可达（1×RTX 4090 空闲）\n\n**论文状态**：就绪\n- 编译通过，8+6 页，零 critical warning\n- Table 1 K-matched 重构 ✅ | Table 3 Pi05 ✅ | 叙事一致性 ✅\n- Title 已锁定 (D179)\n\n**CoRL 2026 DDL: 今天 20:00 北京时间**\n\n等待 Director/用户确认提交决定。无需进一步实验操作。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:crm-always-on-long-s45",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 0/22 | Worker 0 | 磁盘: 3/4 服务器不可达，bjb1-18228 可达但空闲\n\n**Session #30 启动状态汇报**\n\n项目完全空闲：\n- 0 RUNNING 实验，0 活跃 Worker，0 活跃 Cron\n- bjb1-32546 / bjb2-28827 / cqa1-32758 连接失败（AutoDL 实例可能已关机或端口变更）\n- 仅 bjb1-18228 可达（1×RTX 4090 空闲）\n\n**论文状态**：就绪\n- 编译通过，8+6 页，零 critical warning\n- Table 1 K-matched 重构 ✅ | Table 3 Pi05 ✅ | 叙事一致性 ✅\n- Title 已锁定 (D179)\n\n**CoRL 2026 DDL: 今天 20:00 北京时间**\n\n等待 Director/用户确认提交决定。无需进一步实验操作。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-28T21:29:39.240786+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s45",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 3613
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-28T21:29:43.141962+00:00_

已完成 session-start 初始化并向 Director 汇报。

当前状态：项目完全空闲，论文就绪，等待 Director/用户确认 CoRL 2026 提交决定（DDL 今天 20:00 北京时间）。无待处理回调或活跃任务。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:crm-always-on-long-s45"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 19 · 2026-05-29T13:30:07.753799+00:00_

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
  "session": "cron:hook:crm-always-on-long-s45",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-29T13:30:37.603328+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单 22 张，分布在 bjb1-18228, bjb1-32546, bjb2-28827, cqa1-32758
- westd-49937 数据系统性偏低 4-5pp（D174/D175），该服务器结果不可用于论文
- Table 1 只用 K-matched 3 列（VLA-only K=1 / K=2 CRM always-on / K=2 Adaptive），禁止混 K 对比
- perdof 数据因训练条件差异不可用于论文对比（D176）
- crm-always-on-long-s45 是 bonus seed，不进入主 Table 1 统计（主统计用 s42/s43/s44）
- Title 已锁定(D179): "Knowing When Not to Correct: Adaptive Test-Time Correction via Conformal Prediction for Vision-Language-Action Models"
- CoRL 2026 DDL **2026-05-28 20:00 北京时间**（已过或即将到达）

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: 可达，1×RTX 4090 空闲，工作目录 /root/autodl-tmp/acr-vla-conformal-refinement
- **bjb1-32546**: ❌ 连接失败（port 32546 不可达，AutoDL 实例可能已关机/端口变更）
- **bjb2-28827**: ❌ 连接失败（port 28827 不可达）
- **cqa1-32758**: ❌ 连接失败（port 32758 不可达）
- CRM checkpoint: /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt（各服务器同路径）
- 活跃进程：无（0 RUNNING 实验，0 活跃 Worker，0 活跃 Cron）

### 3. 📊 当前状态
项目完全空闲。所有实验已 kill/cancel（2026-05-28 用户指令全面停机）。论文就绪：编译通过，8+6 页，零 critical warning。Table 1 K-matched 重构 ✅，Table 3 Pi05 ✅，叙事一致性 ✅。

Registry: 0 RUNNING / 0 PREPARING。总计 1230 实验（成功 768 / 负向 97 / 失败 130）。

已向 Director 发送 Session #30 启动汇报，等待 Director/用户确认提交决定。无待处理 Worker 回调或 Cron。

### 4. 📋 待办
- Director 回复提交决定 → 执行论文提交流程（submit_paper_to_review）
- 用户要求重新连接服务器（端口变更后）→ 更新 SSH config → 重新探测环境
- 如需补充实验（camera-ready 阶段）→ 先确认服务器可达性 → 恢复 cron 监控 → 重新提交
- DDL 已过且未提交 → 等 Director 指示下一步（转投其他会议 / camera-ready 准备）

### 5. 🎯 战略上下文
- **核心结论**: CRM always-on 在 4/4 suites 有害（Long 最严重 -14.8pp），Adaptive conformal gating 全面恢复。这是论文最强 claim（MC1）
- **数据已锁定**: SmolVLA 4 suites × 3 seeds 齐全。Long: VLA-only 58.0±1.5, CRM-always-on 43.2±2.3, Adaptive 57.7±1.5
- **Table 2 (Pi05)**: 4/4 suites degradation-only（VLA-only + CRM-always-on 两列），Long 94.0→77.0 Δ=-17.0pp
- **Claim 策略**: MC1=4/4 harmful + recovery, MC2=trigger rate↔Δ 单调正相关, MC3=cross-VLA 泛化
- **易错点**: 3/4 服务器不可达，如需重新操作必须先让用户去 AutoDL 控制台查新端口。不要反复重试连接
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:crm-always-on-long-s45"
}
```

</details>

---
