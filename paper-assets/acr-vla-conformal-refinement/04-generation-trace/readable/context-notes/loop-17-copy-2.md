# agent / loop_17.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_17.md`
- **Structured JSON:** [`288245b222521b1e38ff.json`](../../sessions/28/288245b222521b1e38ff.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: idle_timeout
updated: '2026-05-17T07:03:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单严格按 `get_project_status` 的 `execution.gpu_ids`，当前 4 台服务器：bjb1-18228, bjb1-32546, bjb2-28827, bjb2-40593
- bjb2-40593 磁盘 `/usr/bin/nvidia-smi` 分区已用 90%（仅剩 46GB），不要在该服务器启动新实验写大量 checkpoint
- `eval-direct-correction` 实验已连续两次被 SIGTERM 杀死（r1 + r2），不要盲目重试——等诊断 Worker 回调确认根因后再决策
- Narrative B 已锁定 (D043)，论文 framing 不可改动除非 Director 明确批准

### 2. 🖥️ 基础设施快照
- **bjb1-32546**: `/root/acr-vla-conformal-refinement/`，Python 路径未确认（通常 `/root/miniconda3/bin/python`）
- **bjb1-18228**: 同上路径结构
- **bjb2-28827**: 同上
- **bjb2-40593**: 同上（磁盘紧张）
- 模型 checkpoint: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`（obs_only CRM 327K params）
- 评测脚本: `python -u src/evaluate.py --mode {mode} --benchmark object`
- W&B: 未配置（eval 实验不走 W&B，cron 通过进程存活 + log 检测完成）
- 活跃 GPU: 14 个 eval 进程在跑（reconcile 已确认全部 alive），详见 report.md RUNNING 表

### 3. 📊 当前状态
**刚做完**: session-start 初始化（registry 同步、cron reconcile）。收到 `eval-direct-correction-object-seed42-r2` 失败回调（SIGTERM），已派 Worker `worker_diagnose_eval-direct-correction-r2_20260517T030028` SSH 诊断根因。

**RUNNING 实验 (14个)**:
- seed46/47 pairs: `eval-obs-only-object-norm02-seed46/47` + `eval-argmin-object-seed46/47`（扩 pooled 样本到 6-seed）
- perdof ablation: `eval-perdof-object-norm01/02/03/default` × seed44/45（collapse curve 多点支撑）
- multi-variant seed45: `eval-scalar-object-seed45`, `eval-vla-mean-object-seed45`, `eval-obs-only-object-default-seed45`, `eval-obs-only-object-norm03-seed45-r2`

**等待中**:
- Worker 回调: `worker_diagnose_eval-direct-correction-r2` — 诊断 SIGTERM 根因
- 14 个 eval cron 监控中，完成后自动回调

### 4. 📋 待办
- 诊断 Worker 回调 → 根因明确后：OOM 则调整 batch/GPU 重试；被其他进程 kill 则选空闲 GPU 重试；代码 bug 则修复后重试；若 direct_correction 模式本身有系统性问题则汇报 Director 放弃该 ablation
- seed46 obs_only + argmin 完成 → 更新 pooled 统计（目标 6-seed Fisher test）
- seed47 同上 → 合并出最终 pooled p-value
- perdof ablation 完成 → 更新 magnitude curve 数据，确认 collapse 多 seed 一致性
- 所有 eval 完成 → 汇报 Director 最终统计 + 论文 figure 数据就绪

### 5. 🎯 战略上下文
- **核心结论**: obs_only CRM (ε=0.2) 是唯一存活路径。4-seed pooled: obs_only 17.5% vs argmin 13.5%, +4pp, Fisher p=0.118。Narrative B = mechanism insight（obs_only magnitude robustness vs perdof collapse）为主线贡献
- **投稿目标**: CoRL 2026，abstract DDL ~May 26，full paper DDL ~Jun 2（剩 ~10 天）
- **决策链**: D038(ε=0.2最优) → D039(perdof default=0%崩溃) → D042(claim结构) → D043(Narrative B锁定)
- **易错点**: 
  - `eval-direct-correction` 是 Claim 1 的 ablation（CRM 独立价值 vs 需要 multi-sample selection），两次失败不代表方法有问题，可能是资源冲突——先诊断再判断
  - magnitude curve 的 perdof 数据部分来自不同 seed，汇总时注意区分 seed42 单点曲线（论文 figure）和 multi-seed error bar
  - bjb1-32546 当前跑了 5 个进程（cuda:0/1/3/5 + 刚挂的 cuda:4），资源压力大


---
