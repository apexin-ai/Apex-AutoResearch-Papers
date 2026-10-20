# analysis gate wilcoxon test

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gate_wilcoxon_test_20260519T171339_result.json`
- **Structured JSON:** [`5ed15e42c7beda5d9c49.json`](../../sessions/5e/5ed15e42c7beda5d9c49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

### Wilcoxon signed-rank test (28 layers, turn 1 vs turn 21)

| 指标 | 值 |
|------|-----|
| W (one-sided) | 5.0 |
| p (one-sided) | 3.73 × 10⁻⁸ |
| Rank-biserial r | 0.975 (large effect) |
| 方向一致性 | 27/28 layers turn1 < turn21 |

### 分层分析

| Layer group | Mean diff | p-value |
|------------|-----------|---------|
| Bottom (L0–L8) | −0.024 | 0.002 ** |
| Middle (L9–L18) | −0.064 | 0.001 *** |
| Top (L19–L27) | −0.078 | 0.004 ** |

效应从 bottom 到 top 层单调递增（−0.024 → −0.064 → −0.078）。

### Per-conversation consistency
5/5 conversations (100%) 中多数层均满足 turn1 < last_turn。

### 论文用一句话

> Wilcoxon signed-rank test confirmed that gate activation values at turn 1 were significantly lower than at turn 21 across all 28 transformer layers (W=5, p<10⁻⁷, rank-biserial r=0.98), with 27/28 layers exhibiting this pattern consistently across all evaluated conversations.

---
