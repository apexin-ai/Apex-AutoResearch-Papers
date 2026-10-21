# cron hook crm always on long s45

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/cron_hook_crm-always-on-long-s45.jsonl`
- **Structured JSON:** [`34dd97925303903b2450.json`](../../sessions/34/34dd97925303903b2450.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

16 recorded events

### User

_source line 1 · 2026-05-29T13:30:38.026804+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #31。

## 上一轮交接 (task_context)

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

## 可查的历史
前 317 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
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

_source line 2 · 2026-05-29T13:30:48.048511+00:00_

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
  "session": "cron:hook:crm-always-on-long-s45",
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

_source line 3 · 2026-05-29T13:30:48.249609+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s45",
  "tool": "ToolSearch",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-29T13:30:52.466431+00:00_

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
  "session": "cron:hook:crm-always-on-long-s45",
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

_source line 5 · 2026-05-29T13:30:53.370116+00:00_

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
  "session": "cron:hook:crm-always-on-long-s45",
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

_source line 6 · 2026-05-29T13:30:53.370568+00:00_

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

_source line 7 · 2026-05-29T13:30:53.924007+00:00_

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

_source line 8 · 2026-05-29T13:30:54.179850+00:00_

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

_source line 9 · 2026-05-29T13:30:56.813484+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.3228}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s45",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 4347
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-29T13:30:59.823859+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.0161}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s45",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 6453
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-29T13:30:59.924617+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s45",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 6554
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-29T13:30:59.925186+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"# Handover — 2026-05-28\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无运行中实验 — 2026-05-28 全部实验已 kill/cancel）\\n\\n## 待处理\\n（全部 179 项已取消 — 2026-05-28 用户指令全面停机）\\n\\n## 近期结论\\n- **eval-supp-long-adapt-tau025-s44** (negative): Long Adaptive τ=0.25 s44, SR=56%, trigger=4.9%. Below VLA-only baseline (58%). Supplementary seed variance data — 数据已充足。\\n- **pi05-adaptive-goal-s44-backfill** (success): Pi05 Adaptive Conformal on Goal s44. Fills Table 2 gap (only s42/s43 exist). Cross-seed validation for Pi05 Goal adaptive.\\n\\n## 趋势\\n成功 768 / 负向 97 / 失败 130 / 共 1230\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-18228: 1× RTX 4090 空闲（配置说 4 卡但实测仅 1 卡）\\nbjb1-32546: ❌ 连接失败（port 32546 不可达，AutoDL 实例可能已关机/端口变更）\\nbjb2-28827: ❌ 连接失败（port 28827 不可达）\\ncqa1-32758: ❌ 连接失败（port 32758 不可达）\\n\\n## 告警\\n- plan_001-crm-smolvla: 训练失败 — unknown\\n- plan_014-reconvla-baseline: 训练失败 — unknown\\n- eval-smolvla-libero-spatial: 训练失败 — unknown\\n- eval-spatial-reeval-v2: 已被终止 — unknown\\n- precompute-v2-shard0: 已被终止 — unknown\\n- precompute-v2-shard1: 已被终止 — unknown\\n- precompute-v2-shard2: 已被终止 — unknown\\n- eval-spatial-v3-full: 已被终止 — unknown\\n- precompute-v3-shard0: 已被终止 — unknown\\n- precompute-v3-shard1: 已被终止 — unknown\\n- precompute-v3-shard2: 已被终止 — unknown\\n- eval-spatial-v4-full: 已被终止 — unknown\\n- eval-object-v4-full: 已被终止 — unknown\\n- eval-spatial-v5-full: 已被终止 — unknown\\n- crm-train-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v2: 已被终止 — unknown\\n- eval-acr-spatial-v1: 已被终止 — unknown\\n- crm-train-a3-obs-only: 已被终止 — unknown\\n- eval-acr-vla-spatial-v1: 已被终止 — unknown\\n- eval-spatial-v6-full: 已被终止 — unknown\\n- eval-acr-spatial-v2: 已被终止 — unknown\\n- eval-object-v5-full: 已被终止 — unknown\\n- eval-object-v6-full: 已被终止 — unknown\\n- crm-train-a4-s
…[truncated 5000 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s45",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6001
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-29T13:30:59.925586+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-28 22:38 UTC | 更新原因: 反映全面停机真实状态，清理过时待办项（DDL 已过、GPU 停机）\\n\\n> 详见 paper_framing.md（D170/D177/D178: K=2 CRM always-on 4/4 harmful + K-matched Table 1）\\n\\n## 核心方向\\n**ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs**。CoRL 2026 DDL **2026-05-28 20:00 北京时间（已过）**。\\n\\n## 当前进展\\n- **论文就绪**：编译通过，8 页正文 + 6 页（refs 2 + appendix 4），零 critical warning\\n- **Table 1 重构完成**：K-matched 3 列（VLA-only K=1 / K=2 CRM always-on / K=2 Adaptive），4/4 suites harmful 叙事升级 ✅\\n- **Table 3 (Pi05) 完成**：4/4 suites degradation-only（含 Long 94.0→77.0, Δ=-17.0pp），seed-matched ✅\\n- **叙事一致性**：4/4 harmful + gating recovery，全文对齐（Abstract/Intro/Experiments/Conclusion）✅\\n- **贡献**：3 条（OpenVLA 从贡献列表移除，保留 §4.5 + Appendix）✅\\n- **全部实验停机**：2026-05-28 用户指令全面停机，1423 实验全部 DONE/killed/cancelled\\n- **提交状态**：待用户确认（DDL 已过，已询问用户）\\n\\n## CRM always-on 最终数据（SmolVLA, K=2, n=3）\\n| Suite | VLA-only (K=1) | CRM always-on (K=2) | Adaptive (K=2) | Δ CRM vs VLA | Δ Adaptive vs VLA |\\n|-------|---------------|--------------------|-----------|----|---|\\n| Spatial | 79.3±0.8 | 78.0±1.7 | 80.8±1.1 | -1.3pp | +1.5pp |\\n| Goal | 83.7±1.3 | 80.0±0.5 | 85.0±1.3 | -3.7pp | +1.3pp |\\n| Object | 77.7±1.3 | 73.0±1.8 | 77.8±2.1 | -4.7pp | +0.1pp |\\n| Long | 58.0±1.5 | 43.2±2.3 | 57.7±1.5 | -14.8pp | -0.3pp |\\n\\n## 近期任务\\n- [x] 收集 Long CRM always-on 3 seeds → 43.2%\\n- [x] Paper Agent Table 1 K-matched 重构 + 叙事 4/4 升级\\n- [x] Figure 1 间距修复 + AI 声明移至附录 + Table 3 浮动调整\\n- [ ] **等待用户确认**：论文是否已提交 CoRL / 是否转投其他会议\\n- [ ] **等待用户确认**：3 台不可达服务器（bjb1-32546, bjb2-28827, cqa1-32758）是否释放\\n\\n## Claim 策略 (D170/D178)\\n- **MC1**: CRM always-on **4/4 suites** 有害 → Adaptive gating 全面恢复（K-matched controlled experiment）\\n- **MC2**: Trigger rate ↔ Δ 单调正相关（cross-suite + within-suite τ-swe
…[truncated 2108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s45",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 5745
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-29T13:31:16.893149+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 0/22 | Worker 0 | 磁盘: bjb1-18228 未检查（其余 3 台不可达）\n\nSession #31 启动汇报：\n- Registry 确认：0 RUNNING / 0 PREPARING，共 1230 实验（成功 768 / 负向 97 / 失败 130）\n- Cron：0 活跃，reconcile 无变更\n- 论文状态：就绪（编译通过，8+6 页，零 critical warning）\n- 服务器：bjb1-18228 可达但空闲，其余 3 台（bjb1-32546, bjb2-28827, cqa1-32758）不可达\n- CoRL DDL 2026-05-28 20:00 北京时间已过\n\n待 Director 决策：\n1. 论文是否已提交 CoRL？若未提交，是否转投其他会议？\n2. 3 台不可达服务器是否释放？\n3. 下一步方向（camera-ready / 转投 / 新实验）？",
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
    "text": "[资源] GPU 0/22 | Worker 0 | 磁盘: bjb1-18228 未检查（其余 3 台不可达）\n\nSession #31 启动汇报：\n- Registry 确认：0 RUNNING / 0 PREPARING，共 1230 实验（成功 768 / 负向 97 / 失败 130）\n- Cron：0 活跃，reconcile 无变更\n- 论文状态：就绪（编译通过，8+6 页，零 critical warning）\n- 服务器：bjb1-18228 可达但空闲，其余 3 台（bjb1-32546, bjb2-28827, cqa1-32758）不可达\n- CoRL DDL 2026-05-28 20:00 北京时间已过\n\n待 Director 决策：\n1. 论文是否已提交 CoRL？若未提交，是否转投其他会议？\n2. 3 台不可达服务器是否释放？\n3. 下一步方向（camera-ready / 转投 / 新实验）？",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-29T13:31:20.157133+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s45",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 3263
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-29T13:31:23.268582+00:00_

Session #31 初始化完成。

状态总结：项目完全空闲，CoRL DDL 已过，论文就绪待提交决定。已向 Director 汇报，等待指示下一步（提交确认 / 转投 / 新方向）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:crm-always-on-long-s45"
}
```

</details>

---
