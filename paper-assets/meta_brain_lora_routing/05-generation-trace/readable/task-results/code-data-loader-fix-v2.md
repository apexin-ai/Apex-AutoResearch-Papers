# code data loader fix v2

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_data_loader_fix_v2_20260516T015650_result.json`
- **Structured JSON:** [`cb267b27b112aeeadf32.json`](../../sessions/cb/cb267b27b112aeeadf32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 dry-run 全部通过。汇报：

---

## 结果汇报

### 1. LIBERO demo 数据
- 位置：`/root/autodl-tmp/libero_demos/libero_object_image/`（LeRobot v3.0 parquet 格式）
- 当前：**仅 1 个 parquet shard**（`data/chunk-000/file-096.parquet`），1 episode，152 frames
- meta 记录 454 episodes（10 个 task）。**数据下载不完整，需补全剩余 453 个 episode 的 parquet 文件**

### 2. data_loader.py 改动
`data_loader.py` 已被改写为 D008 版本（21KB，567 行），无需再改。改动摘要：
- 数据路径：从 `rollouts/*.pt` → `DEFAULT_LIBERO_DATA_DIR = /root/autodl-tmp/libero_demos/libero_object_image`
- 读取格式：LeRobot parquet shards（`data/chunk-*/file-*.parquet`）
- `LiberoLeRobotDataset`：解析 parquet schema（images PNG bytes、state list[8]、action list[7]），pad state 8→32 / action 7→32，action chunk horizon=50
- `VisualAugmentation`：camera jitter ±5%、brightness/contrast ±30%、Gaussian noise σ=0.05×severity
- `PhysicalAugmentation`：episode-level offset + per-sample jitter，σ=0.04 rad，只改 state[:8]（joint），不改 gripper
- `SpatialAugmentationPlaceholder`：no-op，warn once
- `build_perturbation_augmenter` / `apply_perturbation`：dispatch 逻辑完整

### 3. Dry-run 结果

| perturbation_type | GPU | step 0 loss | step 1 loss | 状态 |
|---|---|---|---|---|
| visual | cuda:0 | 0.0387 | 0.1150 | **通过** |
| physical | cuda:1 | 0.0375 | 0.1309 | **通过** |
| universal | cuda:2 | 0.0375 | 0.1309 | **通过** |

### 4. 待办
1. **下载完整数据集**：当前仅 1/454 episodes。需用 `huggingface-cli download lerobot/libero_object_image` 补全（或用 LeRobot API）。这是启动正式训练的唯一阻塞项
2. **Spatial 增强**：placeholder no-op（需 LIBERO sim re-render，无法纯 data augmentation 实现）。如需实际 spatial LoRA 训练，需另设方案
3. 之前崩溃的进程跑的是旧版代码（`data_loader.py.bak_d008`），当前代码已修复

---
