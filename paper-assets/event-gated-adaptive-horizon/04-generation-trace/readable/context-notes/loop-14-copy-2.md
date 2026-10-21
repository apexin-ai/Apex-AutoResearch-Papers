# agent / loop_14.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_14.md`
- **Structured JSON:** [`db703b897ee8339ef4a9.json`](../../sessions/db/db703b897ee8339ef4a9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: idle_timeout
updated: '2026-05-15T23:06:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 **仅 cuda:0 和 cuda:1**（bjb1-45299），config 里 gpu_ids=["cuda:0", "cuda:1"]
- 训练命令**必须**带 `LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl`，否则 dm_control 渲染崩溃
- submit_training_job 设 CUDA_VISIBLE_DEVICES 隔离，脚本内只能用 `--device cuda:0`（逻辑设备 0 = 分配的物理卡）
- ManiSkill3 与 CUDA_VISIBLE_DEVICES 不兼容（SAPIEN segfault），需特殊处理
- 016e 已分析完毕（NVE=6.59x CIVO 确认），但 registry 状态仍为 PREPARING——**不要重新提交它**，它是历史记录
- 008e_v3_s2 是 **non-CIVO**（imagination-reality divergence），NVE 高是被动的，不要把它算作 CIVO 正例

### 2. 🖥️ 基础设施快照
- **服务器**: bjb1-45299，2×RTX PRO 6000
- **工作目录**: `/root/autodl-tmp/event-gated-adaptive-horizon`
- **Python**: `/root/miniconda3/bin/python`（conda base，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **日志目录**: `~/runs/event-gated-adaptive-horizon/` (tmux logs); logdir 在工作目录下 `logdir/&lt;exp_id>/`
- **代码 commit**: `dccb867841046bf6dc7dcc654ea71f99e1181828`
- **活跃进程**:
  - exp_009d_baseline_walker_s0: PID 149708 (cron reconcile), cuda:0, tmux session, ~228K/500K (~10h remaining)
  - exp_010a_cheetah_baseline_s1: PID 536890, cuda:1, tmux session, 刚启动 (512K steps, ~19h)
- **Cron**: 2 个活跃（009d + 010a），reconcile 确认均 still running

### 3. 📊 当前状态
**刚做完**: D054 AUROC 重算定稿 + 016e SGS 深度分析 + 论文压缩至 ≤8 页主体 + D059/D060 排期决策。

**Registry 活跃实验**:
- `exp_009d_baseline_walker_s0` — RUNNING cuda:0, Walker Walk baseline seed 0, ~228K/500K, eval_return 692@228K 健康上升
- `exp_010a_cheetah_baseline_s1` — RUNNING cuda:1, Cheetah Run baseline seed 1, 刚提交

**等待中**:
- 009d cron 回调（~10h 后完成）
- 010a cron 回调（~19h 后完成）
- 无活跃 Worker（池=0）
- 016e 状态为 PREPARING 但已完成分析，不需要再跑

**趋势**: 成功 7 / 负向 13 / 失败 6 / 共 36

### 4. 📋 待办（条件触发式）
- **009d cron 回调（~10h）** → spawn worker 提取最终 metrics + v/e 校准数据 → 更新 registry DONE → 汇报 Director → cuda:0 空出排下一个实验（ROADMAP 排 Cheetah baseline s0 或 ManiSkill3 适配）
- **010a cron 回调（~19h）** → spawn worker 提取 Cheetah baseline metrics → 更新 registry → cuda:1 空出排 Cheetah collapse config（dt=2 subsample ON）
- **009d + 010a 都完成后** → 两张卡空出，进入 Cheetah 跨环境验证阶段（ROADMAP 5/17-20: Cheetah baseline s0 + Cheetah collapse config）
- **Cheetah 跨环境结果出来** → 验证 C1/C2 跨环境泛化 → 如果 Cheetah 也出现 CIVO → 强化论文 claim；如果不出现 → framing 需要 scope 到 Walker Walk
- **fig3/fig6 需要更新**（含 AUROC=0.933）→ 可在等待训练期间派 Worker 做
- **Appendix task_b1 sensitivity analysis 表格** → 同上，可并行

### 5. 🎯 战略上下文
**项目核心结论**: Trained dt_embedding 是 sustained CIVO (NVE>1.5x) 的必要条件。2×2 消融矩阵已闭合（D049）。SGS reward-only 失败（016e），证明根因在 value dynamics（critic pathway）而非 reward gradient。NVE 诊断力 87.5% accuracy, AUROC=0.933。

**论文定位**: D059 选了 Framing B = diagnostic paper + SGS negative 作为机制深化证据（不是 method paper）。目标 CoRL 2026，DDL 5/29，还剩 14 天。

**关键决策链**: D049（矩阵闭合）→ D051-D054（NVE 诊断框架四轮修正）→ D057-D058（016e SGS 失败分析）→ D059（Framing B 确定）→ D060（GPU 排期）

**最容易判断错的事**:
1. **016e 的 PREPARING 状态会误导你以为它还没跑**——它已经跑完并分析过了（NVE=6.59x），只是 registry 状态没推到 DONE。不要重新提交。
2. **008e_v3_s2 的高 NVE (3.78x) 容易被误判为 CIVO**——它是 non-CIVO（imagination-reality divergence），是 NVE 框架的唯一 FP。论文已加 limitation 讨论。
3. **ManiSkill3 实验在 ROADMAP 5/21-23 排期**，但 SAPIEN 与 CUDA_VISIBLE_DEVICES 不兼容。需要特殊处理（不走 submit_training_job 的标准 GPU 隔离），提前规划。
4. **当前 Worker 池=0**，两个实验都在跑不需要 Worker 干预，但图表更新和 appendix 表格可以现在并行铺——不要等训练完了才开始。


---
