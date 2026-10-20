# reviewer / loop_7.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`2a4bff71caecd873d323.json`](../../sessions/2a/2a4bff71caecd873d323.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-15T04:14:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（bjb1-45299 只有 2 张 RTX PRO 6000 Blackwell 98GB）。两张都归本项目，无跨项目冲突
- exp_008e_v3_subsample_on_dt1_h15 和 exp_008e_v3_walker_s1 **都是 seed=1**，不是独立 seed。writing_plan 中 "s0 + s1 nearly identical" 是同 seed 重复，**不能作为 multi-seed 证据**。C6 目前只有 1 个独立 seed，s2（seed=2，RUNNING）是第一个新 seed
- 论文中引用 lu2018nondelusional 时必须区分：Lu 的 delusional bias 源于 policy class constraint，本项目的 delusional critic 源于 temporal conditioning corruption，机制不同

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299(root)，工作目录 `/root/autodl-tmp/event-gated-adaptive-horizon`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/`
- 无 W&B 配置（不检查 W&B）
- 活跃进程：
  - PID 142513 cuda:0 — exp_009a_baseline_walker_s2（~336K/500K, seed 2）
  - PID 43442 cuda:1 — exp_008e_v3_walker_s2（刚启动, seed 2, 105K steps）
  - PID 908751 cuda:0 — dryrun_cheetah_baseline（CPU 模式残留，552MB CUDA context，无害但可清理）
  - PID 123058 — checkpoint_monitor.py（后台守护）

### 3. 📊 当前状态
**刚完成**：审查了 ~10 个 worker 结果，包括 008e_v3_s1 最终结果（DONE, eval=869.9@105K, C6 PASS）、registry 僵尸清理（6 个 PREPARING→全部 DONE）、文献扫描（72 篇，无 novelty 威胁）、writing_plan 审查（发现 C6 seed 误计，已 CRITICAL 上报 Director）。

**Registry RUNNING**：
- exp_009a_baseline_walker_s2：cuda:0, ~67% done, eval ~948, 收敛稳定
- exp_008e_v3_walker_s2：cuda:1, 刚启动（00:46 UTC），seed 2，~4.5h ETA

**QUEUED 排期**（cuda:1 完成 s2 后）：009e → 009f → 009c(200K) → plan_060

**等待中**：
- Director 对 Framing 调整提案（C2 collapse stochastic → Option A "Reliable Pathological Overestimation"）的决策
- 008e_v3_s2 完成后需立即审查：这是 C6 的第一个独立第二 seed

### 4. 📋 待办（条件触发式）
- 008e_v3_s2 完成 → 立即审查 final eval + v/e ratio + 与 s1 对比（C6 multi-seed 验证的关键数据点）
- 009a_baseline_s2 完成 → 核实 eval 是否接近 s0 的 915.67，更新 baseline reference
- Director 转发 Framing 提案审查 → Read `negative-framing-review.skill.md`，按四维度审
- Director 转发章节写作审查 → 按 §5 模板评分，特别注意 C6 seed 描述是否已修正
- 009e（008d seed 1 repeat）完成 → 审查 collapse 是否复现（当前 collapse probability 1/2）
- Cheetah Run 实验启动 → 核实 GPU 分配 + 验证 dry-run 结论

### 5. 🎯 战略上下文
**核心结论链**：trained dt_embedding + dt>1 imagination → nve>1.5x（4/4 separating power）→ stochastic collapse（1/2 seeds）。Mitigation: dt=1 imagination（008e_v3, 95% baseline）。这是 diagnostic paper，不是 method paper。

**决策链关键节点**：D032（collapse stochastic）→ Framing 调整待决 → D033（008e_v3 dt_emb 实际是 trained，critical variable 是 imagination dt 不是 embedding 训练状态）

**最容易判断错的事**：
1. **C6 seed 数**：写作计划说有 s0+s1 两个 seed，实际都是 seed=1。只有 s2（RUNNING）才是新 seed。已上报但写作 worker 可能未修正——审查论文时必须核对
2. **GPU 利用率低≠异常**：DreamerV3 + DMC 小模型在 98GB 卡上只用 ~4GB、util 0-20% 是正常的，不要误判为 stuck
3. **tail_training_logs 有 buffering 延迟**：tmux stdout log 可能滞后数小时，监控进度应读 `logdir/metrics.jsonl`
4. **008f 不是推荐方案**：008f 去掉 dt_embedding 避免崩塌但 reward 退化 75x。推荐方案是 008e_v3（保留 trained dt_emb + dt=1 imagination）


---
