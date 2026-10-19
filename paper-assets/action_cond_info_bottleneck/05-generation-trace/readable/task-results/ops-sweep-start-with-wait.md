# ops sweep start with wait

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sweep-start-with-wait_20260517T014353_result.json`
- **Structured JSON:** [`3b291f388ab1ee2af559.json`](../../sessions/3b/3b291f388ab1ee2af559.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

alpha=0.1 正在运行（构建 libero_spatial 环境中）。GPU 占用还没显示是因为模型还没加载到 GPU 上。

汇总：

**Eval 结果（v7_contrastive vs baseline）：**

| Suite | seed1 | seed2 | Baseline |
|-------|-------|-------|----------|
| libero_spatial | 58.4% (-7.6pp) | 51.4% (-14.6pp) | 66.0% |
| libero_object | 58.6% (-9.2pp) | 49.4% (-18.4pp) | 67.8% |
| libero_goal | 72.8% (-3.6pp) | 63.0% (-13.4pp) | 76.4% |
| libero_10 | 39.4% (-14.8pp) | NOT DONE | 54.2% |

**Alpha sweep 状态：**
- alpha=0.1：已启动在 GPU1，正在构建环境（libero_spatial task 5/10）
- alpha=0.0：等 GPU0 空闲（seed2 的 libero_10 eval 还在跑）

GPU0 空闲后我再启动 alpha=0.0。需要我设置轮询等待吗？

---
