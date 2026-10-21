# research libero dataset v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_libero-dataset-v2_20260515T125532_result.json`
- **Structured JSON:** [`e6c567c210c4f0487a2d.json`](../../sessions/e6/e6c567c210c4f0487a2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. LIBERO-Object 数据集 ID

`lerobot/libero_object_no_noops` **不存在**。

在 HF Hub 上找到的 LIBERO 数据集：

| 数据集 ID | 格式 | Episodes | Tasks | 说明 |
|-----------|------|----------|-------|------|
| `lerobot/libero` | v3.0 | 1693 | 40 | **全部 4 个 LIBERO suite 合并** |
| `lerobot/libero_10` | v3.0 | ~400 | 10 | 仅前 10 个任务 (LIBERO-Long) |

`lerobot/libero` 的 40 个任务按 task_index 分布：
- **0-9**: LIBERO-Long（长程多步任务）
- **10-19**: LIBERO-Spatial（空间推理）
- **20-29**: LIBERO-Object（不同物体，相同动作 — "pick up X and place it in the basket"）
- **30-39**: LIBERO-Goal（相同物体，不同初始位置）

lerobot 0.5.1 使用 v3.0 格式，完全兼容。LeRobotDatasetMetadata 加载验证通过。

### 2. 配置建议

将 dataset ID 改为 `lerobot/libero`，训练时通过 `task_index` 20-29 过滤 LIBERO-Object 子集。

Features：2 个摄像头图像 (256×256 video)，8D state，7D action，10 FPS。

### 3. MVP 数据集推荐

- **快速验证**：`lerobot/libero_10`（更小，下载快）
- **完整实验**：`lerobot/libero`（过滤 task_index 20-29 得到 LIBERO-Object）
- **备选 aloha**：`lerobot/aloha_sim_transfer_cube_scripted` 或 `lerobot/aloha_sim_insertion_scripted`（不同机器人形态，但更简单、下载更快）

---
