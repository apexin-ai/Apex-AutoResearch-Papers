# agent / loop_20.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_20.md`
- **Structured JSON:** [`5fdda63309e979f7e1e6.json`](../../sessions/5f/5fdda63309e979f7e1e6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: idle_timeout
updated: '2026-05-17T18:04:59+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-45299 的 cuda:0 和 cuda:1，**严禁用其他卡**
- MUJOCO_EGL_DEVICE_ID 必须与物理 GPU 编号一致（cuda:0→EGL=0, cuda:1→EGL=1），否则 eval 死锁
- gate_curriculum_phase1/phase2 单位是 env steps，action_repeat=2 时 50000 env steps = 100K logger steps。提交前必须算清有效 schedule
- submit_training_job 命令必须自带环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && ...`
- detector backtest 必须用 raw V/E ratio（不是 NVE），严格逐条对照 Algorithm 1（之前 Worker 因用 NVE 近似得出错误 TP 结论）

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299，账号 root
- 工作目录：`/root/autodl-tmp/event-gated-adaptive-horizon/`
- 日志目录：`~/runs/event-gated-adaptive-horizon/`
- Python：`/root/miniconda3/bin/python`，conda env = base
- Checkpoint 目录：`/root/autodl-tmp/event-gated-adaptive-horizon/logdir/{exp_id}/`
- 磁盘：/usr 5% used (399G/439G 可用)，充裕
- 活跃进程：exp_019b_pickcube_civo_trigger (PID 649577, cuda:0, tmux managed, cron 监控中)
- W&B：部分实验有 W&B，部分没有（exp_022b 无 wandb logging）

### 3. 📊 当前状态
**刚完成**：exp_022b_no_curriculum 分析 → DONE(negative)。Frozen random dt_emb 阻止 CIVO (ve_ratio 峰值 0.218) 但 gate 近均匀分布 (entropy_ratio=0.912)，eval=300.7 (77% baseline)。已更新 registry + memory.md + 汇报 Director。

**RUNNING**：
- exp_019b_pickcube_civo_trigger (cuda:0) — PickCube CIVO trigger 验证，有 cron 监控

**QUEUED**：
- exp_021_full_sgs_cheetah_s1 — P0，Full-SGS Cheetah Run，等 Director 分配 cuda:1

**PREPARING**：
- exp_023a_cheetah_baseline_s0, exp_023b_cheetah_baseline_s1 — Cheetah vanilla baselines

**等待中**：
- Worker `worker_code_exp_021_prep_20260517T140031` 正在准备 exp_021 启动脚本（SSH dry-run 中，turn 15）
- 等 Director 回复：cuda:1 分配给 exp_021 的审批
- exp_019b cron 回调（仍在跑）

### 4. 📋 待办
- Director 批准 cuda:1 → exp_021 → 用 prep Worker 产出的脚本 submit_on_allocated，MUJOCO_EGL_DEVICE_ID=1
- exp_021 prep Worker 完成 → 读取产出，确认脚本可用，等 GPU 分配
- exp_019b cron 回调（完成/失败）→ 按 on-experiment-done 分析 PickCube CIVO trigger 结果，对比 019a baseline
- exp_019b 完成后 cuda:0 释放 → 可排 exp_023a 或其他 P0 实验
- CIVO detector 待推进：retrospective validation 大部分完成 (AUROC=0.926, 12 实验全集)，待做代码实现 (dreamer.py ~30-50 行) + prospective validation

### 5. 🎯 战略上下文
- **目标**：CoRL 2026，DDL 2026-05-29（剩 12 天）
- **论文定位**：CIVO 诊断论文 + 在线检测工具（D076 升级）
- **核心因果链**：Trained dt_emb → obs decoder gradient → RSSM fidelity gap → reward bias → critic overestimation → collapse
- **C1 (trained dt_emb causes CIVO)**：⚠️ n=2 确认，seed=3 (008d_s3) 数据已有但需更新 bootstrap CI
- **C2 (dt_emb necessary)**：✅ Solid（008f remove + 022b freeze 双重确认）
- **C7 (online detector)**：🔨 开发中，AUROC=0.926 retrospective，需代码实现 + prospective test
- **SGS intervention**：collapse_rate=0.5 (018v2 pass, 018_s2 fail)，不可靠，论文定位为 "informative" 而非 "reliable fix"
- **PickCube**：transient CIVO（NVE spike then self-correct），与 Walker 的 persistent collapse 不同。Detector 正确不触发 (TN)
- **易错点**：
  - 不要把 NVE 和 raw V/E ratio 混用（detector 用后者）
  - exp_022b eval=300.7 是 77% baseline（不是 33%，auto-decision D085 用了旧数据）
  - Full-SGS Cheetah (exp_021) 是跨环境验证 SGS 一致性，不是测 SGS 可靠性（已知不可靠）
  - PickCube 019b detector 结果是 TN（D083 已撤回 D082 的 TP 结论）


---
