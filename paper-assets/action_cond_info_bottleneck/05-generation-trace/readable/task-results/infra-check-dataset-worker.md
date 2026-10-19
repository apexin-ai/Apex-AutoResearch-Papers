# infra check dataset worker

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-dataset-worker_20260515T210832_result.json`
- **Structured JSON:** [`ffbe39e9621296a46604.json`](../../sessions/ff/ffbe39e9621296a46604.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 数据集状态：完成

**`/root/autodl-tmp/libero_dataset/`**：
- 1.9GB，377 个 parquet 文件 (file-000 ~ file-376)
- 1693 episodes, 273,465 frames, 40 tasks
- 视频 1.8GB（两个相机视角 `observation.images.image` / `image2`）

**HF cache**：
- `datasets--lerobot--libero/refs/main` 指向 commit `1595a93b`（仅 ref，无 snapshot blobs）
- `datasets/parquet/` 缓存 1.1GB（8 个子目录，已转换的 parquet 缓存）

### LeRobotDataset 加载验证：通过

| 方式 | 结果 |
|------|------|
| `LeRobotDataset('lerobot/libero', root='/root/autodl-tmp/libero_dataset')` | 273,465 frames |
| `LeRobotDataset('lerobot/libero')` （无 root） | 273,465 frames |

两种方式都能正常加载。返回 keys: `observation.images.image`, `observation.images.image2`, `observation.state`, `action`, `timestamp`, `frame_index`, `episode_index`, `index`, `task_index`, `task`。

### 当前运行的进程
- `lerobot-eval` baseline_std_v3 (libero_spatial, 50 episodes) — PID 109428
- `lerobot-eval` baseline_plus_v2 (libero_spatial, 50 episodes) — PID 109501
- 无下载进程

---
