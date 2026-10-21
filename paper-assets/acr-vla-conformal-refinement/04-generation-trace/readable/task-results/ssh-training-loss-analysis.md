# ssh training loss analysis

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_training-loss-analysis_20260517T011458_result.json`
- **Structured JSON:** [`4081e1074948da0952c0.json`](../../sessions/40/4081e1074948da0952c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析已写入 `artifacts/training_loss_analysis.md`。

核心发现与任务预期的"disconnect"假设相反：**训练 MSE 和闭环 SR 是正相关的**（低 MSE → 高 SR），排序完全一致。真正的 insight 不是"离线指标预测失败"，而是：

1. **obs_only 在两个指标上都最优**（val MSE=0.0165, Object SR=19%）
2. **conformal features 同时伤害了训练和部署**（perdof val MSE 2.2x worse, Object SR -8pp）
3. 论文叙事应聚焦"observation-conditioned correction is sufficient; conformal features are an honest negative result"

---
