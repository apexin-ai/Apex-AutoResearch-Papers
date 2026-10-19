# cron hook pi05 crm always on spatial s42 20260529T100336 487851

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 2
- **Tool calls:** 7
- **Original source:** `logs/chats/archive/cron_hook_pi05-crm-always-on-spatial-s42_20260529T100336_487851.jsonl`
- **Structured JSON:** [`76aecfe3ec44053a515c.json`](../../sessions/76/76aecfe3ec44053a515c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

16 recorded events

### User

_source line 1 · 2026-05-28T17:42:57.483796+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #30。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- CoRL 2026 DDL **2026-05-28 20:00 北京时间**（今天）。ROADMAP 明确"DDL 前不再部署新实验，让运行中的自然完成"
- cqa1-32758 cuda:2 刚释放（pi05-crm-always-on-spatial-s42 完成），**不安排新任务**
- westd-49937 服务器数据系统性偏低 4-5pp（D174/D175），该服务器结果不入主表
- Pi05 Object CRM 数据不入 Table 2 主表，放 Supplement（D171）
- memory.md 被我误覆盖——原文件 Birth 2026-05-26，内容已丢失，只剩我刚写的 Pi05 CRM always-on 追踪段。下一个"你"注意不要用 save_project_file 全量覆盖，应先读再追加

### 2. 🖥️ 基础设施快照
- **cqa1-32758**: Pi05 实验主力。4 个 Pi05 CRM always-on 在跑 (cuda:0/1/3/5)，cuda:2/4 空闲
- **bjb1-18228**: smolvla tau-sweep (cuda:0 tau040-long, cuda:1 tau045-long)
- **bjb1-32546**: crm-always-on-long-s45 bonus seed (cuda:5)
- **bjb2-28827**: smolvla-tau015-spatial-s42-fix (cuda:4) + 4× tau-sweep long (tau015/020/030/035，pid 4609/5160/5635/7362)
- 活跃 cron 共 13 个（reconcile 刚确认），均为进程存活监控
- Worker 池 = 0（无活跃 Worker）

### 3. 📊 当前状态
**刚完成**：pi05-crm-always-on-spatial-s42 结果分析 + 向 Director 汇报
- SR=96%, baseline=97%, Δ=-1pp，确认 Pi05 CRM always-on Spatial 有害，与 SmolVLA 一致
- 已更新 registry（DONE/success）、已汇报 Director

**RUNNING 实验（8 GPU）**：
| exp_id | 服务器 | GPU | 说明 |
|--------|--------|-----|------|
| pi05-crm-always-on-object-s42 | cqa1-32758 | cuda:1 | Table 2 Pi05 CRM always-on |
| pi05-crm-always-on-goal-s42 | cqa1-32758 | cuda:3 | Table 2 Pi05 CRM always-on |
| pi05-crm-always-on-long-s42 | cqa1-32758 | cuda:5 | Table 2 Pi05 CRM always-on |
| pi05-crm-always-on-object-s43 | cqa1-32758 | cuda:0 | Table 2 Pi05 CRM always-on seed2 |
| smolvla-tau040-long-s42 | bjb1-18228 | cuda:0 | tau-sweep 补充 |
| smolvla-tau045-long-s42 | bjb1-18228 | cuda:1 | tau-sweep 补充 |
| crm-always-on-long-s45 | bjb1-32546 | cuda:5 | SmolVLA bonus seed |
| smolvla-tau015-spatial-s42-fix | bjb2-28827 | cuda:4 | tau-sweep 修复 |

**等待**：无 Worker 回调待处理。等待上述 cron 自然回调。Paper Agent 已派单 Table 1 重构（上轮 session）。

### 4. 📋 待办
- pi05-crm-always-on-{object,goal,long}-s42 完成 → 分析结果 + 更新 Table 2 数据 + 汇报 Director（预期全部 harmful）
- pi05-crm-always-on-object-s43 完成 → 与 object-s42 做 multi-seed 一致性检查
- crm-always-on-long-s45 完成 → SmolVLA Long suite 第 4 个 seed，更新均值/std
- smolvla tau-sweep (tau015/020/030/035/040/045 long) 完成 → 更新 Appendix tau-sweep 表
- 所有 Pi05 CRM always-on 到齐 → 组装 Table 2 完整数据，派 Paper Agent 写 Table 2
- DDL 前 Paper Agent Table 1 重构 + 叙事升级完成 → 最终提交流程

### 5. 🎯 战略上下文
- **核心叙事**：CRM 修正是双刃剑，盲目 always-on 在 4/4 suites 有害（SmolVLA 已确认），Adaptive gating 全面恢复。Pi05 实验是 cross-VLA 泛化证据 (MC3)
- **Table 1**：K-matched 3 列（VLA-only K=1 / K=2 CRM always-on / K=2 Adaptive），SmolVLA 数据完整
- **Table 2**：Pi05 数据。VLA-only baseline 已锁定。CRM always-on 刚出 Spatial (-1pp)，其余 3 suites 在跑。Adaptive 已有数据（之前 r2 系列）
- **Long suite 是最有力证据**：SmolVLA CRM always-on Long -14.8pp（D178），Pi05 Long 结果高度期待
- **易错点**：Pi05 VLA-only SR 用的是 percentage（97%=97），但部分旧实验用 0-1 scale（0.98=98%）。看 metrics 时注意 scale 差异
- **D170**：Long tau-sweep 有非单调性，Appendix 诚实报告 + MC2 claim 限定为 cross-suite 层面

## 可查的历史
前 294 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:pi05-crm-always-on-spatial-s42",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-28T17:43:08.458759+00:00_

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
  "session": "cron:hook:pi05-crm-always-on-spatial-s42",
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

_source line 3 · 2026-05-28T17:43:08.509465+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-spatial-s42",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-28T17:43:11.419709+00:00_

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
  "session": "cron:hook:pi05-crm-always-on-spatial-s42",
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

_source line 5 · 2026-05-28T17:43:11.470419+00:00_

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
  "session": "cron:hook:pi05-crm-always-on-spatial-s42",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-28T17:43:12.476689+00:00_

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
  "session": "cron:hook:pi05-crm-always-on-spatial-s42",
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

_source line 7 · 2026-05-28T17:43:12.477104+00:00_

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
  "session": "cron:hook:pi05-crm-always-on-spatial-s42",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-28T17:43:14.636745+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1619}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-spatial-s42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 3217
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-28T17:43:14.688956+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-spatial-s42",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 3218
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-28T17:43:14.689634+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"# Handover — 2026-05-28\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无运行中实验 — 2026-05-28 全部实验已 kill/cancel）\\n\\n## 待处理\\n（全部 179 项已取消 — 2026-05-28 用户指令全面停机）\\n\\n## 近期结论\\n- **eval-supp-long-adapt-tau025-s44** (negative): Long Adaptive τ=0.25 s44, SR=56%, trigger=4.9%. Below VLA-only baseline (58%). Supplementary seed variance data — 数据已充足。\\n- **pi05-adaptive-goal-s44-backfill** (success): Pi05 Adaptive Conformal on Goal s44. Fills Table 2 gap (only s42/s43 exist). Cross-seed validation for Pi05 Goal adaptive.\\n\\n## 趋势\\n成功 768 / 负向 97 / 失败 130 / 共 1230\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-18228: 1× RTX 4090 空闲（配置说 4 卡但实测仅 1 卡）\\nbjb1-32546: ❌ 连接失败（port 32546 不可达，AutoDL 实例可能已关机/端口变更）\\nbjb2-28827: ❌ 连接失败（port 28827 不可达）\\ncqa1-32758: ❌ 连接失败（port 32758 不可达）\\n\\n## 告警\\n- plan_001-crm-smolvla: 训练失败 — unknown\\n- plan_014-reconvla-baseline: 训练失败 — unknown\\n- eval-smolvla-libero-spatial: 训练失败 — unknown\\n- eval-spatial-reeval-v2: 已被终止 — unknown\\n- precompute-v2-shard0: 已被终止 — unknown\\n- precompute-v2-shard1: 已被终止 — unknown\\n- precompute-v2-shard2: 已被终止 — unknown\\n- eval-spatial-v3-full: 已被终止 — unknown\\n- precompute-v3-shard0: 已被终止 — unknown\\n- precompute-v3-shard1: 已被终止 — unknown\\n- precompute-v3-shard2: 已被终止 — unknown\\n- eval-spatial-v4-full: 已被终止 — unknown\\n- eval-object-v4-full: 已被终止 — unknown\\n- eval-spatial-v5-full: 已被终止 — unknown\\n- crm-train-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v2: 已被终止 — unknown\\n- eval-acr-spatial-v1: 已被终止 — unknown\\n- crm-train-a3-obs-only: 已被终止 — unknown\\n- eval-acr-vla-spatial-v1: 已被终止 — unknown\\n- eval-spatial-v6-full: 已被终止 — unknown\\n- eval-acr-spatial-v2: 已被终止 — unknown\\n- eval-object-v5-full: 已被终止 — unknown\\n- eval-object-v6-full: 已被终止 — unknown\\n- crm-train-a4-s
…[truncated 5000 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-spatial-s42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 2212
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-28T17:43:14.740420+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-28 09:39 UTC | 更新原因: Paper Agent 确认 Table 1 重构+叙事升级完成，论文就绪待提交，ROADMAP 更新任务完成状态\\n\\n> 详见 paper_framing.md（D170/D177/D178: K=2 CRM always-on 4/4 harmful + K-matched Table 1）\\n\\n## 核心方向\\n**ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs**。CoRL 2026 DDL **2026-05-28 20:00 北京时间**。\\n\\n## 当前进展\\n- **论文就绪**：编译通过，8 页正文 + 6 页（refs 2 + appendix 4），零 critical warning\\n- **Table 1 重构完成**：K-matched 3 列（VLA-only K=1 / K=2 CRM always-on / K=2 Adaptive），4/4 suites harmful 叙事升级 ✅\\n- **Table 3 (Pi05) 完成**：4/4 suites degradation-only（含 Long 94.0→77.0, Δ=-17.0pp），seed-matched ✅\\n- **叙事一致性**：4/4 harmful + gating recovery，全文对齐（Abstract/Intro/Experiments/Conclusion）✅\\n- **贡献**：3 条（OpenVLA 从贡献列表移除，保留 §4.5 + Appendix）✅\\n- **Backfill 修复**：M115 根因定位（手动 update_registry 不创建 cron），已全部改用 submit_training_job\\n- **GPU**：22/22 满载，补充实验持续产出\\n\\n## CRM always-on 最终数据（SmolVLA, K=2, n=3）\\n| Suite | VLA-only (K=1) | CRM always-on (K=2) | Adaptive (K=2) | Δ CRM vs VLA | Δ Adaptive vs VLA |\\n|-------|---------------|--------------------|-----------|----|---|\\n| Spatial | 79.3±0.8 | 78.0±1.7 | 80.8±1.1 | -1.3pp | +1.5pp |\\n| Goal | 83.7±1.3 | 80.0±0.5 | 85.0±1.3 | -3.7pp | +1.3pp |\\n| Object | 77.7±1.3 | 73.0±1.8 | 77.8±2.1 | -4.7pp | +0.1pp |\\n| Long | 58.0±1.5 | 43.2±2.3 | 57.7±1.5 | -14.8pp | -0.3pp |\\n\\n## 近期任务\\n- [x] **P0** 收集 Long CRM always-on 3 seeds → 43.2%\\n- [x] **P0** Paper Agent Table 1 K-matched 重构 + 叙事 4/4 升级 ✅\\n- [ ] **P0** 等待用户确认 title + CoRL 提交决定（contingency: 18:00 BJ 默认提交）\\n- [ ] **P1** Pi05 CRM always-on long s43/s44（bjb1-18228 运行中）→ supplementary\\n- [ ] **P1** Bonus seeds + tau-sweep 补充点（22 GPU 持续跑）→ supplementary / camera-ready\\n- [ ] **P2** 最终论文提交 submit_paper_to_review\\n- [ ] **Reviewer** 最终 claim 强度
…[truncated 2374 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-spatial-s42",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 2263
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-28T17:43:31.803868+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__main_agent_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-always-on-spatial-s42",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__main_agent_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-28T17:43:33.360396+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-spatial-s42",
  "tool": "ToolSearch",
  "elapsed_ms": 1556
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-28T17:43:40.691427+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 0/22 | Worker 0 | 全面停机状态\n\nLoop #30 session 启动。Registry 确认 0 个 RUNNING 实验，0 个活跃 cron。report.md 显示用户已下令全面停机。\n\n论文状态：编译通过，Table 1 K-matched 重构 + 叙事升级已完成，就绪待提交。\n\n待 Director 指令：\n1. Title 确认 + CoRL 提交决定（ROADMAP contingency: 18:00 BJ 默认提交）\n2. 是否需要最终提交流程（submit_paper_to_review / PDF 打包）",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-always-on-spatial-s42",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 0/22 | Worker 0 | 全面停机状态\n\nLoop #30 session 启动。Registry 确认 0 个 RUNNING 实验，0 个活跃 cron。report.md 显示用户已下令全面停机。\n\n论文状态：编译通过，Table 1 K-matched 重构 + 叙事升级已完成，就绪待提交。\n\n待 Director 指令：\n1. Title 确认 + CoRL 提交决定（ROADMAP contingency: 18:00 BJ 默认提交）\n2. 是否需要最终提交流程（submit_paper_to_review / PDF 打包）",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-28T17:43:44.560162+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-always-on-spatial-s42",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 3868
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-28T17:43:48.047333+00:00_

已完成 session-start 初始化：

- Registry: 0 RUNNING，全面停机
- Cron: 0 活跃
- 论文就绪，待 title 确认 + 提交决定
- 已向 Director 汇报，等待指令

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:pi05-crm-always-on-spatial-s42"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 17 · 2026-05-29T10:02:45.179057+00:00_

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
  "session": "cron:hook:pi05-crm-always-on-spatial-s42",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-29T10:03:36.486244+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- CoRL 2026 DDL **2026-05-28 20:00 北京时间**已过（今天是 2026-05-29）。如果还没提交，需确认 Director 是否已提交或决定放弃
- 用户已下令**全面停机**（2026-05-28），所有 179 项实验已 kill/cancel，**不要启动新实验**除非 Director 明确指令
- westd-49937 服务器数据系统性偏低 4-5pp，该服务器结果**不入主表**
- Pi05 Object CRM 数据不入 Table 2 主表，放 Supplement（D171）
- memory.md 之前被误覆盖（原文件 Birth 2026-05-26 内容丢失），操作 memory.md 时**先读再追加**，禁止 save_project_file 全量覆盖

### 2. 🖥️ 基础设施快照
- **cqa1-32758**: Pi05 实验主力，6 卡。全面停机后状态未知（report.md 显示连接失败）
- **bjb1-18228**: 4 卡（实测可能仅 1 卡可用）。report.md 显示连接失败
- **bjb1-32546**: 6 卡。report.md 显示连接失败（AutoDL 实例可能已关机/端口变更）
- **bjb2-28827**: 6 卡。report.md 显示连接失败
- 活跃进程：0（全面停机）
- 活跃 cron：0（reconcile 确认）
- Worker 池：0

### 3. 📊 当前状态
Loop #30 刚完成 session-start 初始化。Registry 确认 0 个 RUNNING 实验。已向 Director 汇报全面停机状态 + 论文就绪待提交。

论文状态：
- 编译通过，8 页正文 + 6 页（refs 2 + appendix 4）
- Table 1 K-matched 3 列重构完成，4/4 suites harmful 叙事升级完成
- Table 3 (Pi05) 完成，4/4 suites degradation-only
- Title 已锁定："Knowing When Not to Correct: Adaptive Te..."（D179）

等待中：Director 回复——确认是否已提交 CoRL / 下一步指令

### 4. 📋 待办
- Director 回复"已提交" → 项目进入 post-submission 阶段，等 camera-ready 或 rebuttal
- Director 回复"未提交 / 错过 DDL" → 确认是否转投其他会议（注意：不要主动建议 fallback，这是 Director 决策空间）
- Director 要求恢复实验 → 先确认服务器连接状态（4 台都报连接失败，AutoDL 实例可能已过期），再评估 GPU 可用性
- 如需新实验 → 所有 AutoDL 实例端口可能已变，需用户去控制台查新端口更新 SSH config

### 5. 🎯 战略上下文
- **核心叙事**：CRM always-on 是双刃剑，4/4 suites 有害（SmolVLA + Pi05 跨模型验证），Adaptive gating 全面恢复
- **三大 Claim**：MC1（4/4 harmful）、MC2（trigger rate ↔ Δ 单调正相关，cross-suite + τ-sweep）、MC3（跨 VLA 泛化）
- **数据完整性**：SmolVLA 3-seed 完整，Pi05 degradation-only 两列（VLA-only + CRM always-on）完整
- **Long suite 是最强证据**：SmolVLA CRM always-on Long -14.8pp（D178），Pi05 Long 94.0→77.0 Δ=-17.0pp
- **DDL 已过**：今天是 5-29，DDL 是 5-28 20:00 BJ。项目处于"论文就绪但不确定是否已提交"状态。不要假设已提交——等 Director 确认
- **易错点**：Pi05 VLA-only SR 用 percentage scale（97%=97），部分旧实验用 0-1 scale（0.98=98%），看 metrics 注意 scale
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:pi05-crm-always-on-spatial-s42"
}
```

</details>

---
