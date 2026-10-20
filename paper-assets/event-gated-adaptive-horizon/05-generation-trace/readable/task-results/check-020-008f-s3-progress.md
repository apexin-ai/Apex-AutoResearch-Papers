# check 020 008f s3 progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_020-008f_s3-progress_20260516T192916_result.json`
- **Structured JSON:** [`008033158561b06d42b0.json`](../../sessions/00/008033158561b06d42b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果：

## exp_020_vanilla_dreamerv3_s2

```
step=5000   eval_return=41.21   train_return=None
step=15000  eval_return=106.01  train_return=None
step=25000  eval_return=325.33  train_return=None
step=35000  eval_return=354.49  train_return=None
step=45000  eval_return=498.01  train_return=None
step=55000  eval_return=534.13  train_return=None
step=65000  eval_return=688.87  train_return=None
step=75000  eval_return=656.85  train_return=None
step=85000  eval_return=618.73  train_return=None
step=95000  eval_return=596.24  train_return=None
step=105000 eval_return=836.51  train_return=None
```

## exp_008f_s3_no_dt_embed_walker

```
step=5000   eval_return=33.83   value_mean=None
step=15000  eval_return=108.50  value_mean=None
step=25000  eval_return=184.61  value_mean=None
step=35000  eval_return=199.24  value_mean=None
step=45000  eval_return=219.08  value_mean=None
step=55000  eval_return=253.74  value_mean=None
step=65000  eval_return=281.43  value_mean=None
step=75000  eval_return=502.17  value_mean=None
```

## 进程状态

```
PID     ELAPSED    %CPU
596344  02:43:57   0.0
601233  02:08:28   0.0
```

## 分析

**exp_020 collapse 问题：** 75K→95K 区间确实出现下滑（688→656→618→596），模式与 008e_v3_s2 在 85K 崩溃类似。但关键区别——**105K 回弹到 836.51**，创新高。这不是 008e 那种一路崩到 137 的不可逆 collapse，更像是训练中的正常波动/探索噪声。目前看 020 是健康的。

**exp_008f_s3：** 稳步上升中，75K 刚突破 502。value_mean 字段在 metrics.jsonl 中未记录（全为 None），无法计算 ve_ratio。

**进程：** 两个都在跑但 CPU 0.0%——可能是 GPU-bound 阶段或刚完成一个 eval 在等下一轮。

---
