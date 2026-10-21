# ops transfer random occ checkpoint

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_transfer_random_occ_checkpoint_20260524T012626_result.json`
- **Structured JSON:** [`deace7891f9e29ddc591.json`](../../sessions/de/deace7891f9e29ddc591.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

传输完成，全部文件一致。

### 结果汇总

| 项目 | 详情 |
|------|------|
| **Checkpoint 目录** | 25 个文件 + 1 个 lora_adapter 子目录，总计 15GB |
| **关键文件** | 4 个 safetensors（14.5GB）、action_head（289MB）、occ_head（2.4MB）、proprio_projector（65MB）、lora_adapter（463MB） |
| **传输方式** | tar 管道：34685 → 本地中转 → 10894 |
| **传输状态** | 成功，文件大小与源完全一致 |
| **10894 磁盘** | 250GB 总量，已用 111GB，剩余 140GB（45% 使用率） |
| **Checkpoint 路径** | `/root/autodl-tmp/checkpoints/ablation_random_occ_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt` |

---
