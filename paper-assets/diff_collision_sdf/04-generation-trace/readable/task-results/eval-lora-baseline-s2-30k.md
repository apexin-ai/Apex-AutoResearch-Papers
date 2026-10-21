# eval lora baseline s2 30k

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_lora_baseline_s2_30k_20260527T133956_result.json`
- **Structured JSON:** [`e78e40cc25fa632bbcf0.json`](../../sessions/e7/e78e40cc25fa632bbcf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

**Step 1 - 训练验证** ✓
- `train_pi05_lora_baseline_s2_resume` 训练完成，step 30000/30000, EXIT_CODE=0
- Checkpoint: `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed2/30000/` (model.safetensors 7.5GB)
- Final loss=0.0117, 训练时间 10.3h

**Step 2 - Registry 更新** ✓
- status=DONE, conclusion=success, checkpoint_path + metrics 已记录

**Step 3 - Eval 已启动** ✓
- `eval_lora_baseline_30k_s2` 在 westd-45947 cuda:0 运行，PID=512147
- 日志正在产出，模型加载中（LoRA injection 阶段）
- 日志路径: `~/runs/diff_collision_sdf/eval_lora_baseline_30k_s2.log`

---
