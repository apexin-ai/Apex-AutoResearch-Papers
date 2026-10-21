# agent / loop_18.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_18.md`
- **Structured JSON:** [`66d8656f35ad6cbf3871.json`](../../sessions/66/66d8656f35ad6cbf3871.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: idle_timeout
updated: '2026-05-15T22:53:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**：westd cuda:0/1/2/3 + home cuda:0。其他 GPU 禁用（即使 Director 指令也 push back）
- **eval 禁止 --max_samples**：test eval 必须全量 n=9784，val eval 全量 n=9335。违反导致与主表不可比（已踩坑两次）
- **标 FAILED 前必须 `ps -p PID` 确认进程已退出**：否则新任务上同 GPU 会 OOM（v1 事故）
- **seq_length/bs/precision/lr 变更需 Director 审批**（D103）
- **CWM 8B eval 用 `eval_repo_cwm.py`**（不是 eval_repo_cls.py），max_new_tokens=1024
- **home 版 eval 脚本不支持 --max_new_tokens 参数**

### 2. 🖥️ 基础设施快照
- **westd**: `seetacloud-westd-4x5090`，工作目录 `/home/sonny/exec-sim-repair-verifier`
  - Python: `/root/miniconda3/bin/python`，激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
  - HF cache: `/root/autodl-tmp/.hf_cache/`，8B 模型: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`
  - CWM 8B checkpoints: `/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/`（有 400, 4000-4300）
  - CLS 8B s42 resume checkpoints: `/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/`（从 ckpt-600 起）
  - CLS 8B seed123 checkpoints: `/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/` + backup ckpt-3000
- **home**: `home-1x5090`，工作目录 `/home/sonny`，用 `python3`
  - 4B v5 checkpoints: `/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_v5/`
- **活跃进程**:
  - `cwm8b-ckpt400-test-eval`: PID 381618, westd cuda:3, ~30.5% (2984/9784 samples), ETA May 16 17:15 UTC
  - `repo-level-cwm-8b-conda-v5`: PID 400279, westd cuda:2, CWM 8B 训练 resume from ckpt-5200
- **Cron**: 2 个活跃（分别监控上述两个 RUNNING 实验）

### 3. 📊 当前状态
**阶段**: Paper Writing，EMNLP 2026 ARR May 25 截稿（剩 10 天）。

**RUNNING (2)**:
- `cwm8b-ckpt400-test-eval` — CWM 8B best-eval-loss checkpoint test eval，bs=8，30.5% 完成，~8.4 samples/min，ETA May 16 17:15 UTC。完成后锁定 8B-8B CLS-CWM gap。
- `repo-level-cwm-8b-conda-v5` — CWM 8B 训练 resume from ckpt-5200，cuda:2。ROADMAP 标 57%。

**PREPARING (2)**:
- `cls8b-s42-ckpt1000-test-mutation` — per-mutation-type breakdown，计划 home cuda:0
- `cls8b-s42-resume-ckpt1000-test-mutation` — 同上，spec 未填

**Paper Agent 已启动 Full Draft**（ROADMAP 记录），正在 Step 2 图表 → Step 3 写作。

**等待**: 两个 cron 回调（CWM 8B eval 完成 + CWM 8B 训练完成）。无 pending Worker 回调。无 Director 待决策。

### 4. 📋 待办（条件触发式）
- `cwm8b-ckpt400-test-eval` cron 回调 → 提取 accuracy + unparseable rate → update_registry → 计算 8B-8B gap → 如 gap ≥20pp 则 claim 成立，汇报 Director 锁定主表最后一行
- `repo-level-cwm-8b-conda-v5` cron 回调 → 若训练完成，需 eval final checkpoint（与 ckpt-400 对比确认过拟合趋势）→ submit eval on cuda:2
- CWM 8B eval + training 两者都完成 → 主表 6 行全部锁定 → Paper Agent 可写 Results
- PREPARING 的 mutation-type breakdown 实验 → 等 home cuda:0 空闲时提交（需先填 spec）
- westd cuda:0 和 cuda:1 目前空闲 → 检查是否有 s42 resume 训练仍在跑（ROADMAP 标 55%），若已完成则可用于 supplementary eval

### 5. 🎯 战略上下文
**核心结论**: CLS reformulation 在 repo-level 比 CWM 有 ~26pp 优势（multi-seed 平均 25.99pp）。CWM 的主要失败模式是 unparseable output（4B: 53-67%）。已排除 seq_length confound（CLS@2048 仍有 24.79pp gap）和 LoRA rank confound（rank=32 vs 16 差异 <1pp）。

**决策链**: D088 确立 val-selected checkpoint 为主指标 → D093 锁定 multi-seed 数字 → D094-D098 完成 ablation → D100-D101 排除 relaxed matching → D103 禁止未授权参数降级。

**CWM 8B 是最后一个数据点**。eval_loss 持续上升（400=0.286 → 4300=0.482），ckpt-400 很可能是 best。如果 CWM 8B test accuracy 仍 ~58-60%，8B-8B gap ~23-25pp，核心 claim 完全成立。如果 CWM 8B 显著好于 4B（>65%），gap 缩小但 claim 仍成立，需调整措辞强度。

**易错点**:
- 不要把 4B 和 8B 的 CWM 数字直接对比得出"scaling helps CWM"结论——seed/训练步数/数据量都不同
- home 和 westd 的 eval 脚本版本略有差异（home 不支持 --max_new_tokens）
- s42 resume 的 checkpoint 目录从 ckpt-600 起，不含 200/400


---
