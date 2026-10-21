# ssh submit a1 object pudding s0

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_submit_a1_object_pudding_s0_20260520T144435_result.json`
- **Structured JSON:** [`a1efb452dabf8c9a9a67.json`](../../sessions/a1/a1efb452dabf8c9a9a67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动并在 GPU 1 上运行。

**状态汇总：**
- **exp_id**: a1_sdf_object_pudding_s0
- **GPU**: cuda:1 (bus 5A:00.0), 13376 MiB 显存占用
- **PID**: 227389
- **tmux**: `a1_sdf_object_pudding_s0`
- **进度**: step 4/30000, loss ~0.22, ~4.7s/it
- **日志**: `~/runs/diff_collision_sdf/a1_sdf_object_pudding_s0.log`

注意：脚本内部 `os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)`（第284行）会覆盖外部环境变量，所以必须用 `--gpu 1` 而非 `CUDA_VISIBLE_DEVICES=1 --gpu 0`。

---
