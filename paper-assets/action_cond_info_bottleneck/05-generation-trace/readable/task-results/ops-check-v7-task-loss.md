# ops check v7 task loss

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-v7-task-loss_20260516T194643_result.json`
- **Structured JSON:** [`ba36ff26b1e999582401.json`](../../sessions/ba/ba36ff26b1e999582401.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全。汇总如下：

---

## v7 seed1 (acib_v7_contrastive) Task Loss

| 阶段 | Steps | task_loss 范围 | 典型值 |
|------|-------|---------------|--------|
| 初始 | 100-1000 | 0.063–0.118 | ~0.08 |
| 中期 | 10000-13000 | 0.034–0.070 | ~0.05 |
| 终态 | 19000-20000 | 0.031–0.073 | ~0.05 |

**Step 20000 终态**: task=**0.0689**, ib=0.7148, div=-0.2852, ctr=0.9063, total_loss=0.1548

## v7 seed2 对比

| 阶段 | task_loss 范围 | 典型值 |
|------|---------------|--------|
| 初始 (100-1000) | 0.073–0.134 | ~0.10 |
| 终态 (19000-20000) | 0.030–0.072 | ~0.05 |

**Step 20000 终态**: task=**0.0516**, ib=0.8530, div=-0.2383, ctr=0.8639, total_loss=0.1352

## 趋势判断

- **task_loss 单调下降**：从初始 ~0.08-0.10 降到终态 ~0.05，训练在持续学习 task
- **task_loss 没有异常偏高**：终态 0.05-0.07 是正常的微调 loss 水平
- **两个 seed 一致**：seed1 和 seed2 的 task_loss 轨迹几乎相同

## 关键结论

**auxiliary losses 没有破坏 task learning。** task_loss 正常下降到低水平，排除了"辅助损失挤占 task 梯度"的假设。

SR 回退 ~21pp 的原因不是 task_loss 过高，而更可能是：IB bottleneck（ib ~0.71-0.85）和 contrastive loss 改变了表征结构，虽然训练 loss 看起来正常，但泛化到 eval 时的 action 执行质量下降——典型的 train-eval gap，不是训练失败。

---
