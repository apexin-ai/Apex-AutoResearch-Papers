# agent / loop_18.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_18.md`
- **Structured JSON:** [`22f56b75cbbb135647b1.json`](../../sessions/22/22f56b75cbbb135647b1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: idle_timeout
updated: '2026-05-17T07:22:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 bjb1-45299 的 cuda:0 和 cuda:1（gpu_ids=[0,1]）
- submit_training_job 命令必须 `unset CUDA_VISIBLE_DEVICES` 开头，用 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` 激活环境
- MUJOCO_GL=egl + MUJOCO_EGL_DEVICE_ID 必须匹配实际 GPU 编号
- seed=3 实验（008d_civo_trigger_s3）的分析 Worker 正在跑，不要重复 spawn
- CoRL DDL 2026-05-29，剩 12 天，禁止 fallback 思维

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299，工作目录 `/root/autodl-tmp/event-gated-adaptive-horizon`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 代码：DreamerV3 修改版（dreamer.py + 自定义 gate 逻辑）
- logdir：`/root/autodl-tmp/event-gated-adaptive-horizon/logdir/`
- 训练日志：`~/runs/event-gated-adaptive-horizon/`
- 活跃进程：exp_019a_v2_pickcube_baseline (PID 629444, cuda:1, ~65K/200K steps)
- Cron 监控：exp_019a_v2_pickcube_baseline 活跃（reconcile 确认 running）
- Worker 活跃：`worker_analysis_exp_008d_civo_trigger_s3_20260517T031958`（分析中）

### 3. 📊 当前状态
刚收到 exp_008d_civo_trigger_s3 (seed=3, cuda:0) 完成回调，已 spawn Worker 分析 W&B + 日志。Worker 需要判定 conclusion（CIVO 是否 systematic across seeds）。

Registry 状态：
- exp_008d_civo_trigger_s3: ANALYZING（Worker 正在分析）
- exp_019a_v2_pickcube_baseline: RUNNING (cuda:1, PID 629444, ~65K/200K)
- exp_021_full_sgs_cheetah_s1: QUEUED（等 GPU）
- exp_019b_pickcube_civo_trigger: QUEUED（等 019a 完成后用 cuda:1）

等待中：
- Worker `worker_analysis_exp_008d_civo_trigger_s3_20260517T031958` 回调 → 更新 registry + 汇报 Director
- 019a 完成后 → 启动 019b (PickCube CIVO trigger)
- cuda:0 现在空闲（008d_s3 已完成）→ 可跑 exp_021 (Cheetah Full-SGS)

### 4. 📋 待办
- Worker 分析回调到达 → 根据 conclusion 更新 registry(DONE) + report.md + 汇报 Director；如果 success 则更新 bootstrap CI (n=3) 并推进 CIVO detector prospective validation
- cuda:0 空闲 → 008d_s3 分析确认后，提交 exp_021_full_sgs_cheetah_s1（已 QUEUED）
- 019a_v2 完成 → 分析 PickCube baseline 稳定性 → 提交 019b CIVO trigger
- CIVO detector retrospective validation 完成 → 代码实现 + prospective test（用 seed=3 数据）
- 所有实验数据就绪 → 论文集成 detector section + 更新 Table 1 bootstrap CI + submit_paper_to_review

### 5. 🎯 战略上下文
- 核心因果链：Trained dt_emb → obs decoder gradient → RSSM fidelity gap → reward bias → critic overestimation → collapse
- 论文定位已升级：诊断论文 + 实用 CIVO 在线检测器（C7 新 contribution，Director D076 决策）
- seed 状态：seed=0 success, seed=2 negative（009b），seed=3 待定。如果 s3=success → 2/3 seeds confirm CIVO（systematic claim 可用 bootstrap CI）；如果 s3=negative → 只有 1/3，claim 需要降级
- 易错：exp_009b_008d_walker_s2 (seed=2) 是 negative——不要把它当 success 引用。之前有 seed bug（sample_episodes 硬编码 seed=0，D075 确认）已修复，s3 是修复后的验证
- SGS (Selective Gradient Stopping) claim 已降级为 "informative"（C5），018_s2 确认 Full-SGS 未阻止 CIVO onset（D074）
- 93% gradient claim 已被否定（D073），实际 obs=16-22%，不要在论文中使用旧数据


---
