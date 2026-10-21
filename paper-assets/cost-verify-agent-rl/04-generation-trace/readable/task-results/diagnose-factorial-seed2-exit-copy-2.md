# diagnose factorial seed2 exit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_factorial-seed2-exit_20260518T111245_result.json`
- **Structured JSON:** [`4222c7bd2d0602e6d459.json`](../../sessions/42/4222c7bd2d0602e6d459.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。诊断结果如下：

---

## 诊断结果：factorial_h2_episodeadv_seed2

**退出原因：** Worker 进程被信号杀死（疑似 OOM killer 或 SIGSEGV）

**时间线：**
- 18:48:11 — Ray session 启动 (PID 539852)
- 18:48:21 — TaskRunner worker (PID 546362) 启动
- 18:49:10 — W&B run 6rqnrlr7 就绪
- ~18:49 — 开始 val_before_train：134 个 ALFWorld OOD eval 环境并行初始化
- **19:00:42 — Worker 546362 崩溃 (SYSTEM_ERROR)**，导致 GPU workers 546976/546977 被 force-kill
- 19:00:43 — Driver 539852 有序关闭

**GCS server 报告的死因：**
> Worker unexpectedly exits with a connection error code 2. End of file. Common causes: (1) OOM killer, (2) ray stop --force, (3) SIGSEGV or other unexpected error.

**最终训练步数：** 0/15（卡在 val_before_train 阶段，从未开始训练）

**关键 metrics：** 无（W&B 无 metrics 数据，output.log 仅 8 行初始化信息）

**Checkpoint：** 无（空目录 `/root/autodl-tmp/checkpoints/factorial-h2-episodeadv-seed2/`）

**Log 路径：**
- TaskRunner output: `/root/autodl-tmp/tmp/ray/session_2026-05-18_18-48-11_555496_539852/logs/worker-...-546362.out`
- W&B: `/root/autodl-tmp/cost-verify-agent-rl/RAGEN/wandb/run-20260518_184910-6rqnrlr7/`
- Hydra: `/root/autodl-tmp/cost-verify-agent-rl/RAGEN/outputs/2026-05-18/18-48-11/`

**磁盘状态：** /tmp 80% (6.2G free)，TMPDIR 54% (118G free) — 非磁盘原因

**Conclusion：** **FAILED** — 这是第 2 次失败（第 1 次被误杀，本次被信号杀死）。最可能原因是 134 个 eval 环境 + 模型 + Ray 150+ worker 进程导致系统 RAM OOM。无 Python traceback 是 SIGKILL 的特征。重启时建议减少 val eval 并行度或跳过 val_before_train。

---
