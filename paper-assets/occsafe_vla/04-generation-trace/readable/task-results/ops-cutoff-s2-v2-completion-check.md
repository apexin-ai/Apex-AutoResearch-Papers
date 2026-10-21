# ops cutoff s2 v2 completion check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cutoff_s2_v2_completion_check_20260524T044527_result.json`
- **Structured JSON:** [`9f12b2dac1ff916c9835.json`](../../sessions/9f/9f12b2dac1ff916c9835.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**训练结果**: cutoff_s2_v2 **成功完成** (50005/50005 steps)
- 最终指标: occ_loss=0.0137, action_loss=0.0605
- Checkpoint: `/root/autodl-tmp/checkpoints/cutoff_s2_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt`

**GPU 0 状态**: 空闲 → 已用于提交 eval

**Eval 已提交**: `cutoff_s2_v2_eval` (PID 520308)
- westd-10894 GPU 0, 50 rollouts, seed 42
- 日志: `~/runs/occsafe_vla/cutoff_s2_v2_eval.log`
- 预计 ~50-60 分钟完成

---
