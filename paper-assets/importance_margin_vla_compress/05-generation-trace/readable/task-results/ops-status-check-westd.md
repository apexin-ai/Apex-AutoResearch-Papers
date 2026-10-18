# ops status check westd

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status_check_westd_20260517T164409_result.json`
- **Structured JSON:** [`35af47b136187008e5e3.json`](../../sessions/35/35af47b136187008e5e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

**进程状态：ALIVE**
- PID 643978 运行中，已运行 ~60 分钟
- 命令：`python -u eval_openvla_libero.py --mode baseline --suite libero_object --num_episodes 50 --seed 7`

**GPU 占用：**
- GPU 0：RTX PRO 6000，16016MiB / 97887MiB，72% 利用率，python 进程在跑
- GPU 1：空闲

**当前进度：**
- 任务：libero_object，10 tasks × 50 episodes = 500 total
- 已完成 Task 1-2，Task 3 进行中（约到 ep 30）
- 速度：~2.2-2.3 eps/min
- 已完成 task SR：
  - Task 1 (alphabet soup): **0.780** (39/50)
  - Task 2 (cream cheese): **0.800** (40/50)
  - Task 3 (salad dressing): 进行中，26/30 暂时

**预估剩余时间：** 已完成约 130/500 episodes，剩余 ~370 eps ÷ 2.2 eps/min ≈ 168 min（~2.8 小时）

**eval_results/ 目录：** 大量已有结果 JSON（来自之前的 eval runs），当前这次 seed 7 的 baseline eval 尚未输出最终 JSON（还在跑）。

---
