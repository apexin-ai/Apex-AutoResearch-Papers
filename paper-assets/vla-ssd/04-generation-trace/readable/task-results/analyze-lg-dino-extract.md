# analyze lg dino extract

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_lg_dino_extract_20260515T175027_result.json`
- **Structured JSON:** [`dd0bd210ea79b8dd53bb.json`](../../sessions/dd/dd0bd210ea79b8dd53bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。结果汇总：

**lg_dino_extract → success**

| 指标 | 值 |
|------|-----|
| Tasks | 10/10 完成 |
| Demos | 50/task, 500 total |
| Total frames | 63,728 |
| Feature dim | 1024 (ViT-L/14) |
| Feature keys | `cls_token`, `patch_mean` |
| dtype | float16 |
| Files | 10 × .h5, 共 234MB |
| Speed | 183 fps, 347s |
| 输出路径 | `/root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/` |

每个 .h5 文件包含 50 条轨迹（traj_0~traj_49），每条轨迹有两种特征表示，维度均为 (frames, 1024)。数据完整，可用于下游 Goal Classification 实验。

---
