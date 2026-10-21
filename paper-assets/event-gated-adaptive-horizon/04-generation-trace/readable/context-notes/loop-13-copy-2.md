# agent / loop_13.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_13.md`
- **Structured JSON:** [`5d3205bdda3fe6db10e0.json`](../../sessions/5d/5d3205bdda3fe6db10e0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: idle_timeout
updated: '2026-05-15T19:51:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单严格 cuda:0 + cuda:1（bjb1-45299），禁止用其他设备号
- 所有训练命令必须带 `LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl`，否则 dm_control 渲染 segfault
- cuda:1 上的命令还需 `MUJOCO_EGL_DEVICE_ID=1`
- submit_training_job 隔离 CUDA_VISIBLE_DEVICES，脚本内永远 `--device cuda:0`（映射到物理分配卡）
- ManiSkill3 与 CUDA_VISIBLE_DEVICES 不兼容（SAPIEN segfault），需特殊处理
- exp_017 已取消（D044 确认与 008a 冗余），不要重新提交
- logdir 在 `/root/autodl-tmp/event-gated-adaptive-horizon/logdir/`，不在 `/root/runs/`（后者只有 tmux log）

### 2. 🖥️ 基础设施快照
- **服务器**: bjb1-45299, 2×RTX PRO 6000
- **工作目录**: `/root/autodl-tmp/event-gated-adaptive-horizon/`
- **Python**: `/root/miniconda3/bin/python`，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型/数据**: dm_control 内置环境，无外部模型/数据集依赖
- **W&B**: 项目内配置，metrics 通过 `fetch_wandb_metrics` 查询
- **活跃进程**:
  - `exp_009d_baseline_walker_s0`: PID 149708, cuda:0, ~138K/500K steps, **有 cron 监控**
  - `exp_016e_sgs_walker_s1`: PID 526939, cuda:1, 105K steps, tmux session, **⚠️ 无 cron 注册！必须立即注册**

### 3. 📊 当前状态
**刚完成**: D054 AUROC 重算定稿（task_b2 AUROC=0.933）、论文压缩至 ≤8 页主体、016d 失败分析（SummaryWriter.add_video 死锁）并启动 016e（第五次重试，Logger.video → no-op 修复）。

**RUNNING**:
- `exp_016e_sgs_walker_s1` (cuda:1) — **本项目最关键实验**。SGS (reward_dt_emb_detach=True) 验证能否同时避免 CIVO 和 gradient starvation。105K steps，预计 ~4-5h。logdir 沿用 `exp_016d_sgs_walker_s1` 路径。
- `exp_009d_baseline_walker_s0` (cuda:0) — baseline 第三 seed，138K/500K，趋势健康（495@138K），预计还需 ~13h。

**QUEUED**: `exp_010a_cheetah_baseline_s1` 排在 009d 之后用 cuda:0。

**⚠️ 关键遗留**: 016e 没有 cron 监控。reconcile_crons 只发现 009d 的 cron。下一个 session **第一件事**是给 016e 注册 cron（`register_cron`），否则完成/失败不会回调。

**无运行中 Worker**。

### 4. 📋 待办（条件触发式）
- **立即** → 给 exp_016e_sgs_walker_s1 注册 cron 监控（PID 526939, bjb1-45299）
- 016e cron 回调 (success) → spawn Worker 分析 SGS metrics（NVE、eval_return、actor_loss vs 008d/015b 对比）→ 汇报 Director → 决定 SGS 是否进论文 method section → 更新 paper_framing.md
- 016e cron 回调 (failed) → 读日志诊断根因 → 若仍是 video/rendering 问题则进一步 patch 重试；若代码逻辑问题则走 red-section framing
- 016e 结果 positive (NVE<1.5x + eval 不崩) → SGS 成为 paper method contribution，启动 Cheetah SGS 实验做跨环境验证
- 016e 结果 negative (仍崩) → 产出 Framing 调整提案（diagnostic-only paper vs SGS 变体），**禁止默默跑下一个**
- 009d 完成 (~500K) → 记录最终 metrics → cuda:0 启动 exp_010a_cheetah_baseline_s1
- 009d + 010a 完成 → Cheetah collapse config 实验（跨环境验证 C1/C2）
- 5/17-20 窗口 → ManiSkill3 适配（注意 CUDA_VISIBLE_DEVICES 不兼容问题，需特殊启动方式）
- fig3/fig6 需更新（含 AUROC=0.933 修正），可在等实验时并行派 Worker

### 5. 🎯 战略上下文
**核心结论链**:
- D049: Trained dt_emb 是 sustained CIVO (NVE>1.5x) 的必要条件（2×2 矩阵闭合）
- D053/D054: NVE 诊断 7/8 accuracy, AUROC=0.933, 1 FP (008e_v3_s2 = imagination-reality divergence, 非 CIVO)
- 三种崩溃机制已识别：CIVO (008d/006)、Gradient Starvation (015b)、Imagination-Reality Divergence (008e_v3_s2)

**016e 是 fork point**: SGS 成功 → 论文 = diagnostic + method (更强)；SGS 失败 → 论文 = diagnostic-only (仍可投但 contribution 弱一档)。不要在 016e 出结果前动 method section。

**易踩的坑**:
1. 016e 的 logdir 是 `exp_016d_sgs_walker_s1`（不是 016e），因为沿用了上次的 logdir 路径
2. 008d 和 009e 是同一 seed=1 的两次运行，collapse rate = 1/2 independent seeds，不是 2/3
3. 008e_v3_s2 的 NVE>1.5x 是 FP（non-CIVO），不要把它当 CIVO 案例引用
4. exp_017 已被 D044 取消（与 008a 冗余），不要重新排队
5. CoRL DDL = 2026-05-29，仅剩 14 天。关键路径：016e 结果 → framing 决策 → Cheetah 跨环境 → ManiSkill3 → 定稿


---
