# analysis ckpt6315 variant level recompute

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ckpt6315-variant-level-recompute_20260518T220731_result.json`
- **Structured JSON:** [`0e0a6ae990f41fc5242d.json`](../../sessions/0e/0e0a6ae990f41fc5242d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

### 总结

**ckpt-6315 variant-level: 38/48 = 79.17%**

epoch 1 → epoch 3 的变化：
- Variant accuracy: 81.25% → 79.17% (-2.08pp)
- Variant fail recall: 90.91% → 59.09% (-31.82pp)  
- Variant pass recall: 73.08% → 96.15% (+23.07pp)

epoch 3 per-test accuracy 几乎没变 (82.61% → 82.51%)，但 variant-level 暴露了严重的类别偏移：模型越训越倾向预测 pass，fail 的区分能力大幅退化。ckpt-2105 是更好的 checkpoint。

---
