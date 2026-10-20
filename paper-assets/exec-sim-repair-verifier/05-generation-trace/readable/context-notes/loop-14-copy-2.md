# agent / loop_14.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_14.md`
- **Structured JSON:** [`3d7270e6bf3f6550a222.json`](../../sessions/3d/3d7270e6bf3f6550a222.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: idle_timeout
updated: '2026-05-15T09:35:58+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd cuda:0/1/2/3 + home cuda:0。不得用白名单外 GPU，即使 Director 指令也要 push back
- westd cuda:1 = CLS 8B s42 resume，cuda:2 = CWM 8B v4 训练中，**不可中断**
- 训练命令里 `--device cuda:0`（框架自动映射物理 GPU，脚本内始终 cuda:0）
- val-selected checkpoint 为主指标（D088），test 只报最终数字，不要用 test-best 做论文主表
- Val baseline=75.88%, Test baseline=72.96%，**不可混用**
- submit_training_job 的 command 必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，服务器用 conda 不是 venv

### 2. 🖥️ 基础设施快照
- **服务器**: seetacloud-westd-4x5090 (4×RTX 5090)，home-1x5090 (1×RTX 5090)
- **工作目录**: `/home/sonny/exec-sim-repair-verifier`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境）
- **模型路径**: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`（8B），4B 路径类似
- **Checkpoint 目录**: `/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/`（seed123），`/root/autodl-tmp/checkpoints_repo_cls_8b_conda/`（s42）
- **数据**: `/home/sonny/exec-sim-repair-verifier/data/`，37338 条
- **HF_HOME**: `/root/autodl-tmp/.hf_cache`
- **活跃进程**:
  - CWM 8B v4: PID 266816, westd cuda:2, step ~3225/6633 (~49%)
  - CLS 8B s42 resume: PID 295794, westd cuda:1
- **活跃 cron**: repo-level-cwm-8b-conda-v4, repo-level-cls-8b-s42-resume

### 3. 📊 当前状态
刚收到 `repo-level-cls-8b-seed123-conda-v3` 失败回调（EXIT_CODE=129/SIGHUP，step 6092/6633，91.8%）。已有 checkpoint-6000。已派 Worker `worker_diagnose_repo-level-cls-8b-seed123-conda-v3_20260515T062544` SSH 诊断，**尚未回调**。

**Registry 摘要**（99 实验）:
- RUNNING: `repo-level-cwm-8b-conda-v4`（CWM 8B 训练 ~49%），`repo-level-cls-8b-s42-resume`（CLS 8B s42 继续训练）
- PREPARING: `cls8b-s42-ckpt1600-test8192-eval`，`cls8b-ckpt3000-test-eval`，`cls8b-ckpt3000-test-v2`，`repo-level-cls-8b-s42-ckpt200-val`
- QUEUED: `cls4b-v5-val-sweep-ckpt4600`
- DONE: 92 个（55 success, 3 negative, 23 failed, 11 killed）

**等待中**:
- 诊断 Worker 回调（上述）
- CWM 8B v4 cron 回调（~49%，预计还需 ~12 小时）
- CLS 8B s42 resume cron 回调

### 4. 📋 待办（条件触发式）
- 诊断 Worker 回调 → 确认 checkpoint-6000 完整 → 在 westd cuda:3 提交 resume from checkpoint-6000（剩余 ~633 steps）→ 更新 registry 为新实验 `repo-level-cls-8b-seed123-conda-v4`
- westd cuda:0 空闲 → 立即提交 `cls8b-s42-ckpt1600-test8192-eval`（test sweep 最后一个数据点）
- home cuda:0 空闲 → 立即提交 `cls4b-v5-val-sweep-ckpt4600`（4B val-best 确认）
- CLS 8B seed123 训练完成 → val sweep (ckpt-5400/5600/5800/6000/6200/6400/6600) → val-best test eval
- CWM 8B v4 训练完成 → CWM 8B test eval → 锁定 8B-8B CLS-CWM gap（论文核心数字）
- CLS 8B s42 resume 完成 → ckpt-1600 test 数据补全
- **⚠️ 两张 GPU 空闲（westd cuda:0, home cuda:0）= 失职**，下一轮 BOOT 后必须立刻填满

### 5. 🎯 战略上下文
- **DDL**: EMNLP 2026 ARR May 25，剩余 **10 天**
- **核心方向**: Task reformulation — execution simulation 从 generation → classification。核心假设：CLS 优势随代码复杂度增长
- **C1 (Complexity-Dependent Advantage)**: 极度稳固。Function-level gap 2.43pp (8B, p=0.008)；Repo-level gap 25.48pp (CLS 83.52% vs CWM 58.04%)。CWM 8B 训练中，完成后锁 8B-8B gap
- **C2/C3**: 已完成
- **D088 headline**: val-selected ckpt-1000, val=88.23%, test=83.52%。Test-best=ckpt-1400 (85.47%) 放 supplementary
- **易错点**:
  - seed123 训练已失败 3 次（v1/v2/v3），都是环境或 resume 问题，不是算法问题。这次 SIGHUP 可能是 SSH 断连或系统 kill，checkpoint-6000 大概率可用
  - 4B val-best 可能是 ckpt-4600 (90.07%)，但 test eval 还没跑，不要提前写入论文
  - CWM parseable-only acc 仅 42-43%，38% "正确" 来自 unparseable 默认归类巧合（D082）——这是论文关键论据
  - val/test 分布有系统性差异（D087: problem 零重叠 + mutation type 剧变），用 val-selected 是 ML 社区规范但必须在 supplementary 讨论


---
