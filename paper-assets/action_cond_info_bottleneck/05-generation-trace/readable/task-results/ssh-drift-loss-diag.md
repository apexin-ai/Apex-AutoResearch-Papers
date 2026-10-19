# ssh drift loss diag

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_drift-loss-diag_20260517T160000_result.json`
- **Structured JSON:** [`4b38d61948c38a699ace.json`](../../sessions/4b/4b38d61948c38a699ace.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到正确基线了。本地 safetensors 不是训练时加载的模型（差异 296.6），v7.1 scorer_only 的 connector 权重才是真正的原始参考（因为 scorer_only 模式下 connector 冻结）。

## 结果

**v7.2 训练中 drift_loss 的实际量级：**

| Step  | drift_loss (sum_sq) | λ * drift (λ=0.1) |
|-------|--------------------|--------------------|
| 5000  | 0.1052             | 0.0105             |
| 10000 | 0.0918             | 0.0092             |
| 15000 | 0.0843             | 0.0084             |
| 20000 | 0.0836             | 0.0084             |

**判断：**

1. **drift_loss 量级很小**：~0.08-0.1，对应 connector 权重 L2 偏移约 0.29-0.32（原始 norm ~71.8，相对偏移 ~0.4%）
2. **λ=0.1 的约束力非常有效**：drift_loss 从 step 5k 的 0.105 单调下降到 step 20k 的 0.084，且 λ*drift 项仅约 0.008-0.01，远小于 task_loss（~0.1）和 contrastive loss（~1.5-2.0）
3. **connector 本质上被冻结**：inter-checkpoint drift 也在递减（5k→10k: 0.041, 15k→20k: 0.001），connector 在训练后期几乎不再变化
4. **drift penalty 占比极低**：λ*drift ≈ 0.008，仅占 total loss（~0.28）的约 3%

结论：λ=0.1 的 drift 约束有效但偏保守，connector 实际几乎没有移动。如果需要 connector 有更多适应空间，可以降低 λ_drift（如 0.01 或 0.001）。

---
