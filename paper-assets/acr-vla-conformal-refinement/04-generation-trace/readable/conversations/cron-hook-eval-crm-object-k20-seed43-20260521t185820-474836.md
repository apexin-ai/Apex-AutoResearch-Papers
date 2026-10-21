# cron hook eval crm object k20 seed43 20260521T185820 474836

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 2
- **Tool calls:** 17
- **Original source:** `logs/chats/archive/cron_hook_eval-crm-object-k20-seed43_20260521T185820_474836.jsonl`
- **Structured JSON:** [`adb33cd52cd65444dfef.json`](../../sessions/ad/adb33cd52cd65444dfef.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-21T02:44:34.684981+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #23。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单严格按 `get_project_status` 的 `execution.gpu_ids`，即使 Director 指令用白名单外 GPU 也必须 push back
- Object CRM K=10 Table 1 只用 norm02 数据（D080），seed42 的 SR=20% 不纳入（D084 决策）
- Spatial CRM K=10 用 clean n=8 数据 34.4±1.5%（D083），不要引用旧的 n=7
- Long OOD 只能用 cautious wording（MW-U p=0.061 n.s.，D081）
- evaluate.py 使用 batched inference（D082），延迟表和效率 claim 必须与此一致
- CRM checkpoint 路径: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: 6× RTX 4090, root, 工作目录 ~/runs/acr-vla-conformal-refinement/
- **bjb1-32546**: 6× RTX 4090, root, 同上
- **bjb2-28827**: 6× RTX 4090, root, 同上
- **bjb2-40593**: GPU 信息待确认, root, 同上
- Python: 各服务器用 conda（`source /root/miniconda3/bin/activate`），不要假设 .venv
- 代码仓库: 各服务器 ~/acr-vla-conformal-refinement/（含 src/evaluate.py）
- W&B: 可用，cron 回调说 "W&B data available"
- 总计 17× RTX 4090 across 4 servers

### 3. 📊 当前状态
**刚做完**: session-start 初始化（read_registry + reconcile_crons + read report/ROADMAP）。收到 eval-crm-object-k20-seed43 完成回调。

**已有 Worker 结果（上一轮 spawn 的）**:
- eval-crm-object-k20-seed43: **DONE/success, SR=18.0%**（K=20 vs K=10 16.8% 仅 +1.2pp，边际收益可忽略）

**已派 Worker（本轮 spawn，等回调）**:
- `worker_analyze_bjb1-18228-batch_20260520T103655`: 分析 eval-crm-object-k20-seed42 / eval-adaptive-k-spatial-p75-seed42 / eval-vla-only-long-seed49-r2
- `worker_analyze_bjb1-32546-batch_20260520T103702`: 分析 eval-adaptive-k-spatial-p75-seed43 / eval-obs-only-object-norm003-seed43-r2 / eval-obs-only-object-norm005-seed44

**RUNNING 实验**:
- eval-crm-object-k20-seed44 (bjb2-28827) — K=20 sweep 第3 seed
- eval-adaptive-k-spatial-p50-seed42 (bjb2-40593) — Spatial Adaptive K P50 首 seed
- eval-adaptive-k-spatial-p25-seed42 (bjb1-18228) — Spatial P25
- eval-adaptive-k-spatial-p25-seed43 (bjb1-32546) — Spatial P25 seed43
- eval-obs-only-object-norm005-seed44 (bjb1-32546) — 可能刚完成转 ANALYZING
- eval-obs-only-object-norm003-seed43-r2 (bjb1-32546) — 同上

**QUEUED**: eval-obs-only-object-norm003-seed44, eval-obs-only-object-norm005-seed43 (bjb2-28827)

**未汇报 Director**: 本轮还没来得及汇报。需要等两个 batch Worker 回调后汇总所有结果一起报。

### 4. 📋 待办
- Worker bjb1-18228-batch 回调 → 汇总 K=20 seed42 + Spatial P75 seed42 + Long VLA-only seed49-r2 结果
- Worker bjb1-32546-batch 回调 → 汇总 Spatial P75 seed43 + norm003/norm005 结果
- 两个 Worker 都回来后 → 向 Director 汇报（开头带 [资源] 行），内容包括:
  - K=20 sweep 汇总（seed42/43 结果 + seed44 还在跑）→ 预判 K=20 边际收益很小
  - Spatial Adaptive K P75 cross-benchmark 结果
  - plan_500 低 norm 补充数据点
  - Long VLA-only seed49-r2 确认
- eval-crm-object-k20-seed44 完成 → 完成 K=20 sweep 三 seed 汇总，如果都是 ~18% 则结论: K=20 不值得
- Spatial Adaptive K P50 seed42 完成 → 开始 Spatial P50 三 seed 汇总（核心贡献数据）
- **ROADMAP 待部署任务**（需 Director 确认 GPU 分配后执行）:
  - Spatial Adaptive K P50 seed43, seed44
  - Random Selection baseline seed42, seed44 (plan_600)
  - CRM Object K=10 norm02 seed42（Table 1 n=6→n=7）
  - fig3_kvalue 重新生成

### 5. 🎯 战略上下文
- **CoRL 2026 DDL: 2026-05-29，剩 ~8 天**
- **D077（用户硬要求）**: Adaptive K = 论文核心贡献，K=10 分析降为 supporting evidence
- **核心信号**: K=2 L2 distance（ρ=0.9979 vs K10_var），CRM magnitude 和 FMVD 都 NO-GO
- **P50 = Pareto 最优**（D078）: SR 15.3%, avg_K ~3.8, fast_path ~77%, vs K=10 ~91% 性能保留
- Object Adaptive K sweep 12/12 已全部 DONE，现在在做 **Spatial cross-benchmark** 验证
- K=20 sweep 初步结论: seed43 SR=18.0% vs K=10 16.8%，仅 +1.2pp，边际收益可忽略——如果 seed42/44 也类似，K=20 作为 supporting evidence 写入附录即可
- **易错点**: Spatial 实验用的 threshold 是 Object-calibrated 的（τ=P50 0.07246, P75 0.098735），cross-benchmark transfer 是论文的一个 claim，结果好坏直接影响 story strength
- **论文 CRITICAL 待解决**: evaluate.py 推理模式确认(P0)、Spatial n=8 溯源、OOD 全量更新、P25 n=3 更新
- 决策链: D075(FMVD NO-GO) → D076(K=2 L2 GO) → D077(Adaptive K 升核心) → D078(P50 Pareto) → D079(CRM mag NO-GO) → D080(Table1 norm02) → D081(Long OOD cautious) → D082(batched inference) → D083(Spatial n=8 clean) → D084(seed42 SR=20% 排除)

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
前 154 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-21T02:44:50.226692+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed43",
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

_source line 3 · 2026-05-21T02:44:50.277338+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T02:44:53.676376+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed43",
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

_source line 5 · 2026-05-21T02:44:54.992072+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed43",
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

_source line 6 · 2026-05-21T02:44:55.238636+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed43",
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

_source line 7 · 2026-05-21T02:44:55.239060+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T02:44:56.137377+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed43",
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

_source line 9 · 2026-05-21T02:44:56.137798+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T02:45:03.637852+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-pi05-baseline-object-seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T01:50:00.000Z\", \"updated_at\": \"2026-05-21T01:50:00.000Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42 — establishes reference success rate for flow-matching VLA, tests CRM applicability to second VLA backbone\"}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T01:48:00.000Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\"}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T01:48:00.000Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.05 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\"}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T01:48:00.000Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.1 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\"}, \"eval-obs-only-object-norm01-seed71\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T00:55:00.000Z\", \"updated_at\": \"2026-05-21T00:55:00.000Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed71. Norm sweep filling ε=0.1 gap.\"}, \"eval-obs-only-object-norm005-seed72\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T00:55:00.000Z\", \"updated_at\": \"2026-05-21T00:55:00.000Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed72. Norm sweep seed balance.\"}, \"eval-obs-only-object-norm003-seed73\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T00:55:00.000Z\", \"updated_at\": \"2026-05-21T00:55:00.000Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Obje
…[truncated 3533 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 9961
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T02:45:14.052628+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-vla-only-object-seed49\": {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-19T21:15:12.591Z\", \"updated_at\": \"2026-05-20T17:54:33.055Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed49. Expanding VLA-only baseline seed coverage for Object benchmark.\"}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.2744}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 19060
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T02:45:26.774564+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.5977}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 31535
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T02:50:17.010115+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 11, \"results\": [{\"exp_id\": \"eval-obs-only-object-norm003-seed64\", \"success\": true, \"actions\": [\"Job still running (pid=723784)\"]}, {\"exp_id\": \"eval-obs-only-object-norm003-seed65\", \"success\": true, \"actions\": [\"Job still running (pid=725722)\"]}, {\"exp_id\": \"eval-obs-only-object-norm01-seed64\", \"success\": true, \"actions\": [\"Job still running (pid=726800)\"]}, {\"exp_id\": \"eval-obs-only-object-norm01-seed65\", \"success\": true, \"actions\": [\"Job still running (pid=728057)\"]}, {\"exp_id\": \"eval-obs-only-object-norm005-seed64\", \"success\": true, \"actions\": [\"Job still running (pid=729873)\"]}, {\"exp_id\": \"eval-obs-only-object-norm01-seed71\", \"success\": true, \"actions\": [\"Job still running (pid=922504)\"]}, {\"exp_id\": \"eval-obs-only-object-norm005-seed72\", \"success\": true, \"actions\": [\"Job still running (pid=922712)\"]}, {\"exp_id\": \"eval-obs-only-object-norm003-seed73\", \"success\": true, \"actions\": [\"Job still running (pid=922982)\"]}, {\"exp_id\": \"eval-obs-only-object-norm01-seed74\", \"success\": true, \"actions\": [\"Job still running (pid=923256)\"]}, {\"exp_id\": \"eval-obs-only-object-norm005-seed75\", \"success\": true, \"actions\": [\"Job still running (pid=923398)\"]}, {\"exp_id\": \"eval-pi05-baseline-object-seed42\", \"success\": true, \"actions\": [\"Job still running (pid=802634)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 321771
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T02:50:17.062913+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-21T02:36:32Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 541 个实验 — ANALYZING 1, DEPLOYED 5, DONE 482, PREPARING 34, RUNNING 19\\n**DONE 分布**: failed 54, killed 90, negative 38, success 300\\n\\n### GPU 占用\\n- **实际运行**: 19 张 — bjb2-28827:cuda:2(eval-obs-only-object-norm003-seed56), bjb1-32546:cuda:0(eval-obs-only-object-norm003-seed64), bjb1-32546:cuda:1(eval-obs-only-object-norm003-seed65), bjb1-32546:cuda:3(eval-obs-only-object-norm01-seed64), bjb1-32546:cuda:4(eval-obs-only-object-norm01-seed65), bjb1-32546:cuda:5(eval-obs-only-object-norm005-seed64), bjb1-32546:cuda:0(eval-obs-only-object-norm01-seed51-r3), bjb1-32546:cuda:1(eval-obs-only-object-norm01-seed52-r3), bjb1-32546:cuda:3(eval-obs-only-object-norm003-seed62-r2), bjb1-32546:cuda:4(eval-obs-only-object-norm003-seed63-r2), bjb2-28827:cuda:0(eval-obs-only-object-norm01-seed71), bjb2-28827:cuda:1(eval-obs-only-object-norm005-seed72), bjb2-28827:cuda:2(eval-obs-only-object-norm003-seed73), bjb2-28827:cuda:3(eval-obs-only-object-norm01-seed74), bjb2-28827:cuda:4(eval-obs-only-object-norm005-seed75), bjb1-18228:cuda:0(eval-obs-only-object-norm003-seed66), bjb1-18228:cuda:2(eval-obs-only-object-norm005-seed66), bjb1-18228:cuda:3(eval-obs-only-object-norm01-seed66), bjb2-40593:cuda:0(eval-pi05-baseline-object-seed42)\\n\\n### 💾 磁盘余量\\n- **bjb2-40593**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 46G/437G 可用（已用 89%）\\n- **bjb1-18228**:\\n  - `/autodl-pub`: 588G/7.0T 可用（已用 92%） ⚠️\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb1-32546**:\\n  - `/autodl-pub`: 888G/7.0T 可用（已用 88%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%
…[truncated 10581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 320925
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T02:50:17.140716+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-21 00:48 UTC | 更新原因: D092-D095 updates: Plan A LOCKED, OpenVLA CRM CLOSED, π0.5/π added, GPU state corrected\\n\\n> 详见 paper_framing.md（D077: Adaptive K 核心, D088→D090→D092: Plan A GO）\\n\\n## 核心方向\\n**Adaptive inference-time compute for frozen VLAs** — K=2 L2 distance 作为不确定性信号，自适应决定推理策略（直出 vs CRM correction）。CRM correction>selection 分析作为支撑。\\n\\n## 投稿目标\\n**CoRL 2026** DDL **2026-05-29**。剩余 **8 天**。\\n\\n## 方法路径（D088→D092 最终）\\n- ❌ B (Learned Uncertainty Head): NO-GO, mean 12.0% < VLA-only (D090)\\n- ✅ **A (Plan A: K=2 Conformal + Selective CRM)**: Object 18.3%±2.1%, Spatial 35.0%±1.0% — **GO (D092/D094)**\\n- ⏳ C (Action Distribution Geometry): 不再需要，Plan A 已成功\\n\\n## Plan A 核心结果\\n| Benchmark | Plan A (K=2) | K=10 CRM | Δ vs K=10 | Compute |\\n|-----------|-------------|----------|-----------|---------|\\n| Object    | 18.3%±2.1%  | 16.8%    | +1.5pp    | 80% less (K=2 vs K=10) |\\n| Spatial   | 35.0%±1.0%  | 34.5%    | +0.5pp    | 80% less |\\n\\nPipeline: K=2 batched forward → d₂=‖a₁-a₂‖₂ → if d₂>τ: argmin-to-centroid + CRM; if d₂≤τ: direct output。\\n⚠️ Threshold calibration: flatten-L2 (30D) vs per-step-mean-L2 (7D×5) 差异 ~2.77×，当前 τ 在 Plan A scale 上 trigger rate 84%。待决：强调 K=2 效率 vs recalibrate Pareto sweep。\\n\\n## OpenVLA 实验线\\n- ✅ plan_801: OpenVLA v2 baseline SR=69%\\n- ✅ plan_802 train: CRM 训练完成 (val_loss=0.077260)\\n- ❌ **D093: OpenVLA CRM eval 0%** — near-deterministic (T=0.5, 8/10 identical actions)，applicability boundary，CLOSED\\n\\n## π0.5/π 实验线（D095，用户硬要求）\\n- 🔄 Phase 1: WebSearch + 下载模型（Agent 队列中）\\n- ⏳ Phase 2: env setup + baseline eval\\n- ⏳ Phase 3: 检查 action diversity → if stochastic: CRM pipeline\\n- 目的：第二/三个 VLA backbone（flow-matching），解决 M1 (narrow scope) + R2-W1-new (low absolute perf)\\n\\n## Norm Sweep 
…[truncated 3034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 321002
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T02:50:58.686777+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "project": "acr-vla-conformal-refinement",
  "limit": "20",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "project": "acr-vla-conformal-refinement",
    "limit": "20",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T02:50:59.639681+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-obs-only-object-norm005-seed65'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-obs-only-object-norm005-seed65'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T02:51:00.142060+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-vla-only-object-seed49'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-vla-only-object-seed49'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T02:51:00.745587+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm005-seed65\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:30:00.000Z\", \"updated_at\": \"2026-05-21T02:39:12.954Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed65. Norm sweep seed balance for ε=0.05.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 65 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed65.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"622479\", \"seed\": 65, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm005_seed65.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T02:36:11.385Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T02:36:13.448Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T02:36:29.634206+00:00\"}]}, \"notes\": \"失败原因: process dead 5× with no sentinel/W&B。服务器 bjb1-18228, cuda:1。已派 Worker 诊断根因（OOM/SIGHUP/PATH/磁盘？）。同服务器 seed66 系列仍在运行中。\"}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:28:30.000Z\", \"updated_at\": \"2026-05-21T02:30:00.000Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}, \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed56. Norm sweep seed balance for ε=0.03.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 56 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/cr
…[truncated 25520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2058
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T02:51:02.150507+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3991}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2510
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T02:51:03.607485+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.4306}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 3465
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T02:51:54.068439+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__list_workers,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__main_agent_post_to_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__list_workers,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__main_agent_post_to_director",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T02:51:54.132627+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "ToolSearch",
  "elapsed_ms": 64
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T02:51:57.412899+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed43",
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

_source line 25 · 2026-05-21T02:51:57.746309+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"acr-vla-conformal-refinement\", \"section\": \"execution\", \"config\": {\"execution\": {\"account\": \"root\", \"gpu_constraint\": [\"autodl-4090:cuda:0\"], \"gpu_ids\": [\"bjb2-40593:cuda:0\", \"bjb1-18228:cuda:0\", \"bjb1-18228:cuda:1\", \"bjb1-18228:cuda:2\", \"bjb1-18228:cuda:3\", \"bjb1-32546:cuda:0\", \"bjb1-32546:cuda:1\", \"bjb1-32546:cuda:2\", \"bjb1-32546:cuda:3\", \"bjb1-32546:cuda:4\", \"bjb1-32546:cuda:5\", \"bjb2-28827:cuda:0\", \"bjb2-28827:cuda:1\", \"bjb2-28827:cuda:2\", \"bjb2-28827:cuda:3\", \"bjb2-28827:cuda:4\", \"bjb2-28827:cuda:5\"], \"project_path\": \"/root/acr-vla-conformal-refinement\", \"servers\": [\"bjb2-40593\", \"bjb1-18228\", {\"account\": \"root\", \"server\": \"bjb1-32546\"}, {\"account\": \"root\", \"server\": \"bjb2-28827\"}]}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 333
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T02:51:57.746785+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "status": "running"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T02:51:58.174580+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 427
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T02:54:38.952944+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "diagnose:bjb1-18228-norm-seed65-fill",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务：bjb1-18228 诊断 + 填 GPU\n\n### 环境\n- 服务器: bjb1-18228, root 账号\n- conda 环境: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\n- 项目目录: /root/acr-vla-conformal-refinement\n- CRM checkpoint: /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\n\n### 任务 1: 诊断 eval-obs-only-object-norm005-seed65 失败\n这个实验在 bjb1-18228:cuda:1 上运行，PID 622479，被 cron 标记 failed（\"process dead 5× with no sentinel/W&B\"）。\n历史经验：很多类似失败是 cron false positive——eval 脚本不写 sentinel/W&B，正常完成后被误判。\n\n请：\n1. SSH 到 bjb1-18228，检查日志 `/root/autodl-tmp/logs/obs_only_object_norm005_seed65.log`\n2. 查看是否有 \"Overall success rate\" 和 \"Results saved to\" 行\n3. 检查 output JSON 是否存在: `logs/eval_obs_only_object_norm005_seed65.json`\n4. 如果实验实际完成了（有结果），用 update_registry 更新：\n   - conclusion: \"success\"\n   - metrics: {\"success_rate\": X, \"total_rollouts\": 100, \"successful_rollouts\": Y}\n   - notes: \"Cron false positive: 实际 SR=X%\"\n5. 如果是真实失败，记录失败原因到 notes\n\n### 任务 2: 检查 seed66 系列是否正常\nseed66 有 3 个实验在跑（norm003/005/01），没有 cron 监控。\n1. 检查 PID 是否存活:\n   - norm003-seed66: 查 `ps -p 642428`\n   - norm005-seed66: 查 `ps -p 642506`  \n   - norm01-seed66: 查 `ps -p 642775`\n2. 如果进程还活着，报告当前进度（tail 日志最后几行）\n3. 如果有进程已完成，检查结果并更新 registry\n\n### 任务 3: 填补 cuda:1 空闲 GPU\n用 `submit_training_job` 提交新实验 `eval-obs-only-object-norm005-seed67`:\n- exp_id: eval-obs-only-object-norm005-seed67\n- server: bjb1-18228\n- gpu: cuda:1\n- hypothesis: \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed67. Norm sweep seed balance for ε=0.05.\"\n- command: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 67 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed67.json 2>&1 | tee /root/autodl-tmp/logs/obs_only_object_norm005_seed67.log`\n- log_path: /root/autodl-tmp/logs/obs_only_object_norm005_seed67.log\n- timeout_hours: 4\n\n提交前先用 update_registry 创建实验条目（status=PREPARING, hypothesis 如上）。\n\n### 产出\n汇总报告：seed65 诊断结果、seed66 状态、seed67 提交状态。",
  "tool_groups": "['ssh', 'registry']",
  "tools": "['submit_training_job']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "diagnose:bjb1-18228-norm-seed65-fill",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务：bjb1-18228 诊断 + 填 GPU\n\n### 环境\n- 服务器: bjb1-18228, root 账号\n- conda 环境: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\n- 项目目录: /root/acr-vla-conformal-refinement\n- CRM checkpoint: /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\n\n### 任务 1: 诊断 eval-obs-only-object-norm005-seed65 失败\n这个实验在 bjb1-18228:cuda:1 上运行，PID 622479，被 cron 标记 failed（\"process dead 5× with no sentinel/W&B\"）。\n历史经验：很多类似失败是 cron false positive——eval 脚本不写 sentinel/W&B，正常完成后被误判。\n\n请：\n1. SSH 到 bjb1-18228，检查日志 `/root/autodl-tmp/logs/obs_only_object_norm005_seed65.log`\n2. 查看是否有 \"Overall success rate\" 和 \"Results saved to\" 行\n3. 检查 output JSON 是否存在: `logs/eval_obs_only_object_norm005_seed65.json`\n4. 如果实验实际完成了（有结果），用 update_registry 更新：\n   - conclusion: \"success\"\n   - metrics: {\"success_rate\": X, \"total_rollouts\": 100, \"successful_rollouts\": Y}\n   - notes: \"Cron false positive: 实际 SR=X%\"\n5. 如果是真实失败，记录失败原因到 notes\n\n### 任务 2: 检查 seed66 系列是否正常\nseed66 有 3 个实验在跑（norm003/005/01），没有 cron 监控。\n1. 检查 PID 是否存活:\n   - norm003-seed66: 查 `ps -p 642428`\n   - norm005-seed66: 查 `ps -p 642506`  \n   - norm01-seed66: 查 `ps -p 642775`\n2. 如果进程还活着，报告当前进度（tail 日志最后几行）\n3. 如果有进程已完成，检查结果并更新 registry\n\n### 任务 3: 填补 cuda:1 空闲 GPU\n用 `submit_training_job` 提交新实验 `eval-obs-only-object-norm005-seed67`:\n- exp_id: eval-obs-only-object-norm005-seed67\n- server: bjb1-18228\n- gpu: cuda:1\n- hypothesis: \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed67. Norm sweep seed balance for ε=0.05.\"\n- command: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 67 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed67.json 2>&1 | tee /root/autodl-tmp/logs/obs_only_object_norm005_seed67.log`\n- log_path: /root/autodl-tmp/logs/obs_only_object_norm005_seed67.log\n- timeout_hours: 4\n\n提交前先用 update_registry 创建实验条目（status=PREPARING, hypothesis 如上）。\n\n### 产出\n汇总报告：seed65 诊断结果、seed66 状态、seed67 提交状态。",
    "tool_groups": "['ssh', 'registry']",
    "tools": "['submit_training_job']"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-21T02:54:54.552910+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_diagnose_bjb1-18228-norm-seed65-fill_20260521T025446\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_diagnose_bjb1-18228-norm-seed65-fill_20260521T025446.log\", \"setup_data\": {}, \"message\": \"Worker worker_diagnose_bjb1-18228-norm-seed65-fill_20260521T025446 started. Use get_worker_status('worker_diagnose_bjb1-18228-norm-seed65-fill_20260521T025446') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 15599
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T02:54:54.869441+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "diagnose:bjb2-28827-fill-check-unmonitored",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务：bjb2-28827 填 GPU + bjb1-32546 检查未监控实验 + seed49 诊断\n\n### 环境\n- 服务器: bjb2-28827 和 bjb1-32546, root 账号\n- conda 环境: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\n- 项目目录: /root/acr-vla-conformal-refinement\n- CRM checkpoint: /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\n\n### 任务 1: 填补 bjb2-28827:cuda:5\n用 `submit_training_job` 提交新实验 `eval-obs-only-object-norm003-seed76`:\n- exp_id: eval-obs-only-object-norm003-seed76\n- server: bjb2-28827\n- gpu: cuda:5\n- hypothesis: \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed76. Norm sweep seed balance for ε=0.03.\"\n- command: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 76 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed76.json 2>&1 | tee /root/autodl-tmp/logs/obs_only_object_norm003_seed76.log`\n- log_path: /root/autodl-tmp/logs/obs_only_object_norm003_seed76.log\n- timeout_hours: 4\n\n提交前先用 update_registry 创建实验条目（status=PREPARING, hypothesis 如上）。\n\n### 任务 2: 检查 bjb1-32546 未监控实验\n以下实验在 bjb1-32546 上运行但没有 cron 监控：\n- eval-obs-only-object-norm01-seed51-r3 (cuda:0, pid=731912)\n- eval-obs-only-object-norm01-seed52-r3 (cuda:1, pid=733203)\n- eval-obs-only-object-norm003-seed62-r2 (cuda:3, pid=734631)\n- eval-obs-only-object-norm003-seed63-r2 (cuda:4, pid=735998)\n\n它们约 2 小时前提交。每个 eval 大约 1-2 小时。\n\n1. SSH 到 bjb1-32546，检查每个 PID 是否还活着: `ps -p 731912,733203,734631,735998 -o pid,stat,etime`\n2. 对于已完成的，检查 output JSON 和日志最后几行，提取 SR\n3. 用 update_registry 更新：\n   - 如果成功完成: conclusion=success, metrics={success_rate: X, total_rollouts: 100, successful_rollouts: Y}\n   - 如果进程 gone 且无输出: conclusion=failed, notes=原因\n4. 对于仍在运行的，报告当前进度\n\n### 任务 3: 诊断 eval-vla-only-object-seed49\n这个实验卡在 ANALYZING 状态超过 8 小时（since 2026-05-20T17:54:33）。\n1. 用 read_registry 获取完整信息（fields=[\"*\"]），找到它在哪台服务器\n2. SSH 检查它是否有结果\n3. 如果有结果，更新 registry 为 DONE/success + metrics\n4. 如果没有结果且进程已死，更新为 DONE/failed\n\n### 产出\n汇总报告：bjb2-28827 提交状态、bjb1-32546 未监控实验诊断结果、seed49 状态。",
  "tool_groups": "['ssh', 'registry']",
  "tools": "['submit_training_job']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "diagnose:bjb2-28827-fill-check-unmonitored",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务：bjb2-28827 填 GPU + bjb1-32546 检查未监控实验 + seed49 诊断\n\n### 环境\n- 服务器: bjb2-28827 和 bjb1-32546, root 账号\n- conda 环境: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\n- 项目目录: /root/acr-vla-conformal-refinement\n- CRM checkpoint: /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\n\n### 任务 1: 填补 bjb2-28827:cuda:5\n用 `submit_training_job` 提交新实验 `eval-obs-only-object-norm003-seed76`:\n- exp_id: eval-obs-only-object-norm003-seed76\n- server: bjb2-28827\n- gpu: cuda:5\n- hypothesis: \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed76. Norm sweep seed balance for ε=0.03.\"\n- command: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 76 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed76.json 2>&1 | tee /root/autodl-tmp/logs/obs_only_object_norm003_seed76.log`\n- log_path: /root/autodl-tmp/logs/obs_only_object_norm003_seed76.log\n- timeout_hours: 4\n\n提交前先用 update_registry 创建实验条目（status=PREPARING, hypothesis 如上）。\n\n### 任务 2: 检查 bjb1-32546 未监控实验\n以下实验在 bjb1-32546 上运行但没有 cron 监控：\n- eval-obs-only-object-norm01-seed51-r3 (cuda:0, pid=731912)\n- eval-obs-only-object-norm01-seed52-r3 (cuda:1, pid=733203)\n- eval-obs-only-object-norm003-seed62-r2 (cuda:3, pid=734631)\n- eval-obs-only-object-norm003-seed63-r2 (cuda:4, pid=735998)\n\n它们约 2 小时前提交。每个 eval 大约 1-2 小时。\n\n1. SSH 到 bjb1-32546，检查每个 PID 是否还活着: `ps -p 731912,733203,734631,735998 -o pid,stat,etime`\n2. 对于已完成的，检查 output JSON 和日志最后几行，提取 SR\n3. 用 update_registry 更新：\n   - 如果成功完成: conclusion=success, metrics={success_rate: X, total_rollouts: 100, successful_rollouts: Y}\n   - 如果进程 gone 且无输出: conclusion=failed, notes=原因\n4. 对于仍在运行的，报告当前进度\n\n### 任务 3: 诊断 eval-vla-only-object-seed49\n这个实验卡在 ANALYZING 状态超过 8 小时（since 2026-05-20T17:54:33）。\n1. 用 read_registry 获取完整信息（fields=[\"*\"]），找到它在哪台服务器\n2. SSH 检查它是否有结果\n3. 如果有结果，更新 registry 为 DONE/success + metrics\n4. 如果没有结果且进程已死，更新为 DONE/failed\n\n### 产出\n汇总报告：bjb2-28827 提交状态、bjb1-32546 未监控实验诊断结果、seed49 状态。",
    "tool_groups": "['ssh', 'registry']",
    "tools": "['submit_training_job']"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-21T02:54:58.342916+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Worker pool exhausted: 6/6 workers running. Wait for a worker to finish or cancel one.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 3473
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-21T02:55:03.489278+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "status": "running",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "status": "running",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-21T02:55:04.289345+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_diag_cron-false-positive-batch-L23_20260521T025221\", \"task_type\": \"diag:cron-false-positive-batch-L23\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-21T02:52:21.972241+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_diag_verify-nocron-running-L23_20260521T025235\", \"task_type\": \"diag:verify-nocron-running-L23\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-21T02:52:36.226508+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_diagnose_eval-vla-only-object-seed49_20260521T025247\", \"task_type\": \"diagnose:eval-vla-only-object-seed49\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-21T02:52:48.966901+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_diagnose_eval-obs-only-object-norm005-seed65_20260521T025256\", \"task_type\": \"diagnose:eval-obs-only-object-norm005-seed65\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-21T02:52:58.230824+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_diag_bjb1-18228-seed65-seed66_20260521T025310\", \"task_type\": \"diag:bjb1-18228-seed65-seed66\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-21T02:53:12.758178+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_diagnose_bjb1-18228-norm-seed65-fill_20260521T025446\", \"task_type\": \"diagnose:bjb1-18228-norm-seed65-fill\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-21T02:54:48.516848+00:00\", \"ended_at\": null}], \"count\": 6}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 800
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T02:56:07.183758+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 17/17 分配 | 15/17 GPU 在跑 (2 空闲填补中) | Worker 6/6 (全 SSH 诊断) | 磁盘: bjb2-40593 46G可用(89%⚠️) / 其他服务器 399-400G(4-5%)\n\n## 当前状态\n\n### RUNNING (18 实验)\n- **Norm sweep** (17 个): ε=0.03/0.05/0.1 各有 4-7 seeds 在跑，跨 bjb1-18228/32546 + bjb2-28827\n- **π0.5 baseline**: eval-pi05-baseline-object-seed42 on bjb2-40593:cuda:0 (D095/D096)\n\n### Norm Sweep 进度\n| ε | 已完成 | 在跑 | 预计总 n |\n|---|--------|------|---------|\n| 0.03 | ~6 | 6 | ~12 |\n| 0.05 | ~9 | 4 | ~13 |\n| 0.1 | ~8 | 7 | ~15 |\n| 0.2 | 12 | — | LOCKED |\n\n### 操作问题\n1. **2 空闲 GPU**: bjb1-18228:cuda:1（已派 Worker 填 norm005-seed67），bjb2-28827:cuda:5（Worker 池满，待腾出后填 norm003-seed76）\n2. **eval-obs-only-object-norm005-seed65** 疑似 cron false positive — Worker 诊断中\n3. **eval-vla-only-object-seed49** 卡 ANALYZING 8h+ — Worker 诊断中\n4. **bjb1-32546 4 个实验无 cron**（seed51-r3/52-r3/62-r2/63-r2，约 2h 前提交）— Worker 检查中\n5. **bjb2-40593 磁盘仅 46G** — π0.5 模型下载可能需要更多空间，关注中\n\n### 下一步\n- Worker 回调后汇总诊断结果 + 填剩余空闲 GPU\n- Norm sweep 全部完成后生成 Figure 2\n- π0.5 baseline 完成后评估 action diversity → 决定 CRM pipeline 可行性\n- Plan A 结果写入论文（待 Director 指令启动 Paper Agent）",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 17/17 分配 | 15/17 GPU 在跑 (2 空闲填补中) | Worker 6/6 (全 SSH 诊断) | 磁盘: bjb2-40593 46G可用(89%⚠️) / 其他服务器 399-400G(4-5%)\n\n## 当前状态\n\n### RUNNING (18 实验)\n- **Norm sweep** (17 个): ε=0.03/0.05/0.1 各有 4-7 seeds 在跑，跨 bjb1-18228/32546 + bjb2-28827\n- **π0.5 baseline**: eval-pi05-baseline-object-seed42 on bjb2-40593:cuda:0 (D095/D096)\n\n### Norm Sweep 进度\n| ε | 已完成 | 在跑 | 预计总 n |\n|---|--------|------|---------|\n| 0.03 | ~6 | 6 | ~12 |\n| 0.05 | ~9 | 4 | ~13 |\n| 0.1 | ~8 | 7 | ~15 |\n| 0.2 | 12 | — | LOCKED |\n\n### 操作问题\n1. **2 空闲 GPU**: bjb1-18228:cuda:1（已派 Worker 填 norm005-seed67），bjb2-28827:cuda:5（Worker 池满，待腾出后填 norm003-seed76）\n2. **eval-obs-only-object-norm005-seed65** 疑似 cron false positive — Worker 诊断中\n3. **eval-vla-only-object-seed49** 卡 ANALYZING 8h+ — Worker 诊断中\n4. **bjb1-32546 4 个实验无 cron**（seed51-r3/52-r3/62-r2/63-r2，约 2h 前提交）— Worker 检查中\n5. **bjb2-40593 磁盘仅 46G** — π0.5 模型下载可能需要更多空间，关注中\n\n### 下一步\n- Worker 回调后汇总诊断结果 + 填剩余空闲 GPU\n- Norm sweep 全部完成后生成 Figure 2\n- π0.5 baseline 完成后评估 action diversity → 决定 CRM pipeline 可行性\n- Plan A 结果写入论文（待 Director 指令启动 Paper Agent）",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-21T02:56:25.968510+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 18784
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-21T02:56:33.547767+00:00_

已汇报 Director。6 个 Worker 在跑，等回调。当前待处理：

1. Worker 回调 → 处理诊断结果（seed65, seed49, unmonitored experiments）
2. Worker 池腾出 → 填 bjb2-28827:cuda:5（norm003-seed76）
3. 所有 norm sweep 完成 → 汇总 + Figure 2
4. π0.5 baseline 完成 → 评估 action diversity

等待 Worker 回调中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-crm-object-k20-seed43"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 37 · 2026-05-21T18:57:19.350713+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed43",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-21T18:58:20.472944+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单: bjb2-40593:cuda:0, bjb1-18228:cuda:0-3, bjb1-32546:cuda:0-5, bjb2-28827:cuda:0-5（共 17 张）。白名单外 GPU 即使 Director 说也必须 push back
- Object CRM K=10 Table 1 只用 norm02 数据（D080），seed42 SR=20% 不纳入（D084 决策）
- Spatial CRM K=10 用 clean n=8 数据 34.4±1.5%（D083），不引用旧 n=7
- Long OOD 只能 cautious wording（MW-U p=0.061 n.s.，D081）
- CRM checkpoint 唯一路径: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`
- evaluate.py 在 `src/` 子目录下（`python src/evaluate.py`），多次因漏 `src/` 导致 EXIT_CODE=2
- bjb1-32546 命令必须带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&` 前缀，裸 `python` 不在 PATH

### 2. 🖥️ 基础设施快照
- **bjb2-40593**: 1× RTX 4090, root, ~/acr-vla-conformal-refinement/, conda base
- **bjb1-18228**: 4× RTX 4090 (cuda:0-3), root, ~/acr-vla-conformal-refinement/, conda base, `/root/miniconda3/bin/python`
- **bjb1-32546**: 6× RTX 4090 (cuda:0-5), root, ~/acr-vla-conformal-refinement/, conda base, `/root/miniconda3/bin/python`
- **bjb2-28827**: 6× RTX 4090 (cuda:0-5), root, ~/acr-vla-conformal-refinement/, conda base
- CRM checkpoint: 所有服务器 `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`
- 日志统一写 `/root/autodl-tmp/logs/`（不用项目目录下 `logs/`，否则 cron 找不到）
- 磁盘注意: bjb2-40593 仅 46G 可用（89% 已用）⚠️

### 3. 📊 当前状态
**刚做完**: session-start 初始化 + read_registry + reconcile_crons + 向 Director 汇报当前状态。派了 1 个 Worker（bjb1-18228 诊断+填 GPU），第 2 个 Worker 因池满（6/6）被拒。

**RUNNING (18 实验)**:
- Norm sweep ε=0.03: seed64/65 (bjb1-32546), seed62-r2/63-r2 (bjb1-32546), seed66 (bjb1-18228), seed73 (bjb2-28827) — 6 个
- Norm sweep ε=0.05: seed64 (bjb1-32546), seed66 (bjb1-18228), seed72/75 (bjb2-28827) — 4 个
- Norm sweep ε=0.1: seed64/65 (bjb1-32546), seed51-r3/52-r3 (bjb1-32546), seed66 (bjb1-18228), seed71/74 (bjb2-28827) — 7 个
- π0.5 baseline: eval-pi05-baseline-object-seed42 (bjb2-40593:cuda:0)

**ANALYZING (1)**: eval-vla-only-object-seed49 — 卡 8h+，Worker 在诊断

**6 个 Worker 在跑**（池满）:
1. `diag:cron-false-positive-batch-L23` — 批量修正 cron false positive
2. `diag:verify-nocron-running-L23` — 检查无 cron 监控的实验
3. `diagnose:eval-vla-only-object-seed49` — 诊断卡住的 seed49
4. `diagnose:eval-obs-only-object-norm005-seed65` — 诊断 bjb1-18228 seed65 失败
5. `diag:bjb1-18228-seed65-seed66` — bjb1-18228 综合诊断
6. `diagnose:bjb1-18228-norm-seed65-fill` — 我新派的，诊断 seed65 + 填 cuda:1

**空闲 GPU**: bjb1-18228:cuda:1（Worker 在填），bjb2-28827:cuda:5（待 Worker 池腾出）

### 4. 📋 待办
- 任一 Worker 完成回调 → 处理诊断结果，更新 registry，Worker 池腾出后 spawn Worker 填 bjb2-28827:cuda:5（norm003-seed76）
- bjb1-32546 无 cron 实验（seed51-r3/52-r3/62-r2/63-r2）Worker 回报完成 → update_registry + 补录 metrics
- eval-vla-only-object-seed49 诊断回来 → 根据实际状态关闭（DONE/success 或 DONE/failed）
- norm sweep 全部完成（ε=0.03/0.05/0.1 各 ~12 seeds）→ 汇总 mean±std，生成 Figure 2
- eval-pi05-baseline-object-seed42 完成 → 记录 SR，评估 action diversity（是否 near-deterministic 如 OpenVLA），决定 CRM pipeline 可行性
- π0.5 action diversity OK → 按 D095/D096 推进 CRM 训练或直接 eval
- Director 指令启动 Paper Agent → Plan A 结果写入论文

### 5. 🎯 战略上下文
- **CoRL 2026 DDL: 2026-05-29，剩 ~8 天**
- 决策链: D075(FMVD NO-GO) → D076(K=2 L2 GO) → D077(Adaptive K 升核心) → D078(P50 Pareto最优) → D079(CRM mag NO-GO) → D080(Table1 norm02) → D081(Long OOD cautious) → D082(batched inference) → D083(Spatial n=8 clean) → D084(seed42排除) → D088(Learned Unc Head) → D090(Unc Head NO-GO) → D092(Plan A GO) → D093(OpenVLA CRM 0% CLOSED) → D094(Plan A Spatial GO) → D095/D096(π0.5 GO)
- **Plan A LOCKED**: Object 18.3%±2.1%, Spatial 35.0%±1.0% (K=2 conformal + selective CRM)
- **核心贡献**: K=2 L2 distance 做不确定性信号，自适应直出 vs CRM correction
- **π0.5 是关键**: D095 用户硬要求，解决 M1(narrow scope) + R2-W1-new(low absolute perf)。OpenVLA CRM 0% 已 CLOSED（near-deterministic），π0.5 是 flow-matching VLA，理论上 stochastic → CRM 可能 work
- **易错点**: (1) Spatial 实验用 Object-calibrated threshold（τ=P50 0.07246），这是 cross-benchmark transfer claim，不是 bug (2) cron false positive 是常态——eval 脚本不写 sentinel/W&B，进程正常退出后被误判 failed，几乎每个 eval 都需要手动修正 (3) bjb2-40593 磁盘紧张，π0.5 模型下载前检查空间 (4) Worker 池 6/6 容易满，回调处理要快，否则新 Worker 排不上
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-crm-object-k20-seed43"
}
```

</details>

---
