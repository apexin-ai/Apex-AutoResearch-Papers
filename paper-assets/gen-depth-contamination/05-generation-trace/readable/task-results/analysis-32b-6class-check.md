# analysis 32b 6class check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_32b-6class-check_20260520T001512_result.json`
- **Structured JSON:** [`b2d22de8ef5e75cb71c7.json`](../../sessions/b2/b2d22de8ef5e75cb71c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果汇总

**K\* = 2**（1-indexed，与 5-class 一致，θ=0.60）

### Pairwise AUC 对比（6-class vs 5-class）

| Pair | 6-class AUC | 95% CI | 5-class AUC | Δ |
|------|------------|--------|-------------|------|
| 0v1 | **0.9923** | [0.9910, 0.9936] | 0.9575 | +0.0348 |
| 1v2 | **0.6945** | [0.6864, 0.7026] | 0.6183 | +0.0762 |
| 2v3 | **0.5978** | [0.5898, 0.6058] | 0.5454 | +0.0524 |
| 3v4 | **0.5669** | [0.5590, 0.5746] | — | new |
| 4v5 | **0.5426** | [0.5351, 0.5501] | — | new |

### 要点

- **K\* 不变**：6-class 下 K\*=2，与 5-class 完全一致。2v3 AUC=0.5978 刚好低于 θ=0.60 阈值，是分界点。
- **所有已有 pair AUC 均上升**：6-class 重跑后 0v1/1v2/2v3 全部比 5-class 高，可能因为 6-class 分类器在更多类别上训练提供了更好的表征。
- **Signal decay 模式清晰**：0v1 (0.992) → 1v2 (0.695) → 2v3 (0.598) → 3v4 (0.567) → 4v5 (0.543)，单调递减趋向 0.5（随机水平）。
- **4v5 F1 极低（0.26）**：几乎无法区分 depth 4 和 depth 5，AUC 也仅 0.5426，确认深层生成文本的可区分性趋于消失。

---
