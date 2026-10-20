# analysis depth s2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_depth_s2_20260522T215237_result.json`
- **Structured JSON:** [`83e01e673c1dc955afbe.json`](../../sessions/83/83e01e673c1dc955afbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## depth_s2 训练结果总结

| 项目 | 值 |
|------|-----|
| **状态** | 训练成功完成 (EXIT_CODE=0) |
| **总步数** | 50005 |
| **训练时长** | ~14h48m |
| **初始 loss** | depth=0.6042, action=0.5820 |
| **最终 loss** | depth=0.0468, action=0.0498, occ=0.0000 |
| **Checkpoint** | `/root/autodl-tmp/checkpoints/depth_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt` (~15GB, 完整) |
| **保存的 checkpoint** | 10k/20k/30k/40k/50k（仅 50k 留存） |

Checkpoint 包含完整模型文件：4 safetensors shards + action_head + depth_head + proprio_projector + lora_adapter + dataset_statistics。

depth_s2 的 cuda:2 已释放，可用于 eval 或其他任务。depth_s0/s1 在 westd-34685 上状态仍为 RUNNING（之前因磁盘满失败后重启），需要单独检查。

---
