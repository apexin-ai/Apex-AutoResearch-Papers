# code r11 7b8b position residualization

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r11_7b8b_position_residualization_20260518T120530_result.json`
- **Structured JSON:** [`d4ab4262891b34f17a68.json`](../../sessions/d4/d4ab4262891b34f17a68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results complete. Here's the summary:

```
=== R1-8B (L14, W=3, n_test=43) ===
Original HS BA:        0.813
Residualized HS BA:    0.571 (drop: 24.3pp)
Residualized HS p-val: <0.000001 (binomial), 0.000007 (Wilcoxon)
Position-only BA:      0.706
Original Text BA:      0.652
Residualized Text BA:  0.534

=== OT-7B (L16, W=3, n_test=47) ===
Original HS BA:        0.732
Residualized HS BA:    0.609 (drop: 12.3pp)
Residualized HS p-val: <0.000001 (binomial), <0.000001 (Wilcoxon)
Position-only BA:      0.736
Original Text BA:      0.593
Residualized Text BA:  0.540

=== Cross-model comparison ===
| Model         | Orig BA | Resid BA | Drop   | Resid p  | Pos-only |
|---------------|---------|----------|--------|----------|----------|
| R1-8B         | 0.813   | 0.571    | 24.3pp | <0.0001  | 0.706    |
| OT-7B         | 0.732   | 0.609    | 12.3pp | <0.0001  | 0.736    |
| QwQ-32B (ref) | 0.735   | 0.612    | 12.3pp | 0.0024   | 0.519    |
```

**Key findings** (counter to initial hypothesis):

1. **Both 7-8B models have high position-only BA** (0.706, 0.736) vs QwQ-32B's 0.519. Position is much more informative for smaller models.

2. **R1-8B shows the largest drop** (24.3pp) after residualization, suggesting its HS signal is heavily position-mediated. However, residualized BA (0.571) is still significantly above chance (p < 0.001).

3. **OT-7B's position-only BA (0.736) actually exceeds its original HS BA (0.732)**, indicating the probe largely learns position. Residualized BA (0.609) still above chance.

4. **Text probes**: Both models' text probes drop to near-chance after residualization (0.534, 0.540), confirming text content is more position-confounded than HS.

The initial hypothesis that 7-8B models have "position-independent" HS advantage (contrasting with QwQ's "position-mediated") is **not supported**. Instead, position plays an even larger role in smaller models, though a significant residual HS signal persists above chance in both.

---
