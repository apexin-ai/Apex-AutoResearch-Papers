# agent / loop_16.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_16.md`
- **Structured JSON:** [`c6017af41a9fd94aafd7.json`](../../sessions/c6/c6017af41a9fd94aafd7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: idle_timeout
updated: '2026-05-15T15:51:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd cuda:0/1/2/3 + home cuda:0。其他 GPU 一律 push back Director
- test eval 禁止 `--max_samples`，必须评完整 test set (n=9784) / val set (n=9335)——之前 seed123 ckpt-6200/6400 因此被 Reviewer 打回重跑
- 标 FAILED/DONE 前必须 `ps -p PID` 确认进程已退出——v1 误标导致 GPU OOM 事故
- home 版 eval_repo_cls.py **不支持 `--max_new_tokens` 参数**（westd 版支持）
- CWM eval 用 `eval_repo_cwm.py`（不是 eval_repo_cls.py），max_new_tokens=1024
- EMNLP ARR **May 25** deadline，剩 10 天，不要 fallback 思维

### 2. 🖥️ 基础设施快照
- **westd** (seetacloud-westd-4x5090, account=root)
  - 工作目录: `/home/sonny/exec-sim-repair-verifier`
  - Python: `/root/miniconda3/bin/python`，激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
  - 8B 模型: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`
  - CWM 8B ckpts: `/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/` (已有 400, 4000-4300)
  - CLS 8B s42 resume ckpts: `/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/` (从 ckpt-600 起)
  - CLS 8B seed123 ckpts: `/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/` + backup `/root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000/`
- **home** (home-1x5090, account=sonny)
  - 工作目录: `/home/sonny/exec-sim-repair-verifier`
  - 4B v5 ckpts: `/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_v5/`
- **活跃进程 (3 个 cron 监控中)**:
  - `repo-level-cwm-8b-conda-v4`: PID 266816, cuda:2, step ~4013/6633 (60%), ETA May 16 ~11:00 UTC
  - `repo-level-cls-8b-s42-resume`: PID 295789 (tmux), cuda:1, step ~4041/6633 (61%), ETA May 16 ~06:00 UTC
  - `cwm8b-ckpt400-test-eval`: PID 381618, cuda:3, bs=8, ~8.4 samples/min, ETA May 16 ~09:20 UTC
- **空闲 GPU**: westd cuda:0, home cuda:0

### 3. 📊 当前状态
Paper Writing 阶段，Paper Agent 已启动 Full Draft。三个核心实验在跑，等完成后锁最后的主表数字：

| exp_id | GPU | 做什么 | ETA |
|--------|-----|--------|-----|
| repo-level-cwm-8b-conda-v4 | westd:2 | CWM 8B 训练 (从 ckpt-1600 resume) | May 16 ~11:00 |
| repo-level-cls-8b-s42-resume | westd:1 | CLS 8B s42 继续训练 | May 16 ~06:00 |
| cwm8b-ckpt400-test-eval | westd:3 | CWM 8B ckpt-400 test eval (n=9784) | May 16 ~09:20 |

**主表已锁定数字**: CLS 8B s42 test=83.52%, CLS 8B seed123 test=85.60%, CLS 4B s42 test=83.63%, CWM 4B s42 test=58.04%, CWM 4B seed123 test=59.09%, majority=72.96%。**唯一缺口: CWM 8B test**（ckpt-400 eval 在跑）。

**Worker 池 = 0**（全部靠 cron 回调触发下一步）。本 session 无 CronList 任务（cron 由系统 reconcile 管理）。

**PREPARING 残留**: cls8b-seed123-ckpt3000-val8192-eval (stale)、repo-level-cls-8b-seed123-conda-v2 (failed)——都是历史遗留，不影响当前。

### 4. 📋 待办（条件触发式）
- `cwm8b-ckpt400-test-eval` cron 回调（~May 16 09:20 UTC）→ 拿 CWM 8B test accuracy → 算 8B-8B gap → update_registry + report.md → 向 Director 汇报主表完整数字
- `repo-level-cwm-8b-conda-v4` cron 回调（~May 16 11:00 UTC）→ 训练完成后提交 final checkpoint test eval（cuda:2 释放后用它跑），与 ckpt-400 对比确认过拟合程度
- `repo-level-cls-8b-s42-resume` cron 回调（~May 16 06:00 UTC）→ extended val sweep（在 cuda:0 跑新 checkpoint 的 val eval），找 resume 后是否有新 val-best
- CWM 8B 两个 eval（ckpt-400 + final）都出结果 → 确认 eval_loss 上升 = test accuracy 下降趋势 → 选 ckpt-400 作主表数字
- 主表全部锁定后 → Paper Agent 进入 Step 2 图表 → Step 3 写作 → Step 4 审查
- **空闲 GPU 利用**: westd cuda:0 和 home cuda:0 当前待命，可用于 supplementary eval 或 s42 resume val sweep

### 5. 🎯 战略上下文
- **核心结论**: CLS reformulation 在 function-level 与 CWM 等效 (~87%)，但在 repo-level 优势 ~26pp（CWM unparseable 率 54-67%）。论文 story = complexity-dependent reformulation advantage。
- **关键决策链**: D088(val-selected)→D093(multi-seed gap 25.99pp)→D096(主表用 8B-8B 对比)→D097(rank ablation 排除 capacity confound)→D100(relaxed matching 排除 parsing excuse)→D102(CWM eval bs=8 加速)
- **最易判断错的事**:
  1. CWM 8B eval_loss 持续上升（400=0.286→4300=0.482），ckpt-400 几乎肯定是 best，但**必须同时 eval final checkpoint** 作为 evidence（不能只跑 ckpt-400 就声称结论）
  2. 4B seed123 test 极差（75.33%），4B 跨 seed 不稳定——**论文 4B 数据只用 s42**，不做 4B multi-seed claim
  3. s42 resume ckpts 从 ckpt-600 起，不含 200/400——val sweep 别提交不存在的 checkpoint
  4. Paper Agent 已启动但依赖 CWM 8B 数字才能完成主表和图表——催 Paper Agent 写非数据依赖章节（related work, method）先行


---
