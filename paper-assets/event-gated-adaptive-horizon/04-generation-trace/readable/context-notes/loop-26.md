# agent / loop_26.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_26.md`
- **Structured JSON:** [`8582bac88ddf11d0644a.json`](../../sessions/85/8582bac88ddf11d0644a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 26
reason: idle_timeout
updated: '2026-05-28T06:46:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-51268 cuda:0 和 cuda:1，严禁使用其他 GPU
- bjb1-45299 宕机不可用，不要尝试连接
- Cheetah 008a 系列历史上多次 killed/failed（exp_095/096/098/099/102/103），当前命名为 exp_cheetah_008a_s0/s1，不要用旧命名重新创建
- Walker no_dt_emb s0 实际运行名为 exp_walker_008f_s0（不是 exp_walker_no_dt_emb_s0，后者已 killed）
- NVE CIVO 检测阈值已从 1.5 上调至 2.0（D165），分析时用 τ=2.0
- 数据锁定截止：5/28 12:00 UTC（北京时间 20:00），过期不可再跑新实验

### 2. 🖥️ 基础设施快照
- 服务器：westd-51268，2× RTX PRO 6000 Blackwell 96GB
- 工作目录：/root/autodl-tmp/event-gated-adaptive-horizon
- Python：/root/miniconda3/bin/python（conda base 环境，不是 venv）
- 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- EGL 变量：MUJOCO_GL=egl, PYOPENGL_PLATFORM=egl, MUJOCO_EGL_DEVICE_ID={gpu_index}
- W&B：已配置，实验可查
- 活跃进程：
  - exp_cheetah_008a_s0: PID 637656, cuda:1, tmux 管理, cron 监控中
  - exp_walker_008f_s0: PID 637987, cuda:0, tmux 管理, cron 监控中

### 3. 📊 当前状态
收到 exp_cheetah_008a_s1 延迟 CRON 回调，确认该实验已由上个 session 完成分析（DONE/success, NVE=0.584, C3 confirmed）。已向 Director 汇报当前状态。

Registry 运行中：
- exp_cheetah_008a_s0 (RUNNING, cuda:1) — C3 cross-env seed 0，提交 14:21 UTC，ETA ~17:13 UTC
- exp_walker_008f_s0 (RUNNING, cuda:0) — C2 causal control seed 0，提交 14:23 UTC，ETA ~17:15 UTC

等待中：两个实验的 cron 完成回调。无 Worker 运行。无 Director 决策待处理。

实验统计：100 success / 43 negative / 2 running，共 ~200 个

### 4. 📋 待办
- exp_walker_008f_s0 cron 回调 → spawn worker 分析 logs+W&B → NVE<2.0 则 success(C2 confirmed) → update registry → 汇报 Director
- exp_cheetah_008a_s0 cron 回调 → spawn worker 分析 → NVE<2.0 则 success(C3 s0 confirmed) → update registry → 汇报 Director
- 两个实验都完成 → 汇报 Director 全部 multi-seed 数据就绪 → 请求启动 Paper Agent 整合最终结果
- Paper 整合完成 → 数据锁定声明
- 任一实验 NVE≥2.0 或 failed → 诊断原因，距离截止还有 ~18h 可以重跑一次

### 5. 🎯 战略上下文
- 核心发现：DreamerV3 的 trained dt_embedding 驱动 CIVO（Conditioning-Induced Value Overestimation），是 multi-joint locomotion 特异性现象。Frozen/removed dt_emb 可稳健阻止
- C2（causal control）：Walker 已有 s1 success (exp_walker_no_dt_emb_s1)，等 s0 (exp_walker_008f_s0)
- C3（cross-env）：Walker 008a 3-seed 闭合 (s0=778,s1=751,s3=856)，Cheetah 008a s1 success (NVE=0.584)，等 s0
- C6 已 CONFIRMED（4/4 deterministic mitigation）
- Hopper 结论：gate mechanism failure，不是 dt_emb-driven CIVO（D162）
- 投稿目标 CoRL 2026，论文 7 页 + appendix 已基本就绪
- 易错点：exp_walker_008f_s0 和 exp_walker_no_dt_emb_s0 是不同 registry 条目但同一类实验（后者 killed），不要混淆。分析时 baseline 对比用各环境各自的 baseline，不要跨环境比绝对值


---
