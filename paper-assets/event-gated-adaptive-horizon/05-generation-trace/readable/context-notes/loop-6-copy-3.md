# reviewer / loop_6.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`f40a9dfdcda867b48236.json`](../../sessions/f4/f40a9dfdcda867b48236.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: idle_timeout
updated: '2026-05-14T22:01:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（bjb1-45299 上只有 2 张 A800-96GB）
- exp_008d 的实际 seed 是 `--seed 1`，**不是 seed 0**。memory.md "009c 教训" section 仍写 "seed 0 (008f)"，009b registry `metrics.verdict` 仍写 "seed 0's sustained overestimation"——均未修正。**信 command，不信 prose**。
- 不存在 seed 0 的实验——所有实验用 `--seed 1` 或 `--seed 2`。
- 008e_v3 的 dt_embedding 是 **trained**（D033 已确认），Table 1 和 paper_framing.md 中 "untrained" 标注需修正。C6 保护机制是 imagination dt=1，不是 embedding 训练状态。
- exp_006/007 的 subsample 实际是 ON（D016 代码审计确认）。experimental_setup.md Table 1 已修正。

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299 (root)，工作目录 `/root/autodl-tmp/event-gated-adaptive-horizon`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/`
- 无 wandb（本项目不检查 W&B）
- GPU UUID：cuda:0 = GPU-f7b10021-42fd-...，cuda:1 = GPU-7b497967-3578-...
- 活跃进程：
  - exp_009a_baseline_walker_s2：PID 142508（子 142513），cuda:0，~256K/500K，ETA ~9h
  - exp_008e_v3_walker_s1：PID 898127（子 898132），cuda:1，~25K/105K，ETA ~3h

### 3. 📊 当前状态
Loop #6 完成 1 次代码审计 + GPU 合规 + 覆盖度审查 + 进度监控，提交 1 次 reviewer_post_to_director：

| 审查对象 | 结论 | 关键发现 |
|---------|------|---------|
| 008e_v3 dt_emb 代码审计 | WARNING | Table 1 标 "untrained" 但代码确认 trained → D033 已创建 |
| GPU 合规 | PASS | PID→UUID 映射正确 |
| experimental_setup.md 复查 | PASS | 之前 3 个 critical 全部修复 |
| 008e_v3_s1@25K | INFO | eval=155.69, value=26.19, nve=1.93x — 与原始 008e_v3 完全一致（同 seed 确定性复现）|

cuda:1 排期：008e_v3_s1 → 008e_v3_s2 → 009e → 009f → 009c(200K) → plan_060

### 4. 📋 待办
- **008e_v3_s1 到达 35K** → 首个可靠 nve 数据点。原始 008e_v3@35K nve=0.94x。若一致 → 复现确认；若 >1.5x → CRITICAL（C6 story 动摇）
- **008e_v3_s1 完成（105K）** → 最终审查：eval_return 应 ≈869.9，nve 应 <1.0x。这是 crown jewel C6 验证。
- **009a_baseline_s2 完成** → 验证 eval ≈970.4（s1 水平）。用双 seed 均值更新 nve 分母。
- **memory.md / 009b verdict 的 "seed 0" 修正** → 下次审查时再确认是否已修正
- **任何新实验启动** → GPU 边界合规检查（PID→GPU UUID 映射）
- **Cheetah/Cartpole 实验开始** → 检查命令模板是否正确、环境变量是否设置

### 5. 🎯 战略上下文
- **项目本质**：诊断分析论文，目标 CoRL 2026（DDL 2026-05-29，剩 15 天）
- **核心 story（D031 + D033）**：trained dt_embedding → pathological nve>1.5x（4/4 separating power）→ collapse 是 stochastic（1/2 seeds）→ **dt=1 imagination** 是实用 mitigation（008e_v3 = 95% baseline，dt_emb 是 trained 的但不影响）
- **D033 修正**：008e_v3 的 dt_emb 是 trained → C6 保护变量是 imagination dt=1，不是 embedding 训练状态。narrative 更干净：不需要改模型架构，只需改 imagination 策略。
- **最容易判断错的事**：
  1. 008d seed 编号——command 是 seed 1，prose 多处写 seed 0。**信 command**。
  2. 008e_v3 的 dt_emb 状态——曾标 untrained，D033 确认 trained。
  3. GPU 利用率 nvidia-smi 瞬时 0%（eval 阶段正常），用进程 uptime + metrics.jsonl step 交叉确认。
  4. 008e_v3_s1 是同 seed（seed 1）复现，不是新 seed。真正的多 seed 验证是 s2。


---
