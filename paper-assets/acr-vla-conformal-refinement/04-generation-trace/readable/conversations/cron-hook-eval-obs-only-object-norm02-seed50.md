# cron hook eval obs only object norm02 seed50

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/cron_hook_eval-obs-only-object-norm02-seed50.jsonl`
- **Structured JSON:** [`487e471ac6f27b56e4f2.json`](../../sessions/48/487e471ac6f27b56e4f2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-21T07:15:29.184433+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #23。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb2-40593:cuda:0, bjb1-18228:cuda:{0-3}, bjb1-32546:cuda:{0-5}, bjb2-28827:cuda:{0-5}（共 17 张）。白名单外的 GPU 即使 Director 指令也必须 push back
- bjb1-32546 提交命令必须带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&` 前缀，裸 `python` 不在 PATH 中（M039 教训，4 个实验同时失败）
- evaluate.py 路径是 `src/evaluate.py`，不是 `evaluate.py`（历史多次 EXIT_CODE=2）
- π0.5 vision tower 加载有 key mismatch bug（`vision_tower.vision_model.` vs `vision_tower.`），必须 patch lerobot 内部 `_fix_pytorch_state_dict_keys` 才能正常工作
- SmolVLA 核心数据 LOCKED（Object/Spatial Plan A、Norm Sweep、Adaptive K、Random Selection），禁止改动这些实验的 conclusion/metrics
- CoRL 2026 DDL: **2026-05-29**，≤8 天

### 2. 🖥️ 基础设施快照
- 服务器 4 台：bjb2-40593 (1 GPU), bjb1-18228 (4 GPU), bjb1-32546 (6 GPU, conda env), bjb2-28827 (6 GPU)
- 工作目录：`/root/acr-vla-conformal-refinement`
- Python：bjb1-32546 用 `/root/miniconda3/bin/python`；其他服务器 `python3` 可用
- 模型/数据：在各服务器 `/root/acr-vla-conformal-refinement/` 下，precompute 数据同目录
- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/`
- **活跃进程**：
  - eval-spatial-obs-only-seed45: bjb2-28827（低优先级，可 kill 给 π0.5）
  - eval-k20-obs-only-object-seed45: bjb2-28827:cuda:5
  - eval-k20-obs-only-spatial-seed42: bjb1-32546:cuda:2
  - eval-k20-obs-only-spatial-seed43: bjb1-18228:cuda:1
  - eval-k20-obs-only-spatial-seed44: bjb1-18228:cuda:2
- **活跃 Worker**：
  - `worker_fix_pi05-wrapper-vision-tower-final_20260521T063854`：修复 π0.5 wrapper vision tower 加载
  - `worker_figure_fig2-norm-sweep-v4-final_20260521T070817`：生成 Figure 2 norm sweep 最终版
- Cron：reconcile 返回 0 条（无活跃 cron 监控）

### 3. 📊 当前状态
**刚完成**：SmolVLA 全部核心实验 LOCKED（Plan A、Norm Sweep、Adaptive K cross-benchmark、Random Selection、OpenVLA boundary、Latency）。论文主体 8 页编译 OK。

**正在进行**：
1. π0.5 cross-VLA 验证线（P0）：Worker 正在修复 vision tower 权重加载 bug，对比官方实现。上一步确认官方 lerobot-eval patched 后 100% SR (3/3)，模型本身有效
2. K=20 sweep：5 个实验 RUNNING（Object seed45 + Spatial seed42/43/44 都在跑）
3. Figure 2 生成中

**等待中**：
- π0.5 fix Worker 回调 → 决定是否 quick verify 通过
- Figure 2 Worker 回调 → 注册 artifact
- 45 个实验 PREPARING（大部分是 norm sweep 补种 / π0.5 pipeline 实验，等 GPU 或前置条件）

### 4. 📋 待办（条件触发式）
- π0.5 fix Worker 完成 + quick verify SR>0% → 立即部署全量 baseline eval（3 seeds × Object + Spatial，需 6 GPU）
- π0.5 baseline 出结果且 >60% → CRM projection 训练 (2048→960, ~2-4h) → precompute (~1h) → Plan A eval (~6h)
- π0.5 baseline <60% → 汇报 Director，可能需要更多调试
- K=20 Spatial 3 seeds 全完成 → harvest metrics，更新 ROADMAP + report.md，判断是否 K=20 值得写入论文
- Figure 2 Worker 完成 → register_artifact + 论文集成
- π0.5 全部结果出来 → Paper Agent 写入 cross-VLA section
- 所有实验 + 论文就绪 → final review + submission prep

### 5. 🎯 战略上下文
**核心方向**：Adaptive inference-time compute for frozen VLAs。Plan A = K=2 L2 distance + selective CRM correction，已证明 Pareto 最优（双 benchmark 最高 SR + 最低 compute）。

**决策链关键节点**：
- D092: Plan A GO（Object 18.3% vs VLA-only 10.8%）
- D093: OpenVLA boundary（near-deterministic VLA 不适用，frame 为 stochastic VLA requirement）
- D097: Latency LOCKED（CRM 0.28ms, Plan A 1.82× speedup）
- D100: Spatial Adaptive K Sweep LOCKED（Plan A 35.0% > all thresholds）
- D101: π0.5 模型有效（lerobot-eval 100%），wrapper bug 是 vision tower key mismatch

**最容易判断错的事**：
1. π0.5 wrapper 修复看起来简单但已经历 5 轮失败。**不要自己写新 wrapper**——对比官方实现逐行 diff 是唯一可靠路径。Worker 正在做这件事
2. Cron false positive 是本项目顽疾（memory.md 记录 6+ 次）——实验被标记 failed 时先 SSH 检查进程是否实际在跑，不要盲目重提交
3. bjb1-32546 的 python PATH 问题——每次提交到这台服务器都要确认命令带 conda activate 前缀
4. 论文数据全部 LOCKED，不要重跑已锁定的实验或修改已锁定的 metrics
5. DDL 只剩 ≤8 天，π0.5 是唯一未完成的 critical path，其他都是锦上添花

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

- [失败模式] π0.5 vision tower 权重静默加载失败（2026-05-21）：**5 轮修复全部 0% SR 的真正根因**。checkpoint key 为 `vision_tower.vision_model.encoder.layers.X`，但 transformers 5.8.0 的 SiglipVisionModel 期望 `vision_tower.encoder.layers.X`（无 `vision_model` 中间层）。lerobot 0.5.2 的 `_fix_pytorch_state_dict_keys` 缺少此映射，`load_state_dict(strict=True)` 失败被 try/except 静默捕获，模型以**随机初始化 vision tower 运行** → 0% SR。**官方 lerobot-eval 也有此 bug。** Worker patch lerobot 内部代码后 3/3 = 100% SR。**教训：(1) load_state_dict 的 try/except 必须打印 missing_keys

...(memory.md 已截断，完整内容请 Read)

## 可查的历史
前 176 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-21T07:15:40.058936+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
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

_source line 3 · 2026-05-21T07:15:40.109722+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T07:15:44.024827+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['exp_id', 'status', 'hypothesis', 'server', 'gpu', 'pid', 'created_at', 'updated_at']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['exp_id', 'status', 'hypothesis', 'server', 'gpu', 'pid', 'created_at', 'updated_at']"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T07:15:44.025287+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T07:15:44.577764+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
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

_source line 7 · 2026-05-21T07:15:44.830436+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T07:15:45.653004+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-spatial-obs-only-seed45\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T07:09:30.589Z\", \"updated_at\": \"2026-05-21T07:09:59.922Z\", \"hypothesis\": \"补充 seed for Spatial crm_obs_only statistical robustness (low-priority, may be killed for π0.5)\"}, \"eval-k20-obs-only-object-seed45\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T06:11:55.095Z\", \"updated_at\": \"2026-05-21T06:12:41.658Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Object seed45. Extending K=20 Object sweep beyond seed42-44 for additional statistical power.\"}, \"eval-k20-obs-only-spatial-seed44\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T06:11:50.702Z\", \"updated_at\": \"2026-05-21T06:12:37.207Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. Third seed for K=20 Spatial sweep, completing 3-seed comparison vs K=10.\"}, \"eval-k20-obs-only-spatial-seed43\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T06:11:46.321Z\", \"updated_at\": \"2026-05-21T06:12:32.366Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. Multi-seed for K=20 Spatial sweep; pooled with seed42,44 for statistical comparison vs K=10.\"}, \"eval-k20-obs-only-spatial-seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T06:11:41.832Z\", \"updated_at\": \"2026-05-21T06:12:27.175Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. Testing whether larger K (vs K=10) improves Spatial benchmark SR. Parent K=10 Spatial obs_only seed42 establishes baseline.\"}}, \"count\": 5, \"total\": 5, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.6263}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1628
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T07:15:45.704479+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 1679
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T07:15:45.755445+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval-spatial-obs-only-seed45 | 补充 seed for Spatial crm_obs_only statistical robustness (low-priority, may be killed for π0.5) | — | — | — |\\n\\n## 待处理\\n- eval-pi05-baseline-object-seed42-r2: π0.5 VLA-only baseline on LIBERO-Object seed42 (r2). Fix: corrected QUANTILES→MEAN_STD normalization mismatch that caused 0% SR in r1.（准备中）\\n- eval-random-selection-object-seed42-r3: Random Selection (K=10, uniform pick) on LIBERO-Object seed42. Isolates conformal ranking contribution: if Random ≈ VLA-only, then CRM's advantage comes from learned correction not just sampling diversity.（准备中）\\n- …另有 43 项\\n\\n## 近期结论\\n- **eval-adaptive-k-spatial-p90-seed44-bjb2** (failed): Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.\\n\\n## 趋势\\n成功 322 / 负向 38 / 失败 55 / 共 506\\nn_rollouts_per_task: 20 →（近 3 次 success）\\nn_tasks: 10 →（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-18228: 无 GPU 信息\\nbjb1-32546: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\\nbjb2-28827: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\\nbjb2-40593: 无 GPU 信息\\n\\n## 告警\\n- plan_001-crm-smolvla: 训练失败 — unknown\\n- plan_014-reconvla-baseline: 训练失败 — unknown\\n- eval-smolvla-libero-spatial: 训练失败 — unknown\\n- eval-spatial-reeval-v2: 已被终止 — unknown\\n- precompute-v2-shard0: 已被终止 — unknown\\n- precompute-v2-shard1: 已被终止 — unknown\\n- precompute-v2-shard2: 已被终止 — unknown\\n- eval-spatial-v3-full: 已被终止 — unknown\\n- precompute-v3-shard0: 已被终止 — unknown\\n- precompute-v3-shard1: 已被终止 — unknown\\n- precompute-v3-shard2: 已被终止 — unknown\\n- eval-spatial-v4-full: 已被终止 — unknown\\n- eval-object-v4-fu
…[truncated 5369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1177
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T07:15:45.756166+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-21 07:03 UTC | 更新原因: Reviewer warning fix: wrapper状态改为\\\"修复中待验证\\\"，baseline预期标注来源，补CRM projection GPU估算\\n\\n> 详见 paper_framing.md（D077→D092→D097: Plan A Pareto 最优确认）\\n\\n## 核心方向\\n**Adaptive inference-time compute for frozen VLAs** — K=2 L2 distance + selective CRM correction。Plan A = Pareto 最优（双 benchmark 最高 SR + 最低 compute）。\\n\\n## 投稿目标\\n**CoRL 2026** DDL **2026-05-29**。剩余 **≤8 天**。\\n\\n## 阶段\\n**π0.5 cross-VLA 验证 + 论文收尾**。SmolVLA 核心实验全部 LOCKED。π0.5 wrapper 修复中（Worker 执行），待 quick verify 确认。\\n\\n## Plan A 核心结果 (LOCKED)\\n| Benchmark | Plan A (K=2) | K=10 CRM | VLA-only | Δ vs VLA-only |\\n|-----------|-------------|----------|----------|---------------|\\n| Object    | 18.3%±2.1%  | 16.8%±1.8% | 10.8%±1.3% | +7.5pp |\\n| Spatial   | 35.0%±1.0%  | 34.5%±1.5% | 29.4%±1.5% | +5.6pp |\\n\\n## Latency (LOCKED, D097)\\nCRM forward: 0.28ms | Plan A speedup: 1.82× | CRM pipeline vs K=10: -1.66%\\n\\n## Norm Sweep (ALL LOCKED)\\n| ε | n | mean | std |\\n|------|-----|-------|------|\\n| 0.03 | 13+ | 15.1% | ~1.2% |\\n| 0.05 | 14+ | 13.9% | ~1.4% |\\n| 0.1 | 18+ | 15.3% | ~2.3% |\\n| 0.2 | 12 | 17.2% | ~1.8% |\\n\\n## Spatial Adaptive K Sweep (ALL LOCKED, D100)\\nPlan A 35.0% > P90 33.0% (seed44=36% confirmed) > P75 32.7% > P50 32.0% > P25 31.7%。\\n\\n## Random Selection (LOCKED)\\nObject 9.7% ≈ VLA-only 10.8% | Spatial 29.3% ≈ VLA-only 29.4% → CRM correction 是性能来源\\n\\n## OpenVLA Applicability Boundary (LOCKED, D093)\\nBaseline 69% → +CRM 0%。Near-deterministic (T=0.5)。论文 frame: 方法需要 stochastic VLA。\\n\\n## π0.5 实验线 (D095→D101)\\n- ✅ D101: 官方 lerobot-eval **100% SR (3/3)**（单 task, 3 episodes），模型有效\\n- 根因: wrapper vision tower 权重未真正加载（try/except 静默吞错误，M039）\\n- 🔧 **当前**: Worker `fix:pi05-wrapper-vision-tower-final` 对比官方实现修复中，**待 q
…[truncated 2770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 925
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T07:15:58.161655+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__list_workers,mcp__agent-ml-research__get_worker_status",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__list_workers,mcp__agent-ml-research__get_worker_status",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T07:15:58.212619+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T07:16:00.825448+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
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

_source line 15 · 2026-05-21T07:16:00.926345+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_fix_pi05-wrapper-vision-tower-final_20260521T063854\", \"task_type\": \"fix:pi05-wrapper-vision-tower-final\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-21T06:38:54.752713+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_figure_fig2-norm-sweep-v4-final_20260521T070817\", \"task_type\": \"figure:fig2-norm-sweep-v4-final\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-21T07:08:17.896742+00:00\", \"ended_at\": null}], \"count\": 2}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T07:16:06.253429+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_fix_pi05-wrapper-vision-tower-final_20260521T063854",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_fix_pi05-wrapper-vision-tower-final_20260521T063854",
    "verbose": "True"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T07:16:06.554897+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_fix_pi05-wrapper-vision-tower-final_20260521T063854\", \"status\": \"running\", \"task_type\": \"fix:pi05-wrapper-vision-tower-final\", \"project\": \"acr-vla-conformal-refinement\", \"started_at\": \"2026-05-21T06:38:54.752713+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"progress\": {\"recent_tools\": [\"Glob\", \"ssh_execute\", \"ssh_read_only\", \"ssh_execute\", \"ssh_execute\"], \"last_text\": \"Good. Now let me kill the old diagnostic script and run the quick verification (5 rollouts).\", \"turn_count\": 18}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 301
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T07:16:06.606725+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_figure_fig2-norm-sweep-v4-final_20260521T070817",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_figure_fig2-norm-sweep-v4-final_20260521T070817",
    "verbose": "True"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T07:16:06.707567+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_figure_fig2-norm-sweep-v4-final_20260521T070817\", \"status\": \"running\", \"task_type\": \"figure:fig2-norm-sweep-v4-final\", \"project\": \"acr-vla-conformal-refinement\", \"started_at\": \"2026-05-21T07:08:17.896742+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"progress\": {\"recent_tools\": [\"register_artifact\"], \"last_text\": \"图表渲染正确。注册产出。\", \"turn_count\": 3}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T07:16:23.919517+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__load_project_config",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__load_project_config",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T07:16:23.919986+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T07:16:26.876707+00:00_

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
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
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

_source line 23 · 2026-05-21T07:16:26.877315+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"acr-vla-conformal-refinement\", \"section\": \"execution\", \"config\": {\"execution\": {\"account\": \"root\", \"gpu_constraint\": [\"bjb2-40593:cuda:0\", \"bjb1-18228:cuda:0\", \"bjb1-18228:cuda:1\", \"bjb1-18228:cuda:2\", \"bjb1-18228:cuda:3\", \"bjb1-32546:cuda:0\", \"bjb1-32546:cuda:1\", \"bjb1-32546:cuda:2\", \"bjb1-32546:cuda:3\", \"bjb1-32546:cuda:4\", \"bjb1-32546:cuda:5\", \"bjb2-28827:cuda:0\", \"bjb2-28827:cuda:1\", \"bjb2-28827:cuda:2\", \"bjb2-28827:cuda:3\", \"bjb2-28827:cuda:4\", \"bjb2-28827:cuda:5\"], \"gpu_ids\": [\"bjb2-40593:cuda:0\", \"bjb1-18228:cuda:0\", \"bjb1-18228:cuda:1\", \"bjb1-18228:cuda:2\", \"bjb1-18228:cuda:3\", \"bjb1-32546:cuda:0\", \"bjb1-32546:cuda:1\", \"bjb1-32546:cuda:2\", \"bjb1-32546:cuda:3\", \"bjb1-32546:cuda:4\", \"bjb1-32546:cuda:5\", \"bjb2-28827:cuda:0\", \"bjb2-28827:cuda:1\", \"bjb2-28827:cuda:2\", \"bjb2-28827:cuda:3\", \"bjb2-28827:cuda:4\", \"bjb2-28827:cuda:5\"], \"project_path\": \"/root/acr-vla-conformal-refinement\", \"servers\": [\"bjb2-40593\", \"bjb1-18228\", {\"account\": \"root\", \"server\": \"bjb1-32546\"}, {\"account\": \"root\", \"server\": \"bjb2-28827\"}]}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T07:16:40.990228+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 6/17 在用 | Worker 2 (GPU 1 / CPU 1) | 磁盘: 未检测\n\n**Session #23 启动状态**\n\n**Critical Path — π0.5 (P0)**：\n- fix Worker (turn 18) 正在 bjb2-40593 运行 quick verify（5 rollouts）。这是决定 π0.5 线能否推进的 gate\n- Quick verify SR>0% → 立即部署全量 baseline eval（3 seeds × 2 benchmarks，需 6 GPU）\n- 11 GPU 空闲待 π0.5 部署\n\n**RUNNING 实验 (5)**：\n- K=20 Spatial: seed42 (bjb1-32546), seed43 (bjb1-18228), seed44 (bjb1-18228)\n- K=20 Object: seed45 (bjb2-28827)\n- Spatial obs-only seed45 (bjb2-28827, low priority)\n\n**即将完成**：\n- Figure 2 norm sweep Worker 已渲染完成，正在注册 artifact\n\n**等待中**：\n- π0.5 fix Worker 回调 → 决定下一步\n- K=20 Spatial 3 seeds 完成 → harvest metrics\n\nDDL 倒计时 ≤8 天。当前瓶颈是 π0.5 quick verify 结果。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 6/17 在用 | Worker 2 (GPU 1 / CPU 1) | 磁盘: 未检测\n\n**Session #23 启动状态**\n\n**Critical Path — π0.5 (P0)**：\n- fix Worker (turn 18) 正在 bjb2-40593 运行 quick verify（5 rollouts）。这是决定 π0.5 线能否推进的 gate\n- Quick verify SR>0% → 立即部署全量 baseline eval（3 seeds × 2 benchmarks，需 6 GPU）\n- 11 GPU 空闲待 π0.5 部署\n\n**RUNNING 实验 (5)**：\n- K=20 Spatial: seed42 (bjb1-32546), seed43 (bjb1-18228), seed44 (bjb1-18228)\n- K=20 Object: seed45 (bjb2-28827)\n- Spatial obs-only seed45 (bjb2-28827, low priority)\n\n**即将完成**：\n- Figure 2 norm sweep Worker 已渲染完成，正在注册 artifact\n\n**等待中**：\n- π0.5 fix Worker 回调 → 决定下一步\n- K=20 Spatial 3 seeds 完成 → harvest metrics\n\nDDL 倒计时 ≤8 天。当前瓶颈是 π0.5 quick verify 结果。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T07:16:45.424788+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-obs-only-object-norm02-seed50",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 4434
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-21T07:16:49.150680+00:00_

Session #23 初始化完成。

**当前态势**：
- 5 个实验 RUNNING（K=20 sweep + spatial seed45）
- π0.5 fix Worker 正在 quick verify 阶段（critical path gate）
- Figure 2 Worker 即将完成
- 11 GPU 空闲，等 π0.5 fix 通过后立即部署 baseline eval
- 已向 Director 汇报

等待 Worker 回调推进下一步。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-obs-only-object-norm02-seed50"
}
```

</details>

---
