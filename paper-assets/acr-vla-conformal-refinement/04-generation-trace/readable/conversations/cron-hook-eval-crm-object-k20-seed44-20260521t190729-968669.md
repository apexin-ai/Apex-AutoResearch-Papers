# cron hook eval crm object k20 seed44 20260521T190729 968669

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 68
- **Recorded user turns:** 2
- **Tool calls:** 32
- **Original source:** `logs/chats/archive/cron_hook_eval-crm-object-k20-seed44_20260521T190729_968669.jsonl`
- **Structured JSON:** [`dede10abda8a7555a1df.json`](../../sessions/de/dede10abda8a7555a1df.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

66 recorded events

### User

_source line 1 · 2026-05-21T02:55:31.665543+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #23。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单必须查 `get_project_status` 的 `execution.gpu_ids`，不能假设。当前已知分配：bjb2-28827 和 bjb2-40593 上有卡在跑，具体白名单需 BOOT 后重新确认
- D084: eval-obs-only-object-norm02-seed42 (SR=20%) 已被 Director 决定**不纳入 Table 1**（异常高，疑似 outlier）
- CRM checkpoint 唯一路径：`/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`（所有服务器同路径）
- Object Table 1 锁定 norm02-only n=6 (16.8±1.8%)，不混入其他 norm 的结果（D080）
- Long OOD 已降级为 cautious wording（MW-U p=0.061 n.s.，D081）
- Adaptive K 是论文**核心贡献**（D077 用户硬要求），K=10 分析降为 supporting evidence

### 2. 🖥️ 基础设施快照
- **bjb2-28827**: `/root/acr-vla-conformal-refinement`, conda base (`/root/miniconda3/bin/python`), 磁盘 399G/439G 可用(5%)
- **bjb2-40593**: 同上结构, 磁盘 46G/437G 可用(90%) ⚠️ 极低
- **bjb1-18228**: 同上结构, 磁盘 400G/438G 可用(4%)
- **bjb1-32546**: 同上结构, 磁盘 400G/438G 可用(4%)
- 模型: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`
- HF cache: `/root/autodl-tmp/.hf_cache`, 离线模式 `HF_HUB_OFFLINE=1`
- 活跃进程: eval-obs-only-object-norm005-seed43 (bjb2-28827:cuda:4, PID 278354), eval-adaptive-k-spatial-p50-seed42 (bjb2-40593:cuda:0, PID 681823)

### 3. 📊 当前状态
Session 刚 BOOT，完成了 reconcile + registry 读取 + Worker 派发。

**RUNNING (2)**:
- `eval-obs-only-object-norm005-seed43` — CRM obs_only ε=0.05 Object seed43, plan_500 低 norm 补充
- `eval-adaptive-k-spatial-p50-seed42` — Spatial Adaptive K P50 seed42（ROADMAP 关键：Spatial P50 sweep 首个 seed）

**ANALYZING (4, 全部已派分析 Worker)**:
- `eval-crm-object-k20-seed44` — K=20 sweep seed44, plan_601
- `eval-adaptive-k-spatial-p25-seed43` — Spatial P25 seed43
- `eval-adaptive-k-spatial-p25-seed42` — Spatial P25 seed42
- `eval-obs-only-object-norm003-seed44` — ε=0.03 Object seed44, plan_500（retry，之前超时）

**等待 Worker 回调**: 5 个 Worker 在运行（3 个分析 + 1 个 mass-deploy + 1 个刚派的分析），回调到手后需汇总结果向 Director 汇报。

### 4. 📋 待办
- 4 个分析 Worker 回调 → 汇总指标、update_registry 到 DONE、刷新 report.md、向 Director 汇报（开头带 [资源] 行）
- eval-adaptive-k-spatial-p50-seed42 完成 → 分析结果，这是 **Spatial P50 关键数据点**（Object P50 = Pareto 最优 15.3% SR，Spatial 表现决定跨 benchmark 泛化 claim）
- mass-deploy Worker 回调 → 确认新实验是否成功部署，跟进 RUNNING 状态
- Spatial Adaptive K P50 seed43/seed44 需要部署（ROADMAP 待办）
- Random Selection baseline seed42/seed44（plan_600）待部署
- bjb2-40593 磁盘 90% → 提交新实验前必须先清理或换服务器

### 5. 🎯 战略上下文
- **CoRL 2026 DDL: 2026-05-29，剩 ~8 天**
- 核心 story: Adaptive K（K=2 L2 distance 信号，ρ=0.9979 vs K10 variance）自适应推理次数。P50 是 Pareto 最优（91% of K=10 SR, 77% fast-path）
- Object Adaptive K sweep 12/12 已 DONE ✅，现在需要 **Spatial Adaptive K sweep** 完成跨 benchmark 泛化证据
- 信号选择已 CLOSED: K=2 L2 distance 是唯一可用信号（CRM magnitude ρ=0.15 NO-GO, FMVD ρ=0.08 NO-GO）
- 决策链关键节点: D077(Adaptive K 升核心) → D078(P50 Pareto最优) → D079(CRM magnitude NO-GO) → D080(Table 1 norm02 n=6) → D081(Long OOD cautious) → D082(batched inference确认) → D083(Spatial CRM n=8) → D084(seed42 outlier不纳入)
- **易错点**: Spatial CRM K=10 baseline 是 34.4±1.5% (n=8, D083)，不要用旧数据。Object VLA-only baseline 10.9%，Object CRM norm02 16.8±1.8% (n=6, D080)
- ROADMAP 47 个 PREPARING 实验大多是 multi-seed supplement，优先级看 paper_framing.md 的 claim 需求

## 项目硬约束 (memory.md 节选)

## 失败模式记录

- [失败模式] Cron false positive：eval 脚本不写 W&B 也不写 sentinel file，进程正常退出后 cron 5 次检测找不到标记 → 自动标记为 failed。受影响：eval-vla-only-long-seed46, eval-vla-only-goal-seed46。修复方案：tail 日志确认实际完成 → 手动修正 conclusion=success + 补录 metrics。预防：eval 实验应检查 output JSON 是否存在作为 sentinel。

- [失败模式] Cron false positive（2026-05-20）：**eval-adaptive-k-spatial-p50-seed42** 被 cron 误判为 failed（"process dead 5× with no sentinel/W&B"）。实际情况：原 PID 675831 被 deploy worker kill 后，重启为 PID 681823。重启后进程正常运行，但 cron 监控未追踪到新 PID，5 次检测均未发现 sentinel → 自动标记 failed。诊断时（2026-05-20）PID 681823 仍在运行（状态 Rl+，已运行 17h36m），已完成 3/10 tasks（SR: 70%/100%/0%），第 4 个 task 进行中（rollout 5, 1/5 success）。GPU 使用 5972/24564 MiB，日志无错误。**无需重新提交，等待自然完成后手动修正 conclusion。**

- [失败模式] SIGHUP false failure（2026-05-20）：bjb2-28827 上多个实验 EXIT_CODE=129 (SIGHUP) 被标记 failed，实际全部完成。**已确认受影响：P75-seed44, P90-seed42, P25-seed44**。SIGHUP 发生在进程写完结果 JSON 之后（tmux session 断开或 SSH 连接清理）。**诊断方法：tail 日志看 "Results saved to" + "Overall success rate" 行 → 手动修正 conclusion=success 并补录 metrics。**

- [失败模式] Cron 日志路径不匹配（2026-05-20）：**eval-obs-only-goal-norm02-seed51** (bjb1-32546) 被 cron 误判 dead。根因：实验日志写入 `/root/acr-vla-conformal-refinement/logs/`（项目目录下），但 cron 监控在 `~/runs/acr-vla-conformal-refinement/` 下找日志 → 找不到 → 5 次检测均无 sentinel → auto-resolved failed。**教训：submit_training_job 的 log_path 必须与实际 tee 输出路径一致。部分实验用 `tee logs/xxx.log`（相对于 cd 后的项目目录），另一部分用 `~/runs/` 绝对路径，两套路径并存导致 cron 误判。**

- [失败模式] Cron false positive 批量（2026-05-20 诊断）：bjb1-32546 上 **eval-perdof-object-norm02-seed50** (PID 542405) 和 **eval-obs-only-object-norm02-seed51** (PID 542894) 被 cron 报告 "process gone, no sentinel, no W&B"。实际两者均已**正常完成**，output JSON 已写入。bjb1-18228 上 **eval-obs-only-object-norm005-seed44** 同样正常完成但被标记 failed。根因同上：eval 脚本不写 sentinel/W&B，进程正常退出后 cron 无法确认完成状态。结果：perdof-norm02-seed50 SR=10.0%, obs_only-norm02-seed51 SR=17.0%, obs_only-norm005-seed44 SR=12.0%。**均无需重跑，需手动修正 conclusion=success 并补录 metrics。**

- [失败模式] python PATH 不存在（2026-05-21, bjb1-32546）：`nohup: failed to run command 'python': No such file or directory`。bjb1-32546 使用 conda 环境，`python` 不在默认 PATH 中（仅 `/root/miniconda3/bin/python` 可用）。受影响：seed51-r2, seed52-r2, seed62, seed63（4 个实验同时失败）。**修复方案：提交命令前加 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&` 前缀。** 教训：submit_training_job 的 command 不能假设 `python` 在 PATH 中，必须自带环境激活。对照其他服务器（bjb1-18228、bjb2-28827）成功实验的命令格式，它们通过 `bash -c "source ... && python ..."` 包裹。

- [失败模式] FMVD 信号无效：ρ=0.0825 NO-GO。根因：denoising 空间统计量不映射到 action uncertainty。

- [失败模式] CRM correction magnitude 信号无效（2026-05-20）：ρ(K1_corr_mag, K10_var) = 0.1523 NO-GO。**根因：CRM correction magnitude 是常数 (~0.1205)，P25=P50=P75=P90 几乎相同。** CRM 对所有输入产出相同大小的修正向量——修正方向变化但幅度不变。推测因 max_correction_norm=0.2 的 clipping 使得大部分 correction 被截断到相同 norm。K=2 argmin 版本同样无效 (ρ=0.1340)。**教训：clipped norm 的信号没有方差，自然无法做 gate。**

- [失败模式] OpenVLA-7B eval timeout：timeout_hours 至少设 12h。

- [失败模式] Table 1 数据混淆（2026-05-20）：Table 1 原报 CRM Object K=10 = 17.6% (n=7)，实际来自 **norm01+norm02 混合数据**。seed42 只有 norm01 (0.19)，seed43 只有 norm02 (0.16)，两个 config 各自只有 n=6，合并后变 n=7。paper_provenance.yaml C029 引用的 exp_id 是抽象 "obs_only_k10" 而非具体实验 ID，导致问题没被及时发现。**教训：provenance 必须引用具体 registry_id，不用抽象标签。**

- [失败模式] evaluate.py 路径缺 src/ 前缀（2026-05-20）：adaptive_k spatial 实验命令用 `python evaluate.py` 而非 `python src/evaluate.py`，导致 EXIT_CODE=2 (No such file)。受影响：eval-adaptive-k-spatial-p50-seed43, eval-adaptive-k-spatial-p50-seed44（两台服务器 bjb1-32546, bjb2-28827 同时中招）。**教训：提交命令时对照历史成功实验的 command 格式，evaluate.py 在 src/ 子目录下。**

## 可查的历史
前 159 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-21T02:55:52.723536+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-21T02:55:52.774479+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T02:55:58.450761+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_registry reconcile_crons read_project_file read_roadmap",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_registry reconcile_crons read_project_file read_roadmap",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T02:55:58.747995+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "ToolSearch",
  "elapsed_ms": 297
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T02:56:02.987979+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'RUNNING'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'RUNNING'}"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T02:56:03.490424+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed44",
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

_source line 8 · 2026-05-21T02:56:03.517154+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T02:56:03.920927+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed44",
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

_source line 10 · 2026-05-21T02:56:04.310984+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T02:56:12.844015+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm003-seed67\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T02:54:48.643Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed67, norm sweep statistical robustness\"}, \"eval-obs-only-object-norm005-seed67\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T02:35:00.000Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.05 on LIBERO-Object seed67, norm sweep statistical robustness\"}, \"eval-obs-only-object-norm01-seed67\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T02:35:00.000Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.1 on LIBERO-Object seed67, norm sweep statistical robustness\"}, \"eval-pi05-baseline-object-seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T01:50:00.000Z\", \"updated_at\": \"2026-05-21T01:50:00.000Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42 — establishes reference success rate for flow-matching VLA, tests CRM applicability to second VLA backbone\"}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T01:48:00.000Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\"}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T01:48:00.000Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.05 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\"}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T01:48:00.000Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.1 on LIBERO
…[truncated 4344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 9856
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T02:56:23.237927+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-vla-only-object-seed49\": {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-19T21:15:12.591Z\", \"updated_at\": \"2026-05-21T02:56:05.638Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed49. Expanding VLA-only baseline seed coverage for Object benchmark.\", \"metrics\": {\"success_rate\": 0.1, \"total_rollouts\": 100, \"successful_rollouts\": 10}, \"conclusion\": \"success\"}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.2882}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 19747
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T02:57:35.297241+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 21, \"results\": [{\"exp_id\": \"eval-obs-only-object-norm003-seed64\", \"success\": true, \"actions\": [\"Skipped — pending escalation retry\"]}, {\"exp_id\": \"eval-obs-only-object-norm003-seed65\", \"success\": true, \"actions\": [\"Skipped — pending escalation retry\"]}, {\"exp_id\": \"eval-obs-only-object-norm01-seed64\", \"success\": true, \"actions\": [\"Skipped — pending escalation retry\"]}, {\"exp_id\": \"eval-obs-only-object-norm01-seed65\", \"success\": true, \"actions\": [\"Skipped — pending escalation retry\"]}, {\"exp_id\": \"eval-obs-only-object-norm005-seed64\", \"success\": true, \"actions\": [\"Skipped — pending escalation retry\"]}, {\"exp_id\": \"eval-obs-only-object-norm01-seed71\", \"success\": true, \"actions\": [\"Skipped — pending escalation retry\"]}, {\"exp_id\": \"eval-obs-only-object-norm005-seed72\", \"success\": true, \"actions\": [\"Skipped — pending escalation retry\"]}, {\"exp_id\": \"eval-obs-only-object-norm003-seed73\", \"success\": true, \"actions\": [\"Skipped — pending escalation retry\"]}, {\"exp_id\": \"eval-obs-only-object-norm01-seed74\", \"success\": true, \"actions\": [\"Skipped — pending escalation retry\"]}, {\"exp_id\": \"eval-obs-only-object-norm005-seed75\", \"success\": true, \"actions\": [\"Skipped — pending escalation retry\"]}, {\"exp_id\": \"eval-pi05-baseline-object-seed42\", \"success\": true, \"actions\": [\"Job still running (pid=802634)\"]}, {\"exp_id\": \"eval-obs-only-object-norm003-seed67\", \"success\": true, \"actions\": [\"Job still running (pid=969788)\"]}, {\"exp_id\": \"eval-obs-only-object-norm005-seed67\", \"success\": true, \"actions\": [\"Job still running (pid=805840)\"]}, {\"exp_id\": \"eval-obs-only-object-norm01-seed67\", \"success\": true, \"actions\": [\"Job still running (pid=666593)\"]}, {\"exp_id\": \"eval-obs-only-object-norm003-seed66\", \"success\": true, \"actions\": [\"Skipped (created 70s ago < interval 120s)\"]}, {\"exp
…[truncated 857 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 91780
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T02:57:35.361885+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval-obs-only-object-norm005-seed67 | obs_only CRM with epsilon=0.05 on LIBERO-Object seed67, norm sweep statistical robustness | — | — | — |\\n\\n## 待处理\\n- eval-obs-only-object-norm005-seed77（准备中）\\n- eval-obs-only-object-norm02-seed55: CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed55. Norm sweep seed balance.（准备中）\\n- …另有 34 项\\n\\n## 近期结论\\n- **eval-obs-only-object-norm005-seed65** (success): CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed65. Norm sweep seed balance for ε=0.05.\\n\\n## 趋势\\n成功 302 / 负向 38 / 失败 53 / 共 483\\nsuccess_rate: 0.14 ↓（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-18228: 无 GPU 信息\\nbjb1-32546: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\\nbjb2-28827: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\\nbjb2-40593: 无 GPU 信息\\n\\n## 告警\\n- plan_001-crm-smolvla: 训练失败 — unknown\\n- plan_014-reconvla-baseline: 训练失败 — unknown\\n- eval-smolvla-libero-spatial: 训练失败 — unknown\\n- eval-spatial-reeval-v2: 已被终止 — unknown\\n- precompute-v2-shard0: 已被终止 — unknown\\n- precompute-v2-shard1: 已被终止 — unknown\\n- precompute-v2-shard2: 已被终止 — unknown\\n- eval-spatial-v3-full: 已被终止 — unknown\\n- precompute-v3-shard0: 已被终止 — unknown\\n- precompute-v3-shard1: 已被终止 — unknown\\n- precompute-v3-shard2: 已被终止 — unknown\\n- eval-spatial-v4-full: 已被终止 — unknown\\n- eval-object-v4-full: 已被终止 — unknown\\n- eval-spatial-v5-full: 已被终止 — unknown\\n- crm-train-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v2: 已被终止 — unknown\\n- eval-acr-spatial-v1: 已被终止 — unknown\\n- crm-train-a3-obs-only: 已被终止 — unknown\\n- eval-acr-vla-spatial-v1: 已被终止 — unknown\\n- eval-spatial-v6-full: 
…[truncated 5075 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 91440
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T02:57:35.424868+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-21 00:48 UTC | 更新原因: D092-D095 updates: Plan A LOCKED, OpenVLA CRM CLOSED, π0.5/π added, GPU state corrected\\n\\n> 详见 paper_framing.md（D077: Adaptive K 核心, D088→D090→D092: Plan A GO）\\n\\n## 核心方向\\n**Adaptive inference-time compute for frozen VLAs** — K=2 L2 distance 作为不确定性信号，自适应决定推理策略（直出 vs CRM correction）。CRM correction>selection 分析作为支撑。\\n\\n## 投稿目标\\n**CoRL 2026** DDL **2026-05-29**。剩余 **8 天**。\\n\\n## 方法路径（D088→D092 最终）\\n- ❌ B (Learned Uncertainty Head): NO-GO, mean 12.0% < VLA-only (D090)\\n- ✅ **A (Plan A: K=2 Conformal + Selective CRM)**: Object 18.3%±2.1%, Spatial 35.0%±1.0% — **GO (D092/D094)**\\n- ⏳ C (Action Distribution Geometry): 不再需要，Plan A 已成功\\n\\n## Plan A 核心结果\\n| Benchmark | Plan A (K=2) | K=10 CRM | Δ vs K=10 | Compute |\\n|-----------|-------------|----------|-----------|---------|\\n| Object    | 18.3%±2.1%  | 16.8%    | +1.5pp    | 80% less (K=2 vs K=10) |\\n| Spatial   | 35.0%±1.0%  | 34.5%    | +0.5pp    | 80% less |\\n\\nPipeline: K=2 batched forward → d₂=‖a₁-a₂‖₂ → if d₂>τ: argmin-to-centroid + CRM; if d₂≤τ: direct output。\\n⚠️ Threshold calibration: flatten-L2 (30D) vs per-step-mean-L2 (7D×5) 差异 ~2.77×，当前 τ 在 Plan A scale 上 trigger rate 84%。待决：强调 K=2 效率 vs recalibrate Pareto sweep。\\n\\n## OpenVLA 实验线\\n- ✅ plan_801: OpenVLA v2 baseline SR=69%\\n- ✅ plan_802 train: CRM 训练完成 (val_loss=0.077260)\\n- ❌ **D093: OpenVLA CRM eval 0%** — near-deterministic (T=0.5, 8/10 identical actions)，applicability boundary，CLOSED\\n\\n## π0.5/π 实验线（D095，用户硬要求）\\n- 🔄 Phase 1: WebSearch + 下载模型（Agent 队列中）\\n- ⏳ Phase 2: env setup + baseline eval\\n- ⏳ Phase 3: 检查 action diversity → if stochastic: CRM pipeline\\n- 目的：第二/三个 VLA backbone（flow-matching），解决 M1 (narrow scope) + R2-W1-new (low absolute perf)\\n\\n## Norm Sweep 
…[truncated 3034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 91113
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T02:57:54.737389+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'DONE'}",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'DONE'}",
    "limit": "15"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T02:57:56.505829+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_project_resource_usage,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__save_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_project_resource_usage,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__save_project_file",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T02:58:02.060715+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm005-seed65\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:30:00.000Z\", \"updated_at\": \"2026-05-21T02:56:56.339Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed65. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"notes\": \"Cron false positive confirmed. Output JSON 已存在 (1490 bytes)，日志显示正常完成。Overall SR=14.0% (14/100)。进程已退出，无异常。\", \"metrics\": {\"success_rate\": 0.14, \"total_rollouts\": 100, \"successful_rollouts\": 14}}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:28:30.000Z\", \"updated_at\": \"2026-05-21T02:30:00.000Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}, \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed56. Norm sweep seed balance for ε=0.03.\"}, \"eval-obs-only-object-norm005-seed61\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:00:59.021Z\", \"updated_at\": \"2026-05-21T02:05:10.608Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"successful_rollouts\": 15, \"total_rollouts\": 100}, \"notes\": \"Cron false positive（第N次）：eval 脚本正常完成但不写 sentinel/W&B，被 cron 误判 failed。实际 SR=15.0% (15/100)。手动修正 conclusion=success。\", \"hypothesis\": \"CRM obs_only with max_correction_norm=0.05 (ε=0.05) on LIBERO-Object seed61 provides consistent improvement over VLA-only baseline, contributing to norm sweep statistical robustness for the ε=0.05 condition.\"}, \"eval-obs-only-object-norm005-seed58\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T23:18:18.450Z\", \"updated_at\": \"2026-05-21T01:25:14.143Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed58. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"notes\": \"Cron false positive: eval脚本不写W&B/sentinel，正常完成后被cron误判failed。实际SR=16.0%。\", \"metrics\": {\"success_rate\": 0.16, \"total_rollouts\": 100, \"successf
…[truncated 4576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 7323
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T02:58:02.061166+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "ToolSearch",
  "elapsed_ms": 5555
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T02:58:18.743682+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T02:58:18.833320+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "status": "running",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "status": "running",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T02:58:33.893829+00:00_

{"result":"{\"success\": true, \"data\": {\"allocated_gpus\": [], \"actually_running_gpus\": [{\"server\": \"bjb1-32546\", \"gpu_id\": \"cuda:0\", \"exp_id\": \"eval-obs-only-object-norm003-seed64\"}, {\"server\": \"bjb1-32546\", \"gpu_id\": \"cuda:1\", \"exp_id\": \"eval-obs-only-object-norm003-seed65\"}, {\"server\": \"bjb1-32546\", \"gpu_id\": \"cuda:3\", \"exp_id\": \"eval-obs-only-object-norm01-seed64\"}, {\"server\": \"bjb1-32546\", \"gpu_id\": \"cuda:4\", \"exp_id\": \"eval-obs-only-object-norm01-seed65\"}, {\"server\": \"bjb1-32546\", \"gpu_id\": \"cuda:5\", \"exp_id\": \"eval-obs-only-object-norm005-seed64\"}, {\"server\": \"bjb1-32546\", \"gpu_id\": \"cuda:0\", \"exp_id\": \"eval-obs-only-object-norm01-seed51-r3\"}, {\"server\": \"bjb1-32546\", \"gpu_id\": \"cuda:1\", \"exp_id\": \"eval-obs-only-object-norm01-seed52-r3\"}, {\"server\": \"bjb1-32546\", \"gpu_id\": \"cuda:4\", \"exp_id\": \"eval-obs-only-object-norm003-seed63-r2\"}, {\"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:0\", \"exp_id\": \"eval-obs-only-object-norm01-seed71\"}, {\"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:1\", \"exp_id\": \"eval-obs-only-object-norm005-seed72\"}, {\"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:2\", \"exp_id\": \"eval-obs-only-object-norm003-seed73\"}, {\"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:3\", \"exp_id\": \"eval-obs-only-object-norm01-seed74\"}, {\"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:4\", \"exp_id\": \"eval-obs-only-object-norm005-seed75\"}, {\"server\": \"bjb1-18228\", \"gpu_id\": \"cuda:0\", \"exp_id\": \"eval-obs-only-object-norm003-seed66\"}, {\"server\": \"bjb1-18228\", \"gpu_id\": \"cuda:2\", \"exp_id\": \"eval-obs-only-object-norm005-seed66\"}, {\"server\": \"bjb1-18228\", \"gpu_id\": \"cuda:3\", \"exp_id\": \"eval-obs-only-object-norm01-seed66\"}, {\"server\": \"bjb2-40593\", \"gpu_id\": \"cuda:0\", \"exp_id\": \"eval-pi05-baseline-object-seed42\"}, {\"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:5\", \"exp_id\": \"eval-obs-only-object-
…[truncated 3297 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "elapsed_ms": 15150
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T02:58:34.635997+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_diag_verify-nocron-running-L23_20260521T025235\", \"task_type\": \"diag:verify-nocron-running-L23\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-21T02:52:36.226508+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_diagnose_eval-vla-only-object-seed49_20260521T025247\", \"task_type\": \"diagnose:eval-vla-only-object-seed49\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-21T02:52:48.966901+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_diagnose_bjb1-18228-norm-seed65-fill_20260521T025446\", \"task_type\": \"diagnose:bjb1-18228-norm-seed65-fill\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-21T02:54:48.516848+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_diag_bjb1-32546-gpu-conflicts_20260521T025701\", \"task_type\": \"diag:bjb1-32546-gpu-conflicts\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-21T02:57:02.092523+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_diagnose_bjb1-32546-gpu-conflict_20260521T025803\", \"task_type\": \"diagnose:bjb1-32546-gpu-conflict\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-21T02:58:03.949047+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_diagnose_vla-only-object-seed49-analyzing_20260521T025811\", \"task_type\": \"diagnose:vla-only-object-seed49-analyzing\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-21T02:58:12.352444+00:00\", \"ended_at\": null}], \"count\": 6}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 15802
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T02:59:18.486970+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'RUNNING'}",
  "fields": "['exp_id', 'status', 'hypothesis', 'server', 'gpu']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'RUNNING'}",
    "fields": "['exp_id', 'status', 'hypothesis', 'server', 'gpu']"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T02:59:18.789211+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'DONE'}",
  "limit": "30",
  "fields": "['exp_id', 'status', 'conclusion', 'metrics', 'updated_at']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'DONE'}",
    "limit": "30",
    "fields": "['exp_id', 'status', 'conclusion', 'metrics', 'updated_at']"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T02:59:22.203339+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm005-seed67\": {\"status\": \"RUNNING\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed67. Norm sweep seed balance for ε=0.05.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\"}, \"eval-obs-only-object-norm003-seed67\": {\"status\": \"RUNNING\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed67, norm sweep statistical robustness\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\"}, \"eval-obs-only-object-norm01-seed67\": {\"status\": \"RUNNING\", \"hypothesis\": \"obs_only CRM with epsilon=0.1 on LIBERO-Object seed67, norm sweep statistical robustness\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\"}, \"eval-pi05-baseline-object-seed42\": {\"status\": \"RUNNING\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42 — establishes reference success rate for flow-matching VLA, tests CRM applicability to second VLA backbone\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\"}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"RUNNING\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\"}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"RUNNING\", \"hypothesis\": \"obs_only CRM with epsilon=0.05 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\"}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"RUNNING\", \"hypothesis\": \"obs_only CRM with epsilon=0.1 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\"}, \"eval-obs-only-object-norm01-seed71\": {\"status\": \"RUNNING\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed71. Norm sweep filling ε=0.1 gap.\"}, \"eval-obs-only-object-norm005-seed72\": {\"status\": \"RUNN
…[truncated 2079 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 3716
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T02:59:24.719041+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm003-seed63-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T02:58:58.549Z\", \"conclusion\": \"failed\"}, \"eval-vla-only-object-seed49\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T02:58:40.403Z\", \"metrics\": {\"success_rate\": 0.1, \"total_rollouts\": 100, \"successful_rollouts\": 10}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed62-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T02:58:07.615Z\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm005-seed65\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T02:56:56.339Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"total_rollouts\": 100, \"successful_rollouts\": 14}}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T02:30:00.000Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}}, \"eval-obs-only-object-norm005-seed61\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T02:05:10.608Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"successful_rollouts\": 15, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm005-seed58\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T01:25:14.143Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"total_rollouts\": 100, \"successful_rollouts\": 16}}, \"eval-obs-only-object-norm01-seed57\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T01:25:08.752Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.19, \"total_rollouts\": 100, \"successful_rollouts\": 19}}, \"eval-obs-only-object-norm003-seed59\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T01:25:04.366Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"total_rollouts\": 100, \"successful_rollouts\": 13}}, \"eval-obs-only-object-norm005-seed62\": {\"status\": \"DONE\", \"updated_at\": \"2026-05
…[truncated 3946 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 5929
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T02:59:44.671755+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-adaptive-k-spatial-p50-seed42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-adaptive-k-spatial-p50-seed42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T02:59:45.159393+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-obs-only-object-norm005-seed43'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-obs-only-object-norm005-seed43'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T02:59:45.999812+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-obs-only-object-norm003-seed63-r2'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-obs-only-object-norm003-seed63-r2'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-21T02:59:49.688437+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.9808}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 5016
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T02:59:53.666490+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.9252}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 8507
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-21T02:59:57.093880+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.4223}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 11094
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T03:00:06.535607+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "eval-adaptive-k-spatial-p50-seed42",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Grep",
  "tool_args": {
    "pattern": "eval-adaptive-k-spatial-p50-seed42",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T03:00:07.221428+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "eval-obs-only-object-norm005-seed43",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "glob": "*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Grep",
  "tool_args": {
    "pattern": "eval-obs-only-object-norm005-seed43",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
    "glob": "*.yaml"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T03:00:07.362675+00:00_

Found 1 file
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Grep",
  "elapsed_ms": 141
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-21T03:00:12.432851+00:00_

Found 113 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/feishu_group_oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/cron_hook_eval-crm-object-k20-seed44.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_diagnose_vla-only-object-seed49-analyzing_20260521T025811.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a_reviewer.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/cron_hook_eval-adaptive-k-spatial-p25-seed43.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/cron_hook_eval-adaptive-k-spatial-p75-seed42.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/cron_hook_eval-vla-only-long-seed49-r2.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/cron_hook_eval-adaptive-k-spatial-p25-seed42.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/cron_hook_eval-obs-only-object-norm003-seed43-r2.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/cron_hook_eval-crm-object-k20-seed43.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/task_context/agent.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/archive/cron_hook_e
…[truncated 15379 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Grep",
  "elapsed_ms": 5897
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T03:00:18.612581+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/checkpoints/eval-adaptive-k-spatial-p50-seed42_DONE_20260520T111317.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/checkpoints/eval-adaptive-k-spatial-p50-seed42_DONE_20260520T111317.json"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-21T03:00:18.949001+00:00_

1	{
2	  "exp_id": "eval-adaptive-k-spatial-p50-seed42",
3	  "project": "acr-vla-conformal-refinement",
4	  "state": "DONE",
5	  "previous_state": "RUNNING",
6	  "experiment_data": {
7	    "status": "DONE",
8	    "retry_count": 1,
9	    "created_at": "2026-05-20T06:01:50.026Z",
10	    "updated_at": "2026-05-20T11:13:15.994Z",
11	    "hypothesis": "Adaptive K with τ=P50 (0.074855, Object-calibrated) on LIBERO-Spatial seed42. 验证 Adaptive K 方法在第二个 benchmark 上的泛化：使用 Object 上校准的阈值直接应用到 Spatial（无 per-benchmark tuning）。如果 SR 接近 CRM K=10 (34.3%) 且 fast_path >50%，则证明方法跨 benchmark 通用。",
12	    "notes": "PID 681823 在 bjb2-40593:cuda:0 运行中 (State: R, 210 threads, 6483 MiB GPU)。旧 cron 检测旧 PID 675831 死亡后误标 DONE/failed，已恢复 RUNNING。第三次 cron 误报。",
13	    "reproduce": {
14	      "finished_at": "2026-05-20T11:13:08.990Z"
15	    },
16	    "failure_reason": "process dead 5× with no sentinel/W&B — auto-resolved as failed",
17	    "completed_at": "2026-05-20T07:29:59.173Z",
18	    "extra": {
19	      "hook_events": [
20	        {
21	          "event": "on_failed",
22	          "action": "agent",
23	          "ts": "2026-05-20T07:30:08.474411+00:00"
24	        }
25	      ],
26	      "previous_failure": {
27	        "conclusion": "failed",
28	        "notes": "旧PID 675831被kill后，新PID 681823已于cuda:0重新启动，运行正常(11min+)。旧cron检测到675831死亡触发误报回调。已完成3/10 tasks，SR: 70%/100%/0%，第4个task进行中。"
29	      }
30	    },
31	    "spec": {
32	      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.074855 --k_full 10 --benchmark spatial --seed 42 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p50_seed42.json\"",
33	      "server": "bjb2-40593",
34	      "gpu": [
3
…[truncated 336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Read",
  "elapsed_ms": 336
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T03:00:19.330477+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "eval-adaptive-k-spatial-p50-seed42:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "output_mode": "content",
  "-A": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Grep",
  "tool_args": {
    "pattern": "eval-adaptive-k-spatial-p50-seed42:",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "output_mode": "content",
    "-A": "15"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-21T03:00:19.391538+00:00_

15678:  eval-adaptive-k-spatial-p50-seed42:
15679-    status: DONE
15680-    retry_count: 1
15681-    created_at: '2026-05-20T06:01:50.026Z'
15682-    updated_at: '2026-05-20T11:13:15.994Z'
15683-    hypothesis: Adaptive K with τ=P50 (0.074855, Object-calibrated) on LIBERO-Spatial
15684-      seed42. 验证 Adaptive K 方法在第二个 benchmark 上的泛化：使用 Object 上校准的阈值直接应用到 Spatial（无
15685-      per-benchmark tuning）。如果 SR 接近 CRM K=10 (34.3%) 且 fast_path >50%，则证明方法跨 benchmark
15686-      通用。
15687-    notes: Reviewer 三次独立验证确认成功：JSON 完整，SR=30%，PID 自然退出。之前被 cron 误判为 failed（PID dead
15688-      + 无 sentinel）。
15689-    reproduce:
15690-      finished_at: '2026-05-20T11:13:08.990Z'
15691-    failure_reason: ''
15692-    completed_at: '2026-05-20T11:13:08.990Z'
15693-    metrics:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Grep",
  "elapsed_ms": 61
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-21T03:00:24.075456+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "eval-adaptive-k-spatial-p50-seed42:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "output_mode": "content",
  "-A": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Grep",
  "tool_args": {
    "pattern": "eval-adaptive-k-spatial-p50-seed42:",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "output_mode": "content",
    "-A": "40"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-21T03:00:24.141783+00:00_

15678:  eval-adaptive-k-spatial-p50-seed42:
15679-    status: DONE
15680-    retry_count: 1
15681-    created_at: '2026-05-20T06:01:50.026Z'
15682-    updated_at: '2026-05-20T11:13:15.994Z'
15683-    hypothesis: Adaptive K with τ=P50 (0.074855, Object-calibrated) on LIBERO-Spatial
15684-      seed42. 验证 Adaptive K 方法在第二个 benchmark 上的泛化：使用 Object 上校准的阈值直接应用到 Spatial（无
15685-      per-benchmark tuning）。如果 SR 接近 CRM K=10 (34.3%) 且 fast_path >50%，则证明方法跨 benchmark
15686-      通用。
15687-    notes: Reviewer 三次独立验证确认成功：JSON 完整，SR=30%，PID 自然退出。之前被 cron 误判为 failed（PID dead
15688-      + 无 sentinel）。
15689-    reproduce:
15690-      finished_at: '2026-05-20T11:13:08.990Z'
15691-    failure_reason: ''
15692-    completed_at: '2026-05-20T11:13:08.990Z'
15693-    metrics:
15694-      sr: 30
15695-      avg_K: 6.324
15696-      fast_path_pct: 45.95
15697-      mean_l2: 0.0903
15698-      total_rollouts: 100
15699-    extra:
15700-      hook_events:
15701-      - event: on_failed
15702-        action: agent
15703-        ts: '2026-05-20T07:30:08.474411+00:00'
15704-      - event: on_failed
15705-        action: agent
15706-        ts: '2026-05-20T11:13:27.036083+00:00'
15707-      previous_failure:
15708-        conclusion: failed
15709-        notes: '旧PID 675831被kill后，新PID 681823已于cuda:0重新启动，运行正常(11min+)。旧cron检测到675831死亡触发误报回调。已完成3/10
15710-          tasks，SR: 70%/100%/0%，第4个task进行中。'
15711-    spec:
15712-      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
15713-        base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache
15714-        HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py
15715-        --mode adaptive_k --adaptive_threshold 0.074855 --k_full 10 --benchmark spatial
15716-        --seed 42 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt
15717-        --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p50_see
…[truncated 40 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Grep",
  "elapsed_ms": 66
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-21T03:01:19.342561+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-21T03:01:19.471542+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_9d29ee7f.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Read",
  "elapsed_ms": 128
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-21T03:01:22.270434+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-21T03:01:22.488221+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Glob",
  "elapsed_ms": 217
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-21T03:01:25.000761+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation*",
  "path": "/home/ubuntu/agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation*",
    "path": "/home/ubuntu/agent-ml-research"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-21T03:01:26.713309+00:00_

/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Glob",
  "elapsed_ms": 1712
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-21T03:01:29.365524+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-21T03:01:29.432118+00:00_

1	---
2	name: resource-saturation
3	description: "当你准备向 Director 汇报前、收到 cron/worker 回调、审批通过准备开跑、怀疑 Worker 池不够饱和时,立即使用本 skill。四部分:A) GPU 分配率(分配了没跑=失职) B) GPU 效率 C) 非 GPU 任务并行(Worker 池<2=失职) D) 汇报必须带 [资源] 行。"
4	always: false
5	roles:
6	  - director
7	  - agent
8	---
9	
10	# 资源饱和度自检（硬约束）
11	
12	## A. GPU 分配率检查
13	
14	调 `get_project_resource_usage(project)` 看:
15	- 已分配给本项目的 GPU 总数和具体卡号
16	- 实际在跑任务的 GPU 数和具体卡号（交叉 registry RUNNING + nvidia-smi 进程）
17	- 分配了但没跑的 GPU 清单 ⚠️
18	
19	任何"分配了但没跑"的 GPU = 失职。必须立即:
20	- 派 Worker 铺 dry-run / 下一批实验代码准备
21	- 铺 ablation（从 experiment-matrix 空白格子里挑）
22	- 确实无实验可铺 → 向 Director 汇报"暂无可铺实验"+ 建议下一步方向(扩 ablation 维度 / 加 baseline / 加 benchmark)。**不要建议归还 GPU**——项目级 GPU 归还只在归档时由 `archive_project` 自动触发, 不是 Director 中途的动作
23	
24	**单实验不占多卡**: 分配 4 卡但实验只用 1 卡 → 另 3 卡必须并行跑其他实验,不能空占。
25	
26	## B. GPU 效率检查
27	
28	调 `get_gpu_health(server)`:
29	- 空闲 GPU（util < 10% 持续 > 5 min）→ 立即铺任务
30	- 低利用率（util < 50% 持续 > 15 min）→ spawn_worker 诊断（batch / IO / 同步）
31	- OOM 风险（显存 > 90% 持续 10 min）→ 主动降 batch / 调优
32	
33	## C. 非 GPU 任务并行
34	
35	GPU 在跑 ≠ 你空闲。以下 CPU / 网络任务**必须**派独立 Worker 并行:
36	- 下一批实验的数据集下载 / 预处理 / fingerprint
37	- 下一批实验的代码准备 / dry-run / 环境配置
38	- 论文文献调研 / related work 检索
39	- 已完成实验的 log 深度分析 / metric 聚合
40	- 论文章节起草
41	- 代码 review / refactor
42	
43	**硬约束**: 任一时刻 Worker 池 < 2 个 = 失职（除非真的全部下游阻塞在等 GPU,这时应当向 Director 申请扩 GPU）。
44	
45	## D. 汇报格式
46	
47	向 Director 汇报时开头必须带资源声明行:
48	
49	    [资源] GPU 分配 N / 实际在跑 M | Worker 池 K (其中 GPU 任务 A / CPU 任务 B)
50	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Read",
  "elapsed_ms": 66
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-21T03:01:43.807528+00:00_

called mcp__agent-ml-research__load_project_config

<details open><summary>🔧 Tool call — mcp__agent-ml-research__load_project_config</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "section": "execution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__load_project_config",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "section": "execution"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-21T03:01:43.912407+00:00_

Error executing tool load_project_config: 1 validation error for load_project_configArguments
project_name
  Field required [type=missing, input_value={'project': 'acr-vla-conf... 'section': 'execution'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 104
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-21T03:01:46.579480+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__load_project_config",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__load_project_config",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-21T03:01:46.634834+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "ToolSearch",
  "elapsed_ms": 55
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-21T03:01:49.769490+00:00_

called mcp__agent-ml-research__load_project_config

<details open><summary>🔧 Tool call — mcp__agent-ml-research__load_project_config</summary>

```json
{
  "project_name": "acr-vla-conformal-refinement",
  "section": "execution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__load_project_config",
  "tool_args": {
    "project_name": "acr-vla-conformal-refinement",
    "section": "execution"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-21T03:01:49.875459+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"acr-vla-conformal-refinement\", \"section\": \"execution\", \"config\": {\"execution\": {\"account\": \"root\", \"gpu_constraint\": [\"autodl-4090:cuda:0\"], \"gpu_ids\": [\"bjb2-40593:cuda:0\", \"bjb1-18228:cuda:0\", \"bjb1-18228:cuda:1\", \"bjb1-18228:cuda:2\", \"bjb1-18228:cuda:3\", \"bjb1-32546:cuda:0\", \"bjb1-32546:cuda:1\", \"bjb1-32546:cuda:2\", \"bjb1-32546:cuda:3\", \"bjb1-32546:cuda:4\", \"bjb1-32546:cuda:5\", \"bjb2-28827:cuda:0\", \"bjb2-28827:cuda:1\", \"bjb2-28827:cuda:2\", \"bjb2-28827:cuda:3\", \"bjb2-28827:cuda:4\", \"bjb2-28827:cuda:5\"], \"project_path\": \"/root/acr-vla-conformal-refinement\", \"servers\": [\"bjb2-40593\", \"bjb1-18228\", {\"account\": \"root\", \"server\": \"bjb1-32546\"}, {\"account\": \"root\", \"server\": \"bjb2-28827\"}]}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 105
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-21T03:02:40.424529+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "text": "[资源] GPU 17/17 全部在跑（含 bjb1-32546 上 3 个 GPU 冲突待解） | Worker 6 (GPU 2 / CPU 4) | 磁盘: bjb2-40593 90% ⚠️\n\n**Session #23 BOOT 状态报告**\n\n**RUNNING (19)**:\n- **π0.5 baseline** (eval-pi05-baseline-object-seed42): bjb2-40593:cuda:0，D095 关键实验，进行中\n- **Norm sweep 18 个实验**: ε=0.03 (seed62-r2→67), ε=0.05 (seed64→72), ε=0.1 (seed51-r3→74) 跨 bjb1-18228/bjb1-32546/bjb2-28827\n\n**刚完成**:\n- eval-vla-only-object-seed49: SR=10% (VLA-only baseline，与已知 10.9% 一致)\n\n**GPU 冲突 ⚠️**:\n- bjb1-32546 cuda:0/1/4 各有 2 个实验共享 GPU（seed64/65 + retry seed51-r3/52-r3/63-r2）\n- 根因: 前轮部署 retry 时未检查 GPU 占用\n- 6 个诊断 Worker 正在检查实际进程状态，回调后解决冲突\n\n**Cron**: 10 个实验 \"pending escalation retry\"——全部确认实际在跑（GPU 有进程），是已知的 eval 脚本无 sentinel 导致的 false positive 模式\n\n**空闲 GPU**: 0（17/17 全占）。bjb1-18228 cuda:4/5 和 bjb2-40593 cuda:1-5 不在白名单内\n\n**下一步**:\n1. 等待 6 个诊断 Worker 回调 → 解决 GPU 冲突（可能 kill 较新的 retry 实验）\n2. π0.5 baseline 完成后立即分析（D095 关键）\n3. Norm sweep 批量完成后汇总 ε=0.03/0.05/0.1 统计并生成 Figure 2 数据"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "text": "[资源] GPU 17/17 全部在跑（含 bjb1-32546 上 3 个 GPU 冲突待解） | Worker 6 (GPU 2 / CPU 4) | 磁盘: bjb2-40593 90% ⚠️\n\n**Session #23 BOOT 状态报告**\n\n**RUNNING (19)**:\n- **π0.5 baseline** (eval-pi05-baseline-object-seed42): bjb2-40593:cuda:0，D095 关键实验，进行中\n- **Norm sweep 18 个实验**: ε=0.03 (seed62-r2→67), ε=0.05 (seed64→72), ε=0.1 (seed51-r3→74) 跨 bjb1-18228/bjb1-32546/bjb2-28827\n\n**刚完成**:\n- eval-vla-only-object-seed49: SR=10% (VLA-only baseline，与已知 10.9% 一致)\n\n**GPU 冲突 ⚠️**:\n- bjb1-32546 cuda:0/1/4 各有 2 个实验共享 GPU（seed64/65 + retry seed51-r3/52-r3/63-r2）\n- 根因: 前轮部署 retry 时未检查 GPU 占用\n- 6 个诊断 Worker 正在检查实际进程状态，回调后解决冲突\n\n**Cron**: 10 个实验 \"pending escalation retry\"——全部确认实际在跑（GPU 有进程），是已知的 eval 脚本无 sentinel 导致的 false positive 模式\n\n**空闲 GPU**: 0（17/17 全占）。bjb1-18228 cuda:4/5 和 bjb2-40593 cuda:1-5 不在白名单内\n\n**下一步**:\n1. 等待 6 个诊断 Worker 回调 → 解决 GPU 冲突（可能 kill 较新的 retry 实验）\n2. π0.5 baseline 完成后立即分析（D095 关键）\n3. Norm sweep 批量完成后汇总 ε=0.03/0.05/0.1 统计并生成 Figure 2 数据"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-21T03:02:52.959390+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 12534
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-21T03:03:06.414674+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "eval-obs-only-object-norm005-seed43:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "output_mode": "content",
  "-A": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Grep",
  "tool_args": {
    "pattern": "eval-obs-only-object-norm005-seed43:",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "output_mode": "content",
    "-A": "20"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-21T03:03:06.486583+00:00_

7459:  eval-obs-only-object-norm005-seed43:
7460-    status: DONE
7461-    retry_count: 2
7462-    created_at: '2026-05-17T13:32:15.980Z'
7463-    updated_at: '2026-05-20T17:24:01.628Z'
7464-    hypothesis: 'CRM obs_only ε=0.05 on Object seed43. Low-norm multi-seed supplement
7465-      (plan_500): strengthens Figure 2 error bars at small ε.'
7466-    notes: Superseded by eval-obs-only-object-norm005-seed43-r2 (bjb1-32546) and r3
7467-      (bjb1-18228)
7468-    completed_at: '2026-05-17T23:17:56.045Z'
7469-    extra:
7470-      previous_failure:
7471-        conclusion: success
7472-        metrics:
7473-          sr: 0.13
7474-          total: 100
7475-          successes: 13
7476-          benchmark: object
7477-          mode: crm_obs_only
7478-        notes: Superseded by eval-obs-only-object-norm005-seed43-r2 (bjb1-32546) and
7479-          r3 (bjb1-18228)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Grep",
  "elapsed_ms": 71
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-21T03:03:13.022515+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "eval-crm-object-k20-seed44:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "output_mode": "content",
  "-A": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Grep",
  "tool_args": {
    "pattern": "eval-crm-object-k20-seed44:",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "output_mode": "content",
    "-A": "10"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-21T03:03:13.466296+00:00_

16448:  eval-crm-object-k20-seed44:
16449-    status: DONE
16450-    retry_count: 0
16451-    created_at: '2026-05-20T08:47:49.745Z'
16452-    updated_at: '2026-05-20T10:51:11.900Z'
16453-    hypothesis: 'CRM obs_only K=20 on Object seed44. K-value sweep third seed (plan_601):
16454-      tests K=20 vs K=10 compute tradeoff.'
16455-    spec:
16456-      command: bash -c "... python -u src/evaluate.py --mode crm_obs_only --benchmark
16457-        object --seed 44 --n_rollouts 10 --K 20 --max_correction_norm 0.2 ..."
16458-      server: bjb2-28827

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Grep",
  "elapsed_ms": 443
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-21T03:03:13.745640+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "eval-adaptive-k-spatial-p25-seed4[23]:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "output_mode": "content",
  "-A": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Grep",
  "tool_args": {
    "pattern": "eval-adaptive-k-spatial-p25-seed4[23]:",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "output_mode": "content",
    "-A": "10"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-21T03:03:13.803597+00:00_

16169:  eval-adaptive-k-spatial-p25-seed42:
16170-    status: DONE
16171-    retry_count: 0
16172-    created_at: '2026-05-20T08:02:47.126Z'
16173-    updated_at: '2026-05-20T10:52:54.947Z'
16174-    hypothesis: 'Adaptive K with τ=P25 (0.054959, Object-calibrated) on LIBERO-Spatial
16175-      seed42. Cross-benchmark threshold sweep: P25 keeps ~65% fast-path on Object,
16176-      testing transfer to Spatial.'
16177-    spec:
16178-      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
16179-        base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache
--
16339:  eval-adaptive-k-spatial-p25-seed43:
16340-    status: DONE
16341-    retry_count: 0
16342-    created_at: '2026-05-20T08:19:55.884Z'
16343-    updated_at: '2026-05-20T10:51:17.226Z'
16344-    hypothesis: Adaptive K with P25 threshold (τ=0.054959) on LIBERO-Spatial will
16345-      maintain competitive SR compared to K=10 baseline while reducing average inference
16346-      cost by using fewer refinement steps when the model is confident.
16347-    spec:
16348-      command: bash -c "... python -u src/evaluate.py --mode adaptive_k --adaptive_threshold
16349-        0.054959 --k_full 10 --benchmark spatial --seed 43 ..."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "tool": "Grep",
  "elapsed_ms": 57
}
```

</details>

---

### Assistant

_source line 66 · 2026-05-21T03:03:23.530597+00:00_

Session-start 初始化完成。

**状态总结：**
- 19 个实验 RUNNING（18 norm sweep + 1 π0.5 baseline），17/17 分配 GPU 全占
- bjb1-32546 上 3 个 GPU 冲突（cuda:0/1/4 各 2 个实验），6 个诊断 Worker 正在处理
- handoff 提到的 ANALYZING 实验（K20-seed44、P25-seed42/43）均已在前轮处理为 DONE
- eval-adaptive-k-spatial-p50-seed42 已 DONE（SR=30%, avg_K=6.324, fast_path=46%）
- Director 已收到 Session #23 状态报告

等待 6 个诊断 Worker 回调，届时处理 GPU 冲突并推进。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-crm-object-k20-seed44"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 67 · 2026-05-21T19:05:59.438042+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed44",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 68 · 2026-05-21T19:07:29.965732+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单（`execution.gpu_ids`）：bjb2-40593:cuda:0 | bjb1-18228:cuda:0-3 | bjb1-32546:cuda:0-5 | bjb2-28827:cuda:0-5（共 17 张，**不含** bjb1-18228:cuda:4/5 和 bjb2-40593:cuda:1-5）
- D084: eval-obs-only-object-norm02-seed42 (SR=20%) **不纳入 Table 1**（疑似 outlier）
- CRM checkpoint 唯一路径：`/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`
- Object Table 1 锁定 norm02-only n=6 (16.8±1.8%)，不混入其他 norm 的 D080 数据
- Long OOD 降级 cautious wording（MW-U p=0.061 n.s.，D081）
- Adaptive K 是论文**核心贡献**（D077 用户硬要求）
- bjb1-32546 上 GPU 冲突：cuda:0/1/4 各有 2 个实验共享——前轮部署 retry 时未检查占用导致，6 个诊断 Worker 已派出但回调未到

### 2. 🖥️ 基础设施快照
- **bjb2-28827**: `/root/acr-vla-conformal-refinement`, conda base (`/root/miniconda3/bin/python`), 6 GPU 全占（norm seed71-75 + norm003-seed67）
- **bjb1-32546**: 同上结构, 6 GPU 全占（含 3 对冲突：seed64/65 vs retry seed51-r3/52-r3/63-r2）
- **bjb1-18228**: 同上结构, 4 GPU 占（cuda:0-3: seed66 三个 norm + norm01-seed67），cuda:4/5 不在白名单
- **bjb2-40593**: 同上结构, cuda:0 跑 π0.5 baseline，磁盘 90% ⚠️，cuda:1-5 不在白名单
- 模型: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`
- HF cache: `/root/autodl-tmp/.hf_cache`, 离线模式 `HF_HUB_OFFLINE=1`

### 3. 📊 当前状态
Session #23 BOOT 完成：read_registry + reconcile_crons + ROADMAP 读取 + Director 汇报已发。

**RUNNING (19)**:
- **eval-pi05-baseline-object-seed42** — π0.5 VLA-only baseline（D095 关键，bjb2-40593:cuda:0）
- **Norm sweep ×18**: ε=0.03 (seed62-r2 已 fail, seed64/65/66/67/73), ε=0.05 (seed64/66/67/72/75), ε=0.1 (seed51-r3/52-r3/64/65/66/67/71/74)

**刚完成**:
- eval-vla-only-object-seed49: DONE SR=10%（VLA-only baseline，一致）
- eval-obs-only-object-norm003-seed62-r2 / seed63-r2: DONE(failed)——需查原因

**等待回调**: 6 个诊断 Worker（verify-nocron-running, vla-only-seed49-analyzing, bjb1-18228-seed65-fill, bjb1-32546-gpu-conflicts ×2, vla-only-seed49-analyzing-2）——全部由前轮 02:52-02:58 UTC 派出

**Cron**: 10 个实验 "pending escalation retry"——全部确认在跑，是 eval 无 sentinel 的 false positive

### 4. 📋 待办
- 6 个诊断 Worker 回调到达 → 处理 GPU 冲突（大概率需 kill bjb1-32546 上较新的 retry 实验 seed51-r3/52-r3/63-r2），释放后重新部署到不冲突的 GPU
- eval-pi05-baseline-object-seed42 完成 → 分析 SR，如果 >60% 且 action stochastic → D095 CRM pipeline GO，如果 deterministic 如 OpenVLA → CLOSED
- norm sweep 批量完成 → 汇总 ε=0.03/0.05/0.1 统计（目标各 n≥6），更新 Figure 2 数据
- seed62-r2 / seed63-r2 失败 → 查原因，可能需要再次 retry 到无冲突 GPU
- Director 回复 → 按指示行动

### 5. 🎯 战略上下文
- **CoRL 2026 DDL: 2026-05-29，剩 ~8 天**
- 核心 story: Adaptive K（K=2 L2 distance，ρ=0.9979）自适应推理。Plan A LOCKED: Object 18.3%±2.1%, Spatial 35.0%±1.0%
- 信号选择 CLOSED: K=2 L2 distance 唯一可用（CRM magnitude ρ=0.15 NO-GO, FMVD ρ=0.08 NO-GO）
- **Spatial Adaptive K P50 已完成**: seed42 SR=30%, avg_K=6.324, fast_path=46%——显著低于 K=10 CRM 34.5%，P50 在 Spatial 上不是 Pareto 最优（Object 上是）
- OpenVLA CRM CLOSED (D093, 0% SR, near-deterministic)
- π0.5 baseline 正在跑（D095/D096），是解决 M1 (narrow scope) 的关键路径
- 决策链: D077→D078→D079→D080→D081→D082→D083→D084→D088→D090→D092→D093→D094→D095→D096
- **易错点**: (1) bjb1-32546 GPU 冲突未解决前不要再往上面部署 (2) Spatial CRM K=10 baseline 是 34.4±1.5% (n=8, D083) 不要用旧数据 (3) 10 个 cron "pending escalation" 不是真的 failed，不要重跑 (4) eval 脚本不写 sentinel/W&B，几乎所有 cron 完成检测都是 false positive——确认 output JSON 存在即可判定成功
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-crm-object-k20-seed44"
}
```

</details>

---
