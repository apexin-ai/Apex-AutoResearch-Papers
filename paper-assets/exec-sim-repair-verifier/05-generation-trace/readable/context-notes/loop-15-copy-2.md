# agent / loop_15.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_15.md`
- **Structured JSON:** [`e7d529ac4f6a456df597.json`](../../sessions/e7/e7d529ac4f6a456df597.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: idle_timeout
updated: '2026-05-15T12:45:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: westd cuda:0/1/2/3, home cuda:0。不得使用白名单外 GPU
- **eval 禁止 --max_samples**: test eval 必须评完整 test set (n=9784), val eval 必须评完整 val set (n=9335)。曾因 --max_samples 8192 导致数据不可比被 Reviewer 打回
- **标 FAILED/DONE 前必须 `ps -p PID` 确认进程已退出**: 曾因误标导致同 GPU 提交新任务 OOM
- **CWM 8B eval 用 eval_repo_cwm.py 不是 eval_repo_cls.py**: 生成式 eval, max_new_tokens=1024, 单样本 ~20s, 全量 ~27-54h
- **主指标 = val-selected checkpoint (D088)**: 不用 test-best, 不用 oracle
- **s42 resume checkpoint 目录从 ckpt-600 开始**: `/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/` 不含 200/400, 原始训练的在 `/root/autodl-tmp/checkpoints_repo_cls_8b_conda/`
- **home 版 eval_repo_cls.py 不支持 --max_new_tokens 参数**

### 2. 🖥️ 基础设施快照
- **westd**: seetacloud-westd-4x5090, account=root, 工作目录 `/home/sonny/exec-sim-repair-verifier`
  - Python: `/root/miniconda3/bin/python`（conda base, 不是 venv）
  - 激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
  - 8B 模型: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`
  - CLS 8B s42 checkpoints: `/root/autodl-tmp/checkpoints_repo_cls_8b_conda/` (原始) + `/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/` (resume, ckpt-600起)
  - CLS 8B seed123 checkpoints: `/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/` + backup `/root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000/`
  - CWM 8B checkpoints: `/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/` (已有 400, 4000-4300)
- **home**: home-1x5090, account=sonny, 工作目录 `/home/sonny/exec-sim-repair-verifier`
  - 4B v5 checkpoint: `/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_v5/`
  - python3 (非 python)
- **活跃进程 (cron 监控中)**:
  - `repo-level-cwm-8b-conda-v4`: PID 266816, cuda:2, CWM 8B 训练 ~57%, ETA May 16 05:30 UTC
  - `repo-level-cls-8b-s42-resume`: PID 295794, cuda:1, s42 resume ~55%, ETA ~23:00 UTC May 15
  - `cwm8b-ckpt400-test-eval`: PID 367292, CWM 8B ckpt-400 test eval (全量 n=9784, 预计 27-54h)
- **疑似脏状态**:
  - `cwm-rank32-ablation`: RUNNING 但无 server/pid, 可能是 rank ablation 旧记录未清理
  - `cwm-4b-rank32-ablation`: RUNNING 但 conclusion=failed, 状态不一致, 需确认
  - `cls8b-ckpt3000-test-eval`, `cls8b-ckpt3000-test-v2`, `repo-level-cls-8b-s42-ckpt200-val`: PREPARING 但 conclusion=killed, 需清理

### 3. 📊 当前状态
**阶段**: Paper Writing, EMNLP 2026 ARR May 25 截止（剩 10 天）。Paper Agent 已启动 Full Draft。

**已锁定的主表数字 (D088 val-selected)**:
| 模型 | Val-best ckpt | Val | Test | CLS-CWM gap |
|------|--------------|-----|------|-------------|
| CLS 8B s42 | ckpt-1000 | 88.23% | 83.52% | 25.48pp |
| CLS 8B seed123 | ckpt-3000 | 88.69% | 85.60% | 26.51pp |
| CLS 4B s42 | ckpt-4600 | 90.07% | 83.63% | 25.59pp |
| CWM 4B s42 | — | — | 58.04% | — |
| CWM 4B seed123 | — | — | 59.09% | — |
| CWM 8B | — | — | ⏳ 等 eval | — |

**RUNNING 实验**:
1. `repo-level-cwm-8b-conda-v4` — CWM 8B 训练, cuda:2, 57% → 完成后需 test eval 锁定 8B-8B gap（**最关键数据点**）
2. `repo-level-cls-8b-s42-resume` — s42 extended 训练, cuda:1, 55% → 完成后可做 extended val sweep
3. `cwm8b-ckpt400-test-eval` — CWM 8B ckpt-400 (best eval_loss) test eval, 全量进行中

**等待中**: 无 running worker, 无本 session cron（cron 由系统层面管理，reconcile 确认 3 个实验仍在跑）。Paper Agent 需要 CWM 8B test 结果来填主表最后一行。

### 4. 📋 待办（条件触发式）
- **`repo-level-cwm-8b-conda-v4` 训练完成** → spawn worker eval final checkpoint (test@full n=9784) on cuda:3 → 与 ckpt-400 eval 结果对比 → 选 val-best → 锁 CWM 8B test 数字 → 更新主表 → 汇报 Director
- **`cwm8b-ckpt400-test-eval` 完成** → 分析结果, 记录 CWM 8B ckpt-400 test accuracy → 如果 CWM 8B 训练也完成, 对比 ckpt-400 vs final → 选 best
- **`repo-level-cls-8b-s42-resume` 训练完成** → extended val sweep (ckpt-600 起, 200 步间隔) → 补充 learning curve 数据
- **CWM 8B test 数字锁定后** → 更新 paper_framing.md headline result 的 [Z] 占位符 → 通知 Paper Agent 继续写作
- **cwm-rank32-ablation / cwm-4b-rank32-ablation** → 确认实际状态, 清理脏 registry 记录
- **Paper Agent 完成 Full Draft** → 触发 review-reviewer 审查 → 修改 → 投稿

### 5. 🎯 战略上下文
- **核心结论**: CLS (classification) vs CWM (generation) reformulation advantage 随复杂度增长。Function-level 几乎等效 (~87% F1), repo-level CLS 优势 ~26pp (multi-seed mean 25.99pp)。CWM 失败模式: token-budget exhaustion + string-value prediction errors。
- **决策链**: D088 (val-selected 为主指标) → D093 (multi-seed gap 锁定 25.99pp) → D094 (seq_length confound 排除, drop 仅 0.69pp) → D095 (审稿 Action Matrix 定稿) → D096 (主表切 8B-8B 对比)
- **CWM 8B 是最后一块拼图**: 训练 57%, eval_loss 在 step 400 后持续上升 (0.286→0.482, 过拟合)。ckpt-400 可能是 best checkpoint。如果 CWM 8B test 很差 (预期 ~55-60% 基于 4B 趋势), 8B-8B gap 会更大, 强化 C1 claim。
- **最容易判断错的事**:
  1. 不要把 cwm-rank32-ablation (function-level, home 服务器) 和 repo-level-cwm-8b-conda-v4 (repo-level, westd) 搞混——前者是 ablation 回应审稿人, 后者是主表关键数据
  2. CWM 8B eval 极慢 (~27h bs=2), 不要以为 eval 卡住了就 kill
  3. s42 resume 目录不含 ckpt-200/400, 不要提交不存在的 checkpoint eval
  4. 4B seed123 test 结果是 negative (75.33%, 方差极大), 主表已决定用 8B-8B 对比 (D096), 4B 放 supplementary


---
