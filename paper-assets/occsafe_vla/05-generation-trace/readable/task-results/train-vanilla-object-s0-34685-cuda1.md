# train vanilla object s0 34685 cuda1

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_vanilla_object_s0_34685_cuda1_20260527T164502_result.json`
- **Structured JSON:** [`f1cf5c406be39c1ecadc.json`](../../sessions/f1/f1cf5c406be39c1ecadc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动并开始迭代：

- **数据集**: libero_object_no_noops（454 episodes）
- **进度**: step 3/50005，正常运行中
- **action_loss**: 0.5938（初始值合理）
- **occ_loss/depth_loss**: 0.0（Vanilla 模式，符合预期）
- **速度**: ~2s/step，预计约 28 小时完成（在 deadline 前可跑到 ~43k steps，接近 50k）
- **GPU**: westd-34685 cuda:1
- **日志**: `~/runs/occsafe_vla/vanilla_object_s0.log`

---
