# debug v7 2 train eval discrepancy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_v7_2-train-eval-discrepancy_20260515T220153_result.json`
- **Structured JSON:** [`8b45806031fd558dc783.json`](../../sessions/8b/8b45806031fd558dc783.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。修复后各 condition 的 action_loss 合理：

| Condition | 修复前（hard） | 修复后（soft） |
|-----------|-------------|-------------|
| eps0.0_pruneFalse | 0.0330 | **0.0108** |
| eps0.0_pruneTrue | ~0.033 | **0.0074** |
| eps0.05_pruneFalse | - | 0.0250 |

---

## 总结

### 根因
`MarginAwareTokenSelector` 的 `training=True` 用 soft sigmoid mask（连续权重），`training=False` 用 hard binary mask（0/1）。evaluate.py 用 `model.eval()` 触发 hard mode，而训练用 soft mode。v7.2 的 margin（0.40）远小于 v7（1.48），导致 soft mask 更模糊，soft→hard 切换影响更大。

### 额外 bug
`IMMSmolVLAWrapper.__init__` 中 `selector_temperature` 默认 1.0，而 config 的 temperature 是 0.5。selector 比 margin loss 更 soft。

### 已修复
1. **`imm/smolvla_wrapper.py` 第96行**：`selector_temperature` 默认值改为读取 config 的 `temperature`
2. **`evaluate.py` 第351-356行**：action_loss 计算改用 train mode（soft forward）以匹配训练语义

### 后续建议（未实施）
- 考虑训练时用 Straight-Through Estimator (STE)：forward 用 hard mask，backward 用 soft gradient。彻底消除 train/eval 差异
- 或在训练中定期报告 hard action_loss 作为监控指标，避免 soft loss 误导

---
