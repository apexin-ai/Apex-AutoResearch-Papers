# research track a pmax optimization

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_track-a-pmax-optimization_20260522T073809_result.json`
- **Structured JSON:** [`2863bbc7caf0e840242a.json`](../../sessions/28/2863bbc7caf0e840242a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果总结

**P_max = 0.75 模型**：`P(det|α,T) = 0.75 · Φ(A · α^0.24 · √T − z₀)`

核心发现：

| 指标 | 旧模型 | P_max 模型 |
|------|--------|-----------|
| Train MAE | 0.163 | 0.009 |
| Test MAE (T=5,15) | 0.106 | **0.000** |
| T=25 MAE | 0.219 | **0.031** |
| CI 95% coverage | 6/6 | 6/6 |
| Free params | 4 | 2 |

**β 不可辨识**：Profile likelihood 显示 β ∈ [0.05, 0.70] 均给出相同 NLL（ΔNLL < 2）。原因是 T=10 数据存在 quasi-complete separation（0/8 → 6/8 之间无中间值），导致 A 和 z₀ 趋向无穷，仅比值 z₀/A = 2.66 收敛。因此固定 β=0.24（沿用旧模型），γ=2.08 不变。

**高 α 修正**：旧模型在高 α + 高 T 系统性过预测（如 T=25 α=0.75 预测 0.978 vs 实际 0.75），P_max 模型正确 cap 在 0.75。

**Phase boundary**：α_c(T) = 59.01 · T^(−2.083)，与旧模型同 exponent，系数因 P_max 调整而变小。

---
