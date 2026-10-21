# analysis check full occ ln s4 completion

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check_full_occ_ln_s4_completion_20260527T231904_result.json`
- **Structured JSON:** [`236ba8ee535ad4ce2f51.json`](../../sessions/23/236ba8ee535ad4ce2f51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在（可能已被清除或在另一个 session 中创建），无影响。

## 结果

| 项目 | 状态 |
|------|------|
| 判断 | **SUCCESS** |
| 日志结束信息 | `Max step 50005 reached! Stopping training...` |
| 最终 step | 50000 (occ_loss=0.0118, action_loss=0.0552) |
| 训练总时长 | ~14h 4min |
| Checkpoint 路径 | `/root/autodl-tmp/checkpoints/full_occ_ln_s4/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_s4--50000_chkpt` |
| Checkpoint 内容 | 4x safetensors + action_head + occ_head + proprio_projector + lora_adapter + tokenizer（完整） |
| Registry | 已更新为 ANALYZING |

可以启动 eval。需要我现在启动吗？

---
