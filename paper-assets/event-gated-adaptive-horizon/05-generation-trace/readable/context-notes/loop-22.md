# agent / loop_22.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_22.md`
- **Structured JSON:** [`94e3afdb85b6c25eb25d.json`](../../sessions/94/94e3afdb85b6c25eb25d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 22
reason: idle_timeout
updated: '2026-05-21T05:53:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-45299:cuda:0, bjb1-45299:cuda:1, bjb1-40020:cuda:0, bjb1-40020:cuda:1。不得使用白名单外 GPU
- bjb1-45299 使用 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6（libstdc++ 兼容问题），bjb1-40020 不需要
- MUJOCO_EGL_DEVICE_ID 必须与物理 GPU 编号对应（cuda:0→EGL=0, cuda:1→EGL=1），否则 eval 死锁
- 清理 tmux session 必须用 `tmux kill-session -t &lt;name>`，严禁 kill PID（5/19 事故：kill tmux server 导致 3 个实验全灭）
- 禁止在 105K steps 内对实验做成功/失败定性判断——中间报告只做描述性汇报

### 2. 🖥️ 基础设施快照
- **bjb1-45299**（2×RTX PRO 6000）：工作目录 /root/autodl-tmp/event-gated-adaptive-horizon/，Python /root/miniconda3/bin/python，conda activate base，日志 ~/runs/event-gated-adaptive-horizon/
- **bjb1-40020**（2×RTX 4090）：同上路径结构，conda activate base
- **环境激活**：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（两台服务器相同）
- **W&B**：已配置，cron 自动同步指标
- **活跃进程**：
  - exp_031b (bjb1-45299:cuda:0) PID=968495, tmux session, cron 监控中
  - exp_034 (bjb1-45299:cuda:1) PID=993925, tmux session, cron 监控中
  - exp_032 (bjb1-40020:cuda:1) PID=124556, tmux session, cron 监控中
  - exp_033 (bjb1-40020:cuda:0) PID=151860, tmux session, cron 监控中
- 磁盘充裕：bjb1-45299 ~399GB 可用，bjb1-40020 ~389GB 可用

### 3. 📊 当前状态
**刚完成**：exp_032b_dual_critic_walker_s1 — CIVO prevented（NVE<0.5 全程，eval 551.8 peak）。这是项目突破性结果。D120 发现 v1≈v2（critic 差异<1%，ρ>0.998），CIVO 抑制机制不是传统 pessimism。D121 基于此部署了 Cheetah dual-critic + wide-critic ablation。

**4 个实验 RUNNING（全部 4 GPU 满载）**：
| exp_id | server:gpu | 估计进度 | 核心问题 |
|--------|-----------|---------|---------|
| exp_032 dual-critic Walker s0 | 40020:1 | ~60% | 第二个 seed 验证 CIVO 抑制 |
| exp_033 wide-critic Walker | 40020:0 | ~15% | 参数量 vs min 效应 ablation |
| exp_031b PickCube σ=0.5 | 45299:0 | ~60% | TCN 跨域 dose-response |
| exp_034 dual-critic Cheetah | 45299:1 | 刚启动 | 跨环境泛化验证 |

**等待中**：
- Worker worker_analysis_exp_032b... 正在运行（分析 exp_032b 结果）
- 4 个 cron 监控活跃，回调会自动触发

### 4. 📋 待办（条件触发式）
- exp_032 s0 cron 回调到达 → 分析结果：NVE<1.5 + eval≥baseline → 两 seed 确认 dual-critic CIVO 抑制；否则 → 需第三 seed
- exp_033 wide-critic 完成 → **关键分叉**：CIVO 被抑制 → 参数量/容量效应（CIVO=critic underfitting）；CIVO 未被抑制 → min 操作有隐含正则化（CIVO=临界相变）。结果直接决定论文机制解释
- exp_034 Cheetah dual-critic 完成 → CIVO 被抑制 → 跨环境泛化确认，强化 Intervention Hierarchy narrative；失败 → Walker-specific，需更多证据
- exp_031b PickCube σ=0.5 完成 → 预期 negative（Walker σ=0.5 已是过量），主要收集 dose-response 数据点
- worker_analysis_exp_032b 完成 → 读取分析结果，更新 report.md，向 Director 汇报
- **5/25 数据锁定**：所有实验必须在此前完成，剩余 4 天

### 5. 🎯 战略上下文
- **目标**：CoRL 2026，DDL 2026-05-29（8 天）。5/25 数据锁定
- **论文方向（D113 确认）**：Scenario B — Intervention Hierarchy 论文。核心贡献：三层干预框架（representation-level TCN → architecture-level dual-critic → planning-level MPC）+ CIVO 因果诊断 + 架构边界发现
- **D120-121 突破**：dual-critic 抑制 CIVO 但机制不是传统 pessimism（v1≈v2），这是新发现。论文 narrative 需围绕此调整
- **TCN 结果**：Walker σ=0.2 2/4 seeds 有效（高方差），Cheetah 全 σ 失败，PickCube σ=0.2 失败 → TCN 是 partial intervention，支持 hierarchy narrative
- **评分轨迹**：Round 1 实际 4/10 → 目标 6.5+ （dual-critic 结果 + 机制发现）
- **易错点**：
  1. 不要把 GC4-par 和 GC4-seq 直接对比
  2. v1≈v2 是关键发现——不要用传统 pessimism 解释 dual-critic 效果
  3. wide-critic 实验结果决定机制解释，在结果出来前不要在论文中锁定机制 narrative
  4. TCN dose-response 窗口很窄（~σ=0.2），禁止过度泛化为"TCN works"
- **决策链**：D113（Scenario B 确认）→ D118（dual-critic 批准）→ D120（v1≈v2 发现 → wide-critic ablation）→ D121（exp_032b CIVO prevented → Cheetah 部署）


---
