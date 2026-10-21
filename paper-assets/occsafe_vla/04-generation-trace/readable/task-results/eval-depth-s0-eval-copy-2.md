# eval depth s0 eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_depth_s0_eval_20260523T002819_result.json`
- **Structured JSON:** [`c5a398a49868d53231c5.json`](../../sessions/c5/c5a398a49868d53231c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**depth_s0 的 50r eval 已经在 cuda:1 上运行了。** 已有进程 PID 189393，启动于 08:24：

```
CUDA_VISIBLE_DEVICES=1 python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/depth_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \
  --num_rollouts 50 --seed 42
```

我刚启动的进程（PID 206937）已退出，大概率是因为 cuda:1 已被上述进程占用导致 OOM。

**汇总：**
- Checkpoint: `/root/autodl-tmp/checkpoints/depth_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt`
- 已有 eval 进程 PID: **189393**（cuda:1，50 rollouts，运行中）
- 日志: `~/runs/occsafe_vla/depth_s0_eval.log`

不需要重复启动。

---
