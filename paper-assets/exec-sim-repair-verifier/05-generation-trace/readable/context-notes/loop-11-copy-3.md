# reviewer / loop_11.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`d0cb3b1b10484a89d022.json`](../../sessions/d0/d0cb3b1b10484a89d022.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-15T01:28:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd 4 张卡全属本项目，但需核对每个进程的 CUDA_VISIBLE_DEVICES 与 registry spec.gpu 匹配
- home 服务器账号是 `sonny`（不是 root），westd 账号是 `root`
- home 上 `python` 命令可能不存在（sweep 脚本因此崩过），用 `python3` 或确认 PATH
- 8B 模型路径在 westd: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`；4B 模型在 home 用 HF hub 名 `Qwen/Qwen3-4B`
- CWM 方法在 repo-level 已确认 negative（unparseable 53-67%），但 8B CWM 训练仍在跑（v4），是为 apple-to-apple 对比数据——不要 kill

### 2. 🖥️ 基础设施快照
- **westd** (`seetacloud-westd-4x5090`, root): 工作目录 `/home/sonny/exec-sim-repair-verifier`，conda base (`/root/miniconda3/bin/python`)，transformers 4.57.6
  - checkpoints: `/root/autodl-tmp/checkpoints_repo_cls_8b_conda/`, `_8b_s42_resume/`, `_cwm_8b_conda/`, `_cls_8b_seed123_conda/`
  - 活跃进程（截至 handoff）:
    - GPU 0: cls8b-s42-ckpt1000-val8192-eval (PID 310114)
    - GPU 1: repo-level-cls-8b-s42-resume 训练 (PID 295789, step ~1583/6633, ~8.1s/step, 剩~11h)
    - GPU 2: repo-level-cwm-8b-conda-v4 训练 (PID 266816, from ckpt-1600)
    - GPU 3: repo-level-cls-8b-seed123-conda-v3 训练 (PID 266449, from ckpt-3000)
- **home** (`home-1x5090`, sonny): 工作目录 `/home/sonny/exec-sim-repair-verifier`，系统 Python
  - checkpoints: `checkpoints_repo_cls_v5/`, `checkpoints_repo_cls_seed123_home/`
  - 活跃: v5 ckpt-4400 val@5120 eval (PID 3193462, GPU 0)
- 无 W&B 配置，不检查 W&B

### 3. 📊 当前状态
**刚完成的审查**:
- worker_fix_home-v5-sweep-rerun: sweep 脚本 `python` → command not found，worker 手动用 python3 重启。**脚本本身未修复**。
- worker_collect_v5-ckpt4000-result-and-submit-4200: ckpt-4000 收集成功 (acc=89.84%)，但**跳过了 ckpt-4200 直接提交 4400**。ckpt-4200 val@5120 仍缺失。
- cls8b-s42-ckpt800-val8192-eval 完成 (acc=84.5%, F1m=79.2)，未超过 85% 阈值。ckpt-1000 已接力提交。

**Registry RUNNING**:
- `cls8b-s42-ckpt1000-val8192-eval` — westd GPU 0, 8B resume ckpt-1000 val@8192
- `repo-level-cls-8b-s42-resume` — westd GPU 1, 8B CLS s42 全量训练
- `repo-level-cwm-8b-conda-v4` — westd GPU 2, 8B CWM 训练
- `repo-level-cls-8b-seed123-conda-v3` — westd GPU 3, 8B CLS seed123 训练
- home GPU 0 上 ckpt-4400 eval 在跑（PID 3193462），但**无 registry 条目**

### 4. 📋 待办（条件触发式）
- ckpt-4400 val@5120 完成 → 收集结果 → **必须补跑 ckpt-4200 val@5120**（当前 sweep 缺口）→ 再跑 ckpt-4600
- ckpt-1000 val@8192 完成 → 收集结果，若 >85% 需补跑 test@8192；否则继续 ckpt-1200
- 8B s42 resume 训练每产出新 checkpoint (save_steps=200) → 排队 val@8192 eval 到 GPU 0
- CWM 8B / CLS 8B seed123 训练完成 → 需要 eval sweep（这两个训练还剩 ~10h+）
- `run_v5_val5120_sweep.sh` 中 `python` → `python3` 仍未修复，提醒 Agent 修

### 5. 🎯 战略上下文
- **目标**: EMNLP 2026 ARR May 25 截稿（剩 10 天），核心 claim 是 CLS vs CWM complexity-dependent advantage
- **关键数据趋势**: val@5120 上 later checkpoints 表现更好（seed123: ckpt-800 87.92% > ckpt-400 86.01%；v5: ckpt-4000 89.84% > ckpt-600 82.82%），但 **seed123 已显示 val-test distribution shift**（val best ckpt-800 87.92% vs test best ckpt-600 80.73%，ckpt-800 test 退化至 74.27%）。val 趋势不可直接推广到 test。
- **易错点**: 
  1. 不要因 val 数字好就 claim "best checkpoint"——必须看 test 验证
  2. ckpt-4200 val@5120 缺失容易被忽略（已有 ckpt-4200 的 test@2048 旧结果，但那不是 val@5120）
  3. 8B resume 训练的 checkpoint 编号从 800 开始（从 ckpt-600 resume），不要和原始训练的 ckpt-200/400/600 混淆——它们来自不同的 output_dir


---
