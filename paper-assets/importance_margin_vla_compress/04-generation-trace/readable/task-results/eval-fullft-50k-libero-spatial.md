# eval fullft 50k libero spatial

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_fullft_50k_libero_spatial_20260516T200824_result.json`
- **Structured JSON:** [`90ae56b5e877b53e1d1d.json`](../../sessions/90/90ae56b5e877b53e1d1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。

```
=== Full FT 50K libero_spatial EVAL ===
Overall SR: 34/100 (34%)
95% Wilson CI: [25.5%, 43.7%]

Per-task:
  Task 0: 80% (8/10) -- pick up the black bowl between the plate and the ramekin and place it on the plate
  Task 1: 10% (1/10) -- pick up the black bowl next to the ramekin and place it on the plate
  Task 2: 30% (3/10) -- pick up the black bowl from table center and place it on the plate
  Task 3: 20% (2/10) -- pick up the black bowl on the cookie box and place it on the plate
  Task 4: 20% (2/10) -- pick up the black bowl in the top drawer of the wooden cabinet and place it on the plate
  Task 5: 40% (4/10) -- pick up the black bowl on the ramekin and place it on the plate
  Task 6: 30% (3/10) -- pick up the black bowl next to the cookie box and place it on the plate
  Task 7: 20% (2/10) -- pick up the black bowl on the stove and place it on the plate
  Task 8: 60% (6/10) -- pick up the black bowl next to the plate and place it on the plate
  Task 9: 30% (3/10) -- pick up the black bowl on the wooden cabinet and place it on the plate

Per-task SR: [80, 10, 30, 20, 20, 40, 30, 20, 60, 30]

Comparison: libero_object=33%, libero_spatial=34%
```

libero_spatial (34%) 和 libero_object (33%) 基本持平，均在 30-35% 范围内。

Task 0 和 Task 8 明显较强（80%, 60%），都是 bowl 靠近 plate 的简单空间关系。Task 1 最差（10%），区分 "next to the ramekin" 的空间理解较弱。所有 fail episodes 都 timeout 到 280 steps，没有 crash。

结果已保存到 `eval_results/libero_libero_spatial.json`。

---
