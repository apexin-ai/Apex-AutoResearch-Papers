# ops check stale deploy gpu1 westd41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_stale_deploy_gpu1_westd41074_20260526T133715_result.json`
- **Structured JSON:** [`c2e316ced441ce304900.json`](../../sessions/c2/c2e316ced441ce304900.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务完成。汇总：

## 任务 1: 实验状态检查

**eval_openvla_random_k085_long_seed42_v3** (GPU 0, pid=415537)
- **仍在运行**，已跑 ~9 小时，当前 Task 10/10 ep 10/50
- 已完成 9/10 tasks 的 per-task SR：66%, 56%, 66%, 34%, 22%, 78%, 20%, 66%, 30%
- 预计 ~40 分钟内完成

**eval_openvla_attn_k07_object_seed42_v2** (GPU 2, pid=415728)
- **进程已死**，在 Task 7/10 ep 10/50 处静默退出
- 日志无 error/traceback/killed，v1 也在类似位置崩溃
- 已完成 6/10 tasks 的部分结果：38%, 12%, 66%, 30%, 62%, 32% (avg ~40%)
- Registry 已更新为 DONE/failed，metrics 已记录
- **这个实验需要 v3 重跑**，两次都在 Task 6-7 崩溃，可能是 Object suite 特定 task 触发的问题

## 任务 2: 新实验部署

**eval_openvla_l2norm_k05_long_seed42** (GPU 1, pid=657544)
- 已通过 tmux session `eval_l2norm_k05_long` 启动
- 模型加载成功，L2 pruning 256→128 vision tokens (k=0.5)
- 已开始 Task 1/10 eval
- Registry 已更新为 RUNNING，含完整 spec

---
