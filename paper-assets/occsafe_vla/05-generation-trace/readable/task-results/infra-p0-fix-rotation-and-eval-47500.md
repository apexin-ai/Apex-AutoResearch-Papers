# infra P0 fix rotation and eval 47500

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_P0-fix-rotation-and-eval-47500_20260521T070226_result.json`
- **Structured JSON:** [`7460015c6a8daf8faeec.json`](../../sessions/74/7460015c6a8daf8faeec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个紧急任务全部完成。

---

### 紧急 1 结果
- **17500_chkpt**: 安全，未被删除
- **S1 训练**: PID 80898 正常运行
- **新 rotation**: PID 88572，已确认 17500_chkpt 标记为 PROTECTED
- 旧 rotation (PID 71055) 已 kill

### 紧急 2 结果
- **47500_chkpt**: s0 和 s2 均完整（4 shards + action_head + occ_head + proprio_projector）
- **S0 eval**: PID 89038，GPU 0，已在执行 rollout（进度 35% T0）
- **S2 eval**: PID 92050，GPU 2，已开始执行
- 参数从 `monitor_and_eval_occ.sh` 获取：`--model_family openvla --pretrained_checkpoint --num_steps_wait 10 --num_rollouts 20 --center_crop True --use_l1_regression True --num_images_in_input 2 --use_proprio True`
- 结果将保存到：`/root/occsafe_vla/eval_results/occ_s0_final.json` 和 `occ_s2_final.json`

---
