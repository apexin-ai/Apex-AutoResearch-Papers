# agent / loop_5.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`f9be0e5bf93d516abd5c.json`](../../sessions/f9/f9be0e5bf93d516abd5c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-13T00:02:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- **seetacloud cgroup 360GB RAM 限制**：禁止在 seetacloud-westd-4x5090 上并行训练，只能单卡单进程（v3 OOM SIGKILL 教训，D028）
- **westd-48478 = seetacloud-westd-4x5090 是同一台物理机**（D041 确认）。seed123 实验不能和 v10/v4 并行跑在上面，必须等当前训练完
- **repo-level CWM 已迭代 10 版（v1-v10）、CLS 已迭代 4 版**：每次重提交前必须确认根因已修复，不能盲目重启
- **CWM v10 用 `--no_wandb`**：没有 W&B 指标，cron 的 NaN 检测无效，只能靠 SSH 查日志/checkpoint 判断状态
- **CLS v4 也用 `--no_wandb`**：同上

### 2. 🖥️ 基础设施快照
- **seetacloud-westd-4x5090** (root@): 4×RTX 5090, cgroup 360GB
  - 工作目录: `/root/autodl-tmp/` (模型/数据/checkpoint)
  - CWM v10 checkpoint: `/root/autodl-tmp/checkpoints_repo_cwm_v9/` (resume from checkpoint-200)
  - CWM 训练脚本: `train_repo_cwm.py`
  - PID 105205 (cuda:2), cron 监控活跃
- **home-1x5090** (sonny@): 1×RTX 5090, 62GB RAM, 非容器
  - 工作目录: `/home/sonny/exec-sim-repair-verifier/`
  - CLS v4 checkpoint: `/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_home/`
  - CLS 训练脚本: `train_repo_verifier.py`
  - PID 2885139 (cuda:0), cron 监控活跃
- **Python**: seetacloud 用 miniconda3 (conda base)；home 需确认（可能是系统 python 或 venv）
- **Eval 脚本已就绪**（Worker 已完成）: `eval_repo_cls.py`, `eval_repo_cwm.py`, `paired_bootstrap_repo.py`，test data 9784 instances (pass=7138, fail=2646)

### 3. 📊 当前状态

**刚完成**：
- Eval 脚本 Worker 已交付（eval_repo_cls.py / eval_repo_cwm.py / paired_bootstrap_repo.py），格式统一，可直接跑 D008 Go/No-Go

**正在进行**：
- `repo-level-cwm-v10` (RUNNING, seetacloud cuda:2, PID 105205): **疑似 stuck**——诊断 Worker 发现 16h 无新日志、无新 checkpoint，但进程状态 R + GPU 96%。trainer_state 显示 max_steps=6633, should_training_stop=false。Worker 仍在诊断中
- `repo-level-cls-v4` (RUNNING, home cuda:0, PID 2885139): 状态未知，需 SSH 查日志确认进展
- `worker_ssh_cwm-v10-emergency-diag-fix` (RUNNING, turn 10): 正在 SSH 调查 CWM v10 stuck 问题

**PREPARING (blocked)**：
- `repo-level-cwm-seed123`: westd-48478 cuda:3，但 westd-48478=seetacloud 同机，必须等 v10 完成
- `repo-level-cls-seed123`: westd-48478 cuda:2，同上

**总体**：51 实验，30 success / 3 negative / 13 failed / 1 killed / 2 running / 2 preparing

### 4. 📋 待办（条件触发式）
- **CWM v10 诊断 Worker 回调 →** 根据结论决定：(a) 若 stuck 需 kill+v11 重提交；(b) 若实际在跑只是日志问题则等待
- **CWM v10 训练完成 (cron 回调) →** 立即用 `eval_repo_cwm.py` 跑 eval（用 seetacloud 另一张卡，但注意 cgroup 限制）
- **CLS v4 训练完成 (cron 回调) →** 立即用 `eval_repo_cls.py` 跑 eval（home cuda:0）
- **两个 eval 都完成 →** 跑 `paired_bootstrap_repo.py` → D008 Go/No-Go：F1 diff ≥3pp 全推 EMNLP Main；1-3pp 加 seeds；<1pp Kill C1 pivot Plan B
- **D008 Go (≥3pp) →** 激活 seed123 实验 + Paper Agent Step 2-5 全速推进
- **D008 边缘 (1-3pp) →** 提交 seed123 实验（等当前训练完腾出 GPU），加统计检验力
- **CWM v10 再次失败 →** 这是第 10 次失败，必须向 Director 汇报是否 pivot（不能默默 v11）

### 5. 🎯 战略上下文
- **核心 story**: Task reformulation（execution simulation 从 generation → classification）。函数级两者等价（F1 diff <0.5pp, TOST p=0.007），核心假说转为 **complexity-dependent advantage**——repo-level 是决胜战场
- **D008 Go/No-Go 是项目生死线**：repo-level CLS vs CWM 的 F1 gap 决定论文命运。所有前期 30 个 success 实验（函数级 4B/8B、oracle、scaling、traj-level）都是已完成的 supporting evidence
- **CWM repo-level 是最大风险**：v1-v9 全部失败（代码 bug、OOM、磁盘满、平台 SIGTERM、语法错误），v10 当前疑似 stuck。如果 v10 也失败，需要严肃评估是否有系统性问题
- **时间线**：EMNLP ARR May 25 deadline，~13 天。训练 bottleneck ~20h + eval ~3h + paper ~2d = 至少 4-5d，时间仍够但没有余量再失败
- **易踩坑**：
  - 不要假设 westd-48478 是独立服务器（它就是 seetacloud）
  - seetacloud 不能并行训练（cgroup 限制）
  - CWM/CLS 都用 `--no_wandb`，不能靠 W&B 判断状态，必须 SSH 查日志
  - CWM 的 checkpoint 目录名是 `checkpoints_repo_cwm_v9`（不是 v10，因为 resume 自 v9 的 checkpoint）


---
