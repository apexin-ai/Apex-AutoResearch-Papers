# agent / loop_1.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`4f9b5a03935819304069.json`](../../sessions/4f/4f9b5a03935819304069.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: idle_timeout
updated: '2026-05-21T14:44:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-10894 cuda:0-3（4× RTX PRO 6000 96GB），不得用其他服务器/GPU
- conda 环境名：`occsafe`（不是 base，不是 venv）
- 训练命令必须带 `WANDB_MODE=disabled MUJOCO_GL=egl`，否则 W&B 连接失败 / MuJoCo 渲染崩溃
- 数据盘：大文件只放 `/root/autodl-tmp/`，根分区空间有限
- mvp_vanilla_s2 仍在 QUEUED——修复失败原因前不要提交，否则白白浪费 GPU 时间重复同一个错误

### 2. 🖥️ 基础设施快照
- 服务器：westd-10894，account: root
- 工作目录：`/root/occsafe_vla/openvla-oft`
- Python/conda：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe`
- 训练脚本：`/root/occsafe_vla/openvla-oft/vla-scripts/finetune.py`
- 数据：`/root/autodl-tmp/data/modified_libero_rlds/libero_spatial_no_noops/`（432 demos）
- Checkpoint 目录：`/root/autodl-tmp/checkpoints/vanilla_s{0,1,2}`
- 日志：`~/runs/occsafe_vla/mvp_vanilla_s{0,1}.log`
- W&B：disabled（MVP 阶段不用）
- 活跃进程：无。4 张 GPU 全部空闲，无 tmux/cron 活跃任务

### 3. 📊 当前状态
**刚做完**：收到 mvp_vanilla_s0 失败 cron 回调，reconcile_crons 发现 mvp_vanilla_s1 也已失败。已派诊断 Worker（`worker_diagnose_mvp_vanilla_failed_20260520T072518`）SSH 读日志分析根因，已向 Director 汇报两实验均失败。

**Registry**：
- `mvp_vanilla_s0`: DONE(failed) — EXIT_CODE=1，训练 ~8min 崩溃
- `mvp_vanilla_s1`: DONE(failed) — EXIT_CODE=1，同样崩溃
- `mvp_vanilla_s2`: QUEUED — 未提交，等根因修复

**等待中**：
- 诊断 Worker 回调（读日志 + 分析错误 + 给修复建议）——这是最高优先级，回来后立即修复并重跑
- Director 已收到失败汇报，可能有进一步指示

### 4. 📋 待办
- 诊断 Worker 回调到达 → 读诊断报告，确定根因 → 派修复 Worker 改代码/环境 → 重新提交 s0/s1/s2 三个 seed
- 如果根因是环境问题（缺包/版本不兼容）→ 派 Worker 修环境后 dry-run 验证再批量提交
- 如果根因是代码 bug → 派 Worker 修代码 + 本地 dry-run（跑几个 step 确认不崩）→ 提交全部 3 seeds
- 如果根因是 OOM → 降 batch_size 到 4 或开 gradient checkpointing，需要向 Director 确认超参变更
- 三个 seed 修复重跑后 → 进入 MVP 条件 B（+占据辅助头），需要先实现 BEV occupancy aux head

### 5. 🎯 战略上下文
- **项目核心**：首个研究 VLA 空间表征与安全机制交互的工作，3×2 factorial + OccSafe-VLA
- **当前阶段**：MVP 验证，条件 A（vanilla baseline）都还没跑通，是第一步
- **目标会议**：AAAI 2027（Abstract Jul 21，Paper Jul 28，~10 周）
- **决策链**：D001 MVP 方案确定 → D002 ≥3 seeds + paired t-test → D003 单 suite spatial + 50K steps → D004 确认 AAAI 2027
- **易错点**：两个实验参数完全相同（仅 seed 不同）同时崩溃，100% 是系统性问题。不要试不同 seed 碰运气，必须先定位根因。训练只跑了 8 分钟就崩，很可能是启动阶段的问题（import error、数据加载、模型加载），不太可能是训练中期的 OOM
- **时间紧迫**：4 张 GPU 全部空闲 = 资源浪费，修复后应立即并行提交 3 个 seed + 开始准备条件 B 的代码


---
