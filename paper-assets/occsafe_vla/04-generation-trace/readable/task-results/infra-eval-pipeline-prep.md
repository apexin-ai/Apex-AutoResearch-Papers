# infra eval pipeline prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_eval-pipeline-prep_20260526T123430_result.json`
- **Structured JSON:** [`dc0f5318de37a1c0f5c0.json`](../../sessions/dc/dc0f5318de37a1c0f5c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。8 个 eval 命令模板已保存到 memory.md 的 "Eval 命令模板" 段。

关键确认：
- **eval 脚本无 `--use_occ_head` 参数**——自动从 checkpoint 检测，Vanilla 和 OCC 实验用相同命令格式
- **CUDA_VISIBLE_DEVICES 和 MUJOCO_EGL_DEVICE_ID 均匹配训练时的 GPU 编号**
- **checkpoint 路径格式**：`/root/autodl-tmp/checkpoints/{exp_id}/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--{exp_id}--50000_chkpt`（`--50000_chkpt` 目录在训练完成后自动生成）
- 所有 checkpoint 目录已在服务器上存在（目前只有 in-progress 和 10K 中间检查点，50K 最终检查点训练完成后出现）
- 两台服务器的 conda 环境 `occsafe` 和 eval 脚本路径均已验证可用

---
