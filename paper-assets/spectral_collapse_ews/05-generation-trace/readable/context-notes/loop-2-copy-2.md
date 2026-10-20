# agent / loop_2.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`abda7e69bd190bed075f.json`](../../sessions/ab/abda7e69bd190bed075f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-17T10:19:37+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：只能用 rtx6000-diagprobe 的 cuda:0 和 cuda:1，不得用其他设备
- 根分区只有 30GB 且当前已满——任何新实验提交前必须先清理根分区，否则必定复现 exp_002 同样的磁盘满崩溃
- Checkpoint 必须写 /root/autodl-tmp/，绝不能写根分区（symlink 已配置但要验证）
- Phase 1 已获 D009 审批，但启动前需确认根分区空间已清理

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe，2× RTX PRO 6000 (98GB each)
- 工作目录：/root/spectral_collapse_ews/
- Python：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型缓存：/root/autodl-tmp/spectral_collapse_ews/models/（Pythia 410M + 1B）
- 数据：/root/spectral_collapse_ews/data/（train_real_50k.pt, eval_5k.pt, spectral_1k.pt）
- 数据盘：/root/autodl-tmp/ (5.3T/7.3T 可用)
- 活跃进程：exp_001 PID 59365, tmux=exp_001_gen4, cuda:0
- Worker: worker_fix_verify_symlink_disk (CPU, 验证 symlink 任务)

### 3. 📊 当前状态
刚处理 exp_002 (1B pilot) 失败回调——根分区满导致 SIGTERM。已更新 registry、发飞书卡片、向 Director 汇报并建议 cuda:1 立即投入 Phase 1。

Registry:
- **exp_001** RUNNING：Pythia 410M Phase 0 full 10-gen，当前 Gen 5/10 generating，cuda:0
- **exp_002** DONE(failed)：Pythia 1B Phase 0，Gen 0-3 数据保存完好，cuda:1 已释放

等待中：
- Director 回复：是否批准 cuda:1 启动 Phase 1
- exp_001 cron 回调：Gen 5-10 完成后触发
- worker_fix_verify_symlink_disk 回调

### 4. 📋 待办
- Director 批准 Phase 1 on cuda:1 → 先派 Worker 清理根分区（删 pip cache / tmp / 旧 log），确认空间 > 5GB → 提交 Phase 1 condition (a) pure collapse seed=42
- exp_001 完成（Gen 10）→ 运行 analyze_phase0.py 校准 τ/k → 用校准值更新 Phase 1 controller 参数 → cuda:0 也投入 Phase 1 剩余 seeds
- exp_001 失败 → 查日志，大概率也是磁盘问题 → 清理后 resume
- Phase 1 全部完成 → paired t-test 对比 adaptive vs uniform，汇报 Director

### 5. 🎯 战略上下文
- 核心方向：spectral EWS 引导自适应数据混合，对抗 model collapse（paper_framing.md 待 MVP 后创建）
- 投稿目标：EMNLP 2026 ARR May 25（DDL 还剩 8 天，时间极紧）
- 决策链：D001 MVP 方案 → D004 baseline 从 Gen 1 → D005 controller 参数 → D009 Phase 0 PASS，Phase 1 批准
- Phase 0 已证实：eff_rank 不单调下降（先升后平），但 collapse 由 ppl/distinct4/σ₁ 三重确认。EWS 信号候选可能需从 eff_rank 转向 σ₁ 衰减率或 Gini/HHI
- 易错点：(1) 根分区 30GB 极小，每次提交前必须检查磁盘 (2) Phase 1 的 run_phase1.py 已在服务器上验证过，不需要重写 (3) controller 参数 D005 已定（k=1.0, τ=0.02），但 exp_001 完成后 analyze_phase0.py 可能产出更优校准值——Phase 1 先用 D005 默认值跑着，校准值出来后看是否需要 re-run


---
