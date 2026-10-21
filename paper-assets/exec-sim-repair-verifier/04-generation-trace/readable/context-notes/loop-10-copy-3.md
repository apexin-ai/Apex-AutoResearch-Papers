# reviewer / loop_10.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`5826021a6691e6445b08.json`](../../sessions/58/5826021a6691e6445b08.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-14T21:26:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd 训练 GPU 分配：cuda:2 = CWM 8B v4, cuda:3 = CLS 8B seed123 v3。cuda:0/1 仅用于 eval。不可在 cuda:0/1 上启动训练。
- `checkpoints_repo_cls_8b/` 是 transformers 5.8.0 旧训练产物（peft 0.19.1），**已判定无效**（D080）。任何引用该目录 checkpoint 的 eval 必须拦截。
- `checkpoints_backup_cls_8b_seed123/` 是 `auto_backup_checkpoints.sh` 对 conda 训练的自动备份，peft 0.19.0，溯源有效。备份目录保留了被 save_total_limit 删除的历史 checkpoint（17 个 vs 原目录 5 个）。
- D063 硬约束：checkpoint 选择必须在 val set (9335) 上做，test set (9784) 只报最终数字。val eval 需用 max_seq_length ≥ 5120（D077: 2048 导致 20% unparseable）。
- Home 服务器 peft=0.19.1 + transformers=4.57.6 是合法组合，不要和 westd 旧环境（peft 0.19.1 + transformers 5.8.0）混淆。

### 2. 🖥️ 基础设施快照
- **westd**: `seetacloud-westd-4x5090`(root), 工作目录 `/home/sonny/exec-sim-repair-verifier`, Python `/root/miniconda3/bin/python`, conda base
  - 模型: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`, `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B`
  - 数据: `/home/sonny/exec-sim-repair-verifier/data/swebench_full/`
  - 活跃训练: PID 266449 (CLS 8B s123, cuda:3, tmux), PID 266816 (CWM 8B v4, cuda:2, tmux)
  - 活跃 eval: PID 291896 (8B s42 ckpt-400 test@8192, cuda:0), PID 291117 (seed123 8B backup-ckpt-3000 val@8192, cuda:1)
  - Backup script: PID 228418 `auto_backup_checkpoints.sh`
- **home**: `home-1x5090`(sonny), 工作目录 `/home/sonny/exec-sim-repair-verifier`, Python 系统 python3.10 (`/home/sonny/.local/`)
  - 活跃 eval: PID 3172988 (seed123 4B ckpt-800 val@5120, cuda:0)
- 无 W&B 配置（所有实验 --no_wandb）

### 3. 📊 当前状态
刚完成一轮完整审查，关键发现已全部 post 给 Director：

**已完成的重要审查**：
- CWM 4B eval 最终确认：58%/59% accuracy，低于 majority baseline（72.96%），C1 稳固
- CWM error analysis：parseable-only accuracy 仅 42-43%，per-repo unparseable 从 0% (scikit-learn) 到 100% (sphinx)
- **CRITICAL**: 8B s42 val-test checkpoint 排名反转——val best=ckpt-600(85.02%) vs test best=ckpt-400(84.52%)。D063 要求按 val 选，test 数字会从 84.52% 降至 78.51%
- Home checkpoint 溯源通过（peft 0.19.1 + transformers 4.57.6 合法）
- v5_conda ckpt-400 val@8192 = 86.36%（完成），ckpt-600 被 kill 未完成（需重跑）

**Registry RUNNING**：
- `repo-level-cls-8b-seed123-conda-v3`: cuda:3, ~checkpoint-3800/6633 (57%), ETA ~14:00 UTC May 15
- `repo-level-cwm-8b-conda-v4`: cuda:2, ~checkpoint-2000/6633 (30%), ETA ~11:30 UTC May 16

**正在等待的 eval 结果**：
- westd cuda:0: 8B s42 ckpt-400 test@8192（PID 291896）— 解决 val-test 反转混杂变量
- westd cuda:1: seed123 8B backup-ckpt-3000 val@8192（PID 291117）
- home cuda:0: seed123 4B ckpt-800 val@5120（PID 3172988）

### 4. 📋 待办（条件触发式）
- 8B s42 ckpt-400 test@8192 完成 → 对比 test@2048 (84.52%)，如差异 <1pp 则 val-test 反转是真实泛化差异；如显著提升则是 seq_length 混杂 → 需跑 ckpt-600 test@8192
- seed123 8B ckpt-3000 val@8192 完成 → 交叉验证 backup checkpoint 质量，对比 ckpt-3800+ 的 val 结果
- seed123 4B ckpt-800 val@5120 完成 → 更新 val sweep 表，确认 4B val-best（目前 ckpt-400=86.01%）
- CLS 8B seed123 v3 训练完成 → 立即审查最终 checkpoint，启动 val+test sweep
- CWM 8B v4 训练完成 → 审查并启动 8B-8B CLS-CWM 对比 eval
- v5_conda ckpt-600 val@8192 需重跑（被 kill，数据丢失）
- s42 8B CLS resume from ckpt-600 待 GPU 空闲时启动（当前训练仅完成 9%）

### 5. 🎯 战略上下文
**核心结论链**：D004(reframe to task reformulation) → D006(CWM baseline 对比) → D081(CLS-CWM gap 24-26pp) → D082(CWM parseable-only 42%, error analysis 支持 complexity-dependent failure)

**最容易判断错的事**：
1. **peft 版本不是溯源唯一标志**。westd 有两套环境：旧(transformers 5.8.0 + peft 0.19.1 = INVALID) 和 conda(transformers 4.57.6 + peft 0.19.0 = VALID)。但 home 的 peft 0.19.1 + transformers 4.57.6 是合法的。判定溯源看 transformers 版本，不看 peft。
2. **Val-test 反转是当前最大风险**。8B s42 ckpt-600 val=85% 但 test=78.5%。正在跑 test@8192 控制变量。在结果出来前不要下结论说"ckpt-600 是最优"或"ckpt-400 是最优"。
3. **"Worker 标记 failed" ≠ "没产出"**。CWM error analysis worker failed 但文件已生成。审查 failed worker 时先检查服务器上的实际产出。
4. **ROADMAP 的 PID 经常过时**（多次重启训练），以 nvidia-smi 和 ps 实际查到的为准。


---
