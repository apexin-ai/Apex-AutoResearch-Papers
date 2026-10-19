# ops lora baseline launch prep

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_lora_baseline_launch_prep_20260524T061044_result.json`
- **Structured JSON:** [`f20bf304b020d21f4aa6.json`](../../sessions/f2/f20bf304b020d21f4aa6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清单已写入 `artifacts/lora_baseline_launch_checklist.md`。

**总结：**
- 脚本已在 westd-45947 上，版本一致，两个 bug fix 均已包含
- 磁盘 75GB 可用，充足
- 两个 seed 的启动命令已准备好（cuda:0 / cuda:1）
- **2 个需要注意的事项：**
  1. **等 s0_l005/s0_l01 完成释放 GPU 后再启动**
  2. **seed0 启动前须删除 dry-run 残留目录**（`rm -rf /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed0/`），否则 `overwrite=False` 会报错

---
