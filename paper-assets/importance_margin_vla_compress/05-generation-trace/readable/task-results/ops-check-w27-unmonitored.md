# ops check w27 unmonitored

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-w27-unmonitored_20260527T210705_result.json`
- **Structured JSON:** [`663ba9ed652ed9f74bef.json`](../../sessions/66/663ba9ed652ed9f74bef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
实验: eval_pi05_attn_k085_long_seed43_strict_w27_v2
状态: running
PID: 64834 (GPU 0, cuda:0)
进度: Task 9 ep 20/50 (最后一个 task)
已完成 tasks: T0-T8, 累计 217/450=48.2%
T9 当前: 17/20=85%
预计剩余: ~8 min (基于 ~2.7min/10eps)

实验: eval_pi05_attn_k075_long_seed43_strict_w27_v2
状态: running
PID: 64908 (GPU 1, cuda:1)
进度: Task 9 ep 30/50 (最后一个 task)
已完成 tasks: T0-T8, 累计 207/450=46.0%
T9 当前: 26/30=87%
预计剩余: ~5 min (基于 ~2.5min/10eps)
```

两个实验都即将完成（比预计的 21:xx UTC 提前很多），k075 约 05:11 UTC 结束，k085 约 05:14 UTC 结束。

已完成 task 汇总：

| Task | k085 | k075 |
|------|------|------|
| T0-T3 | (未在尾部显示，累计到 T3 末应为 ~94/200) | (累计到 T3 末应为 ~109/200) |
| T4 | 23/50=46% | 16/50=32% |
| T5 | 35/50=70% | 24/50=48% |
| T6 | 36/50=72% | 38/50=76% |
| T7 | 27/50=54% | 13/50=26% |
| T8 | 2/50=4% | 7/50=14% |
| T9 | 进行中 (17/20 暂 85%) | 进行中 (26/30 暂 87%) |

---
