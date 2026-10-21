# analyze eval pi05 random k07 spatial seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k07_spatial_seed42_20260521T222809_result.json`
- **Structured JSON:** [`3136a81ef03493f91942.json`](../../sessions/31/3136a81ef03493f91942.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**eval_pi05_random_k07_spatial_seed42** — SR = **74.4%** (372/500), DONE/success

**Per-task**: T0=90%, T1=96%, T2=94%, T3=52%, T4=60%, T5=42%, T6=58%, T7=76%, T8=80%, T9=96%

**Cross-suite 一致性**: Random k=0.7 在 Object(75.5%) 和 Spatial(74.4%) 上仅差 1.1pp，极高一致性。

**Hypothesis 状态**: 部分验证。Random k=0.7 Spatial 数据已到位(74.4%)。完整验证（random > L2norm 是否跨 suite 成立）需等 `eval_pi05_l2norm_k07_spatial_seed42` 完成。Object 上差距为 +19.1pp (random 75.5% vs L2norm 56.4%)。

---
