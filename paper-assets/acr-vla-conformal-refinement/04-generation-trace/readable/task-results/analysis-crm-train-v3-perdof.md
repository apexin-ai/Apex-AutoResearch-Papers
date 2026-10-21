# analysis crm train v3 perdof

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_crm-train-v3-perdof_20260514T182853_result.json`
- **Structured JSON:** [`12ff2ca625bf6a3bed7c.json`](../../sessions/12/12ff2ca625bf6a3bed7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 分析总结

| 指标 | v2 (未归一化) | v3 (归一化) |
|------|-------------|------------|
| val_loss | 0.009 | 1.191 |
| input_mode | full (per-DOF) | full (per-DOF) |
| epochs | - | 50 |

### 结果

1. **训练成功完成**，50 epochs，0.42 GPU-hours
2. **norm_stats 正确加载**（2402 samples）
3. **Best checkpoint**: `/root/autodl-tmp/checkpoints/crm_v3/perdof/crm_best.pt`
4. **无 W&B tracking**

### 需要注意的问题

- **val_loss 不可直接与 v2 对比**：v3 归一化改变了 target scale，loss 绝对值差异 (~1.19 vs 0.009) 是预期内的，不代表模型变差
- **val_loss 在 epoch 50 仍在下降**（1.274 → 1.191，未出现 plateau），可能需要更多 epochs 或更大 lr
- **真正的对比需要下游 evaluation**：在 conformal prediction pipeline 中比较 coverage rate 和 prediction set size，才能判断归一化是否改善了 CRM 效果

---
