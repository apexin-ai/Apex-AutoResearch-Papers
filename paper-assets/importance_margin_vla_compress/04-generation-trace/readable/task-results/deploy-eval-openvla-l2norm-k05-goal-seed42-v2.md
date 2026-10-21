# deploy eval openvla l2norm k05 goal seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_eval_openvla_l2norm_k05_goal_seed42_v2_20260526T150029_result.json`
- **Structured JSON:** [`5607bec44c697adfd8d8.json`](../../sessions/56/5607bec44c697adfd8d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:1 被 `eval_openvla_random_k05_goal_seed42_v2` 占用，当前进度 Task 1/10, Ep 20/50（~1.9 eps/min），预计还需 ~4 小时完成。cuda:0 也被占用（PID 307307, 15946 MiB）。

**无法在 cuda:1 部署新实验** — 该 GPU 正在运行一个合法的 RUNNING 状态实验 `eval_openvla_random_k05_goal_seed42_v2`，刚跑了 13 分钟，还远未完成。

选项：
1. **等 random k=0.5 goal 跑完**（~4h）后再部署 l2norm k=0.5 goal
2. **Kill 当前 random k=0.5 进程**，立即部署 l2norm k=0.5（会丢失已跑进度）
3. **检查 cuda:0 上的进程**，看是否有更适合中断的

需要确认如何处理。

---
