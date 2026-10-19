# ops extract comp loss curves

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_extract-comp-loss-curves_20260518T115453_result.json`
- **Structured JSON:** [`f8f0a532c3f144208da7.json`](../../sessions/f8/f8f0a532c3f144208da7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 CSV 已保存。汇总：

| 训练 | Initial Loss | Final Loss | 下降比 | Plateau? |
|------|-------------|------------|--------|----------|
| comp_30pct_s42 | 2.3594 | 0.6992 | 70.4% | Yes (900→1000 微升 0.6953→0.6992) |
| comp_30pct_s123 | 2.0469 | 0.7617 | 62.8% | No (700 处 0.6875 后反弹至 0.7617，过拟合迹象) |
| comp_30pct_s456 | 2.0938 | 0.6797 | 67.5% | Yes (800→1000 在 0.72-0.76 间波动) |
| comp_50pct_s42 | 3.4375 | 1.0703 | 68.9% | Yes (900→1000 微升 1.0625→1.0703) |

关键观察：
- 30% 三个 seed 的 final loss 范围 0.68-0.76，s123 在 step 700 后出现反弹（best loss 0.6875 在 step 700）
- 50% 的 initial loss 显著更高（3.44 vs ~2.1-2.4），final loss 也更高（1.07 vs ~0.70），符合更高稀疏率补偿更困难的预期
- 所有训练均在 step 700-900 区间收敛/plateau

---
