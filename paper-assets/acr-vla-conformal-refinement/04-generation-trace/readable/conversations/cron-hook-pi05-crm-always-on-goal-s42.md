# cron hook pi05 crm always on goal s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/cron_hook_pi05-crm-always-on-goal-s42.jsonl`
- **Structured JSON:** [`d7767d71478acf3689c4.json`](../../sessions/d7/d7767d71478acf3689c4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

18 recorded events

### User

_source line 1 · 2026-05-29T10:18:15.237327+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #31。

## 上一轮交接 (task_context)

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

## 可查的历史
前 311 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
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

_source line 2 · 2026-05-29T10:18:25.467313+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__main_agent_post_to_director",
  "max_results": "5"
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
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__main_agent_post_to_director",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-29T10:18:25.568479+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-29T10:18:28.319809+00:00_

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
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
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

_source line 5 · 2026-05-29T10:18:29.022739+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'PREPARING'}",
  "project": "acr-vla-conformal-refinement"
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
    "filters": "{'status': 'PREPARING'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-29T10:18:29.575178+00:00_

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
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
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

_source line 7 · 2026-05-29T10:18:29.575635+00:00_

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

### Tool result

_source line 8 · 2026-05-29T10:18:31.534590+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1804}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 3214
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-29T10:18:34.645906+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1197}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 5623
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-29T10:18:37.708961+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.0231}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 8133
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-29T10:18:37.759630+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 8183
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-29T10:18:40.923436+00:00_

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
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "report.md"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-29T10:18:41.074671+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"# Handover — 2026-05-28\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无运行中实验 — 2026-05-28 全部实验已 kill/cancel）\\n\\n## 待处理\\n（全部 179 项已取消 — 2026-05-28 用户指令全面停机）\\n\\n## 近期结论\\n- **eval-supp-long-adapt-tau025-s44** (negative): Long Adaptive τ=0.25 s44, SR=56%, trigger=4.9%. Below VLA-only baseline (58%). Supplementary seed variance data — 数据已充足。\\n- **pi05-adaptive-goal-s44-backfill** (success): Pi05 Adaptive Conformal on Goal s44. Fills Table 2 gap (only s42/s43 exist). Cross-seed validation for Pi05 Goal adaptive.\\n\\n## 趋势\\n成功 768 / 负向 97 / 失败 130 / 共 1230\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-18228: 1× RTX 4090 空闲（配置说 4 卡但实测仅 1 卡）\\nbjb1-32546: ❌ 连接失败（port 32546 不可达，AutoDL 实例可能已关机/端口变更）\\nbjb2-28827: ❌ 连接失败（port 28827 不可达）\\ncqa1-32758: ❌ 连接失败（port 32758 不可达）\\n\\n## 告警\\n- plan_001-crm-smolvla: 训练失败 — unknown\\n- plan_014-reconvla-baseline: 训练失败 — unknown\\n- eval-smolvla-libero-spatial: 训练失败 — unknown\\n- eval-spatial-reeval-v2: 已被终止 — unknown\\n- precompute-v2-shard0: 已被终止 — unknown\\n- precompute-v2-shard1: 已被终止 — unknown\\n- precompute-v2-shard2: 已被终止 — unknown\\n- eval-spatial-v3-full: 已被终止 — unknown\\n- precompute-v3-shard0: 已被终止 — unknown\\n- precompute-v3-shard1: 已被终止 — unknown\\n- precompute-v3-shard2: 已被终止 — unknown\\n- eval-spatial-v4-full: 已被终止 — unknown\\n- eval-object-v4-full: 已被终止 — unknown\\n- eval-spatial-v5-full: 已被终止 — unknown\\n- crm-train-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v2: 已被终止 — unknown\\n- eval-acr-spatial-v1: 已被终止 — unknown\\n- crm-train-a3-obs-only: 已被终止 — unknown\\n- eval-acr-vla-spatial-v1: 已被终止 — unknown\\n- eval-spatial-v6-full: 已被终止 — unknown\\n- eval-acr-spatial-v2: 已被终止 — unknown\\n- eval-object-v5-full: 已被终止 — unknown\\n- eval-object-v6-full: 已被终止 — unknown\\n- crm-train-a4-s
…[truncated 5000 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-29T10:18:41.126418+00:00_

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

_source line 15 · 2026-05-29T10:18:41.177636+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-28 22:38 UTC | 更新原因: 反映全面停机真实状态，清理过时待办项（DDL 已过、GPU 停机）\\n\\n> 详见 paper_framing.md（D170/D177/D178: K=2 CRM always-on 4/4 harmful + K-matched Table 1）\\n\\n## 核心方向\\n**ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs**。CoRL 2026 DDL **2026-05-28 20:00 北京时间（已过）**。\\n\\n## 当前进展\\n- **论文就绪**：编译通过，8 页正文 + 6 页（refs 2 + appendix 4），零 critical warning\\n- **Table 1 重构完成**：K-matched 3 列（VLA-only K=1 / K=2 CRM always-on / K=2 Adaptive），4/4 suites harmful 叙事升级 ✅\\n- **Table 3 (Pi05) 完成**：4/4 suites degradation-only（含 Long 94.0→77.0, Δ=-17.0pp），seed-matched ✅\\n- **叙事一致性**：4/4 harmful + gating recovery，全文对齐（Abstract/Intro/Experiments/Conclusion）✅\\n- **贡献**：3 条（OpenVLA 从贡献列表移除，保留 §4.5 + Appendix）✅\\n- **全部实验停机**：2026-05-28 用户指令全面停机，1423 实验全部 DONE/killed/cancelled\\n- **提交状态**：待用户确认（DDL 已过，已询问用户）\\n\\n## CRM always-on 最终数据（SmolVLA, K=2, n=3）\\n| Suite | VLA-only (K=1) | CRM always-on (K=2) | Adaptive (K=2) | Δ CRM vs VLA | Δ Adaptive vs VLA |\\n|-------|---------------|--------------------|-----------|----|---|\\n| Spatial | 79.3±0.8 | 78.0±1.7 | 80.8±1.1 | -1.3pp | +1.5pp |\\n| Goal | 83.7±1.3 | 80.0±0.5 | 85.0±1.3 | -3.7pp | +1.3pp |\\n| Object | 77.7±1.3 | 73.0±1.8 | 77.8±2.1 | -4.7pp | +0.1pp |\\n| Long | 58.0±1.5 | 43.2±2.3 | 57.7±1.5 | -14.8pp | -0.3pp |\\n\\n## 近期任务\\n- [x] 收集 Long CRM always-on 3 seeds → 43.2%\\n- [x] Paper Agent Table 1 K-matched 重构 + 叙事 4/4 升级\\n- [x] Figure 1 间距修复 + AI 声明移至附录 + Table 3 浮动调整\\n- [ ] **等待用户确认**：论文是否已提交 CoRL / 是否转投其他会议\\n- [ ] **等待用户确认**：3 台不可达服务器（bjb1-32546, bjb2-28827, cqa1-32758）是否释放\\n\\n## Claim 策略 (D170/D178)\\n- **MC1**: CRM always-on **4/4 suites** 有害 → Adaptive gating 全面恢复（K-matched controlled experiment）\\n- **MC2**: Trigger rate ↔ Δ 单调正相关（cross-suite + within-suite τ-swe
…[truncated 2108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-29T10:18:56.067467+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 0/22 (全面停机) | Worker 0 | 磁盘: 4台服务器均不可达\n\nLoop #31 session-start 完成。\n\n**系统状态**: 0 RUNNING / 0 PREPARING / 0 ANALYZING / 0 cron。全部 4 台服务器关机，系统完全空闲。\n\n**论文状态**: 就绪待提交。编译通过，8+6 页，零 critical warning。\n- Title: \"Knowing When Not to Correct: Adaptive Test-Time Refinement for Frozen Flow-Matching VLAs\"\n- Table 1 K-matched 3 列 ✅ (4/4 suites harmful + Adaptive 恢复)\n- Table 3 Pi05 ✅ (4/4 degradation-only)\n- 总计 1230 实验 (成功 768 / 负向 97 / 失败 130)\n\n**待决**: CoRL DDL (05-28 20:00 北京时间) 已过。等待确认：\n1. 论文是否已提交 CoRL？\n2. 是否转投其他会议？\n3. 3 台不可达服务器是否已释放？",
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
    "text": "[资源] GPU 0/22 (全面停机) | Worker 0 | 磁盘: 4台服务器均不可达\n\nLoop #31 session-start 完成。\n\n**系统状态**: 0 RUNNING / 0 PREPARING / 0 ANALYZING / 0 cron。全部 4 台服务器关机，系统完全空闲。\n\n**论文状态**: 就绪待提交。编译通过，8+6 页，零 critical warning。\n- Title: \"Knowing When Not to Correct: Adaptive Test-Time Refinement for Frozen Flow-Matching VLAs\"\n- Table 1 K-matched 3 列 ✅ (4/4 suites harmful + Adaptive 恢复)\n- Table 3 Pi05 ✅ (4/4 degradation-only)\n- 总计 1230 实验 (成功 768 / 负向 97 / 失败 130)\n\n**待决**: CoRL DDL (05-28 20:00 北京时间) 已过。等待确认：\n1. 论文是否已提交 CoRL？\n2. 是否转投其他会议？\n3. 3 台不可达服务器是否已释放？",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-29T10:18:59.937951+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-goal-s42",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 3870
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-29T10:19:03.916843+00:00_

初始化完成，已向 Director 汇报。

当前状态总结：系统完全空闲（0 实验、0 Worker、0 cron、4台服务器关机）。论文就绪待提交，CoRL DDL 已过。等待 Director 回复确认下一步——是否已提交 CoRL、是否转投其他会议、服务器是否释放。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:pi05-crm-always-on-goal-s42"
}
```

</details>

---
