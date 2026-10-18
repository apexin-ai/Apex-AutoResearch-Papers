# analyze eval openvla l2norm k095 long seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_openvla_l2norm_k095_long_seed42_20260527T120425_result.json`
- **Structured JSON:** [`230893f214d7b1815c03.json`](../../sessions/23/230893f214d7b1815c03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果总结：

**OpenVLA L2norm k=0.95 Long: Overall SR = 42.6% (213/500)**

| Task | SR |
|---|---|
| 1. alphabet soup + tomato sauce → basket | 64% |
| 2. cream cheese + butter → basket | 60% |
| 3. stove + moka pot | 54% |
| 4. black bowl → drawer | 34% |
| 5. mugs → plates | 38% |
| 6. book → caddy | 70% |
| 7. mug + pudding → plate | 26% |
| 8. alphabet soup + cream cheese → basket | 50% |
| 9. both moka pots → stove | 14% |
| 10. mug → microwave | 16% |

**对比：**
- Baseline (no pruning): **52.8%** → L2norm k=0.95 下降 10.2pp
- Attn k=0.95: **49.8%** → L2norm 比 Attn 低 7.2pp
- L2norm k=0.9: **43.6%** → k=0.95 反而略低 1pp（42.6% vs 43.6%），差异在噪声范围内

L2norm 在 Long suite 上整体弱于 Attn pruning，即使只剪 5% tokens (k=0.95) 也比 baseline 掉了 10pp。L2norm curve 起始段补全完成：k=0.95→42.6%, k=0.9→43.6%, k=0.85→38.8%。

---
