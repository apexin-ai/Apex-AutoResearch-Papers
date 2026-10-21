# deploy westd38929 gpu123 redeploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd38929_gpu123_redeploy_20260523T010915_result.json`
- **Structured JSON:** [`3e740dd8e47e72f68937.json`](../../sessions/3e/3e740dd8e47e72f68937.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 个实验都在正常运行。GPU 1/2/3 已经被之前部署（~37分钟前），无需重新部署。

汇报结果：

### GPU 状态总览

| GPU | PID | 实验 | 运行时间 | 显存 | 状态 |
|-----|-----|------|----------|------|------|
| 0 | 209581 | Random k=0.9 seed43 | 2h43m | 10336 MiB | T8 ep20/50, 总计 420/500 = **84%** |
| 1 | 289572 | L2norm k=0.7 seed43 v2 | 37m | 9996 MiB | T2 ep30/50, 83% SR |
| 2 | 289643 | Random k=0.3 seed43 v3 | 37m | 10597 MiB | T1 ep40/50, 8% SR |
| 3 | 289780 | L2norm k=0.85 seed43 v2 | 37m | 10330 MiB | T2 ep40/50, 90% SR |

### GPU 0 进度详情
- **eval_pi05_random_k09_long_seed43**，已运行 2h43m
- Task 7 完成 (SR=50.0%)，当前 Task 8 ep 20/50
- 累计成功率 114/400 = 28.5%（前 8 个 task）
- 进度 ~84%，预计还需 ~30 分钟完成

### 结论
GPU 1/2/3 的三个实验已经在 ~37 分钟前被成功部署（带 HF_HUB_OFFLINE=1 等环境变量），且均在正常产出结果。Registry 中 v2/v3 条目状态为 RUNNING。无需重新部署。

---
