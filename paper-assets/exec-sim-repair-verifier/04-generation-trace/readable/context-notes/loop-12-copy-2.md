# agent / loop_12.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_12.md`
- **Structured JSON:** [`41d19b0c04e738d284a9.json`](../../sessions/41/41d19b0c04e738d284a9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: idle_timeout
updated: '2026-05-14T22:41:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: cuda:0/1/2/3（westd 4x5090）+ home cuda:0（home-1x5090）。不得用白名单外 GPU
- **D063 方法论**: checkpoint 选择必须在 val set (9335 samples) 上做，test set (9784) 只报最终数字。已发现 val-test ranking reversal（ckpt-600 val best 但 test worst），val selection 可能不可靠
- **8B checkpoints_repo_cls_8b/checkpoint-3000 是旧训练产物（transformers 5.x / peft 0.19.1），不可引用**。89.50% val 无效（D080）
- eval_repo_cls.py 8B 模型必须 `--batch_size 1 --max_new_tokens 512`，否则 OOM
- submit_training_job 不支持 shell builtin（source/conda activate），用 `bash -c "source ... && ..."`
- CLS vs CWM 比较必须用 westd conda 数据（同 server/env/data）
- EMNLP 2026 ARR May 25 DDL，剩余 11 天

### 2. 🖥️ 基础设施快照
- **westd** (seetacloud-westd-4x5090, root):
  - 工作目录: `/home/sonny/exec-sim-repair-verifier`
  - Python: `/root/miniconda3/bin/python`（conda base env）
  - 模型: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`
  - 数据: `/home/sonny/exec-sim-repair-verifier/data/swebench_full`（70748 条）
  - Checkpoints:
    - 8B CLS s42: `/root/autodl-tmp/checkpoints_repo_cls_8b_conda/` (ckpt-200~600)
    - 8B CLS s42 resume: `/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/` (训练中，from ckpt-600)
    - 8B CLS seed123: `/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/` (from ckpt-3000 resume)
    - 8B CWM: `/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/`
    - 8B seed123 backup: `/root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000`
  - 活跃进程:
    - cuda:1 — CLS 8B s42 resume, PID 295794, tmux=repo-level-cls-8b-s42-resume, step ~656/6633
    - cuda:2 — CWM 8B v4, PID 266816, tmux=repo-level-cwm-8b-conda-v4, step 1700/6633
    - cuda:3 — CLS 8B seed123 v3, PID 266444, tmux=repo-level-cls-8b-seed123-conda-v3, from ckpt-3000
  - Cron 监控: 4 个活跃（上述 3 个 + cls4b-v5-val5120-sweep-home）

- **home** (home-1x5090, sonny):
  - 工作目录: 同项目路径
  - Checkpoints: `checkpoints_repo_cls_v5/` (4B v5 s42)
  - cuda:0 — cls4b-v5-ckpt600-val5120-eval RUNNING (PID 3179262)
  - Worker `worker_eval_s42-ckpt800-val8192-submit` 正在监控

### 3. 📊 当前状态

**刚完成**: CWM error analysis (D082)、val-test reversal 根因分析 (D087)、8B s42 resume 提交

**RUNNING (4 个)**:
1. `repo-level-cls-8b-s42-resume` — westd cuda:1, 8B CLS s42 full training from ckpt-600→6633, ~13.5h 剩余
2. `repo-level-cwm-8b-conda-v4` — westd cuda:2, 8B CWM 训练 step 1700/6633, ~16h 剩余
3. `repo-level-cls-8b-seed123-conda-v3` — westd cuda:3, 8B CLS seed123 from ckpt-3000
4. `cls4b-v5-ckpt600-val5120-eval` — home cuda:0, 4B v5 ckpt-600 val@5120 eval

**PREPARING (已死/无效，需清理)**:
- `cls4b-v5-val5120-sweep-home` — 4B v5 val sweep 排队等 home cuda:0 空闲
- `repo-level-cls-8b-s42-ckpt200-val` — failed (PID 死)
- `cls8b-ckpt3000-test-v2` / `cls8b-ckpt3000-test-eval` — INVALID (旧 checkpoint)

**等待中**:
- Worker `worker_eval_s42-ckpt800-val8192-submit` (running) — 监控 home eval
- 无待处理 Director 决策

### 4. 📋 待办（条件触发式）
- `cls4b-v5-ckpt600-val5120-eval` 完成 → 启动 `cls4b-v5-val5120-sweep-home`（ckpt-4000/4200/4400/4600 依次 eval），结果入 D063 val sweep
- `repo-level-cls-8b-s42-resume` 完成 → spawn Worker 做 val@5120 sweep（多 checkpoint），确定 8B s42 val-best，再跑 test 最终数字
- `repo-level-cwm-8b-conda-v4` 完成 → spawn Worker eval 8B CWM，得到 8B-8B CLS vs CWM gap
- `repo-level-cls-8b-seed123-conda-v3` 完成 → spawn Worker eval，得到 8B multi-seed 数据
- 所有 val sweep + 8B 训练完成 → 锁定 paper 最终数字，patch paper sections
- 3 个 PREPARING(failed/invalid) 实验 → 清理 registry 标记为 DONE(failed)

### 5. 🎯 战略上下文

**核心结论链**:
- C1 (Complexity-Dependent Advantage): CLS >> CWM，gap 随代码复杂度增长。Function-level gap 1.24pp(4B)/2.43pp(8B)，repo-level gap 24-26pp
- C2 (Diagnostic Granularity): TOST p=0.007 确认
- C3 (Accuracy-Utility Frontier): 已完成
- D082: CWM repo-level 彻底失败（parseable-only acc 仅 42%），直接支持 C1
- D087: Val-test reversal 是真实分布差异（problem 零重叠 + mutation type 剧变），不是截断假象

**易错点**:
- **不要用 test set 数字做 checkpoint selection**——这是 D063 的核心修复点，之前 ROADMAP 里的 CLS 84.52% 就是 test sweep 选出来的
- **不要混淆两个 8B checkpoint 路径**: `checkpoints_repo_cls_8b/`(旧/无效) vs `checkpoints_repo_cls_8b_conda/`(当前有效)
- **westd cuda:0 当前空闲**但之前有 eval 进程死掉——新任务前先确认 GPU 状态
- 4B val sweep 用 home 上的 checkpoint 路径 `checkpoints_repo_cls_v5/`，不是 westd 路径
- CWM seed123 的 unparseable 率 67.2% 远高于 v12 的 53.7%——报告时分开写，不要取平均


---
