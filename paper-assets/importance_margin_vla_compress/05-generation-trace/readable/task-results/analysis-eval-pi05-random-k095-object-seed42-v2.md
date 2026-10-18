# analysis eval pi05 random k095 object seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_random_k095_object_seed42_v2_20260521T214839_result.json`
- **Structured JSON:** [`ed6a8ed85810e920bb64.json`](../../sessions/ed/ed6a8ed85810e920bb64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 分析总结

### k=0.95 结果
**SR = 69.4%** (347/500)，91.3 分钟完成，无错误。

Per-task SR:
| Task | SR |
|---|---|
| T1 cream cheese | 92% |
| T6 butter | 86% |
| T2 salad dressing | 84% |
| T8 chocolate pudding | 80% |
| T5 tomato sauce | 68% |
| T0 alphabet soup | 64% |
| T9 orange juice | 58% |
| T3 bbq sauce | 56% |
| T4 ketchup | 54% |
| T7 milk | 52% |

### Hypothesis 回答

k=0.95 的 69.4% 否定了"转折在 0.9-0.95 之间"的假设。**Cliff 从仅 5% 随机 pruning 就开始了**——baseline 98.2% 直接跌至 69.4%（-28.8pp）。

### π0.5 Random Pruning Degradation Curve（LIBERO-Object, seed42）

```
k=1.00  ████████████████████████████████████████████████  98.2%  (baseline)
k=0.95  ██████████████████████████████████                69.4%  ← 本实验
k=0.90  █████                                             12.0%  (谷底)
k=0.85  ?                                                  ?     (running)
k=0.70  █████████████████████████████████████              77.2%  (回升!)
k=0.50  ██████████████████████████████████                 69.4%
k=0.30  ██████████████████                                 36.4%
```

**关键发现**：曲线呈现极度非单调的 U 型——不是随着 pruning 增加单调下降，而是 k=0.9 是谷底，之后反弹。这说明 random pruning 的性能不取决于 pruning 量，而取决于特定 seed 下恰好保留/丢弃了哪些 token 位置。即使只随机丢 5% 的 token，如果碰到关键位置就会严重退化。

---
