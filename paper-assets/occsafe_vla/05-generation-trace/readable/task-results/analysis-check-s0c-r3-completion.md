# analysis check s0c r3 completion

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check_s0c_r3_completion_20260527T225003_result.json`
- **Structured JSON:** [`3672bfb439868e3b2604.json`](../../sessions/36/3672bfb439868e3b2604.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**判断：SUCCESS** — 训练成功完成。

关键证据：
- 日志最后显示 `Max step 50005 reached! Stopping training...`
- step 50000 指标：`occ_loss=0.0092, depth_loss=0.0000, action_loss=0.0454`
- 50000_chkpt 已保存并完成 merge，包含完整模型文件（4个 safetensors 分片 + action_head + occ_head + proprio_projector + lora_adapter）
- 总训练时间约 14h5m，速度 ~1.08 it/s

**Checkpoint 目录**（3个保留）：
- `...--30000_chkpt`
- `...--40000_chkpt`
- `...--50000_chkpt`

**最终 checkpoint 路径**：
```
/root/autodl-tmp/checkpoints/detach_ln_v2_s0c_r3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s0c_r3--50000_chkpt
```

---
