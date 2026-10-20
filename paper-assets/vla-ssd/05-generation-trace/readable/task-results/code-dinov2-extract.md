# code dinov2 extract

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dinov2-extract_20260515T065320_result.json`
- **Structured JSON:** [`3a6cbd0d4c621fb4273b.json`](../../sessions/3a/3a6cbd0d4c621fb4273b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，结果汇总：

## 产出

### 1. LIBERO-10 HDF5 数据结构
- 10 个 HDF5 文件，每个对应一个 task
- 每个文件 50 个 demo (`data/demo_0` ~ `data/demo_49`)
- Image key: `data/demo_{i}/obs/agentview_rgb` — (T, 128, 128, 3) uint8
- 也有 `eye_in_hand_rgb`（腕部相机，同尺寸）
- 每条 demo ~220-280 timesteps，总计 138,090 帧

### 2. 脚本
`/root/vla-ssd/scripts/extract_dinov2.py` — 107 行

### 3. 提取结果
- 10 个特征文件，总计 503MB，位于 `/root/autodl-tmp/vla-ssd/features/dinov2/`
- 每个文件包含 50 条 trajectory
- 每条 trajectory: `cls_token` (T, 1024) fp16 + `patch_mean` (T, 1024) fp16
- 验证通过：shape、dtype 均正确

### 4. 性能
- 138,090 帧，795.8s，平均 174 fps
- GPU 显存 ~2.5GB（DINO-V2 ViT-L）
- batch_size=32，GPU 利用率 ~78%

### 5. 注意事项
- 需要 `HDF5_USE_FILE_LOCKING=FALSE` 环境变量（AutoDL 数据盘不支持 HDF5 file locking）
- 已直接全量运行完成，无需再通过 `submit_training_job` 提交

---
