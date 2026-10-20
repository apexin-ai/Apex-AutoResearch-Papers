# agent / loop_3.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`780497919da6478c1371.json`](../../sessions/78/780497919da6478c1371.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-17T17:44:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：rtx6000-diagprobe 的 cuda:0 和 cuda:1，不得使用其他设备
- exp_003 已因 3 个 controller bug 被 kill（D011：budget deduction 用 request 而非 actual、Gen 0 baseline 缺失、ratio>0.5 在 50K real pool 下物理不可能），这些 bug 修复状态需确认后才能重跑 adaptive 实验
- checkpoint 必须写 /root/autodl-tmp/（root 分区仅 30GB，exp_002 曾因 root 满崩溃）
- 环境激活必须用 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要假设 .venv 存在

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe（2× RTX PRO 6000, 98GB each）
- 工作目录：/root/spectral_collapse_ews
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型：EleutherAI/pythia-410m-deduped（主），pythia-1b-deduped（scale transfer）；HF cache 本地已有（HF_HUB_OFFLINE=1）
- 数据：/root/spectral_collapse_ews/data/（50K train + 5K eval + 1K spectral）
- Checkpoint 盘：/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/
- 磁盘：/autodl-tmp ~401GB 可用（充裕），root 分区需注意
- 活跃进程：exp_001 (PID 59365, tmux=exp_001_gen4, cuda:0, Phase 0 Gen 8/10)
- 日志：exp_001 → /root/spectral_collapse_ews/results/phase0_gen4_run.log

### 3. 📊 当前状态
**刚发生**：exp_005（Phase 1 adaptive k=20 tau=0.002）失败，"process dead 5× with no sentinel/W&B"。已派 Worker `worker_diagnose_exp_005_20260517T134252` SSH 诊断日志，**尚未回调**——这是最高优先级待处理项。

**Registry 概览**：
- exp_001: RUNNING — Phase 0 纯 collapse 特征化，Gen 8/10，cuda:0，预计 ~2h 完成
- exp_004: PREPARING — Phase 1 fixed_mix 50/50 baseline，等 cuda:0 空出（或可用 cuda:1）
- exp_002: DONE/success — 1B pilot，Gen 0-3 完整，已确认 cross-scale 3-phase pattern
- exp_003: DONE/killed — D011 三 bug，结果无效
- exp_005: DONE/failed — k=20 adaptive，进程异常退出，诊断中

**等待中**：
- Worker 回调：worker_diagnose_exp_005 诊断结果
- Cron：exp_001 进程监控
- cuda:1 当前空闲（exp_005 崩溃后释放）

### 4. 📋 待办
- worker_diagnose_exp_005 回调 → 读诊断结论 → update_registry 写入 failure_reason 细节 → 向 Director 汇报根因和修复方案
- 诊断确认是 bug（非 OOM/disk）→ 派 Worker 修复代码 → dry-run 验证 → 重新提交 exp_005v2 到 cuda:1
- 诊断确认是 OOM/资源 → 调整参数（batch_size / gradient_accumulation）→ 重提交
- exp_001 cron 回调（Gen 10 完成）→ 收集 Gen 0-10 全量 metrics → 跑 analyze_phase0.py → 启动 exp_004（fixed_mix）到空出的 cuda:0
- exp_004 可以不等 cuda:0：cuda:1 现在空闲，确认 exp_005 不会立即重跑的话，可以先把 exp_004 提交到 cuda:1
- Phase 1 核心对比完成（adaptive vs fixed_mix 至少 1 seed）→ 向 Director 汇报 go/no-go

### 5. 🎯 战略上下文
- **投稿目标**：EMNLP 2026 ARR May 25（距今 8 天）
- **核心 narrative**：log-determinant 作为 early warning signal 引导自适应数据混合，比固定比例更有效防止 model collapse
- **决策链**：D009（Phase 0 go/no-go PASS）→ D010（signal 从 eff_rank 切 log_det, tau 0.02→0.005）→ D011（controller 三 bug kill exp_003）→ D012（k 从 1.0 提到 20, tau 从 0.005 降到 0.002 校准）
- **关键风险**：Phase 1 adaptive 实验已连续失败两次（exp_003 killed by bugs, exp_005 crash），还没拿到任何 adaptive vs fixed_mix 的对比数据。DDL 压力下，确保下一次 adaptive run 成功是最高优先级
- **易错点**：D011 修复的三个 bug 是否真的在 exp_005 的代码版本中修好了——exp_005 用了新参数 k=20 但代码修复状态不确定，诊断时需要同时确认代码是否正确
- **Phase 0 数据已足够**：Gen 0-7 monotonic decline 已确认（eff_rank 496→464, ppl 9.55→38.89, HellaSwag -16.7%），Gen 8-10 是补完不阻塞


---
