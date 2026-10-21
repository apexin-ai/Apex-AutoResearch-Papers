# analysis eval pi05 l2norm k085 long seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_l2norm_k085_long_seed42_v3_20260526T175110_result.json`
- **Structured JSON:** [`6c750c578dfc89c7f666.json`](../../sessions/6c/6c750c578dfc89c7f666.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 结果汇总

**overall SR = 78.8%** (394/500)

### Per-task SR

| Task | SR |
|---|---|
| T0 alphabet soup + tomato | 98% |
| T1 cream cheese + butter | 94% |
| T2 stove + moka pot | 88% |
| T3 black bowl → drawer | 98% |
| T4 white mug → left plate | 72% |
| T5 book → back | 98% |
| T6 white mug → plate (hard) | 6% |
| T7 alphabet soup + cream | 86% |
| T8 moka pots → stove | 54% |
| T9 yellow mug → microwave | 94% |

### L2norm Long 单调曲线验证

| keep_ratio | SR | Δ to next |
|---|---|---|
| 0.95 | 87.0% | — |
| 0.90 | 81.0% | −6.0 |
| **0.85** | **78.8%** | **−2.2** |
| 0.75 | 73.4% | −5.4 |
| 0.50 | 50.0% | −23.4 |
| 0.30 | ~23% | −27 |

**单调性完美保持**：78.8% 落在 81%（k=0.9）和 73.4%（k=0.75）之间。

值得注意的是 k=0.9→0.85 的降幅仅 2.2pp，明显小于 k=0.95→0.9 的 6.0pp 和 k=0.85→0.75 的 5.4pp。这表明 L2norm 在 k=0.85~0.90 区间退化特别平缓，存在一个"肩部"（shoulder），而非完美线性下降。这进一步支持 D237 的 position encoding sensitivity 假设——L2norm 按 norm 大小剪枝时，中等重要性的 token 贡献较为均匀，移除少量不会引发 cliff。

---
