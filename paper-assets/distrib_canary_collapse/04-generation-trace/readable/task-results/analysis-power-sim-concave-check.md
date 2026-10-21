# analysis power sim concave check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_power-sim-concave-check_20260522T110413_result.json`
- **Structured JSON:** [`4783f84a8a4f15f00e19.json`](../../sessions/47/4783f84a8a4f15f00e19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。**关键发现与预期不符：**

| Model | γ | Δγ from observed |
|-------|------|-----------------|
| H0 linear (k=1) | 0.85 | 1.24 |
| **H0' concave (k=0.5)** | **1.87** | **0.21** |
| H1 step | 1.96 | 0.12 |
| Observed | 2.08 | — |

**γ_H0' = 1.87，不是预期的 ≈1.0。** 凹信号函数 S(α) = c·α^{0.5} 几乎复现了观测到的 onset scaling（Δγ = 0.21）。原因：α^{0.5} 在低 α 处信号集中度远高于线性（α=0.10 时 H0' 的 b 是 H0 的 2.7×），使得 onset 随 T 的下移幅度接近 step function。

结论从 `real_transition` 变为 `artifact_possible`。这意味着：
1. 单纯用 γ scaling exponent 区分 artifact vs real transition 不够——凹信号也能产生大 γ
2. 需要用 **定性特征**（H1 的 0→1 detection cliff vs H0'/H0 的 gradual ramp）来区分，而非仅靠 γ 值
3. reviewer_note 已更新反映实际结果

---
