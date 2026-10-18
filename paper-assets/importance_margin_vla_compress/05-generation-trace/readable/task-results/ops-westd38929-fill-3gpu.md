# ops westd38929 fill 3gpu

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-fill-3gpu_20260521T052520_result.json`
- **Structured JSON:** [`348e77f8e1e53292854e.json`](../../sessions/34/348e77f8e1e53292854e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**所有 4 块 GPU 都在跑，没有空闲 GPU。** 当前状态：

| GPU | PID | 任务 | 进度 | 速度 |
|-----|-----|------|------|------|
| cuda:0 | 568225 | L2norm k=0.5 Object seed42 | Task 1/10, Ep 30/50 | ~1.5-1.9 eps/min |
| cuda:0 | 596599 | test_math_eval.py (临时测试) | 刚启动 | — |
| cuda:1 | 568905 | Random k=0.3 Object seed42 | Task 1/10, Ep 30/50 | ~1.4 eps/min |
| cuda:2 | 569611 | L2norm k=0.7 Object seed42 | Task 1/10, Ep 30/50 | ~1.5-1.6 eps/min |
| cuda:3 | 570309 | L2norm k=0.3 Object seed42 | Task 1/10, Ep 30/50 | ~1.5 eps/min |

这 4 个 eval 都是约 20 分钟前启动的（日志时间 13:22-13:24），每个要跑 10 tasks × 50 episodes = 500 episodes，按 1.5 eps/min 预估还需 ~5 小时。

另外 GPU 0 上还多了一个 `test_math_eval.py` 临时测试脚本（PID 596599），可能是另一个 agent 启动的，和 L2norm k=0.5 共享 GPU 0（各占 ~16GB，96GB 显存够用）。

**无需再启动新任务。** 你计划中的 3 个实验已经被覆盖了（random k=0.3、l2norm k=0.3 都在跑），是否需要：
1. 等这批跑完后安排下一批？
2. kill 掉某个任务换成别的？
3. kill `test_math_eval.py` 释放 GPU 0 资源？

---
