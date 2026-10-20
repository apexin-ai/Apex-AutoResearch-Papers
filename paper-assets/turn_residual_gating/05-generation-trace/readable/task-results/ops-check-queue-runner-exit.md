# ops check queue runner exit

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_queue_runner_exit_20260522T232511_result.json`
- **Structured JSON:** [`9e1313a5e808f3d2e1d5.json`](../../sessions/9e/9e1313a5e808f3d2e1d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 利用率 72%，21GB 显存占用 — 进程正常运行中，没有卡住。

## 汇报

**queue_runner 没有退出，仍在正常运行。**

### 当前执行进度
- **Item [1/8] SS s42** — 跳过（已完成）
- **Item [2/8] AR N=50 existing s42 checkpoints** — 正在执行
  - [1/4] TG s42 AR N=50 — **完成** ✓
    - Beta=0.0: Mid-GAR=0.0280, PPL=1.41
    - Beta=3.0: Mid-GAR=0.5374, PPL=1.55
    - Beta=5.0: Mid-GAR=0.6795, PPL=1.91
    - 结果保存到 `results/d048_ar_n50_existing/tg_s42_ar_n50.json`
  - [2/4] UG s42 AR N=50 — **正在运行**（模型已加载，生成中）
  - [3/4] 和 [4/4] 待执行
- **Items [3-8]** — 排队中

### GPU 状态
- 利用率 72%，显存 21GB / 98GB — 正常工作
- PID 51492 活跃

### 结论
不需要干预，queue_runner 在 tmux 里按计划串行执行。无 OOM、无 CUDA error、无 traceback。

---
