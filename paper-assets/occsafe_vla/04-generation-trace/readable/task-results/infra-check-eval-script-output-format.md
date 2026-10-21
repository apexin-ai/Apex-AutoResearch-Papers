# infra check eval script output format

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check_eval_script_output_format_20260521T015151_result.json`
- **Structured JSON:** [`b14f8be1723808869e16.json`](../../sessions/b1/b14f8be1723808869e16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已拿到全部所需信息。

## 汇报

### eval 命令完整内容

```bash
CUDA_VISIBLE_DEVICES=${gpu_id} MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=${gpu_id} python vla-scripts/evaluate_safelibero.py \
    --model_family openvla \
    --pretrained_checkpoint "${latest_ckpt}" \
    --task_suite_name libero_spatial \
    --num_steps_wait 10 \
    --num_rollouts 20 \
    --center_crop True \
    --use_l1_regression True \
    --num_images_in_input 2 \
    --use_proprio True \
    --output_path "${EVAL_DIR}/${tag}_final.json"
```

### num_rollouts = **20** ✓

### per-task breakdown: **有** ✓

从 westd-10894 上的 `vanilla_s0_final.json` 确认，输出 JSON 结构：

```
{
  "config": { checkpoint, task_suite, num_rollouts, collision_threshold, seed },
  "tasks": {
    "&lt;task_name>": {
      "task_id": int,
      "n": 20,
      "successes": int,
      "safe": int,
      "tsr": float,
      "car": float,
      "obstacles": [...],
      "episodes": [ { ep, success, collision, max_disp, coll_step, trajectory_length }, ... ]
    },
    ...  // 10 tasks total
  },
  "all_episodes": [ { task_id, task_name, episode_idx, max_displacement, collision_detected, trajectory_length, task_success }, ... ],
  "summary": { total_episodes: 200, tsr, car, total_collisions, displacement_stats }
}
```

`tasks` 字典包含每个 task 的 TSR/CAR breakdown，`--output_path` 已指定为 `${EVAL_DIR}/${tag}_final.json`（即 `/root/occsafe_vla/eval_results/occ_s0_final.json` 等）。

**无需修改，脚本已正确配置 per-task breakdown 输出。**

---
