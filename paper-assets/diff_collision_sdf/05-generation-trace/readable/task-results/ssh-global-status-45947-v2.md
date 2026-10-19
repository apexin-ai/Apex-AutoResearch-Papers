# ssh global status 45947 v2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_global_status_45947_v2_20260520T094447_result.json`
- **Structured JSON:** [`068dc38d896be0fa539d.json`](../../sessions/06/068dc38d896be0fa539d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | 实验 | PID | Step/30000 | Loss | Speed(s/it) | VRAM | 状态 |
|-----|------|-----|-----------|------|-------------|------|------|
| cuda:0 | a3_gradient_spatial_bowl_s0 | 71494 | 1392/30000 (4.6%) | ~0.22-0.28 | ~3.1-4.1 | 16.9/95.6 GB | ✓ 正常 |
| cuda:1 | a3_gradient_object_pudding_s0 | 73165 | 3817/30000 (12.7%) | ~0.17-0.23 | ~3.2-4.3 | 16.9/95.6 GB | ✓ 正常 |

**磁盘:** /root/autodl-tmp 22G/250G (9%)
**内存:** 67Gi/1.0Ti

**无残留 CPU 幽灵进程。** ps 输出只有两个 tmux training session（PID 71488 spatial_bowl, 73165 object_pudding）及其正常子进程（dataloader workers + torch compile workers）。

两个实验均存活，step 进度符合预期。GPU 1 瞬时利用率显示 0% 是 nvidia-smi 采样瞬间的抖动，进程和日志均确认正在训练。

---
