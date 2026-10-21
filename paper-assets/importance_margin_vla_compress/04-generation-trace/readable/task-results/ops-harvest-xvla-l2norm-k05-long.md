# ops harvest xvla l2norm k05 long

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_xvla_l2norm_k05_long_20260523T075739_result.json`
- **Structured JSON:** [`ad03445e6bcd3e80f452.json`](../../sessions/ad/ad03445e6bcd3e80f452.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，cron 不存在（可能已被之前删除）。

## 结果：X-VLA L2norm k=0.5 Long (seed42)

**Overall SR: 45.0%** (225/500), 95% CI: [40.7%, 49.4%]

| Task | SR | Description |
|------|-----|-------------|
| 0 | 26% | alphabet soup + tomato sauce → basket |
| 1 | 0% | cream cheese + butter → basket |
| 2 | 46% | stove + moka pot |
| 3 | 82% | black bowl → drawer + close |
| 4 | 42% | white mug left plate + yellow mug right plate |
| 5 | 92% | book → caddy |
| 6 | 54% | white mug on plate + chocolate pudding |
| 7 | 70% | alphabet soup + cream cheese → basket |
| 8 | 34% | both moka pots → stove |
| 9 | 4% | mug → microwave + close |

### L2norm Long degradation curve 完整数据

| keep_ratio | SR |
|-----------|-----|
| k=0.95 | 47.0% |
| k=0.9 | 27.5% |
| k=0.7 | 49.4% |
| **k=0.5** | **45.0%** |

有趣的发现：k=0.5 (45.0%) 和 k=0.95 (47.0%) 接近，都优于 k=0.9 (27.5%)。k=0.9 的异常低值可能是 outlier 或该 ratio 恰好命中了某些关键 token。L2norm 在 Long suite 上的 degradation 不呈单调递减趋势。

---
