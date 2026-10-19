# diag gpu utilization check

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu_utilization_check_20260515T222621_result.json`
- **Structured JSON:** [`c5d6abafee13f6b3b158.json`](../../sessions/c5/c5d6abafee13f6b3b158.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. 进程存活状态

| PID | 进程 | 状态 | 运行时间 | RSS |
|-----|------|------|----------|-----|
| 294229 | baseline_plus | **ALIVE** (Rl) | 1h05m | 15.4GB |
| 308788 | baseline_std | **ALIVE** (Rl) | 56m | 15.4GB |

### 2. nvidia-smi

| GPU | 利用率 | 显存占用 | 总显存 |
|-----|--------|---------|--------|
| 0 | 1% | 3112 MiB | 97887 MiB |
| 1 | 0% | 3591 MiB | 97887 MiB |

**GPU 利用率低是正常的** — robosuite simulation 是 CPU-bound，模型推理只占 rollout 每步的极小比例。

### 3. Eval 进度

| 进程 | 已完成 suite | 当前 suite | 剩余 |
|------|-------------|-----------|------|
| baseline_plus | libero_spatial (**81.6%** success) | libero_object (rollout中) | libero_goal, libero_10 |
| baseline_std | libero_spatial (**66.0%** success) | libero_object (rollout中) | libero_goal, libero_10 |

每个 suite = 10 tasks × 50 episodes。当前均在 libero_object 执行 rollout，进度条显示单 episode 步数 ~50%。

### 4. ACIB v3 Dry-Run — 失败

数据加载成功（273465 frames），`--data_root` argparse 修复有效。**前向传播报错：image feature key mismatch。**

```
ValueError: All image features are missing from the batch.
  batch keys:    observation.images.image, observation.images.image2
  model expects: observation.images.camera1, observation.images.camera2, observation.images.camera3
```

**根因**：数据集用 `image/image2` 命名，但 pretrained SmolVLA 模型的 config 中 image_features 注册的是 `camera1/camera2/camera3`。需要在训练脚本中添加 key 重映射，或修改数据集 metadata 使 key 匹配模型定义。

附带发现：首次 dry-run 卡住是因为 `LeRobotDataset` 初始化时默认联网校验 HF Hub metadata（2+ min 无响应），加 `HF_HUB_OFFLINE=1` 后正常。训练脚本应默认设置此环境变量。

---
