# analysis w1 cf fallback scierc pilot

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w1_cf_fallback_scierc_pilot_20260515T144938_result.json`
- **Structured JSON:** [`362ddca1e05402cb3f7a.json`](../../sessions/36/362ddca1e05402cb3f7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。总结：

## w1_cf_fallback_scierc_pilot — **NEGATIVE**

| 指标 | Pilot | Baseline (full_s1) | Δ | 判定 |
|------|-------|--------------------|----|------|
| DR | **14.78%** | 0.93% | +13.85pp | **✗** |
| CF | **0.04%** | 9.90% | -9.86pp | ✓ |
| R-F1 | 8.23% | 8.36% | -0.13pp | ✓ |
| E-F1 | 30.98% | 30.98% | 0.00pp | ✓ |

**核心问题**：Fallback 触发率过高（41.12% 的 mask calls），模型实质退化为 unconstrained 行为。CF violations 确实被消除，但代价是 DR violations 从 0.93% 飙升到 14.78%（与 unconstrained baseline 的 15.37% 几乎一致）。违反没有减少，只是从 CF 转移到了 DR，总违反预算还增加了 3.99pp。

**W1 改进方向**：当前的 grammar-first 全量回退太粗暴，应改为仅放松 CF mask 而保留 DR enforcement 的 partial relaxation 方案。

---
