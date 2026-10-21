# code check spatial cross inst progress

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_spatial_cross_inst_progress_20260517T091650_result.json`
- **Structured JSON:** [`bda730670644307302f8.json`](../../sessions/bd/bda730670644307302f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

提取和分类全部完成。完整结果表格：

### LIBERO-Spatial Cross-Instruction 10-way Classification (10 classes, chance=0.1)

| Layer | trained_image_mean | trained_last_preaction | untrained_image_mean | untrained_last_preaction |
|-------|-------------------|----------------------|---------------------|------------------------|
| L0    | 0.100             | 0.100                | 0.100               | 0.100                  |
| L1    | 0.100             | **0.989**            | 0.100               | **0.995**              |
| L4    | 0.100             | **1.000**            | 0.100               | 0.862                  |
| L8    | 0.100             | **1.000**            | 0.101               | 0.683                  |
| L12   | 0.100             | **1.000**            | 0.099               | 0.795                  |
| L16   | 0.100             | **1.000**            | 0.100               | 0.765                  |
| L20   | 0.100             | **1.000**            | 0.099               | 0.689                  |
| L24   | 0.100             | **1.000**            | 0.100               | 0.777                  |
| L28   | 0.100             | **1.000**            | 0.100               | 0.760                  |
| L31   | 0.101             | **1.000**            | 0.100               | 0.754                  |

关键发现（数据呈现，遵守 C001 约束，trained + untrained 对照齐全）：

1. **image_mean token**: trained 和 untrained 都在 chance level (~0.1)，所有层均无 goal 信息。这与 LIBERO-Object 结果一致。

2. **last_preaction token**:
   - **Trained**: L1 即达 0.989，L4 起完美 1.000 并保持到 L31
   - **Untrained**: L1 高达 0.995（与 trained 相当），但 L4 开始显著下降至 0.862，L8 降至 0.683，中高层波动在 0.68-0.80 之间
   - **Trained vs Untrained gap**: L4 起 gap 显著（1.000 vs 0.862），L8 gap 最大（1.000 vs 0.683）

3. 模式与 LIBERO-Object 类似：训练使 last_preaction 位置的 goal classification 从不完美提升到完美，但 image_mean 始终不编码 goal 信息。

注意：untrained 中高层有 ConvergenceWarning（lbfgs 2000 iter 未收敛），实际 accuracy 可能略被低估。

---
