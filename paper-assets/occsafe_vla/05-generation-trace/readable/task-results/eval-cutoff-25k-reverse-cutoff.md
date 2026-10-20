# eval cutoff 25k reverse cutoff

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cutoff_25k_reverse_cutoff_20260523T203327_result.json`
- **Structured JSON:** [`415222388600de140d78.json`](../../sessions/41/415222388600de140d78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 训练结果

| 实验 | action_loss | occ_loss | steps | GPU hours |
|------|------------|----------|-------|-----------|
| cutoff_25k_s0 | 0.0718 | 0.0106 | 50000 | 15.1h |
| reverse_cutoff_s0 | 0.0481 | 0.0083 | 50000 | 15.1h |

### Checkpoint 路径
- **cutoff_25k_s0**: `/root/autodl-tmp/checkpoints/cutoff_25k_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt`
- **reverse_cutoff_s0**: `/root/autodl-tmp/checkpoints/reverse_cutoff_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt`

### Eval 提交状态
- **cutoff_25k_s0_eval** → westd-34685 cuda:2, PID 479938, RUNNING
- **reverse_cutoff_s0_eval** → westd-34685 cuda:3, RUNNING

两个 registry 已更新为 DONE，两个 eval 已成功提交。

---
