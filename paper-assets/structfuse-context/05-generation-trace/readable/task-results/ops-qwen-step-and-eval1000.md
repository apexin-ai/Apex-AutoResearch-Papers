# ops qwen step and eval1000

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qwen-step-and-eval1000_20260515T212422_result.json`
- **Structured JSON:** [`a0784be7fef85bccd93d.json`](../../sessions/a0/a0784be7fef85bccd93d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## dataflow_s43 训练状态报告

### 1. PID 337267
**存活**（bash wrapper，sleeping）。实际训练子进程为 **PID 18427**（python train.py），运行 5h 33m，CPU 99.6%。

### 2. 当前 step
**step 1000 / 2810**（35.6%）。日志最后一行：`step 1000 loss=0.4353 lr=1.63e-05`

### 3. eval@1000
**尚未出结果**。日志自 05:22 CST 起未更新（~8 min），推断 eval@1000 + save@1000 正在执行中。

上一次 eval 结果 (eval@500)：
| 指标 | 值 |
|------|------|
| val_loss | **0.4617** |
| R@1 | **0.5495** |
| R@5 | 0.9728 |
| R@10 | 1.0 |

### 4. 训练速率
**~182 steps/h**（1000 steps / 5.48h，含 eval@500 暂停时间）。**比之前的 ~230 steps/h 慢了 21%。**

原因：GPU 0 上有新的竞争进程——**PID 61328**（`eval_swebench.py` 评估 random_s42_100 checkpoint），占用 **11614 MiB**，已运行 2h 41m。这不是之前 kill 的 PID 94874，而是一个新启动的 swebench eval。

### 5. GPU 状态
| GPU | 利用率 | 显存占用 | 进程 |
|-----|--------|----------|------|
| 0 | 100% | 62620 / 97887 MiB | PID 18427 训练 (50992 MiB) + PID 61328 swebench eval (11614 MiB) |
| 1 | 100% | 54767 / 97887 MiB | PID 38016 starcoder训练 (54758 MiB) |

### 6. ETA 估算

| 阶段 | 剩余 steps | 预计耗时 | 预计完成 (CST) |
|------|-----------|----------|---------------|
| dataflow_s43 (5/7) | 1810 | ~10.7h | May 16 ~16:00 |
| dataflow_s44 (6/7) | 2810 | ~16h | May 17 ~08:00 |
| bm25_s42 (7/7) | 2810 | ~16h | May 18 ~00:00 |

**整链完成：约 May 18 00:00 CST（~43h 后）**

---

**注意**：GPU 0 上的 swebench eval（PID 61328）正在拖慢训练。如果 kill 掉它，速率有望恢复到 230+ steps/h，整链 ETA 可提前约 8-10 小时。是否需要处理？

---
