# gpu advbench heuristic cp sweep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_advbench_heuristic_cp_sweep_20260520T022513_result.json`
- **Structured JSON:** [`68910c68c40305d67075.json`](../../sessions/68/68910c68c40305d67075.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifacts registered. Here are the results:

---

## AdvBench Preliminary Layer Sweep (Pseudo-CP, DeepSeek-R1-Distill-Qwen-8B)

**Setup**: 387 B-class traces, heuristic CP (max cosine dist in text embeddings), L0–L24 × W={1,3,5,15}, PCA→100d, LR(C=1.0, balanced), 60/20/20 split, seed=42

### 各 metric 最优层选择 (HS):

| Metric | W=1 | W=3 | W=5 | W=15 |
|--------|-----|-----|-----|------|
| bal_acc | **L21** (0.763) | **L10** (0.775) | **L23** (0.778) | **L19** (0.776) |
| precision | **L8** (0.690) | **L10** (0.698) | **L0** (0.706) | **L0** (0.759) |
| fpr | **L8** (0.167) | **L0** (0.082) | **L0** (0.099) | **L0** (0.113) |
| crossing_rate | **L0**† (0.974) | **L20** (0.462) | **L19** (0.462) | **L9** (0.474) |
| composite | **L0**† (0.450) | **L20** (0.353) | **L19** (0.355) | **L10** (0.363) |

### Bootstrap 95% CI (overall best per metric):

| Metric | Best config | Point est. | Bootstrap mean [95% CI] |
|--------|------------|------------|------------------------|
| bal_acc | L23 W5 | 0.778 | 0.787 [0.743, 0.824] |
| precision | L0 W15 | 0.759 | 0.765 [0.680, 0.840] |
| fpr | L0 W3 | 0.082 | 0.082 [0.053, 0.112] |
| crossing_rate | L0 W1† | 0.974 | 0.002 [0.000, 0.013] |
| composite | L0 W1† | 0.450 | 0.001 [0.000, 0.007] |

†L0 W1 is **degenerate**: ba=0.462 (below chance), fpr=0.917 — the model predicts class 1 almost everywhere, inflating crossing_rate. Bootstrap correctly exposes this as unstable.

### 核心问题

**CR 是否选 shallow?** 表面上 W=1 选 L0，但这是退化解（ba < chance）。排除 L0 W1 后，CR 选 **mid-deep**: L20 (W3), L19 (W5), L9 (W15)。与 HarmThoughts 的 shallow bias 不同。

**Precision 是否选 deep?** **否** — precision 选 shallow: L0 (W5, W15) 和 L8/L10 (W1, W3)。FPR 同样选 L0/L8。这与 HarmThoughts 的 pattern 反转。

**Ba 是否选 deep?** **是** — ba 一致选 mid-to-deep: L21 (W1), L10 (W3), L23 (W5), L19 (W15)。Bootstrap CI [0.743, 0.824] 表明 L23 W5 的 0.778 是 robust 的。

**关键差异 vs HarmThoughts**: AdvBench pseudo-CP 的 precision/FPR 偏好 shallow (L0)，而 ba 偏好 deep。这可能反映 pseudo-CP 标签噪声大（heuristic max cosine dist），shallow 层的 embedding 结构恰好与 text-level 的 embedding 变化更相关。

---
