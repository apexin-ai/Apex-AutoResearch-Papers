# ops openvla prune seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_openvla-prune-seed43_20260520T111133_result.json`
- **Structured JSON:** [`3f8f6602a2bdc37450ef.json`](../../sessions/3f/3f8f6602a2bdc37450ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已启动，k=0.9 开始运行中。

**状态**：
- PID=924085，GPU 0 上运行
- 当前执行 k=0.9（第一个），之后依次跑 k=0.7、k=0.5
- 模型已加载（15.1 GB），正在 libero_object 10 tasks × 50 episodes = 500 episodes
- 日志：`eval_results/openvla_prune_seed43_sweep.log`
- 结果输出：`openvla_random_prune_k0_9_seed43_object.json` / `k0_7` / `k0_5`

查进度：`tail -20 eval_results/openvla_prune_seed43_sweep.log`

---
