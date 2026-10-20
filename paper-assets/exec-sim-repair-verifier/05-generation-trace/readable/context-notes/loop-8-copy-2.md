# agent / loop_8.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`5ab90eba63c0c6dfd587.json`](../../sessions/5a/5ab90eba63c0c6dfd587.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-14T08:25:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: westd-48478 cuda:0/1/2/3，home cuda:0。不可用其他设备
- **CWM v11 数字已废止 (D057)**：66.6% 不可引用于论文，必须用 v12 全量 eval 结果替代
- **D063 方法论红线**: 所有 checkpoint 选择必须在 val set (9335 samples) 上做，test set (9784) 只报最终数字。当前 ROADMAP 中所有 repo-level CLS accuracy 数字（81.51/78.43/80.73/84.52）均在 test set 上选的 checkpoint，**需要 val set 重跑后可能变化**，引用时必须标注
- **8B 训练未注册 cron**：repo-level-cls-8b-seed123-conda (PID 210652) 和 repo-level-cwm-8b-conda (PID 210568) 是 RUNNING 但 poll_cron 报 "No cron registered"。下一个你接手后**首先注册 cron**，否则训练完成无回调
- **apple-to-apple 对比只能用 westd conda 环境数据**（CLS vs CWM 同 server/env/data），home 环境数字不能直接与 westd 对比

### 2. 🖥️ 基础设施快照
- **westd-48478** (4×RTX 5090): 工作目录 `/home/sonny/exec-sim-repair-verifier`，Python `/root/miniconda3/bin/python`，conda base 环境（transformers 4.57.6）
- **home-1x5090**: 工作目录 `/home/sonny/exec-sim-repair-verifier`，同 conda env
- 模型: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/` (8B), Qwen3-4B (4B)
- Checkpoints: `/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/`, `/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/` 等
- **活跃进程 (westd)**:
  - cuda:0: CWM seed123 eval PID 195531（~25% done, ETA ~02:30 UTC May 15）— cron 存在但 registry=killed
  - cuda:1: CWM v12 eval PID 195668（~25% done, ETA ~02:20 UTC May 15）— cron 存在但 registry=killed
  - cuda:2: 8B CWM 训练 PID 210568, tmux=repo-level-cwm-8b-conda — **无 cron**
  - cuda:3: 8B CLS seed123 训练 PID 210652, tmux=repo-level-cls-8b-seed123-conda — **无 cron**
- **Worker 池**: 0（之前派发的 D063 val sweep worker 已完成或消失）

### 3. 📊 当前状态
- Registry: 59 DONE, 2 RUNNING
- **刚完成**: D056 early stop 5 个 repo-level 训练 → 启动 eval pipeline；D061 启动 8B 训练；D062 改用 F1_macro 选 checkpoint；D063 发现 test set cherry-picking 问题需 val set 修复；D064 部分解除论文阻塞
- **正在跑**: 8B CWM/CLS 训练 (westd cuda:2/3)；CWM v12/seed123 全量 eval (westd cuda:0/1, ~25%)
- **等待中**:
  - CWM v12 + seed123 eval 完成（ETA ~02:20-02:30 UTC May 15）→ 解除 D057 论文阻塞，获得最终 CLS-CWM gap
  - D063 val set checkpoint sweep 结果 → 所有 CLS repo-level 数字需要更新
  - 8B 训练完成 → 8B eval pipeline
  - **Paper Agent Full Draft (D064)** 已部分启动，等 CWM 最终数字

### 4. 📋 待办（条件触发式）
- **CWM v12/seed123 eval cron 回调到达** → spawn worker 提取最终 accuracy/F1 → update_registry → 计算 CLS-CWM gap → 汇报 Director（这是 D057 解除条件）
- **D063 val sweep 完成** → 用 val set 选出的 best checkpoint 在 test set 做最终 eval → 更新 ROADMAP 中所有 repo-level 数字 → Paper Agent patch
- **8B 训练完成** → spawn worker 做 8B checkpoint sweep（val set 选 → test set 报）→ 8B CLS-CWM gap
- **所有 eval 完成** → 最终数字汇总 → Paper Agent 完成 full draft → Reviewer 审查
- **CWM eval 最终 acc < majority baseline (72.96%)** → 已预期（running acc 57-58%），强化 C1 complexity-dependent advantage narrative，不需要 framing 调整

### 5. 🎯 战略上下文
- **EMNLP ARR May 25 = 剩 11 天**，DDL 紧迫
- **核心 story**: CLS vs CWM 在简单代码上等价，但 CLS 随复杂度增长优势放大。函数级 gap 1.24pp (4B) / 2.43pp (8B)；repo-level gap 预估 20-27pp（CLS 78-84% vs CWM 57-58%）
- **C1 极度稳固**，C2 (TOST p=0.007) 和 C3 (accuracy-utility frontier) 已完成
- **最大风险**: D063 val set 重选 checkpoint 后 CLS 数字可能下降——但 CWM 57-58% 远低于 majority baseline，gap 仍会很大
- **易错点**:
  - 不要把 CWM v11 (66.6%, 500 样本) 和 v12 全量 eval 混淆——v11 已废止
  - home vs westd 数字不可直接对比（环境差异 3-22pp）
  - 8B 过拟合极快（ckpt-400 后退化），checkpoint sweep 必须覆盖早期 checkpoint
  - CWM eval 每样本 ~6.5s，全量 9784 样本 ~18h，不要低估 ETA
- **决策链**: D046(超参修正) → D054(conda 重训) → D056(early stop+eval) → D057(CWM 阻塞论文) → D061(8B 训练) → D062(F1_macro 选 ckpt) → D063(val set 修复) → D064(论文部分解除阻塞)


---
