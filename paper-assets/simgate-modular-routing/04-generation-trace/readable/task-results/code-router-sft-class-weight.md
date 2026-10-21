# code router sft class weight

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_router-sft-class-weight_20260513T200820_result.json`
- **Structured JSON:** [`18f04941f250f3f2c6ea.json`](../../sessions/18/18f04941f250f3f2c6ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改摘要：

**新增参数**（向后兼容，所有默认值保持原行为）：
- `--class_weights`: `"auto"`（inverse frequency: `N_total / (num_classes * N_c)`）或手动 `"w0,w1"`，传入 `CrossEntropyLoss(weight=...)`
- `--min_internal_samples 10`: internal 样本低于阈值时打印 WARNING
- `--upsample_minority`: 启用 `WeightedRandomSampler`（per-sample weight = `1/class_count`）

**新增组件**：
- `compute_class_weights()` — 计算 class weights
- `WeightedCETrainer(Trainer)` — 自定义 Trainer，重写 `compute_loss`（加权 CE）和 `get_train_dataloader`（可选 sampler）
- W&B 日志中记录 `class_weights_values`、`train_label_counts`、`upsample_minority`

---
