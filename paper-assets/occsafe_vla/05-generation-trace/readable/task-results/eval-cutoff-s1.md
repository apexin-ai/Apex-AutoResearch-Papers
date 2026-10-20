# eval cutoff s1

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cutoff_s1_20260523T001725_result.json`
- **Structured JSON:** [`964791cf8a8ba9e03d4f.json`](../../sessions/96/964791cf8a8ba9e03d4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型加载成功，eval 已开始运行。

**状态汇总：**
- **Checkpoint**: `/root/autodl-tmp/checkpoints/cutoff_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt`
- **训练日志**: 50005 steps 正常完成，EXIT_CODE=0，最终 occ_loss=0.0129, action_loss=0.0547
- **Eval**: 已在 tmux session `cutoff_s1_eval` 中启动，cuda:3，10 tasks × 50 rollouts，当前 Task 0 进行中
- **日志**: `/root/runs/occsafe_vla/cutoff_s1_eval.log`
- **脚本**: `vla-scripts/evaluate_safelibero.py`（正确版本）
- **预计耗时**: 2-3 小时

---
