# cron hook eval crm object k20 seed42 20260521T190856 456090

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 95
- **Recorded user turns:** 2
- **Tool calls:** 46
- **Original source:** `logs/chats/archive/cron_hook_eval-crm-object-k20-seed42_20260521T190856_456090.jsonl`
- **Structured JSON:** [`156613dba266e06300f0.json`](../../sessions/15/156613dba266e06300f0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

51 recorded events

### User

_source line 1 · 2026-05-21T02:44:27.421478+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #23。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单严格按 `get_project_status` 的 `execution.gpu_ids`，即使 Director 指令用白名单外的 GPU 也必须 push back
- K=10 Object CRM 数据已锁定 norm02-only n=6 (16.8±1.8%)，D084 决定 seed42 (SR=20%) 不纳入 Table 1（异常值）
- Spatial CRM K=10 已修正为 clean n=8 (34.4±1.5%)，D083
- Long OOD 必须用 cautious wording（MW-U p=0.061 n.s.），D081
- evaluate.py 确认使用 batched inference（D082），延迟表和效率 claim 需据此校准
- CoRL 2026 DDL **2026-05-29**，剩余 ~8 天

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: 工作目录 `/root/acr-vla-conformal-refinement`，Python `/root/miniconda3/bin/python`，conda base。磁盘 400G/438G 可用(4%)。CRM checkpoint: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`
- **bjb1-32546**: 同上路径布局。磁盘 400G/438G 可用(4%)。多卡运行中 cuda:1-5
- **bjb2-40593**: 磁盘紧张 46G/437G (90%) ⚠️。cuda:0 跑 adaptive-k-spatial-p50-seed42
- **bjb2-28827**: 磁盘 399G/439G 可用(5%)。当前空闲
- HF cache: `/root/autodl-tmp/.hf_cache`（所有服务器）
- 输出 JSON 路径: `/root/acr-vla-conformal-refinement/logs/eval_*.json`

### 3. 📊 当前状态
**刚做完**: 收到 `eval-crm-object-k20-seed42` 的 cron 完成回调（ANALYZING），已派 Worker `worker_analysis_eval-crm-object-k20-seed42_20260520T103217` 去 SSH 读取结果并更新 registry。**Worker 结果尚未回调**——下一个 session 需要检查该 Worker 是否完成，若完成则处理结果并汇报 Director。

**RUNNING 实验** (7 张 GPU):
| exp_id | server | gpu |
|--------|--------|-----|
| eval-adaptive-k-spatial-p50-seed42 | bjb2-40593 | cuda:0 |
| eval-adaptive-k-spatial-p25-seed42 | bjb1-18228 | cuda:2 |
| eval-adaptive-k-spatial-p75-seed43 | bjb1-32546 | cuda:1 |
| eval-adaptive-k-spatial-p25-seed43 | bjb1-32546 | cuda:2 |
| eval-crm-object-k20-seed43 | bjb1-32546 | cuda:3 |
| eval-obs-only-object-norm003-seed43-r2 | bjb1-32546 | cuda:4 |
| eval-obs-only-object-norm005-seed44 | bjb1-32546 | cuda:5 |

**另有 1 个 running Worker**: `worker_diagnose_eval-adaptive-k-spatial-p50-seed42` (诊断 p50-seed42 运行状况)

**ANALYZING**: eval-crm-object-k20-seed42（等 Worker 回调）

### 4. 📋 待办
- Worker `worker_analysis_eval-crm-object-k20-seed42` 回调 → 读取 K=20 SR，与 K=10 (16.8%) 对比，更新 registry → 汇报 Director（K=20 是否有边际收益，支撑 "K=10 compute-efficient" claim）
- eval-crm-object-k20-seed43 完成 → 同样分析，汇总 K=20 两个 seed 的均值
- eval-adaptive-k-spatial-* 各 seed 完成 → 汇总 Spatial Adaptive K 全矩阵，更新 ROADMAP 的 Spatial sweep 表
- eval-obs-only-object-norm003/005 完成 → 补充 Figure 2 低 ε 区间 error bars
- Spatial Adaptive K P50 3 seeds 全部完成 → 可以写论文 Spatial 段落，验证 cross-benchmark transfer
- bjb2-40593 磁盘 90% → 提交新实验前先 list_large_dirs 清理
- Worker 池 < 2 → 需要补充并行任务（文献联动、论文起草准备等）

### 5. 🎯 战略上下文
- **D077 方向转换**: Adaptive K = 论文核心贡献（用户硬要求）。K=2 L2 distance 是唯一可用不确定性信号 (ρ=0.9979)。K=10 CRM 分析降为 supporting evidence
- **D078**: P50 阈值 = Pareto 最优（Object 3 seeds: 15.3% SR, avg_K~3.8, ~77% fast_path, ~91% of K=10 SR）
- **K-value sweep (plan_601)**: K=20 实验正在分析中。如果 K=20 ≈ K=10 SR，则强化 "diminishing returns beyond K=10" claim；如果 K=20 > K=10，需要重新讨论 K=10 的定位
- **关键格子还缺**: Spatial Adaptive K P50 × 3 seeds, Random Selection baseline (plan_600)
- **易踩坑**: 
  - D084 决定 seed42 norm02 (SR=20%) 是异常值不纳入 Table 1，新 session 别把它算进去
  - bjb2-40593 磁盘极紧张，不要往上面提交新实验
  - eval-adaptive-k-spatial-p50-seed42 在 bjb2-40593 上有诊断 Worker 在跑，可能有问题需要关注

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
前 151 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-21T02:44:37.323753+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__list_workers",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__list_workers",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-21T02:44:37.387104+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "ToolSearch",
  "elapsed_ms": 63
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T02:44:40.179624+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed42",
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

_source line 5 · 2026-05-21T02:44:41.137241+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed42",
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

_source line 6 · 2026-05-21T02:44:41.137681+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T02:44:42.045701+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "status": "running"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T02:44:42.146459+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed42",
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

_source line 9 · 2026-05-21T02:44:48.304307+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-pi05-baseline-object-seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T01:50:00.000Z\", \"updated_at\": \"2026-05-21T01:50:00.000Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42 — establishes reference success rate for flow-matching VLA, tests CRM applicability to second VLA backbone\"}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T01:48:00.000Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\"}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T01:48:00.000Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.05 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\"}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T01:48:00.000Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.1 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\"}, \"eval-obs-only-object-norm01-seed71\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T00:55:00.000Z\", \"updated_at\": \"2026-05-21T00:55:00.000Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed71. Norm sweep filling ε=0.1 gap.\"}, \"eval-obs-only-object-norm005-seed72\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T00:55:00.000Z\", \"updated_at\": \"2026-05-21T00:55:00.000Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed72. Norm sweep seed balance.\"}, \"eval-obs-only-object-norm003-seed73\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T00:55:00.000Z\", \"updated_at\": \"2026-05-21T00:55:00.000Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Obje
…[truncated 3533 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 8124
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T02:44:58.425545+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-vla-only-object-seed49\": {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-19T21:15:12.591Z\", \"updated_at\": \"2026-05-20T17:54:33.055Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed49. Expanding VLA-only baseline seed coverage for Object benchmark.\"}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.0263}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 17288
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T02:49:53.079459+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 11, \"results\": [{\"exp_id\": \"eval-obs-only-object-norm003-seed64\", \"success\": true, \"actions\": [\"Job still running (pid=723784)\"]}, {\"exp_id\": \"eval-obs-only-object-norm003-seed65\", \"success\": true, \"actions\": [\"Job still running (pid=725722)\"]}, {\"exp_id\": \"eval-obs-only-object-norm01-seed64\", \"success\": true, \"actions\": [\"Job still running (pid=726800)\"]}, {\"exp_id\": \"eval-obs-only-object-norm01-seed65\", \"success\": true, \"actions\": [\"Job still running (pid=728057)\"]}, {\"exp_id\": \"eval-obs-only-object-norm005-seed64\", \"success\": true, \"actions\": [\"Job still running (pid=729873)\"]}, {\"exp_id\": \"eval-obs-only-object-norm01-seed71\", \"success\": true, \"actions\": [\"Job still running (pid=922504)\"]}, {\"exp_id\": \"eval-obs-only-object-norm005-seed72\", \"success\": true, \"actions\": [\"Job still running (pid=922712)\"]}, {\"exp_id\": \"eval-obs-only-object-norm003-seed73\", \"success\": true, \"actions\": [\"Job still running (pid=922982)\"]}, {\"exp_id\": \"eval-obs-only-object-norm01-seed74\", \"success\": true, \"actions\": [\"Job still running (pid=923256)\"]}, {\"exp_id\": \"eval-obs-only-object-norm005-seed75\", \"success\": true, \"actions\": [\"Job still running (pid=923398)\"]}, {\"exp_id\": \"eval-pi05-baseline-object-seed42\", \"success\": true, \"actions\": [\"Job still running (pid=802634)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 311941
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T02:49:53.671597+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 311625
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T02:49:53.786333+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-21T02:36:32Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 541 个实验 — ANALYZING 1, DEPLOYED 5, DONE 482, PREPARING 34, RUNNING 19\\n**DONE 分布**: failed 54, killed 90, negative 38, success 300\\n\\n### GPU 占用\\n- **实际运行**: 19 张 — bjb2-28827:cuda:2(eval-obs-only-object-norm003-seed56), bjb1-32546:cuda:0(eval-obs-only-object-norm003-seed64), bjb1-32546:cuda:1(eval-obs-only-object-norm003-seed65), bjb1-32546:cuda:3(eval-obs-only-object-norm01-seed64), bjb1-32546:cuda:4(eval-obs-only-object-norm01-seed65), bjb1-32546:cuda:5(eval-obs-only-object-norm005-seed64), bjb1-32546:cuda:0(eval-obs-only-object-norm01-seed51-r3), bjb1-32546:cuda:1(eval-obs-only-object-norm01-seed52-r3), bjb1-32546:cuda:3(eval-obs-only-object-norm003-seed62-r2), bjb1-32546:cuda:4(eval-obs-only-object-norm003-seed63-r2), bjb2-28827:cuda:0(eval-obs-only-object-norm01-seed71), bjb2-28827:cuda:1(eval-obs-only-object-norm005-seed72), bjb2-28827:cuda:2(eval-obs-only-object-norm003-seed73), bjb2-28827:cuda:3(eval-obs-only-object-norm01-seed74), bjb2-28827:cuda:4(eval-obs-only-object-norm005-seed75), bjb1-18228:cuda:0(eval-obs-only-object-norm003-seed66), bjb1-18228:cuda:2(eval-obs-only-object-norm005-seed66), bjb1-18228:cuda:3(eval-obs-only-object-norm01-seed66), bjb2-40593:cuda:0(eval-pi05-baseline-object-seed42)\\n\\n### 💾 磁盘余量\\n- **bjb2-40593**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 46G/437G 可用（已用 89%）\\n- **bjb1-18228**:\\n  - `/autodl-pub`: 588G/7.0T 可用（已用 92%） ⚠️\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb1-32546**:\\n  - `/autodl-pub`: 888G/7.0T 可用（已用 88%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%
…[truncated 10581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 311639
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T02:50:13.225526+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "project": "acr-vla-conformal-refinement",
  "limit": "20",
  "fields": "['status', 'conclusion', 'metrics', 'updated_at', 'hypothesis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "project": "acr-vla-conformal-refinement",
    "limit": "20",
    "fields": "['status', 'conclusion', 'metrics', 'updated_at', 'hypothesis']"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T02:50:13.283689+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T02:50:20.640465+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm005-seed65\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T02:39:12.954Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed65. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T02:30:00.000Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15}, \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed56. Norm sweep seed balance for ε=0.03.\"}, \"eval-obs-only-object-norm005-seed61\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T02:05:10.608Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"successful_rollouts\": 15, \"total_rollouts\": 100}, \"hypothesis\": \"CRM obs_only with max_correction_norm=0.05 (ε=0.05) on LIBERO-Object seed61 provides consistent improvement over VLA-only baseline, contributing to norm sweep statistical robustness for the ε=0.05 condition.\"}, \"eval-obs-only-object-norm005-seed58\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T01:25:14.143Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed58. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"total_rollouts\": 100, \"successful_rollouts\": 16}}, \"eval-obs-only-object-norm01-seed57\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T01:25:08.752Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed57. Norm sweep: additional ε=0.1 data point.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.19, \"total_rollouts\": 100, \"successful_rollouts\": 19}}, \"eval-obs-only-object-norm003-seed59\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T01:25:04.366Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed59. Norm sweep seed balance for ε=0.03.\", \"conclusion\": \"success\", \"metri
…[truncated 4472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 7414
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T02:50:20.692713+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-21 00:48 UTC | 更新原因: D092-D095 updates: Plan A LOCKED, OpenVLA CRM CLOSED, π0.5/π added, GPU state corrected\\n\\n> 详见 paper_framing.md（D077: Adaptive K 核心, D088→D090→D092: Plan A GO）\\n\\n## 核心方向\\n**Adaptive inference-time compute for frozen VLAs** — K=2 L2 distance 作为不确定性信号，自适应决定推理策略（直出 vs CRM correction）。CRM correction>selection 分析作为支撑。\\n\\n## 投稿目标\\n**CoRL 2026** DDL **2026-05-29**。剩余 **8 天**。\\n\\n## 方法路径（D088→D092 最终）\\n- ❌ B (Learned Uncertainty Head): NO-GO, mean 12.0% < VLA-only (D090)\\n- ✅ **A (Plan A: K=2 Conformal + Selective CRM)**: Object 18.3%±2.1%, Spatial 35.0%±1.0% — **GO (D092/D094)**\\n- ⏳ C (Action Distribution Geometry): 不再需要，Plan A 已成功\\n\\n## Plan A 核心结果\\n| Benchmark | Plan A (K=2) | K=10 CRM | Δ vs K=10 | Compute |\\n|-----------|-------------|----------|-----------|---------|\\n| Object    | 18.3%±2.1%  | 16.8%    | +1.5pp    | 80% less (K=2 vs K=10) |\\n| Spatial   | 35.0%±1.0%  | 34.5%    | +0.5pp    | 80% less |\\n\\nPipeline: K=2 batched forward → d₂=‖a₁-a₂‖₂ → if d₂>τ: argmin-to-centroid + CRM; if d₂≤τ: direct output。\\n⚠️ Threshold calibration: flatten-L2 (30D) vs per-step-mean-L2 (7D×5) 差异 ~2.77×，当前 τ 在 Plan A scale 上 trigger rate 84%。待决：强调 K=2 效率 vs recalibrate Pareto sweep。\\n\\n## OpenVLA 实验线\\n- ✅ plan_801: OpenVLA v2 baseline SR=69%\\n- ✅ plan_802 train: CRM 训练完成 (val_loss=0.077260)\\n- ❌ **D093: OpenVLA CRM eval 0%** — near-deterministic (T=0.5, 8/10 identical actions)，applicability boundary，CLOSED\\n\\n## π0.5/π 实验线（D095，用户硬要求）\\n- 🔄 Phase 1: WebSearch + 下载模型（Agent 队列中）\\n- ⏳ Phase 2: env setup + baseline eval\\n- ⏳ Phase 3: 检查 action diversity → if stochastic: CRM pipeline\\n- 目的：第二/三个 VLA backbone（flow-matching），解决 M1 (narrow scope) + R2-W1-new (low absolute perf)\\n\\n## Norm Sweep 
…[truncated 3034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 7409
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T02:50:57.678435+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE', 'conclusion': 'failed'}",
  "project": "acr-vla-conformal-refinement",
  "limit": "15",
  "fields": "['status', 'conclusion', 'metrics', 'updated_at', 'hypothesis', 'server', 'gpu']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE', 'conclusion': 'failed'}",
    "project": "acr-vla-conformal-refinement",
    "limit": "15",
    "fields": "['status', 'conclusion', 'metrics', 'updated_at', 'hypothesis', 'server', 'gpu']"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T02:50:58.987403+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__send_progress,mcp__agent-ml-research__get_worker_status",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__send_progress,mcp__agent-ml-research__get_worker_status",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T02:50:59.691076+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm005-seed65\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T02:39:12.954Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed65. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm005-seed62\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T01:15:11.709Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed62. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm005-seed63\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T01:14:56.556Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed63. Norm sweep seed balance for ε=0.05.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed61\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T01:14:51.727Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed61. Norm sweep filling ε=0.1 gap.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed63\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T00:36:29.353Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed63. Norm sweep seed balance for ε=0.03.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed62\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T00:36:21.900Z\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed62. Norm sweep seed balance for ε=0.03 (only 3 seeds, need more for reliable mean±std).\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed51-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T00:36:16.959Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed51 r2. Redo of crashed seed51 (process dead, no JSON). Norm sweep: filling ε=0.1 gap.\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed52-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T00:36:12.707Z\", \"hyp
…[truncated 2761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2012
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T02:50:59.743538+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "ToolSearch",
  "elapsed_ms": 756
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T02:51:32.544565+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed42",
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

_source line 23 · 2026-05-21T02:51:33.198942+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed42",
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

### Tool call

_source line 24 · 2026-05-21T02:51:33.900849+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-obs-only-object-norm005-seed62'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['server', 'gpu', 'log_path', 'conclusion']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-obs-only-object-norm005-seed62'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['server', 'gpu', 'log_path', 'conclusion']"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T02:51:34.454503+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-obs-only-object-norm01-seed61'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['server', 'gpu', 'log_path', 'conclusion']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-obs-only-object-norm01-seed61'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['server', 'gpu', 'log_path', 'conclusion']"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T02:51:35.512868+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9103}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2968
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T02:51:37.108630+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.5624}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 3909
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T02:51:39.925596+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.8028}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 6024
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-21T02:51:43.089767+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1123}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 8635
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T02:51:49.595971+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE', 'conclusion': 'failed'}",
  "project": "acr-vla-conformal-refinement",
  "limit": "10",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE', 'conclusion': 'failed'}",
    "project": "acr-vla-conformal-refinement",
    "limit": "10",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T02:51:49.663903+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'ANALYZING'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'ANALYZING'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T02:51:52.409253+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm005-seed65\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:30:00.000Z\", \"updated_at\": \"2026-05-21T02:39:12.954Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed65. Norm sweep seed balance for ε=0.05.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 65 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed65.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"622479\", \"seed\": 65, \"model_name\": \"CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/logs/obs_only_object_norm005_seed65.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T02:36:11.385Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T02:36:13.448Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T02:36:29.634206+00:00\"}]}, \"notes\": \"失败原因: process dead 5× with no sentinel/W&B。服务器 bjb1-18228, cuda:1。已派 Worker 诊断根因（OOM/SIGHUP/PATH/磁盘？）。同服务器 seed66 系列仍在运行中。\"}, \"eval-obs-only-object-norm005-seed62\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:45:00.000Z\", \"updated_at\": \"2026-05-21T01:15:11.709Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed62. Norm sweep seed balance for ε=0.05.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 62 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_
…[truncated 11782 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2813
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-21T02:51:57.387798+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-vla-only-object-seed49\": {\"status\": \"ANALYZING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T21:15:12.591Z\", \"updated_at\": \"2026-05-20T17:54:33.055Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed49. Expanding VLA-only baseline seed coverage for Object benchmark.\", \"completed_at\": \"2026-05-19T22:08:11.590Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T17:54:47.787199+00:00\"}]}, \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark object --seed 49 --n_rollouts 10 --K 1 --output_file logs/eval_vla_only_object_seed49.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA\", \"seed\": 49, \"checkpoint_source\": \"N/A\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-vla-only-object-seed49.log\"}, \"pid\": 542620, \"reproduce\": {\"finished_at\": \"2026-05-20T17:54:31.137Z\"}}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.9428}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 7723
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T02:52:44.107645+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "diagnose:eval-vla-only-object-seed49",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务\n诊断并解决 eval-vla-only-object-seed49 卡在 ANALYZING 状态（>24h）。\n\n## 背景\n- 实验在 bjb1-32546 上运行，VLA-only baseline（LIBERO-Object seed49）\n- completed_at: 2026-05-19T22:08，但状态一直是 ANALYZING\n- 原始命令: `python -u src/evaluate.py --mode vla_only --benchmark object --seed 49 --n_rollouts 10 --K 1 --output_file logs/eval_vla_only_object_seed49.json`\n- 日志路径: `logs/eval-vla-only-object-seed49.log`（注意可能在项目目录 `/root/acr-vla-conformal-refinement/logs/` 下）\n\n## 步骤\n1. SSH 到 bjb1-32546，检查 output JSON 是否存在:\n   ```\n   ls -la /root/acr-vla-conformal-refinement/logs/eval_vla_only_object_seed49.json\n   cat /root/acr-vla-conformal-refinement/logs/eval_vla_only_object_seed49.json | python3 -c \"import sys,json; d=json.load(sys.stdin); print(f'SR={d.get(\\\"overall_success_rate\\\", \\\"N/A\\\")}, rollouts={d.get(\\\"total_rollouts\\\", \\\"N/A\\\")}')\"\n   ```\n2. 如果 JSON 存在且完整 → 提取 success_rate → 用 update_registry 更新:\n   - conclusion=success (如果完成了所有 rollouts)\n   - metrics: {success_rate: X, total_rollouts: 100, successful_rollouts: Y}\n   - status=DONE\n3. 如果 JSON 不存在 → tail 日志查看最后输出，判断是否正常完成\n4. 把结果写入 registry notes\n\n## 环境\n- Python: `/root/miniconda3/bin/python`（conda base 环境）\n- 项目路径: `/root/acr-vla-conformal-refinement`\n",
  "tool_groups": "['ssh', 'registry']"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "diagnose:eval-vla-only-object-seed49",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务\n诊断并解决 eval-vla-only-object-seed49 卡在 ANALYZING 状态（>24h）。\n\n## 背景\n- 实验在 bjb1-32546 上运行，VLA-only baseline（LIBERO-Object seed49）\n- completed_at: 2026-05-19T22:08，但状态一直是 ANALYZING\n- 原始命令: `python -u src/evaluate.py --mode vla_only --benchmark object --seed 49 --n_rollouts 10 --K 1 --output_file logs/eval_vla_only_object_seed49.json`\n- 日志路径: `logs/eval-vla-only-object-seed49.log`（注意可能在项目目录 `/root/acr-vla-conformal-refinement/logs/` 下）\n\n## 步骤\n1. SSH 到 bjb1-32546，检查 output JSON 是否存在:\n   ```\n   ls -la /root/acr-vla-conformal-refinement/logs/eval_vla_only_object_seed49.json\n   cat /root/acr-vla-conformal-refinement/logs/eval_vla_only_object_seed49.json | python3 -c \"import sys,json; d=json.load(sys.stdin); print(f'SR={d.get(\\\"overall_success_rate\\\", \\\"N/A\\\")}, rollouts={d.get(\\\"total_rollouts\\\", \\\"N/A\\\")}')\"\n   ```\n2. 如果 JSON 存在且完整 → 提取 success_rate → 用 update_registry 更新:\n   - conclusion=success (如果完成了所有 rollouts)\n   - metrics: {success_rate: X, total_rollouts: 100, successful_rollouts: Y}\n   - status=DONE\n3. 如果 JSON 不存在 → tail 日志查看最后输出，判断是否正常完成\n4. 把结果写入 registry notes\n\n## 环境\n- Python: `/root/miniconda3/bin/python`（conda base 环境）\n- 项目路径: `/root/acr-vla-conformal-refinement`\n",
    "tool_groups": "['ssh', 'registry']"
  }
}
````

</details>

---

### Tool result

_source line 35 · 2026-05-21T02:52:54.995574+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_diagnose_eval-vla-only-object-seed49_20260521T025247\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_diagnose_eval-vla-only-object-seed49_20260521T025247.log\", \"setup_data\": {}, \"message\": \"Worker worker_diagnose_eval-vla-only-object-seed49_20260521T025247 started. Use get_worker_status('worker_diagnose_eval-vla-only-object-seed49_20260521T025247') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 10887
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T02:52:55.106963+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "diagnose:eval-obs-only-object-norm005-seed65",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务\n诊断 eval-obs-only-object-norm005-seed65 是否为 cron false positive（可能实际完成但被误判为 failed）。\n\n## 背景\n- 服务器: bjb1-18228, cuda:1, PID 622479\n- 命令: `python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 65 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed65.json`\n- 日志路径: `/root/autodl-tmp/logs/obs_only_object_norm005_seed65.log`\n- failure_reason: \"process dead 5× with no sentinel/W&B — auto-resolved as failed\"\n- 同服务器 seed66 系列仍在运行中\n- 项目已知 cron false positive 模式：eval 脚本不写 sentinel/W&B，正常完成后 cron 误判\n\n## 步骤\n1. SSH (read_only) 到 bjb1-18228:\n   ```bash\n   # 检查 output JSON\n   ls -la /root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm005_seed65.json\n   # 检查进程是否还活着\n   ps -p 622479 -o pid,stat,etime,args 2>/dev/null || echo \"PID_GONE\"\n   # 读日志尾部\n   tail -20 /root/autodl-tmp/logs/obs_only_object_norm005_seed65.log 2>/dev/null || echo \"NO_LOG\"\n   ```\n2. 如果 output JSON 存在且完整:\n   - 提取 overall_success_rate\n   - update_registry: conclusion=success, metrics={success_rate: X, total_rollouts: 100, successful_rollouts: Y}\n   - notes: \"Cron false positive confirmed. Output JSON 已存在，实验正常完成。\"\n3. 如果 JSON 不存在但日志显示 \"Results saved to\" + \"Overall success rate\":\n   - 同样提取 SR 并更新 registry\n4. 如果确认真正失败 → 记录失败原因到 notes\n\n## 环境\n- Python: `/root/miniconda3/bin/python`（conda base 环境）\n- 项目路径: `/root/acr-vla-conformal-refinement`\n",
  "tool_groups": "['ssh', 'registry']"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "diagnose:eval-obs-only-object-norm005-seed65",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务\n诊断 eval-obs-only-object-norm005-seed65 是否为 cron false positive（可能实际完成但被误判为 failed）。\n\n## 背景\n- 服务器: bjb1-18228, cuda:1, PID 622479\n- 命令: `python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 65 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed65.json`\n- 日志路径: `/root/autodl-tmp/logs/obs_only_object_norm005_seed65.log`\n- failure_reason: \"process dead 5× with no sentinel/W&B — auto-resolved as failed\"\n- 同服务器 seed66 系列仍在运行中\n- 项目已知 cron false positive 模式：eval 脚本不写 sentinel/W&B，正常完成后 cron 误判\n\n## 步骤\n1. SSH (read_only) 到 bjb1-18228:\n   ```bash\n   # 检查 output JSON\n   ls -la /root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm005_seed65.json\n   # 检查进程是否还活着\n   ps -p 622479 -o pid,stat,etime,args 2>/dev/null || echo \"PID_GONE\"\n   # 读日志尾部\n   tail -20 /root/autodl-tmp/logs/obs_only_object_norm005_seed65.log 2>/dev/null || echo \"NO_LOG\"\n   ```\n2. 如果 output JSON 存在且完整:\n   - 提取 overall_success_rate\n   - update_registry: conclusion=success, metrics={success_rate: X, total_rollouts: 100, successful_rollouts: Y}\n   - notes: \"Cron false positive confirmed. Output JSON 已存在，实验正常完成。\"\n3. 如果 JSON 不存在但日志显示 \"Results saved to\" + \"Overall success rate\":\n   - 同样提取 SR 并更新 registry\n4. 如果确认真正失败 → 记录失败原因到 notes\n\n## 环境\n- Python: `/root/miniconda3/bin/python`（conda base 环境）\n- 项目路径: `/root/acr-vla-conformal-refinement`\n",
    "tool_groups": "['ssh', 'registry']"
  }
}
````

</details>

---

### Tool result

_source line 37 · 2026-05-21T02:53:04.939784+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_diagnose_eval-obs-only-object-norm005-seed65_20260521T025256\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_diagnose_eval-obs-only-object-norm005-seed65_20260521T025256.log\", \"setup_data\": {}, \"message\": \"Worker worker_diagnose_eval-obs-only-object-norm005-seed65_20260521T025256 started. Use get_worker_status('worker_diagnose_eval-obs-only-object-norm005-seed65_20260521T025256') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 9832
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T02:53:16.424848+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-21T02:53:17.129631+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_6406d533.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "elapsed_ms": 704
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T02:53:17.407639+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['server', 'gpu']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['server', 'gpu']"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-21T02:53:33.963145+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm003-seed67\": {\"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\"}, \"eval-obs-only-object-norm005-seed67\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\"}, \"eval-obs-only-object-norm01-seed67\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\"}, \"eval-pi05-baseline-object-seed42\": {\"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\"}, \"eval-obs-only-object-norm003-seed66\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\"}, \"eval-obs-only-object-norm005-seed66\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\"}, \"eval-obs-only-object-norm01-seed66\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\"}, \"eval-obs-only-object-norm01-seed71\": {}, \"eval-obs-only-object-norm005-seed72\": {}, \"eval-obs-only-object-norm003-seed73\": {}, \"eval-obs-only-object-norm01-seed74\": {}, \"eval-obs-only-object-norm005-seed75\": {}, \"eval-obs-only-object-norm003-seed63-r2\": {}, \"eval-obs-only-object-norm003-seed62-r2\": {}, \"eval-obs-only-object-norm01-seed52-r3\": {}, \"eval-obs-only-object-norm01-seed51-r3\": {}, \"eval-obs-only-object-norm003-seed64\": {}, \"eval-obs-only-object-norm003-seed65\": {}, \"eval-obs-only-object-norm01-seed64\": {}, \"eval-obs-only-object-norm01-seed65\": {}, \"eval-obs-only-object-norm005-seed64\": {}}, \"count\": 21, \"total\": 21, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 16.4569}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 16555
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-21T02:53:40.400723+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-21T02:53:40.635545+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Glob",
  "elapsed_ms": 234
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-21T02:53:42.484457+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation*",
  "path": "/home/ubuntu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation*",
    "path": "/home/ubuntu"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-21T02:53:45.429874+00:00_

/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Glob",
  "elapsed_ms": 2945
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-21T02:53:47.509722+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-21T02:53:47.566961+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "elapsed_ms": 57
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-21T02:54:07.623365+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_project_resource_usage,mcp__agent-ml-research__load_project_config",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_project_resource_usage,mcp__agent-ml-research__load_project_config",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-21T02:54:07.677014+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "ToolSearch",
  "elapsed_ms": 53
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-21T02:54:10.191491+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-21T03:04:27.694093+00:00_

现在准备向 Director 汇报。先检查 GPU 分配情况。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-crm-object-k20-seed42"
}
```

</details>

---

## Round 2

44 recorded events

### User

_source line 52 · 2026-05-21T19:05:56.281023+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T19:06:35.622551+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read project state files",
  "subagent_type": "Explore",
  "prompt": "I need to understand the current state of the project \"acr-vla-conformal-refinement\". Read the following files and report their contents:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/report.md\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml\n5. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/experiment_plan.yaml\n6. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ideas.md\n7. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\n\nReport the full contents of each file. If a file doesn't exist, say so."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Agent",
  "tool_args": {
    "description": "Read project state files",
    "subagent_type": "Explore",
    "prompt": "I need to understand the current state of the project \"acr-vla-conformal-refinement\". Read the following files and report their contents:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/report.md\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml\n5. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/experiment_plan.yaml\n6. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ideas.md\n7. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\n\nReport the full contents of each file. If a file doesn't exist, say so."
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-21T19:06:37.834980+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/report.md"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-21T19:06:38.236655+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_6406d533.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-21T19:06:38.237090+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-21T19:06:38.489738+00:00_

1	# acr-vla-conformal-refinement — Research Dashboard
2	
3	> 最后更新: 2026-05-21 17:54 UTC | 更新原因: CRM training 启动 (Object cuda:0 + Spatial cuda:1 on bjb1-18228)
4	
5	> 详见 paper_framing.md（D077→D092→D097→D103→D104→D105）
6	
7	## 核心方向
8	**Adaptive inference-time compute for frozen VLAs** — K=2 L2 distance + selective CRM correction。Plan A = Pareto 最优。
9	
10	## 投稿目标
11	**CoRL 2026** DDL **2026-05-29**。剩余 **≤6 天**。
12	
13	## 阶段
14	**π0.5 CRM training RUNNING**。Precompute + merge 完成。SmolVLA 全部 LOCKED。π0.5 baseline LOCKED (D105)。
15	
16	## Plan A 核心结果 — SmolVLA (LOCKED)
17	| Benchmark | Plan A (K=2) | K=10 CRM | VLA-only | Δ vs VLA-only |
18	|-----------|-------------|----------|----------|---------------|
19	| Object    | 18.3%±2.1%  | 16.8%±1.8% | 10.8%±1.3% | +7.5pp |
20	| Spatial   | 35.0%±1.0%  | 34.5%±1.5% | 29.4%±1.5% | +5.6pp |
21	
22	## π0.5 Baseline (LOCKED, D105)
23	| Benchmark | VLA-only | vs SmolVLA |
24	|-----------|----------|------------|
25	| Object | **81.5%±0.5%** | +70.7pp |
26	| Spatial | **84.2%±1.0%** | +54.8pp |
27	
28	## K=20 Sweep (LOCKED, D102) → Table 5 ✅
29	K=20 ≈ K=2。Diminishing returns 确认。
30	
31	## Latency (LOCKED, D097)
32	CRM forward: 0.28ms | Plan A speedup: 1.82×
33	
34	## π0.5 CRM Pipeline 🔥
35	- ✅ D104: lerobot rsync + baseline eval 部署
36	- ✅ D105: Baseline LOCKED (Object 81.5%, Spatial 84.2%)
37	- ✅ Precompute 完成 + merge (Object 49,700 samples, Spatial 38,500 samples)
38	- 🔄 **RUNNING**: CRM training (bjb1-18228, Object cuda:0 PID 795874, Spatial cuda:1 PID 795051), ~4-7h
39	- ⏳ CRM Plan A eval (6 GPU, ~8h) — 命令已准备 (pi05_eval_commands.md)
40	- Ceiling effect 预期：81-85% baseline 上 CRM 增益有限，framing 准备"no-harm + selective improvement"
41	
42	## 论文状态
43	Figure 2 v4 ✅ | K=20 Table 5 ✅ | Spatial sweep ✅ | Latency ✅ | Per-DOF §4.4 ✅ | Random Selection ✅ | 编译 OK 15页
44	待写入: π0.5 cross-VLA 结果
45	
46	## GPU 状态
47	2/17 GPU 在跑 CRM training (bjb1-18228 cuda:0 Object, cuda:1 Spatial)。bjb1-18228 cuda:3 有旧 precompute 进程待清理。其余 14 GPU 空闲，等 CRM training 完成
…[truncated 2484 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-21T19:06:38.490211+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-21T19:06:38.692975+00:00_

1	# Project Memory
2	
3	## π0.5 Plan A Eval Commands (2026-05-21)
4	
5	### 验证结果
6	- Eval 脚本：`src/evaluate.py`（不是 `eval_crm.py`）
7	- `--crm_checkpoint` 是 `--checkpoint` 的别名（evaluate.py L505-507）
8	- `--obs_dim` 默认 960（SmolVLA），π0.5 **必须**传 `--obs_dim 2048`（evaluate.py L577-582 有 ValueError 校验）
9	- `--mode acr_vla` = `crm_perdof` 别名，是完整 ACR-VLA pipeline
10	- evaluate.py 无 `--cache_dir` 参数（只在 train_crm.py 中有）
11	- 输出文件自动命名：`logs/eval_{benchmark}_acr_vla_pi05_seed{seed}.json`
12	- π0.5 模型路径：`/root/autodl-tmp/models/pi05_libero_finetuned/`
13	
14	### CRM Training Checkpoint 路径约定
15	- train_crm.py `--output_dir` 默认 `/root/autodl-tmp/checkpoints/crm/`
16	- 最终 checkpoint：`{output_dir}/crm_best.pt`
17	- 已有的 SmolVLA CRM checkpoints：
18	  - perdof: `/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt`
19	  - obs_only: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`
20	
21	### 代码同步警告
22	- bjb2-28827 的 evaluate.py (30140 bytes, May 21 05:39) 版本旧于 bjb1-32546 (33058 bytes, May 21 23:49)
23	- eval 前必须在 bjb2-28827 做 git pull 同步代码
24	
25	### 服务器 GPU 配置
26	- bjb1-18228: 4 GPU (cuda:0-3)，CRM training 目标机
27	- bjb1-32546: 6 GPU (cuda:0-5)
28	- bjb2-28827: 6 GPU (cuda:0-5)
29	
30	### 环境变量模板
31	```
32	HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl
33	```
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-21T19:06:38.693528+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-21T19:06:38.896460+00:00_

File content (875.6KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-21T19:06:38.896889+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/experiment_plan.yaml"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-21T19:06:39.097865+00:00_

1	experiments:
2	- id: plan_100
3	  claim: 1
4	  description: obs_only ε=0.2 multi-seed evaluation on LIBERO Object (6 seeds). Core
5	    evidence for pipeline improvement over argmin baseline.
6	  priority: P0
7	  gpu_budget_hours: 36
8	  deps: []
9	  registry_id: eval-obs-only-object-norm02-seed42
10	  notes: '6v6 pooled: 105/600 (17.5%) vs argmin 74/600 (12.3%), Fisher p=0.0074, Cohen''s
11	    d=1.21'
12	- id: plan_101
13	  claim: 1
14	  description: argmin baseline (reconvla K=10) multi-seed evaluation on LIBERO Object
15	    (6 seeds).
16	  priority: P0
17	  gpu_budget_hours: 36
18	  deps: []
19	  registry_id: eval-reconvla-object
20	  notes: 'seeds 42/43/44/45/46/47 = 12/17/13/12/10/10. registry: eval-reconvla-object
21	    (seed42), eval-argmin-object-seed43..seed47'
22	- id: plan_102
23	  claim: 1
24	  description: VLA-only (K=1, no CRM) multi-seed baseline on LIBERO Object.
25	  priority: P0
26	  gpu_budget_hours: 24
27	  deps: []
28	  registry_id: eval-vla-only-object
29	  notes: 'seeds 42/43/44/45/46/47 = 12/12/10/9/11/9%, mean 10.8%. registry: eval-vla-only-object
30	    (seed42), eval-vla-only-object-seed43..seed47'
31	- id: plan_103
32	  claim: 1
33	  description: Direct correction ablation (K=1 CRM, no conformal selection). Tests
34	    whether CRM alone suffices.
35	  priority: P1
36	  gpu_budget_hours: 6
37	  deps: []
38	  registry_id: eval-direct-correction-object-seed42-r3
39	  notes: seed42 = 14% (r3), not significant vs VLA-only. Confirms K=10 selection is
40	    necessary.
41	- id: plan_200
42	  claim: 2
43	  description: 'obs_only magnitude sweep: ε ∈ {0.03, 0.05, 0.1, 0.2, 0.3, default}
44	    on LIBERO Object, multi-seed.'
45	  priority: P0
46	  gpu_budget_hours: 60
47	  deps: []
48	  registry_id: eval-obs-only-object-norm02-seed42
49	  notes: Stable 15-17.5% across all norms. ε=0.2 is peak (6-seed mean 17.5%).
50	- id: plan_201
51	  claim: 2
52	  description: 'perdof magnitude sweep: ε ∈ {0.03, 0.05, 0.1, 0.2, 0.3, default} on
53	    LIBER
…[truncated 6451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-21T19:06:39.098348+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ideas.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ideas.md"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-21T19:06:39.249334+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_6406d533.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-21T19:06:39.299969+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-21T19:06:39.658244+00:00_

1	# Paper Framing — acr-vla-conformal-refinement
2	
3	> Last updated: 2026-05-21 | D090+: Random Selection Spatial 双 benchmark 验证完成, C1 component decomposition 补充 Spatial 维度
4	
5	## Target Venue
6	- **CoRL 2026** (DDL **2026-05-29** per ROADMAP; ⚠️ previously said ~Jun 2 — need user confirmation)
7	- Framing: Analysis paper — inference-time correction dissection + mechanism insights (D065 reframe)
8	- Title: "Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs"
9	
10	## Core Insight (D065 revised)
11	Learned correction is the active mechanism that improves frozen VLA policies, but multi-sampling is an enabling condition: it provides a centered starting point within the CRM's bounded correction radius. Neither works alone — K=1 correction performs below baseline (10.3% vs 10.8%), and selection without correction matches baseline. The improvement (+5.8pp, 16.8% vs 10.8%, K=10 n=7 excl. seed42 per D084; K=5: 15.5%) emerges from correction operating on a multi-sample-centered input. Batched inference (D067) eliminates K as a latency factor (~170ms for all K on RTX 4090). The conditioning-magnitude interaction determines success vs catastrophic failure: observation features yield robust corrections (13.4-16.8% across all ε), while conformal per-DOF features cause progressive collapse (14%→0%). This pipeline requires stochastic VLA action diversity as a prerequisite. **D069 boundary**: CRM correction is task-specific — on held-out tasks (LTO), CRM actively degrades VLA (2% vs 14%), revealing that correction quality is bounded by calibration data coverage. Cross-benchmark results (Spatial K=10: 34.5%±1.5%, n=9) are in-distribution (CRM trained on all 20 tasks). **Adaptive K (D076)**: P50 threshold achieves 15.3% at avg_K=3.8 (~91% of fixed K=10). **OpenVLA (D087)**: v2 baseline 69%, CRM training complete (plan_802).
12	
13	## Headline Metrics
14	- **K=5 CRM obs_only (PRIMARY, D066)**: 16.0%±2.2% (n=7, seeds 42-48=[14,19,17,15,16,13,18]; J
…[truncated 25148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "elapsed_ms": 358
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-21T19:06:58.896773+00:00_

## Project Status Summary

**Project:** acr-vla-conformal-refinement  
**Target:** CoRL 2026 (DDL: **2026-05-29** — **≤8 days remaining**)  
**Current Phase:** π0.5 CRM training RUNNING

---

### File Status

1. **report.md** ✅ exists — Last updated 2026-05-21 17:54 UTC
2. **ROADMAP.md** ✅ exists — Comprehensive dashboard showing core direction, phase status, GPU allocation
3. **memory.md** ✅ exists — Execution notes: eval script paths, checkpoint conventions, server configs, environment templates
4. **registry.yaml** ❌ **File exceeds 256KB** — Cannot read full contents. Contains all experiment records. Use offset/limit if needed.
5. **experiment_plan.yaml** ✅ exists — 31 plan entries (plan_100 to plan_803), organized by claims with status/GPU budgets
6. **ideas.md** ❌ **File does not exist**
7. **paper_framing.md** ✅ exists — Comprehensive framing (272 lines): 3 core claims, D090 Plan A in progress, hard evidence locked

---

### Core Research Status

**Headline:** Adaptive inference-time compute for frozen VLAs with K=2 L2 distance + selective CRM correction.

**Plan A Results (LOCKED — SmolVLA):**
| Benchmark | Plan A (K=2) | K=10 CRM | VLA-only | Δ |
|-----------|----------|----------|----------|--------|
| Object    | 18.3%±2.1% | 16.8%±1.8% | 10.8%±1.3% | **+7.5pp** |
| Spatial   | 35.0%±1.0% | 34.5%±1.5% | 29.4%±1.5% | **+5.6pp** |

**π0.5 Baseline (LOCKED):**
| Benchmark | VLA-only | vs SmolVLA |
|-----------|----------|-----------|
| Object    | **81.5%±0.5%** | +70.7pp |
| Spatial   | **84.2%±1.0%** | +54.8pp |

---

### Current Work (π0.5 CRM Training RUNNING 🔥)
- **Status:** CRM training on bjb1-18228 (Object cuda:0 PID 795874, Spatial cuda:1 PID 795051)
- **ETA:** ~4-7h
- **Next:** CRM Plan A eval (6 GPU, ~8h) — commands prepared in memory.md
- **GPU:** 2/17 in use; 14 idle for eval phase

---

### Key Decisions (Last 3 Days)

| ID | Date | Summary | Status |
|----|------|---------|--------|
| **D105** | 2026-05-21 | π0.5 VLA-only baseline LOCKED (Objec
…[truncated 1770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Agent",
  "elapsed_ms": 23274
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-21T19:07:04.478213+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read memory.md and ROADMAP details",
  "subagent_type": "Explore",
  "prompt": "Read these files carefully and report their full contents:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md — read all of it (use offset/limit if needed, it may be large)\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md — read all of it\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/report.md — read all of it\n\nFocus on: server names, GPU IDs, active processes, working directories, Python paths, model paths, dataset paths, cron tasks, and any infrastructure details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Agent",
  "tool_args": {
    "description": "Read memory.md and ROADMAP details",
    "subagent_type": "Explore",
    "prompt": "Read these files carefully and report their full contents:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md — read all of it (use offset/limit if needed, it may be large)\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md — read all of it\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/report.md — read all of it\n\nFocus on: server names, GPU IDs, active processes, working directories, Python paths, model paths, dataset paths, cron tasks, and any infrastructure details."
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-21T19:07:06.839481+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-21T19:07:07.040622+00:00_

1	# Project Memory
2	
3	## π0.5 Plan A Eval Commands (2026-05-21)
4	
5	### 验证结果
6	- Eval 脚本：`src/evaluate.py`（不是 `eval_crm.py`）
7	- `--crm_checkpoint` 是 `--checkpoint` 的别名（evaluate.py L505-507）
8	- `--obs_dim` 默认 960（SmolVLA），π0.5 **必须**传 `--obs_dim 2048`（evaluate.py L577-582 有 ValueError 校验）
9	- `--mode acr_vla` = `crm_perdof` 别名，是完整 ACR-VLA pipeline
10	- evaluate.py 无 `--cache_dir` 参数（只在 train_crm.py 中有）
11	- 输出文件自动命名：`logs/eval_{benchmark}_acr_vla_pi05_seed{seed}.json`
12	- π0.5 模型路径：`/root/autodl-tmp/models/pi05_libero_finetuned/`
13	
14	### CRM Training Checkpoint 路径约定
15	- train_crm.py `--output_dir` 默认 `/root/autodl-tmp/checkpoints/crm/`
16	- 最终 checkpoint：`{output_dir}/crm_best.pt`
17	- 已有的 SmolVLA CRM checkpoints：
18	  - perdof: `/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt`
19	  - obs_only: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`
20	
21	### 代码同步警告
22	- bjb2-28827 的 evaluate.py (30140 bytes, May 21 05:39) 版本旧于 bjb1-32546 (33058 bytes, May 21 23:49)
23	- eval 前必须在 bjb2-28827 做 git pull 同步代码
24	
25	### 服务器 GPU 配置
26	- bjb1-18228: 4 GPU (cuda:0-3)，CRM training 目标机
27	- bjb1-32546: 6 GPU (cuda:0-5)
28	- bjb2-28827: 6 GPU (cuda:0-5)
29	
30	### 环境变量模板
31	```
32	HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl
33	```
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-21T19:07:07.041186+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-21T19:07:07.242279+00:00_

1	# acr-vla-conformal-refinement — Research Dashboard
2	
3	> 最后更新: 2026-05-21 17:54 UTC | 更新原因: CRM training 启动 (Object cuda:0 + Spatial cuda:1 on bjb1-18228)
4	
5	> 详见 paper_framing.md（D077→D092→D097→D103→D104→D105）
6	
7	## 核心方向
8	**Adaptive inference-time compute for frozen VLAs** — K=2 L2 distance + selective CRM correction。Plan A = Pareto 最优。
9	
10	## 投稿目标
11	**CoRL 2026** DDL **2026-05-29**。剩余 **≤6 天**。
12	
13	## 阶段
14	**π0.5 CRM training RUNNING**。Precompute + merge 完成。SmolVLA 全部 LOCKED。π0.5 baseline LOCKED (D105)。
15	
16	## Plan A 核心结果 — SmolVLA (LOCKED)
17	| Benchmark | Plan A (K=2) | K=10 CRM | VLA-only | Δ vs VLA-only |
18	|-----------|-------------|----------|----------|---------------|
19	| Object    | 18.3%±2.1%  | 16.8%±1.8% | 10.8%±1.3% | +7.5pp |
20	| Spatial   | 35.0%±1.0%  | 34.5%±1.5% | 29.4%±1.5% | +5.6pp |
21	
22	## π0.5 Baseline (LOCKED, D105)
23	| Benchmark | VLA-only | vs SmolVLA |
24	|-----------|----------|------------|
25	| Object | **81.5%±0.5%** | +70.7pp |
26	| Spatial | **84.2%±1.0%** | +54.8pp |
27	
28	## K=20 Sweep (LOCKED, D102) → Table 5 ✅
29	K=20 ≈ K=2。Diminishing returns 确认。
30	
31	## Latency (LOCKED, D097)
32	CRM forward: 0.28ms | Plan A speedup: 1.82×
33	
34	## π0.5 CRM Pipeline 🔥
35	- ✅ D104: lerobot rsync + baseline eval 部署
36	- ✅ D105: Baseline LOCKED (Object 81.5%, Spatial 84.2%)
37	- ✅ Precompute 完成 + merge (Object 49,700 samples, Spatial 38,500 samples)
38	- 🔄 **RUNNING**: CRM training (bjb1-18228, Object cuda:0 PID 795874, Spatial cuda:1 PID 795051), ~4-7h
39	- ⏳ CRM Plan A eval (6 GPU, ~8h) — 命令已准备 (pi05_eval_commands.md)
40	- Ceiling effect 预期：81-85% baseline 上 CRM 增益有限，framing 准备"no-harm + selective improvement"
41	
42	## 论文状态
43	Figure 2 v4 ✅ | K=20 Table 5 ✅ | Spatial sweep ✅ | Latency ✅ | Per-DOF §4.4 ✅ | Random Selection ✅ | 编译 OK 15页
44	待写入: π0.5 cross-VLA 结果
45	
46	## GPU 状态
47	2/17 GPU 在跑 CRM training (bjb1-18228 cuda:0 Object, cuda:1 Spatial)。bjb1-18228 cuda:3 有旧 precompute 进程待清理。其余 14 GPU 空闲，等 CRM training 完成
…[truncated 2484 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-21T19:07:07.242785+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/report.md"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-21T19:07:07.293424+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_6406d533.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-21T19:07:09.587374+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ 2>&1 | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/ 2>&1 | head -20"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-21T19:07:09.939781+00:00_

total 1752
drwxr-xr-x 27 ubuntu ubuntu  12288 May 21 17:39 .
drwxr-xr-x 11 ubuntu ubuntu   4096 May 21 18:56 ..
drwxr-xr-x  2 ubuntu ubuntu   4096 May 15 19:42 __pycache__
drwxr-xr-x  7 ubuntu ubuntu   4096 May 15 13:59 _project
-rw-r--r--  1 ubuntu ubuntu   3070 May 14 21:27 ablation_eval_commands.md
-rw-r--r--  1 ubuntu ubuntu  19401 May 19 16:38 adaptive_k_design.md
drwxr-xr-x  3 ubuntu ubuntu   4096 May 15 20:27 analysis
-rw-r--r--  1 ubuntu ubuntu  16980 May 15 19:52 analysis_magnitude_sweep.py
-rw-r--r--  1 ubuntu ubuntu  12173 May 15 19:43 analysis_object_benchmark.py
-rw-r--r--  1 ubuntu ubuntu  13612 May 15 19:52 analysis_spatial_final.py
-rw-r--r--  1 ubuntu ubuntu   1624 May 16 15:09 argmin_seed44_r2_results.json
-rw-r--r--  1 ubuntu ubuntu   6500 May 19 04:09 batched_inference_feasibility_report.md
-rw-r--r--  1 ubuntu ubuntu  14353 May 20 07:23 benchmark_data_audit.md
-rw-r--r--  1 ubuntu ubuntu  12311 May 19 16:43 benchmark_survey.md
-rw-r--r--  1 ubuntu ubuntu  12204 May 15 20:21 citation_attribution_audit.md
-rw-r--r--  1 ubuntu ubuntu   9138 May 15 20:30 citation_audit_report.md
-rw-r--r--  1 ubuntu ubuntu   7036 May 15 01:48 competitive_analysis_20260515.md
-rw-r--r--  1 ubuntu ubuntu  15772 May 14 07:18 competitor_analysis.md
-rw-r--r--  1 ubuntu ubuntu   1782 May 17 02:15 conclusion_draft.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Bash",
  "elapsed_ms": 352
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-21T19:07:12.355717+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement -name \"report.md\" -o -name \"*.yaml\" -o -name \"paper_framing.md\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement -name \"report.md\" -o -name \"*.yaml\" -o -name \"paper_framing.md\" 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-21T19:07:12.406474+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T015051/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T015051/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T015051/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/worst/imagined_exp
…[truncated 784 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-21T19:07:14.362754+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-21T19:07:14.715360+00:00_

1	# Handover — 2026-05-21
2	
3	> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4	
5	## 运行中
6	| exp_id | 假设 | 状态 | 关键指标 | W&B |
7	|--------|------|------|---------|-----|
8	| crm-train-pi05-object-full | CRM projection trained on π0.5 full precomputed features (69303 object samples, K=10) will learn conformal refinement corrections improving upon π0.5 VLA-only baseline (81.5%) on LIBERO-Object, validating cross-VLA generalization | — | — | — |
9	
10	## 待处理
11	- crm-train-pi05-spatial-full（准备中）
12	- crm-pipeline-auto（准备中）
13	- …另有 83 项
14	
15	## 近期结论
16	- **crm-train-pi05-spatial** (killed): CRM projection trained on π0.5 precomputed features (38500 spatial samples, K=10) will learn to predict conformal refinement corrections that improve upon π0.5 VLA-only baseline (84.2%) on LIBERO-Spatial, validating cross-VLA generalization of CRM beyond SmolVLA
17	
18	## 趋势
19	成功 333 / 负向 38 / 失败 61 / 共 525
20	n_tasks: 10 →（近 3 次 success）
21	success_rate: 0.85 ↑（近 3 次 success）
22	
23	## 下一步
24	（无活跃 idea，请通过 ideas.md 添加）
25	
26	## 资源状态
27	bjb1-18228: 无 GPU 信息
28	bjb1-32546: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5
29	bjb2-28827: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5
30	bjb2-40593: 无 GPU 信息
31	
32	## 告警
33	- plan_001-crm-smolvla: 训练失败 — unknown
34	- plan_014-reconvla-baseline: 训练失败 — unknown
35	- eval-smolvla-libero-spatial: 训练失败 — unknown
36	- eval-spatial-reeval-v2: 已被终止 — unknown
37	- precompute-v2-shard0: 已被终止 — unknown
38	- precompute-v2-shard1: 已被终止 — unknown
39	- precompute-v2-shard2: 已被终止 — unknown
40	- eval-spatial-v3-full: 已被终止 — unknown
41	- precompute-v3-shard0: 已被终止 — unknown
42	- precompute-v3-shard1: 已被终止 — unknown
43	- precompute-v3-shard2: 已被终止 — unknown
44	- eval-spatial-v4-full: 已被终止 — unknown
45	- eval-object-v4-full: 已被终止 — unknown
46	- eval-spatial-v5-full: 已被终止 — unknown
47	- crm-train-v1: 已被终止 — unknown
48	- eval-reconvla-spatial-v1: 已被终止 — unknown
49	- eval-reconvla-spatial-v2: 已被终止 — unknown
50	- eval-acr-spatial-v1: 已被终止 — unknown
51	- crm-train-a
…[truncated 5197 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-21T19:07:14.765965+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-21T19:07:15.171794+00:00_

1	# Paper Framing — acr-vla-conformal-refinement
2	
3	> Last updated: 2026-05-21 | D090+: Random Selection Spatial 双 benchmark 验证完成, C1 component decomposition 补充 Spatial 维度
4	
5	## Target Venue
6	- **CoRL 2026** (DDL **2026-05-29** per ROADMAP; ⚠️ previously said ~Jun 2 — need user confirmation)
7	- Framing: Analysis paper — inference-time correction dissection + mechanism insights (D065 reframe)
8	- Title: "Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs"
9	
10	## Core Insight (D065 revised)
11	Learned correction is the active mechanism that improves frozen VLA policies, but multi-sampling is an enabling condition: it provides a centered starting point within the CRM's bounded correction radius. Neither works alone — K=1 correction performs below baseline (10.3% vs 10.8%), and selection without correction matches baseline. The improvement (+5.8pp, 16.8% vs 10.8%, K=10 n=7 excl. seed42 per D084; K=5: 15.5%) emerges from correction operating on a multi-sample-centered input. Batched inference (D067) eliminates K as a latency factor (~170ms for all K on RTX 4090). The conditioning-magnitude interaction determines success vs catastrophic failure: observation features yield robust corrections (13.4-16.8% across all ε), while conformal per-DOF features cause progressive collapse (14%→0%). This pipeline requires stochastic VLA action diversity as a prerequisite. **D069 boundary**: CRM correction is task-specific — on held-out tasks (LTO), CRM actively degrades VLA (2% vs 14%), revealing that correction quality is bounded by calibration data coverage. Cross-benchmark results (Spatial K=10: 34.5%±1.5%, n=9) are in-distribution (CRM trained on all 20 tasks). **Adaptive K (D076)**: P50 threshold achieves 15.3% at avg_K=3.8 (~91% of fixed K=10). **OpenVLA (D087)**: v2 baseline 69%, CRM training complete (plan_802).
12	
13	## Headline Metrics
14	- **K=5 CRM obs_only (PRIMARY, D066)**: 16.0%±2.2% (n=7, seeds 42-48=[14,19,17,15,16,13,18]; J
…[truncated 25148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-21T19:07:39.161621+00:00_

Perfect. I now have comprehensive visibility into the project infrastructure. Here's the complete summary:

---

## Project Infrastructure Summary — acr-vla-conformal-refinement (2026-05-21)

### **Servers & GPU Configuration**
| Server | Total GPUs | GPU Range | Status | Notes |
|--------|-----------|-----------|--------|-------|
| **bjb1-18228** | 4 | cuda:0-3 | 2 active (CRM training) | CRM training hub: Object on cuda:0, Spatial on cuda:1; cuda:3 has old precompute process pending cleanup |
| **bjb1-32546** | 6 | cuda:0-5 | All idle | General evaluation server |
| **bjb2-28827** | 6 | cuda:0-5 | All idle | Evaluation server; needs code git pull before eval (evaluate.py version lag) |
| **bjb2-40593** | Unknown | — | Unknown | Referenced in memory but limited info |

### **Active Processes (CRM Training — RUNNING)**
```
bjb1-18228:
  - Object CRM training:  PID 795874, cuda:0, est. 4-7h remaining
  - Spatial CRM training: PID 795051, cuda:1, est. 4-7h remaining
  - [STALE] cuda:3 old precompute process awaiting cleanup
```

### **Environment Setup**
**Environment variables (required for all runs):**
```bash
HF_HOME=/root/autodl-tmp/.hf_cache
HF_HUB_OFFLINE=1
TRANSFORMERS_OFFLINE=1
MUJOCO_GL=egl
```

**Python paths:**
- Evaluation script: `/root/` (project root, via rsync to bjb machines)
- Executable: `src/evaluate.py` (not `eval_crm.py`)
- Training: `src/train_crm.py`

### **Model & Data Paths**

**π0.5 Model (SmolVLA):**
- Path: `/root/autodl-tmp/models/pi05_libero_finetuned/`
- **Critical**: Must pass `--obs_dim 2048` to evaluate.py (default 960 is for SmolVLA, π0.5 requires 2048 or ValueError)

**CRM Training Checkpoints:**
- Output default: `/root/autodl-tmp/checkpoints/crm/`
- Final checkpoint: `{output_dir}/crm_best.pt`
- Existing v3 checkpoints:
  - Per-DOF: `/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt`
  - Obs-only: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`

**Precomputed CRM Training Data:**
- Object: 49,700 samples
…[truncated 2588 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Agent",
  "elapsed_ms": 34683
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-21T19:07:41.974184+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-21T19:07:42.024949+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-21T19:07:44.893469+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-21T19:07:44.893875+00:00_

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
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-21T19:07:47.005137+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"crm-train-pi05-object-full\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:26:52.186Z\", \"updated_at\": \"2026-05-21T18:56:42.883Z\", \"hypothesis\": \"CRM projection trained on π0.5 full precomputed features (69303 object samples, K=10) will learn conformal refinement corrections improving upon π0.5 VLA-only baseline (81.5%) on LIBERO-Object, validating cross-VLA generalization\", \"spec\": {\"command\": \"nohup env CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --benchmark object --cache_dir /root/autodl-tmp/crm_cache_pi05/ --output_dir /root/autodl-tmp/checkpoints/crm_pi05_full/object/ --epochs 50 --batch_size 32 --lr 1e-3 --obs_dim 2048\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 800111, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05/object/\", \"data_count\": 69303, \"model_name\": \"crm-pi05-object-full\", \"seed\": 42, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-pi05-object-full.log\"}, \"notes\": \"Training with 69,303 samples (95.6%). Full data available: 72,159 samples (99.5%, shard0 missing ~351 due to kill). Per Director: ≥98% means current checkpoint acceptable. No retrain needed.\"}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0891}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2111
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-21T19:07:53.236713+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 1, \"results\": [{\"exp_id\": \"crm-train-pi05-object-full\", \"success\": true, \"actions\": [\"Job still running (pid=800111)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 8342
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-21T19:07:56.199120+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'PREPARING'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'PREPARING'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-21T19:07:58.069365+00:00_

Error: result (79,524 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-6406d533/e7aaf1f8-9249-43c1-be10-09202b2e283a/tool-results/mcp-agent-ml-research-read_registry-1779390478013.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-6406d533/e7aaf1f8-9249-43c1-be10-09202b2e283a/tool-results/mcp-agent-ml-research-read_registry-1779390478013.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1870
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-21T19:08:03.216028+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-6406d533/e7aaf1f8-9249-43c1-be10-09202b2e283a/tool-results/mcp-agent-ml-research-read_registry-1779390478013.txt | python3 -c \"import json,sys; d=json.loads(json.loads(sys.stdin.read())['result']); exps=d['data']['experiments']; print(f'Count: {len(exps)}'); [print(f'  {k}: {v.get(\\\"hypothesis\\\",\\\"?\\\")[:80]}') for k,v in exps.items()]\"",
  "description": "Parse PREPARING experiments from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-6406d533/e7aaf1f8-9249-43c1-be10-09202b2e283a/tool-results/mcp-agent-ml-research-read_registry-1779390478013.txt | python3 -c \"import json,sys; d=json.loads(json.loads(sys.stdin.read())['result']); exps=d['data']['experiments']; print(f'Count: {len(exps)}'); [print(f'  {k}: {v.get(\\\"hypothesis\\\",\\\"?\\\")[:80]}') for k,v in exps.items()]\"",
    "description": "Parse PREPARING experiments from registry"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-21T19:08:03.316953+00:00_

Count: 85
  crm-train-pi05-spatial-full: CRM projection trained on π0.5 full precomputed features (~60250 spatial samples
  crm-pipeline-auto: ?
  precompute-pi05-obj-s6-r2: ?
  precompute-pi05-obj-s9-r2: ?
  precompute-pi05-obj-s8-r2: ?
  precompute-pi05-obj-s7-r2: ?
  precompute-pi05-obj-s0-r2: ?
  precompute-pi05-obj-s5-r2: ?
  precompute-pi05-obj-s4-r2: ?
  precompute-pi05-obj-s3-r2: ?
  precompute-pi05-obj-s2-r2: ?
  precompute-pi05-obj-s1-r2: ?
  precompute-pi05-obj-s9-fix: ?
  precompute-pi05-obj-s8-fix: ?
  precompute-pi05-obj-s7-fix: ?
  precompute-pi05-obj-s6-fix: ?
  precompute-pi05-obj-s5-fix: ?
  precompute-pi05-obj-shard9: ?
  precompute-pi05-obj-shard8: ?
  precompute-pi05-obj-shard7: ?
  precompute-pi05-obj-shard6: ?
  precompute-pi05-obj-shard5: ?
  precompute-pi05-spatial-shard6: ?
  precompute-pi05-spatial-shard5: ?
  precompute-pi05-spatial-shard4: ?
  precompute-pi05-spatial-shard3: ?
  precompute-pi05-spatial-shard2: ?
  precompute-pi05-spatial-shard1: ?
  precompute-pi05-spatial-shard0: ?
  precompute-pi05-shard0: π0.5 CRM feature precompute (shard 0/6). Extract 2048D obs features + K=10 actio
  precompute-pi05-shard9: π0.5 CRM feature precompute (shard 9/10). Extract 2048D obs features + K=10 acti
  precompute-pi05-shard8: π0.5 CRM feature precompute (shard 8/10). Extract 2048D obs features + K=10 acti
  precompute-pi05-shard7: π0.5 CRM feature precompute (shard 7/10). Extract 2048D obs features + K=10 acti
  precompute-pi05-shard6: π0.5 CRM feature precompute (shard 6/10). Extract 2048D obs features + K=10 acti
  precompute-pi05-shard5: ?
  precompute-pi05-shard4: ?
  precompute-pi05-shard3: ?
  precompute-pi05-shard2: ?
  precompute-pi05-shard1: ?
  precompute-pi05-features-object: Precompute π0.5 2048D obs_features + K=10 action samples from LIBERO demos for C
  eval-pi05-baseline-object-seed42-r2: π0.5 VLA-only baseline on LIBERO-Object seed42 (r2). Fix: corrected QUANTILES→ME
  eval-random-selection-object-seed42-r3: Random Selection (K=
…[truncated 4086 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-crm-object-k20-seed42",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---

### Assistant

_source line 95 · 2026-05-21T19:08:56.453040+00:00_

Now I have enough context. The key findings:
- **1 RUNNING experiment**: `crm-train-pi05-object-full` (PID 800111, cuda:0, bjb1-18228)
- **`crm-train-pi05-spatial-full` is in PREPARING** (not RUNNING) — it may have completed or needs attention
- 85 PREPARING experiments (mostly old precompute shards and eval experiments)
- Cron reconciliation found only 1 active cron (the object training)

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单必须从 `get_project_status` 的 `execution.gpu_ids` 获取，不能假设。当前服务器 bjb1-18228 / bjb1-32546 / bjb2-28827 各有分配
- π0.5 评估必须传 `--obs_dim 2048`（默认 960 是 SmolVLA 用的，π0.5 传错会 ValueError）
- bjb2-28827 的 evaluate.py 是旧版（May 21 05:39），**必须 git pull 后才能跑 eval**，否则结果不可信
- CoRL 2026 DDL = **2026-05-29**，≤8 天，所有决策以此为锚
- evaluate.py 用 `--checkpoint`（不是 `--crm_checkpoint`），`--mode acr_vla` = crm_perdof pipeline

### 2. 🖥️ 基础设施快照
- **bjb1-18228**（4 GPU）：CRM 训练主机，工作目录 /root/，Python 在 conda base
  - 活跃：crm-train-pi05-object-full PID 800111 cuda:0（cron 监控中）
  - cuda:3 有旧 precompute 进程待清理
- **bjb1-32546**（6 GPU）：eval 服务器，全部空闲，代码已同步
- **bjb2-28827**（6 GPU）：eval 服务器，全部空闲，**代码待 git pull**
- 环境变量：`HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl`
- π0.5 模型：`/root/autodl-tmp/models/pi05_libero_finetuned/`
- CRM v3 checkpoints：`/root/autodl-tmp/checkpoints/crm_v3_norm/{perdof,obs_only}/crm_best.pt`
- π0.5 CRM 训练输出：`/root/autodl-tmp/checkpoints/crm_pi05_full/{object,spatial}/`
- 预计算数据：`/root/autodl-tmp/crm_cache_pi05/{object,spatial}/`（Object 69303, Spatial ~60250 samples）
- eval 命令模板已写入 memory.md "π0.5 Plan A Eval Commands" 段

### 3. 📊 当前状态
- **刚完成的关键里程碑**：π0.5 VLA-only baseline LOCKED（D105: Object 81.5%±0.5%, Spatial 84.2%±1.0%）；SmolVLA Plan A 全部 LOCKED；K=20 sweep LOCKED（D102）
- **RUNNING**：`crm-train-pi05-object-full`（bjb1-18228 cuda:0 PID 800111，~50 epochs，预计 4-7h 从 18:26 UTC 开始）
- **异常**：`crm-train-pi05-spatial-full` 状态为 PREPARING 而非 RUNNING——reconcile_crons 未发现它的 cron。**需要检查**：它是否已完成（checkpoint 存在？）、是否从未成功提交、还是进程已退出。这是立即要处理的第一件事
- **等待中**：CRM 训练完成后 → 部署 π0.5 CRM Plan A eval（6 GPU, ~8h, 3 seeds × 2 benchmarks）
- **GPU 利用率**：2/17（仅 object 训练 1 GPU 确认活跃），14+ GPU 空闲等 eval

### 4. 📋 待办（条件触发式）
- **立即**：检查 `crm-train-pi05-spatial-full` 状态 → 若未启动则立即提交；若已完成则更新 registry → DONE
- `crm-train-pi05-object-full` cron 回调（进程退出）→ spawn Worker 验证 checkpoint → 更新 registry → DONE/ANALYZING
- Object + Spatial CRM 训练均完成 → **立即**部署 π0.5 CRM Plan A eval 到 bjb1-32546 + bjb2-28827（先 git pull bjb2-28827）
- π0.5 CRM eval 全部完成 → 汇总结果 → 更新 report.md → 汇报 Director → 启动 Paper Agent 写 π0.5 cross-VLA section
- 若 π0.5 CRM 在 81-85% baseline 上 gain < 2pp → framing 已准备 "no-harm + selective improvement" narrative（见 paper_framing.md）
- eval 跑完 GPU 释放后 → OpenVLA CRM eval（plan_802）如时间允许

### 5. 🎯 战略上下文
- **核心 story**：Adaptive inference-time compute for frozen VLAs。K=2 L2 distance 近似替代 K=10 variance（ρ=0.9979），加上 selective CRM correction = Plan A
- **三大 claim**：C1 Correction > Selection（已证）；C2 Conditioning-Magnitude Interaction（obs_only stable, perdof collapse）；C3 Applicability Boundaries（diversity prerequisite + task proximity）
- **D090 Plan A** 是当前执行路线：SmolVLA 已 LOCKED，π0.5 cross-VLA generalization 是最后一块拼图
- **最容易判断错的事**：π0.5 baseline 81-85% 有天花板效应，CRM 的绝对 gain 可能很小。不要把"绝对 gain 小"等同于"方法无效"——framing 已转向 "no-harm + selective improvement on hard subtasks"，准备按此 narrative 写
- **Spatial CRM 训练状态不明** 是最紧急的问题——如果它没跑，距 DDL 又少了半天
- **决策链关键节点**：D076（Adaptive K 验证）→ D090（Plan A 路线确认）→ D102（K=20 diminishing returns）→ D104（π0.5 baseline eval 部署）→ D105（baseline LOCKED）→ 当前：CRM 训练 → eval → paper
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-crm-object-k20-seed42"
}
```

</details>

---
