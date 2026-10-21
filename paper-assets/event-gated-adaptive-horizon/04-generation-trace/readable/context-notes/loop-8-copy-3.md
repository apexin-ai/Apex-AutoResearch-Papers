# reviewer / loop_8.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`f6f5e3a97c8ff009b540.json`](../../sessions/f6/f6f5e3a97c8ff009b540.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-15T10:07:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（`execution.gpu_ids`）。之前 009a 僵尸进程事件已验证这是硬约束。
- plan_017 命令**必须**用 `--gate_subsample_max_dt 1`（不是 0）才能实现 subsample OFF。代码逻辑：0 → fallback 到 effective_max_dt → subsample 仍然 ON。我已发三次 warning/critical，截至 handoff 时仍未见正确的 dry run 验证。
- plan_015 原始设计（`critic_dt_emb_detach`）是 **no-op**——imagination 阶段不更新 world model 参数，detach dt_emb 不改变任何被应用的梯度。已 redesign 为 plan_015B（`dt_emb_freeze: true`）。
- 审查"未改"类结论前必须双边核对（本地 workspace vs 远程服务器），之前有过误判。

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299(root)，工作目录 `/root/autodl-tmp/event-gated-adaptive-horizon`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/`
- 活跃进程：
  - 009d baseline s1：PID 122271，cuda:0，目标 500K steps
  - 009e (008d s1 复现)：PID 119108，cuda:1，目标 105K steps（当前 ~80K）
- 无 wandb 配置，指标从 `logdir/exp_*/metrics.jsonl` 读取
- ssh_read_only 不支持 `|`（管道）和 `sed`/`git`

### 3. 📊 当前状态
刚完成：plan_015 no-op 分析 + plan_015B/017 代码审查 + GPU 清理验证（dry run 进程已 kill）。

RUNNING 实验：
- **009d** (baseline s1, cuda:0) @ 64K/500K：eval 626@55K，健康上升
- **009e** (008d s1 复现, cuda:1) @ 80K/105K：eval 83@55K→250@65K→178@75K，**CIVO 模式确认中**（55K NVE≈4.13 精确复现 008d）

QUEUED：exp_010a_cheetah_baseline_s1（cuda:0，排 009d 之后）；exp_009f_008f_walker_s1

等待：009e 完成（预计 1-2h）→ 可用 cuda:1 跑 plan_015B 或 plan_017

### 4. 📋 待办
- 009e 完成 → 核实 85K-105K eval/value/entropy 轨迹，确认是否复现 008d Pathway A 崩溃（actor_entropy 持续负值 + value 爆炸）→ post 最终复现结论给 Director
- 009e 释放 cuda:1 → 验证 plan_017/015B 启动命令是否正确（**重点确认 plan_017 有 `--gate_subsample_max_dt 1`**）
- 009d 完成 → 核实 baseline s1 v/e 轨迹，与 001(s1)/009a(s2) 对比稳定性
- plan_015B/017 数据出来 → 构建 2×2 factorial 消融矩阵（trained/frozen dt_emb × subsample ON/OFF）
- 任何 paper 写作/figure 提交 → 按章节审查维度评审

### 5. 🎯 战略上下文
- **核心因果链**：trained dt_emb → CIVO → collapse。C6 PARTIALLY FALSIFIED (D040)：dt=1 imagination 不能阻止崩溃。
- **两条 collapse pathway**：Pathway A (008d s1, 经典 CIVO: value-driven, entropy↓) vs Pathway B (008e_v3 s2, policy destabilization: eval-driven, entropy↑)
- **NVE 1.5x 阈值**：88.9% accuracy (8/9), TPR=80%, TNR=100%。唯一 false negative 是 008e_v3_s1（trained dt_emb 但 nve=0.94，seed-dependent）
- **易错点**：
  1. `gate_subsample_max_dt=0` 直觉上像 "OFF" 但实际是 "fallback to effective_max_dt"（ON）。必须用 1。
  2. plan_015B 和 plan_017 的 dt_emb(1) 都是 untrained（随机 std=0.01），如果两者都不崩溃，存在 confound：可能是 untrained dt_emb(1)≈no dt_emb 而非各自假设成立。论文需注明。
  3. DreamerV3 imagination 中 `RequiresGrad(self)` 启用所有参数梯度，但 actor_opt/value_opt 只更新各自参数。dt_emb_freeze 必须在 `RequiresGrad` 之后再次冻结（models.py:230 已实现）。
  4. 009e 的 eval 在 55K 后振荡（83→250→178），不要把 65K 的 250 当"恢复"——需看 85-105K 趋势。
- **DDL**：CoRL 2026-05-29，剩余 14 天，672 GPU·h 充裕。


---
