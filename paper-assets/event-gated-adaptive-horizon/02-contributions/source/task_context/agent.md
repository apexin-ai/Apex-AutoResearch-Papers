---
loop: 27
reason: idle_timeout
updated: '2026-05-29T08:20:37+00:00'
---

### 1. 🔴 硬约束 / 红线
- **westd-51268 只有 1 块 GPU（cuda:0）**。config 写了 gpu_ids=[cuda:0, cuda:1] 但 cuda:1 物理不存在（torch.cuda.device_count()=1）。不要尝试在 cuda:1 上提交任何实验。
- **MUJOCO_EGL_DEVICE_ID 必须 = CUDA 设备号且物理存在**。exp_quadruped_baseline_s0 就是因为 EGL_DEVICE_ID=1 崩的。
- **D171 数据锁定**：Walker/Cheetah 所有已有实验数据、数值、统计、表格、图表冻结，禁止修改。新环境（Quadruped/Hopper）不受限。
- **Humanoid 已排除（D177/D178）**：baseline NVE=12.97×，不能用于 CIVO 隔离实验。不要再提交 Humanoid 相关实验。
- 所有实验必须设 `export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0`。

### 2. 🖥️ 基础设施快照
- **服务器**: westd-51268，1× RTX PRO 6000 (cuda:0)
- **工作目录**: `/root/autodl-tmp/event-gated-adaptive-horizon`
- **Python**: `/root/miniconda3/bin/python`，激活方式 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **日志目录**: `~/runs/event-gated-adaptive-horizon/`
- **logdir**: `/root/autodl-tmp/event-gated-adaptive-horizon/logdir/`
- **活跃进程**: exp_quadruped_baseline_s0_r2, PID=42263, tmux session, cuda:0
- **活跃 Cron**: 监控 exp_quadruped_baseline_s0_r2（reconcile 确认 still running）
- **活跃 Worker**: worker_diagnose_quadruped-progress-check（正在检查 quadruped 训练进度）

### 3. 📊 当前状态
- **刚做完**: D179 contingency plan 制定（Quadruped baseline NVE@115K=2.3×，不乐观），Humanoid 排除决策（D177/D178），Table error bars 通过 Reviewer 验证。
- **正在跑**: exp_quadruped_baseline_s0_r2 RUNNING on cuda:0，~115K/200K steps，NVE@115K=2.3×（6/10 checkpoint >2.0×），~60% 概率 baseline unhealthy。
- **队列**: exp_quadruped_008d_s0 QUEUED（等 baseline 结果判定 healthy 才提交）；exp_walker_no_dt_emb_s0 需 re-run（C2 causal control，原 run 被 killed），排在 008d 之后。
- **等待中**: worker_diagnose_quadruped-progress-check 回调；quadruped_baseline cron 完成回调（~85K steps 剩余，预计 ~1-1.5h）。
- **无 PENDING 实验**（walker_no_dt_emb_s0 标记在 ROADMAP 但 registry 无 PENDING 记录，需重新创建提交）。

### 4. 📋 待办（条件触发式）
- **quadruped_baseline cron 回调到达** → 分析最终 NVE@200K：
  - NVE < 2.0 → baseline healthy → 立即提交 exp_quadruped_008d_s0（命令已在 registry spec 里）
  - NVE 1.8-2.2 borderline → 汇报 Director 决策
  - NVE clearly > 2.0 → Quadruped 排除 → 汇报 Director → 启动 Hopper 路径（先 baseline，再 008d）
- **worker_diagnose_quadruped-progress-check 回调** → 读取进度分析结果，更新 report.md
- **Quadruped 排除确认后** → 创建 exp_hopper_baseline_s0 + exp_hopper_008d_s0 实验计划 → 提交 Director 审批
- **cuda:0 空出后** → 按串行链推进：008d（或 Hopper baseline）→ walker_no_dt_emb_s0 re-run

### 5. 🎯 战略上下文
- **投稿目标**: ICLR 2027（~10月 DDL），4 个月窗口。从 CoRL fallback 过来（D176）。
- **核心 claim**: DreamerV3 中 trained dt_embedding 驱动 CIVO（Conditioning-Induced Value Overestimation），是 multi-joint locomotion 特异性现象。Frozen/removed dt_emb 可阻止。
- **数据状态**: Walker/Cheetah 已锁定证明 CIVO。需第三环境扩展 scope。Humanoid 已排除。Quadruped 是当前尝试但前景不佳。
- **关键风险**: Quadruped baseline 大概率 unhealthy → 需要 Hopper 作为第三数据点。Hopper 结果决定论文 claim 强度：CIVO + multi-joint 成立（6→6.5+/10）vs 仅 Walker/Cheetah 两环境（停留 6/10）。
- **易错点**:
  - 不要把 config 里的 cuda:1 当真——物理不存在，提交就报错
  - walker_no_dt_emb_s0 在 ROADMAP 标记 PENDING 但 registry 里没有 PENDING 记录——需要重新走创建+提交流程
  - Quadruped/Hopper 实验都需要 EGL 环境变量，忘了就 segfault
  - D171 数据锁定是硬约束——新环境实验不能回头改 Walker/Cheetah 的已有数据
- **论文**: 42 页（8 页主文），ICLR reframe 完成，Reviewer 当前 6/10。实验统计 211 个（103 success / 44 negative / 22 failed / 41 killed）。
