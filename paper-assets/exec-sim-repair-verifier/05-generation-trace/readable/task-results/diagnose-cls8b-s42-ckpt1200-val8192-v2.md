# diagnose cls8b s42 ckpt1200 val8192 v2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cls8b-s42-ckpt1200-val8192-v2_20260515T022203_result.json`
- **Structured JSON:** [`977b839998beedec6918.json`](../../sessions/97/977b839998beedec6918.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. v2 日志 (PID 316307)
日志**无 traceback/错误信息**，在 sample 740/9335 处（10:10:32）干净地中断。这是典型的被 OOM kill 的特征——内核直接杀进程，Python 来不及输出异常。

### 2. cuda:0 当前状态
**被 PID 316940 占用**（19,234 MiB / 32,607 MiB）：

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| 0 | 19,243 / 32,607 MiB | 55% | PID 316940 — eval_repo_cls (ckpt-1200 val eval) |
| 1 | 27,313 / 32,607 MiB | 86% | PID 295794 — train_repo_verifier (cls 8b s42 resume) |
| 2 | 30,733 / 32,607 MiB | 98% | PID 266816 — train_repo_cwm (cwm 8b conda) |
| 3 | 30,913 / 32,607 MiB | 71% | PID 266449 — train_repo_verifier (cls 8b seed123) |

### 3. PID 316940 状态
**存活且正常运行中**。已处理到 3780/9335（running_acc=87.8%），预计还需 ~20 分钟完成。

### 4. tmux sessions
从 ps aux 可见一个残留 tmux session: `eval_cwm_seed123`（PID 194398，5月14日创建）。

### 5. 诊断结论

**根因：eval 进程（PID 316940）与 v2 进程（PID 316307）在 cuda:0 上发生显存冲突。**

时间线：
- **10:07:56** — v2 启动，加载 8B 模型到 cuda:0（~19GB）
- **10:10:32** — v2 最后一条日志（sample 740）
- **10:10:46** — eval (PID 316940) 在同一 cuda:0 上启动，开始加载同一 8B 模型
- **10:10:49~10:10:57** — eval 模型加载，cuda:0 显存需求瞬间翻倍（~38GB > 32GB 上限）
- v2 被 OOM kill，eval 存活（后启动的进程加载完成后独占 GPU）

这与 v1 的失败模式完全一致（v1 也是 cuda:0 被其他进程占用 18.21 GiB 导致 OOM）。两次失败本质上都是**同一 GPU 上并发启动了两个 8B 模型推理任务**。

**当前状态**：eval (PID 316940) 正在正常运行，就是 v2 的同一任务（同 checkpoint、同 split、同参数），无需重跑。等它跑完即可拿到结果。

---
