# cron hook crm always on long s44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/cron_hook_crm-always-on-long-s44.jsonl`
- **Structured JSON:** [`479a0389f5b36c22eb8f.json`](../../sessions/47/479a0389f5b36c22eb8f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-29T08:21:48.286019+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #31。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: 仅 bjb1-18228:cuda:0-3, bjb1-32546:cuda:0-5, bjb2-28827:cuda:0-5, cqa1-32758:cuda:0-5（共 22 卡）。其他服务器/卡号禁止使用
- **westd 服务器数据有毒**: D175 确认 westd-49937 LIBERO assets 版本与其他服务器不同（HF 下载 vs 预装），westd 产出的 eval 数据**不可用于论文 Table**
- **Pi05 unified checkpoint 必须传 `--obs_dim 2048 --unified_obs_dim 2088`**: checkpoint 路径 `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt`，缺参数会 shape mismatch 报错（已踩过两次）
- **CoRL DDL 2026-05-28 20:00 BJ**: D184 锁定，20:00 后数据冻结。论文 title 已锁: "Knowing When Not to Correct: Adaptive Test-Time Refinement for Frozen VLAs"
- **perdof 消融不可与 Table 1 对比**: D176 确认 perdof 训练条件与主表不同，不能放同表

### 2. 🖥️ 基础设施快照
- **服务器 × 4**: bjb1-18228 (4卡), bjb1-32546 (6卡), bjb2-28827 (6卡), cqa1-32758 (6卡)
- **工作目录**: `/root/acr-vla-conformal-refinement`（所有服务器统一路径）
- **账号**: root
- **SmolVLA CRM checkpoint**: `/root/autodl-tmp/checkpoints/crm_smolvla_unified_4suite/crm_best.pt`（obs_dim=960）
- **Pi05 CRM checkpoint**: `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt`（obs_dim=2048, unified_obs_dim=2088）
- **活跃进程**: 无。0 RUNNING 实验, 0 active crons, 0 running workers
- **GPU 状态**: 全部 22 卡空闲

### 3. 📊 当前状态
Loop #30 仅执行了 session-start 初始化：read_registry 确认 0 RUNNING/PREPARING/QUEUED/PENDING/ALLOCATED，reconcile_crons 确认 0 active crons，向 Director 汇报了状态。实验管线完全清空，论文编译通过就绪。

- **Registry**: 1229 实验总计 — 768 success / 96 negative / 130 failed
- **report.md 小不一致**: eval-supp-obj-adapt-tau025-s43 标为运行中但 registry 无 RUNNING——可能已完成但 report 未刷新，不影响主表
- **等待中**: Director 回复提交确认（已通过 main_agent_post_to_director 汇报）。无 Worker/Cron 回调待处理

### 4. 📋 待办（条件触发式）
- Director 确认提交 → 执行 CoRL 提交流程（submit_paper_to_review 或协助用户手动提交）
- 18:00 BJ 无用户响应 → 按 D184 contingency 默认提交
- Director 指示补充 seeds → 起 Worker 跑 supplementary（Pi05 CRM always-on long s43/s44, tau-sweep 补充点），仅 supplementary/camera-ready 用途，不影响主表
- 任何 backfill cron 回调到达 → update_registry + 刷新 report.md

### 5. 🎯 战略上下文
- **核心 narrative**: CRM correction 是双刃剑——无条件应用 4/4 suites 有害; Adaptive gating 正确决定"何时不修正"是核心贡献。Analysis-first paper, method 是分析洞察的产物
- **3 个 Claims**: MC1=CRM always-on 4/4 有害+Adaptive 恢复, MC2=trigger rate↔Δ 单调正相关, MC3=跨 VLA 泛化 (SmolVLA 0.4B + Pi05 3.6B)
- **决策链关键节点**: D170(K-matched重构) → D177(Table 1 3列) → D178(Long最强证据) → D179(Title锁定) → D184(提交确认)
- **易错点**: ① 不要混淆旧 K=10 数据和新 K=2 K-matched 数据——Table 1 只用 D170 之后的数据 ② Pi05 Table 只有 degradation-only 两列（VLA-only + CRM always-on），没有 Adaptive 列 ③ Long suite 是论文最有力证据 (-14.8pp)，任何叙事调整不能弱化这个数据点 ④ OpenVLA-OFT 已放弃(D124)，不要尝试恢复

## 可查的历史
前 308 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:crm-always-on-long-s44",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-29T08:21:56.679452+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:crm-always-on-long-s44",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-29T08:21:56.730090+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s44",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-29T08:21:59.540765+00:00_

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
  "session": "cron:hook:crm-always-on-long-s44",
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

_source line 5 · 2026-05-29T08:22:00.511445+00:00_

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
  "session": "cron:hook:crm-always-on-long-s44",
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

_source line 6 · 2026-05-29T08:22:00.963696+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'PENDING'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:crm-always-on-long-s44",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'PENDING'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-29T08:22:01.417425+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'QUEUED'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:crm-always-on-long-s44",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'QUEUED'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-29T08:22:01.870416+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'ALLOCATED'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:crm-always-on-long-s44",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'ALLOCATED'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-29T08:22:02.373440+00:00_

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
  "session": "cron:hook:crm-always-on-long-s44",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-29T08:22:02.877111+00:00_

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
  "session": "cron:hook:crm-always-on-long-s44",
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

_source line 11 · 2026-05-29T08:22:03.331439+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:crm-always-on-long-s44",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-29T08:22:05.203390+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.643}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s44",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 5662
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-29T08:22:11.795301+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.5493}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s44",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 11283
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-29T08:22:15.255781+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.4611}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s44",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 14292
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-29T08:22:18.570669+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.3087}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s44",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 17153
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-29T08:22:21.683455+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.0915}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s44",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 19813
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-29T08:22:21.734127+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s44",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 19360
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-29T08:22:21.785107+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"# Handover — 2026-05-28\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无运行中实验 — 2026-05-28 全部实验已 kill/cancel）\\n\\n## 待处理\\n（全部 179 项已取消 — 2026-05-28 用户指令全面停机）\\n\\n## 近期结论\\n- **eval-supp-long-adapt-tau025-s44** (negative): Long Adaptive τ=0.25 s44, SR=56%, trigger=4.9%. Below VLA-only baseline (58%). Supplementary seed variance data — 数据已充足。\\n- **pi05-adaptive-goal-s44-backfill** (success): Pi05 Adaptive Conformal on Goal s44. Fills Table 2 gap (only s42/s43 exist). Cross-seed validation for Pi05 Goal adaptive.\\n\\n## 趋势\\n成功 768 / 负向 97 / 失败 130 / 共 1230\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-18228: 1× RTX 4090 空闲（配置说 4 卡但实测仅 1 卡）\\nbjb1-32546: ❌ 连接失败（port 32546 不可达，AutoDL 实例可能已关机/端口变更）\\nbjb2-28827: ❌ 连接失败（port 28827 不可达）\\ncqa1-32758: ❌ 连接失败（port 32758 不可达）\\n\\n## 告警\\n- plan_001-crm-smolvla: 训练失败 — unknown\\n- plan_014-reconvla-baseline: 训练失败 — unknown\\n- eval-smolvla-libero-spatial: 训练失败 — unknown\\n- eval-spatial-reeval-v2: 已被终止 — unknown\\n- precompute-v2-shard0: 已被终止 — unknown\\n- precompute-v2-shard1: 已被终止 — unknown\\n- precompute-v2-shard2: 已被终止 — unknown\\n- eval-spatial-v3-full: 已被终止 — unknown\\n- precompute-v3-shard0: 已被终止 — unknown\\n- precompute-v3-shard1: 已被终止 — unknown\\n- precompute-v3-shard2: 已被终止 — unknown\\n- eval-spatial-v4-full: 已被终止 — unknown\\n- eval-object-v4-full: 已被终止 — unknown\\n- eval-spatial-v5-full: 已被终止 — unknown\\n- crm-train-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v2: 已被终止 — unknown\\n- eval-acr-spatial-v1: 已被终止 — unknown\\n- crm-train-a3-obs-only: 已被终止 — unknown\\n- eval-acr-vla-spatial-v1: 已被终止 — unknown\\n- eval-spatial-v6-full: 已被终止 — unknown\\n- eval-acr-spatial-v2: 已被终止 — unknown\\n- eval-object-v5-full: 已被终止 — unknown\\n- eval-object-v6-full: 已被终止 — unknown\\n- crm-train-a4-s
…[truncated 5000 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s44",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 18907
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-29T08:22:21.785926+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-28 22:38 UTC | 更新原因: 反映全面停机真实状态，清理过时待办项（DDL 已过、GPU 停机）\\n\\n> 详见 paper_framing.md（D170/D177/D178: K=2 CRM always-on 4/4 harmful + K-matched Table 1）\\n\\n## 核心方向\\n**ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs**。CoRL 2026 DDL **2026-05-28 20:00 北京时间（已过）**。\\n\\n## 当前进展\\n- **论文就绪**：编译通过，8 页正文 + 6 页（refs 2 + appendix 4），零 critical warning\\n- **Table 1 重构完成**：K-matched 3 列（VLA-only K=1 / K=2 CRM always-on / K=2 Adaptive），4/4 suites harmful 叙事升级 ✅\\n- **Table 3 (Pi05) 完成**：4/4 suites degradation-only（含 Long 94.0→77.0, Δ=-17.0pp），seed-matched ✅\\n- **叙事一致性**：4/4 harmful + gating recovery，全文对齐（Abstract/Intro/Experiments/Conclusion）✅\\n- **贡献**：3 条（OpenVLA 从贡献列表移除，保留 §4.5 + Appendix）✅\\n- **全部实验停机**：2026-05-28 用户指令全面停机，1423 实验全部 DONE/killed/cancelled\\n- **提交状态**：待用户确认（DDL 已过，已询问用户）\\n\\n## CRM always-on 最终数据（SmolVLA, K=2, n=3）\\n| Suite | VLA-only (K=1) | CRM always-on (K=2) | Adaptive (K=2) | Δ CRM vs VLA | Δ Adaptive vs VLA |\\n|-------|---------------|--------------------|-----------|----|---|\\n| Spatial | 79.3±0.8 | 78.0±1.7 | 80.8±1.1 | -1.3pp | +1.5pp |\\n| Goal | 83.7±1.3 | 80.0±0.5 | 85.0±1.3 | -3.7pp | +1.3pp |\\n| Object | 77.7±1.3 | 73.0±1.8 | 77.8±2.1 | -4.7pp | +0.1pp |\\n| Long | 58.0±1.5 | 43.2±2.3 | 57.7±1.5 | -14.8pp | -0.3pp |\\n\\n## 近期任务\\n- [x] 收集 Long CRM always-on 3 seeds → 43.2%\\n- [x] Paper Agent Table 1 K-matched 重构 + 叙事 4/4 升级\\n- [x] Figure 1 间距修复 + AI 声明移至附录 + Table 3 浮动调整\\n- [ ] **等待用户确认**：论文是否已提交 CoRL / 是否转投其他会议\\n- [ ] **等待用户确认**：3 台不可达服务器（bjb1-32546, bjb2-28827, cqa1-32758）是否释放\\n\\n## Claim 策略 (D170/D178)\\n- **MC1**: CRM always-on **4/4 suites** 有害 → Adaptive gating 全面恢复（K-matched controlled experiment）\\n- **MC2**: Trigger rate ↔ Δ 单调正相关（cross-suite + within-suite τ-swe
…[truncated 2138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s44",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 18454
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-29T08:22:30.725626+00:00_

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
  "session": "cron:hook:crm-always-on-long-s44",
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

_source line 21 · 2026-05-29T08:22:30.876677+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s44",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-29T08:22:39.512567+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 0/22 | Worker 0 (GPU 0 / CPU 0) | 服务器: bjb1-18228 可达(空闲), bjb1-32546/bjb2-28827/cqa1-32758 不可达\n\nLoop #31 session-start 完成。状态确认：\n\n- **实验管线**：完全清空。0 RUNNING / 0 PREPARING / 0 PENDING / 0 QUEUED / 0 ALLOCATED。0 active crons\n- **Registry 总计**：~1230 实验（768 success / 97 negative / 130 failed）\n- **论文**：编译通过就绪，Title 已锁定 \"Knowing When Not to Correct: Adaptive Test-Time Refinement for Frozen VLAs\"\n- **CoRL DDL**：2026-05-28 20:00 BJ 已过\n\n**待 Director 确认**：\n1. 论文是否已提交 CoRL？\n2. 如未提交，是否转投其他会议？\n3. 3 台不可达服务器（bjb1-32546, bjb2-28827, cqa1-32758）是否已释放？\n\n当前无任何阻塞任务，等待指令。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:crm-always-on-long-s44",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 0/22 | Worker 0 (GPU 0 / CPU 0) | 服务器: bjb1-18228 可达(空闲), bjb1-32546/bjb2-28827/cqa1-32758 不可达\n\nLoop #31 session-start 完成。状态确认：\n\n- **实验管线**：完全清空。0 RUNNING / 0 PREPARING / 0 PENDING / 0 QUEUED / 0 ALLOCATED。0 active crons\n- **Registry 总计**：~1230 实验（768 success / 97 negative / 130 failed）\n- **论文**：编译通过就绪，Title 已锁定 \"Knowing When Not to Correct: Adaptive Test-Time Refinement for Frozen VLAs\"\n- **CoRL DDL**：2026-05-28 20:00 BJ 已过\n\n**待 Director 确认**：\n1. 论文是否已提交 CoRL？\n2. 如未提交，是否转投其他会议？\n3. 3 台不可达服务器（bjb1-32546, bjb2-28827, cqa1-32758）是否已释放？\n\n当前无任何阻塞任务，等待指令。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-29T08:22:43.720048+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:crm-always-on-long-s44",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 4207
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-29T08:22:47.736361+00:00_

Session-start 初始化完成，已向 Director 汇报：

- **实验管线**：完全清空，0 活跃实验/cron/worker
- **22 卡全空闲**，3/4 服务器不可达
- **CoRL DDL 已过**，论文就绪待确认提交状态
- 等待 Director 回复下一步指令

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:crm-always-on-long-s44"
}
```

</details>

---
