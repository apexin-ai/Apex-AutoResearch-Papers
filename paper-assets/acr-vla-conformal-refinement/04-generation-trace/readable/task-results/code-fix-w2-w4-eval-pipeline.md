# code fix w2 w4 eval pipeline

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-w2-w4-eval-pipeline_20260514T074040_result.json`
- **Structured JSON:** [`4d1e55404f9b1ed2e1bd.json`](../../sessions/4d/4d1e55404f9b1ed2e1bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改完成，import 验证通过。总结：

**Fix W2 — argmin-selected base action（3 个文件）：**
- `crm.py`: `mean_action` 参数重命名为 `base_action`，残差连接 `base_action + delta`
- `evaluate.py:178-184`: `select_action_crm` 用 argmin Euclidean 距离选取最近 mean 的 sample 作为 base，替代原来的 `K_samples.mean(dim=0)`
- `train_crm.py:285-292`: 新增 `_argmin_base_action()` 辅助函数；训练循环（行401）和验证循环（行447）均用 argmin base 替代 mean
- gripper 处理不变（仍为 mean-aggregated）

**Fix W4 — delta L2 norm clipping（crm.py）：**
- `__init__` 新增 `max_correction_norm` 参数，默认 1.42（训练数据 argmin delta 的 combined p95）
- `forward` 中 `delta = self.net(x)` 后加 L2 clipping：`delta * clamp(max_norm / (norm + eps), max=1.0)`
- 可通过构造函数或命令行传参调优

---
