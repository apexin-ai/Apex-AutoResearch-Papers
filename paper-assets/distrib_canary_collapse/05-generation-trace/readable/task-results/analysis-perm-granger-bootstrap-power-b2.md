# analysis perm granger bootstrap power b2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_perm_granger_bootstrap_power_b2_20260516T063530_result.json`
- **Structured JSON:** [`300076d8979794edc2a5.json`](../../sessions/30/300076d8979794edc2a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**Permutation Granger Bootstrap Power (T=10, B=1000)**

| Pair | Power | Median p |
|------|-------|----------|
| token_entropy → distinct_1/2/3 | **1.0** | 0.001–0.007 |
| ece → distinct_1/2/3 | **1.0** | 0.0005–0.004 |
| canary → perplexity | 0.0 | 0.54–0.78 |

**对比 TY (plan_009)**:
- TY d_max=0: power = 0.205
- TY d_max=1: power = 0.090
- Permutation Granger: power = **1.0** (6/8 causal pairs)

Permutation Granger 在 T=10 下实现完美 power，因为：(1) 不依赖渐近 χ² 近似；(2) α=1.0 的因果信号极强（F-stat 远超 permutation null）。Perplexity 对 power=0 是预期的——它不受 canary 指标 Granger 因果驱动。

产出已注册：`art_20260516_26e905`，JSON 数据存储在 `results/perm_granger_power_bootstrap.json`。

---
