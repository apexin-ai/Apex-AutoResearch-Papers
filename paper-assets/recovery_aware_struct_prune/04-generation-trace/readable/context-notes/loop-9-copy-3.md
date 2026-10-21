# reviewer / loop_9.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`309d95ff55f5e9b32bdf.json`](../../sessions/30/309d95ff55f5e9b32bdf.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-16T02:08:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- westb-23072 GPU 白名单：cuda:0, cuda:1（C001）
- westd-11672 GPU 白名单：cuda:0, cuda:1（C003）
- grpo_unpruned_v2 的 registry 状态被错误标记为 DONE/failed，但进程 PID 75381 仍在 westd GPU 1 活跃训练（step 25+/100）。**不要基于 registry 状态判定该实验已结束**。
- `grpo_unpruned_baseline`（W&B: e49c42ha）实验无效（D040/D041：缺少 SFT 步骤），**禁止在论文或分析中引用其 "collapse at step 80" 数据点**。只有 grpo_unpruned_v2 才是有效 unpruned 对照。
- `sft_recovery.py` 的 `--gpu` 参数会覆盖外层 `CUDA_VISIBLE_DEVICES`（第 20-23 行），启动时必须确保两者一致，否则进程会跑到错误 GPU 上。

### 2. 🖥️ 基础设施快照
- **westb-23072**：`/root/recovery_aware_struct_prune`，conda base（`/root/miniconda3/bin/python`）
  - 模型/checkpoint 在 `/root/autodl-tmp/recovery_aware_struct_prune/`
  - GPU 0: grpo_stage2_rasp_20_v9（PID 566666，step 10/30，COLLAPSING）
  - GPU 1: eval_grpo_rasp_v9_step5（PID 572129，107/1319，acc@100=68%）
- **westd-11672**：同路径结构
  - GPU 0: eval_sft_unpruned_full（PID 74134，485/1319，acc@450=81.11%）
  - GPU 1: grpo_unpruned_v2（PID 75381，step 25+/100，registry 误标 FAILED）
- W&B entity/project 未配置在 project config 中，`fetch_wandb_metrics` 不可用
- W&B run IDs：RASP v9=mrikafz3, Standard v8=q34vz8j2, Unpruned v2=nhsx0bt2

### 3. 📊 当前状态
刚完成两件事：
1. 对 `grpo_unpruned_v2` failure 通知的审查——确认是监控误判，进程仍活跃。已 post 给 Director 要求修正 registry。
2. 对 `artifacts/grpo_collapse_dynamics_analysis.md` 的审查——发现 CRITICAL：三方 collapse 对比引用了无效的 unpruned baseline 数据。已 post 给 Director。

**Registry RUNNING**: eval_sft_unpruned_full, grpo_stage2_rasp_20_v9
**Registry PREPARING**: eval_grpo_rasp_v9_step5（实际已在跑）
**实际仍在跑但 registry 误标 FAILED**: grpo_unpruned_v2

### 4. 📋 待办
- grpo_unpruned_v2 完成（ETA ~35min from handoff）→ 审查 collapse 时间点，这是更新三方 collapse ordering 的唯一有效 unpruned 数据。如果 collapse 在 step <40，"冗余负相关" 结论不成立。
- eval_sft_unpruned_full 完成 → 记录最终 N=1319 准确率，更新三方 SFT 对比表（当前 RASP 61.49%, Standard 59.29%, Unpruned ?%）
- eval_grpo_rasp_v9_step5 完成 → 如果 N=1319 acc > 61.49%（RASP SFT baseline），则 GRPO 在 collapse 前确实有恢复效果——论文关键数据点
- grpo_stage2_rasp_20_v9 完成（step 30）→ 确认 step 20/30 是否仍在 collapse。step 10 已确认 collapse（frac_zero_std=0.875）
- Standard v8 step 90 "recovery" 声明 → 需验证 completions_00090.parquet 输出质量，调查 crash 原因

### 5. 🎯 战略上下文
**核心决策链**：D014(MVP pass) → D027(post-prune claim 崩塌) → D033(GRPO v8 为 pivot 判据) → D043(三模型全 collapse) → D044(narrative pivot: GRPO fails on pruned models)

**当前论文 story**：从 "RASP enables better recovery" 已 pivot 到 "GRPO fails on all pruned models, collapse dynamics as diagnostic"。collapse speed ordering 是主要卖点。

**最易判断错的事**：
1. **不要引用 "Unpruned collapse at step 80"**——那是无效实验。等 grpo_unpruned_v2 结果。
2. **SFT 层面 RASP vs Standard 无统计差异**（61.49% vs 59.29%, p=0.248）。不要基于 2.2pp 差异做 claim。
3. **Standard v8 "recovery at step 90" 未经充分验证**。analysis artifact 中的 TCR（Transient Collapse with Recovery）分类可能过度拟合 n=1 观察。
4. **RASP "N=4 collapse runs" 说法有误导**——v2/v5/v8/v9 参数不同，严格同条件只有 v8/v9。
5. **eval_grpo_rasp_v9_step5 的 N=100 acc=68% 极不稳定**（N=50 时仅 58%），不要过早引用。


---
