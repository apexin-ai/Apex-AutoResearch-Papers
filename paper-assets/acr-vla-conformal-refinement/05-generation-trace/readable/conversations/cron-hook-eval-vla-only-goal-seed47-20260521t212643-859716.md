# cron hook eval vla only goal seed47 20260521T212643 859716

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 133
- **Recorded user turns:** 2
- **Tool calls:** 67
- **Original source:** `logs/chats/archive/cron_hook_eval-vla-only-goal-seed47_20260521T212643_859716.jsonl`
- **Structured JSON:** [`d63169eafd1469dab8d4.json`](../../sessions/d6/d63169eafd1469dab8d4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

93 recorded events

### User

_source line 1 · 2026-05-21T04:21:30.842635+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #23。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单由 Director 通过 `get_project_status` 的 `execution.gpu_ids` 控制，当前项目跨 4 台服务器（bjb1-18228, bjb1-32546, bjb2-28827, bjb2-40593），每台可用 GPU 需实时查
- bjb2-40593 系统盘已用 90%（46G/437G 可用）⚠️ 不要在该服务器启动新实验或下载大文件
- eval 实验 `--mode` 参数（vla_only / obs_only / obs_only_norm02 / perdof / argmin / adaptive_k 等）必须与 registry hypothesis 一致，不可混用
- Table 1 Object CRM 只用 norm02 配置（D080），seed42 的 norm02 结果（SR=20%）因异常偏高被 D084 排除，不纳入统计
- CoRL 2026 DDL: **2026-05-29**，剩余 ~8 天

### 2. 🖥️ 基础设施快照
- **bjb2-28827**: `/root/acr-vla-conformal-refinement/`, conda base (`/root/miniconda3/bin/python`), 6× RTX 4090, 磁盘 399G/439G 可用
- **bjb1-32546**: `/root/acr-vla-conformal-refinement/`, conda base, 6× RTX 4090, 磁盘 400G/438G 可用
- **bjb1-18228**: `/root/acr-vla-conformal-refinement/`, conda base, 磁盘 400G/438G 可用
- **bjb2-40593**: 磁盘紧张（90%），慎用
- 模型: SmolVLA at `/root/autodl-tmp/models/smolvla_libero`（各服务器）
- W&B: 项目 `acr-vla-conformal-refinement`
- 活跃 cron（13 个）: 见 reconcile 结果，主要监控 Spatial Adaptive-K、Random Selection baseline、Object CRM/Argmin 补种

### 3. 📊 当前状态
**刚做完**: 收到 `eval-vla-only-goal-seed47` (ANALYZING) 的 cron 回调，已派 Worker `worker_analyze_eval-vla-only-goal-seed47_20260520T121700` 去 bjb2-28827 读日志提取指标 → 等回调更新 registry + 汇报 Director。

**RUNNING/监控中的实验**（13 个 cron 活跃）:
- Spatial Adaptive-K: P75-seed44, P25-seed44, P90-seed42, P90-seed43（4 个）
- Random Selection Spatial: seed42, seed43, seed44（3 个）
- Object CRM norm02: seed49（1 个）
- Argmin Object: seed48, seed49（2 个）
- VLA-only Spatial: seed48（1 个）
- Obs-only Goal norm02: seed51（1 个）
- Obs-only Object norm02: seed43-r3（1 个）

**PREPARING**: ~41 个实验排队

**等待中**:
- Worker `worker_analyze_eval-vla-only-goal-seed47` 回调 → 提取指标 → 更新 registry → 汇报 Director
- 上述 13 个 RUNNING 实验的 cron 完成回调

### 4. 📋 待办（条件触发式）
- Worker 回调 eval-vla-only-goal-seed47 → 更新 metrics/conclusion/status → 汇报 Director（Goal VLA-only n=7，与 CRM-Goal n=5 对比，OOD Goal 结论: neutral -0.7pp n.s.）
- Spatial Adaptive-K P50 seed42/43/44 全部完成 → 汇总 Spatial P50 均值 → 与 Object P50 (15.3%) 对比 → 验证跨 benchmark 阈值迁移（D085）
- Random Selection Spatial 3 seeds 完成 → 与 Spatial VLA-only (~29.6%) 对比 → 确认 Random ≈ VLA-only 则证明 CRM guidance 是价值来源
- Argmin Object seed48/49 完成 → 补齐 Argmin vs CRM 对比的 seed 数
- Obs-only Object norm02 seed43-r3 完成 → 补齐 Object CRM n→n+1
- 所有 Spatial 实验完成 → 更新论文 Table 1 Spatial 行

### 5. 🎯 战略上下文
- **核心方向**: Adaptive inference-time compute for frozen VLAs。K=2 L2 distance 作为不确定性信号（ρ=0.9979 vs K10 variance），P50 阈值为 Pareto 最优
- **D077**: Adaptive K 升级为论文核心贡献（用户硬要求），K=10 分析降为 supporting evidence
- **D078**: P50 确认为 Pareto 最优（Object: 15.3% SR, avg_K ~3.8, fast_path 77%, 保留 K=10 的 91% 性能）
- **D079**: CRM correction magnitude 信号 NO-GO (ρ=0.15)，只有 K=2 L2 可用
- **D080**: Table 1 Object CRM 统一为 norm02-only n=6 (16.8±1.8%)
- **D081**: Long OOD 降级为 cautious wording (MW-U p=0.061 n.s.)
- **D085**: 跨 benchmark 阈值迁移 framing — P50 为默认，Spatial 正在验证中
- **OOD Goal**: neutral (-0.7pp n.s.)，不是卖点但不是问题
- **OOD LTO**: catastrophic (-12pp)，论文中需要诚实讨论
- **易错点**: 
  - seed42 的 Object norm02 结果 (SR=20%) 被排除（D084），不要误纳入统计
  - Spatial CRM K=10 的 n=8 有溯源问题（D083），registry 只查到 n=7，第 8 个需要确认
  - evaluate.py 使用 batched inference（D082），延迟表和效率 claim 需据此调整
  - 多个 Goal/Long 实验的 PREPARING 状态可能是之前被 kill 后未清理的残留，不要重复提交

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
前 164 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-21T04:21:40.549435+00:00_

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
  "session": "cron:hook:eval-vla-only-goal-seed47",
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

_source line 3 · 2026-05-21T04:21:40.668968+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "ToolSearch",
  "elapsed_ms": 119
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T04:21:43.617021+00:00_

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
  "session": "cron:hook:eval-vla-only-goal-seed47",
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

_source line 5 · 2026-05-21T04:21:44.123856+00:00_

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
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T04:21:44.622915+00:00_

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
  "session": "cron:hook:eval-vla-only-goal-seed47",
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

_source line 7 · 2026-05-21T04:21:44.733807+00:00_

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
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T04:21:46.282604+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-20T13:50:21.016Z\", \"updated_at\": \"2026-05-21T03:04:42.663Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.\"}, \"eval-obs-only-object-norm005-seed67\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T02:58:27.009Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed67. Norm sweep seed balance for ε=0.05.\"}, \"eval-obs-only-object-norm003-seed67\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T02:54:48.643Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed67, norm sweep statistical robustness\"}, \"eval-obs-only-object-norm01-seed67\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T02:35:00.000Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.1 on LIBERO-Object seed67, norm sweep statistical robustness\"}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T01:48:00.000Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.03 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\"}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T01:48:00.000Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.05 on LIBERO-Object seed66, additional seed for norm sweep statistical robustness\"}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T01:30:00.000Z\", \"updated_at\": \"2026-05-21T01:48:00.000Z\", \"hypothesis\": \"obs_only CRM with epsilon=0.1 on LIBERO-Object seed66, additional seed f
…[truncated 153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2665
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T04:22:31.502092+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 6, \"results\": [{\"exp_id\": \"eval-obs-only-object-norm003-seed67\", \"success\": true, \"actions\": [\"Job still running (pid=969788)\"]}, {\"exp_id\": \"eval-obs-only-object-norm005-seed67\", \"success\": true, \"actions\": [\"Job still running (pid=805840)\"]}, {\"exp_id\": \"eval-obs-only-object-norm01-seed67\", \"success\": true, \"actions\": [\"Job still running (pid=666593)\"]}, {\"exp_id\": \"eval-obs-only-object-norm003-seed66\", \"success\": true, \"actions\": [\"Job still running (pid=642428)\"]}, {\"exp_id\": \"eval-obs-only-object-norm005-seed66\", \"success\": true, \"actions\": [\"Job still running (pid=642506)\"]}, {\"exp_id\": \"eval-obs-only-object-norm01-seed66\", \"success\": true, \"actions\": [\"Job still running (pid=642775)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 47378
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T04:22:31.553885+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval-adaptive-k-spatial-p90-seed44-bjb2 | Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep. | — | — | — |\\n\\n## 待处理\\n- eval-obs-only-object-norm003-seed76: CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed76. Norm sweep: ε=0.03 has fewest seeds, expanding coverage for statistical confidence.（准备中）\\n- eval-pi05-baseline-object-seed42-r2: π0.5 VLA-only baseline on LIBERO-Object seed42 (r2). Fix: corrected QUANTILES→MEAN_STD normalization mismatch that caused 0% SR in r1.（准备中）\\n- …另有 42 项\\n\\n## 近期结论\\n- **eval-pi05-baseline-object-seed42** (failed): π0.5 VLA-only baseline on LIBERO-Object seed42 — establishes reference success rate for flow-matching VLA, tests CRM applicability to second VLA backbone\\n\\n## 趋势\\n成功 315 / 负向 38 / 失败 54 / 共 499\\noverall_success_rate: 0.15 →（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-18228: 无 GPU 信息\\nbjb1-32546: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\\nbjb2-28827: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\\nbjb2-40593: 无 GPU 信息\\n\\n## 告警\\n- plan_001-crm-smolvla: 训练失败 — unknown\\n- plan_014-reconvla-baseline: 训练失败 — unknown\\n- eval-smolvla-libero-spatial: 训练失败 — unknown\\n- eval-spatial-reeval-v2: 已被终止 — unknown\\n- precompute-v2-shard0: 已被终止 — unknown\\n- precompute-v2-shard1: 已被终止 — unknown\\n- precompute-v2-shard2: 已被终止 — unknown\\n- eval-spatial-v3-full: 已被终止 — unknown\\n- precompute-v3-shard0: 已被终止 — unknown\\n- precompute-v3-shard1: 已被终止 — unknown\\n- precompute-v3-shard2: 已被终止 — unknown\\n- eval-spatial-v4-full: 已被终止 — unknown\\n- eval-object-v4-full: 已被终止 — unknown\\n- eval-spatial-v5
…[truncated 5372 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 46930
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T04:22:31.554443+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-21 03:28 UTC | 更新原因: D097: Spatial Adaptive K sweep + latency profile done, 9 GPU filling, π0.5 normalization diagnosis\\n\\n> 详见 paper_framing.md（D077: Adaptive K 核心, D088→D092: Plan A GO, D097: Spatial sweep + latency done）\\n\\n## 核心方向\\n**Adaptive inference-time compute for frozen VLAs** — K=2 L2 distance 作为不确定性信号，自适应决定推理策略（直出 vs CRM correction）。Plan A = Pareto 最优（双 benchmark 最高 SR + 最低 compute）。\\n\\n## 投稿目标\\n**CoRL 2026** DDL **2026-05-29**。剩余 **8 天**。\\n\\n## Plan A 核心结果 (LOCKED)\\n| Benchmark | Plan A (K=2) | K=10 CRM | VLA-only | Δ vs K=10 |\\n|-----------|-------------|----------|----------|-----------|\\n| Object    | 18.3%±2.1%  | 16.8%±1.8% | 10.8% | +1.5pp, 80% less compute |\\n| Spatial   | 35.0%±1.0%  | 34.5%±1.5% | 29.6%±1.1% | +0.5pp, 80% less compute |\\n\\n## Adaptive K Sweep (D097, LOCK pending P90-seed44)\\n| Threshold | Object SR | Spatial SR | avg_K | fast_path% |\\n|-----------|-----------|------------|-------|-----------|\\n| P90 | ~16.0% | ~31.5% (2/3) | ~3.5 | ~80% |\\n| P75 | ~15.5% | 32.7%±1.5% | ~5.0 | ~62% |\\n| P50 | 15.3% | 32.0%±1.7% | ~6.35 | ~46% |\\n| P25 | ~16.5% | 31.7%±1.5% | ~7.65 | ~29% |\\n\\n**结论**: 所有阈值 SR 几乎持平，但 compute 差 2×。Plan A 在两个 benchmark 上均优于所有 Adaptive K 变体。\\n\\n## Latency Profile (D097, LOCKED)\\n- VLA K=1: 256.5ms | K=10: 253.2ms（batching 几乎零开销）\\n- CRM forward: **0.28ms**（可忽略）\\n- Plan A speedup: **1.82×** | CRM pipeline vs K=10: **-1.66%**（反而更快）\\n\\n## Norm Sweep 状态（plan_200/500）\\n| ε    | n seeds | mean SR | 状态 |\\n|------|---------|---------|------|\\n| 0.03 | 5       | ~15.5%  | 补种中 (target 10-12) |\\n| 0.05 | 6       | ~14.0%  | 补种中 (target 10-12) |\\n| 0.1  | 9       | ~15.0%  | +40 旧 seeds 待 harvest |\\n| 0.2  | 12      | 17.2%   | LOCKED |\\n\\n## π0.5 实验线（D0
…[truncated 2631 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 46820
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T04:22:48.941436+00:00_

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
  "session": "cron:hook:eval-vla-only-goal-seed47",
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

_source line 13 · 2026-05-21T04:22:50.605979+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__list_workers,mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__send_progress,mcp__agent-ml-research__load_project_config",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__list_workers,mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__send_progress,mcp__agent-ml-research__load_project_config",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T04:22:51.661563+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.6675}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2720
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T04:22:51.661957+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "ToolSearch",
  "elapsed_ms": 1055
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T04:22:56.655520+00:00_

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
  "session": "cron:hook:eval-vla-only-goal-seed47",
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

_source line 17 · 2026-05-21T04:22:57.134884+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_diag_pi05-state-padding_20260521T040022\", \"task_type\": \"diag:pi05-state-padding\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-21T04:00:22.258889+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_harvest_old-preparing-experiments_20260521T041745\", \"task_type\": \"harvest:old-preparing-experiments\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-21T04:17:45.508986+00:00\", \"ended_at\": null}], \"count\": 2}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 479
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T04:22:57.640416+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "status": "done",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "status": "done",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T04:22:57.943548+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_diag_pi05-normalization_20260521T032306\", \"task_type\": \"diag:pi05-normalization\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"done\", \"started_at\": \"2026-05-21T03:23:06.733846+00:00\", \"ended_at\": \"2026-05-21T03:25:33.876597+00:00\"}, {\"worker_id\": \"worker_fix_pi05-normalization_20260521T032653\", \"task_type\": \"fix:pi05-normalization\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"done\", \"started_at\": \"2026-05-21T03:26:53.256753+00:00\", \"ended_at\": \"2026-05-21T03:31:07.481251+00:00\"}, {\"worker_id\": \"worker_verify_gpu-status-all-servers_20260521T032920\", \"task_type\": \"verify:gpu-status-all-servers\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"done\", \"started_at\": \"2026-05-21T03:29:20.650690+00:00\", \"ended_at\": \"2026-05-21T03:31:09.326224+00:00\"}, {\"worker_id\": \"worker_verify_pi05-r2-normfix_20260521T033549\", \"task_type\": \"verify:pi05-r2-normfix\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"done\", \"started_at\": \"2026-05-21T03:35:50.128099+00:00\", \"ended_at\": \"2026-05-21T03:38:38.084432+00:00\"}, {\"worker_id\": \"worker_urgent_pi05-process-conflict_20260521T033630\", \"task_type\": \"urgent:pi05-process-conflict\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"done\", \"started_at\": \"2026-05-21T03:36:30.829750+00:00\", \"ended_at\": \"2026-05-21T03:37:38.051746+00:00\"}, {\"worker_id\": \"worker_harvest_old-norm01-seeds_20260521T035537\", \"task_type\": \"harvest:old-norm01-seeds\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"done\", \"started_at\": \"2026-05-21T03:55:38.144021+00:00\", \"ended_at\": \"2026-05-21T04:03:14.815481+00:00\"}, {\"worker_id\": \"worker_analysis_random-selection-spatial-writeup_20260521T035553\", \"task_type\": \"analysis:random-selection-spatial-writeup\", \"project\": \"acr-vla-conformal-refinement\", \
…[truncated 1077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 303
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T04:22:57.944027+00:00_

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
  "session": "cron:hook:eval-vla-only-goal-seed47",
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

_source line 21 · 2026-05-21T04:22:58.147069+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"acr-vla-conformal-refinement\", \"section\": \"execution\", \"config\": {\"execution\": {\"account\": \"root\", \"gpu_constraint\": [\"autodl-4090:cuda:0\"], \"gpu_ids\": [\"bjb2-40593:cuda:0\", \"bjb1-18228:cuda:0\", \"bjb1-18228:cuda:1\", \"bjb1-18228:cuda:2\", \"bjb1-18228:cuda:3\", \"bjb1-32546:cuda:0\", \"bjb1-32546:cuda:1\", \"bjb1-32546:cuda:2\", \"bjb1-32546:cuda:3\", \"bjb1-32546:cuda:4\", \"bjb1-32546:cuda:5\", \"bjb2-28827:cuda:0\", \"bjb2-28827:cuda:1\", \"bjb2-28827:cuda:2\", \"bjb2-28827:cuda:3\", \"bjb2-28827:cuda:4\", \"bjb2-28827:cuda:5\"], \"project_path\": \"/root/acr-vla-conformal-refinement\", \"servers\": [\"bjb2-40593\", \"bjb1-18228\", {\"account\": \"root\", \"server\": \"bjb1-32546\"}, {\"account\": \"root\", \"server\": \"bjb2-28827\"}]}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 203
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T04:23:22.659413+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "project": "acr-vla-conformal-refinement",
  "limit": "20",
  "fields": "['exp_id', 'status', 'conclusion', 'metrics', 'updated_at', 'hypothesis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "project": "acr-vla-conformal-refinement",
    "limit": "20",
    "fields": "['exp_id', 'status', 'conclusion', 'metrics', 'updated_at', 'hypothesis']"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T04:23:23.113594+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_diag_pi05-state-padding_20260521T040022",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_diag_pi05-state-padding_20260521T040022",
    "verbose": "True"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T04:23:23.165431+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_harvest_old-preparing-experiments_20260521T041745",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_harvest_old-preparing-experiments_20260521T041745",
    "verbose": "True"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T04:23:24.170899+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm01-seed60\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:01:22.020Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed60. Norm sweep filling ε=0.1 gap.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"source\": \"harvested from bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm01_seed60.json\"}}, \"eval-pi05-baseline-object-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:59:27.286Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42 — establishes reference success rate for flow-matching VLA, tests CRM applicability to second VLA backbone\", \"conclusion\": \"failed\", \"metrics\": {\"overall_success_rate\": 0}}, \"eval-obs-only-object-norm01-seed54\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:30:13.218Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed54. Norm sweep: filling ε=0.1 gap, bringing n to 7+.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.15}}, \"eval-obs-only-object-norm01-seed53\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:30:10.368Z\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed53. Norm sweep: filling ε=0.1 gap, bringing n to 6+.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.19}}, \"eval-obs-only-object-norm01-seed52\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:30:07.112Z\", \"conclusion\": \"success\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed52. Norm sweep: filling ε=0.1 gap (ROADMAP TBD), bringing n from 3 to 5+.\", \"metrics\": {\"overall_success_ra
…[truncated 4767 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1511
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T04:23:24.324299+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_diag_pi05-state-padding_20260521T040022\", \"status\": \"running\", \"task_type\": \"diag:pi05-state-padding\", \"project\": \"acr-vla-conformal-refinement\", \"started_at\": \"2026-05-21T04:00:22.258889+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"progress\": {\"recent_tools\": [\"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\"], \"last_text\": \"发现可能的关键 bug：`resize_with_pad_torch` 的输入格式。需要检查函数签名。\", \"turn_count\": 5}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 1210
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T04:23:24.475247+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_harvest_old-preparing-experiments_20260521T041745\", \"status\": \"running\", \"task_type\": \"harvest:old-preparing-experiments\", \"project\": \"acr-vla-conformal-refinement\", \"started_at\": \"2026-05-21T04:17:45.508986+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"progress\": {\"recent_tools\": [\"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\"], \"last_text\": \"You've hit your limit · resets May 22, 5pm (UTC)\", \"turn_count\": 19}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 1309
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T04:24:29.086220+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-21T04:24:29.136842+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T04:24:40.136734+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['exp_id', 'status', 'spec']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['exp_id', 'status', 'spec']"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T04:24:40.840714+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'conclusion': 'success'}",
  "project": "acr-vla-conformal-refinement",
  "limit": "0",
  "fields": "['exp_id', 'metrics', 'hypothesis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'conclusion': 'success'}",
    "project": "acr-vla-conformal-refinement",
    "limit": "0",
    "fields": "['exp_id', 'metrics', 'hypothesis']"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T04:24:42.502168+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.125870 --k_full 10 --benchmark spatial --seed 44 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p90_seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"pid\": 975409, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-adaptive-k-spatial-p90-seed44-bjb2.log\", \"submitted_at\": \"2026-05-20T13:50:48.545Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"model_name\": \"CRM_obs_only_adaptive_k\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}}, \"eval-obs-only-object-norm005-seed67\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"detected on GPU, submitted by prior Worker but not registered\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/autodl-tmp/acr-vla-conformal-refinement/\", \"data_count\": \"100 rollouts\", \"model_name\": \"crm_v3_norm/obs_only\", \"seed\": 67, \"gpu\": \"cuda:2\"}}, \"eval-obs-only-object-norm003-seed67\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"detected on GPU, submitted by prior Worker but not registered\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/acr-vla-conformal-refinement/\", \"data_count\": \"100 rollouts\", \"model_name\": \"crm_v3_norm/obs_only\", \"seed\": 67, \"gpu\": \"cuda:5\"}}, \"eval-obs-only-object-norm01-seed67\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 evaluate.py --benchmark object --K 10 --mode crm_obs_only --max_correction_norm 0.1 --seed 67 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoint
…[truncated 1580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2365
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-21T04:24:45.062912+00:00_

Error: result (137,782 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-870cc8ef/27d5a50a-5e1b-47fe-9022-6bffd93c0a10/tool-results/mcp-agent-ml-research-read_registry-1779337485001.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-870cc8ef/27d5a50a-5e1b-47fe-9022-6bffd93c0a10/tool-results/mcp-agent-ml-research-read_registry-1779337485001.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 4222
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T04:25:07.067827+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-870cc8ef/27d5a50a-5e1b-47fe-9022-6bffd93c0a10/tool-results/mcp-agent-ml-research-read_registry-1779337485001.txt | python3 -c \"\nimport json, sys, re\n\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Count norm sweep seeds per epsilon\nnorm_counts = {'0.03': [], '0.05': [], '0.1': [], '0.2': []}\n\nfor eid, info in exps.items():\n    h = info.get('hypothesis', '') or ''\n    m = info.get('metrics', {}) or {}\n    sr = m.get('overall_success_rate', None)\n    \n    # Match obs_only object experiments with specific norm values\n    if 'obs_only' in h.lower() or 'obs-only' in eid or 'norm0' in eid:\n        if 'object' in h.lower() or 'object' in eid.lower():\n            # Extract epsilon from hypothesis or exp_id\n            eps = None\n            if 'ε=0.03' in h or 'norm003' in eid or 'norm=0.03' in h or 'epsilon=0.03' in h:\n                eps = '0.03'\n            elif 'ε=0.05' in h or 'norm005' in eid or 'norm=0.05' in h or 'epsilon=0.05' in h:\n                eps = '0.05'\n            elif 'ε=0.1' in h or 'norm01' in eid or 'norm=0.1' in h or 'epsilon=0.1' in h:\n                if 'norm02' not in eid:  # exclude norm02\n                    eps = '0.1'\n            elif 'ε=0.2' in h or 'norm02' in eid or 'norm=0.2' in h:\n                eps = '0.2'\n            \n            if eps and sr is not None:\n                norm_counts[eps].append({'id': eid, 'sr': sr})\n\nfor eps in sorted(norm_counts.keys(), key=float):\n    seeds = norm_counts[eps]\n    if seeds:\n        srs = [s['sr'] for s in seeds]\n        mean_sr = sum(srs) / len(srs)\n        print(f'ε={eps}: n={len(seeds)}, mean_SR={mean_sr:.3f}, range=[{min(srs):.2f}, {max(srs):.2f}]')\n    else:\n        print(f'ε={eps}: n=0')\n\"\n",
  "description": "Count norm sweep seeds per epsilon from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-870cc8ef/27d5a50a-5e1b-47fe-9022-6bffd93c0a10/tool-results/mcp-agent-ml-research-read_registry-1779337485001.txt | python3 -c \"\nimport json, sys, re\n\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Count norm sweep seeds per epsilon\nnorm_counts = {'0.03': [], '0.05': [], '0.1': [], '0.2': []}\n\nfor eid, info in exps.items():\n    h = info.get('hypothesis', '') or ''\n    m = info.get('metrics', {}) or {}\n    sr = m.get('overall_success_rate', None)\n    \n    # Match obs_only object experiments with specific norm values\n    if 'obs_only' in h.lower() or 'obs-only' in eid or 'norm0' in eid:\n        if 'object' in h.lower() or 'object' in eid.lower():\n            # Extract epsilon from hypothesis or exp_id\n            eps = None\n            if 'ε=0.03' in h or 'norm003' in eid or 'norm=0.03' in h or 'epsilon=0.03' in h:\n                eps = '0.03'\n            elif 'ε=0.05' in h or 'norm005' in eid or 'norm=0.05' in h or 'epsilon=0.05' in h:\n                eps = '0.05'\n            elif 'ε=0.1' in h or 'norm01' in eid or 'norm=0.1' in h or 'epsilon=0.1' in h:\n                if 'norm02' not in eid:  # exclude norm02\n                    eps = '0.1'\n            elif 'ε=0.2' in h or 'norm02' in eid or 'norm=0.2' in h:\n                eps = '0.2'\n            \n            if eps and sr is not None:\n                norm_counts[eps].append({'id': eid, 'sr': sr})\n\nfor eps in sorted(norm_counts.keys(), key=float):\n    seeds = norm_counts[eps]\n    if seeds:\n        srs = [s['sr'] for s in seeds]\n        mean_sr = sum(srs) / len(srs)\n        print(f'ε={eps}: n={len(seeds)}, mean_SR={mean_sr:.3f}, range=[{min(srs):.2f}, {max(srs):.2f}]')\n    else:\n        print(f'ε={eps}: n=0')\n\"\n",
    "description": "Count norm sweep seeds per epsilon from registry"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-21T04:25:07.367565+00:00_

ε=0.03: n=15, mean_SR=0.149, range=[0.13, 0.17]
ε=0.05: n=15, mean_SR=0.136, range=[0.10, 0.16]
ε=0.1: n=18, mean_SR=0.153, range=[0.11, 0.19]
ε=0.2: n=13, mean_SR=0.231, range=[0.09, 0.72]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Bash",
  "elapsed_ms": 299
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T04:25:36.795967+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-870cc8ef/27d5a50a-5e1b-47fe-9022-6bffd93c0a10/tool-results/mcp-agent-ml-research-read_registry-1779337485001.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Check specific experiment groups\npatterns = [\n    'adaptive-k-spatial-p50',\n    'adaptive-k-spatial-p75', \n    'adaptive-k-spatial-p25',\n    'adaptive-k-spatial-p90',\n    'random-selection-spatial',\n    'argmin-object',\n    'obs-only-object-norm02-seed43',\n    'vla-only-spatial',\n    'vla-only-goal',\n    'plan-a-spatial',\n    'plan-a-object',\n]\n\nfor pat in patterns:\n    matches = {k: v for k, v in exps.items() if pat in k}\n    if matches:\n        print(f'\\n=== {pat} ({len(matches)} exps) ===')\n        for eid, info in sorted(matches.items()):\n            m = info.get('metrics', {}) or {}\n            sr = m.get('overall_success_rate', 'N/A')\n            print(f'  {eid}: SR={sr}')\n\" 2>&1 | head -80\n",
  "description": "Check key experiment groups completion status"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-870cc8ef/27d5a50a-5e1b-47fe-9022-6bffd93c0a10/tool-results/mcp-agent-ml-research-read_registry-1779337485001.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Check specific experiment groups\npatterns = [\n    'adaptive-k-spatial-p50',\n    'adaptive-k-spatial-p75', \n    'adaptive-k-spatial-p25',\n    'adaptive-k-spatial-p90',\n    'random-selection-spatial',\n    'argmin-object',\n    'obs-only-object-norm02-seed43',\n    'vla-only-spatial',\n    'vla-only-goal',\n    'plan-a-spatial',\n    'plan-a-object',\n]\n\nfor pat in patterns:\n    matches = {k: v for k, v in exps.items() if pat in k}\n    if matches:\n        print(f'\\n=== {pat} ({len(matches)} exps) ===')\n        for eid, info in sorted(matches.items()):\n            m = info.get('metrics', {}) or {}\n            sr = m.get('overall_success_rate', 'N/A')\n            print(f'  {eid}: SR={sr}')\n\" 2>&1 | head -80\n",
    "description": "Check key experiment groups completion status"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-21T04:25:36.947530+00:00_

=== adaptive-k-spatial-p50 (5 exps) ===
  eval-adaptive-k-spatial-p50-seed42: SR=N/A
  eval-adaptive-k-spatial-p50-seed43: SR=N/A
  eval-adaptive-k-spatial-p50-seed43-r2: SR=0.33
  eval-adaptive-k-spatial-p50-seed44: SR=N/A
  eval-adaptive-k-spatial-p50-seed44-r2: SR=0.33

=== adaptive-k-spatial-p75 (3 exps) ===
  eval-adaptive-k-spatial-p75-seed42: SR=N/A
  eval-adaptive-k-spatial-p75-seed43: SR=N/A
  eval-adaptive-k-spatial-p75-seed44: SR=N/A

=== adaptive-k-spatial-p25 (2 exps) ===
  eval-adaptive-k-spatial-p25-seed43: SR=N/A
  eval-adaptive-k-spatial-p25-seed44: SR=N/A

=== adaptive-k-spatial-p90 (3 exps) ===
  eval-adaptive-k-spatial-p90-seed42: SR=0.31
  eval-adaptive-k-spatial-p90-seed43: SR=0.32
  eval-adaptive-k-spatial-p90-seed44: SR=N/A

=== random-selection-spatial (5 exps) ===
  eval-random-selection-spatial-seed42-r2: SR=N/A
  eval-random-selection-spatial-seed42-r3: SR=N/A
  eval-random-selection-spatial-seed43: SR=0.26
  eval-random-selection-spatial-seed43-r2: SR=N/A
  eval-random-selection-spatial-seed44: SR=0.28

=== argmin-object (12 exps) ===
  eval-argmin-object-k5-seed42: SR=N/A
  eval-argmin-object-k5-seed43: SR=N/A
  eval-argmin-object-k5-seed44-r2: SR=N/A
  eval-argmin-object-k5-seed45: SR=N/A
  eval-argmin-object-seed43: SR=0.17
  eval-argmin-object-seed44-r2: SR=N/A
  eval-argmin-object-seed45: SR=N/A
  eval-argmin-object-seed46: SR=N/A
  eval-argmin-object-seed47: SR=N/A
  eval-argmin-object-seed48: SR=N/A
  eval-argmin-object-seed49: SR=N/A
  eval-argmin-object-seed50: SR=N/A

=== obs-only-object-norm02-seed43 (2 exps) ===
  eval-obs-only-object-norm02-seed43-r2: SR=N/A
  eval-obs-only-object-norm02-seed43-r3: SR=N/A

=== vla-only-spatial (8 exps) ===
  eval-vla-only-spatial-seed42: SR=N/A
  eval-vla-only-spatial-seed43: SR=N/A
  eval-vla-only-spatial-seed44: SR=N/A
  eval-vla-only-spatial-seed45: SR=N/A
  eval-vla-only-spatial-seed46: SR=0.3
  eval-vla-only-spatial-seed47: SR=0.3
  eval-vla-only-spatial-seed48: SR=0.3
  eval-vla-only-s
…[truncated 596 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T04:26:41.522443+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'PREPARING'}",
  "project": "acr-vla-conformal-refinement",
  "limit": "50",
  "fields": "['exp_id', 'status', 'hypothesis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'PREPARING'}",
    "project": "acr-vla-conformal-refinement",
    "limit": "50",
    "fields": "['exp_id', 'status', 'hypothesis']"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T04:26:41.674444+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-870cc8ef/27d5a50a-5e1b-47fe-9022-6bffd93c0a10/tool-results/mcp-agent-ml-research-read_registry-1779337485001.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Check specific key experiments with full details\nkeys = [\n    'eval-adaptive-k-spatial-p50-seed42',\n    'eval-adaptive-k-spatial-p75-seed42', 'eval-adaptive-k-spatial-p75-seed43', 'eval-adaptive-k-spatial-p75-seed44',\n    'eval-adaptive-k-spatial-p25-seed43', 'eval-adaptive-k-spatial-p25-seed44',\n    'eval-random-selection-spatial-seed42-r2', 'eval-random-selection-spatial-seed42-r3',\n    'eval-argmin-object-seed48', 'eval-argmin-object-seed49',\n    'eval-obs-only-object-norm02-seed43-r3',\n    'eval-vla-only-spatial-seed48',\n]\nfor k in keys:\n    if k in exps:\n        e = exps[k]\n        m = e.get('metrics', {}) or {}\n        sr = m.get('overall_success_rate', 'N/A')\n        # Check for alternative metric fields\n        if sr == 'N/A':\n            sr_alt = m.get('success_rate', m.get('sr', 'N/A'))\n            if sr_alt != 'N/A':\n                sr = f'{sr_alt} (alt field)'\n        print(f'{k}: SR={sr}, metrics_keys={list(m.keys())[:5] if m else \\\"empty\\\"}')\n    else:\n        print(f'{k}: NOT FOUND')\n\"\n",
  "description": "Check specific key experiments status and metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-870cc8ef/27d5a50a-5e1b-47fe-9022-6bffd93c0a10/tool-results/mcp-agent-ml-research-read_registry-1779337485001.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Check specific key experiments with full details\nkeys = [\n    'eval-adaptive-k-spatial-p50-seed42',\n    'eval-adaptive-k-spatial-p75-seed42', 'eval-adaptive-k-spatial-p75-seed43', 'eval-adaptive-k-spatial-p75-seed44',\n    'eval-adaptive-k-spatial-p25-seed43', 'eval-adaptive-k-spatial-p25-seed44',\n    'eval-random-selection-spatial-seed42-r2', 'eval-random-selection-spatial-seed42-r3',\n    'eval-argmin-object-seed48', 'eval-argmin-object-seed49',\n    'eval-obs-only-object-norm02-seed43-r3',\n    'eval-vla-only-spatial-seed48',\n]\nfor k in keys:\n    if k in exps:\n        e = exps[k]\n        m = e.get('metrics', {}) or {}\n        sr = m.get('overall_success_rate', 'N/A')\n        # Check for alternative metric fields\n        if sr == 'N/A':\n            sr_alt = m.get('success_rate', m.get('sr', 'N/A'))\n            if sr_alt != 'N/A':\n                sr = f'{sr_alt} (alt field)'\n        print(f'{k}: SR={sr}, metrics_keys={list(m.keys())[:5] if m else \\\"empty\\\"}')\n    else:\n        print(f'{k}: NOT FOUND')\n\"\n",
    "description": "Check specific key experiments status and metrics"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T04:26:43.580724+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm003-seed76\": {\"status\": \"PREPARING\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed76. Norm sweep: ε=0.03 has fewest seeds, expanding coverage for statistical confidence.\"}, \"eval-pi05-baseline-object-seed42-r2\": {\"status\": \"PREPARING\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42 (r2). Fix: corrected QUANTILES→MEAN_STD normalization mismatch that caused 0% SR in r1.\"}, \"eval-obs-only-object-norm01-seed77\": {\"status\": \"PREPARING\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed77. Norm sweep: ε=0.1 补种.\"}, \"eval-obs-only-object-norm01-seed76\": {\"status\": \"PREPARING\", \"hypothesis\": \"CRM obs_only (ε=0.1) K=10 on LIBERO-Object seed76. Norm sweep: ε=0.1 补种.\"}, \"eval-obs-only-object-norm005-seed77\": {\"status\": \"PREPARING\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed77. Norm sweep: ε=0.05 outlier verification.\"}, \"eval-obs-only-object-norm003-seed63-r3\": {\"status\": \"PREPARING\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed63 r3. Redo of killed seed63-r2 (M036 dual process). Norm sweep ε=0.03 seed balance.\"}, \"eval-obs-only-object-norm005-seed76\": {\"status\": \"PREPARING\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed76. Norm sweep: ε=0.05 has outlier seeds, expanding for variance verification.\"}, \"eval-obs-only-object-norm003-seed62-r3\": {\"status\": \"PREPARING\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed62 r3. Redo of killed seed62-r2 (M036 dual process). Norm sweep ε=0.03 seed balance.\"}, \"eval-obs-only-object-norm003-seed78\": {\"status\": \"PREPARING\", \"hypothesis\": \"CRM obs_only (ε=0.03) K=10 on LIBERO-Object seed78. Norm sweep: ε=0.03 has fewest seeds, expanding coverage.\"}, \"eval-obs-only-object-norm003-seed77\": {\"status\": \"PREPARING\", \"hypothesis\": \"CRM obs_only (ε=0.
…[truncated 5280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2058
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-21T04:26:43.700017+00:00_

eval-adaptive-k-spatial-p50-seed42: SR=30 (alt field), metrics_keys=['sr', 'avg_K', 'fast_path_pct', 'mean_l2', 'total_rollouts']
eval-adaptive-k-spatial-p75-seed42: SR=0.31 (alt field), metrics_keys=['sr', 'avg_k', 'fast_path_ratio', 'mean_l2', 'adaptive_trigger_rate']
eval-adaptive-k-spatial-p75-seed43: SR=34 (alt field), metrics_keys=['success_rate', 'total_rollouts', 'adaptive_stats', 'per_task']
eval-adaptive-k-spatial-p75-seed44: SR=33 (alt field), metrics_keys=['sr', 'avg_k', 'fast_path_pct', 'mean_l2', 'total_rollouts']
eval-adaptive-k-spatial-p25-seed43: SR=30 (alt field), metrics_keys=['sr', 'avg_k', 'fast_path_pct', 'mean_l2', 'total_rollouts']
eval-adaptive-k-spatial-p25-seed44: SR=32 (alt field), metrics_keys=['sr', 'avg_k', 'fast_path_pct', 'mean_l2', 'total_rollouts']
eval-random-selection-spatial-seed42-r2: SR=34 (alt field), metrics_keys=['sr', 'n_tasks', 'n_rollouts', 'total_rollouts']
eval-random-selection-spatial-seed42-r3: SR=0.34 (alt field), metrics_keys=['success_rate', 'successes', 'total_rollouts']
eval-argmin-object-seed48: SR=0.15 (alt field), metrics_keys=['success_rate', 'per_task']
eval-argmin-object-seed49: SR=N/A, metrics_keys=['overall_sr', 'total_successes', 'total_rollouts', 'seed', 'benchmark']
eval-obs-only-object-norm02-seed43-r3: SR=16 (alt field), metrics_keys=['sr']
eval-vla-only-spatial-seed48: SR=0.3, metrics_keys=['overall_success_rate', 'benchmark', 'n_rollouts']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Bash",
  "elapsed_ms": 2025
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-21T04:27:46.754777+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_experiment_plan_with_status",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_experiment_plan_with_status",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-21T04:27:46.807630+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-21T04:27:49.588707+00:00_

called mcp__agent-ml-research__read_experiment_plan_with_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_experiment_plan_with_status</summary>

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
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_experiment_plan_with_status",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-21T04:27:53.426929+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": [{\"id\": \"plan_100\", \"claim\": 1, \"description\": \"obs_only ε=0.2 multi-seed evaluation on LIBERO Object (6 seeds). Core evidence for pipeline improvement over argmin baseline.\", \"priority\": \"P0\", \"gpu_budget_hours\": 36, \"deps\": [], \"registry_id\": \"eval-obs-only-object-norm02-seed42\", \"notes\": \"6v6 pooled: 105/600 (17.5%) vs argmin 74/600 (12.3%), Fisher p=0.0074, Cohen's d=1.21\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.2, \"total_episodes\": 100, \"total_successes\": 20, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.4, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, {\"id\": \"plan_101\", \"claim\": 1, \"description\": \"argmin baseline (reconvla K=10) multi-seed evaluation on LIBERO Object (6 seeds).\", \"priority\": \"P0\", \"gpu_budget_hours\": 36, \"deps\": [], \"registry_id\": \"eval-reconvla-object\", \"notes\": \"seeds 42/43/44/45/46/47 = 12/17/13/12/10/10. registry: eval-reconvla-object (seed42), eval-argmin-object-seed43..seed47\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 12}}, {\"id\": \"plan_102\", \"claim\": 1, \"description\": \"VLA-only (K=1, no CRM) multi-seed baseline on LIBERO Object.\", \"priority\": \"P0\", \"gpu_budget_hours\": 24, \"deps\": [], \"registry_id\": \"eval-vla-only-object\", \"notes\": \"seeds 42/43/44/45/46/47 = 12/12/10/9/11/9%, mean 10.8%. registry: eval-vla-only-object (seed42), eval-vla-only-object-seed43..seed47\", \"status\": \"DONE\
…[truncated 10822 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_experiment_plan_with_status",
  "elapsed_ms": 3838
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-21T04:30:08.627350+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_training_job",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__submit_training_job",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-21T04:30:08.627795+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-21T04:32:07.779641+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "bjb2-28827",
  "gpu_ids": "['cuda:1']",
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark object --K 20 --seed 42 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_k20_seed42.json 2>&1 | tee logs/eval-obs-only-object-norm02-k20-seed42.log\"",
  "exp_id": "eval-obs-only-object-norm02-k20-seed42",
  "timeout_hours": "16",
  "project": "acr-vla-conformal-refinement",
  "plan_id": "plan_601"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "bjb2-28827",
    "gpu_ids": "['cuda:1']",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark object --K 20 --seed 42 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_k20_seed42.json 2>&1 | tee logs/eval-obs-only-object-norm02-k20-seed42.log\"",
    "exp_id": "eval-obs-only-object-norm02-k20-seed42",
    "timeout_hours": "16",
    "project": "acr-vla-conformal-refinement",
    "plan_id": "plan_601"
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T04:32:10.493348+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "bjb2-28827",
  "gpu_ids": "['cuda:2']",
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark object --K 20 --seed 43 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_k20_seed43.json 2>&1 | tee logs/eval-obs-only-object-norm02-k20-seed43.log\"",
  "exp_id": "eval-obs-only-object-norm02-k20-seed43",
  "timeout_hours": "16",
  "project": "acr-vla-conformal-refinement",
  "plan_id": "plan_601"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "bjb2-28827",
    "gpu_ids": "['cuda:2']",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark object --K 20 --seed 43 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_k20_seed43.json 2>&1 | tee logs/eval-obs-only-object-norm02-k20-seed43.log\"",
    "exp_id": "eval-obs-only-object-norm02-k20-seed43",
    "timeout_hours": "16",
    "project": "acr-vla-conformal-refinement",
    "plan_id": "plan_601"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T04:32:12.602631+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"10438\", \"log_file\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k20-seed42.log\", \"gpu_ids\": [\"cuda:1\"], \"server\": \"bjb2-28827\", \"account\": \"root\", \"cuda_visible_devices\": \"1\", \"backend\": \"tmux\", \"tmux_session\": \"eval-obs-only-object-norm02-k20-seed42\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.26}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 4822
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-21T04:32:13.708415+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "bjb2-28827",
  "gpu_ids": "['cuda:3']",
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark object --K 20 --seed 44 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_k20_seed44.json 2>&1 | tee logs/eval-obs-only-object-norm02-k20-seed44.log\"",
  "exp_id": "eval-obs-only-object-norm02-k20-seed44",
  "timeout_hours": "16",
  "project": "acr-vla-conformal-refinement",
  "plan_id": "plan_601"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "bjb2-28827",
    "gpu_ids": "['cuda:3']",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark object --K 20 --seed 44 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_k20_seed44.json 2>&1 | tee logs/eval-obs-only-object-norm02-k20-seed44.log\"",
    "exp_id": "eval-obs-only-object-norm02-k20-seed44",
    "timeout_hours": "16",
    "project": "acr-vla-conformal-refinement",
    "plan_id": "plan_601"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-21T04:32:15.616429+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "bjb2-28827",
  "gpu_ids": "['cuda:4']",
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark spatial --K 10 --seed 49 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed49.json 2>&1 | tee logs/eval-crm-spatial-k10-seed49.log\"",
  "exp_id": "eval-crm-spatial-k10-seed49",
  "timeout_hours": "14",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "bjb2-28827",
    "gpu_ids": "['cuda:4']",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark spatial --K 10 --seed 49 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed49.json 2>&1 | tee logs/eval-crm-spatial-k10-seed49.log\"",
    "exp_id": "eval-crm-spatial-k10-seed49",
    "timeout_hours": "14",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T04:32:18.025077+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "bjb1-32546",
  "gpu_ids": "['cuda:4']",
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark spatial --K 10 --seed 50 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed50.json 2>&1 | tee logs/eval-crm-spatial-k10-seed50.log\"",
  "exp_id": "eval-crm-spatial-k10-seed50",
  "timeout_hours": "14",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "bjb1-32546",
    "gpu_ids": "['cuda:4']",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark spatial --K 10 --seed 50 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed50.json 2>&1 | tee logs/eval-crm-spatial-k10-seed50.log\"",
    "exp_id": "eval-crm-spatial-k10-seed50",
    "timeout_hours": "14",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-21T04:32:19.432872+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"10781\", \"log_file\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k20-seed43.log\", \"gpu_ids\": [\"cuda:2\"], \"server\": \"bjb2-28827\", \"account\": \"root\", \"cuda_visible_devices\": \"2\", \"backend\": \"tmux\", \"tmux_session\": \"eval-obs-only-object-norm02-k20-seed43\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 8939
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-21T04:32:20.388676+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "bjb1-32546",
  "gpu_ids": "['cuda:5']",
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 50 --n_rollouts 10 --output_file logs/eval_vla_only_spatial_seed50.json 2>&1 | tee logs/eval-vla-only-spatial-seed50.log\"",
  "exp_id": "eval-vla-only-spatial-seed50",
  "timeout_hours": "12",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "bjb1-32546",
    "gpu_ids": "['cuda:5']",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 50 --n_rollouts 10 --output_file logs/eval_vla_only_spatial_seed50.json 2>&1 | tee logs/eval-vla-only-spatial-seed50.log\"",
    "exp_id": "eval-vla-only-spatial-seed50",
    "timeout_hours": "12",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-21T04:32:38.293633+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"11078\", \"log_file\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k20-seed44.log\", \"gpu_ids\": [\"cuda:3\"], \"server\": \"bjb2-28827\", \"account\": \"root\", \"cuda_visible_devices\": \"3\", \"backend\": \"tmux\", \"tmux_session\": \"eval-obs-only-object-norm02-k20-seed44\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.62}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 24585
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-21T04:32:38.294067+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"11357\", \"log_file\": \"~/runs/acr-vla-conformal-refinement/eval-crm-spatial-k10-seed49.log\", \"gpu_ids\": [\"cuda:4\"], \"server\": \"bjb2-28827\", \"account\": \"root\", \"cuda_visible_devices\": \"4\", \"backend\": \"tmux\", \"tmux_session\": \"eval-crm-spatial-k10-seed49\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.15}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 22677
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-21T04:32:38.737340+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "deploy:random-selection-object",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务：部署 Random Selection Object baseline 实验\n\n### 背景\nplan_600 要求 Random Selection baseline（K=10 samples, pick 1 uniformly at random, no conformal ranking）。Spatial 版本已完成（seed42=34%, seed43=26%, seed44=28%），但 Object 版本此前全部失败（python path 问题已修复）。\n\n### 步骤\n\n1. **确认 evaluate.py 的 random selection mode**\n   SSH 到 bjb1-32546，读取 evaluate.py 的可用 mode：\n   ```\n   ssh_read_only: cd /root/acr-vla-conformal-refinement && grep -n \"mode.*random\\|random.*selection\\|choices.*mode\\|argparse.*mode\" src/evaluate.py | head -20\n   ```\n   如果没有 --mode random_selection，检查是否有其他 flag 控制 random selection 行为（如 --selection_method random）。\n\n2. **确认 bjb1-32546 的 cuda:0, cuda:1, cuda:3 空闲**\n   ```\n   ssh_read_only: nvidia-smi --query-gpu=index,memory.used,utilization.gpu --format=csv,noheader\n   ```\n\n3. **在 registry 中创建 3 个实验**\n   用 update_registry 创建：\n   - exp_id: eval-random-selection-object-seed42-r3\n     hypothesis: \"Random Selection (K=10, uniform pick) on LIBERO-Object seed42. Isolates conformal ranking contribution: if Random ≈ VLA-only, then CRM's advantage comes from learned correction not just sampling diversity.\"\n   - exp_id: eval-random-selection-object-seed43\n     hypothesis: \"Random Selection (K=10, uniform pick) on LIBERO-Object seed43. Second seed for Random Selection Object baseline.\"\n   - exp_id: eval-random-selection-object-seed44\n     hypothesis: \"Random Selection (K=10, uniform pick) on LIBERO-Object seed44. Third seed for Random Selection Object baseline.\"\n\n4. **用 submit_training_job 提交 3 个实验**\n   命令模板（根据步骤1确认的 mode flag 调整）：\n   ```\n   bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode {MODE_FLAG} --benchmark object --K 10 --seed {SEED} --n_rollouts 10 --output_file logs/eval_random_selection_object_seed{SEED}.json 2>&1 | tee logs/eval-random-selection-object-seed{SEED}.log\"\n   ```\n   分配：\n   - seed42-r3 → bjb1-32546 cuda:0\n   - seed43 → bjb1-32546 cuda:1\n   - seed44 → bjb1-32546 cuda:3\n\n   submit_training_job 参数：\n   - server: bjb1-32546\n   - project: acr-vla-conformal-refinement\n   - timeout_hours: 12\n   - plan_id: plan_600\n\n5. **验证 3 个实验都成功启动**\n\n### 环境\n- 服务器：bjb1-32546\n- Python：conda base（/root/miniconda3/bin/python）\n- 项目路径：/root/acr-vla-conformal-refinement/\n- 不需要 CRM checkpoint（random selection 不用 CRM）\n\n### 注意事项\n- command 必须用 bash -c \"...\" 包裹（tmux 用 sh，不是 bash）\n- 之前 random selection object 失败是因为 python path 不存在，现在用 conda activate 解决\n- 如果 evaluate.py 里找不到 random selection mode，检查是否需要额外参数（如 --random_selection flag）或是否有单独的脚本",
  "tool_groups": "['ssh', 'registry']",
  "tools": "['submit_training_job']"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "deploy:random-selection-object",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务：部署 Random Selection Object baseline 实验\n\n### 背景\nplan_600 要求 Random Selection baseline（K=10 samples, pick 1 uniformly at random, no conformal ranking）。Spatial 版本已完成（seed42=34%, seed43=26%, seed44=28%），但 Object 版本此前全部失败（python path 问题已修复）。\n\n### 步骤\n\n1. **确认 evaluate.py 的 random selection mode**\n   SSH 到 bjb1-32546，读取 evaluate.py 的可用 mode：\n   ```\n   ssh_read_only: cd /root/acr-vla-conformal-refinement && grep -n \"mode.*random\\|random.*selection\\|choices.*mode\\|argparse.*mode\" src/evaluate.py | head -20\n   ```\n   如果没有 --mode random_selection，检查是否有其他 flag 控制 random selection 行为（如 --selection_method random）。\n\n2. **确认 bjb1-32546 的 cuda:0, cuda:1, cuda:3 空闲**\n   ```\n   ssh_read_only: nvidia-smi --query-gpu=index,memory.used,utilization.gpu --format=csv,noheader\n   ```\n\n3. **在 registry 中创建 3 个实验**\n   用 update_registry 创建：\n   - exp_id: eval-random-selection-object-seed42-r3\n     hypothesis: \"Random Selection (K=10, uniform pick) on LIBERO-Object seed42. Isolates conformal ranking contribution: if Random ≈ VLA-only, then CRM's advantage comes from learned correction not just sampling diversity.\"\n   - exp_id: eval-random-selection-object-seed43\n     hypothesis: \"Random Selection (K=10, uniform pick) on LIBERO-Object seed43. Second seed for Random Selection Object baseline.\"\n   - exp_id: eval-random-selection-object-seed44\n     hypothesis: \"Random Selection (K=10, uniform pick) on LIBERO-Object seed44. Third seed for Random Selection Object baseline.\"\n\n4. **用 submit_training_job 提交 3 个实验**\n   命令模板（根据步骤1确认的 mode flag 调整）：\n   ```\n   bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode {MODE_FLAG} --benchmark object --K 10 --seed {SEED} --n_rollouts 10 --output_file logs/eval_random_selection_object_seed{SEED}.json 2>&1 | tee logs/eval-random-selection-object-seed{SEED}.log\"\n   ```\n   分配：\n   - seed42-r3 → bjb1-32546 cuda:0\n   - seed43 → bjb1-32546 cuda:1\n   - seed44 → bjb1-32546 cuda:3\n\n   submit_training_job 参数：\n   - server: bjb1-32546\n   - project: acr-vla-conformal-refinement\n   - timeout_hours: 12\n   - plan_id: plan_600\n\n5. **验证 3 个实验都成功启动**\n\n### 环境\n- 服务器：bjb1-32546\n- Python：conda base（/root/miniconda3/bin/python）\n- 项目路径：/root/acr-vla-conformal-refinement/\n- 不需要 CRM checkpoint（random selection 不用 CRM）\n\n### 注意事项\n- command 必须用 bash -c \"...\" 包裹（tmux 用 sh，不是 bash）\n- 之前 random selection object 失败是因为 python path 不存在，现在用 conda activate 解决\n- 如果 evaluate.py 里找不到 random selection mode，检查是否需要额外参数（如 --random_selection flag）或是否有单独的脚本",
    "tool_groups": "['ssh', 'registry']",
    "tools": "['submit_training_job']"
  }
}
````

</details>

---

### Tool result

_source line 59 · 2026-05-21T04:32:44.792475+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"849760\", \"log_file\": \"~/runs/acr-vla-conformal-refinement/eval-crm-spatial-k10-seed50.log\", \"gpu_ids\": [\"cuda:4\"], \"server\": \"bjb1-32546\", \"account\": \"root\", \"cuda_visible_devices\": \"4\", \"backend\": \"tmux\", \"tmux_session\": \"eval-crm-spatial-k10-seed50\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 26767
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-21T04:32:55.792471+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"850105\", \"log_file\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed50.log\", \"gpu_ids\": [\"cuda:5\"], \"server\": \"bjb1-32546\", \"account\": \"root\", \"cuda_visible_devices\": \"5\", \"backend\": \"tmux\", \"tmux_session\": \"eval-vla-only-spatial-seed50\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.0}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 35403
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-21T04:33:00.314597+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_deploy_random-selection-object_20260521T043257\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_deploy_random-selection-object_20260521T043257.log\", \"setup_data\": {}, \"message\": \"Worker worker_deploy_random-selection-object_20260521T043257 started. Use get_worker_status('worker_deploy_random-selection-object_20260521T043257') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 21577
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-21T04:33:55.466181+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-21T04:33:55.466990+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_870cc8ef.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-21T04:33:58.331851+00:00_

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
  "session": "cron:hook:eval-vla-only-goal-seed47",
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

_source line 65 · 2026-05-21T04:33:58.432708+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-21T04:34:01.193934+00:00_

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
  "session": "cron:hook:eval-vla-only-goal-seed47",
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

_source line 67 · 2026-05-21T04:34:01.344772+00:00_

/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Glob",
  "elapsed_ms": 150
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-21T04:34:04.061743+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-21T04:34:04.112772+00:00_

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
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-21T04:34:49.449585+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 16/17 在跑 | Worker 3 (GPU 0 / CPU 3, 1个rate-limited失效) | 磁盘: bjb2-40593 90% (46G可用)\n\n## Session #23 状态汇报\n\n### Norm Sweep 数据充分（全面超标）\n| ε | 已完成 seeds | 均值 SR | ROADMAP 目标 | 状态 |\n|---|-------------|---------|-------------|------|\n| 0.03 | 15 (+RUNNING 2) | 14.9% | 10-12 | ✅ 超标 |\n| 0.05 | 15 (+RUNNING 2) | 13.6% | 10-12 | ✅ 超标 |\n| 0.1 | 18 (+RUNNING 2) | 15.3% | 10-12 | ✅ 超标 |\n| 0.2 | 13 | 17.2% | LOCKED | ✅ |\n\n**Figure 2 数据已就绪。**\n\n### 本轮新部署 9 GPU\n修复了 13→7 RUNNING（大量实验间隙完成）导致的 GPU 空窗：\n- **K=20 Object** seed42/43/44 → bjb2-28827:cuda:1,2,3 (plan_601, K-value diminishing returns)\n- **CRM Spatial K=10** seed49/50 → bjb2-28827:cuda:4, bjb1-32546:cuda:4 (Table 1 补种)\n- **VLA-only Spatial** seed50 → bjb1-32546:cuda:5 (Table 1 baseline 补种)\n- **Random Selection Object** seed42/43/44 → bjb1-32546:cuda:0,1,3 (plan_600, Worker 部署中)\n\n### RUNNING 实验全景 (16/17 GPU)\n1. **P90-seed44** (bjb2-28827:0) — Spatial Adaptive-K 末尾 seed，完成后 LOCK sweep\n2. **Norm sweep seed66/67** (bjb1-18228 ×4, bjb1-32546:2, bjb2-28827:5) — 6 个 norm 实验\n3. **K=20 Object** (bjb2-28827:1,2,3) — 新提交\n4. **CRM Spatial** (bjb2-28827:4, bjb1-32546:4) — 新提交\n5. **VLA-only Spatial** (bjb1-32546:5) — 新提交\n6. **Random Selection Object** (bjb1-32546:0,1,3) — Worker 部署中\n\n唯一空闲: bjb2-40593:cuda:0（磁盘 90%，不宜新实验）\n\n### π0.5 诊断进行中\nWorker 正在调查 `resize_with_pad_torch` 输入格式 bug。baseline SR=0% 已确认为归一化问题（QUANTILES→MEAN_STD mismatch）。等待诊断结果确认修复方案。\n\n### 建议\n1. **P0** Figure 2 生成——norm sweep 数据已充分，正在派 Worker 生成\n2. **P0** P90-seed44 完成 → LOCK Spatial Adaptive-K sweep → 更新论文\n3. **P1** plan_302 per-DOF mechanism 分析（analytical，无需 GPU）\n4. **P1** Random Selection Object 完成后与 VLA-only Object (10.8%) 对比——如 Random ≈ VLA-only 则证明 CRM correction 是价值来源",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 16/17 在跑 | Worker 3 (GPU 0 / CPU 3, 1个rate-limited失效) | 磁盘: bjb2-40593 90% (46G可用)\n\n## Session #23 状态汇报\n\n### Norm Sweep 数据充分（全面超标）\n| ε | 已完成 seeds | 均值 SR | ROADMAP 目标 | 状态 |\n|---|-------------|---------|-------------|------|\n| 0.03 | 15 (+RUNNING 2) | 14.9% | 10-12 | ✅ 超标 |\n| 0.05 | 15 (+RUNNING 2) | 13.6% | 10-12 | ✅ 超标 |\n| 0.1 | 18 (+RUNNING 2) | 15.3% | 10-12 | ✅ 超标 |\n| 0.2 | 13 | 17.2% | LOCKED | ✅ |\n\n**Figure 2 数据已就绪。**\n\n### 本轮新部署 9 GPU\n修复了 13→7 RUNNING（大量实验间隙完成）导致的 GPU 空窗：\n- **K=20 Object** seed42/43/44 → bjb2-28827:cuda:1,2,3 (plan_601, K-value diminishing returns)\n- **CRM Spatial K=10** seed49/50 → bjb2-28827:cuda:4, bjb1-32546:cuda:4 (Table 1 补种)\n- **VLA-only Spatial** seed50 → bjb1-32546:cuda:5 (Table 1 baseline 补种)\n- **Random Selection Object** seed42/43/44 → bjb1-32546:cuda:0,1,3 (plan_600, Worker 部署中)\n\n### RUNNING 实验全景 (16/17 GPU)\n1. **P90-seed44** (bjb2-28827:0) — Spatial Adaptive-K 末尾 seed，完成后 LOCK sweep\n2. **Norm sweep seed66/67** (bjb1-18228 ×4, bjb1-32546:2, bjb2-28827:5) — 6 个 norm 实验\n3. **K=20 Object** (bjb2-28827:1,2,3) — 新提交\n4. **CRM Spatial** (bjb2-28827:4, bjb1-32546:4) — 新提交\n5. **VLA-only Spatial** (bjb1-32546:5) — 新提交\n6. **Random Selection Object** (bjb1-32546:0,1,3) — Worker 部署中\n\n唯一空闲: bjb2-40593:cuda:0（磁盘 90%，不宜新实验）\n\n### π0.5 诊断进行中\nWorker 正在调查 `resize_with_pad_torch` 输入格式 bug。baseline SR=0% 已确认为归一化问题（QUANTILES→MEAN_STD mismatch）。等待诊断结果确认修复方案。\n\n### 建议\n1. **P0** Figure 2 生成——norm sweep 数据已充分，正在派 Worker 生成\n2. **P0** P90-seed44 完成 → LOCK Spatial Adaptive-K sweep → 更新论文\n3. **P1** plan_302 per-DOF mechanism 分析（analytical，无需 GPU）\n4. **P1** Random Selection Object 完成后与 VLA-only Object (10.8%) 对比——如 Random ≈ VLA-only 则证明 CRM correction 是价值来源",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-21T04:34:54.677649+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 5228
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-21T04:35:36.132809+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "paper:figure2-norm-sweep",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务：生成论文 Figure 2 — Correction Magnitude (ε) Sweep\n\n### 背景\nFigure 2 展示 CRM correction magnitude (ε) 对 success rate 的影响。两条曲线：\n1. **obs_only** (observation-conditioned CRM): 随 ε 增大，SR 先升后趋稳\n2. **perdof** (per-DoF CRM): 随 ε 增大，SR 急剧下降（progressive collapse）\n\n这是 Claim 2 的核心证据：obs_only 对 magnitude 鲁棒，perdof 不行。\n\n### 数据获取\n1. 用 `read_registry` 获取所有 obs_only 和 perdof 实验（conclusion=success），筛选 LIBERO-Object benchmark\n2. obs_only 分组：\n   - ε=0.03 (norm003 in exp_id): ~15 seeds\n   - ε=0.05 (norm005): ~15 seeds\n   - ε=0.1 (norm01): ~18 seeds\n   - ε=0.2 (norm02): ~13 seeds\n   - ε=0.3 (norm03): 若有\n3. perdof 分组：同上 epsilon 值\n4. 提取每个实验的 overall_success_rate（注意：有的实验用 `overall_success_rate`，有的用 `sr`，有的用 `success_rate`，需兼容）\n\n### 图表设计\n- X 轴: ε (correction magnitude), 对数或线性刻度\n- Y 轴: Success Rate (%)\n- 两条线：obs_only (蓝), perdof (红)\n- Error bars: ±1 std across seeds\n- 水平虚线: VLA-only baseline (~10.8%)\n- 标题不要（论文 figure 在 caption 说明）\n- 字体: 12pt, 粗体 axis labels\n- 图例简洁: \"Obs-conditioned CRM\", \"Per-DoF CRM\", \"VLA-only (no correction)\"\n- 尺寸: 适合单栏 (3.5×2.8 inches)\n- 保存为 PDF + PNG (300 DPI)\n\n### 执行\n1. 在 bjb2-28827 或 bjb1-32546 上执行（选一台有 matplotlib 的服务器）\n2. 先检查 matplotlib 可用：`python -c \"import matplotlib; print(matplotlib.__version__)\"`\n3. 生成图表脚本，SSH 执行\n4. 下载 PDF/PNG 到本地 artifacts 目录\n5. 用 register_artifact 注册\n\n### 输出路径\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figure2_norm_sweep.pdf\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figure2_norm_sweep.png\n\n### 注意\n- 排除 seed42 的 norm02 (ε=0.2) 数据（D084 决策：SR=20% 异常偏高，已排除）\n- ε=0.2 的 range 包含 0.72 和 0.09 的极端值——检查这些是否合理或是异常实验\n- 使用 matplotlib 的 Agg backend（远程服务器无 display）\n- 如果 perdof 数据不够（某些 ε 值缺失），在图中标注，不要编造数据",
  "tool_groups": "['ssh', 'registry', 'knowledge']",
  "tools": "['register_artifact']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "paper:figure2-norm-sweep",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务：生成论文 Figure 2 — Correction Magnitude (ε) Sweep\n\n### 背景\nFigure 2 展示 CRM correction magnitude (ε) 对 success rate 的影响。两条曲线：\n1. **obs_only** (observation-conditioned CRM): 随 ε 增大，SR 先升后趋稳\n2. **perdof** (per-DoF CRM): 随 ε 增大，SR 急剧下降（progressive collapse）\n\n这是 Claim 2 的核心证据：obs_only 对 magnitude 鲁棒，perdof 不行。\n\n### 数据获取\n1. 用 `read_registry` 获取所有 obs_only 和 perdof 实验（conclusion=success），筛选 LIBERO-Object benchmark\n2. obs_only 分组：\n   - ε=0.03 (norm003 in exp_id): ~15 seeds\n   - ε=0.05 (norm005): ~15 seeds\n   - ε=0.1 (norm01): ~18 seeds\n   - ε=0.2 (norm02): ~13 seeds\n   - ε=0.3 (norm03): 若有\n3. perdof 分组：同上 epsilon 值\n4. 提取每个实验的 overall_success_rate（注意：有的实验用 `overall_success_rate`，有的用 `sr`，有的用 `success_rate`，需兼容）\n\n### 图表设计\n- X 轴: ε (correction magnitude), 对数或线性刻度\n- Y 轴: Success Rate (%)\n- 两条线：obs_only (蓝), perdof (红)\n- Error bars: ±1 std across seeds\n- 水平虚线: VLA-only baseline (~10.8%)\n- 标题不要（论文 figure 在 caption 说明）\n- 字体: 12pt, 粗体 axis labels\n- 图例简洁: \"Obs-conditioned CRM\", \"Per-DoF CRM\", \"VLA-only (no correction)\"\n- 尺寸: 适合单栏 (3.5×2.8 inches)\n- 保存为 PDF + PNG (300 DPI)\n\n### 执行\n1. 在 bjb2-28827 或 bjb1-32546 上执行（选一台有 matplotlib 的服务器）\n2. 先检查 matplotlib 可用：`python -c \"import matplotlib; print(matplotlib.__version__)\"`\n3. 生成图表脚本，SSH 执行\n4. 下载 PDF/PNG 到本地 artifacts 目录\n5. 用 register_artifact 注册\n\n### 输出路径\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figure2_norm_sweep.pdf\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figure2_norm_sweep.png\n\n### 注意\n- 排除 seed42 的 norm02 (ε=0.2) 数据（D084 决策：SR=20% 异常偏高，已排除）\n- ε=0.2 的 range 包含 0.72 和 0.09 的极端值——检查这些是否合理或是异常实验\n- 使用 matplotlib 的 Agg backend（远程服务器无 display）\n- 如果 perdof 数据不够（某些 ε 值缺失），在图中标注，不要编造数据",
    "tool_groups": "['ssh', 'registry', 'knowledge']",
    "tools": "['register_artifact']"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-21T04:35:41.180380+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_figure2-norm-sweep_20260521T043537\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_paper_figure2-norm-sweep_20260521T043537.log\", \"setup_data\": {}, \"message\": \"Worker worker_paper_figure2-norm-sweep_20260521T043537 started. Use get_worker_status('worker_paper_figure2-norm-sweep_20260521T043537') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 5047
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-21T04:35:50.932874+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-21T04:35:50.933318+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-21T04:36:50.667338+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['exp_id', 'status', 'spec']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['exp_id', 'status', 'spec']"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-21T04:36:52.883580+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.125870 --k_full 10 --benchmark spatial --seed 44 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p90_seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"pid\": 975409, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-adaptive-k-spatial-p90-seed44-bjb2.log\", \"submitted_at\": \"2026-05-20T13:50:48.545Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"model_name\": \"CRM_obs_only_adaptive_k\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}}, \"eval-obs-only-object-norm005-seed67\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"detected on GPU, submitted by prior Worker but not registered\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/autodl-tmp/acr-vla-conformal-refinement/\", \"data_count\": \"100 rollouts\", \"model_name\": \"crm_v3_norm/obs_only\", \"seed\": 67, \"gpu\": \"cuda:2\"}}, \"eval-obs-only-object-norm003-seed67\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"detected on GPU, submitted by prior Worker but not registered\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/acr-vla-conformal-refinement/\", \"data_count\": \"100 rollouts\", \"model_name\": \"crm_v3_norm/obs_only\", \"seed\": 67, \"gpu\": \"cuda:5\"}}, \"eval-obs-only-object-norm01-seed67\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 evaluate.py --benchmark object --K 10 --mode crm_obs_only --max_correction_norm 0.1 --seed 67 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoint
…[truncated 1580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2216
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-21T04:37:01.686758+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-obs-only-object-norm02-k20-seed42'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-obs-only-object-norm02-k20-seed42'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-21T04:37:02.341374+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-crm-spatial-k10-seed49'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-crm-spatial-k10-seed49'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-21T04:37:03.146429+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.4205}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1459
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-21T04:37:03.247119+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-vla-only-spatial-seed50'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-vla-only-spatial-seed50'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-21T04:37:04.602149+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.4459}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2260
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-21T04:37:07.161377+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.5177}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 3914
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-21T04:37:13.538422+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'PREPARING'}",
  "project": "acr-vla-conformal-refinement",
  "limit": "5",
  "fields": "['exp_id', 'status']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'PREPARING'}",
    "project": "acr-vla-conformal-refinement",
    "limit": "5",
    "fields": "['exp_id', 'status']"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-21T04:37:14.945987+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-random-selection-object-seed42-r3\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed50\": {\"status\": \"PREPARING\"}, \"eval-crm-spatial-k10-seed50\": {\"status\": \"PREPARING\"}, \"eval-crm-spatial-k10-seed49\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm02-k20-seed44\": {\"status\": \"PREPARING\"}}, \"count\": 5, \"total\": 45, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3935}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1407
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-21T04:37:36.503239+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm02-k20-seed42",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark object --K 20 --seed 42 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_k20_seed42.json\"', 'server': 'bjb2-28827', 'gpu': 'cuda:1', 'pid': 10438, 'data_path': 'LIBERO-Object', 'data_count': 100, 'model_name': 'CRM_obs_only_K20', 'seed': 42, 'log_path': '~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k20-seed42.log', 'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm02-k20-seed42",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark object --K 20 --seed 42 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_k20_seed42.json\"', 'server': 'bjb2-28827', 'gpu': 'cuda:1', 'pid': 10438, 'data_path': 'LIBERO-Object', 'data_count': 100, 'model_name': 'CRM_obs_only_K20', 'seed': 42, 'log_path': '~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k20-seed42.log', 'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt'}"
  }
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-21T04:37:38.511354+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm02-k20-seed43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark object --K 20 --seed 43 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_k20_seed43.json\"', 'server': 'bjb2-28827', 'gpu': 'cuda:2', 'pid': 10781, 'data_path': 'LIBERO-Object', 'data_count': 100, 'model_name': 'CRM_obs_only_K20', 'seed': 43, 'log_path': '~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k20-seed43.log', 'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm02-k20-seed43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark object --K 20 --seed 43 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_k20_seed43.json\"', 'server': 'bjb2-28827', 'gpu': 'cuda:2', 'pid': 10781, 'data_path': 'LIBERO-Object', 'data_count': 100, 'model_name': 'CRM_obs_only_K20', 'seed': 43, 'log_path': '~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k20-seed43.log', 'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt'}"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-21T04:37:39.064489+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 2.1929}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2561
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-21T04:37:41.848450+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm02-k20-seed44",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark object --K 20 --seed 44 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_k20_seed44.json\"', 'server': 'bjb2-28827', 'gpu': 'cuda:3', 'pid': 11078, 'data_path': 'LIBERO-Object', 'data_count': 100, 'model_name': 'CRM_obs_only_K20', 'seed': 44, 'log_path': '~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k20-seed44.log', 'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm02-k20-seed44",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark object --K 20 --seed 44 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_k20_seed44.json\"', 'server': 'bjb2-28827', 'gpu': 'cuda:3', 'pid': 11078, 'data_path': 'LIBERO-Object', 'data_count': 100, 'model_name': 'CRM_obs_only_K20', 'seed': 44, 'log_path': '~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k20-seed44.log', 'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt'}"
  }
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-21T04:37:45.612494+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-k10-seed49",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark spatial --K 10 --seed 49 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed49.json\"', 'server': 'bjb2-28827', 'gpu': 'cuda:4', 'pid': 11357, 'data_path': 'LIBERO-Spatial', 'data_count': 100, 'model_name': 'CRM_obs_only', 'seed': 49, 'log_path': '~/runs/acr-vla-conformal-refinement/eval-crm-spatial-k10-seed49.log', 'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-k10-seed49",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark spatial --K 10 --seed 49 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed49.json\"', 'server': 'bjb2-28827', 'gpu': 'cuda:4', 'pid': 11357, 'data_path': 'LIBERO-Spatial', 'data_count': 100, 'model_name': 'CRM_obs_only', 'seed': 49, 'log_path': '~/runs/acr-vla-conformal-refinement/eval-crm-spatial-k10-seed49.log', 'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt'}"
  }
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-21T04:37:48.380326+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-k10-seed50",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark spatial --K 10 --seed 50 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed50.json\"', 'server': 'bjb1-32546', 'gpu': 'cuda:4', 'pid': 849760, 'data_path': 'LIBERO-Spatial', 'data_count': 100, 'model_name': 'CRM_obs_only', 'seed': 50, 'log_path': '~/runs/acr-vla-conformal-refinement/eval-crm-spatial-k10-seed50.log', 'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-k10-seed50",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode obs_only --benchmark spatial --K 10 --seed 50 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed50.json\"', 'server': 'bjb1-32546', 'gpu': 'cuda:4', 'pid': 849760, 'data_path': 'LIBERO-Spatial', 'data_count': 100, 'model_name': 'CRM_obs_only', 'seed': 50, 'log_path': '~/runs/acr-vla-conformal-refinement/eval-crm-spatial-k10-seed50.log', 'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt'}"
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-21T04:37:50.689974+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed50",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 50 --n_rollouts 10 --output_file logs/eval_vla_only_spatial_seed50.json\"', 'server': 'bjb1-32546', 'gpu': 'cuda:5', 'pid': 850105, 'data_path': 'LIBERO-Spatial', 'data_count': 100, 'model_name': 'SmolVLA-base', 'seed': 50, 'log_path': '~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed50.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed50",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 50 --n_rollouts 10 --output_file logs/eval_vla_only_spatial_seed50.json\"', 'server': 'bjb1-32546', 'gpu': 'cuda:5', 'pid': 850105, 'data_path': 'LIBERO-Spatial', 'data_count': 100, 'model_name': 'SmolVLA-base', 'seed': 50, 'log_path': '~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed50.log'}"
  }
}
```

</details>

---

### Assistant

_source line 93 · 2026-05-21T04:41:31.187325+00:00_

submit_training_job 启动了进程但没更新 registry 状态。需要手动转 RUNNING + 设置 spec。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-vla-only-goal-seed47"
}
```

</details>

---

## Round 2

40 recorded events

### User

_source line 94 · 2026-05-21T21:23:59.952176+00:00_

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
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-21T21:25:05.134780+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-21T21:25:05.587690+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/camera_ready_template/corl_2026_template_cameraready/corlabbrvnat.bst
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/camera_ready_template/corl_2026_template_cameraready/example.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/review_template/corl_2026_template_submission/corlabbrvnat.bst
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/review_template/corl_2026_template_submission/example.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/camera_ready_template/corl_2026_template_cameraready/example.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/camera_ready_template/corl_2026_template_cameraready/corl_2026.sty
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/review_template/corl_2026_template_submission/corl_2026.sty
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/corl2026_camera_ready_template.zip
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/review_template/corl_2026_template_submission/example.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/corl2026_review_template.zip
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/feishu_group_oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4_director.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/study_status.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/
…[truncated 13087 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-21T21:25:05.588111+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/registry.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/registry.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-21T21:25:05.695578+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Glob",
  "elapsed_ms": 107
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-21T21:25:08.767604+00:00_

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
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-21T21:25:09.120762+00:00_

File content (876.8KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-21T21:25:09.121158+00:00_

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
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-21T21:25:09.676723+00:00_

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
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "elapsed_ms": 555
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-21T21:25:09.677215+00:00_

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
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-21T21:25:10.179590+00:00_

1	# Handover — 2026-05-21
2	
3	> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4	
5	## 运行中
6	| exp_id | 假设 | 状态 | 关键指标 | W&B |
7	|--------|------|------|---------|-----|
8	| crm-train-pi05-spatial-full | CRM projection trained on π0.5 full precomputed features (~60250 spatial samples, K=10) will learn conformal refinement corrections improving upon π0.5 VLA-only baseline (84.2%) on LIBERO-Spatial, validating cross-VLA generalization | — | — | — |
9	
10	## 待处理
11	- crm-pipeline-auto（准备中）
12	- precompute-pi05-obj-s6-r2（准备中）
13	- …另有 82 项
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
51	- crm-train
…[truncated 5199 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-21T21:25:10.179946+00:00_

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
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-21T21:25:10.230375+00:00_

1	# π0.5 CRM Eval 前置准备报告
2	
3	**日期**: 2026-05-22
4	
5	## 1. Object CRM Training 进度 (bjb1-18228)
6	
7	| 指标 | 值 |
8	|------|-----|
9	| 当前进度 | Epoch 7/50, batch 1350/1950 |
10	| 已运行时间 | 52 min 33 sec |
11	| 最佳 val_loss | 0.005511 (epoch 6) |
12	| 当前 train_loss | 0.009881 (epoch 6) |
13	| 预估速度 | ~7.8 min/epoch |
14	| 预计剩余时间 | ~5.5 小时 |
15	| 进程 PID | 800111 |
16	| 输出目录 | `/root/autodl-tmp/checkpoints/crm_pi05_full/object/` |
17	
18	训练命令: `python -u src/train_crm.py --benchmark object --cache_dir /root/autodl-tmp/crm_cache_pi05/ --output_dir /root/autodl-tmp/checkpoints/crm_pi05_full/object/ --epochs 50 --batch_size 32 --lr 1e-3 --obs_dim 2048`
19	
20	## 2. 代码同步状态
21	
22	| 服务器 | evaluate.py 大小 | 版本状态 | Git 状态 |
23	|--------|------------------|----------|----------|
24	| bjb1-32546 | 33058 bytes ✅ | 最新 | 无 .git（直接拷贝） |
25	| bjb2-28827 | 33058 bytes ✅ | 最新 | 有 .git 但无 remote |
26	
27	⚠️ 三台服务器均无有效 git remote。代码此前通过 rsync/scp 同步。当前 evaluate.py 已是最新版本（33058 bytes），无需操作。
28	
29	## 3. Eval 环境检查
30	
31	| 服务器 | PyTorch | CUDA | GPU 数量 | evaluate.py --help | pi05 模型 |
32	|--------|---------|------|----------|-------------------|-----------|
33	| bjb1-32546 | 2.10.0+cu128 ✅ | True ✅ | 6 | OK ✅ | 7.5GB model.safetensors ✅ |
34	| bjb2-28827 | 2.10.0+cu128 ✅ | True ✅ | 6 | OK ✅ | 7.5GB model.safetensors ✅ |
35	
36	两台 eval 服务器环境就绪。
37	
38	## 4. CRM Checkpoint 状态 (bjb1-18228)
39	
40	| 目录 | 内容 | 状态 |
41	|------|------|------|
42	| `crm_pi05_full/object/` | epoch 2-6 checkpoints + crm_best.pt (2.4MB) | ✅ 当前训练输出目录 |
43	| `crm_pi05/object/` | epoch 1-3 checkpoints | ⚠️ 旧 run 残留 |
44	| `crm_pi05/spatial/` | epoch 2-6 checkpoints + crm_best.pt (2.4MB) | ✅ Spatial CRM 已有 best model |
45	
46	## 结论
47	
48	- **Object CRM**: 训练正常推进中，约 5.5h 后完成全部 50 epochs。当前 best checkpoint 可用于早期 eval 测试。
49	- **Eval 环境**: 两台服务器全部就绪（代码、PyTorch、模型均 OK）。
50	- **可立即执行**: 用 `crm_pi05_full/object/crm_best.pt` 做 Object benchmark 早期 eval；用 `crm_pi05/spatial/crm_best.pt` 做 Spatial benchmark eval。
51	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-21T21:25:16.933869+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-21T21:25:17.336756+00:00_

1	baseline: null
2	experiments:
3	  mvp-point-reaching:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-13T01:22:10.415Z'
7	    updated_at: '2026-05-17T03:13:35.534Z'
8	    spec:
9	      hypothesis: Per-DOF uncertainty features carry more actionable information than
10	        scalar uncertainty summaries, enabling dimension-selective correction
11	      description: '3D point-reaching MVP: 3 MLP variants (scalar/per-DOF/no uncertainty)
12	        x 6 groups (3 anisotropy ratios x 2 uncertainty sources)'
13	      server: bjb2-40593
14	      gpu: cuda:0
15	      data_count: 20000
16	      model_name: CorrectionMLP(2-layer, 64-hidden)
17	      seed: 42
18	      command: python -u run_mvp.py
19	      data_path: synthetic (generated in-script)
20	      checkpoint_path: /root/acr-vla-conformal-refinement/mvp/
21	      log_path: /root/acr-vla-conformal-refinement/mvp/mvp_results.log
22	    conclusion: success
23	    completed_at: '2026-05-13T01:44:00.055Z'
24	    metrics:
25	      group1_oracle:
26	        A_scalar:
27	          mse_x: 0.180218
28	          mse_y: 0.02497
29	          mse_z: 0.024232
30	          total: 0.076473
31	        B_perDOF:
32	          mse_x: 0.172652
33	          mse_y: 0.015544
34	          mse_z: 0.01561
35	          total: 0.067935
36	        C_none:
37	          mse_x: 0.22706
38	          mse_y: 0.025542
39	          mse_z: 0.024753
40	          total: 0.092451
41	      group2_oracle:
42	        A_scalar:
43	          mse_x: 0.064642
44	          mse_y: 0.023836
45	          mse_z: 0.022967
46	          total: 0.037148
47	        B_perDOF:
48	          mse_x: 0.053403
49	          mse_y: 0.015695
50	          mse_z: 0.01573
51	          total: 0.028276
52	        C_none:
53	          mse_x: 0.084178
54	          mse_y: 0.025427
55	          mse_z: 0.024798
56	          total: 0.044801
57	      group3_oracle:
58	        A_scalar:
59	          mse_x: 0.042948
60	          mse_y: 0.023218
61	          mse_z: 0.022365
62	   
…[truncated 1033 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-21T21:25:17.538666+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-21T21:25:18.299453+00:00_

1	_next_id: 106
2	decisions:
3	- id: D001
4	  date: 2026-05-13 01:03 UTC
5	  summary: MVP 方案确定：3D Point-Reaching Motivating Experiment 验证 per-DOF conformal 特征的信息优势
6	  rationale: IDEA_BRIEF 已设计了完美的 go/no-go gate：用合成数据的 3D reaching task 对比 per-DOF vs
7	    标量 vs 无不确定性三种 conditioning，直接测试核心假设。成本极低（<0.5 GPU-hours），无需 VLA 基础设施，失败则提前止损。Pass
8	    标准明确：B 在非扰动轴 MSE 比 A 低 >10%。
9	  related_experiments: []
10	  depends_on: []
11	- id: D002
12	  date: 2026-05-13 01:06 UTC
13	  summary: 采纳 Reviewer 建议完善 MVP：增加 B vs C 对比（>5% MSE）、K=10 estimated uncertainty variant、2:1/1.5:1
14	    各向异性 sweep
15	  rationale: Reviewer 正确指出 (1) 缺少 B vs C 对比会遗漏"观测特征已足够"的可能性，这直接关系核心 claim；(2) oracle
16	    uncertainty 与实际 pipeline 存在 gap，K=10 variant 几乎零成本可验证；(3) 5:1 比率过极端，需测试更温和情况。三项改进均不增加显著成本。
17	  related_experiments: []
18	  depends_on:
19	  - D001
20	- id: D003
21	  date: 2026-05-13 01:47 UTC
22	  summary: MVP 通过，GO — 进入 research 阶段
23	  rationale: 全部 3 条 pass 标准满足且 margin 很大：per-DOF (B) 在非扰动轴 MSE 比标量 (A) 低 22-38%，比无
24	    uncertainty (C) 低 15-39%。K=10 estimated 和弱各向异性(1.5:1)下均成立。核心假设"per-DOF conformal
25	    特征携带更多可操作信息"得到验证。关注风险：oracle→K=10 衰减 ~15pp，真实 7-DOF 场景待验证。
26	  related_experiments:
27	  - exp_id: mvp-point-reaching
28	    role: MVP gate
29	    result: PASS — all 6 conditions met criteria
30	  depends_on:
31	  - D001
32	  - D002
33	- id: D004
34	  date: 2026-05-13 02:59 UTC
35	  summary: Horizon 策略：截取 chunk 前 H_eff=5 步，action_dim=6。CGS 输出 40D。
36	  rationale: SmolVLA chunk_size=50 远超原假设 H=5。receding-horizon 执行语义下只需关注近期 action 的
37	    uncertainty，远期 step 对当前校正无意义。H_eff=5 保持与 IDEA_BRIEF 设计一致，CGS 40D 可控（per-DOF std
38	    30 + radius 5 + volume 5），p/n=6/10=0.6 优于原假设 0.7。H_eff=10 留作 ablation。action_dim=6
39	    使 Ledoit-Wolf 更稳定。
40	  related_experiments: []
41	  depends_on:
42	  - D003
43	- id: D005
44	  date: 2026-05-13 03:00 UTC
45	  summary: 不等 Dream 重新提交，直接启动 P0 实验。Dream zombie 占槽，Reviewer 已两轮审核通过 framing/plan。
46	  rationale: Dream dream_20260513T015051 崩溃在 review 阶段（imagine+write
…[truncated 2521 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "elapsed_ms": 760
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-21T21:25:18.508193+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper_framing.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper_framing.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-21T21:25:18.660331+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Glob",
  "elapsed_ms": 152
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-21T21:25:23.464838+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "status: (RUNNING|PREPARING|ALLOCATED|QUEUED)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "output_mode": "content",
  "-B": "3",
  "-A": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Grep",
  "tool_args": {
    "pattern": "status: (RUNNING|PREPARING|ALLOCATED|QUEUED)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "output_mode": "content",
    "-B": "3",
    "-A": "1"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-21T21:25:23.936846+00:00_

7759-    metrics:
7760-      overall_success_rate: 0.14
7761-  eval-obs-only-object-norm02-k20-seed42:
7762:    status: PREPARING
7763-    retry_count: 2
--
12004-    conclusion: failed
12005-    completed_at: '2026-05-19T14:32:21.490Z'
12006-  eval-obs-only-object-norm02-k20-seed43:
12007:    status: PREPARING
12008-    retry_count: 0
--
12030-    failure_reason: 'Director DROP 决策: K=20 代码/参数不支持，三次部署失败。K-value curve 已有 K=1/5/10
12031-      三点。'
12032-  eval-obs-only-object-norm02-k20-seed44:
12033:    status: PREPARING
12034-    retry_count: 0
--
14162-    conclusion: failed
14163-    completed_at: '2026-05-20T03:02:41.906Z'
14164-  eval-vla-only-spatial-seed49-r2:
14165:    status: PREPARING
14166-    retry_count: 0
--
14447-    log_path: logs/eval_adaptive_k_p25_seed43.json
14448-    completed_at: '2026-05-20T05:56:34.512Z'
14449-  eval-adaptive-k-p25-seed44:
14450:    status: PREPARING
14451-    retry_count: 0
--
14568-    checkpoint_path: /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json
14569-    completed_at: '2026-05-20T06:53:17.867Z'
14570-  eval-openvla-object-baseline-seed42-r2:
14571:    status: PREPARING
14572-    retry_count: 0
--
14578-    parent: eval-openvla-object-baseline-seed42
14579-    spec: placeholder
14580-  eval-vla-only-spatial-seed50:
14581:    status: PREPARING
14582-    retry_count: 0
--
14605-      total: 100
14606-    conclusion: success
14607-  eval-crm-spatial-seed47:
14608:    status: PREPARING
14609-    retry_count: 0
--
14626-      backend: tmux
14627-      account: root
14628-  eval-vla-only-object-seed49-r2:
14629:    status: PREPARING
14630-    retry_count: 0
--
14644-      backend: tmux
14645-      account: root
14646-  eval-crm-spatial-seed48:
14647:    status: PREPARING
14648-    retry_count: 0
--
14669-      total: 100
14670-    conclusion: success
14671-  eval-crm-spatial-k10-seed49:
14672:    status: PREPARING
14673-    retry_count: 0
--
14697-      n_rollouts: 10
14698-      total: 100
14699-  eval
…[truncated 5035 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Grep",
  "elapsed_ms": 472
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-21T21:25:23.937312+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-21T21:25:24.840047+00:00_

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
…[truncated 5493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "elapsed_ms": 902
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-21T21:25:24.992485+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/pi05_eval_commands.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/pi05_eval_commands.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-21T21:25:25.093142+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/intermediate/pi05_eval_commands.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/pi05_eval_commands.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/report/pi05_eval_commands.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-21T21:25:34.818873+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "crm-train-pi05",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "output_mode": "content",
  "-A": "30",
  "head_limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Grep",
  "tool_args": {
    "pattern": "crm-train-pi05",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "output_mode": "content",
    "-A": "30",
    "head_limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-21T21:25:35.327819+00:00_

21957:  crm-train-pi05-object:
21958-    status: DONE
21959-    retry_count: 0
21960-    created_at: '2026-05-21T17:52:37.705Z'
21961-    updated_at: '2026-05-21T18:10:26.906Z'
21962-    hypothesis: CRM projection trained on π0.5 precomputed features (49700 object
21963-      samples, K=10) will learn to predict conformal refinement corrections that improve
21964-      upon π0.5 VLA-only baseline (81.5%) on LIBERO-Object, validating cross-VLA generalization
21965-      of CRM beyond SmolVLA
21966-    spec:
21967-      command: nohup python src/train_crm.py --benchmark object --cache_dir /root/autodl-tmp/crm_cache_pi05/
21968-        --output_dir /root/autodl-tmp/checkpoints/crm_pi05/object/ --epochs 50 --batch_size
21969-        32 --obs_dim 2048
21970-      server: bjb1-18228
21971-      gpu: cuda:0
21972-      pid: 795874
21973-      data_path: /root/autodl-tmp/crm_cache_pi05/object/
21974-      data_count: 49700
21975-      model_name: crm-pi05-object
21976-      seed: 42
21977-      checkpoint_path: N/A - incomplete data, pipeline validation only
21978-      log_path: N/A
21979-    notes: ⚠️ INCOMPLETE DATA (68.5% coverage). Pipeline validation only - checkpoint
21980-      NOT for paper. Will retrain after precompute completes with full ~72500 samples.
21981-    conclusion: killed
21982-    completed_at: '2026-05-21T18:10:26.906Z'
21983:  crm-train-pi05-spatial:
21984-    status: DONE
21985-    retry_count: 0
21986-    created_at: '2026-05-21T17:52:42.182Z'
21987-    updated_at: '2026-05-21T18:10:31.701Z'
21988-    hypothesis: CRM projection trained on π0.5 precomputed features (38500 spatial
21989-      samples, K=10) will learn to predict conformal refinement corrections that improve
21990-      upon π0.5 VLA-only baseline (84.2%) on LIBERO-Spatial, validating cross-VLA
21991-      generalization of CRM beyond SmolVLA
21992-    spec:
21993-      command: nohup python src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_pi05/
21994-     
…[truncated 3820 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Grep",
  "elapsed_ms": 508
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-21T21:25:35.478816+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/study_status.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/study_status.yaml",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-21T21:25:36.080685+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_870cc8ef. Did you mean study_status.lock?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "elapsed_ms": 601
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-21T21:25:36.233649+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/pi05_eval_commands.md",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/pi05_eval_commands.md",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-21T21:25:36.287507+00:00_

1	# π0.5 Plan A Eval Commands（6 runs）
2	
3	## 脚本验证结论
4	
5	- 脚本：`/root/acr-vla-conformal-refinement/src/evaluate.py`
6	- `--mode acr_vla` 已支持（docstring 注释为 "alias for crm_perdof — the full ACR-VLA pipeline"）
7	- `--model pi05` 已支持（choices=[smolvla, pi05]）
8	- `--obs_dim` 默认 960 (`OBS_DIM` from utils.py)，π0.5 必须显式传 `--obs_dim 2048`
9	- `--crm_checkpoint` 是 `--checkpoint` 的别名（acr_vla 模式专用）
10	- **`--cache_dir` 不是 eval 参数**（只有 train_crm.py 用），原任务描述里的 `&lt;MERGED_CACHE_DIR>` 占位符忽略
11	- CRM checkpoint 目录已建好：`/root/autodl-tmp/checkpoints/crm_pi05/{object,spatial}/`（按 benchmark 分目录，等训练完产出 `crm_best.pt`）
12	
13	## 占位符
14	
15	- `&lt;CRM_CHECKPOINT_OBJECT>`：CRM training 完成后填入，预期路径 `/root/autodl-tmp/checkpoints/crm_pi05/object/crm_best.pt`
16	- `&lt;CRM_CHECKPOINT_SPATIAL>`：预期路径 `/root/autodl-tmp/checkpoints/crm_pi05/spatial/crm_best.pt`
17	- 如果 CRM training 用单一共享 checkpoint，两个占位符填同一路径
18	
19	## 通用前缀（所有命令复用）
20	
21	```bash
22	source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
23	cd /root/acr-vla-conformal-refinement
24	```
25	
26	## GPU 分配（6 runs 分散到 3 台服务器，每台 2 GPU）
27	
28	| # | Benchmark | Seed | Server       | GPU    |
29	|---|-----------|------|--------------|--------|
30	| 1 | object    | 42   | bjb1-32546   | cuda:0 |
31	| 2 | object    | 43   | bjb1-32546   | cuda:1 |
32	| 3 | object    | 44   | bjb2-28827   | cuda:0 |
33	| 4 | spatial   | 42   | bjb2-28827   | cuda:1 |
34	| 5 | spatial   | 43   | bjb1-18228   | cuda:0 |
35	| 6 | spatial   | 44   | bjb1-18228   | cuda:1 |
36	
37	Notes:
38	- bjb1-18228 训练完 CRM 后再分配 eval（避免抢占 CRM training GPU）
39	- bjb1-32546 和 bjb2-28827 各 6 GPU，未来扩展 ablation 时还有 4 GPU 余量
40	
41	## 6 个完整命令
42	
43	### Run 1: object / seed 42 / bjb1-32546 / cuda:0
44	
45	```bash
46	source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
47	cd /root/acr-vla-conformal-refinement
48	CUDA_VISIBLE_DEVICES=0 TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py \
49	  --model pi05 \
50	  --mode acr_vla \
51	  --benchmark object \
52	  --seed 42 
…[truncated 900 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-21T21:25:41.815038+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "gpu_ids",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "output_mode": "content",
  "-C": "3",
  "glob": "*.yaml",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Grep",
  "tool_args": {
    "pattern": "gpu_ids",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
    "output_mode": "content",
    "-C": "3",
    "glob": "*.yaml",
    "head_limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-21T21:25:42.369595+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml-1880-      submitted_via: submit_training_job
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml-1881-      backend: tmux
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml-1882-      account: root
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml:1883:      gpu_ids:
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml-1884-      - cuda:1
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml-1885-      data_path: /root/autodl-tmp/libero_data/ (spatial)
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml-1886-      data_count: 100
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml-1945-      submitted_via: submit_training_job
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml-1946-      backend: tmux
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml-1947-      account: root
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml:1948:      gpu_ids:
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml-1949-      - cuda:2
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml-1950-      data_path: /root/autodl-tmp/libero_data/ (spatial)
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml-1951-      data_count: 100
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml-2169-        10 --seed 42 --K 10 --crm_check
…[truncated 1827 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Grep",
  "elapsed_ms": 554
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-21T21:25:42.524485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
  "offset": "300",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
    "offset": "300",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-21T21:25:42.575344+00:00_

300	    (features computed fresh each step from K new samples, provide real-time uncertainty
301	    that obs_features alone cannot). Eval success rate is the definitive test. v4-default
302	    (perdof, norm=1.42) is dead and already shown 0/5 on task 1 (D019) — replace with
303	    higher-priority obs_only eval. Use max_norm=0.1 for fair comparison with v4-small
304	    (perdof, norm=0.1). If obs_only eval >= perdof eval → Claim 1 needs fundamental
305	    reframing. If perdof eval > obs_only eval despite worse training loss → compelling
306	    story about conformal features'' value under distribution shift.'
307	  related_experiments:
308	  - exp_id: crm-train-v3-norm-obs-only
309	    role: evidence
310	    result: val_loss=0.0165, best_epoch=48
311	  - exp_id: crm-train-v3-norm-scalar-unc
312	    role: evidence
313	    result: val_loss=0.0374, best_epoch=46
314	  - exp_id: crm-train-v3-norm
315	    role: evidence
316	    result: perdof val_loss=0.0358, best_epoch=47
317	  - exp_id: eval-acr-spatial-v4-default
318	    role: failed
319	    result: Process dead, 0/10 tasks completed
320	  depends_on:
321	  - D019
322	  - D018
323	- id: D021
324	  date: 2026-05-15 01:23 UTC
325	  summary: 'D021: 撤销 D011，重新瞄准 CoRL 2026（abstract DDL ~May 26）。用户承诺提供更多 GPU。全面加速。'
326	  rationale: 用户明确指示重新瞄准 CoRL 2026，表示相信团队能力并愿意提供更多显卡。D011 放弃 CoRL 的主要原因是时间线（pipeline
327	    未跑通 + 13 天不够），现在 pipeline 已修复（wrapper bugs 全部解决，CRM 训练流程验证通过，eval 流程运转中）。距离 abstract
328	    DDL ~May 26 还有 11 天，full paper DDL 估计 ~Jun 2 还有 18 天。AI 团队 24/7 运转，有足够 GPU 并行后，关键路径：(1)
329	    完成当前 5 路 eval（~6h），(2) 确定 framing 方向（1 天），(3) 并行铺全部 ablation + object benchmark（2-3
330	    天），(4) Paper Agent 写初稿（1-2 天），(5) 迭代审稿（2-3 天）。总计 ~8-10 天，紧但可行。需要 12 张额外 GPU 卡实现全面并行。
331	  related_experiments: []
332	  depends_on:
333	  - D011
334	  - D020
335	- id: D022
336	  date: 2026-05-15 01:59 UTC
337	  summary: 'D022: CoRL 论文降为 2 Claims (drop Claim 3 SRPO stacking)，立即准备 Claim 1 备选
338	    framing'
339	  rationale: 'Reviewer 正确指出两
…[truncated 8007 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-21T21:25:49.460116+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "^- id: D10[0-5]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
  "output_mode": "content",
  "-A": "20",
  "head_limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Grep",
  "tool_args": {
    "pattern": "^- id: D10[0-5]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml",
    "output_mode": "content",
    "-A": "20",
    "head_limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-21T21:25:49.912801+00:00_

1882:- id: D100
1883-  date: 2026-05-21 05:26 UTC
1884-  summary: 'D100: Spatial Adaptive K Sweep LOCKED — P90 33.0%±2.6% 完成，全 4 阈值 3 seeds
1885-    齐备'
1886-  rationale: 'P90-seed44=36% 确认（另一台服务器成功完成，bjb2-28827 版本被 cron 误标 failed 可忽略）。完整 Spatial
1887-    sweep: P25 31.7%±1.5%, P50 32.0%±1.7%, P75 32.7%±1.5%, P90 33.0%±2.6%。所有变体 SR
1888-    持平（31.7-33.0%），compute 差 2×（avg_K 3.5→7.65）。Spatial 上 P90 是 Pareto 最优（33.0% +
1889-    avg_K 3.5），与 Object 上 P50 最优不同——阈值自动适配任务复杂度的 narrative 成立。vs CRM K=10 34.6%±1.4%,
1890-    vs VLA-only 29.6%±1.1%。'
1891-  related_experiments:
1892-  - exp_id: eval-adaptive-k-spatial-p90-seed44
1893-    role: trigger
1894-    result: SR=36%, avg_K=3.56, fast_path=80.5%
1895-  - exp_id: eval-adaptive-k-spatial-p90-seed44-bjb2
1896-    role: duplicate_failed
1897-    result: cron false positive, ignored
1898-  depends_on:
1899-  - D097
1900-  - D098
1901:- id: D101
1902-  date: 2026-05-21 06:38 UTC
1903-  summary: 'D101: π0.5 模型有效 (lerobot-eval 100% SR) — wrapper bug 确认，π0.5 线 GO'
1904-  rationale: '官方 lerobot-eval 用 pepijn223/pi05_libero_31_9_non_q 跑 libero_object task_id=0:
1905-    3/3 episodes 成功(100% SR)，每 episode ~140 步，gripper 正常。我们 wrapper 5 轮修复全部 0%。模型有效，问题在
1906-    wrapper——最可能是 _fix_vision_tower_keys() 看似修复但权重未真正加载（strict=False 静默忽略）。值得继续 debug:
1907-    π0.5 baseline ~72%+ 将同时解决 M1(narrow scope) 和 R2-W1(low absolute SR)。'
1908-  related_experiments:
1909-  - exp_id: eval-pi05-baseline-object-seed42-r2
1910-    role: evidence
1911-    result: 0% SR (wrapper)
1912-  - exp_id: eval:pi05-official-lerobot-last-attempt
1913-    role: evidence
1914-    result: 100% SR (3/3, official eval)
1915-  depends_on:
1916-  - D099
1917-  - D098
1918:- id: D102
1919-  date: 2026-05-21 07:30 UTC
1920-  summary: 'D102: K=20 Sweep LOCKED — K=20 ≈ K=2，增加K不改善性能，强力支持Plan A "K=2足够"'
1921-  rationale: K=20 Object 18.8%±0.96% (n=4) vs K=2 18.3%±2.1%；K=20 Spatial 34.3%±0.6%
1922-    (n=3) vs K=2 35.0%±1.0%。两个benchmark上K=20均在K=2误差范围内。Diminishing returns确认：K=2已
…[truncated 3341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-21T21:25:50.515242+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/pi05_eval_commands.md",
  "offset": "80",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/pi05_eval_commands.md",
    "offset": "80",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-21T21:25:50.566551+00:00_

80	
81	### Run 3: object / seed 44 / bjb2-28827 / cuda:0
82	
83	```bash
84	source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
85	cd /root/acr-vla-conformal-refinement
86	CUDA_VISIBLE_DEVICES=0 TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py \
87	  --model pi05 \
88	  --mode acr_vla \
89	  --benchmark object \
90	  --seed 44 \
91	  --n_rollouts 20 \
92	  --K 10 \
93	  --obs_dim 2048 \
94	  --crm_checkpoint &lt;CRM_CHECKPOINT_OBJECT> \
95	  --max_correction_norm 0.2 \
96	  --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \
97	  --output_file logs/eval_object_acr_vla_pi05_seed44.json
98	```
99	
100	### Run 4: spatial / seed 42 / bjb2-28827 / cuda:1
101	
102	```bash
103	source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
104	cd /root/acr-vla-conformal-refinement
105	CUDA_VISIBLE_DEVICES=1 TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py \
106	  --model pi05 \
107	  --mode acr_vla \
108	  --benchmark spatial \
109	  --seed 42 \
110	  --n_rollouts 20 \
111	  --K 10 \
112	  --obs_dim 2048 \
113	  --crm_checkpoint &lt;CRM_CHECKPOINT_SPATIAL> \
114	  --max_correction_norm 0.2 \
115	  --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \
116	  --output_file logs/eval_spatial_acr_vla_pi05_seed42.json
117	```
118	
119	### Run 5: spatial / seed 43 / bjb1-18228 / cuda:0
120	
121	```bash
122	source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
123	cd /root/acr-vla-conformal-refinement
124	CUDA_VISIBLE_DEVICES=0 TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py \
125	  --model pi05 \
126	  --mode acr_vla \
127	  --benchmark spatial \
128	  --seed 43 \
129	  --n_rollouts 20 \
130	  --K 10 \
131	  --obs_dim 2048 \
132	  --crm_checkpoint &lt;CRM_CHECKPOINT_SPATIAL> \
133	  --max_correction_norm 0.2 \
134	  --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \
135	  --output_file logs/eval_spatial_acr_vla_pi05_seed43.json
136	```
137	
138	### Run 6: spatial / seed 44 / bjb1-18228 / cuda:1
139	
140	```bash
141	source /roo
…[truncated 860 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-vla-only-goal-seed47",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Assistant

_source line 133 · 2026-05-21T21:26:43.857326+00:00_

Now I have enough context to write the handoff.

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单必须从 `get_project_status` 的 `execution.gpu_ids` 获取，当前分配：bjb1-18228 cuda:0/1（CRM training）+ bjb1-32546 cuda:0-5 + bjb2-28827 cuda:0-5（eval）。不得使用白名单外 GPU
- π0.5 模型路径：`/root/autodl-tmp/models/pi05_libero_finetuned/`，必须传 `--obs_dim 2048`（默认 960 是 SmolVLA 的）
- π0.5 evaluate.py 的 `--mode acr_vla` 是 crm_perdof 别名（per-DOF CRM），不是 adaptive_conformal_crm。如果想要 Plan A conformal stopping 版本，需要改 mode + 加 `--conformal_threshold`
- SmolVLA 全部结果 LOCKED，不要重跑、不要修改论文中 SmolVLA 数据
- CoRL 2026 DDL **2026-05-29**，仅剩 **≤8 天**
- CRM checkpoint 分 benchmark 存储：object 和 spatial 各自有 crm_best.pt，不共享

### 2. 🖥️ 基础设施快照
- **bjb1-18228**（CRM training 服务器）：工作目录 `/root/acr-vla-conformal-refinement/`，Python `/root/miniconda3/bin/python`，conda base
  - Object CRM: PID 800111, cuda:0, output `/root/autodl-tmp/checkpoints/crm_pi05_full/object/`，epoch 7/50，best val_loss=0.005511
  - Spatial CRM: **FAILED**（`crm-train-pi05-spatial-full` 报 FileNotFoundError: No precomputed cache at spatial），需要诊断 spatial cache 路径问题后重启
  - 旧 precompute 进程 cuda:3 待清理
  - 数据缓存：`/root/autodl-tmp/crm_cache_pi05/{object,spatial}/`
- **bjb1-32546**（eval 服务器）：6 GPU，PyTorch 2.10.0+cu128，evaluate.py 33058 bytes 最新版，pi05 model 7.5GB OK
- **bjb2-28827**（eval 服务器）：6 GPU，同上环境就绪
- **bjb2-40593**：仅 1 GPU，之前跑 SmolVLA 系列，目前空闲
- W&B：项目内未见 wandb 配置引用
- 代码同步方式：rsync/scp（三台服务器均无有效 git remote）

### 3. 📊 当前状态
**刚完成**：π0.5 precompute merge + Object/Spatial CRM training 启动。Spatial CRM 失败（cache 路径问题），Object CRM 在跑（epoch 7/50，~5.5h 剩余）。

**Registry RUNNING**：
- `crm-train-pi05-object-full`：Object CRM training，bjb1-18228 cuda:0，PID 800111，69303 samples，epoch 7/50
- `crm-train-pi05-spatial-full`：标记 RUNNING 但实际 FAILED（FileNotFoundError），需要修复后重启

**PREPARING 积压**：~80+ eval 实验（大部分是旧的 SmolVLA 系列残留，可忽略）

**等待中**：
- Spatial CRM training 修复（cache 路径 `/root/autodl-tmp/crm_cache_pi05/spatial` 缺失或路径不对）
- Object CRM training 完成后 → 6 GPU eval 部署（命令已准备在 `pi05_eval_commands.md`）
- 14 GPU 空闲等 CRM 训练完成后部署 eval

### 4. 📋 待办
- **立即**：诊断 `crm-train-pi05-spatial-full` 失败原因（SSH 检查 `/root/autodl-tmp/crm_cache_pi05/spatial/` 是否存在及内容），修复后在 bjb1-18228 cuda:1 重启 spatial CRM training
- `crm-train-pi05-object-full` cron 回调（预计 ~5h 后）→ scp `crm_best.pt` 到 bjb1-32546 和 bjb2-28827 → 部署 3 个 Object eval（runs 1-3 in pi05_eval_commands.md，替换 `&lt;CRM_CHECKPOINT_OBJECT>` 为实际路径）
- Spatial CRM training 完成 → scp → 部署 3 个 Spatial eval（runs 4-6）
- 6 个 eval 全部完成 → 分析 π0.5 CRM vs VLA-only（81.5% Object / 84.2% Spatial）→ ceiling effect 分析 → 向 Director 汇报
- 汇报后 → Paper Agent 写入 π0.5 cross-VLA 结果 → final review → submission prep

### 5. 🎯 战略上下文
- **核心 story**（D065 reframe）：Learned correction 是有效机制，multi-sampling 是 enabling condition。论文标题"Correction Over Selection"。3 claims: C1=correction 是 active mechanism，C2=conditioning-magnitude interaction，C3=applicability boundaries
- **决策链关键节点**：D065（reframe 到 analysis paper）→ D092/D097（Adaptive K/Latency LOCKED）→ D102（K=20≈K=2 证实 Plan A）→ D103-D105（π0.5 baseline LOCKED）
- **π0.5 是 cross-VLA generalization 验证**，不是主实验。81-85% baseline 意味着 CRM 增益受 ceiling effect 限制。framing 已准备双路径：(1) 有提升→cross-VLA 泛化成功 (2) 持平→"no-harm on strong VLA + significant improvement on weak VLA"
- **易错点**：
  - Spatial CRM training 的 cache 路径问题——可能是 precompute 数据合并时 spatial 目录结构与 object 不同
  - `--mode acr_vla` vs `--mode adaptive_conformal_crm` 不等价——Plan A 需要 conformal stopping，可能需要后者
  - eval 命令中 `--max_correction_norm 0.2` 是 SmolVLA 时代参数，π0.5 action space 不同，可能需要重新校准
  - 代码通过 rsync 同步，改完代码必须手动 scp 到所有服务器
  - bjb1-18228 cuda:3 有旧进程待清理，不要在上面启动新实验
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-vla-only-goal-seed47"
}
```

</details>

---
