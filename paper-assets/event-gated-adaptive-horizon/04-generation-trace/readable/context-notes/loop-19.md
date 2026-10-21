# agent / loop_19.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_19.md`
- **Structured JSON:** [`9cab4c500e7441a88d8b.json`](../../sessions/9c/9cab4c500e7441a88d8b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: idle_timeout
updated: '2026-05-17T11:44:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 cuda:0 + cuda:1（bjb1-45299），绝不碰其他 GPU
- PickCube 实验用 `--configs defaults maniskill`（不是 `maniskill_state`），configs.yaml 中已有 `maniskill` section
- MUJOCO_EGL_DEVICE_ID 必须与 cuda:N 匹配，否则 eval 死锁
- submit 命令必须包含 `unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- Detector backtest 必须用 raw V/E ratio（不是 NVE），严格逐条对照 Algorithm 1 每个条件——之前 Worker 用 NVE 近似导致错误 TP 结论（D083 撤回）
- Curriculum phase 参数以 env steps 计，action_repeat=2 时 logger steps = 2× env steps。105K step 实验 phase1 不能 ≥ 52500

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299（2×RTX PRO 6000 96GB）
- 工作目录：`/root/autodl-tmp/event-gated-adaptive-horizon/`
- 日志目录：`~/runs/event-gated-adaptive-horizon/`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 代码 commit：`3328f53cb32cda27e85b099d560256aeb01db998`
- 活跃进程：
  - exp_019b_pickcube_civo_trigger: PID 649577, cuda:0, cron 监控中
  - exp_022b_no_curriculum: PID 670554, cuda:1, cron 监控中
- W&B：logdir 本地 `./logdir/{exp_id}`
- 无运行中 Worker

### 3. 📊 当前状态
两个实验在跑，零个 Worker 在跑。

| exp_id | GPU | 进度 | 关键指标 |
|--------|-----|------|---------|
| exp_019b_pickcube_civo_trigger | cuda:0 | 132.5K/200K (67.8%) | NVE peak 3.78×@52.5K → 0.08×@132.5K, eval=26.9, transient CIVO (自纠正) |
| exp_022b_no_curriculum | cuda:1 | 15K/105K (14.3%) | eval=167.3@15K, gate_dt_1_frac=0.1, gate_dt_mean=4.6, gate actively exploring |

**上一个 session 完成的关键工作：**
- D083: 撤回 PickCube detector TP 结论 → 实际是 TN（detector 正确未触发，PickCube 是 transient CIVO 不 collapse）
- D081: 发现 exp_022 curriculum 锁住了 gate 整个训练过程，启动 022b（phase1=0, phase2=0）rerun
- D079: Detector 在 3 个 non-CIVO 实验中 FP，选方案 C frame 为 "value-divergence detector"
- D078: C1 从 "causes collapse" reframe 为 "universally degrades"
- D077: seed=3 (008d_s3) 确认自纠正模式
- CIVO online detector 设计完成，retrospective validation 部分完成

### 4. 📋 待办（条件触发式）
- exp_019b cron 回调（DONE）→ 分析最终 eval/NVE pattern → 更新 registry → 确认 transient CIVO 结论 → 不需要额外 PickCube 实验 → cuda:0 释放给 exp_021_full_sgs_cheetah_s1
- exp_022b cron 回调（DONE）→ 分析 gate_dt_1_frac 和 NVE：若 gate 学到 non-trivial temporal abstraction (dt_1_frac < 0.8) 且 NVE < 1.5× → 验证 "frozen dt_emb + learned gate" 安全组合 → 更新 C2 claim 支撑
- exp_022b gate_dt_1_frac 收敛到 ~1.0 → gate 在 frozen dt_emb 下不能学到有意义模式 → negative，需分析 gate 为什么需要 trained dt_emb 的梯度信号
- exp_019b + 022b 都完成 → 两个 GPU 释放 → 提交 exp_021_full_sgs_cheetah_s1 (cuda:0) + CIVO detector prospective validation (cuda:1)
- CIVO detector retrospective validation 完成 → 派 Worker 写 detector 代码（dreamer.py ~30-50 行）→ prospective test
- 所有实验数据齐 → 派 Worker 写 detector section + figure → submit_paper_to_review

### 5. 🎯 战略上下文
**项目核心：** CoRL 2026 投稿（DDL 2026-05-29，剩 12 天）。论文是 CIVO 诊断论文 + 在线检测工具。

**因果链（已验证）：** Trained dt_emb → obs decoder gradient → RSSM fidelity gap → reward bias → critic overestimation → collapse（或 self-correction，取决于环境）

**C1 reframe 关键：** 不是所有 seed 都 collapse（seed=3 自纠正），所以 C1 从 "causes collapse" 改为 "universally degrades"。这影响全文叙事。

**Detector FP 问题：** 3 个 non-CIVO 实验触发了 detector（FP）。D079 决定 frame 为 "value-divergence detector"（更宽泛的适用范围），而非仅 CIVO detector。这影响 paper framing 和 detector section 写法。

**易错点：**
1. PickCube 的 transient CIVO 不等于 Walker 的 persistent CIVO。不要把 019b 的 NVE peak 当作 CIVO collapse 证据——它自纠正了
2. Detector backtest 容易犯方法论错误（已踩过一次坑）——必须用 raw V/E ratio，检查 acceleration + prev_delta + eval decline 三个条件
3. exp_022b 的 gate 正在积极探索（dt_mean=4.6, dt_1_frac=0.1），看起来有前途，但要等到 40K+ 才能判断是否收敛到 meaningful pattern
4. SGS claim（C5）只有 1/2 collapse 率，是 "informative" 不是 "solid"，论文中不能 overclaim
5. Bootstrap CI 需要 n=3 seeds，008d_s3 的数据是关键——确认它的最终状态后立即更新 Table 1


---
