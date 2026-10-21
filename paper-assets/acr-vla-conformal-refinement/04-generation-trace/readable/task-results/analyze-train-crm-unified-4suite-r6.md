# analyze train crm unified 4suite r6

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_train-crm-unified-4suite-r6_20260523T091143_result.json`
- **Structured JSON:** [`b4038305d25d3ed45109.json`](../../sessions/b4/b4038305d25d3ed45109.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验 train-crm-unified-4suite-r6 分析完成，结论：SUCCESS**

关键结果：
- 50 epoch 全部完成，EXIT_CODE=0
- Val loss 从 0.010801 → **0.005669**（↓47.5%），持续收敛无过拟合
- 最终 epoch 仍在刷新 best val_loss，模型未饱和
- Checkpoint: `/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt` (1.3M)
- 无 W&B，无 per-suite loss breakdown
- 数据量 224,555 samples（long 占 60%，goal 占 27%）

建议下一步：用 crm_best.pt 在 4 个 suite 上分别跑 conformal eval，评估 coverage 和 set size。

报告已写入 artifacts 并注册（art_20260523_bc1272）。

---
