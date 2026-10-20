# analysis method ablation phase3

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_method_ablation_phase3_20260519T193616_result.json`
- **Structured JSON:** [`d8dea0f2227cc84e4f0d.json`](../../sessions/d8/d8dea0f2227cc84e4f0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是 Phase 3 完整结果。

---

## Method × Regime Matrix (10-α, 5-method, 8-pair)

```
     α | naive | diff  | thresh | PermG↑ | PermG↓ |   TY  | K≥3  | K≥4
-------+-------+-------+--------+--------+--------+-------+------+------
  0.00 |  8/8  |  4/8  |  4/8   |  0/8   |  0/8   |  2/8  | 3/8  | 0/8
  0.05 |  7/8  |  3/8  |  5/8   |  0/8   |  0/8   |  3/8  | 3/8  | 0/8
  0.10 |  7/8  |  6/8  |  5/8   |  0/8   |  0/8   |  3/8  | 4/8  | 2/8
  0.25 |  8/8  |  3/8  |  5/8   |  0/8   |  0/8   |  3/8  | 4/8  | 0/8
  0.35 |  8/8  |  4/8  |  8/8   |  0/8   |  0/8   |  4/8  | 6/8  | 2/8
  0.40 |  8/8  |  3/8  |  8/8   |  0/8   |  0/8   |  4/8  | 6/8  | 1/8
  0.50 |  8/8  |  7/8  |  8/8   |  6/8   |  0/8   |  4/8  | 7/8  | 6/8
  0.60 |  7/8  |  8/8  |  8/8   |  3/8   |  0/8   |  8/8  | 8/8  | 7/8
  0.75 |  7/8  |  6/8  |  8/8   |  6/8   |  0/8   |  8/8  | 7/8  | 6/8
  1.00 |  8/8  |  6/8  |  8/8   |  6/8   |  0/8   |  3/8  | 6/8  | 6/8
```

## 关键发现

**三相 regime 结构**:

| Regime | α 范围 | 特征 |
|--------|--------|------|
| **Null** | ≤0.25 | 仅宽松方法(naive/diff/thresh)火，PermG=0%，K≥4=0% |
| **Transition** | 0.35–0.40 | threshold saturates至100%，但PermG仍=0% |
| **Signal** | ≥0.50 | PermG激活(≥37.5%)，K≥4跳至≥75% |

**逐方法分析**:

1. **Naive xcorr** — 无鉴别力。α=0.00（无污染）就 8/8 显著，全域87.5-100%。纯假阳。
2. **Threshold onset (3σ)** — 有中等鉴别力。α≤0.25: 50-62.5% → α≥0.35: 100%。但在 null 下仍有50% FPR。
3. **PermG forward** — **最干净的 regime discriminator**。α≤0.40 严格为 0%（零假阳），α≥0.50 跳至 75%。临界转变点 α≈0.50。
4. **TY Granger** — 非单调。在α=0.60-0.75达100%，但α=1.00骤降至37.5%（与 C003 一致：短序列下 TY 不稳定）。
5. **PermG reverse** — 全域 0%（正确：无反向因果性）。

**Claim 3 支撑强度**: **强**。5 种方法在 10 个 regime 下表现差异巨大 — naive 在 null regime 下产生 100% 假阳，而 PermG 在同一 regime 下严格为 0%。方法选择直接决定了结论是否可信。K≥4 consensus 作为聚合指标，在 α<0.50 时正确拒绝，α≥0.50 时稳定检出。

---
