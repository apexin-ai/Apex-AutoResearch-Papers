# cron hook pi05 crm k2 long s42 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/cron_hook_pi05-crm-k2-long-s42-r2.jsonl`
- **Structured JSON:** [`1ac35b3194b38efc2542.json`](../../sessions/1a/1ac35b3194b38efc2542.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-27T05:16:29.528261+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #29。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单严格按 `get_project_status` 的 `execution.gpu_ids`，不可用白名单外 GPU，即使 Director 指令也要 push back
- westd-49937 (RTX PRO 6000 Blackwell) 与 4090 有 ~3pp 系统性偏差 → Table 2 必须 same-server paired comparison，不可跨服务器混用数据
- evaluate.py 必须用 commit a594db5 版本（D163 决策），所有补跑用旧代码确保 Table 一致性
- π0.5 eval 实验不写 W&B metrics，进程自然退出后 cron 会报 false positive → 需手动检查 JSON 输出文件确认是否实际完成
- 脚本内 GPU 编号始终从 0 开始（框架自动注入 CUDA_VISIBLE_DEVICES 映射物理 GPU）

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (4×4090): 工作目录 /root/acr-vla-conformal-refinement, CRM checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt
- **bjb1-32546** (6×4090): 同上结构, 跑 CRM K=2 系列
- **bjb2-28827** (6×4090): π0.5 CRM/Adaptive Spatial 系列
- **bjb2-24035** (1×4090D): 状态待确认
- **cqa1-32758** (6×4090D): τ-sweep + Adaptive 系列, pi05-crm-k2-long-s44-cqa1 运行中
- **westd-49937** (6×RTX PRO 6000): VLA-only baseline paired comparison
- 活跃 cron 监控 24 个实验（reconcile_crons 最新结果见 session 上文）
- JSON 输出路径模式: `/root/acr-vla-conformal-refinement/logs/eval_{suite}_{mode}_{params}_seed{N}_pi05_K2.json`

### 3. 📊 当前状态
- 收到 pi05-crm-k2-long-s42-r2 失败回调 → registry 已标记为 FALSE POSITIVE (success, 82.0%)，无需再处理
- pi05-crm-k2-long-s43-r2 进程消失（cron miss 1/5），已派 Worker `worker_diagnose_pi05-crm-k2-long-s43-r2_20260526T122610` 去 bjb1-18228 诊断 → **等待回调**
- ~20 个实验 RUNNING（CRM K=2 Goal/Object/Spatial/Long 各 3 seed + Adaptive 各 suite 3 seed + westd VLA-only paired）
- DDL: CoRL 2026 **2026-05-29**（~2.5天）

### 4. 📋 待办（条件触发式）
- Worker diagnose s43-r2 回调 → 若 JSON 存在则 update_registry(conclusion=success, metrics=...) + 标记 false positive；若真正失败则重新提交
- pi05-crm-k2-long-s43-r2 cron 继续 miss → 到 5/5 时会自动标记 failed，届时需确认是否已被 Worker 处理
- 各 suite π0.5 实验完成回调 → 更新 registry + 填 Table 2 对应 cell + 汇报 Director
- 全部 π0.5 Table 2 数据收集完成 → 汇报 Director 触发 Paper Agent 写作流水线最终步骤
- 空闲 GPU 出现（bjb1-32546 6卡、cqa1 3卡等完成后） → 部署 QUEUED 实验（如 pi05-k2mean-goal-s42-r2）

### 5. 🎯 战略上下文
- **核心 narrative**: SmolVLA Table 1 完成（36/36 cells），π0.5 Table 2 是最后战场。MC3 已 reframe 为"模型能力依赖性分析"（D155），不再 claim cross-model generalization
- **MC1 consistency claim**: Adaptive ≥ CRM on ALL 4 suites（n=3 p≈0.27 n.s.，附录 8-seed p=0.017）
- **关键决策链**: D157(统一 seed s42/43/44) → D158(westd Blackwell 偏差) → D159(Spatial VLA-only 修正 79.3±0.8) → D163(evaluate.py revert a594db5)
- **易错点 1**: π0.5 eval 进程完成后不写 W&B，cron 会连续报 false positive failure。每次收到失败回调先检查 JSON 输出文件，不要盲目重跑
- **易错点 2**: westd 数据不能与 bjb 数据混入同一 Table row，必须 same-server paired
- **易错点 3**: Table 2 的 K=2 argmin 选择本身对强 VLA (π0.5) 有害（τ=0.90 时 SR=89% vs VLA-only 96%），这不是 CRM 的问题而是 argmin selection 的问题——分析时需区分
- **时间压力**: DDL 5/29，~2.5 天，π0.5 Table 2 预估 12-24h 完成全部数据收集，Paper Agent 已激活 Reframe 模式

## 可查的历史
前 280 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-27T05:16:54.962533+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_registry,reconcile_crons,read_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_registry,reconcile_crons,read_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-27T05:16:55.095500+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "ToolSearch",
  "elapsed_ms": 132
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-27T05:17:00.524203+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "registry cron project",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "registry cron project",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-27T05:17:01.318056+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "ToolSearch",
  "elapsed_ms": 793
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-27T05:17:06.230285+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'RUNNING'}",
  "fields": "['exp_id', 'status', 'conclusion', 'metrics', 'server', 'hypothesis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'RUNNING'}",
    "fields": "['exp_id', 'status', 'conclusion', 'metrics', 'server', 'hypothesis']"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-27T05:17:07.164353+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__reconcile_crons",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__reconcile_crons",
    "max_results": "1"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-27T05:17:08.152067+00:00_

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
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
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

_source line 9 · 2026-05-27T05:17:08.562576+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "ROADMAP.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "ROADMAP.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T05:17:54.741320+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"smolvla-vla-only-long-n20-s43\": {\"status\": \"RUNNING\"}, \"smolvla-vla-only-long-n20-s42\": {\"status\": \"RUNNING\", \"hypothesis\": \"Fair VLA-only baseline for SmolVLA Long with n_rollouts=20 matching CRM experiments; prior baseline used n_rollouts=10 creating unfair comparison\"}, \"smolvla-tau015-long-s43\": {\"status\": \"RUNNING\"}, \"smolvla-tau035-long-s43\": {\"status\": \"RUNNING\"}, \"smolvla-tau025-long-s43\": {\"status\": \"RUNNING\"}}, \"count\": 5, \"total\": 5, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 48.1844}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 48511
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-27T05:17:54.757672+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "ToolSearch",
  "elapsed_ms": 47593
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T05:17:55.079690+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-27T04:16:53Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 1231 个实验 — ANALYZING 1, DEPLOYED 6, DONE 1024, PREPARING 185, QUEUED 10, RUNNING 5\\n**DONE 分布**: failed 98, killed 207, negative 94, success 625\\n\\n### GPU 占用\\n- **实际运行**: 5 张 — bjb1-18228:cuda:0(smolvla-tau015-long-s43), bjb1-18228:cuda:1(smolvla-tau025-long-s43), bjb1-18228:cuda:2(smolvla-tau035-long-s43), cqa1-32758:cuda:0(smolvla-vla-only-long-n20-s42), cqa1-32758:cuda:1(smolvla-vla-only-long-n20-s43)\\n\\n### 💾 磁盘余量\\n- **bjb1-18228**:\\n  - `/init`: 150M/150M 可用（已用 1%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/438G 可用（已用 4%）\\n- **bjb1-32546**:\\n  - `/autodl-pub`: 1.1T/7.0T 可用（已用 85%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/438G 可用（已用 4%）\\n- **bjb2-28827**:\\n  - `/autodl-pub`: 4.3T/14T 可用（已用 70%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/439G 可用（已用 5%）\\n- **cqa1-32758**:\\n  - `/autodl-pub`: 474G/7.0T 可用（已用 94%） ⚠️\\n  - `/autodl-pub/data`: 1.5T/4.0T 可用（已用 65%）\\n  - `/usr/bin/nvidia-smi`: 77G/98G 可用（已用 19%）\\n- **westd-49937**:\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/usr/bin/nvidia-smi`: 815G/879G 可用（已用 3%）\\n- **bjb2-24035**:\\n  - `/autodl-pub`: 5.1T/14T 可用（已用 64%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 45G/437G 可用（已用 90%） ⚠️\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `smolvla-tau015-long-s43` | bjb1-18228 | cuda:0 | 555572 | `…ns/acr-vla-conformal-refinement/smolvla-tau015-long-s43.log` |\\n| `smolvla-tau025-long-s43` | bjb1-18228 | cuda:1 | 556705 | `…ns/acr-vla-confo
…[truncated 7778 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 46927
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-27T05:17:55.202729+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-27 01:34 UTC | 更新原因: D169 Appendix patch 完成 + Agent 系统性问题持续\\n\\n> 详见 paper_framing.md（D168: Goal harm 13.2pp, D169: τ-sweep→sensitivity analysis）\\n\\n## 核心方向\\n**ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs**。CoRL 2026 DDL **2026-05-28 20:00 北京时间**（~34h）。\\n\\n## 当前进展\\n- **Table 1 + Table 2**: ✅ 锁定\\n- **论文写作**: ✅ Step 5 收敛 + D169 Appendix τ-sweep patch 完成（v54, 14页）\\n- **审稿提交**: ✅ submit_paper_to_review 已发，⚠️ pending 用户审批 review mode\\n- **τ-sweep 数据**: scatter_data.csv 89 行。部分实验仍在运行\\n- **Agent 系统性问题**: 连续 7 次 reset 后只处理 1-2 条消息就死。已向 Manager 升级\\n\\n## 近期任务\\n- [x] Table 2 完成\\n- [x] 论文 Step 5 收敛\\n- [x] submit_paper_to_review 提交\\n- [x] D169 Appendix τ-sweep 叙事调整 + Paper Agent patch\\n- [x] 主要 τ-sweep 数据收割（89 行）\\n- [ ] **P0** 等待用户审批 review mode（已多次提醒）\\n- [ ] **P1** Agent 稳定性修复（Manager 已知）\\n- [ ] **P1** 剩余 τ-sweep 收割：cqa1 pi05 s43 (6个) + bjb1-32546 SmolVLA Long s42 (3个)\\n- [ ] **P1** Stale RUNNING registry 修正（6个：bjb1-18228 4个 + bjb2-28827 2个）\\n- [ ] **P2** 正式审稿报告处理\\n- [ ] **P2** paper_framing.md 更新 D165-D169\\n\\n## Claim 策略\\n- **MC1** (D168): Adaptive ≥ CRM on 3/4 suites; recovery 19-38%\\n- **MC2** (D140+D169): Cross-suite trigger rate ↔ Δ 单调正相关。Within-suite τ-sweep 定位为 sensitivity analysis（SR 对 τ 稳健），非 MC2 within-suite 证据\\n- **MC3**: cross-VLA 模型能力依赖\\n\\n## GPU 预算\\n- 本项目分配：29 GPU（6 servers，bjb2-40593 掉线）\\n- 主要实验已完成，剩余 τ-sweep 补充实验在 cqa1/bjb1-32546 运行中\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D169 | 2026-05-27 | D169: τ-sweep Appendix 叙事定位调整 — \\\"sensitivity/robus | smolvla-tau015-goal-s43, smolvla-tau025-goal-s43, smolvla-tau035-goal-s43 |\\n| D168 | 2026-05-26 | D168: Goal CRM harm 计算修正 14.5pp→13.2pp, recovery 3 | pi05-adaptive-goal |\\n| D167 
…[truncated 1205 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 46640
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-27T05:18:01.615459+00:00_

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
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-27T05:18:02.974548+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'QUEUED'}",
  "fields": "['exp_id', 'status', 'server', 'hypothesis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'QUEUED'}",
    "fields": "['exp_id', 'status', 'server', 'hypothesis']"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-27T05:18:03.634751+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'ANALYZING'}",
  "fields": "['exp_id', 'status', 'conclusion', 'metrics', 'server']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'ANALYZING'}",
    "fields": "['exp_id', 'status', 'conclusion', 'metrics', 'server']"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-27T05:26:31.333822+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 5, \"results\": [{\"exp_id\": \"smolvla-tau015-long-s43\", \"success\": true, \"actions\": [\"Job still running (pid=smolvla-tau015-long-s43)\"]}, {\"exp_id\": \"smolvla-tau025-long-s43\", \"success\": true, \"actions\": [\"Job still running (pid=smolvla-tau025-long-s43)\"]}, {\"exp_id\": \"smolvla-tau035-long-s43\", \"success\": true, \"actions\": [\"Job still running (pid=smolvla-tau035-long-s43)\"]}, {\"exp_id\": \"smolvla-vla-only-long-n20-s42\", \"success\": true, \"actions\": [\"Job still running (pid=smolvla-vla-only-long-n20-s42)\"]}, {\"exp_id\": \"smolvla-vla-only-long-n20-s43\", \"success\": true, \"actions\": [\"Job still running (pid=smolvla-vla-only-long-n20-s43)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 509718
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-27T05:27:13.868513+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-k2-tau035-spatial-s42\": {\"status\": \"QUEUED\", \"hypothesis\": \"K=2 τ-sweep: τ=0.35 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting.\"}, \"eval-k2-tau025-spatial-s42\": {\"status\": \"QUEUED\", \"hypothesis\": \"K=2 τ-sweep: τ=0.25 Adaptive Conformal on Spatial s42. K=2 matches Table 1 production setting.\"}, \"eval-pi05-vla-only-object-s43-v2\": {\"status\": \"QUEUED\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s43. Cross-architecture validation without CRM.\"}, \"eval-pi05-vla-only-object-s42-v2\": {\"status\": \"QUEUED\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s42. Cross-architecture validation without CRM.\"}, \"eval-pi05-vla-only-goal-s43-v2\": {\"status\": \"QUEUED\", \"hypothesis\": \"π0.5 VLA-only baseline on Goal s43. Cross-architecture validation without CRM.\"}, \"eval-pi05-vla-only-goal-s42-v2\": {\"status\": \"QUEUED\", \"hypothesis\": \"π0.5 VLA-only baseline on Goal s42. Cross-architecture validation without CRM.\"}, \"eval-pi05-vla-only-spatial-s43-v2\": {\"status\": \"QUEUED\", \"hypothesis\": \"π0.5 VLA-only baseline on Spatial s43. Cross-architecture validation without CRM.\"}, \"eval-pi05-vla-only-spatial-s42-v2\": {\"status\": \"QUEUED\", \"hypothesis\": \"π0.5 VLA-only baseline on Spatial s42. Cross-architecture validation without CRM.\"}, \"eval-supp-object-vla-only-s50\": {\"status\": \"QUEUED\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Object seed 50. Extension seed beyond s42-49 sweep for additional statistical power in Object benchmark.\"}, \"eval-smolvla-lerobot-goal-seed44\": {\"status\": \"QUEUED\", \"hypothesis\": \"SmolVLA lerobot-eval baseline on LIBERO-Goal with seed=44 establishes reference SR for 3-seed mean±std paper comparison\"}}, \"count\": 10, \"total\": 10, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 41.8497}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 550893
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-27T05:27:41.444695+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"smolvla-tau025-object-s42-r2\": {\"status\": \"ANALYZING\"}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 28.0068}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 577809
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-27T05:28:03.512139+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'smolvla-tau025-object-s42-r2'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'smolvla-tau025-object-s42-r2'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-27T05:28:04.029740+00:00_

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
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-27T05:28:04.843643+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'DONE'}",
  "fields": "['exp_id', 'conclusion', 'metrics', 'completed_at']",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'DONE'}",
    "fields": "['exp_id', 'conclusion', 'metrics', 'completed_at']",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-27T05:28:39.871403+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 36.1317}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:pi05-crm-k2-long-s42-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 36359
}
```

</details>

---
